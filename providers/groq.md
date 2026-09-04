---
name: Groq
id: groq
category: hosted-inference
api_base: https://api.groq.com/openai/v1
openai_compatible: true
auth: api-key
docs: https://console.groq.com/docs/openai
website: https://groq.com
signup: https://console.groq.com
last_verified: 2025-09-01
---

# Groq

> 🔵 **Hosted Inference** · **OpenAI-compatible:** ✔ · **Status:** 🟢 Verified

[![Docs](https://img.shields.io/badge/Docs-Documentation-blue)](https://console.groq.com/docs/openai)
[![Sign up](https://img.shields.io/badge/Sign%20up-Free-brightgreen)](https://console.groq.com)

**API Base:** `https://api.groq.com/openai/v1`

## 🔑 Getting Access
1. Sign up at [Groq](https://console.groq.com) — no credit card required.
2. Generate an API key from the dashboard.
3. **Free tier:** Free developer tier with generous limits for building and testing.

## 🌐 Endpoints
| Endpoint | Notes |
|---|---|
| `https://api.groq.com/openai/v1` | OpenAI-compatible (`/chat/completions`, `/models`) |

## 🧠 Models
| Model ID | Context | Notes |
|---|---|---|
| `llama-3.3-70b-versatile` | 131,072 | Flagship open model, high throughput |
| `llama-3.1-8b-instant` | 131,072 | Sub-second latency workhorse |
| `openai/gpt-oss-120b` | 131,072 | OpenAI's open-weight model, LPU-fast |
| `qwen/qwen3-32b` | 131,072 | Strong multilingual + reasoning |
| `deepseek-r1-distill-llama-70b` | 131,072 | Distilled reasoning, streaming thinking tokens |

## ⏱️ Free Tier Limits
Model-dependent — e.g. llama-3.3-70b-versatile: 30 req/min, 12,000 tokens/min, 1,000 req/day.

## ✨ Highlights
- LPU inference — hundreds of tokens/sec, fastest free API available
- Full OpenAI SDK compatibility (base_url swap only)
- No credit card, no expiry; JIT provisioning per model

## 📋 Example Request
```bash
curl https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": "Hello!"}]}'
```

---
*Auto-generated from [`data/providers.json`](../data/providers.json) — last verified 2025-09-01.
Found something wrong? [Open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose).*
