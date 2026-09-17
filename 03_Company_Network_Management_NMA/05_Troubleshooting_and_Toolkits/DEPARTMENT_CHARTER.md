# 📜 ĐIỀU LỆ PHÒNG CÔNG CỤ & PHẦN MỀM HẠ TẦNG (TOOLS & INFRASTRUCTURE SOFTWARE DEPT)
## Phòng 05 — Công Ty Hạ Tầng & Quản Trị Mạng Doanh Nghiệp (CORP-03-NMA)

> **Mã Phòng Ban:** `NMA-DEPT-05`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (Role Handmade) & `PSD-04` (Pedagogical Systems Designer)  
> **Cấp bậc quản trị:** Cấp 2 — Quản lý công cụ chẩn đoán mạng, script tự động hóa hạ tầng (Netmiko/Scapy) và cẩm nang xử lý sự cố FCAPS

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `NMA-DEPT-05` chịu trách nhiệm vận hành công cụ chẩn đoán hạ tầng, phát triển script tự động hóa kiểm tra mạng và chuẩn hóa quy trình xử lý sự cố cho các hệ thống mạng doanh nghiệp:
1. **Quản lý Bộ Công Cụ Chẩn Đoán Mạng**: Thiết lập bộ công cụ kiểm tra thông tuyến, bắt và phân tích gói tin (Wireshark, tcpdump, Nmap, iperf3, traceroute).
2. **Tự Động Hóa Quản Trị Hệ Thống (Network Automation)**: Cung cấp script Python (Netmiko, Scapy) tự động quét cổng, sao lưu cấu hình Router/Switch Cisco định kỳ và kiểm tra tính sẵn sàng của dịch vụ.
3. **Cẩm Nang Xử Lý Sự Cố 7 Tầng OSI**: Xây dựng quy trình ứng cứu sự cố chuẩn hóa (Runbooks) cho các lỗi kinh điển: Bão Broadcast do vòng lặp L2 (STP Failure), đụng độ IP (IP Conflict), cạn kiệt dải cấp phát DHCP và nghẽn băng thông do tấn công từ chối dịch vụ.

---

## 2. BỘ QUY TẮC BẤT BIẾN (DEBUGGING INVARIANTS & HARD CONSTRAINTS)
1. **Nguyên tắc Chẩn Đoán Dưới-Lên (Bottom-Up OSI Troubleshooting Invariant)**: Mọi quy trình xử lý sự cố mất kết nối mạng bắt buộc phải kiểm tra theo thứ tự: Layer 1 (Cáp/Đèn cổng) $\rightarrow$ Layer 2 (MAC Table, VLAN, STP State) $\rightarrow$ Layer 3 (ARP Table, IP Address, Routing Table) $\rightarrow$ Layer 4-7 (Firewall, Cổng dịch vụ). Tuyệt đối cấm can thiệp phần mềm khi tầng vật lý hoặc liên kết dữ liệu chưa Up/Up.
2. **Nguyên tắc Độc Lập Thiết Bị & Cô Lập Lỗi (Fault Isolation Rule)**: Khi xảy ra sự cố diện rộng, kỹ sư phải lập tức cô lập vùng lỗi (VLAN hoặc Subnet tương ứng) bằng cách ngắt kết nối Trunk hoặc vô hiệu hóa cổng để bảo vệ mạng lõi trước bão Broadcast.
3. **Nguyên tắc Quản Lý File Cài Đặt Quá Khổ (Large File Invariant)**: Bộ cài đặt phần mềm nặng (`.exe`, `.iso`, `.ova` vượt quá 50MB) phải được quản lý qua link chia sẻ nội bộ hoặc lưu trong `.gitignore`. File mô tả `README.md` lưu trữ checksum SHA-256 chính thức để xác thực tính toàn vẹn.
4. **Nguyên tắc Lưu Vết Sự Cố (Audit Logging & Post-Mortem)**: Mọi sự cố gián đoạn mạng đều phải được ghi nhận vào nhật ký sự cố gồm: Thời điểm xảy ra, Triệu chứng, Nguyên nhân gốc rễ (Root Cause), Các bước khắc phục và Biện pháp phòng ngừa tái diễn.

