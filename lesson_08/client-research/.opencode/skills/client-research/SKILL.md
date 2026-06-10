---
name: client-research
description: |
  Load khi người dùng muốn research thông tin khách hàng (client), chuẩn bị cuộc họp, tìm hiểu về công ty đối tác hoặc prospect.
  Trigger: research khách hàng, chuẩn bị họp, tìm hiểu công ty, meeting brief, client brief, thông tin về [tên công ty].
  Yêu cầu: Tavily MCP đã kết nối.
---
# Mục đích

Research thông tin khách hàng từ internet và tổng hợp thành meeting brief 1 trang — đọc được trong 5 phút trước khi vào họp.

# Các bước thực hiện

## Bước 1 - Search thông tin client

- Dùng Tavily MCP tìm kiếm với các query:
  - "[tên công ty] 2026 tin tức"
  - "[tên công ty] quy mô doanh thu"
  - "[tên công ty] đối thủ cạnh tranh"
  - "[ngành của công ty] thách thức 2026"

## Bước 2 - Tổng hợp thông tin

- Tổng hợp brief theo 6 phần:
  (1) Tổng quan: quy mô, ngành, sản phẩm chính
  (2) Tin tức 3 tháng gần nhất
  (3) Đối thủ cạnh tranh chính
  (4) Thách thức ngành hiện tại
  (5) Possible pain points phù hợp với TechCorp (dựa vào `AGENTS.md`)
  (6) 3 conversation starters gợi ý
- Format: tối đa 1 trang A4, gạch đầu dòng ngắn gọn

## Bước 3 - Lưu file

- Tạo file docx, lưu vào thư mục `output/client/meeting-brief_[tên-cty]_[DD-MM-YYYY].docx`
  Ví dụ tên file: `meeting-brief_vinamilk_10-03-2026.docx`

## Quy tắc

- Mỗi điểm thông tin phải có nguồn URL kèm theo
- Không đưa ra nhận xét chủ quan về triển vọng deal
- Pain points: chỉ đề xuất những cái liên quan đến sản phẩm TechCorp
