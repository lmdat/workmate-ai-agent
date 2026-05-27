---
name: data-anonymity
description: Skill ẩn danh hóa dữ liệu nhạy cảm trong file bằng cách chạy script Python local qua bash. Dữ liệu gốc KHÔNG được đọc hay gửi lên LLM — toàn bộ xử lý diễn ra trên máy.
---

# Data Anonymity Skill

## Mô tả

Skill ẩn danh hóa dữ liệu nhạy cảm trong file bằng cách chạy script Python local qua bash.
Dữ liệu gốc KHÔNG được đọc hay gửi lên LLM — toàn bộ xử lý diễn ra trên máy.

## Cách dùng

```
# Anonymize
@data-anonymity <đường dẫn file>
@data-anonymity <đường dẫn file> --types phone,email,cccd,name
@data-anonymity <đường dẫn file> --keep-numbers

# Reverse kết quả AI về dữ liệu gốc
@data-anonymity <file_kết_quả_AI> --reverse --mapping tmp/<tên_file>_mapping.json
```

Định dạng hỗ trợ: `.txt` `.csv` `.docx` `.xlsx` `.pdf`

> **PDF**: tự động convert sang `.docx` trước khi mask. Output là file `_masked.docx`, không phải PDF — layout giữ được tốt hơn so với ghi lại PDF.
> **Reverse**: không hỗ trợ `.pdf` — reverse trên file `.docx` đã convert.

---

## Quy trình thực thi

Khi người dùng yêu cầu anonymize một file, hãy thực hiện **đúng thứ tự** sau:

### Bước 1 — Xác định file

Lấy đường dẫn file từ yêu cầu của người dùng. Nếu không rõ, hỏi lại trước khi làm bất cứ điều gì.

Xác định lệnh Python phù hợp với hệ điều hành:
```bash
# Tìm lệnh python khả dụng
python3 --version 2>/dev/null || python --version 2>/dev/null
```

Dùng `python3` nếu có, fallback sang `python` nếu không (thường gặp trên Windows). Dùng lệnh đó nhất quán cho tất cả các bước sau.

Kiểm tra file tồn tại:
```bash
ls -lh "<đường_dẫn_file>"
```

Nếu file không tồn tại → báo lỗi, dừng lại.

### Bước 2 — Kiểm tra và cài package

Kiểm tra từng package bằng bash, cái nào thiếu thì install luôn.
Thay `python3` bằng `python` nếu đang trên Windows:

```bash
python3 -c "import docx" 2>/dev/null || pip install python-docx --quiet
python3 -c "import openpyxl" 2>/dev/null || pip install openpyxl --quiet
python3 -c "import pdf2docx" 2>/dev/null || pip install pdf2docx --quiet
python3 -c "import underthesea" 2>/dev/null || pip install underthesea --quiet
```

Sau khi chạy xong, xác nhận các package bắt buộc:
```bash
python3 -c "import docx, openpyxl, pdf2docx; print('OK')"
```

Nếu lệnh trên in ra `OK` thì tiếp tục. Nếu lỗi → báo người dùng biết package nào không cài được và lý do (copy nguyên stderr).

Lưu ý:
- `pdf2docx` phụ thuộc vào `PyMuPDF` — lần đầu cài hơi lâu (~2 phút)
- `underthesea` nặng ~500MB lần đầu. Nếu cài thất bại thì cảnh báo rồi tiếp tục — tên người sẽ không được mask nhưng các loại khác vẫn hoạt động

### Bước 3 — Chạy anonymize

Output và mapping lưu vào `tmp/` theo quy định workspace. Tạo thư mục nếu chưa có:
```bash
mkdir -p tmp
```

File `anonymity.py` nằm cùng thư mục với `SKILL.md` này. Xác định đường dẫn bằng cách tìm từ vị trí skill được load:

```bash
# Tìm anonymity.py cùng thư mục với SKILL.md
# Thử workspace-local trước, fallback sang global
SKILL_SCRIPT="$(python3 -c "
import os
candidates = [
    os.path.join(os.getcwd(), '.opencode', 'skills', 'data-anonymity', 'anonymity.py'),
    os.path.expanduser('~/.opencode/skills/data-anonymity/anonymity.py'),
]
found = next((p for p in candidates if os.path.exists(p)), None)
print(found or '')
")"

if [ -z "$SKILL_SCRIPT" ]; then
  echo "Lỗi: không tìm thấy anonymity.py" && exit 1
fi
```

Sau đó chạy:
```bash
python3 "$SKILL_SCRIPT" \
  --input "<đường_dẫn_file>" \
  --output "tmp/<tên_file>_masked.<extension>" \
  --mapping "tmp/<tên_file>_mapping.json"
```

Ví dụ cụ thể:
- Input: `documents/danh_sach_uv.xlsx`
- Output: `tmp/danh_sach_uv_masked.xlsx`
- Mapping: `tmp/danh_sach_uv_mapping.json`

### Bước 4 — Đọc và báo cáo kết quả

```bash
python3 "$SKILL_SCRIPT" --summary "tmp/<tên_file>_mapping.json"
```

Báo cáo cho người dùng:
- Tên file output
- Số lượng từng loại dữ liệu đã mask (phone: N, email: N, name: N...)
- Vị trí file mapping (nhắc người dùng giữ file này để reverse nếu cần)
- KHÔNG hiển thị nội dung mapping (chứa dữ liệu gốc)

### Bước 5 — Tiếp tục xử lý (nếu người dùng yêu cầu)

Nếu người dùng muốn tiếp tục phân tích sau khi mask, hãy làm việc với file output (`_masked`), không bao giờ dùng file gốc.

### Bước 6 — Reverse kết quả AI về dữ liệu gốc (nếu được yêu cầu)

Sau khi AI trả về kết quả phân tích (vẫn chứa token `[TÊN_001]`, `[SĐT_001]`...), dùng `--reverse` để khôi phục:

```bash
python3 "$SKILL_SCRIPT" \
  --input "tmp/<file_kết_quả_AI>.<ext>" \
  --reverse \
  --mapping "tmp/<tên_file_gốc>_mapping.json"
```

Output tạo ra: `tmp/<file_kết_quả_AI>_restored.<ext>`

Lưu ý:
- File mapping phải là file được tạo ra từ lần anonymize trước đó
- Nếu người dùng không còn file mapping → không thể reverse, báo rõ để họ biết
- KHÔNG hiển thị nội dung mapping trong chat

---

## Tùy chọn

| Flag | Mô tả | Mặc định |
|---|---|---|
| `--types` | Loại dữ liệu cần mask, cách nhau bằng dấu phẩy | `all` |
| `--keep-numbers` | Giữ nguyên mọi số, chỉ mask text — dùng cho dữ liệu tài chính | `false` |
| `--reverse` | Reverse file đã mask về dữ liệu gốc, bắt buộc kèm `--mapping` | `false` |
| `--show-mapping` | In mapping table ra terminal (cẩn thận môi trường) | `false` |
| `--no-name` | Bỏ qua nhận diện tên người (nhanh hơn, không cần underthesea) | `false` |

Các giá trị hợp lệ cho `--types`: `phone`, `email`, `cccd`, `account`, `name`, `address`, `salary`

---

## Quy tắc bắt buộc

- **KHÔNG BAO GIỜ** đọc nội dung file gốc vào context trước khi chạy script
- **KHÔNG BAO GIỜ** in ra mapping table trong chat (chứa dữ liệu thực)
- Nếu script báo lỗi, hiển thị stderr nguyên văn để người dùng debug
- Luôn xác nhận với người dùng trước khi ghi đè file (nếu output trùng tên input)
