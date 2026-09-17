# 📜 ĐIỀU LỆ PHÒNG SỐ HÓA & KHÔNG GIAN NOTION (NOTION DIGITAL WORKSPACE DEPT)
## Phòng 04 — Công Ty An Toàn Thông Tin & Tác Chiến Mạng (CORP-04-SEC)

> **Mã Phòng Ban:** `SEC-DEPT-04`  
> **Trưởng phòng phụ trách:** Agent `NKA-05` (Notion Knowledge Architect) & Trợ Lý Vận Hành LMS  
> **Cấp bậc quản trị:** Cấp 2 — Số hóa tri thức an toàn mạng, quản lý cơ sở dữ liệu phân tích gói tin Wireshark và theo dõi lỗ hổng bảo mật

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `SEC-DEPT-04` chịu trách nhiệm kiến tạo, duy trì và tối ưu hóa không gian làm việc số Notion LMS dành cho môn An Toàn Mạng:
1. **Quản lý Cơ sở dữ liệu Phân tích Gói tin (Packet Capture Analysis DB)**: Thiết kế hệ thống trang con cho phép sinh viên đính kèm ảnh chụp Wireshark, file `.pcap` và mổ xẻ cấu trúc Hex/ASCII của từng giao thức.
2. **Cơ sở dữ liệu Ma trận Lỗ hổng & Tấn công (Threat & Vulnerability Matrix)**: Quản lý danh mục các dạng tấn công kinh điển (ARP Spoofing, MITM, SYN Flood, SQL Injection) cùng giải pháp phòng thủ tương ứng.
3. **Theo dõi Tiến độ Đồ án & Thẩm định Barem DUT**: Tích hợp các công thức Formula 2.0 để tự động đo lường độ hoàn thiện của bài tập bảo mật theo barem ĐHBK Đà Nẵng.

---

## 2. BỘ QUY TẮC BẤT BIẾN (WORKSPACE INVARIANTS & HARD CONSTRAINTS)
1. **Nguyên tắc Minh Chứng Packet Bắt Buộc**: Mọi dòng dữ liệu phân tích sự cố bảo mật trong database bắt buộc phải có thuộc tính liên kết file `.pcap` hoặc ảnh chụp màn hình hiển thị bộ lọc Wireshark cụ thể.
2. **Nguyên tắc Notion Formula 2.0 Đánh Giá Rủi Ro**: Điểm số mức độ rủi ro (Risk Severity Score) bắt buộc phải được tính toán tự động qua công thức chuẩn CVSS v3.1 mô phỏng bằng Formula 2.0.
3. **Nguyên tắc Bảo Mật Dữ Liệu Học Viên**: Tuyệt đối không lưu trữ khóa riêng tư thực tế (Private Keys), mật khẩu production của trường trên các trang Notion public.
4. **Nguyên tắc Lưu Trữ Đồng Bộ Offline**: File `NOTION_SEC_SECURITY.md` trong thư mục phòng ban là nguồn chân lý (Single Source of Truth) để phục vụ việc lưu trữ cục bộ và kiểm soát phiên bản bằng Git.

---

## 3. BỘ LỆNH & CÔNG CỤ ĐỒNG BỘ NOTION (TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Kiểm tra tính toàn vẹn của các file Markdown Notion an toàn mạng
python -c "import re; content = open('NOTION_SEC_SECURITY.md', encoding='utf-8').read(); links = re.findall(r'\[.*?\]\((.*?)\)', content); print(f'Total Valid Links: {len(links)}')"

# 2. Định dạng lại bảng ma trận tấn công trước khi nhập vào Notion
npx prettier --check "*.md"

# 3. Quét kiểm tra cú pháp Formula 2.0
grep -rn "lets(" ./
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
04_Notion_Digital_Workspace/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── NOTION_SEC_SECURITY.md             # Không gian Notion tích hợp sẵn sàng import
├── schemas/                           # Định dạng schema JSON của các Database an toàn mạng
│   ├── packet_analysis_schema.json
│   └── threat_matrix_schema.json
└── templates/                         # Mẫu trang báo cáo phân tích mã độc & gói tin
    └── WIRESHARK_INCIDENT_REPORT_TEMPLATE.md
```

---

## 5. MẪU KHUNG DATABASE NOTION FORMULA 2.0 (GOLD MASTER SCHEMA)

### Công Thức Formula 2.0 Phân Loại Mức Độ Rủi Ro An Toàn Mạng Dựa Trên CVSS
```javascript
/* NOTION FORMULA 2.0: Đánh giá cấp độ rủi ro (Risk Severity) cho Lab An Toàn Mạng */
lets(
  exploitability, prop("Exploitability Score"), /* Thang điểm 0 - 10 */
  impact, prop("Impact Score"),                 /* Thang điểm 0 - 10 */
  baseScore, round(((exploitability * 0.4) + (impact * 0.6)) * 10) / 10,

  ifs(
    baseScore >= 9.0,
    "🔴 CRITICAL (" + baseScore + ") - Cần ứng cứu khẩn cấp",
    baseScore >= 7.0,
    "🟠 HIGH (" + baseScore + ") - Nguy cơ cao bị khai thác",
    baseScore >= 4.0,
    "🟡 MEDIUM (" + baseScore + ") - Cần vá lỗi định kỳ",
    "🟢 LOW (" + baseScore + ") - Rủi ro thấp"
  )
)
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Trường dữ liệu toàn diện**: Database Packet Capture có đủ các trường: `Giao thức`, `Cổng dịch vụ`, `Trạng thái mã hóa (Cleartext / Encrypted)`, `Bộ lọc Wireshark Display Filter`, `Đánh giá rủi ro Formula 2.0`.
- [x] **Giao diện Gallery View trực quan**: Hỗ trợ hiển thị ảnh chụp gói tin dạng thẻ Gallery để tiện theo dõi.
- [x] **Đồng bộ hóa 100% với Git**: File `NOTION_SEC_SECURITY.md` được lưu trữ đầy đủ nội dung, không có liên kết đứt gãy.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ ĐỒNG BỘ NOTION (TROUBLESHOOTING & RUNBOOK)

### Sự cố 1: File `.pcapng` đính kèm vào Notion vượt quá dung lượng cho phép
- **Hiện tượng**: Notion báo lỗi giới hạn file upload khi người dùng cố đính kèm file bắt gói tin quá lớn.
- **Cách khắc phục**:
  1. Cắt tỉa file capture bằng công cụ `editcap` để chỉ giữ lại các gói tin quan trọng:
     ```bash
     editcap -r full_capture.pcapng trimmed.pcapng 1-500
     ```
  2. Nén file bằng zip hoặc chỉ xuất các packet bị ảnh hưởng (Export Specified Packets) trên giao diện Wireshark.

### Sự cố 2: Ảnh chụp màn hình Wireshark mờ, không đọc được số Hex
- **Cách khắc phục**: Hướng dẫn sinh viên dùng tính năng "Copy as Print Text" trên Wireshark hoặc chụp màn hình ở độ phân giải gốc 100% (không dùng công cụ nén ảnh lossy gây mất chi tiết byte).
