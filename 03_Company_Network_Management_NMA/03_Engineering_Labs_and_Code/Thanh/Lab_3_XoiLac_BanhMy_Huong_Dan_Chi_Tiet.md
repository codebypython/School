# 🍌 GIÁO TRÌNH THỰC HÀNH & HƯỚNG DẪN CHI TIẾT LAB 3: VLAN, DEFAULT ROUTE, STATIC NAT & GOOGLE DNS

> **Mã học phần**: NMA-DUT (Quản trị Mạng & Hệ thống) — Đại học Bách khoa – ĐH Đà Nẵng  
> **Tên bài thực hành**: Lab 03 — Triển khai Mạng Doanh nghiệp Banana: Phân đoạn VLAN, Inter-VLAN Routing, Default Route, Static NAT và Phân giải Google DNS  
> **Tệp mô phỏng Packet Tracer**: `Lab 3 - XoiLac BanhMy.pkt` (thư mục `lab/Thanh`)  
> **Trạng thái**: *Đã chuẩn hóa 100% theo bộ thông số IP và kịch bản kiểm thử của Giảng viên.*

---

## 📑 MỤC LỤC

1. [Phần 1: Phân Tích Chỉ Dẫn Của Thầy & Bảng Thông Số IP Chuẩn Hóa](#phần-1-phân-tích-chỉ-dẫn-của-thầy--bảng-thông-số-ip-chuẩn-hóa)
2. [Phần 2: Sơ Đồ Topo Kết Nối Thiết Bị & Cổng Vật Lý](#phần-2-sơ-đồ-topo-kết-nối-thiết-bị--cổng-vật-lý)
3. [Phần 3: Hướng Dẫn Thao Tác Cấu Hình Chi Tiết Từng Bước](#phần-3-hướng-dẫn-thao-tác-cấu-hình-chi-tiết-từng-bước)
   - [Mục 3.1: Cấu hình VLAN & Trunking trên BANANA SWITCH](#mục-31-cấu-hình-vlan--trunking-trên-banana-switch)
   - [Mục 3.2: Cấu hình Inter-VLAN Routing trên BANANA ROUTER (Chuẩn chỉ dẫn của Thầy)](#mục-32-cấu-hình-inter-vlan-routing-trên-banana-router-chuẩn-chỉ-dẫn-của-thầy)
   - [Mục 3.3: Hướng dẫn cấu hình Định tuyến ngầm định (Default Route) trên Router](#mục-33-hướng-dẫn-cấu-hình-định-tuyến-ngầm-định-default-route-trên-router)
   - [Mục 3.4: Hướng dẫn cấu hình Dịch vụ Static NAT trên Router](#mục-34-hướng-dẫn-cấu-hình-dịch-vụ-static-nat-trên-router)
   - [Mục 3.5: Cấu hình hạ tầng kết nối WAN (Cloud-PT DSL & ISP Router)](#mục-35-cấu-hình-hạ-tầng-kết-nối-wan-cloud-pt-dsl--isp-router)
   - [Mục 3.6: Hướng dẫn lưu trữ tên miền xoilac.xxx và banhmy.xxx trên Google DNS Server](#mục-36-hướng-dẫn-lưu-trữ-tên-miền-xoilacxxx-và-banhmyxxx-trên-google-dns-server)
   - [Mục 3.7: Cấu hình 2 Web Server nội bộ (XOILAC & BANHMY)](#mục-37-cấu-hình-2-web-server-nội-bộ-xoilac--banhmy)
4. [Phần 4: Bản Chất & Hướng Dẫn Thực Hiện Các Bước Kiểm Tra Của Thầy](#phần-4-bản-chất--hướng-dẫn-thực-hiện-các-bước-kiểm-tra-của-thầy)
   - [Kiểm tra 1: Kiểm tra VLAN tĩnh (`show vlan`) & Ping liên VLAN](#kiểm-tra-1-kiểm-tra-vlan-tĩnh-show-vlan--ping-liên-vlan)
   - [Kiểm tra 2: Kiểm tra Phân giải DNS (`nslookup`) ngoài Internet](#kiểm-tra-2-kiểm-tra-phân-giải-dns-nslookup-ngoài-internet)
   - [Kiểm tra 3: Kiểm tra Truy cập Web qua Tên miền trên Trình duyệt Web](#kiểm-tra-3-kiểm-tra-truy-cập-web-qua-tên-miền-trên-trình-duyệt-web)
   - [Kiểm tra 4: Kiểm tra Bảng NAT Table (`show ip nat translation`) với giao thức HTTP (TCP Port 80)](#kiểm-tra-4-kiểm-tra-bảng-nat-table-show-ip-nat-translation-với-giao-thức-http-tcp-port-80)
5. [Phần 5: Bảng Ma Trận Xử Lý Sự Cố Khi Thầy Chấm (Troubleshooting Matrix)](#phần-5-bảng-ma-trận-xử-lý-sự-cố-khi-thầy-chấm-troubleshooting-matrix)
6. [Phần 6: Bí Kíp Vấn Đáp Bảo Vệ Điểm Tối Đa (10/10)](#phần-6-bí-kíp-vấn-đáp-bảo-vệ-điểm-tối-đa-1010)

---

## PHẦN 1: PHÂN TÍCH CHỈ DẪN CỦA THẦY & BẢNG THÔNG SỐ IP CHUẨN HÓA

### 1.1. Phân tích chỉ dẫn của Thầy
Trong đoạn hướng dẫn của Thầy:
```cisco
Router(config)# interface f0/1
Router(config-if)# no shutdown
Router(config-if)# interface f0/1.69
Router(config-subif)# encapsulation dot1q 69
Router(config-subif)# ip address 10.6.9.1 255.255.255.0
Router(config-subif)# interface f0/1.96
Router(config-subif)# encapsulation dot1q 96
Router(config-subif)# ip address 10.9.6.1 255.255.255.0
```

Từ đây ta nhận diện được **quy luật phân bổ địa chỉ IP mạng nội bộ** cực kỳ tinh tế và đồng bộ của Thầy:
- **VLAN 69**: Thầy dùng dải mạng **`10.6.9.0/24`** ($x_1=10, y_1=6, z_1=9$ ứng với số hiệu **69**).
  - Gateway VLAN 69: `10.6.9.1` (gán trên Subinterface `f0/1.69`).
  - Server XOILAC: chọn IP $x_1.y_1.z_1.t_1$ là **`10.6.9.10`** (hoặc `10.6.9.2`).
  - Địa chỉ NAT Public tương ứng: **`6.9.6.69`** (tên miền `xoilac.xxx`).
- **VLAN 96**: Thầy dùng dải mạng **`10.9.6.0/24`** ($x_2=10, y_2=9, z_2=6$ ứng với số hiệu **96**).
  - Gateway VLAN 96: `10.9.6.1` (gán trên Subinterface `f0/1.96`).
  - Server BANHMY: chọn IP $x_2.y_2.z_2.t_2$ là **`10.9.6.10`** (hoặc `10.9.6.2`).
  - Địa chỉ NAT Public tương ứng: **`6.9.6.96`** (tên miền `banhmy.xxx`).
- **Quy ước đuôi tên miền `.xxx`**:
  - `xxx` là **3 chữ số cuối Mã số sinh viên (MSSV)** của bạn (Ví dụ: MSSV là `102210123` $\rightarrow$ tên miền là `xoilac.123` và `banhmy.123`).

---

### 1.2. Bảng Phân Bổ Địa Chỉ IP Chi Tiết (IP Addressing Table)

| Thiết bị | Giao diện (Interface) | Địa chỉ IP | Subnet Mask | Default Gateway | VLAN ID | Chức năng / Vai trò |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Server XOILAC** | `FastEthernet0` | `10.6.9.10` | `255.255.255.0` | `10.6.9.1` | VLAN 69 | Web Server 1 nội bộ (`xoilac.xxx`) |
| **Server BANHMY** | `FastEthernet0` | `10.9.6.10` | `255.255.255.0` | `10.9.6.1` | VLAN 96 | Web Server 2 nội bộ (`banhmy.xxx`) |
| **BANANA SWITCH** | `Vlan 1` | `10.6.9.254` | `255.255.255.0` | `10.6.9.1` | VLAN 1 | Quản trị thiết bị L2 |
| | `FastEthernet0/2` | Unassigned | N/A | N/A | VLAN 69 | Access port nối Server XOILAC |
| | `FastEthernet0/10`| Unassigned | N/A | N/A | VLAN 96 | Access port nối Server BANHMY |
| | `FastEthernet0/1` | Unassigned | N/A | N/A | 1, 69, 96 | Đường 802.1Q Trunking nối Router |
| **BANANA ROUTER** | `FastEthernet0/1` | Unnumbered | N/A | N/A | N/A | Cổng vật lý Trunking (`no shutdown`) |
| | `FastEthernet0/1.69`| `10.6.9.1` | `255.255.255.0` | N/A | VLAN 69 | Gateway VLAN 69 (`ip nat inside`) |
| | `FastEthernet0/1.96`| `10.9.6.1` | `255.255.255.0` | N/A | VLAN 96 | Gateway VLAN 96 (`ip nat inside`) |
| | `FastEthernet0/0` | `6.9.6.2` | `255.255.255.0` | N/A | N/A | Cổng WAN nối DSL (`ip nat outside`) |
| **ISP ROUTER** | `FastEthernet0/0` | `6.9.6.1` | `255.255.255.0` | N/A | N/A | Cổng WAN nối về Banana Router qua DSL |
| | `Vlan 1` (HWIC) | `8.8.8.1` | `255.255.255.0` | N/A | VLAN 1 | Gateway mạng dịch vụ Internet |
| | `Fa0/0/0 - 2` | Unassigned | N/A | N/A | VLAN 1 | Switchport nối 3 máy chủ Internet |
| **Google DNS** | `FastEthernet0` | `8.8.8.8` | `255.255.255.0` | `8.8.8.1` | N/A | Máy chủ DNS lưu trữ bản ghi A |
| **Google Mail** | `FastEthernet0` | `8.8.8.9` | `255.255.255.0` | `8.8.8.1` | N/A | Máy chủ Mail Internet mô phỏng |
| **Server Web** | `FastEthernet0` | `8.8.8.10` | `255.255.255.0` | `8.8.8.1` | N/A | Đóng vai trò Client Internet kiểm thử |

---

## PHẦN 2: SƠ ĐỒ TOPO KẾT NỐI THIẾT BỊ & CỔNG VẬT LÝ

```
===================== KHU VỰC DOANH NGHIỆP BANANA ===================== | ================= KHU VỰC INTERNET / ISP =================

 [ Server XOILAC ]                                                        [ Server Google DNS ]
 (IP: 10.6.9.10)                                                          (IP: 8.8.8.8)
       | Fa0                                                                    | Fa0
       |                                                                        |
       | Fa0/2 (VLAN 69)                                                        | Fa0/0/0 (Vlan 1)
+-------------------+      Trunk 802.1Q       +-------------------+             +-----------------------------------------------+
|   2950-24 SWITCH  | Fa0/1             Fa0/1 |    2811 ROUTER    | Fa0/0 Port1 |                2811 ROUTER ISP                |
|  (BANANA SWITCH)  |=========================|  (BANANA ROUTER)  |-------------| (Gắn card HWIC-4ESW vào Slot 0 cung cấp cổng) |
+-------------------+                         +-------------------+             +-----------------------------------------------+
       | Fa0/10 (VLAN 96)                           Sub: .69 & .96 [DSL-Modem]   Fa0/0/1 |                             | Fa0/0/2
       |                                                               | Port0           |                             |
       | Fa0                                                           | Phone           | Fa0                         | Fa0
 [ Server BANHMY ]                                              [Cloud-PT DSL]           |                             |
 (IP: 10.9.6.10)                                                (Modem4 <-> Eth6) [Google Mail]                     [Server Web]
                                                                       |            (8.8.8.9)                       (8.8.8.10)
                                                                       | Eth6                                     (Client duyệt Web)
                                                                 Fa0/0 |
                                                             (6.9.6.1 /24)
```

---

## PHẦN 3: HƯỚNG DẪN THAO TÁC CẤU HÌNH CHI TIẾT TỪNG BƯỚC

### Mục 3.1: Cấu hình VLAN & Trunking trên BANANA SWITCH
Truy cập CLI của **BANANA SWITCH**:

```cisco
Switch> enable
Switch# configure terminal
Switch(config)# hostname BANANA_SWITCH

! 1. Khởi tạo VLAN 69 và 96
BANANA_SWITCH(config)# vlan 69
BANANA_SWITCH(config-vlan)# name VLAN69_XOILAC
BANANA_SWITCH(config-vlan)# exit

BANANA_SWITCH(config)# vlan 96
BANANA_SWITCH(config-vlan)# name VLAN96_BANHMY
BANANA_SWITCH(config-vlan)# exit

! 2. Gán cổng Fa0/2 vào VLAN 69 (Server Xoilac)
BANANA_SWITCH(config)# interface FastEthernet 0/2
BANANA_SWITCH(config-if)# switchport mode access
BANANA_SWITCH(config-if)# switchport access vlan 69
BANANA_SWITCH(config-if)# no shutdown
BANANA_SWITCH(config-if)# exit

! 3. Gán cổng Fa0/10 vào VLAN 96 (Server Banhmy)
BANANA_SWITCH(config)# interface FastEthernet 0/10
BANANA_SWITCH(config-if)# switchport mode access
BANANA_SWITCH(config-if)# switchport access vlan 96
BANANA_SWITCH(config-if)# no shutdown
BANANA_SWITCH(config-if)# exit

! 4. Cấu hình cổng Fa0/1 làm đường Trunking nối sang Router
BANANA_SWITCH(config)# interface FastEthernet 0/1
BANANA_SWITCH(config-if)# switchport mode trunk
BANANA_SWITCH(config-if)# no shutdown
BANANA_SWITCH(config-if)# exit

BANANA_SWITCH(config)# end
BANANA_SWITCH# write memory
```

---

### Mục 3.2: Cấu hình Inter-VLAN Routing trên BANANA ROUTER (Chuẩn chỉ dẫn của Thầy)

> [!IMPORTANT]
> Dưới đây là đoạn lệnh nguyên mẫu của Thầy, đồng thời được bổ sung 2 lệnh bắt buộc: **`ip nat inside`** trên từng subinterface để phục vụ dịch vụ NAT ở bước sau.

```cisco
Router> enable
Router# configure terminal
Router(config)# hostname BANANA_ROUTER

! Bật cổng vật lý Fa0/1 kết nối Switch
BANANA_ROUTER(config)# interface FastEthernet 0/1
BANANA_ROUTER(config-if)# no ip address
BANANA_ROUTER(config-if)# no shutdown

! Cấu hình Subinterface cho VLAN 69 (Theo hướng dẫn của Thầy)
BANANA_ROUTER(config-if)# interface FastEthernet 0/1.69
BANANA_ROUTER(config-subif)# encapsulation dot1q 69
BANANA_ROUTER(config-subif)# ip address 10.6.9.1 255.255.255.0
BANANA_ROUTER(config-subif)# ip nat inside
BANANA_ROUTER(config-subif)# exit

! Cấu hình Subinterface cho VLAN 96 (Theo hướng dẫn của Thầy)
BANANA_ROUTER(config)# interface FastEthernet 0/1.96
BANANA_ROUTER(config-subif)# encapsulation dot1q 96
BANANA_ROUTER(config-subif)# ip address 10.9.6.1 255.255.255.0
BANANA_ROUTER(config-subif)# ip nat inside
BANANA_ROUTER(config-subif)# exit
```

---

### Mục 3.3: Hướng dẫn cấu hình Định tuyến ngầm định (Default Route) trên Router

#### A. Cấu hình IP và chiều NAT cho cổng WAN (`Fa0/0`):
Cổng `Fa0/0` là cổng nối ra ngoài Internet (qua DSL Modem), đóng vai trò biên mạng:
```cisco
BANANA_ROUTER(config)# interface FastEthernet 0/0
BANANA_ROUTER(config-if)# ip address 6.9.6.2 255.255.255.0
BANANA_ROUTER(config-if)# ip nat outside
BANANA_ROUTER(config-if)# no shutdown
BANANA_ROUTER(config-if)# exit
```

#### B. Cấu hình Default Route:
Vì Router của công ty Banana chỉ có duy nhất một đường ra Internet nối tới cổng `Fa0/0` của Router ISP (`6.9.6.1`), ta tạo tuyến đường mặc định:
```cisco
! Cú pháp: ip route 0.0.0.0 0.0.0.0 <Next_Hop_IP_hoặc_Exit_Interface>
BANANA_ROUTER(config)# ip route 0.0.0.0 0.0.0.0 6.9.6.1
```
*Giải thích*: Tuyến đường `0.0.0.0 0.0.0.0` đại diện cho mọi địa chỉ mạng đích trên toàn thế giới. Khi gói tin không thuộc mạng nội bộ `10.6.9.0/24` hay `10.9.6.0/24`, Router sẽ tự động chuyển tiếp gói tin tới `6.9.6.1` (ISP).

---

### Mục 3.4: Hướng dẫn cấu hình Dịch vụ Static NAT trên Router

Để người dùng ngoài Internet có thể truy cập vào các máy chủ web nội bộ:
```cisco
! Ánh xạ tĩnh 1-to-1: Server Xoilac (10.6.9.10) <---> IP Public 6.9.6.69
BANANA_ROUTER(config)# ip nat inside source static 10.6.9.10 6.9.6.69

! Ánh xạ tĩnh 1-to-1: Server Banhmy (10.9.6.10) <---> IP Public 6.9.6.96
BANANA_ROUTER(config)# ip nat inside source static 10.9.6.10 6.9.6.96

BANANA_ROUTER(config)# end
BANANA_ROUTER# write memory
```

---

### Mục 3.5: Cấu hình hạ tầng kết nối WAN (Cloud-PT DSL & ISP Router)

#### 1. Trên Cloud-PT DSL:
- Mở **Cloud-PT DSL** $\rightarrow$ chọn tab **Config** $\rightarrow$ tại menu bên trái chọn **DSL**.
- Mục **Modem**: chọn `Modem4`.
- Mục **Ethernet**: chọn `Ethernet6`.
- Bấm nút **Add** (Đảm bảo xuất hiện dòng `Modem4 <-> Ethernet6`).

#### 2. Trên ROUTER ISP:
Mở CLI của **ROUTER ISP**:
```cisco
Router> enable
Router# configure terminal
Router(config)# hostname ISP

! Cổng WAN kết nối về Banana Router
ISP(config)# interface FastEthernet 0/0
ISP(config-if)# ip address 6.9.6.1 255.255.255.0
ISP(config-if)# no shutdown
ISP(config-if)# exit

! Cấu hình Gateway cho mạng máy chủ dịch vụ Internet (gắn card HWIC-4ESW)
ISP(config)# interface Vlan 1
ISP(config-if)# ip address 8.8.8.1 255.255.255.0
ISP(config-if)# no shutdown
ISP(config-if)# exit

! Bật các switchport nối 3 máy chủ (Google DNS, Google Mail, Server Web)
ISP(config)# interface range FastEthernet 0/0/0 - 2
ISP(config-if-range)# switchport mode access
ISP(config-if-range)# switchport access vlan 1
ISP(config-if-range)# no shutdown
ISP(config-if-range)# exit

ISP(config)# end
ISP# write memory
```

---

### Mục 3.6: Hướng dẫn lưu trữ tên miền xoilac.xxx và banhmy.xxx trên Google DNS Server

1. **Cấu hình địa chỉ IP cho Google DNS**:
   - Nhấp chọn **Server Google DNS** $\rightarrow$ **Desktop** $\rightarrow$ **IP Configuration**:
     - IPv4 Address: `8.8.8.8`
     - Subnet Mask: `255.255.255.0`
     - Default Gateway: `8.8.8.1`
     - DNS Server: `8.8.8.8`
2. **Khai báo và lưu trữ bản ghi tên miền (DNS Records)**:
   - Chuyển sang tab **Services** $\rightarrow$ chọn mục **DNS** ở danh sách bên trái.
   - Chuyển nút radio **DNS Service** sang **ON**.
   - **Thêm bản ghi cho XOILAC**:
     - Name: `xoilac.xxx` *(ví dụ MSSV đuôi 123 thì gõ: `xoilac.123`)*
     - Type: `A Record`
     - Address: `6.9.6.69`  *(Lưu ý: BẮT BUỘC là IP Public đã NAT, KHÔNG ĐƯỢC nhập IP 10.6.9.10!)*
     - Bấm nút **Add**.
   - **Thêm bản ghi cho BANHMY**:
     - Name: `banhmy.xxx` *(ví dụ: `banhmy.123`)*
     - Type: `A Record`
     - Address: `6.9.6.96`  *(BẮT BUỘC là IP Public đã NAT)*
     - Bấm nút **Add**.

---

### Mục 3.7: Cấu hình 2 Web Server nội bộ (XOILAC & BANHMY)

#### 1. Máy chủ Server XOILAC:
- **IP Configuration**:
  - IP Address: `10.6.9.10`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `10.6.9.1` *(Trỏ về Subinterface Fa0/1.69)*
  - DNS Server: `8.8.8.8`
- **Dịch vụ HTTP Web**:
  - Tab **Services** $\rightarrow$ **HTTP** $\rightarrow$ Đảm bảo **HTTP: ON** và **HTTPS: ON**.
  - Tìm file `index.html` $\rightarrow$ bấm **Edit** $\rightarrow$ chỉnh sửa để khi mở web hiển thị đẹp mắt:
    ```html
    <html>
      <body bgcolor="#FFE4B5">
        <h1 align="center" style="color: brown;">CHAO MUNG DEN VOI SERVER XOILAC</h1>
        <p align="center"><b>VLAN:</b> 69 | <b>IP Noi bo:</b> 10.6.9.10 | <b>IP Public NAT:</b> 6.9.6.69</p>
      </body>
    </html>
    ```
  - Bấm **Save** (chọn Yes).

#### 2. Máy chủ Server BANHMY:
- **IP Configuration**:
  - IP Address: `10.9.6.10`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `10.9.6.1` *(Trỏ về Subinterface Fa0/1.96)*
  - DNS Server: `8.8.8.8`
- **Dịch vụ HTTP Web**:
  - Tab **Services** $\rightarrow$ **HTTP** $\rightarrow$ Đảm bảo **HTTP: ON**.
  - Tìm file `index.html` $\rightarrow$ bấm **Edit**:
    ```html
    <html>
      <body bgcolor="#E0FFFF">
        <h1 align="center" style="color: darkblue;">CHAO MUNG DEN VOI SERVER BANHMY</h1>
        <p align="center"><b>VLAN:</b> 96 | <b>IP Noi bo:</b> 10.9.6.10 | <b>IP Public NAT:</b> 6.9.6.96</p>
      </body>
    </html>
    ```
  - Bấm **Save**.

#### 3. Máy khách Client kiểm thử ngoài Internet (Server Web):
- **IP Configuration**:
  - IP Address: `8.8.8.10`
  - Subnet Mask: `255.255.255.0`
  - Default Gateway: `8.8.8.1`
  - DNS Server: `8.8.8.8`

---

## PHẦN 4: BẢN CHẤT & HƯỚNG DẪN THỰC HIỆN CÁC BƯỚC KIỂM TRA CỦA THẦY

Đây là 4 nội dung mà Thầy yêu cầu thực hiện để nghiệm thu kết quả. Dưới đây là thao tác mẫu kèm lời giải thích bản chất:

```
+---------------------------------------------------------------------------------------------------------+
|                                    4 BƯỚC KIỂM THỬ TRỌNG TÂM CỦA THẦY                                   |
|                                                                                                         |
|  [BƯỚC 1] Kiểm tra VLAN tĩnh & Ping liên VLAN:                                                          |
|           Switch# show vlan                                                                             |
|           Server XOILAC> ping 10.9.6.10                                                                 |
|                                                                                                         |
|  [BƯỚC 2] Kiểm tra phân giải tên miền DNS trên Internet:                                               |
|           Client> nslookup xoilac.xxx  ===> Trả về IP: 6.9.6.69                                        |
|           Client> nslookup banhmy.xxx  ===> Trả về IP: 6.9.6.96                                        |
|                                                                                                         |
|  [BƯỚC 3] Kiểm tra mở Website qua Web Browser:                                                          |
|           Client Browser: http://xoilac.xxx  ===> Hiện Website Xoilac                                   |
|           Client Browser: http://banhmy.xxx  ===> Hiện Website Banhmy                                   |
|                                                                                                         |
|  [BƯỚC 4] Kiểm tra bảng NAT Table với giao thức HTTP (TCP Port 80):                                     |
|           Banana_Router# show ip nat translation                                                        |
|           ===> Thấy entry dịch mã có "tcp 6.9.6.69:80  10.6.9.10:80"                                    |
+---------------------------------------------------------------------------------------------------------+
```

---

### KIỂM TRA 1: Kiểm tra VLAN tĩnh (`show vlan`) & Ping liên VLAN

#### Thao tác 1: Trên BANANA SWITCH gõ `show vlan` (hoặc `show vlan brief`)
```text
BANANA_SWITCH# show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/3, Fa0/4, Fa0/5, Fa0/6...
69   VLAN69_XOILAC                    active    Fa0/2
96   VLAN96_BANHMY                    active    Fa0/10
```
- **Giải thích cho Thầy**:
  - Cổng `Fa0/2` đã gán chính xác vào `VLAN 69` (mạng 10.6.9.0/24).
  - Cổng `Fa0/10` đã gán chính xác vào `VLAN 96` (mạng 10.9.6.0/24).
  - Cổng `Fa0/1` không có trong danh sách vì nó là cổng **Trunk** (kiểm tra bằng lệnh `show interfaces trunk`).

#### Thao tác 2: Đứng từ Server XOILAC ping sang Server BANHMY
Vào **Server XOILAC** $\rightarrow$ chọn **Desktop** $\rightarrow$ mở **Command Prompt** $\rightarrow$ gõ lệnh:
```text
C:\> ping 10.9.6.10
```
*Kết quả hiển thị trên màn hình*:
```text
Pinging 10.9.6.10 with 32 bytes of data:

Request timed out.
Reply from 10.9.6.10: bytes=32 time<1ms TTL=127
Reply from 10.9.6.10: bytes=32 time<1ms TTL=127
Reply from 10.9.6.10: bytes=32 time<1ms TTL=127

Ping statistics for 10.9.6.10:
    Packets: Sent = 4, Received = 3, Lost = 1 (25% loss),
```

- **Giải thích bản chất kỹ thuật cho Thầy**:
  1. Hai máy chủ nằm ở hai VLAN khác nhau (`VLAN 69` và `VLAN 96`) nên không thể giao tiếp trực tiếp qua Switch L2.
  2. Gói tin ping (ICMP Echo Request) được gửi từ `10.6.9.10` lên Default Gateway tại Subinterface `Fa0/1.69` của Router thông qua đường Trunk `Fa0/1` (được gắn thẻ tag 802.1Q mang VLAN ID 69).
  3. Banana Router nhận diện gói tin, bóc thẻ tag, định tuyến sang Subinterface `Fa0/1.96`, gắn thẻ tag VLAN ID 96 và đẩy ngược lại Switch xuống Server BANHMY.
  4. Gói tin đầu tiên bị `Request timed out` là do Router và Switch cần thời gian gửi bản tin **ARP Request** để học địa chỉ MAC của Server BANHMY. Các gói tin sau đều phản hồi thành công (`Reply from...`), chứng minh **Inter-VLAN Routing hoạt động hoàn hảo**.

---

### KIỂM TRA 2: Kiểm tra Phân giải DNS (`nslookup`) ngoài Internet

Vào máy **Server Web** (đóng vai Client ngoài Internet có IP `8.8.8.10`) $\rightarrow$ mở **Command Prompt** gõ:

```text
C:\> nslookup xoilac.xxx
Server:  8.8.8.8
Address: 8.8.8.8

Name:    xoilac.xxx
Address: 6.9.6.69

C:\> nslookup banhmy.xxx
Server:  8.8.8.8
Address: 8.8.8.8

Name:    banhmy.xxx
Address: 6.9.6.96
```

- **Giải thích bản chất kỹ thuật cho Thầy**:
  - Máy Client gửi gói tin truy vấn DNS (UDP port 53) đến Google DNS Server `8.8.8.8`.
  - Google DNS tra cứu bảng ghi A và trả về chính xác địa chỉ **Public NAT (Inside Global)**: `6.9.6.69` cho tên miền Xoilac và `6.9.6.96` cho tên miền Banhmy.
  - Kết quả này **tuyệt đối không được trả về IP nội bộ `10.6.9.10` hay `10.9.6.10`** vì mạng Internet toàn cầu không thể định tuyến tới các địa chỉ IP Private này.

---

### KIỂM TRA 3: Kiểm tra Truy cập Web qua Tên miền trên Trình duyệt Web

1. Trên máy Client ngoài Internet, mở công cụ **Web Browser**.
2. Tại thanh địa chỉ URL, gõ: `http://xoilac.xxx` $\rightarrow$ bấm **Go**.
   - **Kết quả**: Trình duyệt tải thành công trang web màu vàng với tiêu đề: *"CHAO MUNG DEN VOI SERVER XOILAC"*.
3. Gõ tiếp URL: `http://banhmy.xxx` $\rightarrow$ bấm **Go**.
   - **Kết quả**: Trình duyệt tải thành công trang web màu xanh với tiêu đề: *"CHAO MUNG DEN VOI SERVER BANHMY"*.

- **Giải thích bản chất kỹ thuật cho Thầy**:
  - Client gửi yêu cầu HTTP đến IP `6.9.6.69` (đã phân giải từ DNS).
  - Khi gói tin chạm vào cổng WAN `Fa0/0` của Banana Router, router thực hiện **Destination NAT**: đổi IP đích từ `6.9.6.69` thành `10.6.9.10` và chuyển vào VLAN 69.
  - Khi Server phản hồi gói tin HTTP Reply, gói tin đến Router, Router áp dụng **Reverse NAT** (đổi Source IP từ `10.6.9.10` thành `6.9.6.69`).
  - Đồng thời nhờ có **Default Route (`0.0.0.0/0 via 6.9.6.1`)**, Router biết cách chuyển tiếp gói tin trả lời ra ngoài cổng WAN để quay về máy Client.

---

### KIỂM TRA 4: Kiểm tra Bảng NAT Table (`show ip nat translation`) với giao thức HTTP (TCP Port 80)

> [!IMPORTANT]
> Đây chính là yêu cầu đặc biệt của Thầy: *"Trên Router công ty gõ lệnh `show ip nat translation` nếu hiển thị bảng NAT (NAT Table) có giao thức HTTP (Web) <-- TCP: cổng 80 là đúng."*

Mở CLI của **BANANA ROUTER** và gõ lệnh:
```cisco
BANANA_ROUTER# show ip nat translations
```
*(Lưu ý: Bạn có thể gõ `show ip nat translation` hoặc `show ip nat translations` - Cisco IOS đều chấp nhận cú pháp này).*

*Bảng kết quả hiển thị trên màn hình Router*:
```text
Pro Inside global      Inside local       Outside local      Outside global
tcp 6.9.6.69:80        10.6.9.10:80       8.8.8.10:1025      8.8.8.10:1025
--- 6.9.6.69           10.6.9.10          ---                ---
tcp 6.9.6.96:80        10.9.6.10:80       8.8.8.10:1026      8.8.8.10:1026
--- 6.9.6.96           10.9.6.10          ---                ---
```

#### Phân tích chi tiết từng cột trong bảng NAT để giải trình với Thầy:

| Cột thông số | Giá trị hiển thị | Ý nghĩa kỹ thuật cốt lõi |
| :--- | :--- | :--- |
| **`Pro`** | **`tcp`** | Giao thức tầng Giao vận (Transport Layer) được sử dụng để truyền tải dịch vụ Web HTTP. |
| **`Inside global`** | **`6.9.6.69:80`** | Địa chỉ IP công cộng kèm số hiệu cổng **TCP: 80** đại diện cho máy chủ XOILAC ra toàn cầu. |
| **`Inside local`** | **`10.6.9.10:80`** | Địa chỉ IP mạng riêng nội bộ kèm cổng dịch vụ Web **HTTP (TCP: 80)** của máy chủ thật sự. |
| **`Outside local`** | **`8.8.8.10:1025`** | Địa chỉ IP và Source Port ngẫu nhiên của máy khách Client ngoài Internet nhìn từ mạng nội bộ. |
| **`Outside global`**| **`8.8.8.10:1025`** | Địa chỉ IP thực tế và Port của máy khách Client ngoài Internet. |

> **Lời giải trình chuẩn mực cho Thầy**:  
> *"Thưa Thầy, dòng `--- 6.9.6.69  10.6.9.10` là ánh xạ tĩnh (Static NAT Entry) cố định luôn thường trực. Khi Client bên ngoài truy cập Web, Router ghi nhận một phiên kết nối thực tế với giao thức **TCP cổng 80 (HTTP Web)** xuất hiện ở dòng `tcp 6.9.6.69:80  10.6.9.10:80`. Điều này chứng minh dịch vụ Web của máy chủ nội bộ đã được biên dịch địa chỉ và phục vụ thành công ra Internet!"*

---

## PHẦN 5: BẢNG MA TRẬN XỬ LÝ SỰ CỐ KHI THẦY CHẤM (TROUBLESHOOTING MATRIX)

| Triệu chứng lỗi khi Thầy xem | Nguyên nhân cốt lõi | Câu lệnh / Thao tác khắc phục tức thời |
| :--- | :--- | :--- |
| **Ping từ Server Xoilac sang Server Banhmy bị Request timed out 100%** | 1. Quên `no shutdown` trên cổng vật lý `Fa0/1` của Router.<br>2. Chưa điền Default Gateway trên máy Server Xoilac (`10.6.9.1`) hoặc Banhmy (`10.9.6.1`). | 1. Trên Router: `interface Fa0/1` $\rightarrow$ `no shutdown`<br>2. Mở Server $\rightarrow$ Desktop $\rightarrow$ IP Configuration $\rightarrow$ điền đúng Gateway. |
| **Lệnh `nslookup` báo lỗi `DNS request timed out`** | 1. Google DNS chưa bật `DNS Service: ON`.<br>2. Client chưa cấu hình IP DNS Server `8.8.8.8`. | 1. Google DNS $\rightarrow$ Services $\rightarrow$ DNS $\rightarrow$ chọn **ON**.<br>2. Cấu hình DNS `8.8.8.8` trên Client. |
| **`nslookup` ra đúng nhưng Web Browser báo `Host Not Found` / `Timeout`** | 1. Router chưa cấu hình Default Route.<br>2. Router thiếu lệnh `ip nat outside` trên `Fa0/0`.<br>3. Chưa bấm Add cầu nối trên Cloud-PT DSL. | 1. Router: `ip route 0.0.0.0 0.0.0.0 6.9.6.1`<br>2. Router: `int Fa0/0` $\rightarrow$ `ip nat outside`<br>3. Cloud-PT DSL $\rightarrow$ add `Modem4 <-> Ethernet6`. |
| **Gõ `show ip nat translation` chỉ hiện 2 dòng `---`, không thấy dòng `tcp :80`** | Do chưa có ai mở Web Browser hoặc phiên TCP đã kết thúc (Timeout). | Giữ nguyên cửa sổ CLI, mở lại Web Browser trên Client và bấm **Go** vào `http://xoilac.xxx`, sau đó quay lại gõ ngay `show ip nat translations`. |

---

## PHẦN 6: BÍ KÍP VẤN ĐÁP BẢO VỆ ĐIỂM TỐI ĐA (10/10)

### ❓ Câu hỏi 1: *"Tại sao trên cổng Fa0/1 của Banana Router ta không gán trực tiếp IP mà lại chia thành Fa0/1.69 và Fa0/1.96?"*
- **Trả lời**: Cổng `Fa0/1` là đường truyền Trunking mang cùng lúc các khung dữ liệu của cả 2 VLAN (có gắn thẻ 802.1Q). Nếu đặt trực tiếp 1 IP lên cổng vật lý, Router sẽ chỉ hiểu đó là 1 mạng đơn nhất. Việc tạo các subinterface logic giúp Router phân tách từng luồng VLAN theo thẻ tag để đóng vai trò làm Default Gateway riêng biệt cho từng mạng con (`10.6.9.0/24` và `10.9.6.0/24`).

### ❓ Câu hỏi 2: *"Làm thế nào Router Banana nhận được gói tin gửi đến 6.9.6.69 khi cổng Fa0/0 của nó chỉ có IP là 6.9.6.2?"*
- **Trả lời**: Nhờ tính năng **Proxy ARP** được tự động kích hoạt bởi lệnh `ip nat inside source static 10.6.9.10 6.9.6.69`. Khi Router ISP gửi bản tin hỏi MAC của `6.9.6.69`, Banana Router sẽ đứng ra trả lời thay bằng chính địa chỉ MAC cổng `Fa0/0` của mình, từ đó nhận gói tin và thực hiện dịch chuyển địa chỉ NAT.

### ❓ Câu hỏi 3: *"Tại sao trong bài này ta bắt buộc phải có lệnh Default Route?"*
- **Trả lời**: Khi máy chủ Web nội bộ phản hồi yêu cầu (HTTP Response) cho Client ngoài Internet (ví dụ Client có IP `8.8.8.10`), Router không có thông tin mạng này trong bảng định tuyến cục bộ. Lệnh Default Route (`0.0.0.0 0.0.0.0 6.9.6.1`) giúp đẩy tất cả các gói tin phản hồi ra ngoài cổng WAN về phía ISP, đảm bảo phiên truyền thông hai chiều không bị đứt đoạn.
