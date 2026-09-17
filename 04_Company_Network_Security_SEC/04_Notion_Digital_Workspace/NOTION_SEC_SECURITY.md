# 🔐 MASTER WORKSPACE: AN TOÀN MẠNG (SECURITY)
# Đại học Bách khoa — Đại học Đà Nẵng | Semester 7

> 🏛️ **Mã học phần**: SEC-DUT
> 🛠️ **Công cụ**: GNS3, Wireshark, Cisco Packet Tracer
> 🎯 **Trọng tâm**: Authentication Protocols (RIPv2, OSPF, EIGRP), PPP (PAP/CHAP), Packet Analysis

---

## 📊 I. COURSE PROGRESS — THEO DÕI TIẾN ĐỘ

> 💡 **Notion**: Convert thành Database → Tạo **Board View** grouped by `Chủ đề chính`.

| Chủ Đề | Nội Dung Chi Tiết | Tài Liệu Tham Khảo | Lý Thuyết | Lab GNS3 | Wireshark Analysis | Trạng Thái | Ghi Chú |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **RIPv2 Authentication** | Cấu hình MD5 Authentication cho RIPv2, chống route injection | Authentication RIPv2.pdf | ⬜ | ⬜ | ⬜ rip.pcapng | 🔲 Chưa bắt đầu | Key-chain based |
| **OSPF Authentication** | MD5 Authentication cho OSPF Area, virtual-link security | Authentication OSPF.pdf | ⬜ | ⬜ | ⬜ ospf.pcapng | 🔲 Chưa bắt đầu | Per-interface & area |
| **EIGRP Authentication** | MD5 Authentication cho EIGRP AS, neighbor verification | Authentication EIGRP.pdf | ⬜ | ⬜ | ⬜ eigrp.pcapng | 🔲 Chưa bắt đầu | Key-chain based |
| **PPP Protocol** | PAP vs CHAP Authentication, Multilink PPP, LCP/NCP | PPP.pdf | ⬜ | ⬜ | ⬜ | 🔲 Chưa bắt đầu | WAN encapsulation |
| **GNS3 & Wireshark Setup** | Cài đặt môi trường lab, capture configuration | Video hướng dẫn (.mp4) | ⬜ | ⬜ | ⬜ | 🔲 Chưa bắt đầu | Prerequisite |
| **Firewall & ACL** | Access Control Lists, Stateful Inspection | — | ⬜ | ⬜ | ⬜ | 🔲 Chưa bắt đầu | |
| **VPN Fundamentals** | IPsec, GRE Tunneling, Site-to-Site | — | ⬜ | ⬜ | ⬜ | 🔲 Chưa bắt đầu | |
| **Network Attack Analysis** | DoS, Man-in-the-Middle, ARP Spoofing | — | ⬜ | ⬜ | ⬜ | 🔲 Chưa bắt đầu | Wireshark detection |

---

## 🧠 II. PROTOCOL SECURITY FLASHCARDS (Spaced Repetition)

> 💡 **Notion Formula** cho cột `Cần Ôn?`:
> ```javascript
> if(empty(prop("Lần Ôn")), true, dateAdd(prop("Lần Ôn"), prop("Chu Kỳ"), "days") <= now())
> ```

