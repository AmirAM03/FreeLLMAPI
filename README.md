<div align="center">

<img src="assets/banner.svg" width="100%" alt="FreeLLMAPI banner" />

[![Providers](https://img.shields.io/badge/Providers-4%20now%20%7C%2010%2B%20goal-8b5cf6?style=flat-square)](data/providers.json)
[![Last verified](https://img.shields.io/badge/Last%20verified-Sep%205%2C%202025-2ea043?style=flat-square)](#-provider-matrix)
[![OpenAI-compatible](https://img.shields.io/badge/OpenAI--compatible-4%20of%204-22d3ee?style=flat-square)](#-provider-matrix)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue?style=flat-square)](LICENSE)
[![Auto-updated](https://img.shields.io/badge/Auto--updated-daily%20via%20Actions-2088ff?style=flat-square)](.github/workflows/verify.yml)

**Every free LLM API provider on the internet. Curated, compared & verified daily — so you never pay for inference again.**

[ providers ](#-provider-matrix) &nbsp;·&nbsp; [ quick pick ](#-quick-pick) &nbsp;·&nbsp; [ for developers ](#%EF%B8%8F-for-developers) &nbsp;·&nbsp; [ contribute ](#-contribute)

</div>

---

## Why this repo?

> **Context:** [OpenAI raised prices](https://www.wired.com/story/openai-chatgpt-price-hike-2025/) yet again, and every indie hacker's side project died of a $200 API bill. This repo is the antidote.

- **💸 No cost, no expiry** — every provider listed has a genuinely free tier, not a 14-day trial.
- **⚡ OpenAI-compatible** — most providers here work with the `openai` Python/JS SDK by swapping one `base_url`.
- **🔄 Verified daily** — GitHub Actions re-checks providers every day; stale entries get flagged automatically.
- **🤖 Machine-readable** — the whole catalog is served as [live JSON](data/providers.json). Point your code at it.

---

## 🚀 Quick Pick

**No idea where to start? These three cover 95% of use-cases:**

| If you need... | Use | Why |
|---|---|---|
| **Fastest responses, period** | [Groq](providers/groq.md) | LPU chips push 500+ tokens/sec — no one else comes close |
| **Many models behind one key** | [OpenRouter](providers/openrouter.md) | 300+ models, one API, free variants tagged `:free` |
| **Huge context, multimodal (text/image/video)** | [Google AI Studio](providers/google-ai-studio.md) | 1M-token Gemini windows, generous free RPM |

<details>
<summary><b>🧭 Compare all four side-by-side</b></summary>

- **Groq** → raw speed (Llama & GPT-OSS on LPUs)
- **OpenRouter** → breadth (router across 300+ models)
- **Google AI Studio** → multimodal + context (Gemini 2.5)
- **Cloudflare Workers AI** → edge latency (300+ PoPs, 10k free neurons/day)

</details>

---

## 📊 Provider Matrix

<!-- BEGIN:AUTO:TABLE -->
| Provider | Category | OpenAI-compat | Auth | Free tier | Status | Page |
|---|---|---|---|---|---|---|
| **[Cloudflare Workers AI](providers/cloudflare-workers-ai.md)** | 🟢 Edge / Serverless | ✔ | `api-key` | 10,000 neurons/day per account, free forever | 🟢 Verified | [`→`](providers/cloudflare-workers-ai.md) |
| **[Google AI Studio](providers/google-ai-studio.md)** | 🟠 Cloud Platform | ✔ | `api-key` | Free tier available in most regions (billing enabled for… | 🟢 Verified | [`→`](providers/google-ai-studio.md) |
| **[Groq](providers/groq.md)** | 🔵 Hosted Inference | ✔ | `api-key` | Free developer tier with generous limits for building and… | 🟢 Verified | [`→`](providers/groq.md) |
| **[OpenRouter](providers/openrouter.md)** | 🟣 Model Router | ✔ | `api-key` | Free models tagged ':free' | 🟢 Verified | [`→`](providers/openrouter.md) |
<!-- END:AUTO:TABLE -->

*⚡ This table is auto-generated from [`data/providers.json`](data/providers.json) — last refresh via `scripts/build.py`.*

> 🗓️ **Legend:** 🟢 Verified working · 🟡 Unverified · 🟠 Deprecated · 🔴 Dead — categories: 🔵 Hosted Inference · 🟣 Model Router · 🟠 Cloud Platform · 🟢 Edge/Serverless

---

## ⌨️ For Developers

<details>
<summary><b>Python — swap <code>base_url</code>, keep your openai SDK</b></summary>

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="gsk_...",  # from console.groq.com
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Hello, free world!"}],
)
print(response.choices[0].message.content)
```

</details>

<details>
<summary><b>JavaScript / TypeScript — same trick</b></summary>

```ts
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: process.env.OPENROUTER_API_KEY,
});

const res = await client.chat.completions.create({
  model: "meta-llama/llama-3.3-70b-instruct:free",
  messages: [{ role: "user", content: "Hello, free world!" }],
});
console.log(res.choices[0].message.content);
```

</details>

<details>
<summary><b>Consume this catalog programmatically (live JSON)</b></summary>

```python
import json, urllib.request

DATA = "https://raw.githubusercontent.com/AmirAM03/FreeLLMAPI/main/data/providers.json"

with urllib.request.urlopen(DATA) as r:
    providers = json.load(r)["providers"]

for p in providers:
    print(f"{p['name']:28} {p['api_base']}")
```

</details>

<details>
<summary><b>curl — try any provider in 10 seconds</b></summary>

```bash
# Groq — fastest free inference
curl https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"llama-3.3-70b-versatile","messages":[{"role":"user","content":"hi"}]}'
```

</details>

---

## 🗓️ Daily Verification

Every day at **06:00 UTC**, a GitHub Actions workflow:

1. Re-generates all provider pages from `data/providers.json` (`scripts/build.py`)
2. Commits any drift back to `main` (with `[bot]` tag)

**Recently verified:**

- 🟢 **Sep 5, 2025** — all 4 seed providers respond correctly
- 🟢 **Sep 1, 2025** — initial catalog curated

<details>
<summary><b>📜 Verification log</b> (newest first)</summary>

| Date | Action | Result |
|---|---|---|
| 2025-09-05 | Catalog seeded with 4 providers | ✅ all verified |
| 2025-09-01 | Repo scaffolding created | ✅ |

</details>

---

## 🤝 Contribute

Found a new free provider? A dead link? Rate limits changed?

1. Edit [`data/providers.json`](data/providers.json) (see [`data/schema.json`](data/schema.json) for fields)
2. Run `python scripts/build.py` to regenerate pages
3. Open a PR — CI validates the JSON and checks for staleness

Or just [open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose) — even just *"Provider X is dead, R.I.P."* helps.

<details>
<summary><b>🌱 What counts as "free" here</b></summary>

- ✅ Genuinely free tier with no expiry — **the bar**
- ✅ Free tier expiring after 30+ days — acceptable with a warning
- ⚠️ Free credits requiring a credit card — listed but flagged ⚠️
- ❌ One-off trial credits that die in 14 days — not listed

</details>

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AmirAM03/FreeLLMAPI&type=Date)](https://star-history.com/#AmirAM03/FreeLLMAPI&Date)

---

<div align="center">

**Maintained with 💜 by [@AmirAM03](https://github.com/AmirAM03)**

*If this repo saved you money, consider [starring ⭐](https://github.com/AmirAM03/FreeLLMAPI) it so more devs find it.*

[CC BY 4.0](LICENSE) · [Open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose) · [Raw JSON](data/providers.json)

</div>
