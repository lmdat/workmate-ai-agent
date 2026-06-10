---
name: contract-triage
description: |
  Load khi người dùng muốn review, tóm tắt, đánh giá hợp đồng, NDA, thỏa thuận.
  Trigger: review hợp đồng, tóm tắt NDA, kiểm tra điều khoản, triage contract,
  hợp đồng có gì bất thường, điều khoản rủi ro, contract review.
---
 
## Các bước thực hiện
1. Đọc toàn bộ nội dung file hợp đồng

2. Tóm tắt 5 phần:
   (1) Loại hợp đồng và các bên liên quan
   (2) Đối tượng và phạm vi dịch vụ/thỏa thuận
   (3) Giá trị tài chính và lịch thanh toán
   (4) Thời hạn và điều kiện chấm dứt
   (5) Điều khoản đặc biệt cần chú ý

3. Bảng Risk Flags:
   Với mỗi điểm bất thường: Mức độ (CAO/TRUNG BÌNH/THẤP) | Điều khoản | Đề xuất xử lý
   So sánh với ngưỡng rủi ro trong `AGENTS.md`

4. Kết luận: Mức độ ưu tiên review (Cao/Trung bình/Thấp) + lý do

5. Lưu file docx vào `output/contract-review/review_[tên file]_[DD-MM-YYYY].docx`

6. Hoàn thành khi — và chỉ khi
- Liệt kê `output/` và xác nhận thấy đủ các file sau:
   - `output/contract-review/review_[tên file]_[DD-MM-YYYY].docx`
- Nếu thiếu bất kỳ file nào → chưa hoàn thành, tiếp tục tạo file còn thiếu.
- Không được báo "đã xong" khi chưa pass bước kiểm tra này.
 
## Quy tắc
- Ngôn ngữ tóm tắt: tiếng Việt (có dấu) đơn giản, không dùng legalese
- Nếu không rõ điều khoản: ghi "Cần làm rõ: [câu hỏi cụ thể]"
- Không đưa ra khuyến nghị ký hay không ký
- Tag [LUẬT SƯ REVIEW] nếu có bất kỳ rủi ro CAO nào
