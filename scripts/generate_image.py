#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate image via Kie.ai Nano Banana 2
Creates a task and returns task_id for async retrieval
"""

import os
import sys
import json
import requests
from datetime import datetime

# Fix emoji encoding on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load .env if exists
def load_env():
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()

load_env()

# Config
KIE_API_KEY = os.getenv("KIE_API_KEY")  # Use Kie.ai API key, not Gemini
KIE_BASE_URL = "https://api.kie.ai/api/v1/jobs"

# Brand template
BRAND_TEMPLATE = {
    "background": "#000000",  # Black
    "text_primary": "#FFFFFF",  # White
    "accent": "#00C8FF",  # Cyan
    "accent_alt": "#8B5CF6",  # Purple
    "font": "Inter Bold / Montserrat Black",
    "dimensions": "1080x1080px",
    "logo": "brief.ia - circular badge with white/cyan design, top-left corner, 100px diameter, subtle",
}

def create_slide_prompt(slide_num: int, title: str, body: str, context: str = "", style: str = "default") -> str:
    """
    Create a standardized visual prompt for Kie.ai Nano Banana 2

    Args:
        slide_num: Slide number (1-5 typically)
        title: Main headline/title
        body: Body text (1-2 lines)
        context: Additional context about the carousel (topic, theme)
        style: Visual style ('default', 'impact', 'verdict', 'signal')
               'impact' = large dramatic text with effects
               'verdict' = emphasized score/conclusion
               'signal' = contrasting ideas (dead vs alive)

    Returns:
        Prompt string for Nano Banana 2 (with reference image support)
    """

    # Style-specific instructions
    style_prompts = {
        "default": """
VISUAL STYLE:
- High-contrast minimalist design
- Large bold sans-serif text
- Black background with white/cyan text
- Clean, professional, tech-forward
""",
        "impact": """
