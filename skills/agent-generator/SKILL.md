---
name: agent-generator
description: >
  Tạo Custom Agent hoàn chỉnh từ mô tả tiếng Việt thông thường.
  Dùng khi người dùng muốn xây Agent mới cho một tác vụ cụ thể —
  ví dụ: "tạo agent đọc CV", "tạo agent tổng hợp báo cáo".
  Skill sẽ hỏi thêm nếu cần, rồi generate file .opencode/agents/[tên-agent].md đầy đủ.
usage: |
  Gọi Skill này khi người dùng:
  - Nói "tạo agent [mô tả]"
  - Nói "tôi cần agent [làm gì đó]"
  - Nói "build agent cho [tác vụ]"
  - Hỏi "làm sao tạo agent [...]"
 
  KHÔNG gọi Skill này khi:
  - Người dùng muốn CHỈNH SỬA agent có sẵn (dùng str_replace trực tiếp)
  - Người dùng muốn CHẠY agent (dùng /agent hoặc mention @agent)
  - Người dùng hỏi về lý thuyết Agent mà không muốn tạo file
---

# Agent Generator

## Mô tả
Nhận mô tả bằng tiếng Việt thông thường từ người dùng,
tự động tạo file Custom Agent hoàn chỉnh theo đúng cấu trúc OpenCode
và lưu vào `.opencode/agents/[tên-agent].md`.

---

## Input

Người dùng mô tả Agent cần tạo. Có thể là:
- 1 câu: "Tạo agent đọc CV và chấm điểm theo JD"
- Vài câu: "Tôi cần agent tổng hợp báo cáo tháng từ nhiều phòng ban,
  output ra Excel 2 sheet, highlight phòng nào cần CEO xem."
- Có hoặc không có thông tin về input/output cụ thể

Nếu thông tin chưa đủ để tạo Agent chất lượng cao →
hỏi thêm tối đa 3 câu trước khi generate.

---

## Quy trình xử lý

### Bước 1 — Phân tích mô tả
Từ input của người dùng, xác định:
- **Tên agent**: danh từ ngắn, chữ thường, dùng dấu gạch ngang
  (ví dụ: `cv-screener`, `report-builder`, `vendor-analyzer`)
- **Vai trò**: AI đóng vai ai? Chuyên gia gì?
- **Input files**: loại file nào, ở đâu, bao nhiêu
- **Output files**: tên file, format, cấu trúc
- **Quy tắc xử lý**: những logic đặc thù cần định nghĩa
- **Edge cases**: tình huống bất thường có thể xảy ra

### Bước 2 — Hỏi thêm (chỉ khi thiếu thông tin quan trọng)
Hỏi tối đa 3 câu, mỗi câu 1 dòng. Không hỏi những gì có thể tự suy ra.

Hỏi khi thiếu:
- Không rõ output format (Excel? Markdown? Word? Chỉ text?)
- Không rõ tiêu chí đánh giá/phân loại (nếu agent cần chấm điểm hay lọc)
- Không rõ người dùng cuối là ai (ảnh hưởng đến tone và độ chi tiết của output)

Không hỏi khi:
- Có thể dùng best practice mặc định
- Thông tin đủ để generate agent hoạt động được

### Bước 3 — Generate file Agent
Tạo file `.opencode/agents/[tên-agent].md` với cấu trúc đầy đủ bên dưới.

### Bước 4 — Tóm tắt sau khi tạo
Sau khi tạo file xong, in ra:
```
✅ Đã tạo: .opencode/agents/[tên-agent].md

Dùng Agent này bằng lệnh:
  /agent [tên-agent]

Hoặc mention trong prompt:
  "Xử lý @Input/... theo @[tên-agent]"

Muốn chỉnh sửa Agent? Mở file và sửa trực tiếp.
```

---

## Cấu trúc file Agent output

