# 📘 CẨM NANG VẬN HÀNH THỰC CHIẾN HÀNG NGÀY (MANUAL OPERATOR GUIDE)
## Dành Cho Vai Trò HANDMADE (Sinh Viên Kỹ Sư DUT)

> **Mục tiêu:** Định hình nếp sinh hoạt học tập kỷ luật, biến việc học từ áp lực thành một quy trình khoa học, thấu suốt bản chất và tự tin bảo vệ đồ án/thi cử đạt điểm A.

---

## 1. KHUNG THỜI GIAN CHUẨN TRONG TUẦN (WEEKLY RHYTHM)

```
┌─────────────────────────────────────────────────────────────────────────┐
│ THỨ 2: KHỞI ĐỘNG TUẦN & HOẠCH ĐỊNH (Weekly Kick-off)                    │
│ ➔ 07:30: Mở SEMESTER DASHBOARD trên Notion, kiểm tra deadline tuần.    │
│ ➔ 08:00: Phân công task tuần vào mục WEEKLY PLANNER.                   │
├─────────────────────────────────────────────────────────────────────────┤
│ THỨ 3 & THỨ 5: NGÀY THỰC CHIẾN MÃ NGUỒN & HỆ THỐNG (Code & Systems)     │
│ ➔ Tập trung: Môn Học Máy (Numpy / Sklearn) & Quản trị Mạng (Cisco/Linux)│
│ ➔ Nguyên tắc: Vừa gõ code vừa quan sát log; gặp lỗi ➔ Log vào Notion.  │
├─────────────────────────────────────────────────────────────────────────┤
│ THỨ 4 & THỨ 6: NGÀY LÝ THUYẾT ĐÀO SÂU & AN TOÀN (Deep Theory & Security)│
│ ➔ Tập trung: Computer Vision (Toán Tensor/CNN) & An Toàn Mạng (Wireshark)│
│ ➔ Nguyên tắc: Đọc bài giảng 4 tầng của PSD-04; làm Flashcards.         │
├─────────────────────────────────────────────────────────────────────────┤
│ MỖI NGÀY (30 PHÚT ĐẦU BUỔI SÁNG): TIẾNG NHẬT N3 KỶ LUẬT (Daily Drill)   │
│ ➔ 15 phút: Quẹt Notion Flashcards Kanji (Chiết tự bộ thủ).             │
│ ➔ 15 phút: Luyện nghe Shadowing / 5 câu ngữ pháp tương phản.           │
├─────────────────────────────────────────────────────────────────────────┤
│ THỨ 7: TỔNG LỰC CHO ĐỒ ÁN PBL6 (VietLawAssist Sprint)                   │
│ ➔ Chạy thực nghiệm so sánh 4 tầng; ghi log số liệu Recall/Latency.     │
├─────────────────────────────────────────────────────────────────────────┤
│ CHỦ NHẬT (20:00): REVIEW & REFLECTION (Tổng kết tuần)                   │
│ ➔ Tự kiểm tra xem đạt bao nhiêu % mục tiêu; dọn dẹp không gian làm việc│
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. QUY TRÌNH 4 BƯỚC "NO MAGIC" KHI LÀM LAB HOẶC CODE

Mỗi khi bắt tay vào một bài thực hành hoặc đoạn code mẫu từ Agent:

### Bước 1: Đọc Để Hiểu "Tại Sao" (Why?)
- Đừng vội mở IDE gõ ngay. Đọc mục lý thuyết nền tảng của bài học.
- Tự hỏi: *Thuật toán này giải quyết bài toán gì? Hàm mục tiêu (Objective function) là gì?*

### Bước 2: Tự Tay Gõ Lại (Hands-on Typing)
- **Tuyệt đối không dùng tính năng copy-paste nguyên khối code**.
- Việc tự tay gõ từng dòng lệnh (`import`, vòng lặp `for`, ma trận `np.dot`, hoặc lệnh Cisco `ip route`) giúp xây dựng "trí nhớ cơ bắp" (muscle memory) và phát hiện ngay những lỗi typo nhỏ nhất.

### Bước 3: Phá Vỡ Để Thấu Suốt (Break It to Master It)
- Sau khi code hoặc cấu hình chạy thành công:
  - Hãy thử đổi một tham số: Ví dụ trong K-Means đổi $K$ từ 3 sang 5; trong Cisco đổi subnet mask từ `/24` sang `/25`.
  - Quan sát xem hệ thống báo lỗi gì hoặc kết quả thay đổi ra sao. Đây là cách nhanh nhất để trở thành chuyên gia xử lý sự cố.

### Bước 4: Chụp Màn Hình & Log Lỗi (Error Journaling)
- Khi gặp lỗi: Chụp ảnh màn hình terminal / Wireshark frame $\rightarrow$ Dán vào Notion `LAB ERROR JOURNAL` $\rightarrow$ Viết 2 câu tóm tắt:
  1. *Triệu chứng lỗi:* (VD: Ping Request Timed Out).
  2. *Nguyên nhân gốc rễ & Cách sửa:* (VD: Quên cấu hình Default Gateway trên Router nhánh).

---

## 3. CÁCH ĐỐI CHIẾU NGUỒN NGOẠI SINH VỚI BÀI GIẢNG TRÊN LỚP

Khi Thầy/Cô trên lớp giảng lướt qua một phần kiến thức khó (ví dụ: Backprop trên ma trận tích chập hay cơ chế phân giải DNS đệ quy):
1. Mở tệp [EXTERNAL_KNOWLEDGE_VAULT.md](file:///d:/User/7th/School/00_Corporate_Knowledge_Vault/EXTERNAL_KNOWLEDGE_VAULT.md).
2. Tra cứu môn học tương ứng $\rightarrow$ Mở đúng tài liệu **Tier A+** đã được chỉ định (Ví dụ: Stanford CS231n cho Vision, hoặc Kurose-Ross cho Mạng).
3. Đọc đúng chương được ghi chú trong mục `Giá Trị Chắt Lọc`.
4. Nếu vẫn còn điểm chưa hiểu, gõ câu hỏi vào Box Chat để kích hoạt Agent `PSD-04` hoặc `DUT Network Admin Mentor` giảng giải lại theo phương pháp Socratic.
