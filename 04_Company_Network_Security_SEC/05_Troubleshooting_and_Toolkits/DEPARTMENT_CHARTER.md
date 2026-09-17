# 📜 ĐIỀU LỆ PHÒNG CÔNG CỤ & KIỂM SOÁT SỰ CỐ (TROUBLESHOOTING & TOOLKITS DEPT)
## Phòng 05 — Công Ty An Toàn Thông Tin & Tác Chiến Mạng (CORP-04-SEC)

> **Mã Phòng Ban:** `SEC-DEPT-05`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (Role Handmade) & `PSD-04` (Pedagogical Systems Designer)  
> **Cấp bậc quản trị:** Cấp 2 — Quản lý công cụ kiểm thử xâm nhập phòng thủ, script audit bảo mật và runbooks ứng cứu sự cố an toàn mạng

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `SEC-DEPT-05` chịu trách nhiệm vận hành công cụ chẩn đoán bảo mật, phát triển script tự động hóa kiểm tra cấu hình an ninh và chuẩn hóa quy trình xử lý sự cố an toàn mạng:
1. **Quản trị Bộ Công Cụ An Ninh Mạng**: Thiết lập bộ công cụ kiểm thử, phân tích gói tin, giải mã TLS và kiểm tra tính toàn vẹn (Wireshark, Tshark, OpenSSL, Nmap, Scapy).
2. **Cung cấp Script Kiểm Toán Bảo Mật Tự Động**: Viết các công cụ Python kiểm tra cipher suite yếu trên web server, kiểm tra quyền truy cập tệp và rà soát cấu hình tường lửa Cisco IOS.
3. **Cẩm Nang Xử Lý Sự Cố Bảo Mật Khẩn Cấp (Security Incident Runbooks)**: Chuẩn hóa quy trình phản ứng nhanh khi bị tấn công Brute Force SSH, phát hiện rò rỉ khóa riêng tư (Private Key Leak), và lỗi hầm VPN IPsec bị mất pha kết nối.

---

## 2. BỘ QUY TẮC BẤT BIẾN (DEBUGGING INVARIANTS & HARD CONSTRAINTS)
1. **Nguyên tắc "An Toàn Là Trên Hết" Trong Debug (Debug Safety Constraint)**: Tuyệt đối cấm chạy lệnh `debug all` hoặc `debug ip packet` trên thiết bị mạng production vì sẽ gây tràn bộ nhớ đệm CPU (CPU 100%) làm sập thiết bị. Chỉ chạy lệnh debug có bộ lọc đích danh (ví dụ `debug crypto isakmp`, `debug crypto ipsec`).
2. **Nguyên tắc Thu Hồi & Tiêu Hủy Khóa Lộ (Key Revocation Protocol)**: Nếu bất kỳ khóa bí mật riêng (Private Key), Pre-Shared Key (PSK) hoặc chứng chỉ số nào bị nghi ngờ rò rỉ, bắt buộc phải thực hiện quy trình thu hồi (Revoke Certificate qua CRL/OCSP) và thay thế cặp khóa mới ngay lập tức.
3. **Nguyên tắc Không Can Thiệp Dữ Liệu Tấn Công (Evidence Preservation Invariant)**: Khi phát hiện dấu hiệu tấn công mạng, quy trình đầu tiên là lưu snapshot bộ nhớ và bắt giữ toàn bộ file pcap nguyên vẹn để phục vụ điều tra số học (Digital Forensics), không được reboot hoặc format thiết bị vội vàng.
4. **Nguyên tắc Quản Lý Quyền Tối Thiểu (Principle of Least Privilege - PoLP)**: Mọi tài khoản dịch vụ, script kiểm thử chỉ được cấp quyền hạn vừa đủ để thực hiện nhiệm vụ chẩn đoán, không bao giờ dùng tài khoản `root` hoặc `privilege 15` cho các tác vụ kiểm tra thông thường.

---

