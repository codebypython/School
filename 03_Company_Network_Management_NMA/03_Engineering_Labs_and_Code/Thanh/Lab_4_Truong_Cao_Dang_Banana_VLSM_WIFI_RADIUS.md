# 🍌 BÁO CÁO THIẾT KẾ & TRIỂN KHAI HỆ THỐNG MẠNG TRƯỜNG CAO ĐẲNG BANANA (LAB 4)

> **Mã học phần**: NMA-DUT (Quản trị Mạng & Hệ thống) — Đại học Bách khoa – ĐH Đà Nẵng  
> **Chủ đề**: Phân hoạch địa chỉ mạng VLSM ($10.0.0.0/19$), Định tuyến Inter-VLAN, Dịch vụ Internet (NAT Overload/PAT + Default Route), Cấp phát DHCP đa vùng, Mạng không dây (Free Wi-Fi Lớp học) và Bảo mật Doanh nghiệp Văn phòng (WPA2-Enterprise RADIUS 802.1X + MAC Filtering + Port Security)  
> **Địa bàn áp dụng**: Trường Cao Đẳng Banana  
> **Vị trí lưu trữ**: `lab/Thanh/Lab_4_Truong_Cao_Dang_Banana_VLSM_WIFI_RADIUS.md`

---

## 📑 MỤC LỤC

