#!/usr/bin/env python3
"""
🤖 HỌC PHẦN: AN TOÀN MẠNG & MẬT MÃ HỌC ỨNG DỤNG (CORP-04-SEC)
Công cụ: VMware Workstation Automated Lab Controller
Tác giả: DUT Cyber Security Mentor

Chức năng:
- Tự động phát hiện đường dẫn cài đặt vmrun.exe trên Windows.
- Khởi động, dừng, kiểm tra danh sách máy ảo chạy ngầm (Headless/NoGUI).
- Can thiệp chỉnh sửa trực tiếp file .vmx (đổi card mạng VMnet, tăng RAM, đổi CPU).
- Tạo và phục hồi snapshot trong vài giây.
"""

import sys
import io
import os
import re
import shutil
import subprocess
import argparse
from typing import Optional, List, Dict

# Đảm bảo in UTF-8 mượt mà trên môi trường Windows console
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DEFAULT_VMRUN_PATHS = [
    r"C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe",
    r"C:\Program Files\VMware\VMware Workstation\vmrun.exe",
    r"C:\Program Files (x86)\VMware\VMware Player\vmrun.exe",
]


def find_vmrun() -> Optional[str]:
    """Tìm đường dẫn tệp thực thi vmrun.exe trên hệ thống."""
    # Kiểm tra biến môi trường PATH
    path_in_env = shutil.which("vmrun")
    if path_in_env:
        return path_in_env
    # Kiểm tra các đường dẫn mặc định
    for path in DEFAULT_VMRUN_PATHS:
        if os.path.isfile(path):
            return path
    return None


def run_vmrun_cmd(args: List[str]) -> TupleBool:
    """Thực thi một lệnh vmrun với các tham số tương ứng."""
    vmrun_bin = find_vmrun()
    if not vmrun_bin:
        print("⚠️ CẢNH BÁO: Không tìm thấy 'vmrun.exe' trên máy tính.")
        print("   Vui lòng đảm bảo đã cài đặt VMware Workstation Pro.")
        return False
    
    full_cmd = [vmrun_bin, "-T", "ws"] + args
    print(f"[*] Thực thi: {' '.join(full_cmd)}")
    try:
        res = subprocess.run(full_cmd, capture_output=True, text=True, check=False)
        if res.stdout:
            print(res.stdout.strip())
        if res.stderr:
            print(f"Lỗi: {res.stderr.strip()}", file=sys.stderr)
        return res.returncode == 0
    except Exception as e:
        print(f"❌ Lỗi ngoại lệ: {e}", file=sys.stderr)
        return False


