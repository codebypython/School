# 🧹 CẨM NANG DỌN DẸP & GỠ CÀI ĐẶT HOÀN TOÀN ORACLE VIRTUALBOX
## Phòng 05: Troubleshooting & Toolkits — `CORP-04-SEC`
> **Mục tiêu:** Loại bỏ hoàn toàn Oracle VirtualBox, dọn dẹp card mạng ảo `vboxnet` bị thừa, giải phóng tài nguyên và tránh xung đột với hệ sinh thái VMware Workstation Pro.

---

## 📑 MỤC LỤC
1. [Tại Sao Cần Gỡ Bỏ VirtualBox Sau Khi Chuyển Sang VMware](#1-tại-sao-cần-gỡ-bỏ-virtualbox-sau-khi-chuyển-sang-vmware)
2. [Checklist An Toàn Trước Khi Gỡ Bỏ](#2-checklist-an-toàn-trước-khi-gỡ-bỏ)
3. [Quy Trình Dọn Dẹp & Gỡ Cài Đặt Tự Động Bằng PowerShell](#3-quy-trình-dọn-dẹp--gỡ-cài-đặt-tự-động-bằng-powershell)
4. [Các Bước Gỡ Bỏ Thủ Công Qua Windows Settings (Nếu Muốn)](#4-các-bước-gỡ-bỏ-thủ-công-qua-windows-settings-nếu-muốn)
5. [Kiểm Tra Xác Nhận Hệ Thống Sau Khi Gỡ Bỏ](#5-kiểm-tra-xác-nhận-hệ-thống-sau-khi-gỡ-bỏ)

---

## 1. TẠI SAO CẦN GỠ BỎ VIRTUALBOX SAU KHI CHUYỂN SANG VMWARE

Khi bạn đã chuyển dịch toàn bộ các bài Lab sang **VMware Workstation Pro**:
1. **Tránh xung đột card mạng ảo**: VirtualBox tạo các card mạng ảo `VirtualBox Host-Only Network Adapter` (`vboxnet0`, `vboxnet1`...). Trên Windows 10/11, driver `VBoxNetAdp` rất hay xung đột với driver mạng của VMware (`VMnet1`, `VMnet8`), làm gián đoạn việc truyền gói tin trong GNS3.
2. **Dừng các tiến trình ngầm**: Tiến trình `VBoxSVC.exe` liên tục chạy ngầm trong Task Manager để quản lý socket, gây tốn RAM và CPU.
3. **Đồng bộ GNS3**: Khi GNS3 không còn thấy VirtualBox, phần mềm sẽ không bao giờ hiển thị cảnh báo đỏ thiếu máy ảo nữa.

---

## 2. CHECKLIST AN TOÀN TRƯỚC KHI GỠ BỎ

- [x] **Toàn bộ máy ảo cần thiết đã được chuyển đổi**: Đã triển khai xong `Server2003_LAN2`, `Server2003_LAN3`, `TACAS_Server` trên VMware Workstation (`D:\VMware_SEC_Labs`).
- [x] **GNS3 project đã được cập nhật**: File `acl.gns3` và `TACAS.gns3` đã chuyển sang `node_type: "vmware"` và `node_type: "cloud"`.
- [x] **Tắt toàn bộ máy ảo đang chạy**: Đảm bảo không có máy ảo VirtualBox nào đang bật.

---

## 3. QUY TRÌNH DỌN DẸP & GỠ CÀI ĐẶT TỰ ĐỘNG BẰNG POWERSHELL

Chúng tôi đã thiết lập sẵn kịch bản PowerShell tự động:  
👉 [`uninstall_virtualbox_safely.ps1`](uninstall_virtualbox_safely.ps1)

### Cách thực thi (Mở PowerShell với quyền Administrator):
```powershell
# Di chuyển vào thư mục toolkits và chạy script dọn dẹp:
cd "D:\User\7th\School\04_Company_Network_Security_SEC\05_Troubleshooting_and_Toolkits"
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\uninstall_virtualbox_safely.ps1
```

### Các tác vụ mà script tự động thực hiện:
1. Quét tìm và tắt triệt để các tiến trình VirtualBox (`VirtualBox.exe`, `VBoxSVC.exe`, `VBoxHeadless.exe`).
2. Xóa sạch các card mạng ảo `VirtualBox Host-Only Ethernet Adapter` bằng lệnh `VBoxManage hostonlyif remove`.
3. Gọi trình gỡ cài đặt chính thức của Windows (MSI uninstaller hoặc `winget uninstall Oracle.VirtualBox`).
4. Xóa thư mục cấu hình rác trong `%USERPROFILE%\.VirtualBox`.

---

## 4. CÁC BƯỚC GỠ BỎ THỦ CÔNG QUA WINDOWS SETTINGS (NẾU MUỐN)

Nếu muốn thao tác bằng tay:
1. Bấm tổ hợp phím **`Windows + I`** để mở **Settings** $\rightarrow$ Chọn **Apps** (Ứng dụng) $\rightarrow$ **Installed apps** (Ứng dụng đã cài đặt).
2. Nhập vào ô tìm kiếm: **`VirtualBox`** hoặc **`Oracle VM VirtualBox`**.
3. Bấm vào dấu ba chấm `...` bên cạnh $\rightarrow$ Chọn **Uninstall** (Gỡ cài đặt).
4. Xác nhận và làm theo hướng dẫn trên màn hình cho đến khi hoàn tất.
5. Khởi động lại máy tính (Restart) để giải phóng toàn bộ driver mạng cũ.

---

## 5. KIỂM TRA XÁC NHẬN HỆ THỐNG SAU KHI GỠ BỎ

Mở PowerShell kiểm tra:
```powershell
# 1. Xác nhận VirtualBox đã biến mất hoàn toàn:
Get-Command VBoxManage -ErrorAction SilentlyContinue
# Kết quả: Rỗng (Không còn tìm thấy)

# 2. Xác nhận VMware Workstation Pro đang hoạt động hoàn hảo độc tôn:
vmrun -T ws list
# Kết quả: "Total running VMs: 0"
```
