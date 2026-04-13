---
name: newsletter-to-instagram
description: |
  Transforms newsletter content (PDF files in the newsletter/ folder) into high-impact Instagram posts.
  Extracts the most relevant information for the brief.ia audience (French-speaking founders, freelancers, creators),
  scores each info by Instagram potential, and generates complete post packages: caption FR, slide-by-slide text,
  Canva specs, and hashtags.

  Use when asked to:
  - Create an Instagram post from newsletters
  - Find what's hot in newsletters this week
  - Transform newsletter content into Instagram content
  - Generate post ideas from newsletters
  - What should I post based on newsletters

  Triggers: "newsletter", "post from newsletter", "contenu newsletter", "newsletter instagram",
  "quoi poster", "infos chaudes", "news de la semaine"
---

# Newsletter → Instagram Post

Transform newsletter content into high-impact Instagram posts for brief.ia.

## Overview

This skill reads PDF newsletters, extracts the most relevant information for the brief.ia audience
(French-speaking founders, freelancers, creators), scores each piece of content by Instagram potential,
and produces a complete post package ready for Canva + publication.

## Audience Profile (brief.ia)

Always filter and angle content through this lens:
- **Who**: French-speaking founders, freelancers, creators building with AI
- **Pain points**: productivity, staying ahead of AI tools, not getting left behind, building faster
- **Content that works**: tool reveals, "X is dead / X replaces Y", choc numbers, controversy, actionable tips
- **Tone**: direct, informed, slightly provocative — not corporate

## Workflow

### Step 1 — Read PDFs

Read all PDF files in the `newsletter/` folder:

```python
# Use the Read tool on each PDF file found with Glob pattern: newsletter/*.pdf
# Extract full text from each page
```

List all found newsletters and their sources (Product Hunt, Every, The Rundown, TLDR, etc.).

### Step 2 — Extract & Score Information

For each piece of information found, evaluate its Instagram potential score (1–10):

**Scoring criteria:**
| Criterion | Weight | Questions to ask |
|-----------|--------|-----------------|
| Freshness | 25% | Is this from the last 3 days? New announcement? |
| Wow factor | 25% | Does it surprise? Choc numbers? Counterintuitive? |
| Relevance to brief.ia audience | 25% | Does it matter to FR founders/freelancers/creators? |
| Hook potential | 15% | Can you open with a punchy one-liner? |
| Actionability | 10% | Can the audience do something with this today? |

**Score threshold**: only keep items scoring ≥ 7/10.

Output a ranked table:

```
| # | Info | Source | Score | Why it works |
|---|------|--------|-------|--------------|
| 1 | ... | ... | 9/10 | ... |
```

### Step 3 — Select Top Pick

Choose the #1 item based on score. If two items are close (within 0.5 points), present both as options
and ask the user to choose.

Explain the choice: why this info, why today, what angle.

### Step 4 — Generate Post Package

For the selected item, generate a complete post package:

#### A. FORMAT CHOICE
Choose the best format based on content type:
- **Carrousel** (3–7 slides): for explanations, comparisons, lists, tutorials
- **Single image**: for choc stats, quotes, simple announcements
- **Reel script**: for storytelling, demos, reactions

#### B. SLIDE-BY-SLIDE CONTENT (for carrousel)

For each slide, provide:
```
SLIDE [N] — [Role: Hook / Context / Shift / Proof / CTA]
─────────────────────────────────
TITRE (bold, max 8 words):
[text]

CORPS (optional, max 3 lines):
[text]

VISUEL CANVA:
[description of background, colors, layout, elements]
─────────────────────────────────
```

Standard carrousel structure:
- **Slide 1 (Hook)**: provocative statement, question, or choc number
- **Slide 2 (Context)**: why this matters, what's changing
- **Slide 3 (Shift)**: the key insight — before/after, comparison, twist
- **Slide 4 (Proof/Application)**: concrete examples, numbers, or how to apply
- **Slide 5 (CTA)**: lead magnet + comment trigger

#### C. CAPTION (French)

Structure:
```
[Hook line — same as slide 1, punchy]

[2-3 lines of context]

[Key insight, formatted with → or numbered list]

[Stakes / why it matters for the reader]

[CTA — "Commente [MOT] pour recevoir [RESSOURCE]"]

[5-8 hashtags]
```

Rules:
- Write in French
- No corporate language — direct, informed, slightly provocative
- Hook must work as standalone (first 2 lines visible before "voir plus")
- CTA must use a single French word (GUIDE, LIEN, LISTE, OUTIL, etc.)

#### D. CANVA SPECS

Always apply the brief.ia brand guidelines from `.claude/context/brand-guidelines.md`:

```
FORMAT: 1080×1080px (carré) — défaut brief.ia
BACKGROUND: #000000 (noir pur)
TEXT COLOR: #FFFFFF (blanc)
ACCENT / MOT CLÉ: #00C8FF (cyan électrique)
BORDER: violette #8B5CF6 sur tous les côtés
FONT: Bold sans-serif (Inter Bold / Montserrat Black / Space Grotesk Bold)
LOGO: "brief.ia" — coin haut gauche, discret
LAYOUT: texte centré, max 3–4 lignes par slide, marges généreuses
VISUAL ELEMENTS: [éléments spécifiques au sujet — mockups, chiffres, icônes]
```

#### E. HASHTAGS

Provide 8–12 hashtags split into:
- 3 broad (#IA, #intelligence_artificielle, #tech)
- 3 medium (#fondateurs, #freelance, #entrepreneuriat)
- 2–3 niche (#contextengineering, #agentsIA, etc.)
- 1 branded (#briefia)

### Step 5 — Save Post to File

Save the complete post package to `newsletter-posts/YYYY-MM-DD_[topic].md`:

```markdown
# Post: [Topic]
Date: [YYYY-MM-DD]
Source: [Newsletter name]
Format: [Carrousel/Single/Reel]
Score: [X/10]

## Slides
[Full slide content]

## Caption
[Full caption]

## Canva Specs
[Full specs]

## Hashtags
[Full list]
```

Create the `newsletter-posts/` folder if it doesn't exist.

## Quick Reference

Full workflow summary:
1. `Glob newsletter/*.pdf` → find all PDFs
2. `Read` each PDF → extract content
3. Score each info item (≥7/10 to keep)
4. Select top pick, explain choice
5. Generate: slides + caption + Canva specs + hashtags
6. Save to `newsletter-posts/YYYY-MM-DD_[topic].md`

## Content Patterns That Score High for brief.ia

**Hook formulas that work:**
- "[X] est mort. Voici ce qui le remplace."
- "[Chiffre choc] — et personne n'en parle."
- "Ce que [Big Company] vient de faire change tout pour les fondateurs."
- "[Outil] vient de sortir. Il fait [résultat impressionnant] gratuitement."
- "La raison pour laquelle [X] ne fonctionne plus en 2026."

**Angles that work for this audience:**
- Productivity gains (time saved, costs cut)
- Competitive advantage ("ceux qui maîtrisent ça auront une longueur d'avance")
- Tool comparisons ("X remplace Y")
- Behind-the-scenes of big AI companies
- Actionable tutorials (do this in 3 steps)

**Angles to avoid:**
- Pure technical/research content without business angle
- US-market-only content with no relevance to FR founders
- Content already covered everywhere (no freshness)
