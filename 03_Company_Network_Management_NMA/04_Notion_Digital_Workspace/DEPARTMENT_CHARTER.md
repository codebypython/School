# 📜 ĐIỀU LỆ PHÒNG SỐ HÓA & KHÔNG GIAN NOTION (NOTION DIGITAL WORKSPACE DEPT)
## Phòng 04 — Công Ty Hạ Tầng & Quản Trị Mạng Doanh Nghiệp (CORP-03-NMA)

> **Mã Phòng Ban:** `NMA-DEPT-04`  
> **Trưởng phòng phụ trách:** Agent `NKA-05` (Notion Knowledge Architect) & Trợ Lý Vận Hành LMS  
> **Cấp bậc quản trị:** Cấp 2 — Số hóa tri thức hạ tầng mạng, quản lý cơ sở dữ liệu Flashcard giao thức, Port Matrix và tiến độ đồ án

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `NMA-DEPT-04` chịu trách nhiệm kiến tạo, duy trì và tối ưu hóa không gian số Notion LMS dành cho môn Quản trị Mạng:
1. **Quản lý Không gian LMS Môn Quản trị Mạng**: Cung cấp các template Markdown sẵn sàng import vào Notion, tổ chức theo dõi 15 tuần học và các bài lab thực hành.
2. **Cơ sở dữ liệu Giao thức & Cổng Dịch vụ IANA**: Xây dựng bảng tra cứu Flashcard thông minh gồm: Số cổng, Giao thức tầng Transport, Mã RFC và câu lệnh CLI kiểm thử tương ứng.
3. **Theo dõi Đồ án Mạng Doanh nghiệp & Lab Error Journal**: Quản lý tiến độ đồ án phủ sóng WiFi, cấu hình Router/Switch và thư viện nhật ký khắc phục sự cố (Troubleshooting Gallery).

---

## 2. BỘ QUY TẮC BẤT BIẾN (WORKSPACE INVARIANTS & HARD CONSTRAINTS)
1. **Nguyên tắc Chuẩn Hóa Bảng Port IANA**: Mọi dịch vụ mạng trên Notion bắt buộc phải có đủ 4 trường: Cổng mặc định (Default Port), Tầng Transport (TCP/UDP), Giao thức bảo mật thay thế (ví dụ HTTP 80 vs HTTPS 443; DNS 53 vs DoT 853; LDAP 389 vs LDAPS 636), và Trạng thái thẩm định.
2. **Nguyên tắc Notion Formula 2.0 Tính Điểm Lab**: Sử dụng công thức Formula 2.0 hiện đại để tự động chấm điểm tiến độ hoàn thành cấu hình dựa trên kết quả ping và snapshot packet capture.
3. **Nguyên tắc Đồng bộ Hai Chiều (Bi-directional Sync)**: Mọi thay đổi trong cấu trúc thư mục thực hành phải được phản ánh tương ứng trong bảng theo dõi Notion LMS.
4. **Nguyên tắc Lưu Bản Sao Cục Bộ**: Toàn bộ dữ liệu không gian Notion bắt buộc phải có bản backup định dạng Markdown `.md` lưu trữ trong git repository.

---

## 3. BỘ LỆNH & CÔNG CỤ ĐỒNG BỘ NOTION (TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Kiểm tra tính hợp lệ của các liên kết tài liệu trong thư mục Notion
python -c "import re; content = open('NOTION_NMA_NETWORK_MANAGEMENT.md', encoding='utf-8').read(); links = re.findall(r'\[.*?\]\((.*?)\)', content); print(f'Total Links: {len(links)}')"

# 2. Định dạng lại bảng Markdown trước khi import vào Notion Database
npx prettier --write "*.md"

