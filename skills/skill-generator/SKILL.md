---
name: skill-generator
description: >
  Tạo Skill mới hoàn chỉnh từ mô tả tiếng Việt thông thường.
  Dùng khi người dùng muốn đóng gói một quy trình làm việc thành Skill
  để tái sử dụng nhiều lần — ví dụ: "tạo skill viết báo cáo",
  "tạo skill format hóa đơn", "đóng gói quy trình này thành skill".
  Skill sẽ hỏi thêm nếu cần, rồi tạo file .opencode/skills/[tên-skill]/SKILL.md đầy đủ.

  Gọi Skill này khi người dùng:
  - Nói "tạo skill [mô tả]"
  - Nói "đóng gói quy trình này thành skill"
  - Nói "tôi muốn tái sử dụng cái này → tạo skill"
  - Hỏi "làm sao tạo skill [...]"

  KHÔNG gọi Skill này khi:
  - Người dùng muốn tạo Agent (dùng /agent-generator)
  - Người dùng muốn chỉnh sửa Skill có sẵn (str_replace trực tiếp)
  - Người dùng muốn CHẠY một quy trình (thực thi ngay, không cần đóng gói)

  Phân biệt Skill vs Agent:
  - Skill = công cụ tái sử dụng, dạy AI "làm thế nào" (cách format, cách viết, cách xử lý)
  - Agent = trợ lý có vai trò cụ thể, dạy AI "là ai và làm gì" (cv-screener, report-builder)
  - Nếu người dùng mô tả một "trợ lý" hoặc "vai trò" → gợi ý dùng /agent-generator thay thế
---

# Skill Generator

## Mô tả
Nhận mô tả quy trình bằng tiếng Việt thông thường từ người dùng,
tự động tạo file Skill hoàn chỉnh theo đúng cấu trúc OpenCode
và lưu vào `.opencode/skills/[tên-skill]/SKILL.md`.

---

## Sự khác biệt cốt lõi: Skill vs Agent

Trước khi tạo, xác định rõ người dùng cần cái gì:

| | Skill | Agent |
|---|---|---|
| **Là gì** | Công cụ — dạy AI cách làm | Trợ lý — AI đóng vai cụ thể |
| **Dùng khi** | Có quy trình lặp lại cần chuẩn hóa | Cần AI xử lý end-to-end một tác vụ |
| **Ví dụ** | skill format-report, skill clean-data | agent cv-screener, agent report-builder |
| **Trigger** | Được gọi trong prompt của Agent hoặc người dùng | Chạy độc lập khi được mention |
| **Phạm vi** | Hẹp — 1 kỹ năng cụ thể | Rộng — toàn bộ workflow |

**Nếu người dùng mô tả một "trợ lý" hoặc "vai trò"** → hỏi lại:
"Anh/chị muốn tạo Skill (công cụ tái sử dụng) hay Agent (trợ lý có vai trò)?
Nếu cần Agent, dùng @create-agent sẽ phù hợp hơn."

---

## Quy trình xử lý

### Bước 1 — Phân tích mô tả
Từ input của người dùng, xác định:

- **Tên skill**: động từ + danh từ, chữ thường, dấu gạch ngang
  (ví dụ: `format-report`, `clean-data`, `write-email`, `extract-table`)
- **Mục đích**: skill này dạy AI làm gì cụ thể?
- **Input**: nhận loại dữ liệu/file gì?
- **Output**: tạo ra gì, format nào?
- **Quy tắc**: những rule cụ thể cần follow
- **Ví dụ**: có thể lấy từ mô tả của người dùng không?

### Bước 2 — Hỏi thêm (tối đa 3 câu, chỉ khi thiếu)
Hỏi khi không thể tự suy ra:
- Output format không rõ (text? Excel? Markdown? Word?)
- Tiêu chí chất lượng không rõ (viết cho ai đọc? tone thế nào?)
- Scope không rõ (xử lý 1 file hay nhiều file?)

Không hỏi khi đủ thông tin để tạo Skill hoạt động được.

### Bước 3 — Tạo file Skill
Tạo `.opencode/skills/[tên-skill]/SKILL.md` với cấu trúc đầy đủ.

