# 🖥️ Virtual Machine Labs (Môi trường máy ảo thực hành SEC)
## CyberDefense Corp (`CORP-04-SEC`) — VMware Workstation Migration Standard

> **Bộ môn:** An toàn thông tin & Mạng máy tính (`CORP-04-SEC`)  
> **Lưu ý kỹ thuật:** Tệp máy ảo `.ova` (>900MB) được loại trừ khỏi Git repository theo quy chuẩn MQAVP-2026 và được quản lý qua bảng mã băm SHA-256.

---

## 📦 Danh mục Tệp Máy Ảo:

| Tên Tệp OVA | Dung lượng | SHA-256 Checksum | Hệ điều hành khách | Tài khoản mặc định |
|:---|:---:|:---|:---|:---|
| `Server 2003 R2.ova` | ~968.7 MB | `2930B7388BE03CEE1778D31B43E6A0C01B2E6C55022BF9447AA4D0ACE65AE2F1` | Windows Server 2003 R2 Enterprise SP2 | `Administrator` / `123qwe!@#` |

---

## 🚀 Hướng Dẫn Import Chuyển Đổi Sang VMware Workstation Pro (100% Free):

1. **Kiểm tra tính toàn vẹn (Checksum SHA-256):**
   ```powershell
   Get-FileHash "Server 2003 R2.ova" -Algorithm SHA256
   # Hoặc dùng certutil
   certutil -hashfile "Server 2003 R2.ova" SHA256
   ```
2. **Import vào VMware Workstation Pro:**
   - Mở **VMware Workstation Pro**.
   - Chọn menu `File` $\rightarrow$ `Open...` (hoặc bấm `Ctrl + O`).
   - Trỏ tới file `Server 2003 R2.ova`.
   - Đặt tên máy ảo: `Server 2003 R2 - SEC Lab` và chọn thư mục lưu trữ trên ổ SSD.
   - Nhấn **Import**. VMware sẽ tự động giải nén OVF và chuyển đổi ổ đĩa sang định dạng `.vmdk`.
   - *Lưu ý*: Nếu xuất hiện thông báo cảnh báo OVF specification conformance, nhấn **Retry** (Bỏ qua) để VMware tự động cấu hình tương thích.
3. **Cài đặt / Cập nhật VMware Tools:**
   - Sau khi máy ảo khởi động, chọn `VM` $\rightarrow$ `Install VMware Tools...` để kích hoạt tính năng copy-paste, kéo thả file và hỗ trợ điều khiển ngầm qua `vmrun.exe`.
4. **Cấu hình Card Mạng:**
   - Mặc định máy ảo sẽ có card mạng `Bridged` hoặc `NAT`.
   - Khi thực hành Lab 3 hoặc Lab 4 kết nối GNS3, chỉnh card mạng sang:
     - `Custom: Specific virtual network` $\rightarrow$ `VMnet2` (hoặc `VMnet1` Host-Only).
