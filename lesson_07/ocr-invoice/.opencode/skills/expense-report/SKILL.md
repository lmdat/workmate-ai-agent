---
name: expense-report
description: |
  Load skill này khi người dùng muốn tổng hợp hóa đơn, chi phí, expense report,
  báo cáo chi phí, quyết toán chi phí.
  Trigger khi nhắc đến: hóa đơn, invoice, expense, chi phí tháng, tổng hợp hóa đơn, đọc hóa đơn, extract invoice, expense report, quyết toán.
permission:
	websearch:	deny
---
## Mục đích

Đọc ảnh hóa đơn, extract thông tin, xử lý quy đổi tỷ giá (nếu có USD), và tổng hợp vào expense report theo template.


## Các bước thực hiện — LUÔN thực hiện 2 bước tách biệt

### BƯỚC 1 — Extract & Preview (DỪNG để review trước)

Gọi Agent `@data-extractor` để đọc tất cả file trong `input/invoice/`, extract thông tin cần thiết, và tạo file `output/raw-data-[today].xlsx` để người dùng review trước khi sang Bước 2. Cụ thể:

1. List tất cả file trong `input/invoice/`

2. Đọc từng file ảnh, extract:
   - Nhà cung cấp (Vendor)
   - Ngày hóa đơn
   - Loại chi phí (tự phân loại: Văn phòng phẩm / Dịch vụ / Tiếp khách / SaaS / Cloud / Khác)
   - Số tiền và đơn vị (VNĐ hoặc USD):
     - Sub total
     - VAT (nếu có)
     - Total (Tổng cộng)
3. Với hóa đơn USD:
   - Dùng Chrome DevTools mở link: https://acb.com.vn/ty-gia-hoi-doai
   - Lấy tỷ giá bán (selling rate) — ghi rõ tỷ giá và ngày lấy
   - Tính quy đổi VNĐ = USD × tỷ giá
   - Ghi cả 2 cột: Ngoại tệ (USD) | Quy đổi VNĐ
4. Tạo `output/raw-data-[today theo dịnh dạng yyyy-mm-dd].xlsx` với 7 cột:
   Nhà cung cấp | Ngày | Loại chi phí | Ngoại tệ | Tỷ giá | Quy đổi VNĐ | VAT
5. DỪNG và thông báo: "Đã extract xong. Vui lòng review `output/raw-data-[today theo dịnh dạng yyyy-mm-dd].xlsx` trước khi sang Bước 2."

### BƯỚC 2 — Tạo Expense Report (chỉ chạy sau khi nhận lệnh tiếp theo)

Gọi Agent `@report-writer` để tổng hợp data đã review vào template `templates/expense-template.xlsx` (nếu không có thì tạo mới theo cấu trúc đã mô tả), và lưu ra `output/expense-report-[yyyy-mm-dd].xlsx`. Cụ thể:

1. Đọc `output/raw-data-[today theo dịnh dạng yyyy-mm-dd].xlsx` đã được review
2. Điền vào `templates/expense-template.xlsx` (nếu không có file mẫu thì tạo mới theo cấu trúc sau):
   - Tổng theo từng loại chi phí
   - Subtotal VNĐ và Subtotal USD (kèm tỷ giá áp dụng)
   - Grand total quy về VNĐ
   - Ghi chú: các hóa đơn cần xác nhận thêm (nếu có)
3. Lưu ra `output/expense-report-[yyyy-mm-dd].xlsx`

## Quy tắc

- KHÔNG bỏ qua Bước 1 dù người dùng yêu cầu làm 1 lần
- Số tiền không rõ ràng trong ảnh: ghi "KHÔNG RÕ — cần kiểm tra thủ công"
- Không tự điền số liệu còn thiếu — ghi N/A
- Tỷ giá USD: bắt buộc ghi nguồn (ACB) và ngày lấy
