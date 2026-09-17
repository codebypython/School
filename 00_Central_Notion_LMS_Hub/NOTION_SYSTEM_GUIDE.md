# 🧭 BỘ SÁNG KIẾN & HƯỚNG DẪN SỬ DỤNG HỆ THỐNG NOTION HỌC TẬP (SEMESTER 7)

Tài liệu này là **"Bản thiết kế vận hành" (SOP - Standard Operating Procedure)** giúp bạn khai thác 100% sức mạnh của 6 file Notion đã được tạo. Hãy đọc kỹ phần Setup ban đầu và áp dụng Workflow hàng ngày cho từng môn học.

---

## ⚙️ PHẦN 1: HƯỚNG DẪN SETUP BAN ĐẦU (1 LẦN DUY NHẤT)

Sau khi kéo thả 6 file `.md` vào Notion của bạn, hãy thực hiện các bước "hô biến" văn bản tĩnh thành Hệ thống Động (Dynamic System).

### 1. Kích hoạt Database (Dữ liệu động)
Mặc định, Notion sẽ nhận diện các bảng (Table) trong file Markdown là bảng tĩnh.
*   **Thao tác:** Đưa chuột lên góc trên cùng bên phải của bảng $\rightarrow$ Click vào biểu tượng `···` (Options) $\rightarrow$ Chọn **`Turn into database`**.
*   **Kết quả:** Bảng của bạn giờ đây đã có các tính năng Filter (Lọc), Sort (Sắp xếp), và Views (Góc nhìn).

### 2. Thiết lập "Bộ não Spaced Repetition" (Lặp lại ngắt quãng)
Tại các Database có tính năng Flashcard (NMA, CV, Security, Japanese), bạn cần kích hoạt công thức để Notion tự động nhắc bài.
*   **Thao tác:** 
    1. Click chuột trái vào tiêu đề cột `Cần Ôn?` $\rightarrow$ Chọn `Edit property`.
    2. Đổi `Type` từ *Text* sang **`Formula`**.
    3. Paste công thức sau vào ô Formula:
       ```javascript
       if(empty(prop("Lần Ôn Gần Nhất")), true, dateAdd(prop("Lần Ôn Gần Nhất"), prop("Chu Kỳ (Ngày)"), "days") <= now())
       ```
    4. Cột này giờ sẽ tự động trả về ô vuông tick (hoặc giá trị True/False) nếu đã đến hạn ôn tập!

### 3. Tạo các Góc nhìn (Views) thần thánh
Để không bị ngợp data, hãy tạo các View khác nhau trên cùng một Database:
*   **Board View (Kanban):** Click dấu `+` cạnh chữ *Table* ở góc trên Database $\rightarrow$ Chọn `Board`. Rất hữu ích cho Sprint PBL6 hoặc Tracker môn học (kéo thả task từ *Todo* $\rightarrow$ *In Progress* $\rightarrow$ *Done*).
*   **Gallery View:** Chọn `Gallery`. Hữu ích cho *Lab Error Journal* (môn NMA, Security) $\rightarrow$ Chỉnh `Card preview` thành `Page content` để hiện thẳng ảnh chụp lỗi màn hình!

---

## 🚀 PHẦN 2: WORKFLOW & THAO TÁC SỬ DỤNG TỪNG PAGE

### 🏠 1. SEMESTER DASHBOARD (Command Center)
Đây là trang bạn mở ra đầu tiên mỗi buổi sáng và cuối cùng mỗi buổi tối chủ nhật.

*   **Sáng Thứ 2 (Lên lịch tuần):** 
    *   Vào `II. WEEKLY PLANNER`. 
    *   **Thao tác Notion:** Lọc (Filter) cột `Tuần` = `W1` (hoặc tuần hiện tại). Ghi các công việc trọng tâm từ 5 page môn học vào đây.
*   **Tối Thứ 7 / Chủ nhật (Review):**
    *   Vào `VI. WEEKLY REFLECTION`.
    *   **Thao tác Notion:** Copy/Duplicate toàn bộ khối Toggle "Tuần W___" để tạo bản ghi cho tuần mới. Nhìn lại lịch sử để xem mình có đạt đủ giờ học mục tiêu (Mục V) không.
*   **Quản lý Deadline:**
    *   Cột `Sự kiện` ở Mục III sẽ đếm ngược ngày. **Thao tác:** Tạo `Sort` $\rightarrow$ Sắp xếp cột Ngày theo thứ tự *Ascending* (Tăng dần) để việc gấp tự trồi lên trên.

---

