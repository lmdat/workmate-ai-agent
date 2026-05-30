# Thông tin cá nhân
Tôi là [Họ Tên] — Operations Manager / Executive Assistant tại TechCorp Vietnam.
Phòng Vận Hành, báo cáo trực tiếp cho CEO.
Phụ trách quy trình vận hành, quản lý hành chính, theo dõi action items và hỗ trợ điều hành.

# Thông tin Agent
Tên:
Chức vụ:

# Cấu trúc thư mục làm việc
- input/inbox/: tài liệu mới nhận (invoice, hợp đồng, biên bản họp)
- input/pending/: tài liệu đang xử lý, chờ approval
- input/meetings/: biên bản họp, agenda, tài liệu họp
- output/reports/: báo cáo tổng hợp tuần/tháng
- output/archive/: tài liệu đã hoàn tất, lưu theo YYYYMM
- output/action-items/: danh sách việc cần làm từ họp
- templates/: mẫu biên bản, mẫu báo cáo tuần, mẫu action item list
- scripts/: các file script python, javascript tạo ra trong quá trình thực hiện công việc.
- tmp/: các file nội dung tạm.

# Naming Convention (bắt buộc áp dụng)
- Invoice:      [TenNhaCungCap]_Invoice_[SoHD]_[YYYYMM]
  VD:           ViettelTelecom_Invoice_HD2026031_202603
- Biên bản họp: Minutes_[TenCuocHop]_[YYYYMMDD]
  VD:           Minutes_KickoffQ2_20260415
- Báo cáo tuần: WeeklyReport_W[SoTuan]_[YYYY]
  VD:           WeeklyReport_W16_2026
- Action items: ActionItems_[TenCuocHop]_[YYYYMMDD]

# Quy tắc xử lý invoice
Luồng bắt buộc: inbox/ → review → pending/ (chờ approval) → processed/ → archive/YYYYMM/
- KHÔNG di chuyển invoice từ pending/ sang processed/ nếu chưa có xác nhận approval
- Mọi invoice trên 10 triệu đồng: cần approval CEO hoặc CFO trước khi xử lý
- Invoice trùng lặp (cùng vendor + số HĐ): flag ngay, không xử lý tiếp

# Quy tắc action items
- Mỗi action item phải có: Task rõ ràng | Owner (tên người) | Deadline cụ thể | Status
- Task quá hạn > 2 ngày: highlight màu vàng
- Task quá hạn > 5 ngày: highlight màu đỏ + gửi nhắc nhở
- Sắp xếp: theo deadline tăng dần (gần nhất lên trên)
- Status mặc định khi mới tạo: để trống (không tự điền "Pending")

# Quy tắc báo cáo tuần
- Gửi: cuối ngày thứ Sáu mỗi tuần
- Format cố định: (1) Action items tuần này → (2) Action items quá hạn → (3) Việc cần làm tuần tới
- Người nhận: CEO + các manager liên quan
- Không quá 1 trang A4 khi in ra

# Quy tắc an toàn
- KHÔNG di chuyển hoặc xóa file trong input/inbox/ — chỉ đọc và copy sang thư mục xử lý
- Trước khi archive hàng loạt: backup toàn bộ vào output/archive/backup_[YYYYMMDD]/ trước
- Hợp đồng và văn bản pháp lý: chỉ tóm tắt, KHÔNG tự chỉnh sửa nội dung
- Luôn dùng Plan Mode với task di chuyển hoặc rename hàng loạt file
