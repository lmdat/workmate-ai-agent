# Thông tin cá nhân
Tôi là [Họ Tên] — HR Manager tại TechCorp Vietnam.
Phòng Nhân Sự, báo cáo trực tiếp cho CEO.
Phụ trách toàn bộ tuyển dụng, onboarding, performance review, và chính sách nhân sự.

# Thông tin Agent
Tên:
Chức vụ:

# Cấu trúc thư mục làm việc
- input/cv/: hồ sơ ứng viên (PDF, DOCX)
- input/jd/: job description và yêu cầu tuyển dụng
- input/performance/: file đánh giá KPI, self-assessment
- output/shortlist/: danh sách ứng viên qua vòng sàng lọc
- output/interview-schedule/: lịch phỏng vấn
- output/onboarding/: tài liệu cho nhân viên mới
- output/confidential/: thông tin lương, thưởng, kỷ luật (bảo mật)
- templates/: mẫu JD, mẫu email, mẫu offer letter
- scripts/: các file script python, javascript tạo ra trong quá trình thực hiện công việc.
- tmp/: các file nội dung tạm.

# Quy tắc output
- Ngôn ngữ: tiếng Việt
- File shortlist: Excel, mỗi ứng viên 1 hàng
- Email tuyển dụng: tone chuyên nghiệp, thân thiện, không quá 200 từ
- Tên file CV chuẩn: [HoTen]_[ViTri]_[YYYYMMDD] (VD: NguyenVanA_SalesExec_20260415)

# Tiêu chí tuyển dụng mặc định
## Vị trí Sales Executive:
- Kinh nghiệm tối thiểu: 2 năm Sales B2B
- Kỹ năng bắt buộc: đàm phán, CRM, báo cáo kết quả
- Kỹ năng ưu tiên: kinh nghiệm ngành tech/phần mềm
- Học vấn: Đại học trở lên (ưu tiên Kinh tế, Quản trị Kinh doanh)
- Điểm loại ngay: thiếu kinh nghiệm Sales, không có track record số liệu

## Vị trí Marketing Manager:
- Kinh nghiệm tối thiểu: 3 năm Marketing B2B/B2C
- Kỹ năng bắt buộc: digital marketing, data analytics, quản lý team
- Kỹ năng ưu tiên: kinh nghiệm với ngân sách > 500 triệu/năm
- Học vấn: Đại học trở lên (Marketing, Truyền thông)
- Điểm loại ngay: chỉ có kinh nghiệm freelance, không quản lý campaign có KPI

# Quy tắc nghiệp vụ
- KHÔNG tự quyết định Pass/Fail — chỉ đề xuất "Tiềm năng cao / Xem xét / Loại" kèm lý do cụ thể
- Mọi đề xuất phải có bằng chứng từ CV (trích dẫn đoạn cụ thể)
- Ứng viên thiếu 1 kỹ năng bắt buộc: ghi rõ và để HR quyết định — không tự loại
- Khi tạo email mời phỏng vấn: luôn đề cập tên vị trí, thời gian linh hoạt, địa điểm/hình thức

# Quy tắc an toàn
- KHÔNG log hoặc hiển thị thông tin lương, thưởng, kỷ luật ra ngoài output/confidential/
- KHÔNG lưu số CMND, số hộ chiếu, thông tin ngân hàng của ứng viên ra bất kỳ đâu
- KHÔNG tự xóa CV gốc trong input/cv/ — chỉ đọc, không ghi đè
- Luôn dùng Plan Mode trước khi xử lý batch > 20 CV
