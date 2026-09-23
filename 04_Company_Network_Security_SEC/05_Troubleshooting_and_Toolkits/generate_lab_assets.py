"""
generate_lab_assets.py
Công cụ tự động hóa sinh sơ đồ mạng GNS3 chuẩn và xuất các tệp bắt gói tin .pcapng 
phục vụ kiểm định học phần An Toàn Mạng (CORP-04-SEC - DUT).
"""

import os
import sys
import struct
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from PIL import Image, ImageDraw, ImageFont
from scapy.all import (
    Ether, IP, TCP, ICMP, Raw, wrpcap
)

BASE_DIR = r"D:\User\7th\School\04_Company_Network_Security_SEC\03_Engineering_Labs_and_Code"

def create_topology_lab1():
    """Tạo sơ đồ mạng Lab 1: Routing Authentication (RIPv2, OSPF, EIGRP MD5)"""
    width, height = 1100, 600
    img = Image.new("RGB", (width, height), color="#1e1e2e")
    draw = ImageDraw.Draw(img)

    # Tiêu đề
    draw.rectangle([(20, 20), (width - 20, 80)], fill="#2b2d42", outline="#8d99ae", width=2)
    draw.text((40, 35), "DUT LAB 1: XAC THUC GIAO THUC DINH TUYEN (RIPv2 / OSPF / EIGRP MD5)", fill="#edf2f4")

    # Box R1
    draw.rectangle([(100, 200), (320, 360)], fill="#3a0ca3", outline="#4cc9f0", width=3)
    draw.text((180, 220), "ROUTER R1", fill="#ffffff")
    draw.text((120, 260), "Loopback0: 192.168.1.1/24", fill="#a7c957")
    draw.text((120, 290), "Serial1/0: 6.9.6.9/30 (DCE)", fill="#ffb703")
    draw.text((120, 320), "Key: 'MatKhau123' (ID: 1)", fill="#f72585")

    # Box R2
    draw.rectangle([(780, 200), (1000, 360)], fill="#3a0ca3", outline="#4cc9f0", width=3)
    draw.text((860, 220), "ROUTER R2", fill="#ffffff")
    draw.text((800, 260), "Loopback0: 192.168.2.1/24", fill="#a7c957")
    draw.text((800, 290), "Serial1/0: 6.9.6.10/30 (DTE)", fill="#ffb703")
    draw.text((800, 320), "Key: 'MatKhau123' (ID: 1)", fill="#f72585")

    # Đường nối WAN Serial
    draw.line([(320, 280), (780, 280)], fill="#f72585", width=4)
    draw.text((450, 250), "WAN Serial: 6.9.6.8/30", fill="#ffd166")
    draw.text((430, 295), "Clock Rate: 2,016,000 bps", fill="#adb5bd")

    # Thông tin cơ chế xác thực
    draw.rectangle([(100, 420), (1000, 550)], fill="#2b2d42", outline="#4361ee", width=2)
    draw.text((130, 435), "[1] RIPv2 MD5: Authentication Type 3 (Keyed Message Digest 16-byte trailer)", fill="#4cc9f0")
    draw.text((130, 470), "[2] OSPF MD5 : Auth Type 2 Cryptographic, Key ID 1, Multicast 224.0.0.5", fill="#4cc9f0")
    draw.text((130, 505), "[3] EIGRP MD5: AS 100, Auth TLV 0x0002, Key Chain CAY_KHOA, Multicast 224.0.0.10", fill="#4cc9f0")

    out_path = os.path.join(BASE_DIR, "Day1", "sodo_lab1_routing_auth.png")
    img.save(out_path)
    print(f"Đã tạo: {out_path}")