VISUAL STYLE — DRAMATIC & IMPACTFUL:
- Gritty, high-impact visual design
- HUGE main title (takes 60-70% of space) in WHITE
- Visual effects: cracks, breaks, shatters, or glitch effects on key words
- If showing contradiction: use RED (#FF3333) for "dead/broken/wrong" concepts
- RED glow or halo around emphasized words
- Black background for maximum contrast
- Professional but bold/edgy, not clean corporate
- Think: tech disruption, breaking news, paradigm shift
""",
        "verdict": """
VISUAL STYLE — SCORE/CONCLUSION:
- Verdict number or statement DOMINATES (60%+ of space)
- Simple, bold, dramatic
- White text on black
- Optional: subtle background accent color (cyan or purple)
- Clear visual hierarchy
""",
        "signal": """
VISUAL STYLE — CONTRASTING IDEAS:
- Show two opposing concepts visually
- "Dead/Old" idea: darker, breaking apart, fading, or struck-through
- "New/Alive" idea: bright, glowing, prominent
- Use RED for "old/dead", CYAN or WHITE for "new/alive"
- High contrast between the two ideas
"""
    }

    selected_style = style_prompts.get(style, style_prompts["default"])

    content = f"""
You are a professional designer creating an Instagram carousel slide #{slide_num}/5 for French tech founders.
Audience: Solopreneurs, freelancers, startup builders interested in AI tools.

SLIDE TEXT CONTENT:
TITLE: {title}
BODY: {body}

{f"CONTEXT: {context}" if context else ""}

BRAND STANDARDS:
- Canvas: 1080×1080px square
- Background: #000000 (pure black, no gradients)
- Primary font: Inter Bold, Montserrat Black, or similar modern sans-serif
- Primary colors: #FFFFFF (white), #00C8FF (cyan), #FF3333 (red for impact)
- Style: High-contrast, minimal, mobile-readable

LOGO PLACEMENT (MUST INCLUDE):
- Position: TOP-LEFT CORNER (20-30px from edges)
- Design: Circular badge, dark gray/charcoal background
- Content: Text "brief" in WHITE, ".ia" in CYAN (#00C8FF)
- Size: 100-120px diameter (clearly visible)
- Opacity: Fully visible (NOT faded or transparent)
- Important: Logo must appear on every slide at this exact position

{selected_style}

CRITICAL RULES:
1. **LOGO MUST BE PRESENT** — Include brief.ia circular badge in top-left corner (100-120px, clearly visible)
2. Title/main text must be READABLE on mobile (at least 1080/10 = ~100px minimum)
3. Text must be centered or well-aligned, not scattered
4. NO photography, no faces, no complex illustrations
5. NO watermarks except brief.ia logo (which MUST appear)
6. If using effects (cracks, glows, breaks): keep text readable under/over them
7. Generate 1080×1080 PNG

TEXT TO RENDER:
Main: {title}
Subtitle: {body}

Create a professional, high-impact Instagram carousel slide that matches the visual style above.
"""

    return content.strip()


def submit_generation_task(
    title: str,
    body: str,
    slide_num: int = 1,
    context: str = "",
    aspect_ratio: str = "1:1",
    resolution: str = "1K",
    style: str = "default",
    reference_image_url: str = None
) -> dict:
    """
    Submit image generation task to Kie.ai

    Args:
        style: 'default', 'impact' (dramatic), 'verdict' (score), 'signal' (contrast)
        reference_image_url: Optional URL to reference image for style guidance

    Returns:
        {
            "task_id": "abc-123",
            "status": "created",
            "timestamp": "2026-04-14T10:30:00Z"
        }
    """

    if not KIE_API_KEY:
        raise ValueError("KIE_API_KEY not set in environment")

    prompt = create_slide_prompt(slide_num, title, body, context, style)

    headers = {
        "Authorization": f"Bearer {KIE_API_KEY}",
        "Content-Type": "application/json"
    }

    # Build input object (Kie.ai requires params in "input" field)
    input_obj = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "resolution": resolution,
        "output_format": "png"
    }

    # Add reference image if provided (for style guidance)
    if reference_image_url:
        input_obj["image_input"] = [reference_image_url]

    payload = {
        "model": "nano-banana-2",
        "input": input_obj
    }

    try:
        response = requests.post(
            f"{KIE_BASE_URL}/createTask",
            headers=headers,
            json=payload,
            timeout=10
        )
        response.raise_for_status()

        result = response.json()

        # Handle Kie.ai response format: {"code": 200, "msg": "success", "data": {"taskId": "...", "recordId": "..."}}
        if result.get("code") == 200 and result.get("data"):
            task_id = result["data"].get("taskId") or result["data"].get("recordId")
        else:
            task_id = result.get("task_id") or result.get("taskId")

        if not task_id:
            raise ValueError(f"No task_id in response: {result}")

        return {
            "task_id": task_id,
            "status": "created",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "slide_num": slide_num,
            "title": title[:50],  # Store first 50 chars for reference
            "cost_estimated": 0.04  # Nano Banana 2 at 1K
        }

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] API request failed: {e}", file=sys.stderr)
        raise


def main():
    """CLI interface"""

    if len(sys.argv) < 3:
        print("Usage: python3 generate_image.py <slide_num> <title> <body> [context] [--style STYLE] [--ref IMAGE_URL]")
        print()
        print("Styles: default, impact, verdict, signal")
        print()
        print("Examples:")
        print('  python3 generate_image.py 1 "Voici le hook" "Description courte"')
        print('  python3 generate_image.py 1 "Le prompt engineering" "est mort." --style impact --ref https://example.com/ref.png')
        sys.exit(1)

    slide_num = int(sys.argv[1])
    title = sys.argv[2]
    body = sys.argv[3]
    context = ""
    style = "default"
    ref_image = None

    # Parse optional arguments
    for i in range(4, len(sys.argv)):
        if sys.argv[i] == "--style" and i + 1 < len(sys.argv):
            style = sys.argv[i + 1]
        elif sys.argv[i] == "--ref" and i + 1 < len(sys.argv):
            ref_image = sys.argv[i + 1]
        elif not sys.argv[i].startswith("--"):
            context = sys.argv[i]

    print(f"[GENERATE] Slide {slide_num} ({style})...")
    print(f"   Title: {title}")
    print(f"   Body: {body[:50]}...")
    if ref_image:
        print(f"   Ref: {ref_image[:60]}...")

    result = submit_generation_task(
        title=title,
        body=body,
        slide_num=slide_num,
        context=context,
        style=style,
        reference_image_url=ref_image
    )

    # Output JSON for easy parsing by other tools
    print(json.dumps(result, indent=2))

    return result


if __name__ == "__main__":
    main()
