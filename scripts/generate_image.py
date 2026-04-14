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
KIE_API_KEY = os.getenv("GEMINI_API_KEY")
KIE_BASE_URL = "https://api.kie.ai/api/v1/jobs"

# Brand template
BRAND_TEMPLATE = {
    "background": "#000000",  # Black
    "text_primary": "#FFFFFF",  # White
    "accent": "#00C8FF",  # Cyan
    "accent_alt": "#8B5CF6",  # Purple
    "font": "Inter Bold / Montserrat Black",
    "dimensions": "1080x1080px",
    "logo": "brief.ia (top-left, subtle)",
}

def create_slide_prompt(slide_num: int, title: str, body: str, context: str = "") -> str:
    """
    Create a standardized visual prompt for Kie.ai

    Args:
        slide_num: Slide number (1-5 typically)
        title: Main headline/title
        body: Body text (1-2 lines)
        context: Additional context about the carousel (topic, theme)

    Returns:
        Prompt string for Nano Banana 2
    """

    brand_info = f"""
Brand Identity:
- Background: {BRAND_TEMPLATE['background']} (pure black)
- Primary text: {BRAND_TEMPLATE['text_primary']} (white)
- Accent color: {BRAND_TEMPLATE['accent']} (electric cyan)
- Font: {BRAND_TEMPLATE['font']}, bold, sans-serif
- Dimensions: {BRAND_TEMPLATE['dimensions']}
- Logo: {BRAND_TEMPLATE['logo']}
- Style: High-contrast, minimalist, tech-forward, readable on mobile
"""

    content = f"""
You are a professional designer creating Instagram carousel slide #{slide_num}/5 for a tech/business audience.

{brand_info}

Slide Content:
TITLE: {title}
BODY: {body}

{f"Context: {context}" if context else ""}

CRITICAL REQUIREMENTS:
1. Black background (#000000) — no gradients, pure solid black
2. Text must be LARGE and HIGH-CONTRAST:
   - Title: 72pt+ (very bold)
   - Body: 36pt+ (bold)
   - White text (#FFFFFF) for readability
3. Use cyan accents (#00C8FF) for:
   - Key numbers
   - Verdict words
   - CTA text
4. "brief.ia" logo must appear top-left (15-20pt, subtle, ~10% opacity)
5. Purple borders (#8B5CF6) optional but elegant if used
6. NO noise, filters, or visual clutter — clean edges only
7. Text must be centered or left-aligned (not scattered)
8. Ensure text is fully readable on 400px mobile screen

TEXT TO DISPLAY:
"{title}"

"{body}"

Generate a 1080×1080 PNG image matching these specifications exactly.
"""

    return content.strip()


def submit_generation_task(
    title: str,
    body: str,
    slide_num: int = 1,
    context: str = "",
    aspect_ratio: str = "1:1",
    resolution: str = "1K"
) -> dict:
    """
    Submit image generation task to Kie.ai

    Returns:
        {
            "task_id": "abc-123",
            "status": "created",
            "timestamp": "2026-04-14T10:30:00Z"
        }
    """

    if not KIE_API_KEY:
        raise ValueError("GEMINI_API_KEY not set in environment")

    prompt = create_slide_prompt(slide_num, title, body, context)

    headers = {
        "Authorization": f"Bearer {KIE_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "nano-banana-2",
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "resolution": resolution,
        "output_format": "PNG"
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
        task_id = result.get("task_id")

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
        print("Usage: python3 generate_image.py <slide_num> <title> <body> [context]")
        print()
        print("Example:")
        print('  python3 generate_image.py 1 "Voici le hook" "Description courte de 1-2 lignes"')
        sys.exit(1)

    slide_num = int(sys.argv[1])
    title = sys.argv[2]
    body = sys.argv[3]
    context = sys.argv[4] if len(sys.argv) > 4 else ""

    print(f"[GENERATE] Slide {slide_num}...")
    print(f"   Title: {title}")
    print(f"   Body: {body[:50]}...")

    result = submit_generation_task(
        title=title,
        body=body,
        slide_num=slide_num,
        context=context
    )

    # Output JSON for easy parsing by other tools
    print(json.dumps(result, indent=2))

    return result


if __name__ == "__main__":
    main()