1. [Phần 1: Bối Cảnh, Đề Bài & Phân Tích Kỹ Thuật Chi Tiết](#phần-1-bối-cảnh-đề-bài--phân-tích-kỹ-thuật-chi-tiết)
2. [Phần 2: Tính Toán Phân Hoạch Địa Chỉ Mạng VLSM (Từng Bước)](#phần-2-tính-toán-phân-hoạch-địa-chỉ-mạng-vlsm-từng-bước)
3. [Phần 3: Bảng Phân Bổ Địa Chỉ IP & Sơ Đồ Topo Mạng Chuẩn](#phần-3-bảng-phân-bổ-địa-chỉ-ip--sơ-đồ-topo-mạng-chuẩn)
4. [Phần 4: Bản Chất Cốt Lõi Kỹ Thuật (Tại Sao Phải Thiết Kế Như Vậy?)](#phần-4-bản-chất-cốt-lõi-kỹ-thuật-tại-sao-phải-thiết-kế-như-vậy)
5. [Phần 5: Hướng Dẫn Thao Tác Cấu Hình Chi Tiết Từng Bước (Làm Thế Nào?)](#phần-5-hướng-dẫn-thao-tác-cấu-hình-chi-tiết-từng-bước-làm-thế-nào)
   - [Bước 1: Cấu hình Switch Trung tâm (Phân chia VLAN 10, 20, 30 & Trunking)](#bước-1-cấu-hình-switch-trung-tâm-phân-chia-vlan-10-20-30--trunking)
   - [Bước 2: Cấu hình Router Biên Trường Banana (Inter-VLAN + DHCP Multi-Pool + PAT + Default Route)](#bước-2-cấu-hình-router-biên-trường-banana-inter-vlan--dhcp-multi-pool--pat--default-route)
   - [Bước 3: Cấu hình Mạng Không Dây Lớp Học (Free Wi-Fi)](#bước-3-cấu-hình-mạng-không-dây-lớp-học-free-wi-fi)
   - [Bước 4: Cấu hình Mạng Phòng Thí Nghiệm (Wired Only)](#bước-4-cấu-hình-mạng-phòng-thí-nghiệm-wired-only)
   - [Bước 5: Cấu hình Bảo Mật Văn Phòng (RADIUS Server 802.1X + Wi-Fi MAC Filter + Port Security)](#bước-5-cấu-hình-bảo-mật-văn-phòng-radius-server-8021x--wi-fi-mac-filter--port-security)
   - [Bước 6: Cấu hình Phía Nhà Cung Cấp Dịch Vụ Internet (ISP & DNS Test)](#bước-6-cấu-hình-phía-nhà-cung-cấp-dịch-vụ-internet-isp--dns-test)
6. [Phần 6: Kịch Bản Kiểm Thử & Nghiệm Thu Cho Giảng Viên Chấm Điểm](#phần-6-kịch-bản-kiểm-thử--nghiệm-thu-cho-giảng-viên-chấm-điểm)
7. [Phần 7: Cảnh Báo Bẫy Kỹ Thuật & Khắc Phục Sự Cố (Troubleshooting)](#phần-7-cảnh-báo-bẫy-kỹ-thuật--khắc-phục-sự-cố-troubleshooting)
8. [Phần 8: Bộ Câu Hỏi Vấn Đáp Bảo Vệ Đạt Điểm Tuyệt Đối (10/10)](#phần-8-bộ-câu-hỏi-vấn-đáp-bảo-vệ-đạt-điểm-tuyệt-đối-1010)

---

## PHẦN 1: BỐI CẢNH, ĐỀ BÀI & PHÂN TÍCH KỸ THUẬT CHI TIẾT

### 1.1. Yêu cầu đầu bài
Hệ thống mạng Trường Cao Đẳng Banana cần đáp ứng:
- **Đường truyền Internet**: Trường đã thuê bao đường truyền kết nối với ISP. Toàn bộ thiết bị trong trường phải truy cập được Internet.
- **Mạng tổng cấp phát**: $10.0.0.0/u$ với $u = 19$ $\implies$ Mạng tổng: **$10.0.0.0/19$**.
- **3 Khu vực chức năng**:
  1. **Lớp học (Classrooms)**: Quy mô **969 sinh viên**, sử dụng **kết nối Wi-Fi miễn phí (Free Wi-Fi)**.
  2. **Phòng thí nghiệm (Labs)**: Quy mô **400 máy tính**, chỉ sử dụng **kết nối có dây (Wired only)**.
  3. **Văn phòng (Office)**: Quy mô **69 nhân viên**, vừa có **kết nối Wi-Fi**, vừa có **kết nối có dây**. Yêu cầu bảo mật cấp cao: **Xác thực tập trung qua RADIUS Server** kết hợp **Lọc địa chỉ vật lý MAC (MAC Filtering / Port Security)**.
- **Kỹ thuật phân chia**: Áp dụng phân hoạch mạng con có độ dài mặt nạ thay đổi (**VLSM - Variable Length Subnet Masking**) từ mạng tổng $10.0.0.0/19$ để tối ưu hóa không gian địa chỉ, tránh lãng phí IP.

---

## PHẦN 2: TÍNH TOÁN PHÂN HOẠCH ĐỊA CHỈ MẠNG VLSM (TỪNG BƯỚC)

### 2.1. Phân tích mạng tổng $10.0.0.0/19$
- **Subnet Mask gốc**: $/19$  
  Dạng nhị phân: `11111111.11111111.11100000.00000000`  
  Dạng thập phân: **$255.255.224.0$**
- **Tổng số địa chỉ IP trong mạng tổng**:
  $$\text{Tổng IP} = 2^{32 - 19} = 2^{13} = 8192 \text{ địa chỉ}$$
- **Dải địa chỉ của mạng tổng**: `10.0.0.0` đến `10.0.31.255`.

---

### 2.2. Quy tắc vàng trong VLSM
> **Nguyên tắc bắt buộc**: Luôn sắp xếp các mạng con theo **nhu cầu số lượng host giảm dần (từ lớn nhất đến nhỏ nhất)**. Thứ tự cấp phát:  
> **Lớp học (969 hosts)** $\longrightarrow$ **Phòng thí nghiệm (400 hosts)** $\longrightarrow$ **Văn phòng (69 hosts)**.

---

### 2.3. Chi tiết tính toán từng mạng con

#### 🔹 BƯỚC 1: Tính toán cho Phân đoạn "LỚP HỌC" (Nhu cầu: 969 sinh viên)
- Nhu cầu thực tế: 969 thiết bị truy cập đồng thời.
- Công thức tính số bit phần Host ($h_1$):
  $$2^{h_1} - 2 \ge 969 \implies 2^{h_1} \ge 971$$
- Thử lũy thừa của 2:
  - Nếu $h_1 = 9 \implies 2^9 = 512 \implies 512 - 2 = 510 < 969$ (Không đủ).
  - Nếu $h_1 = 10 \implies 2^{10} = 1024 \implies 1024 - 2 = 1022 \ge 969$ (**Thỏa mãn!**).
- **Số bit mạng (Prefix length)**: $32 - 10 = \mathbf{/22}$.
- **Subnet Mask**: `11111111.11111111.11111100.00000000` $\implies \mathbf{255.255.252.0}$.
- **Bước nhảy (Block size)** tại Octet thứ 3: $256 - 252 = \mathbf{4}$.
- **Thông số mạng Lớp học (VLAN 10)**:
  - **Địa chỉ mạng (Network Address)**: `10.0.0.0/22`
  - **Địa chỉ Host đầu tiên (First Usable IP)**: `10.0.0.1` (dùng làm Default Gateway)
  - **Địa chỉ Host cuối cùng (Last Usable IP)**: `10.0.3.254`
  - **Địa chỉ Quảng bá (Broadcast Address)**: `10.0.3.255`
  - **Số lượng IP khả dụng**: 1022 địa chỉ (Dư 53 IP dự phòng cho Giảng viên/Thiết bị mới).
  - **Mạng tiếp theo bắt đầu từ**: $\mathbf{10.0.4.0}$.

---

#### 🔹 BƯỚC 2: Tính toán cho Phân đoạn "PHÒNG THÍ NGHIỆM" (Nhu cầu: 400 máy tính)
- Nhu cầu thực tế: 400 máy tính có dây.
- Mạng bắt đầu tiếp theo từ bước 1: `10.0.4.0`.
- Công thức tính số bit phần Host ($h_2$):
  $$2^{h_2} - 2 \ge 400 \implies 2^{h_2} \ge 402$$
- Thử lũy thừa của 2:
  - Nếu $h_2 = 8 \implies 2^8 = 256 \implies 256 - 2 = 254 < 400$ (Không đủ).
  - Nếu $h_2 = 9 \implies 2^9 = 512 \implies 512 - 2 = 510 \ge 400$ (**Thỏa mãn!**).
- **Số bit mạng (Prefix length)**: $32 - 9 = \mathbf{/23}$.
- **Subnet Mask**: `11111111.11111111.11111110.00000000` $\implies \mathbf{255.255.254.0}$.
- **Bước nhảy (Block size)** tại Octet thứ 3: $256 - 254 = \mathbf{2}$.
- **Thông số mạng Phòng thí nghiệm (VLAN 20)**:
  - **Địa chỉ mạng (Network Address)**: `10.0.4.0/23`
  - **Địa chỉ Host đầu tiên (First Usable IP)**: `10.0.4.1` (Default Gateway)
  - **Địa chỉ Host cuối cùng (Last Usable IP)**: `10.0.5.254`
  - **Địa chỉ Quảng bá (Broadcast Address)**: `10.0.5.255`
  - **Số lượng IP khả dụng**: 510 địa chỉ (Dư 110 IP dự phòng mở rộng máy in/Server thí nghiệm).
  - **Mạng tiếp theo bắt đầu từ**: $\mathbf{10.0.6.0}$.

---

#### 🔹 BƯỚC 3: Tính toán cho Phân đoạn "VĂN PHÒNG" (Nhu cầu: 69 nhân viên)
- Nhu cầu thực tế: 69 nhân viên (sử dụng cả máy bàn có dây và Wi-Fi).
- Mạng bắt đầu tiếp theo từ bước 2: `10.0.6.0`.
- Công thức tính số bit phần Host ($h_3$):
  $$2^{h_3} - 2 \ge 69 \implies 2^{h_3} \ge 71$$
- Thử lũy thừa của 2:
  - Nếu $h_3 = 6 \implies 2^6 = 64 \implies 64 - 2 = 62 < 69$ (Không đủ, thiếu 7 IP!).
  - Nếu $h_3 = 7 \implies 2^7 = 128 \implies 128 - 2 = 126 \ge 69$ (**Thỏa mãn!**).
- **Số bit mạng (Prefix length)**: $32 - 7 = \mathbf{/25}$.
- **Subnet Mask**: `11111111.11111111.11111111.10000000` $\implies \mathbf{255.255.255.128}$.
- **Bước nhảy (Block size)** tại Octet thứ 4: $256 - 128 = \mathbf{128}$.
- **Thông số mạng Văn phòng (VLAN 30)**:
  - **Địa chỉ mạng (Network Address)**: `10.0.6.0/25`
  - **Địa chỉ Host đầu tiên (First Usable IP)**: `10.0.6.1` (Default Gateway)
  - **Địa chỉ RADIUS Server (IP Tĩnh)**: `10.0.6.2`
  - **Địa chỉ Host cuối cùng (Last Usable IP)**: `10.0.6.126`
  - **Địa chỉ Quảng bá (Broadcast Address)**: `10.0.6.127`
  - **Số lượng IP khả dụng**: 126 địa chỉ (Thỏa mãn 69 nhân viên + Server RADIUS + AP Văn phòng).

---

### 2.4. Bảng Tổng Hợp VLSM Mạng Trường Banana

| STT | Khu Vực (Phân đoạn) | Số Host Yêu Cầu | Số Host Cung Cấp | Network Address | Subnet Mask | Dải IP Khả Dụng (Usable Range) | Default Gateway | Broadcast Address |
| :---: | :--- | :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Lớp Học (VLAN 10)** | 969 | 1022 | `10.0.0.0/22` | `255.255.252.0` | `10.0.0.1` – `10.0.3.254` | `10.0.0.1` | `10.0.3.255` |
| **2** | **Phòng Thí Nghiệm (VLAN 20)**| 400 | 510 | `10.0.4.0/23` | `255.255.254.0` | `10.0.4.1` – `10.0.5.254` | `10.0.4.1` | `10.0.5.255` |
| **3** | **Văn Phòng (VLAN 30)** | 69 | 126 | `10.0.6.0/25` | `255.255.255.128` | `10.0.6.1` – `10.0.6.126` | `10.0.6.1` | `10.0.6.127` |
| **-** | *Dải IP dự phòng mở rộng* | — | 6528 | `10.0.6.128/25` đến `10.0.31.255` | Phục vụ quy hoạch tòa nhà mới trong tương lai |

---

## PHẦN 3: BẢNG PHÂN BỔ ĐỊA CHỈ IP & SƠ ĐỒ TOPO MẠNG CHUẨN

### 3.1. Sơ đồ kiến trúc kết nối Topo mạng (Topology)

```
                                  [ INTERNET / ISP CLOUD ]
                                             |
                                             | (Fa0/0) 203.0.113.1/30
                                     +---------------+
                                     |   ROUTER ISP  |
                                     +---------------+
                                             | (Fa0/1) 203.0.113.2/30 (WAN)
                                             v
                                  +---------------------+
                                  |   BANANA_ROUTER     |
                                  | (Gateway & PAT Nat) |
                                  +---------------------+
                                             |
                                             | Trunk 802.1Q (Fa0/1)
                                             v
                                  +---------------------+
                                  |    CORE_SWITCH      |
                                  |  (2960 / 2950-24)   |
                                  +---------------------+
                                  /          |          \
                 (VLAN 10 Trunk/Acc)Fa0/2    |Fa0/3 (VLAN 20) \Fa0/4 (VLAN 30)
                                /            |                  \
                               v             v                   v
                     +---------------+  +--------------+  +---------------+
                     | AP_CLASSROOM  |  | PC_LAB_01    |  | SW_OFFICE     |
                     | (Free Wi-Fi)  |  | (Wired Only) |  | (VLAN 30)     |
                     +---------------+  +--------------+  +---------------+
                            |                                  /        \
                   (Sóng không dây)                           v          v
                            v                           +-----------+ +------------+
                     [ Laptop Sinh Viên ]               | RADIUS-SRV| | AP_OFFICE  |
                     (10.0.0.x /22 DHCP)                | (10.0.6.2)| | (WPA2-Ent) |
                                                        +-----------+ +------------+
                                                                            |
                                                                    (EAP-RADIUS + MAC Filter)
                                                                            v
                                                                     [ Laptop NV ]
```

---

### 3.2. Bảng Phân Bổ Địa Chỉ Cụ Thể Từng Thiết Bị

| Thiết bị (Device) | Interface | Địa chỉ IP / Prefix | Default Gateway | VLAN ID | Chức năng / Dịch vụ đảm nhiệm |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BANANA_ROUTER** | `Fa0/0` (WAN) | `203.0.113.2 /30` | `203.0.113.1` | N/A | Cổng WAN ra Internet (`ip nat outside`) |
| | `Fa0/1` (LAN) | Unassigned | N/A | N/A | Cổng vật lý Trunking nối Core Switch |
| | `Fa0/1.10` | `10.0.0.1 /22` | N/A | VLAN 10 | Gateway Lớp học (`ip nat inside`, DHCP Pool) |
| | `Fa0/1.20` | `10.0.4.1 /23` | N/A | VLAN 20 | Gateway Phòng lab (`ip nat inside`, DHCP Pool) |
| | `Fa0/1.30` | `10.0.6.1 /25` | N/A | VLAN 30 | Gateway Văn phòng (`ip nat inside`, DHCP Pool) |
| **CORE_SWITCH** | `Vlan 1` (Mgmt) | `10.0.6.254 /25` | `10.0.6.1` | VLAN 1 | Quản trị Switch |
| | `Fa0/1` | Trunking 802.1Q | N/A | 10,20,30 | Kết nối Router biên Banana |
| | `Fa0/2` | Access VLAN 10 | N/A | VLAN 10 | Nối Access Point Lớp học (`AP_CLASSROOM`) |
| | `Fa0/3` | Access VLAN 20 | N/A | VLAN 20 | Nối cụm máy tính Phòng thí nghiệm |
| | `Fa0/4` | Access VLAN 30 | N/A | VLAN 30 | Nối Switch Văn phòng / Thiết bị Văn phòng |
| **AP_CLASSROOM** | `Port 0` (Wired) | N/A (L2 AP) | N/A | VLAN 10 | Cầu nối không dây Lớp học |
| | `Port 1` (SSID) | `Banana_Free_WiFi`| N/A | VLAN 10 | Mở tự do, không mật khẩu |
| **RADIUS_SERVER** | `Fa0` | `10.0.6.2 /25` | `10.0.6.1` | VLAN 30 | Dịch vụ AAA (Port 1812 Authentication) |
| **AP_OFFICE** | `Port 0` (Wired) | N/A (hoặc DHCP) | `10.0.6.1` | VLAN 30 | Access Point Văn phòng bảo mật |
| | `Port 1` (SSID) | `Banana_Office` | N/A | VLAN 30 | WPA2-Enterprise + MAC Filter |
| **ROUTER_ISP** | `Fa0/0` | `203.0.113.1 /30` | N/A | N/A | Gateway nhà mạng ISP |
| | `Fa0/1` | `8.8.8.1 /24` | N/A | N/A | Mạng dịch vụ Internet (Google DNS) |
| **GOOGLE_DNS** | `Fa0` | `8.8.8.8 /24` | `8.8.8.1` | N/A | Máy chủ DNS công cộng kiểm thử |

---

## PHẦN 4: BẢN CHẤT CỐT LÕI KỸ THUẬT (TẠI SAO PHẢI THIẾT KẾ NHƯ VẬY?)

```
+---------------------------------------------------------------------------------------------------------+
|                                         CỐT LÕI KỸ THUẬT LAB 4                                          |
|                                                                                                         |
| 1. Kỹ thuật VLSM:                                                                                       |
|    - Nếu dùng FLSM (Fixed Length Subnet Mask), toàn bộ các mạng phải dùng chung /22 (1024 IP),          |
|      khi đó mạng Văn phòng (chỉ cần 69 host) sẽ lãng phí hơn 900 địa chỉ IP vô ích!                    |
|    - VLSM cho phép cắt các mạng con có kích thước chuẩn xác theo nhu cầu (/22 -> /23 -> /25).          |
|                                                                                                         |
| 2. NAT Overload (PAT - Port Address Translation):                                                       |
|    - Tổng quy mô: 969 + 400 + 69 = 1438 host trong mạng nội bộ. Nhà mạng ISP chỉ cấp 1 địa chỉ IP WAN  |
|      (203.0.113.2). PAT sử dụng số hiệu cổng TCP/UDP (16-bit Port: từ 1024 đến 65535) để cho phép     |
|      hàng nghìn thiết bị cùng ra Internet đồng thời qua 1 IP duy nhất!                                  |
|                                                                                                         |
| 3. Xác thực RADIUS (WPA2-Enterprise / 802.1X):                                                          |
|    - Mạng văn phòng lưu trữ dữ liệu điểm số, tài chính nên KHÔNG ĐƯỢC dùng mật khẩu chia sẻ WPA2-PSK     |
|      (vì nhân viên nghỉ việc sẽ làm lộ pass).                                                           |
|    - 802.1X RADIUS yêu cầu mỗi nhân viên phải có Username/Password riêng lưu trên AAA Server tập trung.|
|                                                                                                         |
| 4. Cơ chế kép: MAC Filtering & Port Security:                                                           |
|    - Lớp phòng thủ 1 (Wi-Fi): AP kiểm tra danh sách White-list MAC, từ chối kết nối trước cả khi hỏi   |
|      User/Pass.                                                                                         |
|    - Lớp phòng thủ 2 (Có dây): Switch Port Security khóa cứng địa chỉ MAC trên switchport. Kẻ gian cắm |
|      trộm máy lạ vào dây mạng văn phòng sẽ bị ngắt cổng ngay lập tức (err-disable)!                    |
+---------------------------------------------------------------------------------------------------------+
```

---

## PHẦN 5: HƯỚNG DẪN THAO TÁC CẤU HÌNH CHI TIẾT TỪNG BƯỚC (LÀM THẾ NÀO?)

### Bước 1: Cấu hình Switch Trung tâm (Phân chia VLAN 10, 20, 30 & Trunking)

Mở CLI của **CORE_SWITCH (2960 hoặc 2950-24)**:

```cisco
Switch> enable
Switch# configure terminal
Switch(config)# hostname CORE_SWITCH

! --- 1. Tạo các VLAN theo quy hoạch VLSM ---
CORE_SWITCH(config)# vlan 10
CORE_SWITCH(config-vlan)# name VLAN10_LOPHOC
CORE_SWITCH(config-vlan)# exit

CORE_SWITCH(config)# vlan 20
CORE_SWITCH(config-vlan)# name VLAN20_PHONGTHI_NGHIEM
CORE_SWITCH(config-vlan)# exit

CORE_SWITCH(config)# vlan 30
CORE_SWITCH(config-vlan)# name VLAN30_VANPHONG
CORE_SWITCH(config-vlan)# exit

! --- 2. Cổng Fa0/1 làm đường Trunk 802.1Q kết nối Router ---
CORE_SWITCH(config)# interface FastEthernet 0/1
CORE_SWITCH(config-if)# switchport mode trunk
CORE_SWITCH(config-if)# no shutdown
CORE_SWITCH(config-if)# exit

! --- 3. Cổng Fa0/2 nối AP Lớp học (VLAN 10) ---
CORE_SWITCH(config)# interface FastEthernet 0/2
CORE_SWITCH(config-if)# switchport mode access
CORE_SWITCH(config-if)# switchport access vlan 10
CORE_SWITCH(config-if)# no shutdown
CORE_SWITCH(config-if)# exit

! --- 4. Cổng Fa0/3 nối cụm máy tính Phòng Lab (VLAN 20) ---
CORE_SWITCH(config)# interface FastEthernet 0/3
CORE_SWITCH(config-if)# switchport mode access
CORE_SWITCH(config-if)# switchport access vlan 20
CORE_SWITCH(config-if)# no shutdown
CORE_SWITCH(config-if)# exit

! --- 5. Cổng Fa0/4 nối cụm thiết bị Văn phòng (VLAN 30) ---
CORE_SWITCH(config)# interface FastEthernet 0/4
CORE_SWITCH(config-if)# switchport mode access
CORE_SWITCH(config-if)# switchport access vlan 30
CORE_SWITCH(config-if)# no shutdown
CORE_SWITCH(config-if)# exit

CORE_SWITCH(config)# end
CORE_SWITCH# write memory
```

---

### Bước 2: Cấu hình Router Biên Trường Banana (Inter-VLAN + DHCP Multi-Pool + PAT + Default Route)

Mở CLI của **BANANA_ROUTER (2811)**:

```cisco
Router> enable
Router# configure terminal
Router(config)# hostname BANANA_ROUTER

! =================================================================
! PHẦN A: BẬT CỔNG VẬT LÝ VÀ CẤU HÌNH SUBINTERFACE (ROUTER-ON-STICK)
! =================================================================
BANANA_ROUTER(config)# interface FastEthernet 0/1
BANANA_ROUTER(config-if)# no ip address
BANANA_ROUTER(config-if)# no shutdown
BANANA_ROUTER(config-if)# exit

! Subinterface cho VLAN 10 (Lớp học: 10.0.0.0/22)
BANANA_ROUTER(config)# interface FastEthernet 0/1.10
BANANA_ROUTER(config-subif)# encapsulation dot1Q 10
BANANA_ROUTER(config-subif)# ip address 10.0.0.1 255.255.252.0
BANANA_ROUTER(config-subif)# ip nat inside
BANANA_ROUTER(config-subif)# exit

! Subinterface cho VLAN 20 (Phòng Lab: 10.0.4.0/23)
BANANA_ROUTER(config)# interface FastEthernet 0/1.20
BANANA_ROUTER(config-subif)# encapsulation dot1Q 20
BANANA_ROUTER(config-subif)# ip address 10.0.4.1 255.255.254.0
BANANA_ROUTER(config-subif)# ip nat inside
BANANA_ROUTER(config-subif)# exit

! Subinterface cho VLAN 30 (Văn phòng: 10.0.6.0/25)
BANANA_ROUTER(config)# interface FastEthernet 0/1.30
BANANA_ROUTER(config-subif)# encapsulation dot1Q 30
BANANA_ROUTER(config-subif)# ip address 10.0.6.1 255.255.255.128
BANANA_ROUTER(config-subif)# ip nat inside
BANANA_ROUTER(config-subif)# exit

! =================================================================
! PHẦN B: CẤU HÌNH CỔNG WAN & ĐỊNH TUYẾN NGẦM ĐỊNH (DEFAULT ROUTE)
! =================================================================
BANANA_ROUTER(config)# interface FastEthernet 0/0
BANANA_ROUTER(config-if)# ip address 203.0.113.2 255.255.255.252
BANANA_ROUTER(config-if)# ip nat outside
BANANA_ROUTER(config-if)# no shutdown
BANANA_ROUTER(config-if)# exit

! Định tuyến ngầm định ra Internet (Next-hop của ISP)
BANANA_ROUTER(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.1

! =================================================================
! PHẦN C: CẤU HÌNH DHCP SERVER CHO CẢ 3 PHÂN ĐOẠN MẠNG CON
! =================================================================
! Loại trừ các IP Gateway và Server tĩnh
BANANA_ROUTER(config)# ip dhcp excluded-address 10.0.0.1 10.0.0.9
BANANA_ROUTER(config)# ip dhcp excluded-address 10.0.4.1 10.0.4.9
BANANA_ROUTER(config)# ip dhcp excluded-address 10.0.6.1 10.0.6.9

! 1. DHCP Pool cho Lớp Học (VLAN 10)
BANANA_ROUTER(config)# ip dhcp pool POOL_LOPHOC
BANANA_ROUTER(dhcp-config)# network 10.0.0.0 255.255.252.0
BANANA_ROUTER(dhcp-config)# default-router 10.0.0.1
BANANA_ROUTER(dhcp-config)# dns-server 8.8.8.8
BANANA_ROUTER(dhcp-config)# exit

! 2. DHCP Pool cho Phòng Lab (VLAN 20)
BANANA_ROUTER(config)# ip dhcp pool POOL_PHONGLAB
BANANA_ROUTER(dhcp-config)# network 10.0.4.0 255.255.254.0
BANANA_ROUTER(dhcp-config)# default-router 10.0.4.1
BANANA_ROUTER(dhcp-config)# dns-server 8.8.8.8
BANANA_ROUTER(dhcp-config)# exit

! 3. DHCP Pool cho Văn Phòng (VLAN 30)
BANANA_ROUTER(config)# ip dhcp pool POOL_VANPHONG
BANANA_ROUTER(dhcp-config)# network 10.0.6.0 255.255.255.128
BANANA_ROUTER(dhcp-config)# default-router 10.0.6.1
BANANA_ROUTER(dhcp-config)# dns-server 8.8.8.8
BANANA_ROUTER(dhcp-config)# exit

! =================================================================
! PHẦN D: CẤU HÌNH DỊCH VỤ NAT OVERLOAD (PAT) RA INTERNET
! =================================================================
! Access-list cho phép toàn bộ mạng tổng 10.0.0.0/19 (Wildcard: 0.0.31.255)
BANANA_ROUTER(config)# access-list 1 permit 10.0.0.0 0.0.31.255
BANANA_ROUTER(config)# ip nat inside source list 1 interface FastEthernet 0/0 overload

BANANA_ROUTER(config)# end
BANANA_ROUTER# write memory
```

---

### Bước 3: Cấu hình Mạng Không Dây Lớp Học (Free Wi-Fi)

Khu vực Lớp học sử dụng **Access Point (AP-PT)** nối vào cổng `Fa0/2` của Core Switch:
1. Nhấp chọn thiết bị **AP-PT** $\rightarrow$ chọn tab **Config**.
2. Chọn cổng **Port 1** (Cổng phát sóng Wireless):
   - **SSID**: Đặt tên là `Banana_Free_WiFi`.
   - **Authentication**: Chọn **Disabled** (Mạng không dây mở, hoàn toàn miễn phí, không mật khẩu).
3. **Thử nghiệm trên Laptop Sinh viên**:
   - Tắt nguồn máy tính, tháo card mạng có dây và kéo card không dây **WPC300N** vào máy $\rightarrow$ Bật nguồn lại.
   - Mở **Desktop** $\rightarrow$ **PC Wireless** $\rightarrow$ chọn tab **Connect** $\rightarrow$ bấm **Refresh**.
   - Thấy mạng `Banana_Free_WiFi` $\rightarrow$ bấm **Connect**.
   - Mở **IP Configuration** $\rightarrow$ Thấy laptop tự động nhận IP động dạng `10.0.0.x /22`, Gateway `10.0.0.1`, DNS `8.8.8.8`!

---

### Bước 4: Cấu hình Mạng Phòng Thí Nghiệm (Wired Only)

Khu vực này yêu cầu **chỉ sử dụng kết nối có dây**:
1. Dùng cáp thẳng nối cổng mạng `Fa0` của các máy tính trong phòng Lab vào cổng `Fa0/3` của Switch (hoặc thông qua một Switch nhánh của phòng Lab nối về `Fa0/3`).
2. Mở máy tính **PC_LAB** $\rightarrow$ **Desktop** $\rightarrow$ **IP Configuration** $\rightarrow$ chọn **DHCP**.
3. **Xác thực**: Máy tính tự động nhận địa chỉ IP trong dải `10.0.4.x /23`, Default Gateway là `10.0.4.1`.

---

### Bước 5: Cấu hình Bảo Mật Văn Phòng (RADIUS Server 802.1X + Wi-Fi MAC Filter + Port Security)

Mạng Văn phòng có yêu cầu bảo mật cao nhất, bao gồm cả mạng có dây và không dây:

#### 1. Cấu hình Máy Chủ Xác Thực RADIUS Server (AAA Server)
- Đặt một máy chủ **Server-PT** đặt tên là `RADIUS_SERVER`, nối vào cổng thuộc VLAN 30.
- **Cấu hình IP Tĩnh**:
  - IP Address: `10.0.6.2`
  - Subnet Mask: `255.255.255.128`
  - Default Gateway: `10.0.6.1`
- **Kích hoạt Dịch vụ AAA (RADIUS)**:
  - Vào tab **Services** $\rightarrow$ chọn mục **AAA** bên trái.
  - Chọn nút radio **AAA Service**: **ON**.
  - **Mục Network Configuration (Đăng ký Client là AP Văn phòng)**:
    - Client Name: `AP_OFFICE`
    - Client IP: `10.0.6.3` (hoặc IP của Gateway `10.0.6.1`)
    - Secret: `cisco123` (Khóa bí mật chia sẻ giữa AP và Server)
    - Server Type: chọn **Radius** $\rightarrow$ bấm nút **Add**.
  - **Mục User Setup (Tạo tài khoản định danh nhân viên)**:
    - Username: `nhanvien01`
    - Password: `Banana@Password123`
    - Bấm nút **Add**.

#### 2. Cấu hình Access Point Văn phòng (WPA2-Enterprise + MAC Filter)
Sử dụng thiết bị không dây văn phòng (như **AccessPoint-PT** hoặc **WRT300N**):
- **Cấu hình WPA2-Enterprise (802.1X)**:
  - SSID: `Banana_Office_Secure`
  - Authentication: Chọn **WPA2-Enterprise** (hoặc WPA-Enterprise).
  - Encryption: **AES**.
  - RADIUS Server IP: Điền `10.0.6.2`.
  - Shared Secret: Điền `cisco123`.
- **Cấu hình Lọc địa chỉ vật lý MAC (MAC Filtering)**:
  - Chọn mục **Wireless MAC Filter**.
  - Chuyển trạng thái sang **Enable**.
  - Chọn chế độ: **Permit (Allow)** - Chỉ cho phép các địa chỉ MAC có trong danh sách được kết nối.
  - Xem MAC của Laptop nhân viên (bằng lệnh `ipconfig /all`, ví dụ: `0001.96A2.69BC`) $\rightarrow$ Nhập vào danh sách và bấm **Save**.

#### 3. Cấu hình Lọc MAC trên Cổng Switch Có Dây (Port Security)
Trên Switch nối máy tính bàn của nhân viên Văn phòng:
```cisco
CORE_SWITCH(config)# interface FastEthernet 0/4
CORE_SWITCH(config-if)# switchport mode access
CORE_SWITCH(config-if)# switchport access vlan 30

! Bật tính năng Port Security
CORE_SWITCH(config-if)# switchport port-security
! Giới hạn chỉ đúng 1 địa chỉ MAC duy nhất được cắm vào cổng này
CORE_SWITCH(config-if)# switchport port-security maximum 1
! Tự động học và gán cứng MAC của máy nhân viên vào cấu hình
CORE_SWITCH(config-if)# switchport port-security mac-address sticky
! Nếu cắm máy lạ vào sẽ tự động tắt cổng (Shutdown) để chống xâm nhập
CORE_SWITCH(config-if)# switchport port-security violation shutdown
CORE_SWITCH(config-if)# exit
```

#### 4. Thử nghiệm kết nối trên Laptop Nhân Viên Văn Phòng:
- Mở **Laptop_NhanVien** $\rightarrow$ **Desktop** $\rightarrow$ **PC Wireless** $\rightarrow$ chọn **Profiles** $\rightarrow$ **New**:
  - Profile Name: `Office_Profile` $\rightarrow$ bấm OK.
  - Chọn mạng `Banana_Office_Secure` $\rightarrow$ bấm **Advanced Setup**.
  - Security Mode: Chọn **WPA2-Enterprise**.
  - Nhập **Username**: `nhanvien01`, **Password**: `Banana@Password123` $\rightarrow$ bấm **Save**.
- **Kết quả**: Laptop gửi gói tin EAP tới AP $\rightarrow$ AP hỏi RADIUS Server `10.0.6.2` $\rightarrow$ RADIUS trả về thành công $\rightarrow$ Sóng không dây kết nối thành công!

---

### Bước 6: Cấu hình Phía Nhà Cung Cấp Dịch Vụ Internet (ISP & DNS Test)

Mở CLI của **ROUTER_ISP**:

```cisco
Router> enable
Router# configure terminal
Router(config)# hostname ISP

! Cổng WAN nối về Router Trường Banana
ISP(config)# interface FastEthernet 0/0
ISP(config-if)# ip address 203.0.113.1 255.255.255.252
ISP(config-if)# no shutdown
ISP(config-if)# exit

! Cổng nối máy chủ Google DNS công cộng
ISP(config)# interface FastEthernet 0/1
ISP(config-if)# ip address 8.8.8.1 255.255.255.0
ISP(config-if)# no shutdown
ISP(config-if)# exit

ISP(config)# end
ISP# write memory
```

---

## PHẦN 6: KỊCH BẢN KIỂM THỬ & NGHIỆM THU CHO GIẢNG VIÊN CHẤM ĐIỂM

Khi Thầy chấm bài Lab 4, bạn tiến hành thực hiện tuần tự 4 bước nghiệm thu sau:

### 🎯 CHECKPOINT 1: Nghiệm thu tính toán VLSM & Trạng thái Gateway
Thầy sẽ mở CLI của Banana Router và kiểm tra bảng định tuyến:
```cisco
BANANA_ROUTER# show ip route
```
*Output chuẩn*:
```text
Gateway of last resort is 203.0.113.1 to network 0.0.0.0

S*   0.0.0.0/0 [1/0] via 203.0.113.1
     10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
C       10.0.0.0/22 is directly connected, FastEthernet0/1.10
C       10.0.4.0/23 is directly connected, FastEthernet0/1.20
C       10.0.6.0/25 is directly connected, FastEthernet0/1.30
     203.0.113.0/30 is subnetted, 1 subnets
C       203.0.113.0 is directly connected, FastEthernet0/0
```
> **Điểm Thầy chấm**: Cả 3 mạng con với 3 mặt nạ khác biệt (`/22`, `/23`, `/25`) cùng dòng Default Route `S* 0.0.0.0/0` hiển thị chính xác 100%!

---

### 🎯 CHECKPOINT 2: Nghiệm thu Cấp phát DHCP đa vùng (DHCP Binding)
Trên Banana Router, gõ lệnh:
```cisco
BANANA_ROUTER# show ip dhcp binding
```
*Output chuẩn*:
```text
IP address       Client-ID/Hardware address          Lease expiration        Type
10.0.0.10        0001.96a2.69bc                     --                      Automatic
10.0.4.10        0002.164a.22aa                     --                      Automatic
10.0.6.10        0003.55cc.33dd                     --                      Automatic
```
> **Giải trình với Thầy**: Router đã tự động nhận diện thiết bị ở từng VLAN thông qua Router-on-a-Stick và cấp đúng dải IP tương ứng với từng mạng con.

---

### 🎯 CHECKPOINT 3: Nghiệm thu Bảo Mật Văn Phòng (RADIUS + MAC Filter)
1. **Kiểm tra xác thực RADIUS**:
   - Mở Laptop Nhân viên $\rightarrow$ Kết nối Wi-Fi bằng `nhanvien01` / `Banana@Password123` $\rightarrow$ Báo **Connected**.
   - Đổi thử sai mật khẩu thành `123456` $\rightarrow$ Kết nối bị từ chối ngay lập tức.
2. **Kiểm tra MAC Filter**:
   - Thử dùng một Laptop lạ (chưa đăng ký MAC trong White-list của AP) kết nối vào mạng `Banana_Office_Secure` dù nhập đúng tài khoản nhân viên $\rightarrow$ Vẫn bị từ chối không cho gia nhập mạng!
3. **Kiểm tra Port Security trên Switch**:
   - Trên Switch gõ: `show port-security interface Fa0/4`. Thấy `Port Security: Enabled`, `Port Status: Secure-up`, địa chỉ MAC đã được học cố định (`sticky`).

---

### 🎯 CHECKPOINT 4: Nghiệm thu Dịch Vụ Internet & NAT Overload (PAT)
1. Đứng từ bất kỳ máy nào (Laptop Sinh viên, Máy tính Lab, hoặc Laptop Nhân viên), mở **Command Prompt** gõ:
   ```text
   C:\> ping 8.8.8.8
   Reply from 8.8.8.8: bytes=32 time=12ms TTL=126
   ```
2. Trên **BANANA_ROUTER**, gõ lệnh kiểm tra NAT:
   ```cisco
   BANANA_ROUTER# show ip nat translations
   ```
   *Output chuẩn*:
   ```text
   Pro Inside global         Inside local          Outside local      Outside global
   icmp 203.0.113.2:1        10.0.0.10:1           8.8.8.8:1          8.8.8.8:1
   icmp 203.0.113.2:2        10.0.4.10:2           8.8.8.8:2          8.8.8.8:2
   icmp 203.0.113.2:3        10.0.6.10:3           8.8.8.8:3          8.8.8.8:3
   ```
> **Giải thích cho Thầy**: Toàn bộ các máy từ 3 khu vực khác nhau khi đi ra Internet đều được ánh xạ qua duy nhất một địa chỉ IP Public `203.0.113.2` và phân biệt bằng các Session ID / Cổng khác nhau.

---

## PHẦN 7: CẢNH BÁO BẪY KỸ THUẬT & KHẮC PHỤC SỰ CỐ (TROUBLESHOOTING)

### ⚠️ Bẫy 1: Sai lệch Subnet Mask khi tính VLSM
- **Nguy cơ**: Sinh viên quen tay tính Subnet Mask của mạng Lớp học là `255.255.255.0` (/24).
- **Hậu quả**: Dải /24 chỉ cấp được tối đa 254 máy, trong khi đề bài yêu cầu 969 sinh viên $\rightarrow$ Rớt bài ngay từ bước đầu!
- **Khắc phục**: 969 sinh viên bắt buộc phải dùng **/22** (`255.255.252.0`).

---

### ⚠️ Bẫy 2: Quên cấu hình Default Route trên Banana Router
- **Hiện tượng**: Trong nội bộ trường ping thấy thông nhau hoàn toàn, nhưng không máy nào ping được ra IP `8.8.8.8` của Internet.
- **Khắc phục**: Gõ `ip route 0.0.0.0 0.0.0.0 203.0.113.1` trên Banana Router.

---

### ⚠️ Bẫy 3: Khóa Secret giữa RADIUS Server và AP không khớp nhau
- **Hiện tượng**: Laptop nhân viên nhập đúng tài khoản nhưng luôn bị treo ở trạng thái *"Authenticating..."* rồi ngắt kết nối.
- **Khắc phục**: Kiểm tra lại chuỗi bí mật (Secret Key) trên mục AAA của Server và mục WPA2-Enterprise của AP đảm bảo khớp từng ký tự (ví dụ: `cisco123`).

---

## PHẦN 8: BỘ CÂU HỎI VẤN ĐÁP BẢO VỆ ĐẠT ĐIỂM TUYỆT ĐỐI (10/10)

### ❓ Câu hỏi 1: *"Tại sao trong bài toán này ta phải sắp xếp chia VLSM theo thứ tự Lớp học -> Phòng Lab -> Văn phòng mà không chia theo thứ tự ngược lại?"*
- **Trả lời**: Kỹ thuật VLSM hoạt động theo nguyên tắc chia khối nhị phân liên tục. Việc cấp phát cho mạng có nhu cầu lớn nhất trước (khối block lớn) đảm bảo các ranh giới mạng (Network Boundary) luôn khớp với bội số của bước nhảy, tránh gây phân mảnh (fragmentation) không gian địa chỉ IP và không làm chồng lấn địa chỉ mạng lên nhau.

---

### ❓ Câu hỏi 2: *"Sự khác biệt bản chất giữa Static NAT trong Lab 3 và Dynamic NAT Overload (PAT) trong Lab 4 là gì?"*
- **Trả lời**:
  - **Static NAT (Lab 3)**: Ánh xạ cố định theo tỉ lệ 1:1 giữa một địa chỉ IP Private và một địa chỉ IP Public. Phù hợp để xuất bản các dịch vụ máy chủ cố định (Web, Mail) từ ngoài vào.
  - **PAT / NAT Overload (Lab 4)**: Ánh xạ theo tỉ lệ N:1 (nhiều IP Private ra 1 IP Public) bằng cách theo dõi số hiệu cổng tầng Giao vận (TCP/UDP Port). Đây là giải pháp sống còn giúp hàng nghìn sinh viên và nhân viên trường Banana cùng lướt Internet đồng thời chỉ với 1 địa chỉ IP WAN thuê bao.

---

### ❓ Câu hỏi 3: *"Tại sao mạng Văn phòng đã có bảo mật WPA2-Enterprise RADIUS rồi mà vẫn phải cấu hình thêm MAC Filtering?"*
- **Trả lời**: Đây là mô hình bảo mật đa tầng chuyên sâu (**Defense-in-Depth**):
  - Xác thực RADIUS bảo vệ ở **Tầng logic / Định danh (Who you are)**: Chứng minh bạn là nhân viên hợp lệ có tài khoản.
  - Lọc MAC bảo vệ ở **Tầng vật lý / Thiết bị (What device you use)**: Ngăn chặn triệt để trường hợp nhân viên đem laptop cá nhân hoặc thiết bị không rõ nguồn gốc (BYOD - tiềm ẩn mã độc) vào cắm vào mạng nội bộ cơ quan. Thiết bị muốn truy cập vừa phải có tài khoản nhân viên, vừa phải là máy tính do cơ quan cấp phát chính thức!