---

## 3. BỘ LỆNH & CÔNG CỤ CHẨN ĐOÁN MẠNG (DIAGNOSTIC TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Quét trạng thái cổng và phát hiện dịch vụ mạng đang chạy bằng Nmap
nmap -sS -sV -p 22,53,67,80,389,443,445 192.168.10.0/24

# 2. Đo lường băng thông thực tế và độ trễ mạng giữa Client và Server với iperf3
iperf3 -c 192.168.10.2 -t 10 -P 4

# 3. Phân tích đường đi và độ trễ từng chặng (Hop-by-hop latency)
mtr --report --report-cycles=10 192.168.10.1

# 4. Kiểm tra bảng phân giải địa chỉ MAC (ARP Table) và xóa cache ARP
arp -a
arp -d *

# 5. Bắt gói tin DHCP DORA lọc theo bootp
sudo tcpdump -i eth0 -vvv -s 1500 '((port 67 or port 68) and (udp[248:4] = 0x63825363))'
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
05_Troubleshooting_and_Toolkits/
├── DEPARTMENT_CHARTER.md                          # Điều lệ phòng ban 7 tầng chuẩn hóa
├── network_health_scanner.py                      # Script tự động quét IP & Ping Sweep toàn mạng
├── cisco_config_backup.py                         # Script sao lưu tự động cấu hình router/switch
├── README_LARGE_BINARIES.md                       # Hướng dẫn tải & Checksum SHA-256 các bộ cài
├── chi phí đi dây, chi phí công thợ, c.txt       # Định mức dự toán kinh tế cho đồ án mạng
└── runbooks/                                      # Cẩm nang ứng cứu sự cố mạng chuẩn hóa
    ├── RUNBOOK_L2_BROADCAST_STORM.md              # Khắc phục bão Broadcast và lỗi STP
    ├── RUNBOOK_IP_CONFLICT_RESOLUTION.md          # Định vị và xử lý xung đột địa chỉ IP
    ├── RUNBOOK_DHCP_STARVATION_EXHAUSTION.md      # Xử lý cạn kiệt dải IP DHCP
    └── RUNBOOK_MTU_MSS_MISMATCH.md                # Xử lý phân mảnh gói tin và kẹt đường truyền
```

---

## 5. MẪU KHUNG CODE CHẨN ĐOÁN & ỨNG CỨU MẠNG (GOLD MASTER BOILERPLATE)

### Bộ Script Tự Động Quét Dải Mạng & Kiểm Tra Tính Sẵn Sàng Dịch Vụ Core (`network_health_scanner.py`)
```python
"""
GOLD MASTER: AUTOMATED NETWORK SERVICE HEALTH CHECKER
Tác giả: CORP-03-NMA Infrastructure Engineering Team
Mục tiêu: Quét nhanh dải Subnet, kiểm tra ICMP Ping và các cổng dịch vụ lõi (DNS, DHCP, HTTP, SSH).
"""

import socket
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor


CORE_SERVICES = {
    53: "DNS",
    67: "DHCP",
    80: "HTTP",
    389: "LDAP (Active Directory)",
    443: "HTTPS",
    445: "SMB / File Sharing",
    22: "SSH"
}


def ping_host(host_ip: str, timeout_ms: int = 1000) -> bool:
    """Gửi 1 gói tin ICMP Echo Request để xác định host còn sống."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    timeout_flag = "-w" if platform.system().lower() == "windows" else "-W"
    cmd = ["ping", param, "1", timeout_flag, str(timeout_ms), host_ip]
    try:
        res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return res.returncode == 0
    except Exception:
        return False


def scan_port(host_ip: str, port: int, timeout_sec: float = 1.0) -> bool:
    """Kiểm tra một cổng TCP cụ thể có đang mở và lắng nghe hay không."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout_sec)
    try:
        result = sock.connect_ex((host_ip, port))
        sock.close()
        return result == 0
    except Exception:
        return False