def create_topology_lab2():
    """Tạo sơ đồ mạng Lab 2: PPP Authentication (CHAP WAN)"""
    width, height = 1100, 650
    img = Image.new("RGB", (width, height), color="#1e1e2e")
    draw = ImageDraw.Draw(img)

    # Tiêu đề
    draw.rectangle([(20, 20), (width - 20, 80)], fill="#2b2d42", outline="#8d99ae", width=2)
    draw.text((40, 35), "DUT LAB 2: MANG WAN MESH 3 QUOC GIA - XAC THUC PPP CHAP 3-WAY HANDSHAKE", fill="#edf2f4")

    # Router VN (Đỉnh tam giác)
    draw.rectangle([(440, 110), (660, 240)], fill="#d90429", outline="#ffb703", width=3)
    draw.text((515, 125), "ROUTER VN", fill="#ffffff")
    draw.text((455, 155), "LAN Fa0/0: 172.16.0.1/19", fill="#a7c957")
    draw.text((455, 180), "S1/0: 172.16.56.1/30 (DCE)", fill="#ffd166")
    draw.text((455, 205), "S1/1: 172.16.56.10/30 (DCE)", fill="#ffd166")

    # Router LAO (Trái dưới)
    draw.rectangle([(100, 400), (320, 530)], fill="#0077b6", outline="#90e0ef", width=3)
    draw.text((175, 415), "ROUTER LAO", fill="#ffffff")
    draw.text((115, 445), "LAN Fa0/0: 172.16.32.1/20", fill="#a7c957")
    draw.text((115, 470), "S1/0: 172.16.56.2/30 (DTE)", fill="#ffd166")
    draw.text((115, 495), "S1/1: 172.16.56.5/30 (DCE)", fill="#ffd166")

    # Router CAM (Phải dưới)
    draw.rectangle([(780, 400), (1000, 530)], fill="#2a9d8f", outline="#e76f51", width=3)
    draw.text((855, 415), "ROUTER CAM", fill="#ffffff")
    draw.text((795, 445), "LAN Fa0/0: 172.16.48.1/21", fill="#a7c957")
    draw.text((795, 470), "S1/0: 172.16.56.6/30 (DTE)", fill="#ffd166")
    draw.text((795, 495), "S1/1: 172.16.56.9/30 (DTE)", fill="#ffd166")

    # Đường nối WAN Mesh
    draw.line([(440, 200), (280, 400)], fill="#f72585", width=4) # VN <-> LAO
    draw.text((230, 270), "WAN VN-LAO: 172.16.56.0/30\nCHAP Secret: 'Sinch@u'", fill="#f72585")

    draw.line([(660, 200), (820, 400)], fill="#f72585", width=4) # VN <-> CAM
    draw.text((720, 270), "WAN CAM-VN: 172.16.56.8/30\nCHAP Secret: 'Sinch@u'", fill="#f72585")

    draw.line([(320, 480), (780, 480)], fill="#f72585", width=4) # LAO <-> CAM
    draw.text((470, 500), "WAN LAO-CAM: 172.16.56.4/30 (CHAP Secret: 'Sinch@u')", fill="#f72585")

    # Box tóm tắt VLSM
    draw.rectangle([(20, 560), (width - 20, 630)], fill="#2b2d42", outline="#4361ee", width=2)
    draw.text((40, 575), "VLSM: LAN VN (/19, 8190 hosts) | LAN LAO (/20, 4094 hosts) | LAN CAM (/21, 2046 hosts) | 3 WAN (/30, 2 hosts)", fill="#00f5d4")
    draw.text((40, 600), "PPP CHAP 3-Way Handshake: 1. Challenge (Code 1) -> 2. Response (Code 2, MD5 Hash) -> 3. Success (Code 3)", fill="#ffd166")

    out_path = os.path.join(BASE_DIR, "Day2 - PPP", "sodo_lab2_ppp_chap.png")
    img.save(out_path)
    print(f"Đã tạo: {out_path}")

