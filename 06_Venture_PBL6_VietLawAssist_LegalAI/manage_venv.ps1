# ==============================================================================
# VietLawAssist — Trình Quản Lý Môi Trường Ảo (.venv Manager)
# Dự án: PBL6 Machine Learning Training Model Project
# ==============================================================================

param (
    [Parameter(Position = 0)]
    [ValidateSet("check", "activate", "install", "run-server", "test", "help")]
    [string]$Command = "check"
)

$VenvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
$VenvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
$RequirementsFile = Join-Path $PSScriptRoot "Project\requirements.txt"
$CheckScript = Join-Path $PSScriptRoot "Project\scripts\check_env.py"

if (-not (Test-Path $VenvPython)) {
    Write-Host "[!] Không tìm thấy .venv tại: $VenvPython" -ForegroundColor Red
    Write-Host "[*] Vui lòng chạy lệnh tạo venv: py -3.11 -m venv Project\.venv" -ForegroundColor Yellow
    exit 1
}

switch ($Command) {
    "check" {
        & $VenvPython $CheckScript
    }

    "activate" {
        Write-Host "[*] Để kích hoạt môi trường ảo trong PowerShell hiện tại, hãy chạy:" -ForegroundColor Cyan
        Write-Host "    .\.venv\Scripts\Activate.ps1" -ForegroundColor Green
        Write-Host "[*] Nếu gặp lỗi script execution, chạy trước:" -ForegroundColor Cyan
        Write-Host "    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Yellow
    }

    "install" {
        Write-Host "[*] Cập nhật pip và cài đặt toàn bộ thư viện từ requirements.txt..." -ForegroundColor Cyan
        & $VenvPython -m pip install --upgrade pip
        & $VenvPython -m pip install -r $RequirementsFile
    }

    "test" {
        Write-Host "[*] Khởi chạy kiểm thử tự động với PyTest..." -ForegroundColor Cyan
        Set-Location (Join-Path $PSScriptRoot "Project")
        & $VenvPython -m pytest
    }

    "run-server" {
        Write-Host "[*] Khởi chạy FastAPI Backend Server..." -ForegroundColor Cyan
        Set-Location (Join-Path $PSScriptRoot "Project")
        & $VenvPython -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
    }

    "help" {
        Write-Host "Cách sử dụng: .\manage_venv.ps1 [command]" -ForegroundColor Cyan
        Write-Host "Danh sách lệnh:"
        Write-Host "  .\manage_venv.ps1 check       Kiểm tra trạng thái Python và 21 thư viện cốt lõi"
        Write-Host "  .\manage_venv.ps1 activate    Hiển thị hướng dẫn kích hoạt venv"
        Write-Host "  .\manage_venv.ps1 install     Cài đặt / Cập nhật thư viện từ requirements.txt"
        Write-Host "  .\manage_venv.ps1 run-server  Khởi chạy FastAPI server (http://127.0.0.1:8000)"
        Write-Host "  .\manage_venv.ps1 test        Chạy bộ kiểm thử tự động với pytest"
    }
}
