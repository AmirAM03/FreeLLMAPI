#!/usr/bin/env python3
"""FreeLLMAPI — generate provider pages + README comparison table.

Reads  data/providers.json
Writes providers/<id>.md for every provider
Injects the auto-generated comparison table into README.md
between the <!-- BEGIN:AUTO:TABLE --> ... <!-- END:AUTO:TABLE --> markers.

Usage:
    python scripts/build.py            # build everything
    python scripts/build.py --check    # exit 1 if generated files are stale
"""

import json
import argparse
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "providers.json"
PROVIDERS_DIR = ROOT / "providers"
README = ROOT / "README.md"
TABLE_START = "<!-- BEGIN:AUTO:TABLE -->"
TABLE_END = "<!-- END:AUTO:TABLE -->"

CATEGORY_DOTS = {
    "hosted-inference": "🔵",
    "model-router": "🟣",
    "cloud-platform": "🟠",
    "edge-serverless": "🟢",
    "other": "⚪",
}

STATUS_BADGES = {
    "verified": "🟢 Verified",
    "unverified": "🟡 Unverified",
    "deprecated": "🟠 Deprecated",
    "dead": "🔴 Dead",
}


def load_providers():
    with DATA.open(encoding="utf-8") as f:
        return json.load(f)


def slug_link(provider):
    return f"providers/{provider['id']}.md"


def clip(text, limit=60):
    """Trim text to a word boundary with an ellipsis."""
    if len(text) <= limit:
        return text
    trimmed = text[: limit - 1].rsplit(" ", 1)[0]
    return trimmed + "…"


def render_table(data):
    """Generate the README comparison table from all providers."""
    lines = [
        f"| Provider | Category | OpenAI-compat | Auth | Free tier | Status | Page |",
        f"|---|---|---|---|---|---|---|",
    ]
    for p in sorted(data["providers"], key=lambda x: x["name"].lower()):
        dot = CATEGORY_DOTS.get(p["category"], "⚪")
        cat = f"{dot} {p.get('category_label', p['category'].replace('-', ' ').title())}"
        compat = "✔" if p["openai_compatible"] else "✖"
        auth = "`" + p["auth"] + "`"
        free = clip(p["free_tier"].split("—")[0].split(".")[0].strip())
        status = STATUS_BADGES.get(p["status"], p["status"])
        lines.append(
            f"| **[{p['name']}]({slug_link(p)})** | {cat} | {compat} | {auth} | {free} | {status} | [`→`]({slug_link(p)}) |"
        )
    return "\n".join(lines)


def render_page(p):
    """Generate a full provider page (providers/<id>.md)."""
    dot = CATEGORY_DOTS.get(p["category"], "⚪")
    compat = "✔" if p["openai_compatible"] else "✖"
    status = STATUS_BADGES.get(p["status"], p["status"])

    model_rows = "\n".join(
        f"| `{m['id']}` | {int(m['context']):,} | {m.get('notes', '')} |"
        if str(m["context"]).isdigit()
        else f"| `{m['id']}` | {m['context']} | {m.get('notes', '')} |"
        for m in p["models"]
    )
    highlights = "\n".join(f"- {h}" for h in p["highlights"])

    return f"""---
name: {p['name']}
id: {p['id']}
category: {p['category']}
api_base: {p['api_base']}
openai_compatible: {str(p['openai_compatible']).lower()}
auth: {p['auth']}
docs: {p['docs']}
website: {p['website']}
signup: {p['signup']}
last_verified: {p['last_verified']}
---

# {p['name']}

> {dot} **{p.get('category_label', p['category'])}** · **OpenAI-compatible:** {compat} · **Status:** {status}

[![Docs](https://img.shields.io/badge/Docs-Documentation-blue)]({p['docs']})
[![Sign up](https://img.shields.io/badge/Sign%20up-Free-brightgreen)]({p['signup']})

**API Base:** `{p['api_base']}`

## 🔑 Getting Access
1. Sign up at [{p['name']}]({p['signup']}) — no credit card required.
2. Generate an API key from the dashboard.
3. **Free tier:** {p['free_tier']}

## 🌐 Endpoints
| Endpoint | Notes |
|---|---|
| `{p['api_base']}` | {'OpenAI-compatible (`/chat/completions`, `/models`)' if p['openai_compatible'] else 'Provider-specific API — see docs'} |

## 🧠 Models
| Model ID | Context | Notes |
|---|---|---|
{model_rows}

## ⏱️ Free Tier Limits
{p['rate_limits']}

## ✨ Highlights
{highlights}

## 📋 Example Request
```bash
curl {p['api_base']}/chat/completions \\
  -H "Authorization: Bearer $KEY" \\
  -H "Content-Type: application/json" \\
  -d '{{"model": "{p['models'][0]['id'] if p['models'] else 'model-id'}", "messages": [{{"role": "user", "content": "Hello!"}}]}}'
```

---
*Auto-generated from [`data/providers.json`](../data/providers.json) — last verified {p['last_verified']}.
Found something wrong? [Open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose).*
"""


def inject_table(readme_text, table):
    """Replace the marked section in README with the fresh table."""
    if TABLE_START not in readme_text or TABLE_END not in readme_text:
        sys.exit(f"ERROR: markers not found in {README} — need {TABLE_START} / {TABLE_END}")
    head, rest = readme_text.split(TABLE_START, 1)
    _, tail = rest.split(TABLE_END, 1)
    return f"{head}{TABLE_START}\n{table}\n{TABLE_END}{tail}"


def build(check=False):
    data = load_providers()
    changed = []

    table = render_table(data)
    readme = README.read_text(encoding="utf-8")
    new_readme = inject_table(readme, table)
    if new_readme != readme:
        changed.append(str(README))
        if not check:
            README.write_text(new_readme, encoding="utf-8", newline="\n")

    PROVIDERS_DIR.mkdir(exist_ok=True)
    for p in data["providers"]:
        page = render_page(p)
        path = PROVIDERS_DIR / f"{p['id']}.md"
        if not path.exists() or path.read_text(encoding="utf-8") != page:
            changed.append(str(path))
            if not check:
                path.write_text(page, encoding="utf-8", newline="\n")

    if check:
        if changed:
            print("STALE — regenerate with: python scripts/build.py")
            print("\n".join(sorted(changed)))
            return 1
        print("OK — generated files are up to date")
        return 0

    print(f"Built {len(data['providers'])} provider pages")
    for f in changed:
        print(f"  updated: {Path(f).relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if generated files are stale")
    sys.exit(build(check=ap.parse_args().check))