| Giao Thức / Khái Niệm | Cơ Chế Auth | Hash/Cipher | Port / Layer | Confidence | Lần Ôn | Chu Kỳ | Cần Ôn? | CLI Cấu Hình |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **RIPv2 — MD5 Auth** | Key-chain + MD5 hash trên mỗi update | MD5 | UDP 520 / L7 | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `key chain`, `ip rip authentication` |
| **RIPv2 — Plaintext Auth** | Key-string gửi dạng cleartext (KHÔNG AN TOÀN) | None (plaintext) | UDP 520 / L7 | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `ip rip authentication mode text` |
| **OSPF — MD5 Auth (Interface)** | MD5 trên từng interface, key-id + key-string | MD5 | IP Protocol 89 / L3 | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `ip ospf message-digest-key` |
| **OSPF — MD5 Auth (Area)** | MD5 cho toàn bộ Area, áp dụng trên router ospf | MD5 | IP Protocol 89 / L3 | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `area <id> authentication message-digest` |
| **OSPF — Simple Password** | Cleartext password trên interface (TEST ONLY) | None | IP Protocol 89 / L3 | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | `ip ospf authentication-key` |
| **EIGRP — MD5 Auth** | Key-chain + MD5 hash, neighbor phải khớp key | MD5 | IP Protocol 88 / L3 | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `ip authentication mode eigrp <AS> md5` |
| **EIGRP — SHA-256 Auth** | Named mode EIGRP, HMAC-SHA-256 (mạnh hơn MD5) | SHA-256 | IP Protocol 88 / L3 | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | `authentication mode hmac-sha-256` |
| **PPP — PAP** | 2-Way Handshake, gửi username/password PLAINTEXT | None (cleartext) | Layer 2 (Data Link) | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `ppp authentication pap`, `ppp pap sent-username` |
| **PPP — CHAP** | 3-Way Handshake, Challenge-Response, KHÔNG gửi password | MD5 | Layer 2 (Data Link) | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `ppp authentication chap`, hostname+password phải khớp |
| **PPP — LCP/NCP** | LCP: thiết lập link, NCP: cấu hình protocol (IPCP) | N/A | Layer 2 | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | `debug ppp negotiation` |
| **ACL — Standard** | Lọc theo Source IP only, đặt gần Destination | N/A | Layer 3 | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `access-list <1-99> permit/deny <src>` |
| **ACL — Extended** | Lọc theo Src/Dst IP, Port, Protocol, đặt gần Source | N/A | Layer 3/4 | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `access-list <100-199> permit tcp <src> <dst> eq <port>` |
| **IPsec — AH vs ESP** | AH: chỉ auth, không mã hóa; ESP: auth + mã hóa | AH:MD5/SHA; ESP:AES/3DES | IP Protocol 51/50 / L3 | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Luôn dùng ESP cho VPN thực tế |
| **IKE Phase 1 & 2** | Phase1: ISAKMP SA (auth nhau); Phase2: IPsec SA (data tunnel) | AES/SHA/DH | UDP 500 / L7 | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | `crypto isakmp policy`, `crypto ipsec transform-set` |

---

## 🔬 III. PACKET CAPTURE ANALYSIS LOG

> 💡 **Notion**: Convert thành Database → Tạo **Gallery View** để xem visual cho từng capture.

| File Capture | Giao Thức | Ngày Capture | Tool | Phát Hiện Chính | Kết Luận Bảo Mật | Wireshark Filter | Trạng Thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **rip.pcapng** | RIPv2 | — | Wireshark | Quan sát MD5 auth field trong RIP Update | Xác thực có/không có auth → So sánh plaintext vs MD5 | `rip` hoặc `udp.port == 520` | ⬜ Chưa phân tích |
| **ospf.pcapng** | OSPF | — | Wireshark | Quan sát Hello packet + Auth field | Xác minh MD5 digest trong OSPF header | `ospf` hoặc `ip.proto == 89` | ⬜ Chưa phân tích |
| **eigrp.pcapng** | EIGRP | — | Wireshark | Quan sát EIGRP Hello + Auth TLV | Xác thực Key-ID + MD5 hash presence | `eigrp` hoặc `ip.proto == 88` | ⬜ Chưa phân tích |
| _Template_ | _Protocol_ | _YYYY-MM-DD_ | _Tool_ | _Observations..._ | _Security conclusion_ | _display filter_ | ⬜ |

---

## 📖 IV. KNOWLEDGE BASE — FEYNMAN NOTES

<details>
<summary><b>🔐 Routing Protocol Authentication — Tại sao cần?</b></summary>

### Ẩn dụ Feynman
Tưởng tượng mạng routing như một nhóm bạn chia sẻ bản đồ đường đi với nhau. Nếu **bất kỳ ai** cũng có thể tham gia nhóm và nói "Đi theo đường tôi chỉ nhé!" → Kẻ xấu có thể chỉ đường sai (route injection/poisoning) → Dữ liệu đi lạc hoặc bị chặn.