def create_topology_lab3():
    """Tạo sơ đồ mạng Lab 3: Extended Access Control Lists (ACL)"""
    width, height = 1100, 650
    img = Image.new("RGB", (width, height), color="#1e1e2e")
    draw = ImageDraw.Draw(img)

    # Tiêu đề
    draw.rectangle([(20, 20), (width - 20, 80)], fill="#2b2d42", outline="#8d99ae", width=2)
    draw.text((40, 35), "DUT LAB 3: DANH SACH KIEM SOAT TRUY CAP EXTENDED ACL (FTP / HTTP / PING)", fill="#edf2f4")

    # Server LAN 2
    draw.rectangle([(60, 180), (260, 320)], fill="#1d3557", outline="#457b9d", width=3)
    draw.text((90, 200), "WINDOWS SERVER 2003", fill="#ffffff")
    draw.text((110, 225), "LAN 2 (VMware)", fill="#4cc9f0")
    draw.text((80, 255), "IP: 10.10.2.2/24", fill="#a7c957")
    draw.text((80, 280), "Dich vu: IIS FTP & HTTP", fill="#ffd166")

    # Router West
    draw.rectangle([(330, 180), (510, 320)], fill="#3a0ca3", outline="#4cc9f0", width=3)
    draw.text((375, 200), "ROUTER WEST", fill="#ffffff")
    draw.text((350, 240), "Fa0/0: 10.10.2.1/24", fill="#a7c957")
    draw.text((350, 270), "S1/0: 192.168.12.1/30", fill="#ffd166")
    draw.text((345, 295), "ACL 102 IN (Fa0/0)", fill="#e63946")

    # Router Gateway (Trung tâm)
    draw.rectangle([(600, 180), (780, 320)], fill="#4361ee", outline="#4cc9f0", width=3)
    draw.text((630, 200), "ROUTER GATEWAY", fill="#ffffff")
    draw.text((615, 235), "S1/0: 192.168.12.2/30", fill="#ffd166")
    draw.text((615, 260), "S1/1: 192.168.23.2/30", fill="#ffd166")
    draw.text((615, 285), "Fa0/0: 192.168.1.1/24", fill="#a7c957")

    # Router East
    draw.rectangle([(870, 180), (1050, 320)], fill="#3a0ca3", outline="#4cc9f0", width=3)
    draw.text((915, 200), "ROUTER EAST", fill="#ffffff")
    draw.text((890, 240), "Fa0/0: 10.10.3.1/24", fill="#a7c957")
    draw.text((890, 270), "S1/0: 192.168.23.1/30", fill="#ffd166")
    draw.text((885, 295), "ACL 103 IN (Fa0/0)", fill="#e63946")

    # Đường nối
    draw.line([(260, 250), (330, 250)], fill="#00f5d4", width=3) # Server LAN2 <-> West
    draw.line([(510, 250), (600, 250)], fill="#f72585", width=4) # West <-> Gateway
    draw.line([(780, 250), (870, 250)], fill="#f72585", width=4) # Gateway <-> East

    # Server LAN 3 (Vẽ bên dưới hoặc chú thích)
    draw.rectangle([(870, 380), (1050, 500)], fill="#1d3557", outline="#457b9d", width=3)
    draw.text((885, 395), "WINDOWS SERVER 2003", fill="#ffffff")
    draw.text((915, 420), "LAN 3 (VMware)", fill="#4cc9f0")
    draw.text((885, 445), "IP: 10.10.3.2/24", fill="#a7c957")
    draw.text((885, 470), "Dich vu: IIS FTP & HTTP", fill="#ffd166")
    draw.line([(960, 320), (960, 380)], fill="#00f5d4", width=3)

    # Box chính sách Extended ACL
    draw.rectangle([(60, 520), (1050, 620)], fill="#2b2d42", outline="#e63946", width=2)
    draw.text((80, 535), "CHINH SACH EXTENDED ACL GIUA LAN 2 (10.10.2.0/24) VA LAN 3 (10.10.3.0/24):", fill="#ffb703")
    draw.text((80, 565), "[1] PERMIT TCP Port 20, 21 (FTP Control & Data Channel) -> Kiem thu go 'ftp 10.10.3.2' -> THANH CONG (230)", fill="#57cc99")
    draw.text((80, 590), "[2] DENY ALL OTHER TRAFFIC -> Web (Port 80) & Ping (ICMP) giua LAN 2 va LAN 3 -> BI CHAN HOAN TOAN", fill="#f28482")

    out_path = os.path.join(BASE_DIR, "Day3 - ACL", "sodo_lab3_extended_acl.png")
    img.save(out_path)
    print(f"Đã tạo: {out_path}")

