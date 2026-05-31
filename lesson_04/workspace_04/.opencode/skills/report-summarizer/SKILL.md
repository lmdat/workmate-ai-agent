---
name: report-summarizer
description: |
  Load skill này khi người dùng muốn tóm tắt, tổng hợp, hoặc đọc hiểu nội dung báo cáo.
  Trigger khi nhắc đến: tóm tắt báo cáo, summarize report, tổng hợp file,
  đọc báo cáo, xem báo cáo, review report, tóm tắt nội dung, điểm chính là gì,
  báo cáo nói gì, rút ra điểm chính.
---

## Mục đích
Đọc và tóm tắt nội dung báo cáo thành dạng dễ đọc, đúng format theo AGENTS.md.

## Các bước thực hiện

1. Đọc toàn bộ nội dung file được chỉ định qua đường dẫn cụ thể mà user cung cấp

2. Xác định các phần chính của báo cáo:
   - Kết quả / số liệu quan trọng nhất
   - Vấn đề hoặc rủi ro nếu có
   - Kế hoạch hoặc hành động tiếp theo

3. Tạo tóm tắt theo format sau:
   - Dòng tiêu đề: tên báo cáo + thời gian
   - Bảng 3 cột: Chủ đề | Điểm chính | Số liệu/Chi tiết
   - Mỗi chủ đề tối đa 2 dòng trong bảng
   - Tổng số hàng: không quá 8

4. Lưu kết quả vào output/summary-[tên file gốc].txt
   (nếu người dùng không chỉ định file output cụ thể)

## Quy tắc
- Ngôn ngữ: giữ nguyên ngôn ngữ của file gốc (tiếng Việt → tiếng Việt)
- Không tự thêm nhận xét chủ quan — chỉ tóm tắt những gì có trong file
- Nếu file có nhiều phần, ưu tiên phần kết quả và vấn đề tồn đọng
- Nếu không đọc được file: thông báo rõ lỗi, không tự đoán nội dung
