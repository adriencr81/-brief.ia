---
name: newsletter-to-instagram-with-ai-images
description: |
  Fast workflow to transform newsletter content into Instagram posts with AI-generated visuals.
  Extracts top 3-5 news from newsletters, scores by Instagram potential, and generates a standardized post with 5 matching AI images.
  Uses Nano-Banana MCP (Google Gemini Flash) to generate carousel images matching brand identity.
  One reusable CTA, minimal customization, ~2-3 min per post. Best text quality for Instagram slides.

  Use when asked to:
  - Create Instagram post from newsletter (fast track)
  - Generate carousel with AI images from news
  - Weekly news-to-Instagram automation
  - Transform newsletter to social content (lightweight)

  Triggers: "newsletter instagram", "post news", "carousel news", "news instagram"
---

# Newsletter → Instagram Post (Fast, Standardized, AI Images)

Transform newsletter content into branded Instagram carousel posts in 2-3 minutes with zero custom copywriting.

## Overview

This skill is designed for **speed and repetition**:
- ✅ Reads PDF newsletters
- ✅ Auto-scores and selects top 3-5 news
- ✅ Fills a **standardized template** (no custom writing per post)
- ✅ Generates 5 AI images matching brand colors (via Nano-Banana MCP + Gemini Flash)
- ✅ One reusable CTA (configured once, used every time)
- ✅ Markdown post + images → ready to publish

**Speed**: 2-3 minutes from PDF to published post (no ManyChat setup needed per post)

**Template-driven**: Same structure every post, different news content

**Cost**: ~€10-15/month (best text-to-image quality for automated Instagram posts)

## Audience Profile (brief.ia)

- **Who**: French-speaking founders, freelancers, creators building with AI
- **What matters**: productivity, tool reveals, competitive advantage, "X is dead / Y replaces it", shocking numbers
- **Tone**: direct, informed, provocative — no corporate fluff

## Workflow (4 Steps, ~2-3 min)

### Step 1 — Read & Score PDFs

1. Find all PDFs in `newsletter/` folder
2. Extract key news/links from each
3. Score each by Instagram potential (1–10):
   - Freshness (new this week?) — 25%
   - Wow factor (shocking/surprising?) — 25%
   - Relevance (matters for FR founders?) — 25%
   - Hook strength (catchy opening?) — 15%
   - Actionability (can do something?) — 10%
4. **Keep only ≥7/10 scores**
5. **Select TOP 3-5 news** (stop here, no overthinking)

Output:
```
| # | News | Score | Source |
|----|------|-------|--------|
| 1 | ... | 9/10 | ... |
| 2 | ... | 8/10 | ... |
| 3 | ... | 7.5/10 | ... |
```

### Step 2 — Extract Info (No Writing)