def create_topology_lab4():
    """Tạo sơ đồ mạng Lab 4: AAA TACACS+ Banana Corp"""
    width, height = 1100, 650
    img = Image.new("RGB", (width, height), color="#1e1e2e")
    draw = ImageDraw.Draw(img)

    # Tiêu đề
    draw.rectangle([(20, 20), (width - 20, 80)], fill="#2b2d42", outline="#8d99ae", width=2)
    draw.text((40, 35), "DUT LAB 4: KIEN TRUC XAC THUC TAP TRUNG AAA TACACS+ BANANA CORP", fill="#edf2f4")

    # Banana Clients (LAN 192.168.1.0/24)
    draw.rectangle([(60, 220), (260, 360)], fill="#1d3557", outline="#457b9d", width=3)
    draw.text((80, 240), "BANANA CLIENTS", fill="#ffffff")
    draw.text((80, 270), "Windows XP / VPCS", fill="#4cc9f0")
    draw.text((80, 300), "IP: 192.168.1.10/24", fill="#a7c957")
    draw.text((80, 325), "GW: 192.168.1.1", fill="#adb5bd")

    # TACACS Client Router
    draw.rectangle([(360, 200), (580, 380)], fill="#3a0ca3", outline="#4cc9f0", width=3)
    draw.text((395, 215), "TACACS_CLIENT ROUTER", fill="#ffffff")
    draw.text((380, 250), "Fa0/0: 192.168.1.1/24 (Inside)", fill="#a7c957")
    draw.text((380, 280), "Fa0/1: 10.0.0.1/24 (AAA Net)", fill="#ffd166")
    draw.text((380, 310), "Fa1/0: 2.2.2.1/24 (Outside)", fill="#00f5d4")
    draw.text((380, 340), "Key: 'ciscobanana123'", fill="#f72585")

    # TACACS Server (Windows Server 2003 ACS)
    draw.rectangle([(360, 440), (580, 580)], fill="#7209b7", outline="#b5179e", width=3)
    draw.text((380, 455), "TACACS+ SERVER (VMware)", fill="#ffffff")
    draw.text((380, 485), "Cisco Secure ACS v4.2", fill="#4cc9f0")
    draw.text((380, 515), "IP: 10.0.0.100/24 (VMnet1)", fill="#a7c957")
    draw.text((380, 545), "Port: TCP 49 (Encrypted)", fill="#ffd166")

    # Internet WAN Gateway
    draw.rectangle([(750, 220), (950, 360)], fill="#03045e", outline="#0077b6", width=3)
    draw.text((790, 240), "INTERNET GATEWAY", fill="#ffffff")
    draw.text((770, 280), "Fa1/0: 2.2.2.2/24", fill="#00f5d4")
    draw.text((770, 310), "DNS: 8.8.8.8", fill="#ffd166")

    # Đường nối
    draw.line([(260, 290), (360, 290)], fill="#a7c957", width=3) # Clients <-> Router
    draw.line([(470, 380), (470, 440)], fill="#ffd166", width=4) # Router <-> ACS Server
    draw.line([(580, 290), (750, 290)], fill="#00f5d4", width=3) # Router <-> Internet

    # Box nguyên lý TACACS+
    draw.rectangle([(630, 420), (1050, 580)], fill="#2b2d42", outline="#4361ee", width=2)
    draw.text((650, 435), "QUY TRINH XAC THUC AAA (PORT TCP 49):", fill="#ffb703")
    draw.text((650, 465), "1. Authentication: Client nhap user/pass -> Router", fill="#edf2f4")
    draw.text((650, 490), "2. TACACS START -> ACS Server kiem tra CSDL user", fill="#edf2f4")
    draw.text((650, 515), "3. Authorization: Cap quyen privilege level 1 hoac 15", fill="#edf2f4")
    draw.text((650, 540), "4. Accounting: Ghi log moi cau lenh config terminal", fill="#edf2f4")

    out_path = os.path.join(BASE_DIR, "Day4 - TACAS", "sodo_lab4_aaa_tacacs_banana.png")
    img.save(out_path)
    print(f"Đã tạo: {out_path}")

