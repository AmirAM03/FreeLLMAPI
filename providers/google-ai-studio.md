---
name: Google AI Studio
id: google-ai-studio
category: cloud-platform
api_base: https://generativelanguage.googleapis.com/v1beta
openai_compatible: true
auth: api-key
docs: https://ai.google.dev/gemini-api/docs
website: https://ai.google.dev
signup: https://aistudio.google.com
last_verified: 2025-09-01
---

# Google AI Studio

> 🟠 **Cloud Platform** · **OpenAI-compatible:** ✔ · **Status:** 🟢 Verified

[![Docs](https://img.shields.io/badge/Docs-Documentation-blue)](https://ai.google.dev/gemini-api/docs)
[![Sign up](https://img.shields.io/badge/Sign%20up-Free-brightgreen)](https://aistudio.google.com)

**API Base:** `https://generativelanguage.googleapis.com/v1beta`

## 🔑 Getting Access
1. Sign up at [Google AI Studio](https://aistudio.google.com) — no credit card required.
2. Generate an API key from the dashboard.
3. **Free tier:** Free tier available in most regions (billing enabled for overages).

## 🌐 Endpoints
| Endpoint | Notes |
|---|---|
| `https://generativelanguage.googleapis.com/v1beta` | OpenAI-compatible (`/chat/completions`, `/models`) |

## 🧠 Models
| Model ID | Context | Notes |
|---|---|---|
| `gemini-2.5-flash` | 1,048,576 | Best price-performance with adaptive thinking |
| `gemini-2.5-pro` | 1,048,576 | Top reasoning quality |
| `gemini-2.0-flash` | 1,048,576 | Efficient multimodal workhorse |
| `gemini-2.0-flash-lite` | 1,048,576 | Cheapest, fastest Flash variant |
| `gemini-1.5-flash-8b` | 1,048,576 | High-RPM free workhorse (1,500 req/day) |

## ⏱️ Free Tier Limits
Gemini 2.5 Pro: 5 RPM / 100 RPD (paid tier) — free tier for 2.5 Flash: 10 RPM / 250 RPD; 1.5 Flash: 15 RPM / 1,500 RPD; 1.5 Flash-8B: 15 RPM / 1,500 RPD.

## ✨ Highlights
- Native multimodal — text, images, video, audio, PDFs in one call
- OpenAI-compatible endpoint available (`/v1beta/openai/`)
- 1M-token context windows

## 📋 Example Request
```bash
curl https://generativelanguage.googleapis.com/v1beta/chat/completions \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gemini-2.5-flash", "messages": [{"role": "user", "content": "Hello!"}]}'
```

---
*Auto-generated from [`data/providers.json`](../data/providers.json) — last verified 2025-09-01.
Found something wrong? [Open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose).*
