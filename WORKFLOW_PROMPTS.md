# Prompt Engineering — Kie.ai Nano Banana 2

## Problem Solved

Images générées via Kie.ai étaient basiques (Image 1).
Référence Gemini était excellente (Image 2) = crack effects, RED glow, impact visuel.

**Solution**: Créer des prompts spécialisés pour Kie.ai qui demandent explicitement les effets visuels.

---

## Prompt Templates

### Style: "impact" (Dramatic & Bold)

**Cas d'usage**: Slide 1 (hook), annonces disruptives, verdicts

**Caractéristiques visuelles demandées**:
- ✅ GROS texte blanc (domине 60-70% de l'espace)
- ✅ Effets visuels: cracks, breaks, shatters, glitch sur mots clés
- ✅ **RED (#FF3333)** pour concepts "morts/brisés"
- ✅ **RED glow** autour des mots en RED
- ✅ Fond noir (#000000) pour maximum de contraste
- ✅ Professionnel mais **edgy/disruptif**, pas corporate

**Prompt pour Kie.ai**:
```
You are a professional designer creating an impactful Instagram carousel slide.

SLIDE TEXT:
Main: [TITLE]
Subtitle: [BODY]

BRAND SPECS:
- Canvas: 1080×1080px
- Background: #000000 (pure black)
- Fonts: Inter Bold, Montserrat Black
- Colors: #FFFFFF (white), #FF3333 (red for impact), #00C8FF (cyan accent)

CRITICAL VISUAL STYLE — DRAMATIC & IMPACTFUL:
- Gritty, high-impact visual design
- HUGE main title in WHITE (takes 60-70% of visible space)
- Visual effects: cracks, breaks, shatters, or glitch effects on key words
- If showing contradiction: use RED (#FF3333) for "dead/broken/wrong" concepts
- RED glow or halo around emphasized words (like glass breaking with red light)
- Black background for MAXIMUM contrast
- Professional but bold/edgy (tech disruption, not corporate slides)
- Think: "paradigm shift", "this tool is dead", "broken promises"

EXAMPLE EFFECT:
If main text is "Le prompt engineering est mort" → 
- "Le prompt engineering" = white, normal
- "est mort" = RED (#FF3333) with shattered/crack effect visible

TEXT TO RENDER:
Main: [TITLE]
Subtitle: [BODY]

Generate a 1080×1080 PNG with gritty, impactful visual design.
```

---

### Style: "signal" (Contrast: Old vs New)

**Cas d'usage**: "X is dead, here's what replaces it" content

**Caractéristiques**:
- ✅ Show old idea: darker, fading, struck-through, or breaking
- ✅ Show new idea: bright, glowing, prominent
- ✅ **RED** for old/dead, **CYAN/WHITE** for new/alive
- ✅ Strong visual separation between the two

**Prompt**:
```
CRITICAL VISUAL STYLE — CONTRASTING IDEAS:
- Visual concept: Show two opposing ideas side-by-side or stacked
- "Dead/Old" concept: darker, fading, breaking apart, struck-through, or cracked
- "New/Alive" concept: bright, glowing, prominent, intact
- Color coding: RED for "old/dead", CYAN (#00C8FF) or WHITE for "new/alive"
- High contrast between the two ideas
- Make the comparison visual, not just textual
```

---

### Style: "verdict" (Score/Conclusion)

**Cas d'usage**: Test results, final score

**Caractéristiques**:
- ✅ Verdict number/statement **DOMINATES** (60%+ of space)
- ✅ Simple, bold, dramatic
- ✅ White text on black
- ✅ Optional subtle accent color (cyan or purple)

**Prompt**:
```
CRITICAL VISUAL STYLE — SCORE/CONCLUSION:
- Verdict number or statement DOMINATES the composition (60%+ visible space)
- Simple, bold, dramatic typography
- White text (#FFFFFF) on black (#000000) background
- Optional: subtle accent color glow (cyan #00C8FF or purple #8B5CF6)
- Clear visual hierarchy - nothing else competes with the score
```

---

## Key Optimization Tips

### 1. Be Explicit About Effects
❌ "Make it impactful"
✅ "Add crack/shatter effects on the word 'mort', with RED glow"

### 2. Use Color Coding
❌ "Show contrast"
✅ "RED (#FF3333) for old idea, CYAN (#00C8FF) for new idea - they should be visually distinct"

### 3. Specify Dominance
❌ "Make text large"
✅ "Title takes 60-70% of visible space - it should dominate the composition"

### 4. Use Reference Images (When Available)
```bash
python3 generate_image.py 1 "Title" "Body" \
  --style impact \
  --ref https://example.com/reference_image.png
```

If Kie.ai has an image of the desired style, it can use it as guidance.

---

## Complete Workflow Example

### Generate "Impact" Style Slide
```bash
cd scripts

python3 generate_image.py 1 \
  "Le prompt engineering" \
  "est mort." \
  "Paperclip vs AI agents" \
  --style impact
```

**Output**:
```json
{
  "task_id": "79b135ffcfc45c002ee8247030166c55",
  "status": "created",
  "cost_estimated": 0.04
}
```

### Retrieve & Save Image
```bash
python3 retrieve_image.py 79b135ffcfc45c002ee8247030166c55 \
  ../images/2026-04-14_prompt-engineering/slide_1.png
```

### Verify Quality
```bash
python3 verify_image.py ../images/2026-04-14_prompt-engineering/slide_1.png
```

---

## Troubleshooting

### Image looks too plain
- Try `--style impact` or `--style signal`
- Check that prompt includes explicit effect descriptions
- Use `--ref` with a reference image

### Text is too small/hard to read
- Prompt should say "takes 60-70% of visible space"
- Request larger font size explicitly

### Colors not right
- Verify hex codes in prompt (#FF3333 for red, #00C8FF for cyan)
- Be explicit: "RED glow", "CYAN accent", not just "red", "cyan"

### Red effect not showing
- If trying to show "dead" concept: request "RED (#FF3333) with crack/shatter effect"
- If trying to show "glow": request "RED glow or halo"
- Be explicit about HOW the red is used

---

## References

- Kie.ai Docs: https://docs.kie.ai/market/google/nanobanana2
- API: POST https://api.kie.ai/api/v1/jobs/createTask
- Polling: GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId={taskId}
