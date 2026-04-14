#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Retrieve generated image from Kie.ai
Polls task status until complete, then downloads PNG
"""

import os
import sys
import json
import time
import requests
from datetime import datetime
from pathlib import Path

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
KIE_API_KEY = os.getenv("KIE_API_KEY")
KIE_BASE_URL = "https://api.kie.ai/api/v1/jobs"

# Polling config
POLL_INTERVAL = 2  # seconds
MAX_RETRIES = 100  # ~200 sec = ~3 min
BACKOFF_MULTIPLIER = 1.01  # Slight exponential backoff


def poll_task_status(task_id: str, max_retries: int = MAX_RETRIES) -> dict:
    """
    Poll task status until success or failure

    Returns:
        {
            "task_id": "...",
            "state": "success|fail",
            "image_url": "https://...",  # if success
            "fail_msg": "...",  # if fail
            "retries": N,
            "elapsed_seconds": N
        }
    """

    if not KIE_API_KEY:
        raise ValueError("KIE_API_KEY not set in environment")

    headers = {
        "Authorization": f"Bearer {KIE_API_KEY}",
        "Content-Type": "application/json"
    }

    start_time = time.time()
    retry = 0
    current_interval = POLL_INTERVAL

    while retry < max_retries:
        try:
            response = requests.get(
                f"{KIE_BASE_URL}/recordInfo",
                headers=headers,
                params={"taskId": task_id},
                timeout=10
            )
            response.raise_for_status()

            result = response.json()

            # Extract task from Kie.ai response
            task = result.get("data", result)
            state = task.get("state")
            fail_msg = task.get("failMsg", "")

            elapsed = time.time() - start_time

            # Parse resultJson (it's a string in Kie.ai response)
            result_json_str = task.get("resultJson", "{}")
            try:
                result_json = json.loads(result_json_str) if isinstance(result_json_str, str) else result_json_str
            except json.JSONDecodeError:
                result_json = {}

            # Extract image URL (can be in resultUrls or image_url)
            image_url = None
            if result_json.get("resultUrls"):
                image_url = result_json["resultUrls"][0]
            elif result_json.get("image_url"):
                image_url = result_json["image_url"]

            if state == "success":
                print(f"[SUCCESS] Task {task_id} succeeded in {elapsed:.1f}s")
                return {
                    "task_id": task_id,
                    "state": "success",
                    "image_url": image_url,
                    "cost": 0.04,
                    "retries": retry,
                    "elapsed_seconds": elapsed
                }

            elif state == "fail":
                print(f"[FAILED] Task {task_id} failed: {fail_msg}")
                return {
                    "task_id": task_id,
                    "state": "fail",
                    "fail_msg": fail_msg,
                    "retries": retry,
                    "elapsed_seconds": elapsed
                }

            else:
                print(f"[POLLING] {state}... ({retry+1}/{max_retries}, {elapsed:.1f}s)")

        except requests.exceptions.RequestException as e:
            print(f"[WARN] Poll error: {e}", file=sys.stderr)

        # Exponential backoff
        time.sleep(current_interval)
        current_interval *= BACKOFF_MULTIPLIER
        retry += 1

    elapsed = time.time() - start_time
    return {
        "task_id": task_id,
        "state": "timeout",
        "fail_msg": f"Max retries ({max_retries}) exceeded after {elapsed:.1f}s",
        "retries": retry,
        "elapsed_seconds": elapsed
    }


def download_image(image_url: str, output_path: str) -> bool:
    """
    Download image from URL and save locally

    Returns:
        True if successful, False otherwise
    """

    try:
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()

        # Ensure directory exists
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        # Save file
        with open(output_path, "wb") as f:
            f.write(response.content)

        file_size = len(response.content) / 1024  # KB
        print(f"[SAVED] {output_path} ({file_size:.1f} KB)")
        return True

    except Exception as e:
        print(f"[ERROR] Download failed: {e}", file=sys.stderr)
        return False


def retrieve_and_save(task_id: str, output_path: str = None, max_retries: int = MAX_RETRIES) -> dict:
    """
    Full workflow: poll + download + save

    If output_path is None, uses default: images/{task_id}.png
    """

    if output_path is None:
        output_path = f"images/{task_id}.png"

    print(f"[RETRIEVE] Polling task {task_id}...")
    poll_result = poll_task_status(task_id, max_retries)

    if poll_result["state"] != "success":
        return poll_result

    image_url = poll_result["image_url"]
    if not image_url:
        return {**poll_result, "state": "error", "fail_msg": "No image_url in response"}

    print(f"[DOWNLOAD] From {image_url[:80]}...")
    success = download_image(image_url, output_path)

    return {
        **poll_result,
        "output_path": output_path if success else None,
        "download_success": success
    }


def main():
    """CLI interface"""

    if len(sys.argv) < 2:
        print("Usage: python3 retrieve_image.py <task_id> [output_path]")
        print()
        print("Example:")
        print("  python3 retrieve_image.py abc-123-def images/2026-04-14_paperclip/slide_1.png")
        sys.exit(1)

    task_id = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    result = retrieve_and_save(task_id, output_path)

    # Output JSON
    print("\n" + json.dumps(result, indent=2))

    if result["state"] == "success" and result.get("download_success"):
        print(f"\n[COMPLETE] Image ready at: {result['output_path']}")
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
