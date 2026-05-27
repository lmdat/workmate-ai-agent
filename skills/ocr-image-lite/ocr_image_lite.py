#!/usr/bin/env python3
"""
OCR Skill (Lite) — Tesseract only, no EasyOCR
Usage: python ocr_image_lite.py <image_path> [--lang vie+eng] [--psm 6]

Output: raw text → stdout | logs → stderr
Exit:   0 = success | 1 = error

Dependencies:
    pip install pytesseract pillow
    Linux:   sudo apt-get install tesseract-ocr tesseract-ocr-vie
    macOS:   brew install tesseract
    Windows: https://github.com/UB-Mannheim/tesseract/wiki
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import pytesseract
    from PIL import Image, ImageFilter, ImageOps
except ImportError:
    print("ERROR: pip install pytesseract pillow", file=sys.stderr)
    sys.exit(1)

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tiff", ".tif", ".bmp", ".webp"}


def log(msg: str):
    print(msg, file=sys.stderr)


def validate_image(image_path: str) -> Path:
    p = Path(image_path).resolve()
    if not p.exists():
        log(f"ERROR: File không tồn tại: {p}")
        sys.exit(1)
    if p.suffix.lower() not in SUPPORTED_EXTENSIONS:
        log(f"ERROR: Định dạng không hỗ trợ '{p.suffix}'. Supported: {', '.join(SUPPORTED_EXTENSIONS)}")
        sys.exit(1)
    return p


def preprocess_image(image_path: Path) -> Image.Image:
    img = Image.open(image_path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    w, h = img.size
    if w < 1200:
        scale = 1200 / w
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    img = ImageOps.grayscale(img)
    img = ImageOps.autocontrast(img, cutoff=2)
    img = img.filter(ImageFilter.SHARPEN)
    return img


def run_tesseract(img: Image.Image, lang: str, psm: int) -> str:
    raw = pytesseract.image_to_string(img, lang=lang, config=f"--psm {psm} --oem 3")
    lines = [l.strip() for l in raw.splitlines() if l.strip()]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="OCR Lite: extract text from image → stdout")
    parser.add_argument("image",         help="Đường dẫn file ảnh")
    parser.add_argument("--lang",        default="vie+eng", help="Tesseract language (default: vie+eng)")
    parser.add_argument("--psm",         type=int, default=6,
                        help="Tesseract PSM mode (default: 6). "
                             "6=block, 4=single column, 11=sparse text")
    args = parser.parse_args()

    image_path = validate_image(args.image)
    log(f"[OCR] File: {image_path} | lang: {args.lang} | psm: {args.psm}")

    img = preprocess_image(image_path)
    log("[OCR] Chạy Tesseract...")
    text = run_tesseract(img, args.lang, args.psm)

    if not text.strip():
        log("ERROR: Không đọc được text. Thử đổi --psm hoặc kiểm tra chất lượng ảnh.")
        log("  Gợi ý: --psm 4 (single column) hoặc --psm 11 (sparse text)")
        log("  Gợi ý: --lang eng (cho tiếng Việt không dấu)")
        
        sys.exit(1)

    log(f"[OCR] Done — {len(text)} ký tự")
    print(text)


if __name__ == "__main__":
    main()