For each of the TOP 3-5, extract ONLY:
- **Headline** (copy from news, max 10 words)
- **1-line summary** (copy/extract, not written — just what's the key fact)

Example:
```
Headline: "Claude agents révolutionnent l'IA d'entreprise"
Summary: "Anthropic lance les agents Claude — des IA autonomes capables de réfléchir avant d'agir."
```

**NO CUSTOM WRITING AT THIS STEP** — just extraction.

### Step 3 — Fill Standardized Post Template

Each post uses the **same template** with different news:

```
SLIDE 1 — Hook
────────────────
TITRE: [News 1 headline, max 10 words]
CORPS: [1-line summary]

SLIDE 2 — Context
────────────────
TITRE: [Why this matters]
CORPS: [1 line explaining impact]

SLIDE 3 — Key Insight
────────────────
TITRE: [The shift / What changes]
CORPS: [1-2 lines]

SLIDE 4 — Related News
────────────────
TITRE: [Quick mention of news 2-3]
CORPS: [Combine top 2-3 other news in bullet points, very short]

SLIDE 5 — CTA
────────────────
TITRE: "La semaine en bref.ia"
CORPS: [Standard CTA — see below]
```

**CAPTION** (same for all posts):
```
[Hook line from slide 1]

[1-2 lines context from slide 2]

Dossiers cette semaine:
• [News 1]
• [News 2]
• [News 3]

Et 10+ infos, analyses et outils chaque semaine dans brief.ia.

#IA #fondateurs #freelance #briefia
```

**CTA** (FIXED — configured once, reused always):
```
"Commente NEWS pour recevoir les infos brutes de la semaine"
```

**Brand specs** (same every post):
- 1080×1080px, black background (#000000)
- White text, cyan accents (#00C8FF)
- Inter Bold or Montserrat Black
- "brief.ia" logo top-left, discrete
- Purple borders (#8B5CF6) optional

### Step 4 — Generate AI Images (for the 5 slides)

For each of the 5 slides, generate a custom AI image using **Nano-Banana MCP** (Google Gemini Flash).

**Simple prompt per slide:**

```
You are a visual designer creating Instagram carousel slides for a tech/business audience (French founders).

Slide [N]/5: [SLIDE TITLE]
Text: [SLIDE BODY - 1-2 lines]

Design:
- Black background (#000000)
- White + cyan (#00C8FF) text, bold sans-serif
- 1080×1080px square
- "brief.ia" logo top-left, subtle
- Minimalist, high-contrast, readable on mobile

Text to display: [SLIDE TITLE] + [SLIDE BODY]
```

**Process:**
1. Generate this prompt for each slide
2. Call Nano-Banana MCP (uses GEMINI_API_KEY from .env)
3. Save PNG to: `images/YYYY-MM-DD_[topic-from-main-news]/slide_[N].png`

**Time**: ~1-2 min total (5 images)

### Step 5 — Save Post

Save to `newsletter-posts/YYYY-MM-DD_[topic].md`:

```markdown
# Newsletter Post — [Date]

## Slides

**Slide 1**
![](../../images/YYYY-MM-DD_topic/slide_1.png)

**Slide 2**
![](../../images/YYYY-MM-DD_topic/slide_2.png)

[... etc ...]

## Caption

[From template above]

## Brand Specs

- 1080×1080px, black bg (#000000), white text, cyan accents (#00C8FF)
- Font: Inter Bold / Montserrat Black
- Logo: brief.ia top-left, discrete
```

Done. Images ready for Instagram or Canva upload.

## Quick Reference

**4 Simple Steps (2-3 min):**

1. Read PDFs + Score news → Keep TOP 3-5 (≥7/10)
2. Extract headlines + 1-line summaries (NO custom writing)
3. Fill template: Slide 1 = Hook, Slide 2 = Context, Slide 3 = Insight, Slide 4 = Related News, Slide 5 = CTA
4. Generate 5 AI images → Save post markdown → Done

**Output:**
- `images/YYYY-MM-DD_[topic]/slide_1.png` through `slide_5.png`
- `newsletter-posts/YYYY-MM-DD_[topic].md` (ready to publish)

## Tech Setup

**Required:**
- `REPLICATE_TOKEN` in `.env` (get free from https://replicate.com)
- Python or Node.js SDK for Replicate (optional, can use REST API directly)
- `/images` folder created ✓

**Setup steps:**
1. Sign up at https://replicate.com (free account)
2. Get API token from https://replicate.com/account/api-tokens
3. Add to `.env`: `REPLICATE_TOKEN=your_token_here`

**Costs:**
- ~$0.002-0.003 per image (Stable Diffusion 3)
- Typical: 5 images/post × 7 posts/week = 35 images/week → Budget **€0.50-1.00/month**
- Replicate gives $25 free monthly credit on new accounts (covers 8,000+ images)

**API Example (Python):**
```python
import replicate

output = replicate.run(
  "stability-ai/stable-diffusion-3-medium",
  input={
    "prompt": "Your prompt here...",
    "width": 1080,
    "height": 1080,
    "num_outputs": 1,
    "guidance_scale": 7.5,
    "num_inference_steps": 30
  }
)
# output is a list of URLs
```

**If image generation fails:**
- Continue without images (Canva specs only)
- Retry later (rate limits are very generous)
- Check API token validity
