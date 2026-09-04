# Contributing to FreeLLMAPI

Thanks for helping keep the free LLM API catalog accurate!

## How to add or update a provider

**The golden rule:** never edit `providers/*.md` or the README table by hand — they are auto-generated from [`data/providers.json`](data/providers.json) by `scripts/build.py`.

### Quick flow

1. **Fork & clone** the repo
2. **Edit** `data/providers.json` — add or update a provider entry
3. **Regenerate:**
   ```bash
   python scripts/build.py
   ```
4. **Commit & PR** — CI runs `build.py --check` to confirm everything is in sync

### Field reference

| Field | Type | Description |
|---|---|---|
| `id` | string | URL slug, lowercase-kebab (e.g. `openrouter`) |
| `name` | string | Display name |
| `category` | enum | `hosted-inference` \| `model-router` \| `cloud-platform` \| `edge-serverless` \| `other` |
| `status` | enum | `verified` \| `unverified` \| `deprecated` \| `dead` |
| `openai_compatible` | bool | Works with the OpenAI SDK via `base_url` swap? |
| `auth` | enum | `api-key` \| `oauth` \| `none` \| `custom` |
| `api_base` | string | Root API endpoint |
| `docs` / `website` / `signup` / `playground` | string | Links |
| `free_tier` | string | One-line description of what's free |
| `rate_limits` | string | RPM / RPD / token limits |
| `models` | array | `{ id, context, notes }` per model |
| `highlights` | array | Bullet points for the provider page |
| `verified` / `last_verified` | date | YYYY-MM-DD |

Full machine-readable schema: [`data/schema.json`](data/schema.json)

## What counts as "free"

- ✅ Genuinely free tier, no expiry — **the bar**
- ✅ Free tier expiring after 30+ days — acceptable with a note
- ⚠️ Free credits requiring a credit card — listed but flagged ⚠️
- ❌ One-off trial credits that die in 14 days — not listed

## Verification etiquette

- Only mark a provider `verified` if you actually made a successful API call with a free key **this month**.
- If a provider fails, don't delete it — set `status: "dead"` or `"deprecated"` and note the date. History has value.

## Questions?

[Open an issue](https://github.com/AmirAM03/FreeLLMAPI/issues/new/choose) — happy to help.
