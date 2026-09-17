# 🍌 BÁO CÁO THIẾT KẾ & TRIỂN KHAI HỆ THỐNG MẠNG TRƯỜNG CAO ĐẲNG BANANA (LAB 4)

> **Mã học phần**: NMA-DUT (Quản trị Mạng & Hệ thống) — Đại học Bách khoa – ĐH Đà Nẵng  
> **Chủ đề**: Phân hoạch địa chỉ mạng VLSM ($10.0.0.0/19$), Định tuyến Inter-VLAN (Router-on-a-Stick), Dịch vụ Internet (NAT Overload/PAT + Default Route), Cấp phát DHCP đa vùng, Mạng không dây (Free Wi-Fi Lớp học) và Bảo mật Doanh nghiệp Văn phòng (WPA2-Enterprise RADIUS 802.1X + MAC Filtering + Port Security).  
> **Địa bàn áp dụng**: Trường Cao Đẳng Banana.  
> **Tài liệu tham chiếu**: Bộ hình ảnh bài giảng & bài giải viết tay trên bảng/giấy (`Ảnh 1, 2: Bảng đen tính toán u=19` và `Ảnh 3, 4: Giấy nháp phân tích trường hợp`).  
> **Tác giả / Mentor chuyên trách**: DUT Network Admin Mentor (NetAdmin Corp).  

---

## 📑 MỤC LỤC