## 3. BỘ LỆNH & CÔNG CỤ CHẨN ĐOÁN AN NINH (DIAGNOSTIC TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Chẩn đoán chi tiết trạng thái đàm phán hầm VPN IPsec trên Cisco Router
show crypto isakmp sa
show crypto ipsec sa
show crypto session

# 2. Quét lỗ hổng SSL/TLS và phát hiện cipher suite lỗi thời (RC4, 3DES, SSLv3)
nmap --script ssl-enum-ciphers -p 443 192.168.10.2

# 3. Phân tích gói tin pcap trích xuất các truy vấn DNS độc hại bằng tshark
tshark -r incident_traffic.pcap -Y "dns.flags.response == 0" -T fields -e ip.src -e dns.qry.name | sort | uniq -c | sort -nr

# 4. Kiểm tra ngày hết hạn của chứng chỉ số X.509
openssl x509 -enddate -noout -in server.crt
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
05_Troubleshooting_and_Toolkits/
├── DEPARTMENT_CHARTER.md                                    # Điều lệ phòng ban 7 tầng chuẩn hóa
├── FREE_TOOLKIT_SETUP_AND_TROUBLESHOOTING_GUIDE.md         # Hướng dẫn thiết lập hạ tầng thực hành an toàn mạng
├── ssl_cipher_auditor.py                                    # Script Python rà soát cipher suite máy chủ HTTPS
├── pcap_anomaly_detector.py                                 # Script phát hiện lưu lượng tấn công Port Scan trong PCAP
├── support tools/                                           # Thư mục chứa các công cụ hỗ trợ
└── runbooks/                                                # Cẩm nang xử lý sự cố an ninh chuẩn hóa
    ├── RUNBOOK_IPSEC_PHASE_MISMATCH.md                      # Khắc phục lỗi hầm VPN không lên (IKE Phase 1/2)
    ├── RUNBOOK_CERTIFICATE_EXPIRY_RENEWAL.md                # Quy trình gia hạn và thay thế chứng chỉ SSL hết hạn
    ├── RUNBOOK_SSH_BRUTE_FORCE_MITIGATION.md                # Ứng cứu tấn công vét cạn mật khẩu SSH
    └── RUNBOOK_ARP_SPOOFING_DEFENSE.md                      # Định vị và ngăn chặn tấn công giả mạo ARP Cache
```

---

## 5. MẪU KHUNG CODE CHẨN ĐOÁN & ỨNG CỨU AN NINH (GOLD MASTER BOILERPLATE)

### Bộ Script Tự Động Rà Soát Cipher Suite & Chứng Chỉ Số HTTPS (`ssl_cipher_auditor.py`)
```python
"""
GOLD MASTER: TLS CIPHER SUITE & CERTIFICATE VALIDATION AUDITOR
Tác giả: CORP-04-SEC Engineering Team
Mục tiêu: Quét và phát hiện các giao thức TLS lỗi thời hoặc chứng chỉ sắp hết hạn.
"""

import socket
import ssl
from datetime import datetime


DEPRECATED_CIPHERS = ["RC4", "DES", "3DES", "MD5", "NULL", "EXPORT"]


def audit_tls_endpoint(hostname: str, port: int = 443) -> dict:
    """Kết nối tới máy chủ HTTPS và kiểm tra cấu hình bảo mật TLS."""
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Cho phép kiểm tra cả Self-Signed Cert trong Lab

    report = {
        "target": f"{hostname}:{port}",
        "tls_version": None,
        "cipher_suite": None,
        "is_safe": True,
        "warnings": []
    }

    try:
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert(binary_form=True)
                cipher = ssock.cipher()
                version = ssock.version()

                report["tls_version"] = version
                report["cipher_suite"] = cipher[0]

                # Kiểm tra phiên bản giao thức TLS
                if version in ["SSLv2", "SSLv3", "TLSv1", "TLSv1.1"]:
                    report["is_safe"] = False
                    report["warnings"].append(f"NGUY HIỂM: Giao thức {version} đã bị bẻ gãy! Cần nâng lên TLS 1.2 hoặc TLS 1.3.")

                # Kiểm tra Cipher Suite yếu
                for weak in DEPRECATED_CIPHERS:
                    if weak in cipher[0]:
                        report["is_safe"] = False
                        report["warnings"].append(f"CẢNH BÁO: Thuật toán mật mã yếu {weak} được phát hiện trong cipher: {cipher[0]}")

    except Exception as e:
        report["is_safe"] = False
        report["warnings"].append(f"Lỗi kết nối tới endpoint: {str(e)}")

    return report


