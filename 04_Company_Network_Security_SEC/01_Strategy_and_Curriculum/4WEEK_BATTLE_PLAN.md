# ⚡ KẾ HOẠCH TÁC CHIẾN 4 TUẦN: CÔNG TY AN TOÀN MẠNG (CYBERDEFENSE CORP)
## 4-Week Tactical Execution Plan — Network Security & Cryptography (SEC)

> **Mã Doanh Nghiệp:** `CORP-04-SEC`  
> **Cố vấn chuyên môn:** Giám Đốc An Toàn Thông Tin (`PSD-04`)  
> **Người thực thi:** Kỹ Sư Trưởng Handmade (`HM-00` / Bạn)

---

## 🎯 MỤC TIÊU THÁNG 1
Nắm chắc nền tảng toán học mật mã khối AES-128/256, tự lập trình sinh khóa RSA bằng Python; tự dựng hạ tầng PKI Root CA bằng OpenSSL và phân tích bắt tay TLS 1.3 trên Wireshark.

---

## 📅 LỘ TRÌNH CHI TIẾT TỪNG TUẦN

### Tuần 1: Mô Hình An Toàn CIA Triad & Thám Mã Cổ Điển (Cryptanalysis)
- **Lý thuyết**: 3 mục tiêu an ninh CIA (Bí mật, Toàn vẹn, Khả dụng), Các vector tấn công thụ động (Passive) vs chủ động (Active), Kỹ thuật thám mã tần suất chữ cái trên mật mã Vigenere.
- **Thực hành (Lab)**:
  - Viết script Python cài đặt bộ mã hóa/giải mã Vigenere.
  - Viết thuật toán thám mã tự động tìm độ dài khóa bằng chỉ số trùng lặp (Index of Coincidence - IoC) và bẻ khóa thông điệp mà không cần khóa bí mật.
- **Sản phẩm bàn giao**: Notebook `03_Engineering_Labs_and_Code/W1_Classical_Cryptanalysis.ipynb`.
- **KPI nghiệm thu**: Bẻ khóa thành công bức điện mật tiếng Anh/Việt dài 200 từ.

---

### Tuần 2: Chuẩn Mã Hóa AES & Nguy Hiểm Của Chế Độ ECB Mode
- **Lý thuyết**: Cấu trúc khối 128-bit của AES, 4 phép biến đổi trong 1 Round (`SubBytes`, `ShiftRows`, `MixColumns`, `AddRoundKey`), Phép nhân đa thức trong trường hữu hạn Galois $GF(2^8)$, Sự khác biệt giữa các chế độ mã khối: ECB, CBC, CTR, GCM.
- **Thực hành (Lab)**:
  - Viết script Python thực nghiệm trên file ảnh BMP:
    - Mã hóa ảnh bằng AES-128 ở chế độ `ECB`: Quan sát thấy ảnh sau khi mã hóa vẫn lộ rõ đường nét vật thể (lỗ hổng kinh điển).
    - Mã hóa ảnh bằng AES-128 ở chế độ `CBC` (với vector khởi tạo IV ngẫu nhiên) và `GCM`: Ảnh biến thành nhiễu hạt hoàn toàn ngẫu nhiên.
- **Sản phẩm bàn giao**: Báo cáo trực quan hóa ảnh kèm mã nguồn trong `03_Engineering_Labs_and_Code/W2_AES_Modes_Comparison/`.
- **KPI nghiệm thu**: Chứng minh trực quan lý do tại sao cấm tuyệt đối sử dụng ECB mode trong môi trường sản xuất.

---

### Tuần 3: Mật Mã Khóa Công Khai RSA & Trao Đổi Khóa Diffie-Hellman
- **Lý thuyết**: Bài toán phân tích thừa số nguyên tố lớn, Định lý Euler, Hàm số $\phi(n) = (p-1)(q-1)$, Tìm nghịch đảo modulo bằng thuật toán Euclid mở rộng, Bắt tay trao đổi khóa Diffie-Hellman qua kênh không an toàn.
- **Thực hành (Lab)**:
  - Tự lập trình trọn vẹn thuật toán RSA từ scratch bằng Python (không dùng thư viện `cryptography`):
    1. Hàm kiểm tra số nguyên tố Miller-Rabin.
    2. Hàm tính nghịch đảo modulo $d = e^{-1} \pmod{\phi(n)}$.
    3. Hàm mã hóa $c = m^e \pmod n$ và giải mã $m = c^d \pmod n$ bằng thuật toán bình phương và nhân liên tiếp (Square-and-Multiply).
- **Sản phẩm bàn giao**: File script `rsa_from_scratch.py` có comment chi tiết.
- **KPI nghiệm thu**: Mã hóa và giải mã thành công một chuỗi văn bản với cặp số nguyên tố tự sinh.

---

### Tuần 4: Xây Dựng Hạ Tầng PKI Root CA Với OpenSSL & Soi Bắt Tay TLS 1.3
- **Lý thuyết**: Hàm băm an toàn SHA-256 (tính chất kháng tiền ảnh & kháng va chạm), Mã xác thực thông điệp HMAC, Chữ ký số, Cấu trúc chứng chỉ số X.509, Cơ chế thẩm định CA chuỗi tin cậy (Chain of Trust), Giao thức TLS 1.3 1-RTT.
- **Thực hành (Lab)**:
  - Dùng OpenSSL CLI dựng hạ tầng PKI nội bộ:
    ```bash
    # 1. Tạo Root CA
    openssl req -x509 -newkey rsa:2048 -nodes -keyout rootCA.key -out rootCA.crt -days 365
    # 2. Tạo CSR và ký chứng chỉ cho Web Server nội bộ
    openssl req -newkey rsa:2048 -nodes -keyout web.key -out web.csr
    openssl x509 -req -in web.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out web.crt -days 180
    ```
  - Bắt gói tin Wireshark khi truy cập web HTTPS: Phân tích các trường trong bản tin `Client Hello` (Cipher Suites, Server Name Indication - SNI, Key Share extension).
- **Sản phẩm bàn giao**: Thư mục chứng chỉ số và file `.pcapng` bắt gói tin TLS dán vào `04_Notion_Digital_Workspace/`.
- **KPI nghiệm thu**: Trình duyệt tin cậy chứng chỉ số nội bộ (hiện ổ khóa xanh); phân tích rõ ràng luồng bắt tay TLS 1.3 trên Wireshark.