def audit_host_services(host_ip: str) -> dict:
    """Kiểm tra toàn diện một máy chủ mạng."""
    is_alive = ping_host(host_ip)
    report = {
        "ip": host_ip,
        "is_alive": is_alive,
        "open_services": []
    }
    if not is_alive:
        return report

    for port, service_name in CORE_SERVICES.items():
        if scan_port(host_ip, port):
            report["open_services"].append(f"{service_name} (Port {port})")
            
    return report


if __name__ == "__main__":
    test_ip = "192.168.10.2"
    print(f"[*] Bắt đầu kiểm toán máy chủ: {test_ip}...")
    res = audit_host_services(test_ip)
    print(f"-> Trạng thái: {'HOẠT ĐỘNG (Alive)' if res['is_alive'] else 'MẤT KẾT NỐI (Down)'}")
    print(f"-> Các dịch vụ đang mở: {res['open_services'] if res['open_services'] else 'Không có dịch vụ nào phản hồi'}")
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Cô lập lỗi theo 7 tầng**: Toàn bộ tài liệu hướng dẫn xử lý sự cố phải trình bày theo trình tự OSI từ thấp lên cao.
- [x] **Có kịch bản tái hiện & giải pháp**: Mỗi Runbook phải nêu rõ: Triệu chứng nhận biết, Nguyên nhân gốc rễ, Lệnh kiểm chứng và Câu lệnh cấu hình khắc phục tức thời.
- [x] **An toàn kho mã nguồn Git**: Bộ cài đặt phần mềm lớn được quản lý qua tài liệu checksum SHA-256, không chứa binary >100MB trong git index.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ KHẨN CẤP (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: Bão Broadcast làm tê liệt toàn bộ hệ thống mạng Switch (Layer 2 Loop)
- **Hiện tượng**: Đèn cổng switch nhấp nháy điên cuồng liên tục với tần suất cao; băng thông mạng bị nghẽn 100%; không thể ping tới gateway hoặc latency vọt lên hàng nghìn ms.
- **Nguyên nhân gốc rễ**: Có người dùng cắm nhầm hai đầu dây cáp vào hai cổng của cùng một switch hoặc nối hai switch với nhau tạo thành vòng kín mà Spanning Tree Protocol (STP) bị vô hiệu hóa hoặc chưa hội tụ.
- **Quy trình xử lý 4 bước**:
  1. *Bước 1 (Cách ly khẩn cấp)*: Lập tức rút cáp uplink kết nối giữa các switch hoặc shutdown cổng có lưu lượng tăng vọt.
  2. *Bước 2 (Kiểm tra Spanning Tree)*: Đăng nhập console switch và gõ lệnh:
     ```cisco
     show spanning-tree active
     ```
  3. *Bước 3 (Bật STP & BPDU Guard)*: Kích hoạt Rapid-PVST và tính năng chống cắm nhầm trên cổng Access:
     ```cisco
     spanning-tree mode rapid-pvst
     interface range FastEthernet0/1 - 24
      spanning-tree portfast
      spanning-tree bpduguard enable
     ```
  4. *Bước 4 (Xác nhận)*: Kiểm tra đèn switch chuyển về trạng thái ổn định và latency ping giảm về dưới 1ms.

### Sự cố 2: Đụng độ địa chỉ IP (IP Address Conflict) trong mạng nội bộ
- **Hiện tượng**: Người dùng liên tục bị mất mạng kèm thông báo "Windows has detected an IP address conflict"; ARP table bị thay đổi địa chỉ MAC liên tục (ARP Flapping).
- **Quy trình xử lý**:
  1. Kiểm tra địa chỉ MAC đang tranh chấp bằng lệnh `arp -a`.
  2. Tra cứu địa chỉ MAC trên Switch Core để định vị cổng vật lý gây lỗi:
     ```cisco
     show mac address-table address <MAC_Tranh_Chap>
     ```
  3. Shutdown cổng của thiết bị cài đặt IP tĩnh sai quy hoạch hoặc cấu hình DHCP Snooping trên Switch để chặn các thiết bị tự ý đặt IP.
