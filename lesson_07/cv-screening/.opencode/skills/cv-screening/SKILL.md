---
name: cv-screening
description: |
  Load skill này khi người dùng muốn sàng lọc, đánh giá, review CV hoặc hồ sơ ứng viên.
  Trigger khi nhắc đến: sàng lọc CV, đọc CV, lọc ứng viên, review hồ sơ,
  shortlist, đánh giá ứng viên, screen CV, xem CV, CV nào phù hợp,
  ứng viên nào pass, lọc theo tiêu chí.
---

# CV Screener Skill

## Mục đích
- Đọc và đánh giá CV hàng loạt theo tiêu chí tuyển dụng trong AGENTS.md.
- Tạo shortlist và email mời phỏng vấn cho ứng viên Pass.

---

## Bước 0 — Tạo plan và chờ xác nhận

Trình bày plan cho người dùng theo đúng format sau, không được bỏ qua:

---
**Plan xử lý CV**
- Số file CV: [liệt kê tên file trong `input/cv/`]
- Thư mục làm việc: `tmp/` (masked), `output/` (kết quả)
- File output dự kiến: `output/shortlist_{ngày}.xlsx`, `output/interview_emails_{ngày}.txt`

**Checklist:**
- [ ] Anonymize toàn bộ CV → lưu vào `tmp/`
- [ ] Liệt kê và kiểm tra file masked
- [ ] Extract 5 trường thông tin từng CV
- [ ] Chấm điểm theo tiêu chí trong AGENTS.md
- [ ] Revert tên thật cho TẤT CẢ ứng viên (Pass + Fail)
- [ ] Tạo shortlist Excel đầy đủ tất cả ứng viên
- [ ] Viết email cho ứng viên điểm ≥ 7
---

Sau đó hỏi người dùng: **"Anh/chị có muốn em bắt đầu không?"**

Dừng lại và chờ phản hồi. Chỉ tiếp tục khi người dùng xác nhận. Không tự động chuyển sang bước tiếp theo.

---

## ⛔ PRECONDITION — Bắt buộc kiểm tra sau khi đã có plan

Kiểm tra thư mục `tmp/` xem đã có file nào tên bắt đầu bằng `masked_` tương ứng với những file trong `input/cv/` chưa.

- Nếu **đã có** → bỏ qua bước 1, chuyển thẳng sang bước 2
- Nếu **chưa có** → thực hiện bước 1 trước, **không được đọc file trong `input/cv/`**

---

## Các bước thực hiện

### Bước 1 — Anonymize file CV

Dùng skill `data-anonymity` để anonymize toàn bộ file trong `input/cv/`.

- Output (file đã mask) lưu vào `tmp/`, tên format: `masked_{tên_file_gốc}`
- Mapping file lưu vào `tmp/`, tên format: `masked_{tên_file_gốc}_mapping.json`

Sau khi chạy xong, kiểm tra lại `tmp/` để xác nhận đã có file masked.
Nếu `tmp/` vẫn trống → báo lỗi cho người dùng, dừng lại, không tiếp tục.

### Bước 2 — Liệt kê file

Liệt kê tất cả file `masked_*` trong `tmp/`.
Ghi nhận: tổng số file, định dạng (PDF/DOCX/khác).
Nếu có định dạng không đọc được: ghi chú tên file, tiếp tục với các file còn lại.

### Bước 3 — Extract thông tin từng CV

Với mỗi file `masked_*` trong `tmp/`, extract 5 trường:
- Họ tên ứng viên
- Số năm kinh nghiệm liên quan
- Kỹ năng chính (tối đa 5)
- Vị trí gần nhất + tên công ty
- Học vấn cao nhất

### Bước 4 — Đánh giá

- So khớp với tiêu chí vị trí trong `AGENTS.md`.
- Cho điểm 1–10 theo thang điểm trong `AGENTS.md`.
- Ghi rõ: điểm mạnh (khớp gì), điểm yếu (thiếu gì). Dẫn chứng cụ thể từ CV.

### Bước 5 — Revert tên thật cho TẤT CẢ ứng viên

Dùng skill `data-anonymity` với flag `--reverse` để revert token về tên thật.

**Quan trọng: revert toàn bộ ứng viên — cả Pass lẫn Fail — không bỏ sót ai.**

Lý do: shortlist Excel cần hiển thị đầy đủ tất cả ứng viên (có cột kết quả Pass/Fail), không chỉ riêng ứng viên Pass.

Không được chuyển sang bước 6 khi kết quả còn chứa token `[TÊN_XXX]`, `[SĐT_XXX]`...

### Bước 6 — Tạo shortlist Excel

Tạo file Excel: `output/shortlist_{YYYY-MM-DD}.xlsx`

File bao gồm **tất cả ứng viên**, có cột Pass/Fail để phân biệt.

### Bước 7 — Viết email mời phỏng vấn

Tạo file txt: `output/interview_emails_{YYYY-MM-DD}.txt`
Chỉ viết email cho ứng viên điểm ≥ 7.
Mỗi email có: Subject, Body (50–80 từ), gợi ý 3 khung thời gian.
Subject chuẩn: "[Tên công ty] — Thư mời phỏng vấn — [Vị trí]"