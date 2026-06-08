---
name: monthly-summary
description: |
  Load skill này khi người dùng muốn tổng hợp báo cáo tháng, báo cáo phòng ban,
  tạo executive summary, tóm tắt cho BGĐ hoặc Ban Giám Đốc.
  Trigger khi nhắc đến: tổng hợp báo cáo tháng, executive summary, tóm tắt cho BGĐ,
  báo cáo phòng ban, monthly report, tổng hợp kết quả tháng.
---

## Mục đích
Đọc báo cáo từ nhiều phòng ban, tổng hợp thành Executive Summary để trình BGĐ.

## ⛔ PRECONDITION — Bắt buộc kiểm tra

Kiểm tra thư mục `tmp/` xem đã có file nào tên bắt đầu bằng `masked_` tương ứng với những file trong `input/report/` theo tháng-năm cần dùng làm report chưa.

- Nếu **đã có** → thực hiện bước 1 và ghi đè lại file, chuyển thẳng sang bước 2
- Nếu **chưa có** → thực hiện bước 1 trước, **không được đọc file trong `input/report/`**, sau đó chuyển thẳng sang bước 2.


## Các bước thực hiện

### Bước 1 — Anonymize file báo cáo

Dùng skill `@data-anonymity` với flag `--keep-number` để anonymize toàn bộ file trong `input/report/` theo tháng-năm cần dùng làm report.

- Output (file đã mask) lưu vào `tmp/`, tên format: `masked_{tên_file_gốc}`
- Mapping file lưu vào `tmp/`, tên format: `masked_{tên_file_gốc}_mapping.json`

Sau khi chạy xong, kiểm tra lại `tmp/` để xác nhận đã có file masked.
Nếu `tmp/` vẫn trống → báo lỗi cho người dùng, dừng lại, không tiếp tục.

### Bước 2: Đọc báo cáo phòng ban
- Liệt kê tất cả file `masked_*` trong `tmp/` tương ứng với tháng-năm cần tổng hợp.
- Đối chiếu với danh sách phòng ban trong `AGENTS.md`. Ghi nhận: bao nhiêu phòng ban, có thiếu phòng nào không

### Bước 3: Tổng hợp số liệu
Đọc từng file báo cáo đã masked, extract:
   - Tên phòng ban
   - KPI/doanh thu thực tế vs kế hoạch (nếu có)
   - Vấn đề tồn đọng và mức độ nghiêm trọng
   - Hành động cần làm / cần CEO quyết định

### Bước 4: Viết Executive Summary
- **Section 1 — Doanh thu vs kế hoạch:**
  Bảng: Chỉ tiêu | Thực tế | Kế hoạch | % đạt | So tháng trước
  Kèm emoji status: 🔴🟡🟢 theo ngưỡng `AGENTS.md`

- **Section 2 — Chi phí vs ngân sách:**
  Bảng: Danh mục chi phí | Thực tế | Ngân sách | % sử dụng
  Highlight overspend (> 100% ngân sách).

- **Section 3 — Top 3 vấn đề cần BGĐ quyết định:**
  Mỗi vấn đề: mô tả 1 câu + ảnh hưởng + option A/B/C
  Chỉ nêu vấn đề CẦN quyết định — không nêu vấn đề đang xử lý được.

- **Section 4 — Đề xuất hành động tháng tới:**
  Tối đa 5 bullet. Cụ thể, có số liệu, có người chịu trách nhiệm.
  VD: "Sales: tăng 15% quota cho 3 rep đang overperform (Sales Manager)"

### Bước 5 — Revert tên thật cho TẤT CẢ báo cáo
- Dùng skill `data-anonymity` với flag `--reverse`  để revert token về tên thật.
- Không được chuyển sang bước 6 khi kết quả còn chứa token anonymize.

### Bước 6: Lưu báo cáo
- Lưu vào `output/monthly_summary_[thang]-[nam].docx`
Ví dụ: `output/monthly_summary_02-2026.docx`

