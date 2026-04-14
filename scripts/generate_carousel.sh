#!/bin/bash
# Generate a complete 5-slide carousel for brief.ia Instagram
# Usage: ./generate_carousel.sh "Topic Name" "Style" "Ref Image URL (optional)"

set -e

TOPIC=${1:-"test"}
STYLE=${2:-"default"}  # Changed from "impact" to "default" (less sensational)
REF_IMG=${3:-""}

SLIDES_FILE="../contenu/carousel-${TOPIC}.md"
OUTPUT_DIR="../images/$(date +%Y-%m-%d)_${TOPIC}"

echo "[CAROUSEL] Generating 5 slides for: $TOPIC (style: $STYLE)"
echo "[INFO] Output: $OUTPUT_DIR"

mkdir -p "$OUTPUT_DIR"

# Task IDs will be stored here
TASKS=()

# Parse slides from markdown (basic parsing - adjust as needed)
echo "[PARSE] Reading slides from contenu/carousel-*.md..."

# For now, use manual slide definition
# Real version would parse the markdown file

# Slide 1 - Hook
echo "[STEP 1] Generating slide 1 (hook)..."
TASK=$(python3 generate_image.py 1 "Anthropic bloque" "Claude hors de portée" "" --style "$STYLE" $([[ ! -z "$REF_IMG" ]] && echo "--ref $REF_IMG") 2>&1 | grep -o '"task_id": "[^"]*"' | cut -d'"' -f4)
TASKS+=($TASK)
echo "  → Task ID: $TASK"

# Slide 2 - Context
echo "[STEP 2] Generating slide 2 (context)..."
TASK=$(python3 generate_image.py 2 "Fini les agents tiers" "Seule l'API reste" "" --style "$STYLE" 2>&1 | grep -o '"task_id": "[^"]*"' | cut -d'"' -f4)
TASKS+=($TASK)
echo "  → Task ID: $TASK"

# Slide 3 - Comparison
echo "[STEP 3] Generating slide 3 (comparison)..."
TASK=$(python3 generate_image.py 3 "OpenAI vs Anthropic" "Open vs Fermé" "" --style "$STYLE" 2>&1 | grep -o '"task_id": "[^"]*"' | cut -d'"' -f4)
TASKS+=($TASK)
echo "  → Task ID: $TASK"

# Slide 4 - Impact
echo "[STEP 4] Generating slide 4 (impact)..."
TASK=$(python3 generate_image.py 4 "Les builders perdent" "Changement de règles" "" --style "$STYLE" 2>&1 | grep -o '"task_id": "[^"]*"' | cut -d'"' -f4)
TASKS+=($TASK)
echo "  → Task ID: $TASK"

# Slide 5 - Conclusion
echo "[STEP 5] Generating slide 5 (conclusion)..."
TASK=$(python3 generate_image.py 5 "Contrôle vs Écosystème" "Quelle stratégie gagne?" "" --style "$STYLE" 2>&1 | grep -o '"task_id": "[^"]*"' | cut -d'"' -f4)
TASKS+=($TASK)
echo "  → Task ID: $TASK"

echo ""
echo "[RETRIEVE] Downloading images (this may take 30-60 seconds)..."

# Retrieve all in parallel
for i in "${!TASKS[@]}"; do
  SLIDE_NUM=$((i + 1))
  TASK_ID="${TASKS[$i]}"
  OUTPUT_FILE="$OUTPUT_DIR/slide_${SLIDE_NUM}.png"

  echo "[RETRIEVE] Slide $SLIDE_NUM (task: $TASK_ID)..."
  python3 retrieve_image.py "$TASK_ID" "$OUTPUT_FILE" &
done

wait
echo ""
echo "[VERIFY] Checking image quality..."

for i in "${!TASKS[@]}"; do
  SLIDE_NUM=$((i + 1))
  OUTPUT_FILE="$OUTPUT_DIR/slide_${SLIDE_NUM}.png"

  if [ -f "$OUTPUT_FILE" ]; then
    python3 verify_image.py "$OUTPUT_FILE" | grep "\[PASS\]\|\[FAIL\]"
  else
    echo "[FAIL] Slide $SLIDE_NUM: File not found"
  fi
done

echo ""
echo "[COMPLETE] Carousel generated!"
echo "Location: $OUTPUT_DIR"
echo ""
echo "Next steps:"
echo "  1. Review images in $OUTPUT_DIR"
echo "  2. Create post markdown"
echo "  3. Publish to Instagram"