### Bước 4 — Tóm tắt
Sau khi tạo xong, in:
```
✅ Đã tạo: .opencode/skills/[tên-skill]/SKILL.md

Dùng Skill này trong prompt:
  "Xử lý @Input/file.txt theo /[tên-skill]"
  "Dùng @[tên-skill] để format file này"

Hoặc gọi trong Agent khác:
  Thêm "Dùng skill /[tên-skill] để [bước cụ thể]" vào Agent file.

Muốn chỉnh sửa? Mở file và sửa trực tiếp.
```

---

## Cấu trúc file Skill output

```markdown
---
name: [tên-skill]
description: >
  [2–3 câu mô tả Skill làm gì và khi nào dùng.
  Viết "pushy" — nêu rõ trigger conditions để OpenCode tự chọn đúng Skill.
  Ví dụ: "Dùng khi người dùng cần format báo cáo, chuẩn hóa số liệu,
  hoặc xuất dữ liệu thành bảng — kể cả khi không nói rõ 'dùng skill này'."]

  - Gọi Skill này khi: [liệt kê trigger phrases]
  - KHÔNG gọi khi: [liệt kê exclusions để tránh nhầm]
  - Cách gọi mẫu:
		[ví dụ prompt 1]
		[ví dụ prompt 2]
  - input: "[mô tả input ngắn gọn]"
  - output: "[mô tả output ngắn gọn]"
---

# [Tên Skill đầy đủ]

## Mục đích
[1–2 câu: Skill này dạy AI làm gì, dùng trong tình huống nào.
Khác với Agent — không cần "đóng vai", chỉ cần mô tả kỹ năng.]

## Input
[Mô tả rõ:
- Loại dữ liệu/file nhận vào
- Format được chấp nhận
- Có thể là 1 hay nhiều đơn vị]

## Output
[Mô tả rõ:
- Tên file / format
- Cấu trúc chi tiết (tên cột, số phần, thứ tự)]

## Quy tắc thực thi

[Liệt kê các rule dưới dạng hành động cụ thể — không phải mong muốn chung chung.
SAI: "Đảm bảo chính xác"
ĐÚNG: "Số liệu lấy nguyên từ file, không làm tròn, không ước tính"]

### Xử lý dữ liệu đầu vào
[Quy tắc đọc, validate, xử lý thiếu/mâu thuẫn]

### Tạo output
[Quy tắc format, style, những gì bắt buộc / không được có]

## Ví dụ

### Ví dụ tốt ✅
Input: [mô tả input ngắn]
Output đúng:
[ví dụ output cụ thể — dùng số liệu/tên giả lập thật, không dùng placeholder]

### Ví dụ hay sai ❌
Input: [mô tả input]
Output SAI:
[ví dụ output sai]
→ Lý do sai: [giải thích ngắn]
Output ĐÚNG phải là:
[ví dụ output đúng]

## Xử lý trường hợp bất thường
[Ít nhất 2 edge case + cách xử lý:
- Nếu [condition] → [action cụ thể]
- Nếu [condition] → [action cụ thể]]

## Không được làm
[3–5 rule negative — những gì Skill không được tự ý làm]
```

---

## Quy tắc viết Skill chất lượng cao

### Tên Skill
- Dùng gerund hoặc động từ: `format-report` ✅ | `report-formatter` ❌
- Chữ thường, dấu gạch ngang, không dấu tiếng Việt
- Mô tả hành động, không mô tả đối tượng

### Description — viết "pushy"
Description trong YAML frontmatter phải đủ mạnh để OpenCode tự chọn Skill đúng.
Không chỉ mô tả "skill làm gì" — mà còn nêu rõ "khi nào dùng":

SAI: `"Format báo cáo tài chính"`
ĐÚNG: `"Format báo cáo tài chính thành bảng chuẩn. Dùng khi người dùng
cần chuẩn hóa số liệu, xuất ra bảng, hoặc format lại dữ liệu thô —
kể cả khi không nói rõ 'dùng skill format'."`

### Quy tắc thực thi
- Viết dưới dạng hành động, không dưới dạng mong muốn
- Mỗi rule phải đủ cụ thể để AI biết CHÍNH XÁC phải làm gì
- Luôn có rule xử lý khi thiếu thông tin: "Nếu X không có → ghi 'N/A', không tự điền"

