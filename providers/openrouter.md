---
name: OpenRouter
id: openrouter
category: model-router
api_base: https://openrouter.ai/api/v1
openai_compatible: true
auth: api-key
docs: https://openrouter.ai/docs
website: https://openrouter.ai
signup: https://openrouter.ai
last_verified: 2025-09-01
---

# OpenRouter

> 🟣 **Model Router** · **OpenAI-compatible:** ✔ · **Status:** 🟢 Verified

[![Docs](https://img.shields.io/badge/Docs-Documentation-blue)](https://openrouter.ai/docs)
[![Sign up](https://img.shields.io/badge/Sign%20up-Free-brightgreen)](https://openrouter.ai)

**API Base:** `https://openrouter.ai/api/v1`

## 🔑 Getting Access
1. Sign up at [OpenRouter](https://openrouter.ai) — no credit card required.
2. Generate an API key from the dashboard.
3. **Free tier:** Free models tagged ':free' — generous daily limits, no credit card required.

## 🌐 Endpoints
| Endpoint | Notes |
|---|---|
| `https://openrouter.ai/api/v1` | OpenAI-compatible (`/chat/completions`, `/models`) |

## 🧠 Models
| Model ID | Context | Notes |
|---|---|---|
| `meta-llama/llama-3.3-70b-instruct:free` | 131,072 | Flagship open model, strong all-rounder |
| `google/gemini-2.0-flash-exp:free` | 1,048,576 | Experimental Gemini Flash, 1M context |
| `deepseek/deepseek-r1:free` | 163,840 | Reasoning model |
| `qwen/qwen-2.5-72b-instruct:free` | 32,768 | Multilingual workhorse |
| `mistralai/mistral-7b-instruct:free` | 32,768 | Fast & lightweight |

## ⏱️ Free Tier Limits
:free models — 20 req/min, 50 req/day (or 1000 req/day with $10+ credit balance).

## ✨ Highlights
- Unified API for 300+ models — swap models by changing the `model` string
- Automatic fallback across providers if one is down
- Free tier does not expire; some limits lift with $10 credit

## 📋 Example Request
```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "meta-llama/llama-3.3-70b-instruct:free", "messages": [{"role": "user", "content": "Hello!"}]}'
```

---
*Auto-generated from [`data/providers.json`](../data/providers.json) — last verified 2025-09-01.
Found something wrong? [Open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose).*
