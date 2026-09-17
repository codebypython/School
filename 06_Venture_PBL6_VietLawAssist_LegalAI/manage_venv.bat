@echo off
REM ==============================================================================
REM VietLawAssist — Trình Quản Lý Môi Trường Ảo (.venv Manager cho CMD)
REM ==============================================================================

set VENV_PYTHON="%~dp0.venv\Scripts\python.exe"
set CHECK_SCRIPT="%~dp0Project\scripts\check_env.py"
set REQUIREMENTS="%~dp0Project\requirements.txt"

if not exist %VENV_PYTHON% (
    echo [!] Khong tim thay .venv tai: %VENV_PYTHON%
    echo [*] Vui long tao moi truong ao bang Python 3.11: py -3.11 -m venv Project\.venv
    exit /b 1
)

if "%1"=="" goto check
if "%1"=="check" goto check
if "%1"=="activate" goto activate
if "%1"=="install" goto install
if "%1"=="test" goto test
if "%1"=="run-server" goto run_server
if "%1"=="help" goto help

:check
%VENV_PYTHON% %CHECK_SCRIPT%
goto end

:activate
echo [*] De kich hoat moi truong ao trong CMD, chay lenh:
echo     call .venv\Scripts\activate.bat
goto end

:install
echo [*] Dang cap nhat pip va cai dat dependencies...
%VENV_PYTHON% -m pip install --upgrade pip
%VENV_PYTHON% -m pip install -r %REQUIREMENTS%
goto end

:test
echo [*] Dang chay kiem thu tu dong voi pytest...
cd /d "%~dp0Project"
%VENV_PYTHON% -m pytest
goto end

:run_server
echo [*] Dang khoi chay FastAPI Server (http://127.0.0.1:8000)...
cd /d "%~dp0Project"
%VENV_PYTHON% -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
goto end

:help
echo Cach su dung: manage_venv.bat [command]
echo Commands:
echo   check       Kiem tra Python va trang thai cac thu vien (Mac dinh)
echo   activate    Huong dan lenh kich hoat venv
echo   install     Cai dat/Cap nhat thu vien tu requirements.txt
echo   run-server  Khoi chay FastAPI Uvicorn Server
echo   test        Chay kiem thu pytest
goto end

:end
