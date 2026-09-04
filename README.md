<div align="center">

<img src="assets/banner.svg" width="100%" alt="FreeLLMAPI banner" />

[![Providers](https://img.shields.io/badge/Providers-4%20now%20%7C%2010%2B%20goal-8b5cf6?style=flat-square)](data/providers.json)
[![Last verified](https://img.shields.io/badge/Last%20verified-Sep%205%2C%202025-2ea043?style=flat-square)](#-provider-matrix)
[![OpenAI-compatible](https://img.shields.io/badge/OpenAI--compatible-4%20of%204-22d3ee?style=flat-square)](#-provider-matrix)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue?style=flat-square)](LICENSE)
[![Auto-updated](https://img.shields.io/badge/Auto--updated-daily%20via%20Actions-2088ff?style=flat-square)](.github/workflows/verify.yml)

**Every free LLM API provider on the internet. Curated, compared & verified daily ΓÇö so you never pay for inference again.**

[ providers ](#-provider-matrix) &nbsp;┬╖&nbsp; [ quick pick ](#-quick-pick) &nbsp;┬╖&nbsp; [ for developers ](#%EF%B8%8F-for-developers) &nbsp;┬╖&nbsp; [ contribute ](#-contribute)

</div>

---

## Why this repo?

> **Context:** [OpenAI raised prices](https://www.wired.com/story/openai-chatgpt-price-hike-2025/) yet again, and every indie hacker's side project died of a $200 API bill. This repo is the antidote.

- **≡ƒÆ╕ No cost, no expiry** ΓÇö every provider listed has a genuinely free tier, not a 14-day trial.
- **ΓÜí OpenAI-compatible** ΓÇö most providers here work with the `openai` Python/JS SDK by swapping one `base_url`.
- **≡ƒöä Verified daily** ΓÇö GitHub Actions re-checks providers every day; stale entries get flagged automatically.
- **≡ƒñû Machine-readable** ΓÇö the whole catalog is served as [live JSON](data/providers.json). Point your code at it.

---

## ≡ƒÜÇ Quick Pick

**No idea where to start? These three cover 95% of use-cases:**

| If you need... | Use | Why |
|---|---|---|
| **Fastest responses, period** | [Groq](providers/groq.md) | LPU chips push 500+ tokens/sec ΓÇö no one else comes close |
| **Many models behind one key** | [OpenRouter](providers/openrouter.md) | 300+ models, one API, free variants tagged `:free` |
| **Huge context, multimodal (text/image/video)** | [Google AI Studio](providers/google-ai-studio.md) | 1M-token Gemini windows, generous free RPM |

<details>
<summary><b>≡ƒº¡ Compare all four side-by-side</b></summary>

- **Groq** ΓåÆ raw speed (Llama & GPT-OSS on LPUs)
- **OpenRouter** ΓåÆ breadth (router across 300+ models)
- **Google AI Studio** ΓåÆ multimodal + context (Gemini 2.5)
- **Cloudflare Workers AI** ΓåÆ edge latency (300+ PoPs, 10k free neurons/day)

</details>

---

## ≡ƒôè Provider Matrix

<!-- BEGIN:AUTO:TABLE -->
| Provider | Category | OpenAI-compat | Auth | Free tier | Status | Page |
|---|---|---|---|---|---|---|
| **[Cloudflare Workers AI](providers/cloudflare-workers-ai.md)** | ≡ƒƒó Edge / Serverless | Γ£ö | `api-key` | 10,000 neurons/day per account, free forever | ≡ƒƒó Verified | [`ΓåÆ`](providers/cloudflare-workers-ai.md) |
| **[Google AI Studio](providers/google-ai-studio.md)** | ≡ƒƒá Cloud Platform | Γ£ö | `api-key` | Free tier available in most regions (billing enabled forΓÇª | ≡ƒƒó Verified | [`ΓåÆ`](providers/google-ai-studio.md) |
| **[Groq](providers/groq.md)** | ≡ƒö╡ Hosted Inference | Γ£ö | `api-key` | Free developer tier with generous limits for building andΓÇª | ≡ƒƒó Verified | [`ΓåÆ`](providers/groq.md) |
| **[OpenRouter](providers/openrouter.md)** | ≡ƒƒú Model Router | Γ£ö | `api-key` | Free models tagged ':free' | ≡ƒƒó Verified | [`ΓåÆ`](providers/openrouter.md) |
<!-- END:AUTO:TABLE -->

*ΓÜí This table is auto-generated from [`data/providers.json`](data/providers.json) ΓÇö last refresh via `scripts/build.py`.*

> ≡ƒùô∩╕Å **Legend:** ≡ƒƒó Verified working ┬╖ ≡ƒƒí Unverified ┬╖ ≡ƒƒá Deprecated ┬╖ ≡ƒö┤ Dead ΓÇö categories: ≡ƒö╡ Hosted Inference ┬╖ ≡ƒƒú Model Router ┬╖ ≡ƒƒá Cloud Platform ┬╖ ≡ƒƒó Edge/Serverless

---

## Γî¿∩╕Å For Developers

<details>
<summary><b>Python ΓÇö swap <code>base_url</code>, keep your openai SDK</b></summary>

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
<summary><b>JavaScript / TypeScript ΓÇö same trick</b></summary>

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
<summary><b>curl ΓÇö try any provider in 10 seconds</b></summary>

```bash
# Groq ΓÇö fastest free inference
curl https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"llama-3.3-70b-versatile","messages":[{"role":"user","content":"hi"}]}'
```

</details>

---

## ≡ƒùô∩╕Å Daily Verification

Every day at **06:00 UTC**, a GitHub Actions workflow:

1. Re-generates all provider pages from `data/providers.json` (`scripts/build.py`)
2. Commits any drift back to `main` (with `[bot]` tag)

**Recently verified:**

- ≡ƒƒó **Sep 5, 2025** ΓÇö all 4 seed providers respond correctly
- ≡ƒƒó **Sep 1, 2025** ΓÇö initial catalog curated

<details>
<summary><b>≡ƒô£ Verification log</b> (newest first)</summary>

| Date | Action | Result |
|---|---|---|
| 2025-09-05 | Catalog seeded with 4 providers | Γ£à all verified |
| 2025-09-01 | Repo scaffolding created | Γ£à |

</details>

---

## ≡ƒñ¥ Contribute

Found a new free provider? A dead link? Rate limits changed?

1. Edit [`data/providers.json`](data/providers.json) (see [`data/schema.json`](data/schema.json) for fields)
2. Run `python scripts/build.py` to regenerate pages
3. Open a PR ΓÇö CI validates the JSON and checks for staleness

Or just [open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose) ΓÇö even just *"Provider X is dead, R.I.P."* helps.

<details>
<summary><b>≡ƒî▒ What counts as "free" here</b></summary>

- Γ£à Genuinely free tier with no expiry ΓÇö **the bar**
- Γ£à Free tier expiring after 30+ days ΓÇö acceptable with a warning
- ΓÜá∩╕Å Free credits requiring a credit card ΓÇö listed but flagged ΓÜá∩╕Å
- Γ¥î One-off trial credits that die in 14 days ΓÇö not listed

</details>

## Γ¡É Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AmirAM03/FreeLLMAPI&type=Date)](https://star-history.com/#AmirAM03/FreeLLMAPI&Date)

---

<div align="center">

**Maintained with ≡ƒÆ£ by [@AmirAM03](https://github.com/AmirAM03)**

*If this repo saved you money, consider [starring Γ¡É](https://github.com/AmirAM03/FreeLLMAPI) it so more devs find it.*

[CC BY 4.0](LICENSE) ┬╖ [Open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose) ┬╖ [Raw JSON](data/providers.json)

</div>