### 📡 2. QUẢN TRỊ MẠNG (NMA-DUT)
Khối lượng thực hành môn này rất lớn, cần focus vào Lệnh CLI và Troubleshooting.

*   **15 Phút Buổi Sáng (Active Recall):** 
    *   **Thao tác:** Ở DB Flashcard, tạo 1 View tên là `⚠️ Cần Ôn`. Chỉnh Filter $\rightarrow$ `Cần Ôn?` = `Checked` (hoặc True). 
    *   Chỉ nhìn khái niệm (cột 1) $\rightarrow$ Tự nhẩm đáp án $\rightarrow$ Kéo thanh ngang xem đáp án đúng không $\rightarrow$ Nếu đúng, sửa `Lần Ôn Gần Nhất` thành `Today`, tăng `Chu Kỳ` lên (VD: 1 $\rightarrow$ 3 $\rightarrow$ 7 ngày).
*   **Khi làm Lab (Chiều):** 
    *   Mở mục `V. LAB CLI QUICK REFERENCE`, bung các Toggle (`>`) ra để copy/tham khảo khung lệnh Cisco/Linux chuẩn, không cần mò lại slide.
*   **Khi Lab Bị Lỗi (Rất quan trọng):** 
    *   Mở mục `III. LAB ERROR JOURNAL`. Điền mã lỗi (VD: cấu hình sai DHCP). 
    *   **Thao tác:** Click `Open` (Mở rộng dòng thành 1 trang riêng) $\rightarrow$ Copy cái Template báo lỗi ở Mục VII thả vào $\rightarrow$ Viết nguyên nhân gốc rễ và paste cả code sai / code đúng. Trực tiếp dán Screenshot màn hình (Ctrl+V) vào trong Page đó.

---

### 👁️ 3. COMPUTER VISION (CV)
Môn này tập trung vào Toán, Thuật toán, và Đọc Paper (Nghiên cứu).

*   **Khi đọc báo cáo/Paper (Paper Reading Tracker):**
    *   **Thao tác:** Chuyển DB thành **Board View** (Group theo `Trạng thái`: Todo $\rightarrow$ Reading $\rightarrow$ Done). Khi bắt đầu đọc 1 paper (VD: ResNet), kéo thả card sang *Reading*.
    *   Bên trong card của paper, sử dụng Notion AI (nếu có) hoặc tự tóm tắt *Architecture* và *Innovation* để sau này viết báo cáo lấy từ đây.
*   **Khi code Project/Lab:**
    *   Vào mục `IV. CODE SNIPPET VAULT`. Copy trực tiếp các template Dataset, Dataloader, Training Loop để bắt đầu project nhanh, tránh lỗi cú pháp cơ bản.
*   **Trước ngày thi/kiểm tra:**
    *   Mở `V. ACTIVE RECALL QUIZ`. 
    *   **Thao tác:** Nhìn câu hỏi $\rightarrow$ Suy nghĩ đáp án $\rightarrow$ Click tam giác `>` để bung đáp án đối chiếu (Feynman technique).

---

### 🔐 4. AN TOÀN MẠNG (SECURITY)
Điểm "ăn tiền" của môn này là phân tích gói tin mạng (Packet Analysis).

*   **Thực hành Wireshark (Capture Log):**
    *   Sau mỗi bài lab GNS3, lưu file pcapng.
    *   Vào `III. PACKET CAPTURE ANALYSIS LOG`. 
    *   **Thao tác:** Click `Open` row đó ra. **Dán hình chụp (Screenshot) các frame Wireshark quan trọng trực tiếp vào thân Page của row đó.** Đóng gói 1 bài lab hoàn chỉnh gồm "Cấu hình Auth $\rightarrow$ Chụp gói tin $\rightarrow$ Chỉ ra chỗ mã hóa/hash trong hình".
*   **Học Giao thức (Protocol Flashcards):**
    *   Tương tự NMA, lọc những thẻ đến hạn. Chú trọng cột `CLI Cấu hình` vì môn này bắt buộc phải thuộc lệnh Authentication.

---

### 🤖 5. ĐỒ ÁN CHUYÊN NGÀNH PBL6 (VIETLAWASSIST)
Đây là môi trường làm việc nhóm và Quản lý dự án chuẩn Agile.

*   **Quản lý tiến độ (Sprint Board):**
    *   **Thao tác:** Setup DB thành **Board View** grouped by `Status`. 
    *   **Filter:** Tạo View riêng cho từng thành viên (Ví dụ: Lọc `Assignee` = `Người A`).
    *   Mỗi thứ 2 hàng tuần: Kéo task từ *Backlog* sang *In Progress*. Cuối tuần kéo sang *Done*.
