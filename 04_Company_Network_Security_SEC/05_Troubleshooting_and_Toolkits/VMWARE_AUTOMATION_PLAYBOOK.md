# 🤖 CẨM NANG TỰ ĐỘNG HÓA VMWARE WORKSTATION (VMWARE AUTOMATION PLAYBOOK)
## Phòng 05: Troubleshooting & Toolkits — `CORP-04-SEC`
> **Mục tiêu:** Cung cấp giải pháp can thiệp, lập trình điều khiển tự động máy ảo VMware (Windows Server 2003, Linux) bằng dòng lệnh và script, thay thế hoàn toàn giao diện thủ công.

---

## 📑 MỤC LỤC
1. [Tổng Quan Năng Lực Tự Động Hóa VMware Của Agent](#1-tổng-quan-năng-lực-tự-động-hóa-vmware-của-agent)
2. [Cẩm Nang Dòng Lệnh `vmrun.exe` (VMware VIX CLI)](#2-cẩm-nang-dòng-lệnh-vmrunexe-vmware-vix-cli)
3. [Kỹ Thuật Can Thiệp Trực Tiếp File Cấu Hình `.vmx`](#3-kỹ-thuật-can-thiệp-trực-tiếp-file-cấu-hình-vmx)
4. [Tập Lệnh PowerShell Điều Khiển Mạng Ảo VMnet](#4-tập-lệnh-powershell-điều-khiển-mạng-ảo-vmnet)
5. [Quy Trình Khôi Phục Nhanh Khi Lab Bị Sự Cố (Snapshot Workflow)](#5-quy-trình-khôi-phục-nhanh-khi-lab-bị-sự-cố-snapshot-workflow)

---

## 1. TỔNG QUAN NĂNG LỰC TỰ ĐỘNG HÓA VMWARE CỦA AGENT

So với VirtualBox (`VBoxManage`), VMware Workstation sở hữu kiến trúc tự động hóa cực kỳ thân thiện với các công cụ lập trình:
- **Tệp cấu hình `.vmx` là văn bản thuần**: Có thể đọc, sửa, thay đổi tham số card mạng hoặc phần cứng bằng regex mà không sợ hỏng cây cấu trúc.
- **Tiện ích `vmrun.exe` chạy độc lập**: Hỗ trợ thực thi lệnh từ xa bên trong hệ điều hành khách (Guest Execution) và copy file 2 chiều mà không cần SSH/Telnet.

---

## 2. CẨM NANG DÒNG LỆNH `vmrun.exe` (VMWARE VIX CLI)

Đường dẫn mặc định trên Windows:
```cmd
"C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe"
```

### 2.1. Quản lý Vòng đời Máy ảo
```powershell
# 1. Liệt kê danh sách các máy ảo đang chạy
vmrun list

# 2. Khởi động máy ảo ở chế độ chạy ngầm (Headless / No GUI)
vmrun -T ws start "D:\VMs\Server2003\server.vmx" nogui

# 3. Khởi động máy ảo hiển thị giao diện đồ họa
vmrun -T ws start "D:\VMs\Server2003\server.vmx" gui

# 4. Tắt máy ảo an toàn (Graceful Shutdown)
vmrun -T ws stop "D:\VMs\Server2003\server.vmx" soft

# 5. Khởi động lại máy ảo
vmrun -T ws reset "D:\VMs\Server2003\server.vmx" soft
```

### 2.2. Can thiệp Thực thi Lệnh Trực tiếp Bên trong Khách (Guest Execution)
> Yêu cầu: Máy ảo đã cài VMware Tools và biết tài khoản Administrator.

```powershell
# Chạy lệnh xem cấu hình IP trong Server 2003
vmrun -T ws -gu Administrator -gp 123qwe!@# runProgramInGuest "D:\VMs\Server2003\server.vmx" cmd.exe /c "ipconfig /all > C:\ip_report.txt"

# Copy file kết quả từ máy ảo ra máy thật Host
vmrun -T ws -gu Administrator -gp 123qwe!@# copyFileFromGuestToHost "D:\VMs\Server2003\server.vmx" "C:\ip_report.txt" "D:\ip_report.txt"

# Bơm kịch bản cấu hình mạng hoặc dịch vụ vào Server 2003
vmrun -T ws -gu Administrator -gp 123qwe!@# copyFileFromHostToGuest "D:\VMs\Server2003\server.vmx" "D:\setup_iis.bat" "C:\setup_iis.bat"
vmrun -T ws -gu Administrator -gp 123qwe!@# runProgramInGuest "D:\VMs\Server2003\server.vmx" cmd.exe /c "C:\setup_iis.bat"
```

### 2.3. Chụp Ảnh Màn Hình Máy Ảo Nghiệm Thu Báo Cáo
```powershell
# Chụp ảnh màn hình Desktop hiện tại của Server 2003 lưu ra Host
vmrun -T ws captureScreen "D:\VMs\Server2003\server.vmx" "D:\screenshot_evidence.png"
```

---

## 3. KỸ THUẬT CAN THIỆP TRỰC TIẾP FILE CẤU HÌNH `.vmx`

File `.vmx` được cấu trúc theo dạng từng dòng `key = "value"`. Agent có thể tự động đọc và sửa đổi cấu hình mà không cần mở giao diện VMware:

### Các trường quan trọng điều khiển Card Mạng (Network):
```ini
# Gán card mạng đầu tiên (ethernet0) vào VMnet2 cho Lab 3 LAN2
ethernet0.present = "TRUE"
ethernet0.connectionType = "custom"
ethernet0.vnet = "VMnet2"

# Hoặc gán vào VMnet1 Host-Only cho Lab 4 TACACS+
ethernet0.present = "TRUE"
ethernet0.connectionType = "custom"
ethernet0.vnet = "VMnet1"

# Tinh chỉnh RAM và số nhân CPU
memsize = "1024"
numvcpus = "2"
```

---

## 4. QUY TRÌNH QUẢN LÝ SNAPSHOT AN TOÀN TRONG 3 GIÂY

Trước khi thực hành cấu hình phức tạp (như cài ACS 4.2 hoặc chỉnh sửa registry), luôn tạo một Snapshot trạng thái sạch:
```powershell
# 1. Tạo Snapshot sạch
vmrun -T ws snapshot "D:\VMs\Server2003\server.vmx" "Clean_Install_State"

# 2. Nếu lỡ tay làm hỏng cấu hình, khôi phục lại trong 3 giây:
vmrun -T ws revertToSnapshot "D:\VMs\Server2003\server.vmx" "Clean_Install_State"
```