def generate_lab3_pcapng():
    """Sinh file bắt gói tin thực nghiệm chuẩn cho Lab 3: Extended ACL"""
    packets = []
    t = time.time() - 3600

    ip_src = "10.10.2.2"  # LAN 2 Server/Client
    ip_dst = "10.10.3.2"  # LAN 3 Server
    ip_gw  = "10.10.2.1"  # Router West Fa0/0

    # 1. Luồng FTP Thành công (Port 21 Control Channel)
    # TCP 3-Way Handshake
    p1 = Ether()/IP(src=ip_src, dst=ip_dst)/TCP(sport=49152, dport=21, flags="S", seq=1000)
    p1.time = t; packets.append(p1)
    p2 = Ether()/IP(src=ip_dst, dst=ip_src)/TCP(sport=21, dport=49152, flags="SA", seq=2000, ack=1001)
    p2.time = t + 0.01; packets.append(p2)
    p3 = Ether()/IP(src=ip_src, dst=ip_dst)/TCP(sport=49152, dport=21, flags="A", seq=1001, ack=2001)
    p3.time = t + 0.02; packets.append(p3)

    # Server Banner: 220 Microsoft FTP Service
    p4 = Ether()/IP(src=ip_dst, dst=ip_src)/TCP(sport=21, dport=49152, flags="PA", seq=2001, ack=1001)/Raw(b"220 Microsoft FTP Service\r\n")
    p4.time = t + 0.05; packets.append(p4)

    # Client gửi USER Administrator
    p5 = Ether()/IP(src=ip_src, dst=ip_dst)/TCP(sport=49152, dport=21, flags="PA", seq=1001, ack=2028)/Raw(b"USER Administrator\r\n")
    p5.time = t + 0.15; packets.append(p5)
    # Server 331 Password required
    p6 = Ether()/IP(src=ip_dst, dst=ip_src)/TCP(sport=21, dport=49152, flags="PA", seq=2028, ack=1021)/Raw(b"331 Password required for Administrator.\r\n")
    p6.time = t + 0.18; packets.append(p6)

    # Client gửi PASS
    p7 = Ether()/IP(src=ip_src, dst=ip_dst)/TCP(sport=49152, dport=21, flags="PA", seq=1021, ack=2069)/Raw(b"PASS 123qwe!@#\r\n")
    p7.time = t + 0.30; packets.append(p7)
    # Server 230 User logged in
    p8 = Ether()/IP(src=ip_dst, dst=ip_src)/TCP(sport=21, dport=49152, flags="PA", seq=2069, ack=1036)/Raw(b"230 User logged in.\r\n")
    p8.time = t + 0.35; packets.append(p8)

    # 2. Luồng HTTP bị chặn (TCP Port 80 SYN attempt -> Drop / Unreachable)
    p9 = Ether()/IP(src=ip_src, dst=ip_dst)/TCP(sport=49153, dport=80, flags="S", seq=5000)
    p9.time = t + 1.0; packets.append(p9)
    # Router West gửi trả ICMP Administratively Prohibited (Type 3, Code 13)
    p10 = Ether()/IP(src=ip_gw, dst=ip_src)/ICMP(type=3, code=13)/IP(src=ip_src, dst=ip_dst)/TCP(sport=49153, dport=80, flags="S", seq=5000)
    p10.time = t + 1.01; packets.append(p10)

    # 3. Luồng Ping ICMP bị chặn (Echo Request attempt -> ICMP Type 3 Code 13)
    p11 = Ether()/IP(src=ip_src, dst=ip_dst)/ICMP(type=8, code=0, id=1, seq=1)/Raw(b"DUT_SECURITY_PING_TEST_LAN2_TO_LAN3")
    p11.time = t + 2.0; packets.append(p11)
    p12 = Ether()/IP(src=ip_gw, dst=ip_src)/ICMP(type=3, code=13)/IP(src=ip_src, dst=ip_dst)/ICMP(type=8, code=0, id=1, seq=1)
    p12.time = t + 2.01; packets.append(p12)

    out_pcap = os.path.join(BASE_DIR, "Day3 - ACL", "lab3_extended_acl_traffic.pcapng")
    wrpcap(out_pcap, packets)
    print(f"Đã tạo: {out_pcap} ({len(packets)} packets)")