1. [Phần 1: Bối Cảnh, Đề Bài & Phân Tích Hình Ảnh Kỹ Thuật Thực Tế](#phần-1-bối-cảnh-đề-bài--phân-tích-hình-ảnh-kỹ-thuật-thực-tế)
   - [1.1. Mô tả yêu cầu đề bài](#11-mô-tả-yêu-cầu-đề-bài)
   - [1.2. Phân tích chi tiết 4 hình ảnh tính toán trên bảng & giấy nháp](#12-phân-tích-chi-tiết-4-hình-ảnh-tính-toán-trên-bảng--giấy-nháp)
   - [1.3. Đánh giá & Nhận xét phản biện: Cách tính trên bảng đã chuẩn VLSM chưa?](#13-đánh-giá--nhận-xét-phản-biện-cách-tính-trên-bảng-đã-chuẩn-vlsm-chưa)
2. [Phần 2: Tái Thiết Kế Phân Hoạch Địa Chỉ Mạng VLSM Hoàn Chỉnh & Chính Xác 100%](#phần-2-tái-thiết-kế-phân-hoạch-địa-chỉ-mạng-vlsm-hoàn-chỉnh--chính-xác-100)
   - [2.1. Phân tích mạng tổng 10.0.0.0/19](#21-phân-tích-mạng-tổng-1000019)
   - [2.2. Quy tắc vàng trong kỹ thuật VLSM](#22-quy-tắc-vàng-trong-kỹ-thuật-vlsm)
   - [2.3. Các bước tính toán chi tiết từng mạng con](#23-các-bước-tính-toán-chi-tiết-từng-mạng-con)
   - [2.4. Bảng tổng hợp phân hoạch VLSM chuẩn mực](#24-bảng-tổng-hợp-phân-hoạch-vlsm-chuẩn-mực)
3. [Phần 3: Bảng Phân Bổ Địa Chỉ IP & Sơ Đồ Topo Mạng Chuẩn Hóa](#phần-3-bảng-phân-bổ-địa-chỉ-ip--sơ-đồ-topo-mạng-chuẩn-hóa)
   - [3.1. Sơ đồ kiến trúc kết nối Topo mạng](#31-sơ-đồ-kiến-trúc-kết-nối-topo-mạng)
   - [3.2. Bảng phân bổ IP chi tiết từng thiết bị](#32-bảng-phân-bổ-ip-chi-tiết-từng-thiết-bị)
4. [Phần 4: Bản Chất Cốt Lõi Kỹ Thuật (Tại Sao Phải Thiết Kế Như Vậy?)](#phần-4-bản-chất-cốt-lõi-kỹ-thuật-tại-sao-phải-thiết-kế-như-vậy)
5. [Phần 5: Hướng Dẫn Thao Tác Cấu Hình Chi Tiết Từng Bước (Làm Thế Nào?)](#phần-5-hướng-dẫn-thao-tác-cấu-hình-chi-tiết-từng-bước-làm-thế-nào)
   - [Bước 1: Cấu hình Core Switch (Phân chia VLAN 10, 20, 30 & Trunking)](#bước-1-cấu-hình-core-switch-phân-chia-vlan-10-20-30--trunking)
   - [Bước 2: Cấu hình Router Banana (Sub-interfaces + DHCP Multi-Pool + PAT + Default Route)](#bước-2-cấu-hình-router-banana-sub-interfaces--dhcp-multi-pool--pat--default-route)
   - [Bước 3: Cấu hình Mạng Không Dây Lớp Học (Free Wi-Fi)](#bước-3-cấu-hình-mạng-không-dây-lớp-học-free-wi-fi)
   - [Bước 4: Cấu hình Mạng Phòng Thí Nghiệm (Wired Only)](#bước-4-cấu-hình-mạng-phòng-thí-nghiệm-wired-only)
   - [Bước 5: Cấu hình Bảo Mật Văn Phòng (RADIUS Server 802.1X + Wi-Fi MAC Filter + Port Security)](#bước-5-cấu-hình-bảo-mật-văn-phòng-radius-server-8021x--wi-fi-mac-filter--port-security)
   - [Bước 6: Cấu hình Phía Nhà Mạng ISP & DNS](#bước-6-cấu-hình-phía-nhà-mạng-isp--dns)
6. [Phần 6: Kịch Bản Kiểm Thử & Nghiệm Thu Cho Giảng Viên Chấm Điểm 10/10](#phần-6-kịch-bản-kiểm-thử--nghiệm-thu-cho-giảng-viên-chấm-điểm-1010)
7. [Phần 7: Cảnh Báo Bẫy Kỹ Thuật & Khắc Phục Sự Cố (Troubleshooting)](#phần-7-cảnh-báo-bẫy-kỹ-thuật--khắc-phục-sự-cố-troubleshooting)
8. [Phần 8: Bộ Câu Hỏi Vấn Đáp Bảo Vệ Đạt Điểm Tuyệt Đối](#phần-8-bộ-câu-hỏi-vấn-đáp-bảo-vệ-đạt-điểm-tuyệt-đối)

---

## PHẦN 1: BỐI CẢNH, ĐỀ BÀI & PHÂN TÍCH HÌNH ẢNH KỸ THUẬT THỰC TẾ

### 1.1. Mô tả yêu cầu đề bài
Hệ thống mạng Trường Cao Đẳng Banana cần được quy hoạch và triển khai đáp ứng:
- **Đường truyền Internet**: Trường thuê bao đường truyền kết nối với ISP qua địa chỉ IP Public lớp WAN. Toàn bộ thiết bị trong trường phải truy cập được Internet thông qua kỹ thuật biên dịch địa chỉ NAT Overload (PAT).
- **Mạng tổng cấp phát**: Mạng Private Class A dạng $10.0.0.0/u$. Cần tìm tiền tố $u$ và phân hoạch chi tiết.
- **3 Khu vực chức năng**:
  1. **Lớp học (Classrooms)**: Quy mô **969 sinh viên**. Mỗi sinh viên sử dụng trung bình **2 thiết bị không dây** (1 Smartphone + 1 Laptop/Tablet) $\implies \mathbf{1938\text{ thiết bị}}$, sử dụng **kết nối Wi-Fi miễn phí (Free Wi-Fi)**.
  2. **Phòng thí nghiệm (Labs)**: Quy mô **400 máy tính**, chỉ sử dụng **kết nối có dây (Wired only)**.
  3. **Văn phòng (Office)**: Quy mô **69 nhân viên**. Mỗi nhân viên sử dụng **2 thiết bị** (1 máy tính bàn có dây + 1 thiết bị di động/laptop Wi-Fi) $\implies \mathbf{138\text{ thiết bị}}$. Yêu cầu bảo mật cấp cao: **Xác thực tập trung qua RADIUS Server (802.1X)** kết hợp **Lọc địa chỉ vật lý MAC (MAC Filtering / Port Security)**.
- **Tổng số thiết bị cần cấp phát**: $1938 + 400 + 138 = \mathbf{2476\text{ hosts}}$.

---

### 1.2. Phân tích chi tiết 4 hình ảnh tính toán trên bảng & giấy nháp

Trong buổi học thực tế trên lớp, giảng viên và sinh viên đã thực hiện tính toán trên bảng đen và giấy nháp (thể hiện qua 4 bức ảnh tài liệu):

```
+-------------------------------------------------------------------------------------------------------------+
|                                    TỔNG QUAN NỘI DUNG 4 ẢNH TƯ LIỆU THỰC TẾ                                  |
|                                                                                                             |
| [Ảnh 1 - Bảng đen 1]: Ghi công thức xuất phát:                                                              |
|   10.0.0.0/u  (u = ?)                                                                                       |
|   (S) <= 2^n                                                                                                |
|   (h) <= 2^(32 - u - n) - 2                                                                                 |
|                                                                                                             |
| [Ảnh 2 - Bảng đen 2]: Thay số tính toán tiền tố u:                                                          |
|   S = 3 <= 2^n  => n = 2                                                                                    |
|   h = 969 * 2 <= 2^(32 - u - n) - 2                                                                         |
|   n = 2 => 1938 <= 2^(30 - u) - 2                                                                           |
|   2048 IPs = 2^11 = 2^(30 - u) > 1940                                                                       |
|   => 30 - u = 11 => u = 19                                                                                  |
|                                                                                                             |
| [Ảnh 3 - Giấy nháp kẻ ngang]: Sinh viên thử tính riêng cho từng phòng:                                      |
|   Lớp: h = 969 * 2 <= 2^(30 - u) - 2 => 2048 IPs = 2^11 = 2^(30 - u) > 1940 => u = 19                      |
|   Labs: h = 400 <= 2^(30 - u) - 2 => 402 <= 2^(30 - u) => u = 21                                            |
|   VP: h = 69 * 2 <= 2^(30 - u) - 2 => 256 IPs = 2^8 <= 2^(30 - u) > 138 => u = 22                           |
|                                                                                                             |
| [Ảnh 4 - Giấy nháp trắng A4]: Sinh viên so sánh 2 trường hợp:                                               |
|   TH1: Không mượn n bit: Lớp h = 969 * 2 <= 2^(32 - u) - 2 => 2^11 <= 2^(32 - u) => u = 21                |
|   Tổng host: 1938 + 400 + 138 = 2476 hosts => Mạng tổng cần 2^12 = 4096 IP => 10.0.0.0/20                  |
+-------------------------------------------------------------------------------------------------------------+
```

---

### 1.3. Đánh giá & Nhận xét phản biện: Cách tính trên bảng đã chuẩn VLSM chưa?

> 🛑 **KẾT LUẬN CỦA DUT NETWORK ADMIN MENTOR**:  
> **CÁCH TÍNH TOÁN TRÊN BẢNG VÀ TRONG GIẤY NHÁP Ở CẢ 4 ẢNH CHƯA PHẢI LÀ CHUẨN VLSM! ĐÂY LÀ SỰ NHẦM LẪN KINH ĐIỂN GIỮA PHƯƠNG PHÁP FLSM VÀ VLSM!**

#### ❌ Phân tích các sai lầm kỹ thuật cốt lõi trong các ảnh:

1. **Nhầm lẫn giữa FLSM (Fixed Length) và VLSM (Variable Length)**:
   - Công thức $S \le 2^n$ và $h \le 2^{32 - u - n} - 2$ (Ảnh 1 & Ảnh 2) là **công thức định nghĩa của FLSM (Chia mạng con có độ dài cố định)**.
   - Trong FLSM, người ta mượn cố định $n = 2\text{ bit}$ từ mạng tổng để chia đều thành $2^2 = 4$ mạng con có **cùng một kích thước và cùng một Subnet Mask** là:
     $$\text{Mask}_{\text{chung}} = /(u + n) = /(19 + 2) = \mathbf{/21} \quad (2048\text{ IP/mạng con})$$
   - **Hậu quả lãng phí tài nguyên khủng khiếp của FLSM**:
     - *Phân đoạn Lớp học*: Cần 1938 IP $\implies$ nhận mạng $/21$ (2046 host khả dụng) $\implies$ Đủ.
     - *Phân đoạn Phòng Lab*: Chỉ cần 400 IP $\implies$ nhưng lại bị ép dùng mạng $/21$ (2046 host khả dụng) $\implies$ **Lãng phí tới $2046 - 400 = 1646\text{ địa chỉ IP}$ (Lãng phí hơn $80\%$ không gian)!**
     - *Phân đoạn Văn phòng*: Chỉ cần 138 IP $\implies$ nhưng cũng bị ép dùng mạng $/21$ (2046 host khả dụng) $\implies$ **Lãng phí tới $2046 - 138 = 1908\text{ địa chỉ IP}$ (Lãng phí hơn $93\%$ không gian)!**
   - Điều này đi ngược lại hoàn toàn tôn chỉ ra đời của kỹ thuật VLSM: *"Tối ưu hóa không gian địa chỉ, mạng cần bao nhiêu thì cấp bấy nhiêu, không cấp thừa!"*

2. **Lỗi ngộ nhận khái niệm toán học trong Ảnh 3**:
   - Trong Ảnh 3, sinh viên nhận thấy Lab và Văn phòng không cần nhiều IP đến thế nên đã cố tính riêng:
     - Lớp: $u = 19$
     - Lab: $u = 21$
     - Văn phòng: $u = 22$
   - Đây là **lỗi sai bản chất**: Mạng tổng của cả Trường Banana là $10.0.0.0/u$ do cơ quan viễn thông cấp phát, nó chỉ có **MỘT giá trị tiền tố $u$ duy nhất**. Không thể có chuyện mạng tổng của trường vừa là $/19$, vừa là $/21$, vừa là $/22$!
   - Các giá trị $/21$, $/23$, $/24$ mà sinh viên tính ra thực chất là **Subnet Mask riêng biệt của từng mạng con trong VLSM**, chứ không phải là tiền tố của mạng tổng!

3. **Phân tích phát hiện trong Ảnh 4**:
   - Sinh viên đã rất nhạy bén khi cộng dồn tổng số host thực tế:
     $$\text{Tổng host} = 1938 + 400 + 138 = \mathbf{2476\text{ hosts}}$$
   - Vì $2^{11} = 2048 < 2476 < 2^{12} = 4096$, nên về mặt lý thuyết, nếu nhà trường chỉ cần một mạng tổng vừa khít nhu cầu thì mạng **$10.0.0.0/20$** ($4096$ IP) là đã đủ chứa toàn bộ trường!
   - Tuy nhiên, khi nhà trường đã chốt được cấp mạng tổng là **$10.0.0.0/19$** ($8192$ IP — dư giả cho cả việc mở rộng các khoa viện sau này), thì quy trình phân hoạch **VLSM chuẩn quốc tế của Cisco** phải được tính toán lại độc lập, không mượn $n$ bit cố định như trên bảng!

---

## PHẦN 2: TÁI THIẾT KẾ PHÂN HOẠCH ĐỊA CHỈ MẠNG VLSM HOÀN CHỈNH & CHÍNH XÁC 100%

### 2.1. Phân tích mạng tổng $10.0.0.0/19$
- **Mạng tổng được cấp**: **$10.0.0.0/19$**
- **Subnet Mask gốc**: `11111111.11111111.11100000.00000000` $\implies$ **$255.255.224.0$**
- **Tổng số địa chỉ IP trong mạng tổng**:
  $$\text{Tổng IP} = 2^{32 - 19} = 2^{13} = \mathbf{8192\text{ địa chỉ IP}}$$
- **Dải địa chỉ của mạng tổng**: Từ `10.0.0.0` đến `10.0.31.255`.

---

### 2.2. Quy tắc vàng trong kỹ thuật VLSM
> 📌 **Nguyên tắc bất di bất dịch của VLSM**:
> 1. Luôn sắp xếp các mạng con theo **nhu cầu số lượng host giảm dần (từ lớn nhất đến nhỏ nhất)**.
> 2. Tính số bit phần Host ($h_i$) riêng biệt cho từng mạng con theo công thức: $2^{h_i} - 2 \ge \text{Nhu cầu}_i$.
> 3. Độ dài tiền tố của từng mạng con được xác định độc lập: $\text{Prefix}_i = 32 - h_i$.
> 4. Thứ tự phân bổ chuẩn xác:  
>    $$\mathbf{Lớp\ học\ (1938\ hosts)} \longrightarrow \mathbf{Phòng\ thí\ nghiệm\ (400\ hosts)} \longrightarrow \mathbf{Văn\ phòng\ (138\ hosts)}$$

---

### 2.3. Các bước tính toán chi tiết từng mạng con

```
Mạng Tổng: 10.0.0.0/19 (8192 IP: 10.0.0.0 -> 10.0.31.255)
+------------------------------------+------------------+----------------+------------------------------------------+
| VLAN 10 - Lớp Học                  | VLAN 20 - Lab    | VLAN 30 - VP   | Dải IP Dự Phòng Cho Tương Lai            |
| 10.0.0.0/21 (2048 IP)              | 10.0.8.0/23      | 10.0.10.0/24   | 10.0.11.0 đến 10.0.31.255                |
| (10.0.0.0 -> 10.0.7.255)           | (512 IP)         | (256 IP)       | (Còn trống 5376 IP cho tòa nhà mới)      |
+------------------------------------+------------------+----------------+------------------------------------------+
```

#### 🔹 BƯỚC 1: Tính toán cho Phân đoạn "LỚP HỌC" (VLAN 10)
- **Nhu cầu thực tế**: $969\text{ sinh viên} \times 2\text{ thiết bị} = \mathbf{1938\text{ thiết bị}}$ (kết nối Wi-Fi miễn phí).
- **Tính số bit phần Host ($h_1$)**:
  $$2^{h_1} - 2 \ge 1938 \implies 2^{h_1} \ge 1940$$
  - Thử $h_1 = 10 \implies 2^{10} = 1024 \implies 1024 - 2 = 1022 < 1938$ (Không đủ!).
  - Thử $h_1 = 11 \implies 2^{11} = 2048 \implies 2048 - 2 = 2046 \ge 1938$ (**Thỏa mãn!**).
- **Số bit mạng (Prefix length)**: $32 - 11 = \mathbf{/21}$.
- **Subnet Mask**: `11111111.11111111.11111000.00000000` $\implies \mathbf{255.255.248.0}$.
- **Bước nhảy (Block size)** tại Octet thứ 3: $256 - 248 = \mathbf{8}$.
- **Thông số mạng Lớp học (VLAN 10)**:
  - **Địa chỉ mạng (Network Address)**: `10.0.0.0/21`
  - **Địa chỉ Host đầu tiên (First Usable IP)**: `10.0.0.1` (dùng làm Default Gateway trên Router)
  - **Địa chỉ Host cuối cùng (Last Usable IP)**: `10.0.7.254`
  - **Địa chỉ Quảng bá (Broadcast Address)**: `10.0.7.255`
  - **Số lượng IP khả dụng**: $2046\text{ địa chỉ}$ (Dư 108 IP dự phòng cho Giảng viên và thiết bị mới).
  - **Mạng tiếp theo bắt đầu từ**: $\mathbf{10.0.8.0}$.

---

#### 🔹 BƯỚC 2: Tính toán cho Phân đoạn "PHÒNG THÍ NGHIỆM" (VLAN 20)
- **Nhu cầu thực tế**: $\mathbf{400\text{ máy tính}}$ (kết nối có dây cố định).
- **Mạng bắt đầu tiếp theo**: `10.0.8.0`.
- **Tính số bit phần Host ($h_2$)**:
  $$2^{h_2} - 2 \ge 400 \implies 2^{h_2} \ge 402$$
  - Thử $h_2 = 8 \implies 2^8 = 256 \implies 256 - 2 = 254 < 400$ (Không đủ!).
  - Thử $h_2 = 9 \implies 2^9 = 512 \implies 512 - 2 = 510 \ge 400$ (**Thỏa mãn!**).
- **Số bit mạng (Prefix length)**: $32 - 9 = \mathbf{/23}$.
- **Subnet Mask**: `11111111.11111111.11111110.00000000` $\implies \mathbf{255.255.254.0}$.
- **Bước nhảy (Block size)** tại Octet thứ 3: $256 - 254 = \mathbf{2}$.
- **Thông số mạng Phòng thí nghiệm (VLAN 20)**:
  - **Địa chỉ mạng (Network Address)**: `10.0.8.0/23`
  - **Địa chỉ Host đầu tiên (First Usable IP)**: `10.0.8.1` (Default Gateway trên Router)
  - **Địa chỉ Host cuối cùng (Last Usable IP)**: `10.0.9.254`
  - **Địa chỉ Quảng bá (Broadcast Address)**: `10.0.9.255`
  - **Số lượng IP khả dụng**: $510\text{ địa chỉ}$ (Dư 110 IP dự phòng cho máy chủ thí nghiệm, máy in).
  - **Mạng tiếp theo bắt đầu từ**: $\mathbf{10.0.10.0}$.

---

#### 🔹 BƯỚC 3: Tính toán cho Phân đoạn "VĂN PHÒNG" (VLAN 30)
- **Nhu cầu thực tế**: $69\text{ nhân viên} \times 2\text{ thiết bị} = \mathbf{138\text{ thiết bị}}$ (sử dụng cả máy tính bàn có dây và Wi-Fi bảo mật).
- **Mạng bắt đầu tiếp theo**: `10.0.10.0`.
- **Tính số bit phần Host ($h_3$)**:
  $$2^{h_3} - 2 \ge 138 \implies 2^{h_3} \ge 140$$
  - Thử $h_3 = 7 \implies 2^7 = 128 \implies 128 - 2 = 126 < 138$ (Không đủ, thiếu 12 IP!).
  - Thử $h_3 = 8 \implies 2^8 = 256 \implies 256 - 2 = 254 \ge 138$ (**Thỏa mãn!**).
- **Số bit mạng (Prefix length)**: $32 - 8 = \mathbf{/24}$.
- **Subnet Mask**: `11111111.11111111.11111111.00000000` $\implies \mathbf{255.255.255.0}$.
- **Bước nhảy (Block size)** tại Octet thứ 3: $1$ (Octet thứ 4 bước nhảy $256$).
- **Thông số mạng Văn phòng (VLAN 30)**:
  - **Địa chỉ mạng (Network Address)**: `10.0.10.0/24`
  - **Địa chỉ Host đầu tiên (First Usable IP)**: `10.0.10.1` (Default Gateway trên Router)
  - **Địa chỉ RADIUS Server (IP Tĩnh)**: `10.0.10.2`
  - **Địa chỉ AP Văn phòng (IP Tĩnh)**: `10.0.10.3`
  - **Địa chỉ Host cuối cùng (Last Usable IP)**: `10.0.10.254`
  - **Địa chỉ Quảng bá (Broadcast Address)**: `10.0.10.255`
  - **Số lượng IP khả dụng**: $254\text{ địa chỉ}$ (Dư 114 IP dự phòng cho cán bộ mới, máy in và thiết bị kiểm soát ra vào).
  - **Mạng tiếp theo bắt đầu từ**: $\mathbf{10.0.11.0}$.

---

### 2.4. Bảng tổng hợp phân hoạch VLSM chuẩn mực

| STT | Phân Đoạn (VLAN) | Nhu Cầu Thực Tế | IP Cung Cấp | Network Address | Subnet Mask | Dải IP Khả Dụng (Usable Range) | Default Gateway | Broadcast Address |
| :---: | :--- | :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Lớp Học (VLAN 10)** | 1938 hosts | 2046 | `10.0.0.0/21` | `255.255.248.0` | `10.0.0.1` – `10.0.7.254` | `10.0.0.1` | `10.0.7.255` |
| **2** | **Phòng Lab (VLAN 20)**| 400 hosts | 510 | `10.0.8.0/23` | `255.255.254.0` | `10.0.8.1` – `10.0.9.254` | `10.0.8.1` | `10.0.9.255` |
| **3** | **Văn Phòng (VLAN 30)** | 138 hosts | 254 | `10.0.10.0/24` | `255.255.255.0` | `10.0.10.1` – `10.0.10.254` | `10.0.10.1` | `10.0.10.255` |
| **-** | *Dải IP dự phòng sạch* | — | **5376** | `10.0.11.0/24` đến `10.0.31.255` | Dành cho mở rộng các viện nghiên cứu, ký túc xá sau này |

---

## PHẦN 3: BẢNG PHÂN BỔ ĐỊA CHỈ IP & SƠ ĐỒ TOPO MẠNG CHUẨN HÓA

### 3.1. Sơ đồ kiến trúc kết nối Topo mạng

```
                                  [ INTERNET / ISP CLOUD ]
                                             |
                                             | (Fa0/0) 203.0.113.1/30
                                     +---------------+
                                     |   ROUTER ISP  |
                                     +---------------+
                                             | (Fa0/1) 203.0.113.2/30 (WAN IP Public)
                                             v
                                  +---------------------+
                                  |    BANANA_ROUTER    |
                                  | (Gateway & PAT Nat) |
                                  +---------------------+
                                             |
                                             | Đường Trunk 802.1Q (Fa0/1)
                                             v
                                  +---------------------+
                                  |     CORE_SWITCH     |
                                  |  (Cisco Catalyst)   |
                                  +---------------------+
                                  /          |          \
                 (Fa0/2 - VLAN 10)          |Fa0/3       \(Fa0/4 - VLAN 30)
                                /       (VLAN 20)         \
                               v             v             v
                     +---------------+  +----------+  +---------------+
                     | AP_CLASSROOM  |  | PC_LAB   |  | SW_OFFICE     |
                     | (Free Wi-Fi)  |  | (Wired)  |  | (VLAN 30)     |
                     +---------------+  +----------+  +---------------+
                            |                               /        \
                   (Sóng không dây)                        v          v
                            v                        +-----------+ +------------+
                     [ Laptop Sinh Viên ]            | RADIUS-SRV| | AP_OFFICE  |
                     (10.0.0.x /21 DHCP)             | (10.0.10.2)| | (WPA2-Ent) |
                                                     +-----------+ +------------+
                                                                         |
                                                                 (EAP-RADIUS + MAC Filter)
                                                                         v
                                                                  [ Laptop Nhân Viên ]
```

---

### 3.2. Bảng phân bổ IP chi tiết từng thiết bị

| Thiết bị (Device) | Interface | Địa chỉ IP / Prefix | Default Gateway | VLAN ID | Chức năng / Dịch vụ đảm nhiệm |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BANANA_ROUTER** | `Fa0/0` (WAN) | `203.0.113.2/30` | `203.0.113.1` | N/A | Cổng WAN ra Internet (`ip nat outside`) |
| | `Fa0/1` (LAN) | Unassigned | N/A | N/A | Cổng vật lý Trunking nối Core Switch |
| | `Fa0/1.10` | `10.0.0.1/21` | N/A | VLAN 10 | Gateway Lớp học (`ip nat inside`, DHCP Pool) |
| | `Fa0/1.20` | `10.0.8.1/23` | N/A | VLAN 20 | Gateway Phòng lab (`ip nat inside`, DHCP Pool) |
| | `Fa0/1.30` | `10.0.10.1/24` | N/A | VLAN 30 | Gateway Văn phòng (`ip nat inside`, DHCP Pool) |
| **CORE_SWITCH** | `Vlan 1` (Mgmt) | `10.0.10.254/24` | `10.0.10.1` | VLAN 1 | Quản trị thiết bị Switch từ xa qua SSH |
| | `Fa0/1` | Trunking 802.1Q | N/A | 10,20,30 | Kết nối Router biên Banana |
| | `Fa0/2` | Access VLAN 10 | N/A | VLAN 10 | Nối Access Point Lớp học (`AP_CLASSROOM`) |
| | `Fa0/3` | Access VLAN 20 | N/A | VLAN 20 | Nối Switch nhánh / Máy tính Phòng Lab |
| | `Fa0/4` | Access VLAN 30 | N/A | VLAN 30 | Nối Switch Văn phòng / Cụm máy Văn phòng |
| **AP_CLASSROOM** | `Port 0` (Wired) | N/A (L2 Bridge) | N/A | VLAN 10 | Cầu nối không dây Lớp học |
| | `Port 1` (SSID) | `Banana_Free_WiFi`| N/A | VLAN 10 | Không mật khẩu, kết nối tự do |
| **RADIUS_SERVER** | `Fa0` | `10.0.10.2/24` | `10.0.10.1` | VLAN 30 | Máy chủ xác thực AAA (Port 1812 UDP) |
| **AP_OFFICE** | `Port 0` (Wired) | `10.0.10.3/24` (hoặc L2)| `10.0.10.1` | VLAN 30 | AP Văn phòng bảo mật |
| | `Port 1` (SSID) | `Banana_Office_Secure` | N/A | VLAN 30 | Xác thực WPA2-Enterprise + Lọc MAC |
| **ROUTER_ISP** | `Fa0/0` | `203.0.113.1/30` | N/A | N/A | Gateway nhà mạng ISP |
| | `Fa0/1` | `8.8.8.1/24` | N/A | N/A | Mạng dịch vụ Internet (Google DNS) |
| **GOOGLE_DNS** | `Fa0` | `8.8.8.8/24` | `8.8.8.1` | N/A | Máy chủ DNS công cộng kiểm thử |

---

## PHẦN 4: BẢN CHẤT CỐT LÕI KỸ THUẬT (TẠI SAO PHẢI THIẾT KẾ NHƯ VẬY?)

```
+---------------------------------------------------------------------------------------------------------+
|                                    CỐT LÕI KỸ THUẬT TRƯỜNG BANANA (LAB 4)                               |
|                                                                                                         |
| 1. Kỹ thuật VLSM (Variable Length Subnet Masking):                                                      |
|    - Cắt các mặt nạ không đồng đều (/21 cho Lớp, /23 cho Lab, /24 cho Văn phòng).                      |
|    - Giúp tiết kiệm tới hơn 3300 địa chỉ IP so với FLSM, để dành không gian liên tục 10.0.11.0/24 đến   |
|      10.0.31.255 cho phát triển sau này.                                                                |
|                                                                                                         |
| 2. Kỹ thuật PAT (Port Address Translation / NAT Overload):                                              |
|    - Tổng quy mô: 1938 + 400 + 138 = 2476 host trong mạng nội bộ. Nhà mạng ISP chỉ cấp đúng 1 IP WAN   |
|      Public (203.0.113.2). PAT sử dụng số hiệu Port TCP/UDP (16-bit: 1024 - 65535) để cho phép hàng    |
|      nghìn thiết bị cùng truy cập Internet đồng thời qua 1 IP duy nhất.                                 |
|                                                                                                         |
| 3. Bảo mật Văn phòng đa tầng (Defense-in-Depth):                                                        |
|    - Tầng logic (Identity): Xác thực 802.1X RADIUS yêu cầu mỗi nhân viên phải dùng tài khoản cá nhân     |
|      riêng (nhanvien01 / Banana@Password123), chấm dứt hoàn toàn nguy cơ lộ mật khẩu chung WPA2-PSK.   |
|    - Tầng vật lý (Hardware): Lọc địa chỉ MAC (White-list) trên AP và Port Security trên Switch. Kẻ xấu |
|      có lấy cắp được tài khoản nhân viên nhưng dùng máy tính lạ thì vẫn bị chặn ngay từ cổng vào!       |
+---------------------------------------------------------------------------------------------------------+
```

---

## PHẦN 5: HƯỚNG DẪN THAO TÁC CẤU HÌNH CHI TIẾT TỪNG BƯỚC (LÀM THẾ NÀO?)

### Bước 1: Cấu hình Core Switch (Phân chia VLAN 10, 20, 30 & Trunking)

Mở CLI của **CORE_SWITCH (Cisco 2960)**:

```cisco
Switch> enable
Switch# configure terminal
Switch(config)# hostname CORE_SWITCH

! --- 1. Tạo các VLAN tương ứng với 3 phân đoạn mạng ---
CORE_SWITCH(config)# vlan 10
CORE_SWITCH(config-vlan)# name VLAN10_LOPHOC
CORE_SWITCH(config-vlan)# exit

CORE_SWITCH(config)# vlan 20
CORE_SWITCH(config-vlan)# name VLAN20_PHONGTHI_NGHIEM
CORE_SWITCH(config-vlan)# exit

CORE_SWITCH(config)# vlan 30
CORE_SWITCH(config-vlan)# name VLAN30_VANPHONG
CORE_SWITCH(config-vlan)# exit

! --- 2. Cổng Fa0/1 làm đường Trunk 802.1Q nối Router Banana ---
CORE_SWITCH(config)# interface FastEthernet 0/1
CORE_SWITCH(config-if)# switchport mode trunk
CORE_SWITCH(config-if)# no shutdown
CORE_SWITCH(config-if)# exit

! --- 3. Cổng Fa0/2 gán vào VLAN 10 nối AP Lớp học ---
CORE_SWITCH(config)# interface FastEthernet 0/2
CORE_SWITCH(config-if)# switchport mode access
CORE_SWITCH(config-if)# switchport access vlan 10
CORE_SWITCH(config-if)# spanning-tree portfast          ! Chuyển trạng thái tức thì cho AP
CORE_SWITCH(config-if)# no shutdown
CORE_SWITCH(config-if)# exit

! --- 4. Cổng Fa0/3 gán vào VLAN 20 nối Phòng Lab ---
CORE_SWITCH(config)# interface FastEthernet 0/3
CORE_SWITCH(config-if)# switchport mode access
CORE_SWITCH(config-if)# switchport access vlan 20
CORE_SWITCH(config-if)# spanning-tree portfast
CORE_SWITCH(config-if)# no shutdown
CORE_SWITCH(config-if)# exit

! --- 5. Cổng Fa0/4 gán vào VLAN 30 nối Văn phòng ---
CORE_SWITCH(config)# interface FastEthernet 0/4
CORE_SWITCH(config-if)# switchport mode access
CORE_SWITCH(config-if)# switchport access vlan 30
CORE_SWITCH(config-if)# spanning-tree portfast
CORE_SWITCH(config-if)# no shutdown
CORE_SWITCH(config-if)# exit

! --- 6. Cấu hình IP quản trị Switch tại VLAN 1 ---
CORE_SWITCH(config)# interface Vlan 1
CORE_SWITCH(config-if)# ip address 10.0.10.254 255.255.255.0
CORE_SWITCH(config-if)# no shutdown
CORE_SWITCH(config-if)# exit
CORE_SWITCH(config)# ip default-gateway 10.0.10.1

CORE_SWITCH(config)# end
CORE_SWITCH# write memory
```

---

### Bước 2: Cấu hình Router Banana (Sub-interfaces + DHCP Multi-Pool + PAT + Default Route)

Mở CLI của **BANANA_ROUTER (Cisco 2811/2911)**:

```cisco
Router> enable
Router# configure terminal
hostname BANANA_ROUTER

! ==============================================================================
! PHẦN A: CẤU HÌNH SUB-INTERFACES ĐỊNH TUYẾN LIÊN VLAN (ROUTER-ON-A-STICK)
! ==============================================================================
BANANA_ROUTER(config)# interface FastEthernet 0/1
BANANA_ROUTER(config-if)# no ip address
BANANA_ROUTER(config-if)# no shutdown                   ! Bật cổng vật lý
BANANA_ROUTER(config-if)# exit

! 1. Sub-interface cho VLAN 10 (Lớp học: 10.0.0.0/21)
BANANA_ROUTER(config)# interface FastEthernet 0/1.10
BANANA_ROUTER(config-subif)# encapsulation dot1Q 10
BANANA_ROUTER(config-subif)# ip address 10.0.0.1 255.255.248.0   ! Subnet Mask /21 chuẩn
BANANA_ROUTER(config-subif)# ip nat inside
BANANA_ROUTER(config-subif)# exit

! 2. Sub-interface cho VLAN 20 (Phòng Lab: 10.0.8.0/23)
BANANA_ROUTER(config)# interface FastEthernet 0/1.20
BANANA_ROUTER(config-subif)# encapsulation dot1Q 20
BANANA_ROUTER(config-subif)# ip address 10.0.8.1 255.255.254.0   ! Subnet Mask /23 chuẩn
BANANA_ROUTER(config-subif)# ip nat inside
BANANA_ROUTER(config-subif)# exit

! 3. Sub-interface cho VLAN 30 (Văn phòng: 10.0.10.0/24)
BANANA_ROUTER(config)# interface FastEthernet 0/1.30
BANANA_ROUTER(config-subif)# encapsulation dot1Q 30
BANANA_ROUTER(config-subif)# ip address 10.0.10.1 255.255.255.0  ! Subnet Mask /24 chuẩn
BANANA_ROUTER(config-subif)# ip nat inside
BANANA_ROUTER(config-subif)# exit

! ==============================================================================
! PHẦN B: CẤU HÌNH CỔNG WAN & TUYẾN ĐỊNH TUYẾN MẶC ĐỊNH (DEFAULT ROUTE)
! ==============================================================================
BANANA_ROUTER(config)# interface FastEthernet 0/0
BANANA_ROUTER(config-if)# ip address 203.0.113.2 255.255.255.252
BANANA_ROUTER(config-if)# ip nat outside
BANANA_ROUTER(config-if)# no shutdown
BANANA_ROUTER(config-if)# exit

! Trỏ Default Route về địa chỉ IP của Router ISP
BANANA_ROUTER(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.1

! ==============================================================================
! PHẦN C: CẤU HÌNH DỊCH VỤ DHCP SERVER CHO CẢ 3 VÙNG MẠNG
! ==============================================================================
! Loại trừ các địa chỉ IP Gateway và máy chủ cố định
BANANA_ROUTER(config)# ip dhcp excluded-address 10.0.0.1 10.0.0.9
BANANA_ROUTER(config)# ip dhcp excluded-address 10.0.8.1 10.0.8.9
BANANA_ROUTER(config)# ip dhcp excluded-address 10.0.10.1 10.0.10.9

! 1. Pool cấp phát cho Lớp học (VLAN 10)
BANANA_ROUTER(config)# ip dhcp pool POOL_LOPHOC
BANANA_ROUTER(dhcp-config)# network 10.0.0.0 255.255.248.0
BANANA_ROUTER(dhcp-config)# default-router 10.0.0.1
BANANA_ROUTER(dhcp-config)# dns-server 8.8.8.8
BANANA_ROUTER(dhcp-config)# exit

! 2. Pool cấp phát cho Phòng Lab (VLAN 20)
BANANA_ROUTER(config)# ip dhcp pool POOL_PHONGLAB
BANANA_ROUTER(dhcp-config)# network 10.0.8.0 255.255.254.0
BANANA_ROUTER(dhcp-config)# default-router 10.0.8.1
BANANA_ROUTER(dhcp-config)# dns-server 8.8.8.8
BANANA_ROUTER(dhcp-config)# exit

! 3. Pool cấp phát cho Văn phòng (VLAN 30)
BANANA_ROUTER(config)# ip dhcp pool POOL_VANPHONG
BANANA_ROUTER(dhcp-config)# network 10.0.10.0 255.255.255.0
BANANA_ROUTER(dhcp-config)# default-router 10.0.10.1
BANANA_ROUTER(dhcp-config)# dns-server 8.8.8.8
BANANA_ROUTER(dhcp-config)# exit

! ==============================================================================
! PHẦN D: CẤU HÌNH BIÊN DỊCH ĐỊA CHỈ NAT OVERLOAD (PAT)
! ==============================================================================
! Cho phép toàn bộ dải mạng tổng 10.0.0.0/19 (Wildcard Mask: 0.0.31.255)
BANANA_ROUTER(config)# access-list 1 permit 10.0.0.0 0.0.31.255
BANANA_ROUTER(config)# ip nat inside source list 1 interface FastEthernet 0/0 overload

BANANA_ROUTER(config)# end
BANANA_ROUTER# write memory
```

---

### Bước 3: Cấu hình Mạng Không Dây Lớp Học (Free Wi-Fi)

1. Nhấp chọn thiết bị **AP_CLASSROOM** (AccessPoint-PT) nối vào `Fa0/2` của Core Switch $\rightarrow$ tab **Config**.
2. Chọn cổng **Port 1** (Wireless):
   - **SSID**: Đặt tên là `Banana_Free_WiFi`.
   - **Authentication**: Chọn **Disabled** (Mạng không dây mở, hoàn toàn miễn phí, không mật khẩu).
3. **Thử nghiệm trên Laptop Sinh viên**:
   - Gắn card mạng không dây **WPC300N** vào Laptop $\rightarrow$ Bật nguồn lại.
   - Mở **Desktop** $\rightarrow$ **PC Wireless** $\rightarrow$ chọn tab **Connect** $\rightarrow$ kết nối mạng `Banana_Free_WiFi`.
   - Mở **Command Prompt**, gõ `ipconfig /all`: Laptop tự động nhận IP trong dải `10.0.0.x /21`, Gateway `10.0.0.1`, DNS `8.8.8.8`.

---

### Bước 4: Cấu hình Mạng Phòng Thí Nghiệm (Wired Only)

1. Nối dây cáp mạng thẳng từ card mạng `Fa0` của máy tính phòng Lab vào cổng `Fa0/3` của Switch.
2. Mở máy tính **PC_LAB** $\rightarrow$ **Desktop** $\rightarrow$ **IP Configuration** $\rightarrow$ chọn **DHCP**.
3. **Xác thực**: Máy tính nhận chính xác địa chỉ IP trong dải `10.0.8.x /23`, Subnet Mask `255.255.254.0`, Default Gateway `10.0.8.1`.

---

### Bước 5: Cấu hình Bảo Mật Văn Phòng (RADIUS Server 802.1X + Wi-Fi MAC Filter + Port Security)

#### 1. Cấu hình Máy Chủ Xác Thực RADIUS (AAA Server)
- Đặt một thiết bị **Server-PT** đặt tên là `RADIUS_SERVER`, nối vào cổng thuộc VLAN 30.
- **Thiết lập IP tĩnh**:
  - IP Address: `10.0.10.2`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `10.0.10.1`
- **Kích hoạt Dịch vụ AAA (RADIUS)**:
  - Vào tab **Services** $\rightarrow$ mục **AAA**.
  - Bật radio button **AAA Service**: **ON**.
  - **Khai báo Network Configuration (Đăng ký Client là AP Văn phòng)**:
    - Client Name: `AP_OFFICE`
    - Client IP: `10.0.10.3` (hoặc IP Gateway `10.0.10.1`)
    - Secret: `cisco123` (Mã khóa bí mật chia sẻ giữa AP và Server)
    - Server Type: chọn **Radius** $\rightarrow$ nhấn **Add**.
  - **Tạo tài khoản định danh nhân viên (User Setup)**:
    - Username: `nhanvien01`
    - Password: `Banana@Password123`
    - Nhấn nút **Add**.

#### 2. Cấu hình AP Văn Phòng (WPA2-Enterprise + Lọc MAC)
- Mở AP Văn phòng:
  - **Cấu hình WPA2-Enterprise (802.1X)**:
    - SSID: `Banana_Office_Secure`
    - Authentication: Chọn **WPA2-Enterprise**.
    - Encryption: **AES**.
    - RADIUS Server IP: Điền `10.0.10.2`.
    - Shared Secret: Điền `cisco123`.
  - **Cấu hình Lọc địa chỉ MAC (Wireless MAC Filter)**:
    - Bật **Enable**. Chọn chế độ **Permit (Allow)**.
    - Nhập địa chỉ MAC card Wi-Fi của Laptop nhân viên (ví dụ: `0001.96A2.69BC`) vào danh sách cho phép.

#### 3. Cấu hình Port Security trên Cổng Switch Văn Phòng
```cisco
CORE_SWITCH(config)# interface FastEthernet 0/4
CORE_SWITCH(config-if)# switchport mode access
CORE_SWITCH(config-if)# switchport access vlan 30

! Kích hoạt Port Security chống cắm máy lạ
CORE_SWITCH(config-if)# switchport port-security
CORE_SWITCH(config-if)# switchport port-security maximum 1
CORE_SWITCH(config-if)# switchport port-security mac-address sticky
CORE_SWITCH(config-if)# switchport port-security violation shutdown
CORE_SWITCH(config-if)# exit
```

---

### Bước 6: Cấu hình Phía Nhà Mạng ISP & DNS

Mở CLI của **ROUTER_ISP**:

```cisco
Router> enable
Router# configure terminal
hostname ISP

! Cổng WAN nối về Router Trường Banana
ISP(config)# interface FastEthernet 0/0
ISP(config-if)# ip address 203.0.113.1 255.255.255.252
ISP(config-if)# no shutdown
ISP(config-if)# exit

! Cổng nối máy chủ Google DNS kiểm thử
ISP(config)# interface FastEthernet 0/1
ISP(config-if)# ip address 8.8.8.1 255.255.255.0
ISP(config-if)# no shutdown
ISP(config-if)# exit

ISP(config)# end
ISP# write memory
```

---

## PHẦN 6: KỊCH BẢN KIỂM THỬ & NGHIỆM THU CHO GIẢNG VIÊN CHẤM ĐIỂM 10/10

### 🎯 CHECKPOINT 1: Nghiệm thu Bảng Định Tuyến & Subnet Masks Độc Lập
Trên Router Banana, gõ lệnh:
```cisco
BANANA_ROUTER# show ip route
```
*Kết quả chuẩn mực*:
```text
Gateway of last resort is 203.0.113.1 to network 0.0.0.0

S*   0.0.0.0/0 [1/0] via 203.0.113.1
     10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
C       10.0.0.0/21 is directly connected, FastEthernet0/1.10
C       10.0.8.0/23 is directly connected, FastEthernet0/1.20
C       10.0.10.0/24 is directly connected, FastEthernet0/1.30
     203.0.113.0/30 is subnetted, 1 subnets
C       203.0.113.0 is directly connected, FastEthernet0/0
```
> **Điểm mấu chốt**: Dòng chữ `variably subnetted, 3 subnets, 3 masks` chứng minh hệ thống đã áp dụng **VLSM chuẩn xác tuyệt đối với 3 mặt nạ khác nhau (/21, /23, /24)**, hoàn toàn không bị gò bó vào 1 mặt nạ /21 như FLSM trên bảng!

---

### 🎯 CHECKPOINT 2: Nghiệm thu Cấp phát DHCP 3 Phân Vùng
```cisco
BANANA_ROUTER# show ip dhcp binding
```
*Kết quả chuẩn mực*:
```text
IP address       Client-ID/Hardware address          Lease expiration        Type
10.0.0.10        0001.96a2.69bc                     --                      Automatic
10.0.8.10        0002.164a.22aa                     --                      Automatic
10.0.10.10       0003.55cc.33dd                     --                      Automatic
```

---

### 🎯 CHECKPOINT 3: Nghiệm thu NAT Overload & Thông Tuyến Internet
Từ máy trạm bất kỳ, thực hiện ping ra ngoài Internet:
```cmd
ping 8.8.8.8
```
Trên Router Banana, kiểm tra bảng chuyển đổi NAT:
```cisco
BANANA_ROUTER# show ip nat translations
```
*Kết quả chuẩn mực*:
```text
Pro Inside global         Inside local          Outside local      Outside global
icmp 203.0.113.2:1        10.0.0.10:1           8.8.8.8:1          8.8.8.8:1
icmp 203.0.113.2:2        10.0.8.10:2           8.8.8.8:2          8.8.8.8:2
icmp 203.0.113.2:3        10.0.10.10:3          8.8.8.8:3          8.8.8.8:3
```

---

## PHẦN 7: CẢNH BÁO BẪY KỸ THUẬT & KHẮC PHỤC SỰ CỐ (TROUBLESHOOTING)

1. **Bẫy nhầm lẫn giữa FLSM và VLSM khi tính toán**:
   - *Sai lầm*: Sinh viên áp dụng công thức $S \le 2^n$ và lấy $n = 2$ mượn cho mọi mạng con $\implies$ Tất cả các phòng đều dùng chung subnet mask $/21$.
   - *Hậu quả*: Bị giảng viên trừ nặng điểm vì lãng phí tới hơn 3500 địa chỉ IP trong phòng Lab và Văn phòng.
   - *Khắc phục*: Tính độc lập số bit host $h_i$ cho từng phân đoạn theo đúng thứ tự giảm dần: Lớp học ($/21$) $\rightarrow$ Lab ($/23$) $\rightarrow$ Văn phòng ($/24$).
2. **Bẫy quên bật `no shutdown` trên cổng vật lý cha Fa0/1**:
   - *Hiện tượng*: Đã cấu hình đầy đủ các sub-interface `Fa0/1.10`, `Fa0/1.20`, `Fa0/1.30` nhưng toàn bộ các sub-interface đều báo trạng thái `line protocol down`.
   - *Nguyên nhân*: Cổng vật lý cha `Fa0/1` vẫn đang ở trạng thái `Administratively down`.
   - *Khắc phục*: Vào `interface Fa0/1` và gõ lệnh `no shutdown`.
3. **Bẫy lệch dải IP của RADIUS Server sau khi đổi VLSM**:
   - *Hiện tượng*: Khi đổi mạng Văn phòng từ `10.0.6.0/25` sang chuẩn mới `10.0.10.0/24`, máy chủ RADIUS nếu không cập nhật IP tĩnh lên `10.0.10.2` thì AP Văn phòng sẽ không thể kết nối tới máy chủ xác thực.
   - *Khắc phục*: Luôn kiểm tra đồng bộ IP của RADIUS Server (`10.0.10.2`), Default Gateway (`10.0.10.1`) và khai báo Client IP trong mục AAA.

---

## PHẦN 8: BỘ CÂU HỎI VẤN ĐÁP BẢO VỆ ĐẠT ĐIỂM TUYỆT ĐỐI

### ❓ Câu hỏi 1: *"Hãy chỉ ra sự khác biệt cốt lõi giữa cách giải trên bảng của lớp (Ảnh 1 & Ảnh 2) và giải pháp thiết kế lại của bạn?"*
* **Trả lời chuẩn DUT**: 
  - Cách giải trên bảng áp dụng phương pháp **FLSM (Fixed Length Subnet Masking)** với công thức $S \le 2^n \implies n = 2$. Do mượn 2 bit cố định cho mọi mạng, cả 3 mạng con đều nhận chung một Subnet Mask là $/21$ ($2048$ IP). Điều này khiến phòng Lab (400 máy) và Văn phòng (138 máy) bị lãng phí hơn 3500 IP.
  - Giải pháp thiết kế lại của em là **VLSM (Variable Length Subnet Masking) chuẩn mực**: Mỗi mạng con được cấp một mặt nạ riêng biệt phù hợp hoàn hảo với số lượng host thực tế: Lớp học nhận **/21** ($2046$ IP), Phòng Lab nhận **/23** ($510$ IP), và Văn phòng nhận **/24** ($254$ IP). Nhờ đó, em bảo toàn được dải IP dự phòng liên tục từ `10.0.11.0` đến `10.0.31.255` (dư hơn 5300 IP sạch cho các dự án sau này).

### ❓ Câu hỏi 2: *"Tại sao trong bảng tính toán ở Ảnh 3, việc sinh viên ghi $u=19$ cho lớp, $u=21$ cho lab và $u=22$ cho văn phòng lại là một sai lầm về mặt khái niệm?"*
* **Trả lời chuẩn DUT**: Vì $u$ là tiền tố của **mạng tổng $10.0.0.0/u$** được cấp phát bởi nhà mạng cho toàn bộ nhà trường. Trường học chỉ có một mạng tổng duy nhất nên $u$ chỉ có một giá trị duy nhất (ở đây là $u = 19$). Các con số $/21$, $/23$, $/24$ là **độ dài mặt nạ Subnet Mask của từng mạng con** được cắt nhỏ ra từ mạng tổng, không được đánh đồng với tiền tố $u$ của mạng tổng.

### ❓ Câu hỏi 3: *"Tại sao mạng Văn phòng đã trang bị xác thực 802.1X RADIUS rồi mà vẫn bắt buộc phải cấu hình thêm MAC Filtering và Switch Port Security?"*
* **Trả lời chuẩn DUT**: Đây là mô hình phòng thủ theo chiều sâu (**Defense-in-Depth**):
  - Xác thực RADIUS bảo vệ ở **Tầng Logic / Định danh (Who you are)**: Đảm bảo người đăng nhập là nhân viên hợp lệ có Username/Password.
  - Lọc MAC và Port Security bảo vệ ở **Tầng Vật lý / Thiết bị (What device you use)**: Ngăn chặn triệt để trường hợp nhân viên vô tình hay cố ý mang laptop cá nhân hoặc thiết bị lạ ngoài luồng cắm vào mạng nội bộ (nguy cơ lây nhiễm mã độc, botnet). Một kết nối chỉ thành công khi vừa có tài khoản nhân viên, vừa sử dụng đúng thiết bị phần cứng được nhà trường phê duyệt!