**Authentication** = Yêu cầu mỗi thành viên phải có **mật mã bí mật** (key) → Chỉ những router có đúng key mới được tham gia chia sẻ bảng định tuyến.

### So sánh 3 Routing Protocol Authentication

| Tiêu chí | RIPv2 | OSPF | EIGRP |
|:---------|:------|:-----|:------|
| **Cấu trúc Key** | Key-chain (nhiều key, xoay vòng) | Key trực tiếp trên interface/area | Key-chain (nhiều key, xoay vòng) |
| **Hash hỗ trợ** | MD5 | MD5 (Classic) / SHA (OSPFv3) | MD5 (Classic) / SHA-256 (Named) |
| **Phạm vi áp dụng** | Per-interface | Per-interface hoặc Per-area | Per-interface (trong AS) |
| **Config phức tạp** | Trung bình | Đơn giản nhất | Trung bình |

</details>

<details>
<summary><b>🔗 PPP — PAP vs CHAP Deep Dive</b></summary>

### PAP (Password Authentication Protocol)
```
Client                          Server
  |-- Username + Password ------→|  (Cleartext! Nguy hiểm!)
  |←---- Accept / Reject --------|
```
- **2-Way Handshake** — Client gửi credential, Server trả lời
- ⚠️ **Password gửi PLAINTEXT** → Wireshark bắt được ngay
- Chỉ xác thực 1 lần khi thiết lập link

### CHAP (Challenge-Handshake Authentication Protocol)
```
Client                          Server
  |←---- Challenge (random) -----|  Bước 1: Server gửi số ngẫu nhiên
  |-- MD5(Challenge+Password) --→|  Bước 2: Client hash Challenge + Password
  |←---- Accept / Reject --------|  Bước 3: Server so sánh hash
```
- **3-Way Handshake** — Challenge-Response
- ✅ **Password KHÔNG BAO GIỜ gửi qua mạng** — chỉ gửi hash
- Có thể xác thực lại định kỳ (periodic re-authentication)

### Quy tắc vàng
> **Luôn dùng CHAP.** PAP chỉ dùng khi thiết bị đối phương quá cũ không hỗ trợ CHAP.

</details>

<details>
<summary><b>🛡️ ACL — Standard vs Extended</b></summary>

### Standard ACL (1-99)
- Lọc **chỉ theo Source IP**
- Đặt **gần Destination** (vì filter ít chính xác, đặt gần nguồn sẽ block quá nhiều)
- `access-list 10 deny 192.168.1.0 0.0.0.255`

### Extended ACL (100-199)
- Lọc theo **Source IP, Destination IP, Protocol, Port**
- Đặt **gần Source** (filter chính xác, block sớm = tiết kiệm bandwidth)
- `access-list 100 permit tcp 192.168.1.0 0.0.0.255 host 10.0.0.5 eq 443`

### Wildcard Mask — Ẩn dụ
- Subnet Mask: 255.255.255.0 = "Tôi thuộc nhóm nào"
- Wildcard Mask: 0.0.0.255 = "Ai khớp với tôi?" (đảo bit của subnet mask)

</details>

<details>
<summary><b>🔒 IPsec VPN — 2 Phase Negotiation</b></summary>

### Phase 1: ISAKMP SA (Management Tunnel)
1. Thỏa thuận: Encryption (AES-256), Hash (SHA-256), DH Group (14), Authentication (Pre-shared Key)
2. Hai bên xác thực nhau bằng PSK hoặc Certificate
3. Kết quả: Tạo **ISAKMP SA** — đường hầm bảo mật để thương lượng Phase 2

### Phase 2: IPsec SA (Data Tunnel)
1. Thỏa thuận Transform Set: ESP-AES + ESP-SHA-HMAC
2. Xác định traffic cần bảo vệ (Interesting Traffic — ACL)
3. Kết quả: Tạo **IPsec SA** — đường hầm thực sự bảo vệ dữ liệu

### AH vs ESP
| | AH (Protocol 51) | ESP (Protocol 50) |
|:--|:---|:---|
| Authentication | ✅ | ✅ |
| Encryption | ❌ | ✅ |
| Dùng thực tế | Hiếm | **Luôn dùng ESP** |