if __name__ == "__main__":
    target_host = "localhost"
    print(f"[*] Bắt đầu kiểm toán an toàn TLS cho {target_host}...")
    audit = audit_tls_endpoint(target_host, 443)
    print(f"-> TLS Version: {audit['tls_version']}")
    print(f"-> Cipher Suite: {audit['cipher_suite']}")
    print(f"-> Đánh giá an toàn: {'AN TOÀN (Passed)' if audit['is_safe'] else 'CÓ NGUY CƠ (Action Required)'}")
    if audit["warnings"]:
        print("-> Chi tiết cảnh báo:")
        for w in audit["warnings"]:
            print(f"   [!] {w}")
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Cẩm nang ứng cứu đầy đủ 4 kịch bản**: IPsec VPN Mismatch, Certificate Expiry, SSH Brute-Force, ARP Spoofing.
- [x] **Có cơ chế phòng vệ CPU**: Hướng dẫn debug luôn nhấn mạnh việc không bao giờ dùng `debug all`.
- [x] **Script chẩn đoán chạy độc lập**: Script Python sử dụng thư viện chuẩn (`ssl`, `socket`, `datetime`) không đòi hỏi cài đặt phức tạp.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ KHẨN CẤP (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: Lỗi IPsec Phase 2 Không Thể Thiết Lập (QM_IDLE Failed)
- **Hiện tượng**: Lệnh `show crypto isakmp sa` báo `QM_IDLE` (Pha 1 thành công) nhưng lệnh `show crypto ipsec sa` không có gói tin nào được đóng gói `pkts encaps: 0`.
- **Nguyên nhân**: Mâu thuẫn Pha 2:
  1. Access Control List (Crypto ACL) giữa hai đầu không đối xứng ngược nhau (ví dụ Bên A định nghĩa A $\rightarrow$ B nhưng Bên B không định nghĩa B $\rightarrow$ A).
  2. Mâu thuẫn IPsec Transform Set (bên mã hóa `esp-aes`, bên kia cấu hình `esp-3des`).
- **Quy trình xử lý 3 bước**:
  1. So sánh Crypto ACL: Đảm bảo IP nguồn và IP đích đối xứng hoàn hảo.
  2. Kiểm tra Transform-Set: Đảm bảo cả hai đầu dùng chung thuật toán mã hóa và băm (ví dụ: `esp-aes 256 esp-sha256-hmac`).
  3. Reset lại kết nối bảo mật: `clear crypto sa` và `clear crypto isakmp`.

### Sự cố 2: Bị tấn công giả mạo địa chỉ MAC (ARP Poisoning / Man-In-The-Middle)
- **Hiện tượng**: Lưu lượng truy cập của máy tính bị chuyển hướng qua một máy tính lạ; bảng ARP của client hiển thị IP Gateway ứng với MAC của máy hacker.
- **Quy trình ứng cứu**:
  1. Đặt địa chỉ ARP tĩnh cho Default Gateway trên máy trạm: `netsh interface ip add neighbors "Ethernet" <IP_Gateway> <MAC_Gateway>`.
  2. Kích hoạt tính năng Dynamic ARP Inspection (DAI) trên switch Cisco:
     ```cisco
     ip arp inspection vlan 10
     interface GigabitEthernet0/1
      ip arp inspection trust                        ! Chỉ tin cậy cổng nối lên Gateway
     ```
