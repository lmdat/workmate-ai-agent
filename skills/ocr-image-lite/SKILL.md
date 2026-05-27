---
name: ocr-image-lite
description: "Use this skill whenever the task involves extracting text from an image file (PNG, JPG, JPEG, TIFF, BMP, WEBP). Lightweight version — Tesseract only, no EasyOCR. Fast, minimal install (~10MB vs ~500MB). Use when you need OCR on clean/decent quality images. Trigger on any mention of: reading text from image, scan hóa đơn, đọc file ảnh, extract text PNG/JPG, OCR."
---

# OCR Image Skill (Lite)

Tesseract only — không có EasyOCR fallback. Nhẹ, nhanh, đủ dùng cho ảnh chất lượng tốt.

## Script location

```
ocr_image_lite.py
```

## Step 1: Detect Python command

**Linux/macOS (bash):**
```bash
if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "ERROR: Python not found"; exit 1
fi
```

**Windows (PowerShell):**
```powershell
if (Get-Command python -ErrorAction SilentlyContinue) {
    $PYTHON = "python"
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $PYTHON = "python3"
} else {
    Write-Error "ERROR: Python not found"; exit 1
}
```

## Step 2: Check and install dependencies

```bash
# Python packages (~10MB total)
$PYTHON -c "import pytesseract" 2>/dev/null || pip install pytesseract
$PYTHON -c "from PIL import Image" 2>/dev/null || pip install pillow

# Tesseract binary
# Linux:   sudo apt-get install -y tesseract-ocr tesseract-ocr-vie
# macOS:   brew install tesseract
# Windows: https://github.com/UB-Mannheim/tesseract/wiki
#          Tải thêm vie.traineddata → bỏ vào thư mục tessdata

# Kiểm tra
tesseract --version 2>/dev/null || echo "WARNING: Tesseract not found"
tesseract --list-langs 2>/dev/null | grep -q "vie" \
    || echo "WARNING: Vietnamese pack not found, dùng --lang eng"
```

## Step 3: Run the script

```bash
$PYTHON ocr_image_lite.py <image_path>
```

### Options

| Argument | Default | Description |
|---|---|---|
| `image` | (required) | Path to image file |
| `--lang` | `vie+eng` | Tesseract language. Dùng `eng` nếu không có Vietnamese pack |
| `--psm` | `6` | Tesseract page segmentation mode |

### PSM modes hay dùng

| PSM | Dùng khi |
|---|---|
| `6` | Hóa đơn, bảng biểu thẳng hàng (default) |
| `4` | Layout dạng cột dọc |
| `11` | Text rải rác, layout phức tạp |

### Examples

```bash
$PYTHON ocr_image_lite.py invoice.png
$PYTHON ocr_image_lite.py receipt.jpg --lang eng
$PYTHON ocr_image_lite.py scan.png --psm 4
```

## Step 4: Use the output

- **stdout** → raw extracted text (dùng cái này)
- **stderr** → logs (bỏ qua, chỉ để debug)
- **Exit code 0** = success, **Exit code 1** = error

```bash
TEXT=$($PYTHON ocr_image_lite.py invoice.png)
```

## Khi nào nên dùng bản full (ocr-image)?

Nếu ảnh bị mờ, scan nghiêng, chất lượng kém → dùng `ocr-image` (có EasyOCR fallback).
Bản lite này phù hợp cho ảnh chụp rõ, scan thẳng.

## Supported formats

`.png` `.jpg` `.jpeg` `.tiff` `.tif` `.bmp` `.webp`
