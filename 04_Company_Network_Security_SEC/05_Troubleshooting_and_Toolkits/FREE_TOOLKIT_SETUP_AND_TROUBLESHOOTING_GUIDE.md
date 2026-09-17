# 🛠️ CẨM NANG HẠ TẦNG THỰC HÀNH AN TOÀN MẠNG MIỄN PHÍ (100% FREE & OPEN-SOURCE)
## Hướng Dẫn Cài Đặt, Tối Ưu Hóa (Modify) & Sổ Tay Xử Lý Sự Cố (Troubleshooting Matrix)
> **Đơn vị ban hành:** CyberDefense Corp (`CORP-04-SEC`) — DUT Academic Mentors Hub  
> **Mentor phụ trách:** DUT Cyber Security Mentor  
> **Mục tiêu:** Trang bị toàn bộ môi trường giả lập mạng (Network Emulation), công cụ mật mã học và phân tích gói tin cho sinh viên mà không tốn một đồng chi phí bản quyền.

---

## 📑 MỤC LỤC
1. [Kiến Trúc Bộ Hành Trang 100% Miễn Phí](#1-kiến-trúc-bộ-hành-trang-100-miễn-phí)
2. [Checklist Phần Mềm, Tài Nguyên & Tài Liệu Cần Có](#2-checklist-phần-mềm-tài-nguyên--tài-liệu-cần-có)
3. [Quy Trình Cài Đặt & Cấu Hình Từng Bước (Step-by-Step)](#3-quy-trình-cài-đặt--cấu-hình-từng-bước-step-by-step)
4. [Kỹ Thuật Tinh Chỉnh & Mở Rộng Thiết Bị (Modify & Templates)](#4-kỹ-thuật-tinh-chỉnh--mở-rộng-thiết-bị-modify--templates)
5. [Ma Trận Nghiên Cứu Sự Cố & Giải Pháp Khắc Phục (Troubleshooting Matrix)](#5-ma-trận-nghiên-cứu-sự-cố--giải-pháp-khắc-phục-troubleshooting-matrix)
6. [⚠️ Lỗi Phổ Biến Sinh Viên Hay Gặp](#️-lỗi-phổ-biến-sinh-viên-hay-gặp)
7. [💡 Micro-Quiz / Câu Hỏi Phản Biện](#-micro-quiz--câu-hỏi-phản-biện)

---

## 1. KIẾN TRÚC BỘ HÀNH TRANG 100% MIỄN PHÍ

Học phần **An Toàn Mạng & Mật Mã Học Ứng Dụng (`CORP-04-SEC`)** đòi hỏi sinh viên vừa phải can thiệp ở tầng toán mật mã (Mã hóa, băm, ký số), vừa phải cấu hình trên thiết bị mạng thực tế (Router, Firewall, Switch) và bắt gói tin xác thực.

### Mô hình triển khai chuẩn trên máy Host (Windows):

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             WINDOWS HOST MACHINE                                 │
│  - Python 3.11+ (cryptography, hashlib, hmac)                                   │
│  - OpenSSL v3.x CLI (Sinh khóa RSA/ECC, ký chứng chỉ X.509)                      │
│  - Wireshark 4.x + Npcap (Bắt gói tin sâu & giải mã giao thức)                  │
│  - Tabby / Solar-PuTTY (Trình quản lý Multi-tab Console CLI)                     │
│  - GNS3 Client GUI (Phần mềm thiết kế sơ đồ mạng kéo-thả)                       │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │ TCP Port 3080 (GNS3 API)
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   VMWARE WORKSTATION PRO (Free Personal Use)                     │
│ ┌──────────────────────────────────────────────────────────────────────────────┐ │
│ │                         GNS3 VM (Ubuntu Server)                              │ │
│ │  - Nested KVM Acceleration: /dev/kvm (Tăng tốc phần cứng máy ảo)             │ │
│ │  - QEMU Emulator Engine (Chạy hệ điều hành mạng thực tế)                     │ │
│ │  - Docker Container Engine (Chạy máy trạm siêu nhẹ Alpine/Ubuntu)             │ │
│ │                                                                              │ │
│ │  [Các Node Ảo Hóa Miễn Phí Hoạt Động Bên Trong GNS3 VM]:                     │ │
│ │   1. pfSense Community Edition (Next-Gen Firewall, IPSec, OpenVPN)           │ │
│ │   2. VyOS Community Rolling / LTS (Enterprise Router, ZBF, BGP, OSPF)        │ │
│ │   3. Alpine Linux Network Host (Client/Server siêu nhẹ ~30MB RAM)            │ │
│ │   4. Cisco ASAv Evaluation (Firewall Cisco chính hãng, Free 100kbps limit)    │ │
│ │   5. Snort / Suricata IDS Container (Hệ thống phát hiện xâm nhập)            │ │
│ └──────────────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. CHECKLIST PHẦN MỀM, TÀI NGUYÊN & TÀI LIỆU CẦN CÓ

### 2.1. Phần mềm cần cài đặt (100% Free / Community)
1. **VMware Workstation Pro**: Hiện đã được Broadcom cung cấp **hoàn toàn miễn phí** cho mục đích cá nhân và học tập (*Free for Personal Use*).
2. **GNS3 All-in-One + GNS3 VM**: Bản cài đặt Client trên Windows và bản OVA máy ảo trên VMware (đồng bộ cùng phiên bản, ví dụ `2.2.49+`).
3. **Wireshark & Npcap**: Bộ đôi phân tích gói tin tiêu chuẩn công nghiệp (Open Source).
4. **OpenSSL v3.x for Windows**: Tiện ích dòng lệnh mật mã học (tải bản binary từ Shining Light Productions hoặc qua Git for Windows).
5. **Python 3.10+**: Môi trường lập trình mật mã và tự động hóa kiểm thử an ninh.
6. **Tabby Terminal / Solar-PuTTY**: Quản lý nhiều tab Console SSH/Telnet cùng lúc.

### 2.2. Tài nguyên & Appliance Image miễn phí chất lượng cao
| Tên Appliance | Định dạng | Nguồn tải / Giấy phép | Vai trò trong Học phần SEC |
| :--- | :--- | :--- | :--- |
| **VyOS** | `.qcow2` | Miễn phí (Community Build) | Làm Router định tuyến doanh nghiệp, cấu hình IPsec VPN, Zone-Based Firewall (ZBF), NAT. |
| **pfSense CE** | `.iso` / `.qcow2` | Miễn phí (Open Source) | Tường lửa có giao diện Web GUI, cấu hình kiểm soát gói tin theo trạng thái (Stateful Inspection), DMZ, OpenVPN. |
| **Alpine Linux** | Docker Image | Miễn phí (GNS3 Registry) | Cực nhẹ (chỉ tốn 30MB RAM/node), làm Web Server (Nginx), FTP Server, DNS Server hoặc Client để test ping. |
| **Cisco ASAv** | `.qcow2` | Free Evaluation (Cisco.com) | Thực hành cú pháp Cisco Adaptive Security Appliance. Giới hạn 100kbps băng thông nhưng đầy đủ 100% tập lệnh. |
| **Kali Linux** | `.qcow2` / Appliance | Miễn phí (OffSec) | Dùng làm máy tấn công giả lập: Nmap quét cổng, Hping3 tạo bão SYN Flood, Arpspoof. |

### 2.3. Tài liệu học thuật cần đọc (Tier A+ Open & Academic References)
1. **Giáo trình cốt lõi**:
   - *Cryptography and Network Security: Principles and Practice* (William Stallings) — Tham chiếu chuẩn cho các tuần lý thuyết mật mã.
   - *Wireshark Network Analysis: The Official Wireshark Certified Network Analyst Study Guide* (Laura Chappell).
2. **Tài liệu tiêu chuẩn công nghiệp (Free RFC & NIST SP)**:
   - **NIST SP 800-38A / 800-38D**: Tiêu chuẩn các chế độ khối Block Cipher (CBC, CTR, GCM).
   - **RFC 5246 (TLS 1.2) & RFC 8446 (TLS 1.3)**: So sánh cơ chế bắt tay và lý do loại bỏ RSA key exchange.
   - **RFC 4301 & RFC 7296**: Cấu trúc bảo mật IPsec và giao thức bắt tay IKEv2.
   - **NIST SP 800-52 Rev. 2**: Hướng dẫn cấu hình an toàn cho TLS trên máy chủ.
3. **Cheat Sheets & Playbooks**:
   - *Wireshark Display Filters Cheat Sheet* (SANS Institute).
   - *OpenSSL Command-line Quick Reference* (Ivan Ristić / Feisty Duck).

---

## 3. QUY TRÌNH CÀI ĐẶT & CẤU HÌNH TỪNG BƯỚC (STEP-BY-STEP)

### Bước 1: Kích hoạt Ảo hóa Phần cứng & Cài đặt VMware Workstation Pro
1. Khởi động lại máy tính, bấm `F2` / `Del` để vào **BIOS/UEFI**.
2. Tìm mục **Intel Virtualization Technology (VT-x)** hoặc **AMD-V / SVM Mode** $\rightarrow$ Chọn **Enabled** $\rightarrow$ Lưu (`F10`) và khởi động vào Windows.
3. Tải và cài đặt **VMware Workstation Pro**. Khi được hỏi mục đích sử dụng, chọn: **"Use VMware Workstation for Personal Use"** (Miễn phí bản quyền).

### Bước 2: Cài đặt GNS3 All-in-One và GNS3 VM
1. Tải bộ cài `GNS3-2.2.x-all-in-one.exe` và file `GNS3.VM.VMware.Workstation.2.2.x.zip` từ trang chủ `gns3.com`.
2. Chạy file cài đặt GNS3 trên Windows. Trong mục **Choose Components**, tích chọn:
   - `GNS3 Desktop`
   - `Wireshark`
   - `Npcap` (Lưu ý: Nếu có tùy chọn WinPcap, bỏ chọn và chỉ chọn Npcap)
   - Bỏ chọn các công cụ thương mại bên thứ ba (SolarWinds, v.v.).
3. Giải nén file zip của GNS3 VM, mở VMware Workstation $\rightarrow$ `File` $\rightarrow$ `Open` $\rightarrow$ Chọn file `GNS3 VM.ova` $\rightarrow$ Đặt tên và chọn thư mục lưu trữ (khuyến nghị trên ổ SSD).
4. **Cấu hình phần cứng cho GNS3 VM trên VMware**:
   - `Memory`: Gán tối thiểu 4 GB (tốt nhất là 8 GB - 12 GB nếu máy Host có 16 GB - 32 GB RAM).
   - `Processors`: Gán 2 Cores hoặc 4 Cores.
   - **BẮT BUỘC**: Tích vào ô checkbox **"Virtualize Intel VT-x/EPT or AMD-V/RVI"** (đây là tính năng Nested Virtualization giúp QEMU chạy tăng tốc KVM).
   - `Network Adapter`: Mặc định gồm Adapter 1 (Host-only - VMnet1) và Adapter 2 (NAT - VMnet8). Giữ nguyên.

### Bước 3: Đồng bộ GNS3 Client với GNS3 VM
1. Bật GNS3 GUI trên Windows. Hộp thoại **Setup Wizard** sẽ xuất hiện.
2. Chọn **"Run appliances in a virtual machine"** $\rightarrow$ Next.
3. Chọn VM provider: **VMware**, VM name: **GNS3 VM**.
4. GNS3 sẽ tự động gọi VMware khởi động máy ảo GNS3 VM. Khi màn hình GNS3 VM hiện IP (ví dụ: `192.168.137.128`) và thanh Server Summary trên GNS3 GUI chuyển sang **màu xanh lá cây (Green)** là thành công.

### Bước 4: Thiết lập Môi trường Mật mã Python & OpenSSL trên Windows
Mở PowerShell (Run as Administrator) và thực thi các lệnh sau:

```powershell
# 1. Kiểm tra phiên bản Python đã cài đặt
python --version

# 2. Tạo môi trường ảo riêng biệt cho học phần Security
python -m venv D:\User\7th\School\04_Company_Network_Security_SEC\sec_env

# 3. Kích hoạt môi trường ảo
& "D:\User\7th\School\04_Company_Network_Security_SEC\sec_env\Scripts\Activate.ps1"

# 4. Cài đặt các thư viện mật mã học chuyên dụng
# - cryptography: Thư viện chuẩn công nghiệp cho AES, RSA, ECC, X.509
# - scapy: Thư viện can thiệp, phân tích và giả lập gói tin ở tầng thấp
# - pycryptodome: Hỗ trợ phân tích mã khối và chế độ mã học thuật
pip install --upgrade pip
pip install cryptography scapy pycryptodome

# 5. Kiểm tra cài đặt thư viện thành công
python -c "import cryptography; print('Cryptography Version:', cryptography.__version__)"
```

---

## 4. KỸ THUẬT TINH CHỈNH & MỞ RỘNG THIẾT BỊ (MODIFY & TEMPLATES)

### 4.1. Import Thiết Bị Mạng Miễn Phí qua GNS3 Appliance Template (`.gns3a`)
Để không phải cấu hình thủ công từng thông số phần cứng của QEMU, GNS3 cung cấp kho template chuẩn:

1. Vào menu GNS3: `File` $\rightarrow$ `Import appliance`.
2. Tải các file template chính thức từ GNS3 Marketplace:
   - `vyos.gns3a`: Template dành cho router mã nguồn mở VyOS.
   - `pfsense.gns3a`: Template dành cho tường lửa pfSense.
   - `alpine.gns3a`: Template container Alpine Linux.
3. Chọn **Install the appliance on the GNS3 VM (recommended)**.
4. GNS3 sẽ liệt kê tên file image tương ứng (ví dụ: `vyos-1.4-rolling-....qcow2`). Bạn chỉ cần nhấn **Import** và trỏ đến file đã tải về.

### 4.2. Tinh chỉnh Node Alpine Linux làm Máy trạm kiểm thử siêu nhẹ
Node Alpine chỉ tốn **30MB RAM** mỗi node (so với 1-2GB của Windows XP/7). Để biến Alpine thành một Web Server HTTPS hoặc DNS Server thử nghiệm:
1. Kéo node Alpine vào Topology.
2. Chuột phải $\rightarrow$ `Edit config` để chỉnh sửa file cấu hình mạng `/etc/network/interfaces`:
```text
# Cấu hình IP tĩnh cho máy trạm thử nghiệm
auto eth0
iface eth0 inet static
    address 192.168.10.100
    netmask 255.255.255.0
    gateway 192.168.10.1
```
3. Khởi động Alpine, mở console và cài đặt nhanh các công cụ mạng:
```bash
# Cập nhật repository và cài đặt công cụ kiểm tra mạng
apk update
apk add curl tcpdump bind-tools openssl nginx

# Khởi động dịch vụ web server phục vụ lab kiểm tra tường lửa
rc-service nginx start
```

### 4.3. Tối ưu hóa Idle-PC cho Router Cisco Dynamips (Nếu dùng Router c3725 / c7200)
Nếu bạn có sẵn image Cisco IOS cổ điển (`.bin`):
1. Vào `Edit` $\rightarrow$ `Preferences` $\rightarrow$ `Dynamips` $\rightarrow$ `IOS Routers`.
2. Chọn Router $\rightarrow$ Bấm `Edit` $\rightarrow$ Tab `Advanced`.
3. Nhấp vào nút **"Idle-PC finder"**. GNS3 sẽ chạy thử router và tìm một giá trị offset có dấu hoa thị `*` (ví dụ: `0x60bf8038*`).
4. Áp dụng giá trị này. Khi khởi chạy, CPU máy tính Host sẽ duy trì ở mức dưới 5%.

---

## 5. MA TRẬN NGHIÊN CỨU SỰ CỐ & GIẢI PHÁP KHẮC PHỤC (TROUBLESHOOTING MATRIX)

Bảng ma trận phân tích từ triệu chứng (Symptoms), bản chất gốc rễ (Root Cause), cách dự đoán (Predictive Checks) đến quy trình xử lý chi tiết (Remediation Workflow):

| Mã lỗi | Triệu chứng thực tế | Nguyên nhân gốc rễ (Root Cause) | Lệnh / Thao tác dự đoán lỗi | Quy trình khắc phục chuẩn |
| :--- | :--- | :--- | :--- | :--- |
| **ERR-01** | Bật GNS3 báo: *“Cannot connect to compute 'GNS3 VM' on 192.168.x.x:3080”*. GNS3 VM chấm xám/đỏ. | Lệch dải IP của VMware Network Adapter (VMnet1/VMnet8) hoặc Firewall Windows chặn port 3080. | `Test-NetConnection -ComputerName <IP_GNS3_VM> -Port 3080` trong PowerShell. | 1. Mở VMware `Virtual Network Editor` $\rightarrow$ Bấm `Restore Defaults` để reset lại card mạng ảo.<br>2. Thêm rule cho phép TCP port 3080 qua Windows Defender Firewall. |
| **ERR-02** | Kéo thiết bị QEMU (VyOS, ASAv) ra bật thì báo lỗi: *“KVM acceleration is not available”*. Thiết bị không khởi động được. | Chưa bật ảo hóa lồng nhau (Nested VT-x) trong VMware hoặc CPU Host chưa kích hoạt VT-x trong BIOS. | Trên GNS3 VM console chạy: `egrep -c '(vmx\|svm)' /proc/cpuinfo`. Nếu ra số 0 là chưa nhận KVM. | 1. Tắt GNS3 VM hoàn toàn.<br>2. Mở VMware Settings $\rightarrow$ `Processors` $\rightarrow$ Tích chọn: `Virtualize Intel VT-x/EPT or AMD-V/RVI`.<br>3. Khởi động lại GNS3 VM. |
| **ERR-03** | Khởi chạy 1-2 Router Cisco Dynamips làm quạt tản nhiệt rú mạnh, Task Manager báo CPU Host 100%. | Chưa tính toán hoặc mất giá trị `Idle-PC`. Dynamips liên tục lặp vô tận trong chu kỳ CPU MIPS. | Mở Task Manager trên Windows $\rightarrow$ Tab `Details` $\rightarrow$ Tìm tiến trình `dynamips.exe` chiếm 50-100% CPU. | 1. Trong GNS3, chuột phải vào Router $\rightarrow$ Chọn **Idle-PC**.<br>2. Chờ GNS3 tính toán khoảng 10 giây $\rightarrow$ Chọn giá trị có đánh dấu `*` trong ngoặc vuông $\rightarrow$ Apply. |
| **ERR-04** | Chuột phải vào dây cáp chọn *Start capture* nhưng Wireshark không hiện lên, hoặc báo lỗi *“Npcap is not running”*. | Dịch vụ Npcap bị dừng hoặc xung đột giữa Npcap và driver WinPcap cũ trên Windows. | Mở CMD (Admin): `sc query npcap`. Kiểm tra State có phải `RUNNING` hay không. | 1. Chạy lệnh: `net start npcap`.<br>2. Nếu vẫn lỗi, gỡ sạch Wireshark và Npcap, tải bản Npcap mới nhất từ `npcap.com` và cài lại với tùy chọn *"Support loopback traffic"*. |
| **ERR-05** | Hai thiết bị nối với nhau trong GNS3 đã up interface, cấu hình đúng IP nhưng không thể ping thấy nhau. | GNS3 VM bị nghẽn switch ảo `uBridge` hoặc xung đột card mạng Host-Only VMnet1. | 1. Kiểm tra MAC table trên switch ảo.<br>2. Chạy Wireshark bắt trực tiếp trên đường truyền giữa 2 node xem có ARP Request đi ra không. | 1. Xóa đường link kết nối, cắm lại sang port khác.<br>2. Nếu là node Docker/Linux, kiểm tra lệnh `iptables -L -n` xem chính sách mặc định có DROP gói tin ICMP hay không. |
| **ERR-06** | Python báo lỗi: *“ImportError: cannot import name 'AES' from 'Crypto.Cipher'”*. | Cài đặt xung đột cùng lúc cả 2 gói thư viện `crypto` và `pycryptodome`. | `pip list \| Select-String "crypto"` | 1. Gỡ cài đặt cả 2 thư viện:<br>`pip uninstall -y crypto pycrypto pycryptodome`<br>2. Cài đặt lại DUY NHẤT một gói:<br>`pip install pycryptodome` |

---

## 6. ⚠️ LỖI PHỔ BIẾN SINH VIÊN HAY GẶP

1. **Lệch phiên bản GNS3 GUI và GNS3 VM**:
   - *Biểu hiện*: Tải GNS3 GUI bản mới nhất (vd: `2.2.49`) nhưng lại dùng file OVA của GNS3 VM bản cũ (vd: `2.2.38`).
   - *Hậu quả*: Client liên tục báo lỗi phiên bản giao thức không tương thích và ngắt kết nối. Luôn đảm bảo tải cả hai từ cùng một release page.
2. **Cấu hình sai dải mạng trong VMware Virtual Network Editor**:
   - Khi chỉnh sửa card mạng lung tung trên máy tính hoặc bật phần mềm VPN bên thứ ba (Cisco AnyConnect, OpenVPN client, WARP 1.1.1.1), các adapter `VMnet1` và `VMnet8` bị định tuyến đè lên, khiến GNS3 Client không thể giao tiếp với GNS3 VM qua port 3080.
   - *Cách giải quyết tức thời*: Tắt phần mềm VPN trên máy tính Host trước khi mở GNS3.
3. **Cố gắng chạy các bài lab Switch L2 nâng cao trên Router gắn card `NM-16ESW`**:
   - Card switch mở rộng cũ này của Cisco Dynamips không hỗ trợ Private VLAN, Spanning-Tree MSTP hiện đại hay Dynamic ARP Inspection. Hãy chuyển sang sử dụng thiết bị mạng ảo hóa thuần L2 (như Cisco IOL L2 hoặc Open vSwitch tích hợp trong GNS3).
4. **Quên lưu cấu hình thiết bị trước khi tắt GNS3 Project**:
   - Trên các thiết bị mạng (VyOS, Cisco, pfSense), nếu chỉ nhấn nút Stop hoặc tắt GNS3 mà chưa thực hiện lệnh lưu cấu hình vào bộ nhớ bất biến (`commit; save` trên VyOS hoặc `write memory` trên Cisco), toàn bộ cấu hình sẽ biến mất trong lần khởi động sau.

---

## 7. 💡 MICRO-QUIZ / CÂU HỎI PHẢN BIỆN

> **Câu hỏi dành cho sinh viên:**  
> Giả sử bạn đang dựng một mô hình kiểm thử an ninh mạng gồm 1 Tường lửa **pfSense** (đóng vai trò Gateway) và 2 máy trạm **Alpine Linux** (đóng vai trò Web Server DMZ và Attacker ngoài WAN). Khi bạn dùng Wireshark bắt gói tin trên đường link kết nối giữa pfSense và Web Server:  
> **Tại sao bạn nhìn thấy gói tin TCP SYN gửi từ Attacker đến Web Server, nhưng hoàn toàn KHÔNG thấy gói tin TCP SYN-ACK phản hồi trở lại, mặc dù Web Server vẫn đang chạy dịch vụ Nginx bình thường? Hãy nêu 2 nguyên nhân gốc rễ có thể xảy ra trong môi trường mạng giả lập này.**