```markdown
---
name: [tên-agent]
description: [2-3 câu mô tả ngắn gọn — dùng khi OpenCode tự chọn agent]
---

# [Tên Agent đầy đủ]

## Vai trò
[Mô tả AI đóng vai ai, phục vụ ai, mục tiêu là gì.
2–4 câu. Bao gồm: người đọc output là ai và họ cần gì.]

## Input
[Liệt kê rõ:
- Loại file nào, đường dẫn nào
- Có thể có bao nhiêu file
- File có thể ở format nào]

## Output
[Liệt kê rõ từng file output:
- Tên file
- Format
- Cấu trúc chi tiết (số cột, tên cột, số sheet, v.v.)]

## Quy tắc xử lý

### Đọc input
[Quy tắc đọc file — đọc toàn bộ hay chỉ phần nào,
xử lý file thiếu thông tin thế nào]

### Xử lý dữ liệu
[Logic chính — tiêu chí, thang điểm, phân loại, tính toán]

### Viết output
[Format, style, những gì bắt buộc có / không được có]

## Few-shot ví dụ

### Ví dụ 1 — [Tên tình huống điển hình] ✅
Input: [mô tả ngắn input]
Output đúng:
[ví dụ output cụ thể]

### Ví dụ 2 — [Tình huống hay sai] ❌
Input: [mô tả input]
Output SAI:
[ví dụ output sai]
→ Lý do sai: [giải thích]
Output ĐÚNG phải là:
[ví dụ output đúng]

## Edge cases
[Ít nhất 2 tình huống bất thường + cách xử lý cụ thể]

## Không được làm
[3–5 rule negative]
```

---

## Quy tắc viết Agent chất lượng cao

### Tên agent
- Ngắn, mô tả chức năng: `cv-screener` ✅ | `my-agent` ❌
- Chữ thường, dấu gạch ngang, không dấu tiếng Việt
- Không quá 3 từ

### Vai trò
- Luôn có: AI đóng vai gì + phục vụ ai + output phục vụ mục đích gì
- SAI: "Bạn là trợ lý AI giúp người dùng."
- ĐÚNG: "Bạn là HR Analyst. Nhiệm vụ: đọc CV ứng viên, chấm điểm theo tiêu chí trong JD,
  và tạo bảng shortlist để HR Manager ra quyết định trong 5 phút."

### Quy tắc xử lý
- Phải có rule cho trường hợp thiếu thông tin:
  "Nếu field X không có trong file → ghi 'N/A', KHÔNG tự điền"
- Phải có rule cho trường hợp mâu thuẫn:
  "Nếu 2 file cho thông tin khác nhau → ghi cả 2, thêm ghi chú ⚠️"

### Few-shot
- Bắt buộc có ít nhất 1 ví dụ SAI với lý do giải thích
- Ví dụ phải dùng đúng tên field/cột sẽ xuất hiện trong output thật
- Không dùng placeholder như "[tên ứng viên]" trong ví dụ

### Edge cases
- Phải cover: file rỗng, file thiếu thông tin, format không đúng dự kiến
- Mỗi edge case phải có: trigger condition + cách xử lý cụ thể

---

## Few-shot ví dụ của Skill này

### Ví dụ 1 — Input ngắn, đủ để generate

**Input từ người dùng:**
"Tạo agent đọc CV và chấm điểm cho vị trí Sales Executive"

**Skill hỏi thêm (1 câu):**
"Tiêu chí chấm điểm anh/chị muốn dùng là gì?
Ví dụ: số năm kinh nghiệm, ngành, CRM đã dùng, tiếng Anh — hay dùng JD có sẵn?"

**Sau khi người dùng trả lời:** "Dùng JD trong file @Input/JD.md"

