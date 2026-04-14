#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Instagram Story (1080×1920, 9:16 aspect ratio) via Kie.ai Nano Banana 2
Adapted from generate_image.py for vertical story format
"""

import os
import sys
import json
import requests
from datetime import datetime

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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

KIE_API_KEY = os.getenv("KIE_API_KEY")
KIE_BASE_URL = "https://api.kie.ai/api/v1/jobs"

def create_story_prompt(story_num: int, headline: str, body: str, context: str = "", style: str = "default") -> str:
    """
    Create visual prompt for Instagram Story (vertical 9:16)

    Args:
        story_num: Story sequence (1, 2, 3...)
        headline: Main text (top/center)
        body: Secondary text (bottom)
        context: Additional context
        style: 'default' (clean), 'impact' (dramatic), 'minimal' (text-only)
    """

    style_prompts = {
        "default": """
VISUAL STYLE — Instagram Story:
- Vertical format 1080×1920 (Instagram Story native)
- Black background (#000000)
- Large bold text, white primary (#FFFFFF), cyan accent (#00C8FF)
- Minimal design, maximum readability on mobile
- Top 20% and bottom 40% reserved for text
- Center area: breathing room
""",
        "minimal": """
VISUAL STYLE — Text Only:
- Vertical 1080×1920
- Pure black background
- Text ONLY, no graphics, no effects
- White text, cyan highlights
- Typography-focused
""",
        "impact": """
VISUAL STYLE — High Impact:
- Vertical 1080×1920
- Dark background with gradient (black → dark grey)
- Large dramatic text
- RED (#FF3333) for shock value, CYAN for questions
- Emphasis on contrast
"""
    }

    selected_style = style_prompts.get(style, style_prompts["default"])

    content = f"""
You are a professional designer creating an Instagram Story for brief.ia (day {story_num}).
Audience: Solopreneurs, freelancers interested in AI tools and honest tests.

STORY TEXT:
HEADLINE: {headline}
BODY: {body}

{f"CONTEXT: {context}" if context else ""}

SPECIFICATIONS:
- Canvas: 1080×1920px (vertical, Instagram Story native)
- Aspect ratio: 9:16
- Background: #000000 (black, no gradients)
- Primary text color: #FFFFFF (white)
- Highlight/accent: #00C8FF (cyan)
- Font: Inter Bold or Montserrat Black (modern sans-serif)
- Safe text zones: Top 20% (headlines) + Bottom 40% (body text)
- Center area: 40% breathing room for visual interest

LOGO PLACEMENT (OPTIONAL):
- Position: Top-right corner (if included)
- Size: 60×60px (small, doesn't overwhelm story)
- Fully visible, NOT transparent

{selected_style}

CRITICAL RULES:
1. **VERTICAL FORMAT** — This is a Story (9:16), NOT a carousel slide (1:1)
2. Text must be HUGE and readable at glance (min 50pt for headline)
3. Keep text in safe zones (top/bottom margins 100px)
4. NO photography, NO faces, NO watermarks except brief.ia logo
5. High contrast for mobile screens
6. Generate 1080×1920 PNG

TEXT TO RENDER:
Headline: {headline}
Body: {body}

Create a striking Instagram Story that's immediately scannable and memorable.
"""

    return content.strip()


def submit_story_task(
    story_num: int,
    headline: str,
    body: str,
    context: str = "",
    style: str = "default"
) -> dict:
    """
    Submit Instagram Story generation task to Kie.ai

    Returns:
        {"task_id": "...", "status": "created", "timestamp": "..."}
    """

    if not KIE_API_KEY:
        raise ValueError("KIE_API_KEY not set in environment")

    prompt = create_story_prompt(story_num, headline, body, context, style)

    headers = {
        "Authorization": f"Bearer {KIE_API_KEY}",
        "Content-Type": "application/json"
    }

    input_obj = {
        "prompt": prompt,
        "aspect_ratio": "9:16",  # Instagram Story vertical
        "resolution": "1K",  # 1080×1920
        "output_format": "png"
    }

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
            "story_num": story_num,
            "format": "Instagram Story (9:16)",
            "cost_estimated": 0.04
        }

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] API request failed: {e}", file=sys.stderr)
        raise


def main():
    """CLI interface"""

    if len(sys.argv) < 3:
        print("Usage: python3 generate_story.py <story_num> <headline> <body> [context] [--style STYLE]")
        print()
        print("Styles: default, minimal, impact")
        print()
        print("Examples:")
        print('  python3 generate_story.py 1 "Jour 1 : test Paperclip" "Setup: quelques min → 1h"')
        print('  python3 generate_story.py 2 "Problème découvert" "Writer bloqué." --style default')
        sys.exit(1)

    story_num = int(sys.argv[1])
    headline = sys.argv[2]
    body = sys.argv[3]
    context = ""
    style = "default"

    for i in range(4, len(sys.argv)):
        if sys.argv[i] == "--style" and i + 1 < len(sys.argv):
            style = sys.argv[i + 1]
        elif not sys.argv[i].startswith("--"):
            context = sys.argv[i]

    print(f"[STORY] Generating Story #{story_num} (9:16 vertical)...")
    print(f"   Headline: {headline}")
    print(f"   Body: {body[:50]}...")

    result = submit_story_task(
        story_num=story_num,
        headline=headline,
        body=body,
        context=context,
        style=style
    )

    print(json.dumps(result, indent=2))

    return result


if __name__ == "__main__":
    main()
