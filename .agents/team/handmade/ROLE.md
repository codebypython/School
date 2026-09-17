# 🛠 Role: HANDMADE (Human-in-the-Loop Student Operator)

> **Mã Vai Trò:** `HM-00` / `HANDMADE`  
> **Tên vai trò:** Kỹ Sư Thực Thi Thủ Công & Chủ Thể Học Tập (Student Operator & Scholar)  
> **Người đảm nhận:** Bạn (Sinh viên Kỹ sư CNTT — Đại học Bách khoa, ĐH Đà Nẵng)  
> **Kế thừa quy cách từ:** `HANDMADE` (VietLawAssist PBL6)

---

## 1. MỤC ĐÍCH & Ý NGHĨA VAI TRÒ "HANDMADE"

Trong thời đại AI tạo sinh, nguy cơ lớn nhất của sinh viên kỹ thuật là **"Ảo tưởng thành thạo" (Illusion of Competence)** — tức là để AI viết code, tóm tắt slide rồi tưởng rằng mình đã hiểu, nhưng khi đứng trước Hội đồng chấm thi vấn đáp hoặc đối mặt với sự cố mạng thực tế thì lúng túng, không giải thích được bản chất.

Role **Handmade** được thiết kế để giữ vững vị thế **Chủ Thể Làm Chủ Tri Thức**:
1. **Hiểu thấu gốc rễ (Deep Understanding)**: Tự tay code từng thuật toán Numpy, tự tay gõ từng dòng lệnh Cisco/Linux, tự tay mở Wireshark bắt gói tin để "nhìn thấy" dữ liệu chạy trên đường truyền.
2. **Bản lĩnh trước Hội đồng chấm thi**: Khi Thầy/Cô hỏi bất kỳ câu hỏi phản biện nào (Tại sao dùng mô hình này? Tại sao subnet này không ping được? Đoạn mã hóa này nằm ở đâu trong gói tin?), bạn đều trả lời rành rọt từ trải nghiệm thực chiến.
3. **Phối hợp Người - AI tối ưu**: Các AI Agent là ban cố vấn tinh hoa (tổng hợp tài liệu, kiểm tra lỗi, thiết kế bài giảng); còn Bạn là người ra quyết định, thực thi và tiếp thu tri thức vào bộ não của mình.

---

## 2. PHẠM VI TRÁCH NHIỆM

| Lĩnh Vực | Trách Nhiệm Chi Tiết Của Bạn (Handmade) | AI Agents Hỗ Trợ |
| :--- | :--- | :--- |
| **1. Tự tay thực hành Code & Lab** | Tự gõ mã nguồn, tự dựng sơ đồ mạng trên Cisco Packet Tracer/GNS3, nạp cấu hình và quan sát log kết quả. | `PSD-04` & `DUT Network Admin Mentor` (Cung cấp kịch bản, topo, giải thích lệnh) |
| **2. Active Recall & Flashcard hàng ngày** | Dành 15 phút mỗi sáng mở Notion làm Flashcard lặp lại ngắt quãng (Spaced Repetition) để khắc sâu khái niệm vào trí nhớ dài hạn. | `NKA-05` (Cung cấp công thức SuperMemo và thẻ ôn tập) |
| **3. Ghi chép Nhật ký Sự cố (Error Journal)** | Mỗi khi gặp lỗi (Bug code, lỗi định tuyến, lỗi bắt tay TLS), chụp màn hình và ghi lại nguyên nhân gốc rễ vào Notion Error Journal. | `PSD-04` (Chỉ ra cạm bẫy kinh điển và cách sửa) |
| **4. Thẩm định & Phản hồi Thực tế** | Thử nghiệm các nguồn tài liệu do `EKC-03` chắt lọc; phản hồi lại nếu tài liệu quá khó hiểu hoặc không chạy được trên máy cá nhân. | `EKC-03` & `ACD-01` (Điều chỉnh độ khó và tìm nguồn thay thế) |

---

## 3. QUY TẮC "NO MAGIC" CHO NGƯỜI HỌC

```
┌────────────────────────────────────────────────────────────────────────┐
│                        QUY TẮC BẤT DI BẤT DỊCH                         │
│                                                                        │
│ 1. Không bao giờ copy-paste code mà không hiểu từng dòng lệnh làm gì.   │
│ 2. Khi code chạy thành công ➔ Hãy thử đổi 1 tham số để xem nó lỗi ra  │
│    sao (Break it to learn it).                                         │
│ 3. Khi lab bị lỗi ➔ Đừng vội xóa làm lại, hãy dùng Wireshark/Ping/     │
│    Traceroute để cô lập nguyên nhân (Troubleshoot like a pro).         │
│ 4. Mỗi tuần tự kiểm tra bằng 1 câu hỏi Micro-quiz cuối bài.           │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 4. TÀI LIỆU GIAO TIẾP VÀ VẬN HÀNH

- **Checklist công việc của bạn:** [.agents/team/handmade/TASKS.md](file:///d:/User/7th/School/.agents/team/handmade/TASKS.md)
- **Cẩm nang vận hành hàng ngày (SOP):** [.agents/team/handmade/MANUAL_OPERATOR_GUIDE.md](file:///d:/User/7th/School/.agents/team/handmade/MANUAL_OPERATOR_GUIDE.md)
- **Báo cáo tự đánh giá của bạn:** [.agents/team/handmade/REVIEW.md](file:///d:/User/7th/School/.agents/team/handmade/REVIEW.md)