def parse_vmx(vmx_path: str) -> Dict[str, str]:
    """Đọc và phân tích cú pháp tệp .vmx thành từ điển Key-Value."""
    if not os.path.isfile(vmx_path):
        raise FileNotFoundError(f"Không tìm thấy file: {vmx_path}")
    
    data = {}
    with open(vmx_path, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            match = re.match(r'^([a-zA-Z0-9_\.]+)\s*=\s*"(.*)"$', line)
            if match:
                data[match.group(1)] = match.group(2)
    return data


def write_vmx(vmx_path: str, data: Dict[str, str]) -> None:
    """Ghi dữ liệu cấu hình đã cập nhật vào tệp .vmx (tự động tạo bản sao lưu .bak)."""
    bak_path = vmx_path + ".bak"
    shutil.copy2(vmx_path, bak_path)
    print(f"[*] Đã tạo bản sao lưu an toàn: '{os.path.basename(bak_path)}'")
    
    with open(vmx_path, 'w', encoding='utf-8') as f:
        for k, v in sorted(data.items()):
            f.write(f'{k} = "{v}"\n')
    print(f"✅ Đã cập nhật thành công cấu hình: '{os.path.basename(vmx_path)}'")


def cmd_info(vmx_path: str) -> None:
    """Hiển thị thông tin tóm tắt cấu hình máy ảo."""
    cfg = parse_vmx(vmx_path)
    print("=" * 60)
    print(f"🖥️ THÔNG TIN MÁY ẢO VMWARE: {os.path.basename(vmx_path)}")
    print("=" * 60)
    print(f"  Tên hiển thị (DisplayName): {cfg.get('displayName', 'N/A')}")
    print(f"  Hệ điều hành khách (GuestOS): {cfg.get('guestOS', 'N/A')}")
    print(f"  Dung lượng RAM (Memory):     {cfg.get('memsize', 'N/A')} MB")
    print(f"  Số nhân CPU (vCPUs):         {cfg.get('numvcpus', '1')}")
    
    # Tìm kiếm các card mạng
    adapters = [k for k in cfg.keys() if k.startswith('ethernet') and k.endswith('.present')]
    print(f"  Danh sách Card Mạng ({len(adapters)} card):")
    for ad in adapters:
        prefix = ad.split('.')[0]
        conn_type = cfg.get(f"{prefix}.connectionType", "bridged")
        vnet = cfg.get(f"{prefix}.vnet", "N/A")
        print(f"    - {prefix}: Kiểu kết nối = '{conn_type}' | Mạng gán = '{vnet}'")
    print("=" * 60)


def cmd_set_vmnet(vmx_path: str, vmnet_name: str, adapter_index: int = 0) -> None:
    """Chuyển đổi card mạng máy ảo sang mạng VMnet mong muốn."""
    cfg = parse_vmx(vmx_path)
    prefix = f"ethernet{adapter_index}"
    cfg[f"{prefix}.present"] = "TRUE"
    cfg[f"{prefix}.connectionType"] = "custom"
    cfg[f"{prefix}.vnet"] = vmnet_name
    write_vmx(vmx_path, cfg)
    print(f"⭐ Card mạng '{prefix}' đã được chuyển thành công sang '{vmnet_name}'!")


def cmd_set_ram(vmx_path: str, mem_mb: int) -> None:
    """Thay đổi dung lượng RAM máy ảo."""
    cfg = parse_vmx(vmx_path)
    cfg["memsize"] = str(mem_mb)
    write_vmx(vmx_path, cfg)
    print(f"⭐ RAM đã được cập nhật thành: {mem_mb} MB!")


def main():
    parser = argparse.ArgumentParser(
        description="VMware Workstation Automated Lab Controller — DUT CORP-04-SEC"
    )
    subparsers = parser.add_subparsers(dest="action", help="Lệnh hành động")

    # Lệnh: list
    subparsers.add_parser("list", help="Liệt kê các máy ảo đang chạy")

    # Lệnh: info
    parser_info = subparsers.add_parser("info", help="Xem chi tiết thông số file .vmx")
    parser_info.add_argument("vmx", help="Đường dẫn tới file .vmx")

    # Lệnh: set-vmnet
    parser_vmnet = subparsers.add_parser("set-vmnet", help="Gán card mạng ảo VMnet")
    parser_vmnet.add_argument("vmx", help="Đường dẫn tới file .vmx")
    parser_vmnet.add_argument("net", help="Tên mạng ảo (ví dụ: VMnet1, VMnet2, VMnet3)")
    parser_vmnet.add_argument("--adapter", type=int, default=0, help="Chỉ số card mạng (mặc định: 0)")

    # Lệnh: set-ram
    parser_ram = subparsers.add_parser("set-ram", help="Chỉnh sửa dung lượng RAM")
    parser_ram.add_argument("vmx", help="Đường dẫn tới file .vmx")
    parser_ram.add_argument("mb", type=int, help="Dung lượng RAM tính bằng MB (ví dụ: 1024)")

    # Lệnh: start
    parser_start = subparsers.add_parser("start", help="Khởi động máy ảo")
    parser_start.add_argument("vmx", help="Đường dẫn tới file .vmx")
    parser_start.add_argument("--gui", action="store_true", help="Hiển thị cửa sổ giao diện GUI")

    # Lệnh: stop
    parser_stop = subparsers.add_parser("stop", help="Tắt máy ảo an toàn")
    parser_stop.add_argument("vmx", help="Đường dẫn tới file .vmx")

    # Lệnh: snapshot
    parser_snap = subparsers.add_parser("snapshot", help="Tạo snapshot khôi phục")
    parser_snap.add_argument("vmx", help="Đường dẫn tới file .vmx")
    parser_snap.add_argument("name", help="Tên snapshot")

    # Lệnh: revert
    parser_rev = subparsers.add_parser("revert", help="Phục hồi về snapshot cũ")
    parser_rev.add_argument("vmx", help="Đường dẫn tới file .vmx")
    parser_rev.add_argument("name", help="Tên snapshot")

    args = parser.parse_args()

    if not args.action:
        parser.print_help()
        sys.exit(0)

    if args.action == "list":
        run_vmrun_cmd(["list"])
    elif args.action == "info":
        cmd_info(args.vmx)
    elif args.action == "set-vmnet":
        cmd_set_vmnet(args.vmx, args.net, args.adapter)
    elif args.action == "set-ram":
        cmd_set_ram(args.vmx, args.mb)
    elif args.action == "start":
        mode = "gui" if args.gui else "nogui"
        run_vmrun_cmd(["start", args.vmx, mode])
    elif args.action == "stop":
        run_vmrun_cmd(["stop", args.vmx, "soft"])
    elif args.action == "snapshot":
        run_vmrun_cmd(["snapshot", args.vmx, args.name])
    elif args.action == "revert":
        run_vmrun_cmd(["revertToSnapshot", args.vmx, args.name])


if __name__ == "__main__":
    main()
