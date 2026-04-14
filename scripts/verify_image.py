#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verify generated image meets brief.ia standards
Checks dimensions, format, basic quality
"""

import sys
import json
from pathlib import Path

# Fix emoji encoding on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    from PIL import Image
except ImportError:
    print("[ERROR] PIL not installed. Run: pip install Pillow", file=sys.stderr)
    sys.exit(1)


# Brand standards
EXPECTED_WIDTH = 1080
EXPECTED_HEIGHT = 1080
EXPECTED_FORMAT = "PNG"
MIN_FILE_SIZE_KB = 50  # Too small = likely broken
MAX_FILE_SIZE_KB = 5000  # Too large = inefficient


def verify_image(image_path: str) -> dict:
    """
    Verify image meets specifications

    Returns:
        {
            "valid": True/False,
            "errors": [list of issues],
            "warnings": [list of warnings],
            "metadata": {
                "width": 1080,
                "height": 1080,
                "format": "PNG",
                "file_size_kb": 123,
                "mode": "RGB"
            }
        }
    """

    errors = []
    warnings = []
    metadata = {}

    # File exists?
    path = Path(image_path)
    if not path.exists():
        return {
            "valid": False,
            "errors": [f"File not found: {image_path}"],
            "warnings": [],
            "metadata": {}
        }

    # File size
    file_size_kb = path.stat().st_size / 1024
    metadata["file_size_kb"] = file_size_kb

    if file_size_kb < MIN_FILE_SIZE_KB:
        errors.append(f"File too small ({file_size_kb:.1f} KB). Possible corrupt image.")
    if file_size_kb > MAX_FILE_SIZE_KB:
        warnings.append(f"File large ({file_size_kb:.1f} KB). Consider compression.")

    # Image properties
    try:
        img = Image.open(image_path)
        width, height = img.size
        img_format = img.format
        img_mode = img.mode

        metadata["width"] = width
        metadata["height"] = height
        metadata["format"] = img_format
        metadata["mode"] = img_mode

        # Dimensions
        if width != EXPECTED_WIDTH or height != EXPECTED_HEIGHT:
            errors.append(
                f"Wrong dimensions: {width}×{height}. Expected {EXPECTED_WIDTH}×{EXPECTED_HEIGHT}"
            )

        # Format
        if img_format != EXPECTED_FORMAT:
            errors.append(f"Wrong format: {img_format}. Expected {EXPECTED_FORMAT}")

        # Color mode (should be RGB or RGBA)
        if img_mode not in ("RGB", "RGBA"):
            warnings.append(f"Unusual color mode: {img_mode}. Standard is RGB/RGBA.")

    except Exception as e:
        errors.append(f"Cannot read image: {e}")

    # Summary
    valid = len(errors) == 0

    return {
        "valid": valid,
        "errors": errors,
        "warnings": warnings,
        "metadata": metadata,
        "status": "[PASS]" if valid else "[FAIL]"
    }


def main():
    """CLI interface"""

    if len(sys.argv) < 2:
        print("Usage: python3 verify_image.py <image_path>")
        print()
        print("Example:")
        print("  python3 verify_image.py images/2026-04-14_paperclip/slide_1.png")
        sys.exit(1)

    image_path = sys.argv[1]

    print(f"[VERIFY] {image_path}...")
    result = verify_image(image_path)

    # Print human-readable output
    print(f"\n{result['status']}\n")

    if result["metadata"]:
        print("Metadata:")
        for key, value in result["metadata"].items():
            print(f"  {key}: {value}")

    if result["errors"]:
        print("\n[ERRORS]")
        for error in result["errors"]:
            print(f"  - {error}")

    if result["warnings"]:
        print("\n[WARNINGS]")
        for warning in result["warnings"]:
            print(f"  - {warning}")

    # Output JSON for automation
    print("\n" + json.dumps(result, indent=2))

    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
