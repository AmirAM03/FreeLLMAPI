---
name: Cloudflare Workers AI
id: cloudflare-workers-ai
category: edge-serverless
api_base: https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/v1
openai_compatible: true
auth: api-key
docs: https://developers.cloudflare.com/workers-ai/
website: https://developers.cloudflare.com/workers-ai/
signup: https://dash.cloudflare.com
last_verified: 2025-09-01
---

# Cloudflare Workers AI

> 🟢 **Edge / Serverless** · **OpenAI-compatible:** ✔ · **Status:** 🟢 Verified

[![Docs](https://img.shields.io/badge/Docs-Documentation-blue)](https://developers.cloudflare.com/workers-ai/)
[![Sign up](https://img.shields.io/badge/Sign%20up-Free-brightgreen)](https://dash.cloudflare.com)

**API Base:** `https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/v1`

## 🔑 Getting Access
1. Sign up at [Cloudflare Workers AI](https://dash.cloudflare.com) — no credit card required.
2. Generate an API key from the dashboard.
3. **Free tier:** 10,000 neurons/day per account, free forever.

## 🌐 Endpoints
| Endpoint | Notes |
|---|---|
| `https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/v1` | OpenAI-compatible (`/chat/completions`, `/models`) |

## 🧠 Models
| Model ID | Context | Notes |
|---|---|---|
| `@cf/meta/llama-3.3-70b-instruct-fp8-fast` | 16,384 | Largest open model on the edge, FP8-fast |
| `@cf/meta/llama-3.1-8b-instruct` | 128,000 | Fast general-purpose |
| `@cf/qwen/qwen2.5-coder-32b-instruct` | 16,384 | Code completion & chat |
| `@cf/mistralai/mistral-small-3.1-24b-instruct` | 131,072 | Multimodal + function calling |

## ⏱️ Free Tier Limits
10,000 neurons/day; no hard RPM cap published.

## ✨ Highlights
- Inference at the edge — runs in 300+ cities near your users
- OpenAI-compatible REST adapters for chat/embeddings
- Neurons-based free allocation resets daily

## 📋 Example Request
```bash
curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/v1/chat/completions \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "@cf/meta/llama-3.3-70b-instruct-fp8-fast", "messages": [{"role": "user", "content": "Hello!"}]}'
```

---
*Auto-generated from [`data/providers.json`](../data/providers.json) — last verified 2025-09-01.
Found something wrong? [Open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose).*
