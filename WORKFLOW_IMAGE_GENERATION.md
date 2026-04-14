# Image Generation Workflow — brief.ia

**3 modular scripts:**
1. `generate_image.py` — Create task (Kie.ai)
2. `retrieve_image.py` — Poll & download
3. `verify_image.py` — Check quality

---

## Quick Start

### Step 1: Generate (Create Task)
```bash
cd scripts

python3 generate_image.py 1 "J'ai passé 2h à configurer 4 agents IA." "Ils m'ont sorti une newsletter sur un outil de 2022."
```

**Output:**
```json
{
  "task_id": "abc-123-def-456",
  "status": "created",
  "slide_num": 1,
  "cost_estimated": 0.04
}
```

### Step 2: Retrieve (Poll & Download)
```bash
python3 retrieve_image.py abc-123-def-456 ../images/2026-04-14_paperclip/slide_1.png
```

**Output:**
```json
{
  "task_id": "abc-123-def-456",
  "state": "success",
  "output_path": "../images/2026-04-14_paperclip/slide_1.png",
  "elapsed_seconds": 15,
  "download_success": true
}
```

### Step 3: Verify (Quality Check)
```bash
python3 verify_image.py ../images/2026-04-14_paperclip/slide_1.png
```

**Output:**
```
✅ PASS

Metadata:
  width: 1080
  height: 1080
  format: PNG
  file_size_kb: 245.3
  mode: RGB

{...json...}
```

---

## Full Carousel Workflow (5 Slides)

### Prepare Content
Create a markdown file with your 5 slides:

```markdown
# Carousel — My Topic

## Slide 1 — Hook
**Title:** J'ai passé 2h à configurer 4 agents IA.
**Body:** Ils m'ont sorti une newsletter sur un outil de 2022.

## Slide 2 — Context
**Title:** Ce que j'ai voulu automatiser
**Body:** Ma veille IA → newsletter hebdo en français...

[... etc for slides 3-5 ...]
```

### Generate All 5 (Parallel Friendly)

```bash
# Create all 5 tasks
python3 generate_image.py 1 "Hook title" "Hook body" > slide_1_task.json
python3 generate_image.py 2 "Context title" "Context body" > slide_2_task.json
python3 generate_image.py 3 "Insight title" "Insight body" > slide_3_task.json
python3 generate_image.py 4 "Related title" "Related body" > slide_4_task.json
python3 generate_image.py 5 "CTA title" "CTA body" > slide_5_task.json

# Extract task IDs
TASK_1=$(jq -r .task_id slide_1_task.json)
TASK_2=$(jq -r .task_id slide_2_task.json)
TASK_3=$(jq -r .task_id slide_3_task.json)
TASK_4=$(jq -r .task_id slide_4_task.json)
TASK_5=$(jq -r .task_id slide_5_task.json)

# Retrieve all 5 (will poll in parallel)
python3 retrieve_image.py $TASK_1 ../images/2026-04-14_topic/slide_1.png &
python3 retrieve_image.py $TASK_2 ../images/2026-04-14_topic/slide_2.png &
python3 retrieve_image.py $TASK_3 ../images/2026-04-14_topic/slide_3.png &
python3 retrieve_image.py $TASK_4 ../images/2026-04-14_topic/slide_4.png &
python3 retrieve_image.py $TASK_5 ../images/2026-04-14_topic/slide_5.png &
wait

# Verify all 5
for i in {1..5}; do
  python3 verify_image.py ../images/2026-04-14_topic/slide_$i.png
done
```

---

## Script Details

### generate_image.py

**Usage:**
```
python3 generate_image.py <slide_num> <title> <body> [context]
```

**Parameters:**
- `slide_num`: 1-5 (for context in the prompt)
- `title`: Main headline (10-20 words)
- `body`: Supporting text (1-2 lines)
- `context`: Optional context (topic, theme of carousel)

**What it does:**
1. Takes title + body
2. Applies brand template (1080×1080, black bg, cyan accents)
3. Creates visual design prompt for Nano Banana 2
4. Submits to Kie.ai
5. Returns `task_id` for async retrieval

**Cost:** $0.04 per image (auto-charged)

**Speed:** <5 seconds (task creation only)

---

### retrieve_image.py

**Usage:**
```
python3 retrieve_image.py <task_id> [output_path]
```

**Parameters:**
- `task_id`: From generate_image.py output
- `output_path`: Where to save PNG (default: `images/{task_id}.png`)

**What it does:**
1. Polls Kie.ai every 2 seconds
2. Exponential backoff (2s → 2.02s → 2.04s...)
3. Max 100 retries (~3 minutes timeout)
4. When `state === "success"`, downloads PNG
5. Saves to `output_path`

**Polling states:**
- `waiting` / `queuing` / `generating` → keep polling
- `success` → download and save ✅
- `fail` → return error ❌

**Speed:** 15-45 seconds typical (generation on Kie.ai)

---

### verify_image.py

**Usage:**
```
python3 verify_image.py <image_path>
```

**Checks:**
- ✅ File exists
- ✅ Dimensions: 1080×1080 (exact)
- ✅ Format: PNG
- ✅ File size: 50-5000 KB (not broken, not bloated)
- ✅ Color mode: RGB/RGBA

**Output:**
- `valid: true/false`
- Detailed errors/warnings
- Metadata (size, format, etc.)

**Speed:** <1 second

---

## Automation: Creating a Skill

Combine these into a Claude skill:

```
📁 .claude/skills/
  └─ generate-carousel-ai/
      ├─ SKILL.md
      └─ (symlink to ../../../scripts/)
```

The skill can:
1. Read carousel markdown
2. Extract 5 slides
3. Call generate_image.py (all 5 in parallel)
4. Call retrieve_image.py (wait for all)
5. Call verify_image.py (check quality)
6. If all pass: create post markdown
7. If any fail: notify for manual retry

---

## Brand Template Reference

All generated images follow this template automatically:

| Property | Value |
|----------|-------|
| **Dimensions** | 1080×1080px (square) |
| **Background** | #000000 (pure black) |
| **Text Primary** | #FFFFFF (white) |
| **Accent** | #00C8FF (cyan) |
| **Accent Alt** | #8B5CF6 (purple) |
| **Font** | Inter Bold / Montserrat Black |
| **Style** | High-contrast, minimalist, mobile-readable |
| **Logo** | brief.ia (top-left, subtle, ~10% opacity) |

---

## Troubleshooting

### Task stuck in "generating"
- Normal up to 60 seconds
- Check: `python3 retrieve_image.py <task_id>`
- If >100s: likely API issue, try different task

### Image looks wrong (text/colors off)
- Check verify_image.py passes dimensions/format
- Visual check: open in browser/editor
- If Kie.ai issue: regenerate with tweaked prompt

### API errors (401, 402, 429)
- 401: Check GEMINI_API_KEY in .env
- 402: Out of credits (Kie.ai account)
- 429: Rate limited (>20 tasks/10s) — slow down

### Timeout after 100 retries
- Rare, but possible if Kie.ai is slow
- Increase MAX_RETRIES in retrieve_image.py if needed
- Usually safe to retry — same task_id = no new charge

---

## Next Steps

1. ✅ Scripts created
2. ⏭️ Test with real content (1 slide)
3. ⏭️ Verify output quality
4. ⏭️ Create a Skill to automate 5-slide generation
5. ⏭️ Integrate into newsletter-to-instagram workflow
