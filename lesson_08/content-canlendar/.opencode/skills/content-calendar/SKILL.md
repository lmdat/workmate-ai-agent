---
name: content-calendar
description: Tạo content calendar cho nhiều channels. Trigger khi người dùng yêu cầu "content calendar", "lịch đăng bài", "kế hoạch content", "content tháng".
---

## Workflow thực hiện

### Bước 1 — Phân tích brief
- Đọc brand voice: nếu trong thư mục `input/brief/` có file nào tên chứa "Brand Voice" hoặc "Tone", đọc kỹ để nắm rõ tone giọng chung và tone theo từng channel. Nếu không có, thì dùng brand voice chung đã có trong `AGENTS.md`.
- Đọc brief chiến dịch trong prompt (nếu có thì ưu tiên). Nếu trong prompt không có brief thì hãy đọc nội dung file docx trong thư mục `input/brief/` mà tên file có chữ "Brief" hoặc "Campaign". Xác định các thông tin sau:
    Mục tiêu chính của chiến dịch
    Sản phẩm/dịch vụ được quảng bá
    Target audience (độ tuổi, giới tính, sở thích, pain points)
    Sự kiện đặc biệt (nếu có)
    Tone giọng chung và tone theo từng channel (nếu có)

### Bước 2 — Xây dựng content framework
- Phân bổ 4 tuần theo nguyên tắc:
  - Tuần 1: Awareness — giới thiệu, tạo tò mò
  - Tuần 2: Education — giải thích giá trị, how-it-works
  - Tuần 3: Consideration — social proof, so sánh, FAQ
  - Tuần 4: Conversion — CTA mạnh, urgency, last call
- Sự kiện đặc biệt: ưu tiên đặt vào tuần gần nhất và cover 2–3 posts.


### Bước 3 — Tạo từng post
- Với mỗi post điền đủ 7 cột:
  - Cột 1 — Ngày đăng  : phân bổ đều, tránh 2 channels cùng ngày
  - Cột 2 — Channel    : Facebook / Email / LinkedIn
  - Cột 3 — Chủ đề     : tiêu đề ngắn 5–8 từ
  - Cột 4 — Caption    : 50–100 từ, đúng tone từng channel theo AGENTS.md
  - Cột 5 — Visual     : mô tả ảnh/video cần thiết (1–2 câu)
  - Cột 6 — Hashtag    : FB ≤ 10 tags, IG ≤ 20 tags, LinkedIn ≤ 5 tags
  - Cột 7 — Status     : để trống (team điền sau)

### Bước 4 — Kiểm tra và lưu file
Lưu file excel vào thư mục `output/content-calendar` với tên file format: `content_calendar_{MM-YYYY}.xlsx`
Ví dụ tên file: `content_calendar_02-2026.xlsx`

## Checklist
- [ ] Mỗi channel đủ 4 posts/tuần × 4 tuần = 16 posts
- [ ] Không có 2 posts cùng channel cùng ngày
- [ ] Caption Facebook có emoji, LinkedIn không có emoji
- [ ] Sự kiện đặc biệt đã được cover
- [ ] Caption đã dùng brand voice từ AGENTS.md (không có từ bị cấm)
- [ ] Tên file đúng format và lưu đúng thư mục