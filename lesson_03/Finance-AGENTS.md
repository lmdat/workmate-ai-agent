# Thông tin cá nhân
Tôi là [Họ Tên] — Finance Manager / CFO tại TechCorp Vietnam.
Phòng Tài Chính - Kế Toán, báo cáo trực tiếp cho CEO.
Phụ trách báo cáo tài chính, kiểm soát ngân sách, quản lý dòng tiền và tuân thủ quy định.

# Thông tin Agent
Tên:
Chức vụ:

# Cấu trúc thư mục làm việc
- input/reports/: báo cáo tài chính từ các phòng ban (Excel, Word)
- input/invoices/: hóa đơn nhà cung cấp (PDF, ảnh JPG/PNG)
- input/bank/: sao kê ngân hàng (Excel, CSV)
- output/summary/: báo cáo tổng hợp gửi CEO và BGĐ
- output/board-pack/: tài liệu họp Board/Investor
- output/confidential/: thông tin lương, dòng tiền nội bộ
- templates/: mẫu báo cáo tháng, mẫu expense report, mẫu budget
- scripts/: các file script python, javascript tạo ra trong quá trình thực hiện công việc
- tmp/: các file nội dung tạm

# Quy tắc số liệu và format
- Đơn vị tiền: VNĐ (làm tròn đến triệu đồng trong báo cáo tóm tắt)
- Định dạng số: dùng dấu chấm phân cách nghìn (1.250.000.000 → 1.250 triệu)
- USD: giữ nguyên đến 2 chữ số thập phân, ghi kèm tỷ giá tham chiếu
- Luôn có cột so sánh: Thực tế | Kế hoạch | Chênh lệch | % Chênh lệch
- File Excel: sheet đầu = Executive Summary, các sheet sau = chi tiết theo phòng ban

# Quy tắc nghiệp vụ
- KHÔNG tự điền số liệu còn thiếu — ghi "N/A" và ghi chú "[Cần xác nhận từ phòng X]"
- Deviation > 10% so với kế hoạch: highlight màu vàng + ghi chú nguyên nhân sơ bộ
- Deviation > 20%: highlight màu đỏ + yêu cầu giải trình từ phòng liên quan
- KPI ưu tiên cao nhất: Doanh thu, Gross Profit Margin, EBITDA, Cash Flow
- Báo cáo gửi BGĐ: tóm tắt Executive Summary 1 trang, phụ lục chi tiết tách riêng
- Mọi con số phải trace được về file nguồn — ghi rõ "Nguồn: [tên file]"

# Quy tắc an toàn
- KHÔNG bao giờ làm tròn LÊN số liệu tài chính — chỉ làm tròn xuống hoặc giữ nguyên
- KHÔNG lưu thông tin lương, thưởng, kỷ luật ra ngoài output/confidential/
- KHÔNG tự xóa hoặc ghi đè file trong input/ — chỉ đọc
- Trước khi tạo báo cáo batch: luôn dùng Plan Mode, xác nhận danh sách file sẽ đọc
- Sau khi tạo báo cáo: liệt kê rõ "Các file đã sử dụng" ở cuối tài liệu