</details>

---

## 💻 V. LAB CLI TEMPLATES

<details>
<summary><b>🔧 RIPv2 MD5 Authentication</b></summary>

```cisco
! === ROUTER A ===
Router-A(config)# key chain RIP_KEYS
Router-A(config-keychain)# key 1
Router-A(config-keychain-key)# key-string S3cur3K3y!
Router-A(config-keychain-key)# exit
Router-A(config-keychain)# exit

Router-A(config)# interface Serial0/0
Router-A(config-if)# ip rip authentication key-chain RIP_KEYS
Router-A(config-if)# ip rip authentication mode md5
! ⚠️ Key-chain name + key-string phải GIỐNG NHAU trên cả 2 router!

! === VERIFICATION ===
Router-A# show ip rip database
Router-A# debug ip rip
```

</details>

<details>
<summary><b>🔧 OSPF MD5 Authentication (Per-Interface)</b></summary>

```cisco
Router-A(config)# interface Serial0/0
Router-A(config-if)# ip ospf message-digest-key 1 md5 0$PF_S3cur3!
Router-A(config-if)# ip ospf authentication message-digest
! ⚠️ key-id (1) + password phải khớp trên neighbor!

! === Hoặc Per-Area ===
Router-A(config-router)# area 0 authentication message-digest

! === VERIFICATION ===
Router-A# show ip ospf neighbor
Router-A# show ip ospf interface serial0/0
Router-A# debug ip ospf adj
```

</details>

<details>
<summary><b>🔧 EIGRP MD5 Authentication</b></summary>

```cisco
Router-A(config)# key chain EIGRP_KEYS
Router-A(config-keychain)# key 1
Router-A(config-keychain-key)# key-string E1GRP_S3cur3!
Router-A(config-keychain-key)# exit

Router-A(config)# interface Serial0/0
Router-A(config-if)# ip authentication mode eigrp 100 md5
Router-A(config-if)# ip authentication key-chain eigrp 100 EIGRP_KEYS
! ⚠️ AS number (100) phải đúng, key phải khớp!

! === VERIFICATION ===
Router-A# show ip eigrp neighbors
Router-A# show key chain
```

</details>

<details>
<summary><b>🔧 PPP CHAP Authentication</b></summary>

```cisco
! === ROUTER A (hostname: RouterA) ===
RouterA(config)# username RouterB password Ch@pP@ss!
RouterA(config)# interface Serial0/0
RouterA(config-if)# encapsulation ppp
RouterA(config-if)# ppp authentication chap

! === ROUTER B (hostname: RouterB) ===
RouterB(config)# username RouterA password Ch@pP@ss!
RouterB(config)# interface Serial0/0
RouterB(config-if)# encapsulation ppp
RouterB(config-if)# ppp authentication chap

! ⚠️ CHAP rules:
! 1. username = hostname của ĐỐI PHƯƠNG (case-sensitive!)
! 2. password phải GIỐNG NHAU trên cả 2 router
! 3. hostname phải match — kiểm tra bằng `show running | include hostname`

! === VERIFICATION ===
RouterA# show ppp all
RouterA# debug ppp authentication
```

</details>

<details>
<summary><b>🔍 Wireshark Filters Cheat Sheet</b></summary>

```
# === ROUTING PROTOCOLS ===
rip                          # Tất cả gói RIP
ospf                         # Tất cả gói OSPF
eigrp                        # Tất cả gói EIGRP

# === BY PORT/PROTOCOL ===
udp.port == 520              # RIPv2
ip.proto == 89               # OSPF
ip.proto == 88               # EIGRP
tcp.port == 179              # BGP

# === PPP ===
ppp                          # Tất cả gói PPP
ppp.protocol == 0xc023       # PAP
ppp.protocol == 0xc223       # CHAP

# === SECURITY ANALYSIS ===
tcp.flags.syn == 1 && tcp.flags.ack == 0    # SYN Scan detection
arp.duplicate-address-detected               # ARP Spoofing
icmp.type == 3                               # Destination Unreachable

# === COMBINATION ===
ospf && ospf.auth.type == 2   # OSPF packets with Cryptographic Auth
```