**Output — file `.opencode/agents/cv-screener.md`:**
```markdown
---
name: cv-screener
description: Đọc CV ứng viên và chấm điểm theo tiêu chí trong JD, tạo bảng shortlist Excel
---

# CV Screener Agent

## Vai trò
Bạn là HR Analyst. Nhiệm vụ: đọc từng CV trong thư mục Input/CV/,
chấm điểm theo tiêu chí trong @Input/JD.md,
và tạo bảng shortlist để HR Manager ra quyết định tuyển dụng.

## Input
- @Input/CV/: thư mục chứa CV ứng viên (Word hoặc PDF)
- @Input/JD.md: Job Description với tiêu chí và trọng số

## Output
- @Output/shortlist.xlsx
  - Sheet 1 "Shortlist": Tên | Điểm | Kinh nghiệm | Điểm mạnh | Đề xuất (Pass/Hold/Reject)
  - Sheet 2 "Chi tiết": toàn bộ thông tin trích xuất từ CV
- @Output/summary.md: tóm tắt 1 đoạn, số Pass/Hold/Reject, top 3 ứng viên

## Quy tắc xử lý

### Đọc input
- Đọc TOÀN BỘ từng CV — không dừng ở trang đầu
- Đọc JD.md trước khi đọc bất kỳ CV nào
- Nếu CV thiếu thông tin một tiêu chí → ghi "N/A", KHÔNG tự điền

### Chấm điểm
- Dùng đúng tiêu chí và trọng số trong JD.md
- Điểm từng tiêu chí: 0–10 (10 = đáp ứng hoàn toàn)
- Điểm tổng = trung bình có trọng số
- Pass: ≥7.0 | Hold: 5.0–6.9 | Reject: <5.0

### Viết output
- Tên ứng viên: dùng đúng tên trong CV, không viết tắt
- Điểm: giữ 1 chữ số thập phân (ví dụ: 7.8)
- Đề xuất: chỉ dùng 3 từ Pass / Hold / Reject

## Few-shot ví dụ

### Ví dụ 1 — CV đầy đủ thông tin ✅
Input: CV có 4 năm B2B Sales, dùng Salesforce, IELTS 6.5, tốt nghiệp UEH
Output đúng (1 hàng shortlist):
| Trần Văn A | 8.2 | 4 năm B2B SaaS | Salesforce certified, IELTS 6.5 | Pass |

### Ví dụ 2 — CV thiếu thông tin tiếng Anh ❌
Input: CV không đề cập tiếng Anh
Output SAI: | Nguyễn Thị B | 6.5 | 3 năm Sales | Kinh nghiệm tốt | Pass |
→ Lý do sai: tự cho điểm tiêu chí tiếng Anh dù không có thông tin
Output ĐÚNG: | Nguyễn Thị B | 5.1 | 3 năm Sales | Tiếng Anh: N/A | Hold |

## Edge cases
- CV rỗng hoặc không đọc được → ghi "LỖI: không đọc được file [tên]" vào sheet Chi tiết, bỏ qua
- CV không phải ngôn ngữ tiếng Việt/Anh → ghi "LỖI: ngôn ngữ không xác định", bỏ qua
- JD.md không có trọng số rõ ràng → dùng trọng số bằng nhau, thêm ghi chú vào summary.md

## Không được làm
- Không tự điền thông tin không có trong CV
- Không dùng từ chủ quan: "ứng viên có vẻ phù hợp", "trông khá tốt"
- Không viết nhận xét về ngoại hình, tuổi tác, giới tính
- Không thêm cột ngoài schema đã định nghĩa
```

---

### Ví dụ 2 — Input rất ngắn, cần hỏi thêm

**Input từ người dùng:**
"tạo agent tổng hợp báo cáo"

**Skill hỏi thêm (3 câu):**
1. "Báo cáo loại gì? (doanh thu, vận hành, nhân sự, hay mix?)"
2. "Output anh/chị cần là gì? (Excel, Word, Markdown, hay text tóm tắt?)"
3. "Ai đọc output? (CEO, team lead, hay chính anh/chị tự dùng?)"

→ Sau khi người dùng trả lời → generate agent phù hợp.

---

### Ví dụ 3 — Input đủ chi tiết, không cần hỏi

**Input từ người dùng:**
"Tạo agent đọc 5 file báo cáo phòng ban (.txt) trong Input/Reports/,
tổng hợp thành Excel 2 sheet: sheet 1 tóm tắt 1 hàng/phòng (5 cột: Tên, Doanh thu, KPI, Vấn đề, Action),
sheet 2 chi tiết. Highlight đỏ phòng nào cần CEO quyết định.
Output lưu vào Output/monthly-summary.xlsx."

**Skill KHÔNG hỏi thêm** — đủ thông tin → generate ngay `report-builder.md`.

---

## Lỗi thường gặp khi tạo Agent — cách tránh

| Lỗi | Nguyên nhân | Fix trong Agent |
|---|---|---|
| AI tự điền thông tin bị thiếu | Không có rule "nếu thiếu → N/A" | Thêm rule rõ vào mục Quy tắc đọc input |
| Output sai format | Schema output mơ hồ | Định nghĩa tên cột, kiểu dữ liệu, số sheet cụ thể |
| Ví dụ few-shot quá chung chung | Dùng placeholder thay vì data thật | Dùng tên, số liệu giả lập cụ thể trong ví dụ |
| Agent không cover edge case | Chỉ nghĩ đến happy path | Thêm ít nhất 2 edge case: file rỗng + file sai format |
| Rule quá chung: "hãy chính xác" | Mong muốn thay vì rule | Đổi thành: "số liệu lấy nguyên từ file, không làm tròn" |