### Ví dụ (few-shot)
- Phải có ít nhất 1 ví dụ SAI kèm lý do — AI học từ phản ví dụ hiệu quả hơn
- Dùng số liệu và tên giả lập cụ thể, không dùng `[tên]`, `[số]`
- Ví dụ phải dùng đúng tên field/cột xuất hiện trong output thật

### Edge cases
- Bắt buộc cover: input rỗng, input thiếu trường quan trọng, format không đúng dự kiến
- Mỗi edge case: trigger condition + hành động cụ thể (không phải "xử lý linh hoạt")

### Scope
- 1 Skill = 1 kỹ năng — không nhét nhiều tác vụ không liên quan vào cùng 1 Skill
- Nếu người dùng mô tả quy trình 3–4 bước khác nhau → tách thành nhiều Skill
  hoặc đề xuất dùng Agent thay vì Skill

---

## Few-shot ví dụ của Skill này

### Ví dụ 1 — Input đủ thông tin, generate ngay

**Input từ người dùng:**
"Tạo skill format dữ liệu bán hàng thô thành bảng Excel chuẩn —
cột: Ngày, Mã đơn, Khách hàng, Sản phẩm, Số lượng, Doanh thu.
Dữ liệu thô từ nhiều nguồn, format khác nhau."

**Skill không hỏi thêm** — đủ thông tin → generate ngay `format-sales-data.md`

**Output tạo ra:**
```
.opencode/skills/format-sales-data/SKILL.md

---
name: format-sales-data
description: >
  Chuẩn hóa dữ liệu bán hàng thô từ nhiều nguồn thành bảng Excel
  6 cột chuẩn. Dùng khi người dùng cần clean data, chuẩn hóa bảng,
  hoặc merge dữ liệu từ nhiều file — kể cả khi không nói rõ 'dùng skill này'.
---
[...nội dung đầy đủ...]
```

---

### Ví dụ 2 — Input mơ hồ, cần hỏi thêm

**Input từ người dùng:**
"Tạo skill viết báo cáo"

**Skill hỏi thêm (2 câu):**
1. "Báo cáo loại gì? (tài chính, vận hành, nhân sự, hay loại khác?)"
2. "Output format anh/chị cần là gì? (Word, Markdown, text thuần, hay Excel?)"

→ Sau khi người dùng trả lời → generate Skill phù hợp.

---

### Ví dụ 3 — Nhầm với Agent, cần gợi ý đúng

**Input từ người dùng:**
"Tạo skill là một HR analyst đọc CV và chấm điểm ứng viên"

**Skill nhận ra đây là Agent, không phải Skill:**
"Mô tả này phù hợp với Agent hơn là Skill —
vì anh/chị cần AI đóng vai HR Analyst và xử lý end-to-end.

Gợi ý: dùng `@create-agent` với mô tả tương tự.
Nếu anh/chị vẫn muốn tạo Skill (ví dụ: chỉ cần kỹ năng 'chấm điểm CV'
để dùng trong một Agent khác), tôi có thể tạo skill `score-cv` cho anh/chị."

---

## Bảng lỗi thường gặp khi tạo Skill

| Lỗi | Nguyên nhân | Fix |
|---|---|---|
| Skill không được tự động chọn | Description quá ngắn, thiếu trigger conditions | Viết description "pushy" — thêm "Dùng khi..." |
| AI không follow Skill đúng | Quy tắc viết dạng mong muốn, không phải hành động | Đổi "hãy chính xác" → "số liệu lấy nguyên từ file, không làm tròn" |
| Output sai format | Schema output không có tên cột / số sheet cụ thể | Định nghĩa tên cột, kiểu dữ liệu, thứ tự |
| Skill và Agent bị nhầm | Người dùng mô tả "vai trò" thay vì "kỹ năng" | Hỏi lại + gợi ý dùng @create-agent nếu phù hợp hơn |
| Few-shot dùng placeholder | Ví dụ không đủ cụ thể để AI học | Dùng tên/số giả lập thật, không dùng [tên], [số] |
| 1 Skill quá nhiều tác vụ | Nhét nhiều kỹ năng không liên quan | Tách thành nhiều Skill, mỗi Skill 1 kỹ năng |