</details>

---

## 🔴 VI. LAB ERROR JOURNAL

| Mã Lỗi | Lab | Giao Thức | Nguyên Nhân Gốc Rễ | Config Sai | Config Đúng | Mức Độ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SEC-001 | RIPv2 Auth | RIPv2 | Key-chain name không khớp giữa 2 router | Router A: `key chain RIP1`, Router B: `key chain RIP2` | Cả 2 phải cùng key-string (tên chain có thể khác) | 🚨 Nguy hiểm |
| SEC-002 | OSPF Auth | OSPF | Quên enable authentication trên interface | Chỉ set `message-digest-key` nhưng thiếu `ip ospf authentication message-digest` | Phải có CẢ 2 lệnh! | 🚨 Nguy hiểm |
| SEC-003 | EIGRP Auth | EIGRP | AS number không khớp | `ip authentication mode eigrp 100` vs neighbor dùng AS 200 | Kiểm tra `show ip eigrp neighbors` — cùng AS | 🚨 Nguy hiểm |
| SEC-004 | PPP CHAP | PPP | Username không đúng hostname đối phương | `username WrongName password...` | Username = hostname chính xác của router đối diện (case-sensitive) | 🚨 Nguy hiểm |
| SEC-005 | PPP CHAP | PPP | Password không khớp | Router A: `pass123`, Router B: `Pass123` | Password phải GIỐNG HỆT (case-sensitive!) | ⚠️ Thường gặp |
| _Template_ | _Lab_ | _Protocol_ | _Root cause analysis_ | _Wrong config_ | _Correct config_ | _⚠️/🚨_ |

---

## 🎯 VII. EXAM PREP — CHECKLIST

### ✅ Kiến thức cốt lõi cần nắm vững

**Routing Authentication:**
- [ ] Giải thích tại sao routing protocol cần authentication
- [ ] So sánh RIPv2 / OSPF / EIGRP authentication (bảng so sánh)
- [ ] Cấu hình MD5 auth cho cả 3 protocol (không nhìn tài liệu)
- [ ] Xác thực bằng `show` commands và `debug`

**PPP:**
- [ ] Phân biệt PAP vs CHAP (vẽ sơ đồ bắt tay)
- [ ] Giải thích tại sao CHAP an toàn hơn PAP
- [ ] Cấu hình PPP CHAP trên 2 router (nhớ quy tắc hostname/password)
- [ ] Debug PPP negotiation

**Wireshark Analysis:**
- [ ] Mở file .pcapng và xác định auth field
- [ ] Viết display filter cho từng protocol
- [ ] Phân biệt traffic có auth vs không auth
- [ ] Phát hiện dấu hiệu tấn công (SYN flood, ARP spoofing)

**ACL & Firewall:**
- [ ] Phân biệt Standard vs Extended ACL
- [ ] Quy tắc đặt ACL (gần source vs gần destination)
- [ ] Viết ACL cho scenario cụ thể

**IPsec VPN:**
- [ ] Giải thích IKE Phase 1 & Phase 2
- [ ] Phân biệt AH vs ESP
- [ ] Tunnel Mode vs Transport Mode

---

## 🗓️ VIII. DAILY SOP — QUY TRÌNH HỌC HÀNG NGÀY

- [ ] 🌅 **Sáng (15 phút)**: Mở DB Flashcards → Filter `Cần Ôn? = ⚠️` → Tự recall CLI trước khi xem đáp án
- [ ] 🌤️ **Chiều (60 phút)**: Mở GNS3 → Thực hành Lab theo topic hiện tại → Bắt packet Wireshark
- [ ] 🌃 **Tối (15 phút)**: Phân tích .pcapng → Ghi vào Capture Analysis Log → Ghi lỗi vào Error Journal

---

> 🏁 **Mục tiêu: Nắm vững cấu hình Auth cho 3 routing protocol + PPP CHAP. Mỗi lab xong PHẢI có file .pcapng kèm phân tích.**
