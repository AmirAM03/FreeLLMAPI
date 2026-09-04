<!--
  ⚠️  TEMPLATE ONLY — provider pages are AUTO-GENERATED from data/providers.json
  by scripts/build.py. Do not edit generated pages directly.

  To add or update a provider, edit data/providers.json instead.
  See CONTRIBUTING.md for the full field reference.
-->

---
name: Provider Name
category: hosted-inference | model-router | cloud-platform | edge-serverless
api_base: https://api.example.com/v1
openai_compatible: true
auth: api-key
docs: https://docs.example.com
website: https://example.com
signup: https://console.example.com
playground: https://example.com/playground
last_verified: YYYY-MM-DD
---

# Provider Name

> **Category dot** Category Label · **OpenAI-compatible:** ✔ · **Status:** 🟢

One-sentence summary of what makes this provider worth using.

## 🔑 Getting Access
1. Sign up at the console (link) — no credit card required.
2. Generate an API key from the dashboard.
3. Quota notes from `free_tier`.

## 🌐 Endpoints
| Endpoint | Notes |
|---|---|
| `{api_base}` | OpenAI-compatible (`/chat/completions`, `/models`) |

## 🧠 Models
| Model ID | Context | Notes |
|---|---|---|
| `model-id` | 128,000 | Why you'd pick this one |

## ⏱️ Free Tier Limits
Rate limits and quota description from `rate_limits`.

## ✨ Highlights
- Bullets from the `highlights` array

## 📋 Example Request
```bash
curl {api_base}/chat/completions \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "model-id", "messages": [{"role": "user", "content": "Hello!"}]}'
```

---
*Auto-generated from [`data/providers.json`](../data/providers.json) — last updated YYYY-MM-DD.
Found something wrong? [Open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose).*