# 3. Quét kiểm tra cú pháp Formula 2.0 trong tài liệu
grep -rn "lets(" ./
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
04_Notion_Digital_Workspace/
├── DEPARTMENT_CHARTER.md                          # Điều lệ phòng ban 7 tầng chuẩn hóa
├── NOTION_NMA_NETWORK_MANAGEMENT.md              # Không gian LMS trung tâm môn Quản trị mạng
├── NOTION_STUDY_WORKSPACE_CAFE_WIFI.md           # Không gian đồ án mạng Cafe Wifi
└── NOTION_IMPORT_NMA_CAFE_WIFI.md                # Hướng dẫn import đồ án mạng vào Notion
```

---

## 5. MẪU KHUNG DATABASE NOTION FORMULA 2.0 (GOLD MASTER SCHEMA)

### Công Thức Formula 2.0 Đánh Giá Tiến Độ Hoàn Thành & Xác Thực Lab Quản Trị Mạng
```javascript
/* NOTION FORMULA 2.0: Đo lường tiến độ Lab Mạng & Cảnh báo kiểm thử */
lets(
  topoDone, if(prop("Topology & IP Planned"), 1, 0),
  configDone, if(prop("CLI Commands Applied"), 1, 0),
  pingVerified, if(prop("Ping & Traceroute Passed"), 1, 0),
  wiresharkVerified, if(prop("Wireshark Capture Attached"), 1, 0),
  savedNVRAM, if(prop("Saved to Startup-Config"), 1, 0),

  totalSteps, topoDone + configDone + pingVerified + wiresharkVerified + savedNVRAM,
  progress, (totalSteps / 5) * 100,

  ifs(
    progress == 100,
    "🟢 Lab Hoàn Tất Chuẩn Mực (100%)",
    progress >= 60 && !prop("Saved to Startup-Config"),
    "⚠️ Cảnh báo: Chưa lưu cấu hình vào NVRAM! (" + progress + "%)",
    progress >= 60,
    "🟡 Đang cấu hình & kiểm thử (" + progress + "%)",
    "🔴 Mới khởi tạo / Thiếu kiểm thử (" + progress + "%)"
  )
)
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Trường dữ liệu toàn diện**: Database Lab có đầy đủ trường: `Tên Lab`, `Chuyên đề (FCAPS/Services/Cisco)`, `Thiết bị liên quan`, `Trạng thái Ping`, `Trạng thái Lưu NVRAM`, `Tiến độ Formula 2.0`.
- [x] **Cập nhật đầy đủ 3 không gian số**: Cả 3 file Markdown Notion đều có cấu trúc rõ ràng, không bị lỗi liên kết.
- [x] **Tích hợp Flashcard tra cứu cổng IANA**: Bảng tra cứu cổng có đầy đủ các giao thức kinh điển (DHCP, DNS, HTTP, HTTPS, SSH, Telnet, FTP, TFTP, SNMP, Syslog, LDAP, Kerberos).
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ ĐỒNG BỘ NOTION (TROUBLESHOOTING & RUNBOOK)

### Sự cố 1: Bảng phân bổ IP bị vỡ khung khi copy từ Markdown sang Notion
- **Hiện tượng**: Bảng IP có nhiều cột bị tràn lề hoặc các dòng ghi chú CIDR biến thành text rời rạc.
- **Cách khắc phục**:
  1. Sử dụng tính năng "Import as CSV" hoặc tạo Table trực tiếp trên Notion trước khi dán nội dung.
  2. Bật chế độ "Wrap Column" cho cột Ghi chú cấu hình.

### Sự cố 2: Sinh viên quên backup cấu hình thiết bị trước khi xóa phòng lab
- **Hiện tượng**: Tệp cấu hình trên router Cisco bị mất trắng sau khi tắt phần mềm mô phỏng.
- **Cách khắc phục**:
  1. Yêu cầu bắt buộc nộp file cấu hình dạng text `running-config.txt` đính kèm vào trang Notion của từng Lab.
  2. Áp dụng quy tắc kiểm tra tiêu chí `DoD-5 (NVRAM Saved)` trước khi bấm hoàn thành bài thực hành.