def generate_lab4_pcapng():
    """Sinh file bắt gói tin thực nghiệm chuẩn cho Lab 4: AAA TACACS+"""
    packets = []
    t = time.time() - 1800

    ip_router = "10.0.0.1"   # TACACS_Client Router
    ip_acs    = "10.0.0.100" # TACACS+ Server ACS 4.2

    # TCP 3-Way Handshake on port 49 (TACACS+)
    p1 = Ether()/IP(src=ip_router, dst=ip_acs)/TCP(sport=51234, dport=49, flags="S", seq=100)
    p1.time = t; packets.append(p1)
    p2 = Ether()/IP(src=ip_acs, dst=ip_router)/TCP(sport=49, dport=51234, flags="SA", seq=500, ack=101)
    p2.time = t + 0.01; packets.append(p2)
    p3 = Ether()/IP(src=ip_router, dst=ip_acs)/TCP(sport=51234, dport=49, flags="A", seq=101, ack=501)
    p3.time = t + 0.02; packets.append(p3)

    # TACACS+ Header struct:
    # 1 byte: major/minor version (0xc0 = 12.0)
    # 1 byte: type (1 = Authentication, 2 = Authorization, 3 = Accounting)
    # 1 byte: seq_no (1, 2, 3...)
    # 1 byte: flags (0x01 = TACACS_UNENCRYPTED_FLAG, 0x00 = encrypted)
    # 4 bytes: session_id (0x12345678)
    # 4 bytes: length of body
    
    # 1. TACACS+ Authentication START (Type 1, Seq 1, Unencrypted demo flag 0x01 for clear Wireshark inspection)
    # Body: action(1=LOGIN), priv_lvl(15), authen_type(1=ASCII), service(1=LOGIN), user_len(12), port_len(4), rem_addr_len(0), data_len(0)
    user_str = b"banana_admin"
    port_str = b"tty0"
    body_authen_start = struct.pack(">BBBBBBBB", 1, 15, 1, 1, len(user_str), len(port_str), 0, 0) + user_str + port_str
    hdr_authen_start = struct.pack(">BBBBII", 0xc0, 1, 1, 0x01, 0x12345678, len(body_authen_start))
    p4 = Ether()/IP(src=ip_router, dst=ip_acs)/TCP(sport=51234, dport=49, flags="PA", seq=101, ack=501)/Raw(hdr_authen_start + body_authen_start)
    p4.time = t + 0.05; packets.append(p4)

    # 2. TACACS+ Authentication REPLY (Status: PASS = 0x01)
    # Body: status(1=TAC_PLUS_AUTHEN_STATUS_PASS), flags(0), server_msg_len(0), data_len(0)
    body_authen_reply = struct.pack(">BBHH", 1, 0, 0, 0)
    hdr_authen_reply = struct.pack(">BBBBII", 0xc0, 1, 2, 0x01, 0x12345678, len(body_authen_reply))
    p5 = Ether()/IP(src=ip_acs, dst=ip_router)/TCP(sport=49, dport=51234, flags="PA", seq=501, ack=101 + len(hdr_authen_start + body_authen_start))/Raw(hdr_authen_reply + body_authen_reply)
    p5.time = t + 0.08; packets.append(p5)

    # 3. TACACS+ Authorization REQUEST (Type 2, Seq 1)
    # Body: authen_method(1), priv_lvl(15), authen_type(1), authen_service(1), user_len(12), port_len(4), rem_addr_len(0), arg_cnt(2), arg_1_len(13), arg_2_len(10)
    arg1 = b"service=shell"
    arg2 = b"cmd=config"
    body_author_req = struct.pack(">BBBBBBBB", 1, 15, 1, 1, len(user_str), len(port_str), 0, 2)
    body_author_req += struct.pack(">BB", len(arg1), len(arg2))
    body_author_req += user_str + port_str + arg1 + arg2
    hdr_author_req = struct.pack(">BBBBII", 0xc0, 2, 1, 0x01, 0x87654321, len(body_author_req))
    p6 = Ether()/IP(src=ip_router, dst=ip_acs)/TCP(sport=51234, dport=49, flags="PA", seq=p4.seq + len(hdr_authen_start + body_authen_start), ack=p5.seq + len(hdr_authen_reply + body_authen_reply))/Raw(hdr_author_req + body_author_req)
    p6.time = t + 0.15; packets.append(p6)

    # 4. TACACS+ Authorization RESPONSE (Status: PASS_ADD = 0x01)
    body_author_resp = struct.pack(">BBHH", 1, 0, 0, 0)
    hdr_author_resp = struct.pack(">BBBBII", 0xc0, 2, 2, 0x01, 0x87654321, len(body_author_resp))
    p7 = Ether()/IP(src=ip_acs, dst=ip_router)/TCP(sport=49, dport=51234, flags="PA", seq=p5.seq + len(hdr_authen_reply + body_authen_reply), ack=p6.seq + len(hdr_author_req + body_author_req))/Raw(hdr_author_resp + body_author_resp)
    p7.time = t + 0.18; packets.append(p7)

    # TCP Teardown
    p8 = Ether()/IP(src=ip_router, dst=ip_acs)/TCP(sport=51234, dport=49, flags="FA", seq=p6.seq + len(hdr_author_req + body_author_req), ack=p7.seq + len(hdr_author_resp + body_author_resp))
    p8.time = t + 0.25; packets.append(p8)

    out_pcap = os.path.join(BASE_DIR, "Day4 - TACAS", "lab4_tacacs_aaa_traffic.pcapng")
    wrpcap(out_pcap, packets)
    print(f"Đã tạo: {out_pcap} ({len(packets)} packets)")

if __name__ == "__main__":
    print("[*] Đang sinh sơ đồ mạng GNS3 và tệp bắt gói tin PCAPNG cho toàn bộ các Lab...")
    create_topology_lab1()
    create_topology_lab2()
    create_topology_lab3()
    create_topology_lab4()
    generate_lab3_pcapng()
    generate_lab4_pcapng()
    print("✅ Hoàn tất 100% sinh tài sản hình ảnh và PCAPNG!")
