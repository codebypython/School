<#
.SYNOPSIS
    Kịch bản dọn dẹp và gỡ cài đặt hoàn toàn Oracle VirtualBox sau khi chuyển dịch sang VMware.
.DESCRIPTION
    1. Tắt toàn bộ tiến trình VirtualBox đang chạy ngầm.
    2. Gỡ bỏ sạch các card mạng ảo Host-Only (vboxnet) tránh xung đột mạng.
    3. Gỡ cài đặt ứng dụng Oracle VirtualBox qua Windows Installer / Winget.
    4. Dọn dẹp thư mục cấu hình rác trong thư mục người dùng.
#>

# Đảm bảo bảng mã UTF-8 cho console
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Kiểm tra quyền Administrator - Tự động kích hoạt RunAs nếu thiếu quyền
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "[!] Đang yêu cầu quyền Administrator để gỡ bỏ network driver của VirtualBox..." -ForegroundColor Yellow
    Start-Process powershell.exe -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "🧹 HỌC PHẦN AN TOÀN MẠNG DUT — QUY TRÌNH GỠ CÀI ĐẶT ORACLE VIRTUALBOX" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

# 1. Tắt các tiến trình VirtualBox
Write-Host "`n[*] Bước 1: Quét tìm và dừng các tiến trình VirtualBox đang chạy..." -ForegroundColor Yellow
$vboxProcesses = @("VirtualBox", "VBoxSVC", "VBoxHeadless", "VBoxManage")
foreach ($proc in $vboxProcesses) {
    $running = Get-Process -Name $proc -ErrorAction SilentlyContinue
    if ($running) {
        Write-Host "    - Đang tắt tiến trình: $proc (PID: $($running.Id -join ', '))" -ForegroundColor Gray
        Stop-Process -Name $proc -Force -ErrorAction SilentlyContinue
    }
}
Write-Host "    ✅ Đã dừng toàn bộ tiến trình VirtualBox!" -ForegroundColor Green

# 2. Xóa các card mạng ảo VirtualBox Host-Only
Write-Host "`n[*] Bước 2: Dọn dẹp các card mạng ảo Host-Only cũ..." -ForegroundColor Yellow
$vboxManageCmd = "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
if (Test-Path $vboxManageCmd) {
    try {
        $adapters = & $vboxManageCmd list hostonlyifs
        if ($adapters) {
            $adapterNames = $adapters | Where-Object { $_ -match "^Name:\s+(.+)$" } | ForEach-Object { $matches[1].Trim() }
            foreach ($name in $adapterNames) {
                Write-Host "    - Đang xóa card mạng: $name" -ForegroundColor Gray
                & $vboxManageCmd hostonlyif remove "$name" | Out-Null
            }
        }
    } catch {
        Write-Host "    (Không tìm thấy card mạng ảo nào cần xóa)" -ForegroundColor Gray
    }
}
Write-Host "    ✅ Đã dọn dẹp sạch card mạng ảo!" -ForegroundColor Green

# 3. Gỡ cài đặt VirtualBox
Write-Host "`n[*] Bước 3: Đang thực thi gỡ cài đặt Oracle VM VirtualBox..." -ForegroundColor Yellow
$uninstalled = $false

# Phương án A: Thử gỡ qua Winget
$wingetCheck = Get-Command winget -ErrorAction SilentlyContinue
if ($wingetCheck) {
    Write-Host "    - Thực thi qua Windows Package Manager (winget)..." -ForegroundColor Gray
    $res = Start-Process winget -ArgumentList "uninstall --id Oracle.VirtualBox --accept-source-agreements --silent" -Wait -PassThru -NoNewWindow
    if ($res.ExitCode -eq 0) {
        $uninstalled = $true
    }
}

# Phương án B: Nếu winget chưa xong, quét Registry tìm ProductCode MSI
if (-not $uninstalled) {
    Write-Host "    - Quét registry tìm mã gói MSI của VirtualBox..." -ForegroundColor Gray
    $regPaths = @(
        "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*",
        "HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*"
    )
    $vboxKey = Get-ItemProperty $regPaths -ErrorAction SilentlyContinue | Where-Object { $_.DisplayName -like "*VirtualBox*" } | Select-Object -First 1
    if ($vboxKey -and $vboxKey.UninstallString) {
        Write-Host "    - Phát hiện: $($vboxKey.DisplayName)" -ForegroundColor Gray
        if ($vboxKey.UninstallString -match "\{([A-Fa-f0-9\-]+)\}") {
            $guid = $matches[1]
            Write-Host "    - Đang gỡ bỏ bằng MSI: msiexec /x {$guid} /qn" -ForegroundColor Gray
            Start-Process msiexec.exe -ArgumentList "/x {$guid} /qn /norestart" -Wait -NoNewWindow
            $uninstalled = $true
        }
    }
}

# 4. Xóa file cấu hình rác
$vboxHome = "$env:USERPROFILE\.VirtualBox"
if (Test-Path $vboxHome) {
    Write-Host "`n[*] Bước 4: Xóa thư mục cấu hình rác tại $vboxHome..." -ForegroundColor Yellow
    Remove-Item -Path $vboxHome -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "    ✅ Đã dọn dẹp thư mục cấu hình!" -ForegroundColor Green
}

Write-Host "`n======================================================================" -ForegroundColor Cyan
Write-Host "🎉 HOÀN TẤT DỌN DẸP VIRTUALBOX! HỆ THỐNG ĐÃ SẴN SÀNG 100% CHO VMWARE." -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Cyan