*   **Ghi chép Thực nghiệm (Experiment Log):**
    *   Mỗi khi run 1 script kiểm thử (BM25, FAISS, LoRA), tạo 1 dòng mới trong `IV. EXPERIMENT LOG`.
    *   Ghi rõ điểm Recall, Latency, và VRAM để **làm minh chứng đưa vào Báo cáo cuối kỳ**. So sánh trực quan sự tăng tiến qua 4 tầng cấu trúc.
*   **Học & Research:**
    *   Link mọi bài báo/tutorial vào `Learning Resource Tracker`. Thấy bài hay trên mạng $\rightarrow$ Dùng *Notion Web Clipper* lưu thẳng vào DB này.

---

### 🇯🇵 6. TIẾNG NHẬT N3
Chìa khóa ngôn ngữ là sự kiên trì và Drill (luyện tập) hàng ngày.

*   **Buổi Sáng (Drill Kanji & Vocab):**
    *   Vào `II. KANJI MASTER` và `III. VOCABULARY`. 
    *   **Thao tác:** Bật Filter `Cần Ôn? = True`. Nhìn âm On/Kun $\rightarrow$ Viết ra nháp 3 lần $\rightarrow$ Đánh dấu đã ôn để Notion đẩy sang ngày hôm sau (hoặc 3 ngày sau).
    *   Để học nhanh, hãy đọc cột `Mẹo Nhớ` (phân tích chiết tự theo Bộ thủ).
*   **Học Ngữ Pháp:**
    *   Sử dụng DB `GRAMMAR PATTERN LIBRARY`. Nhóm (Group) DB này theo `Level` hoặc `Sách`. 
    *   Việc tự đặt câu ví dụ trong DB sẽ giúp bạn nhớ sâu hơn là chỉ học thuộc công thức.
*   **Tracking Đọc Hiểu & Kỷ luật:**
    *   Hoàn thành xong 1 bài đọc Kosei, log ngay vào `READING LOG`. Chấm điểm tự đánh giá (VD: 7/10).
    *   Cuối tuần tổng kết `WEEKLY DRILL TRACKER` xem mình đã cày đủ số từ và số bài chưa.

---

### 🧠 7. HỌC MÁY VÀ ỨNG DỤNG (MACHINE LEARNING)
Môn học này yêu cầu tư duy toán học cao và năng lực code "from scratch" thay vì chỉ gọi thư viện.

*   **Khi học Thuật toán & Toán (Cheatsheet):**
    *   Sử dụng DB `ALGORITHM & MATH CHEATSHEET`. Tương tự các môn khác, nhớ filter thẻ `Cần Ôn = True`.
    *   **Thao tác Notion:** Nên gõ công thức toán bằng cú pháp KaTeX của Notion (Gõ `$$` rồi nhập công thức) vào cột Hàm mục tiêu để công thức render ra chuẩn đẹp.
*   **Khi làm Lab (Đối chiếu hiệu năng):**
    *   Sử dụng `FROM-SCRATCH VS LIBRARY COMPARISON LOG`.
    *   Mỗi khi viết xong hàm Numpy và chạy so sánh với Sklearn, hãy ghi lại số vòng lặp và Runtime vào đây.
    *   **Thao tác:** Bật tính năng tính toán ở dưới cùng của cột Number (chọn `Calculate` $\rightarrow$ `Average` hoặc `Sum`) để thống kê hiệu năng.
*   **Lưu trữ Code "Chống cháy" (Code Vault):**
    *   Các đoạn code tính khoảng cách hay vẽ đồ thị Matplotlib được lưu sẵn ở mục IV. Bạn chỉ cần click `Copy to clipboard` là có thể paste ngay vào Jupyter Notebook.

---

## 🎯 LỜI KHUYÊN CUỐI
Hệ thống này được thiết kế theo tư duy **Single Source of Truth** (Chân lý tại một điểm). Nghĩa là:
1. Gặp lỗi khi code/lab? Đừng ghi ra nháp $\rightarrow$ **Ghi vào Error Journal**.
2. Thấy link web hay? Đừng bookmark trình duyệt $\rightarrow$ **Lưu vào Resource Tracker**.
3. Cần xem lịch tuần sau? Đừng mở lịch điện thoại $\rightarrow$ **Vào Dashboard Tổng**.

Kiên trì duy trì kỷ luật nhập liệu vào Notion trong 2-3 tuần đầu, bạn sẽ thấy việc kiểm soát tiến độ Semester 7 trở nên cực kỳ trơn tru và khoa học!
