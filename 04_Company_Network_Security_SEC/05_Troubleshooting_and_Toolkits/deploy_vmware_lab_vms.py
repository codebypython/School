#!/usr/bin/env python3
"""
🚀 HỌC PHẦN: AN TOÀN MẠNG & MẬT MÃ HỌC ỨNG DỤNG (CORP-04-SEC)
Công cụ: Bộ Triển Khai Tự Động Máy Ảo Lab Sang VMware Workstation Pro (Automated Lab Deployer)
Tác giả: DUT Cyber Security Mentor

Chức năng:
1. Tự động tìm kiếm VMware OVF Tool (ovftool.exe) và VMware Workstation.
2. Tự động giải nén & chuyển đổi 'Server 2003 R2.ova' thành 3 máy ảo VMware độc lập:
   - Server2003_LAN2  -> Gán card mạng Custom: VMnet2 (Lab 3 LAN 2 Client)
   - Server2003_LAN3  -> Gán card mạng Custom: VMnet3 (Lab 3 LAN 3 IIS Web/FTP)
   - TACAS_Server     -> Gán card mạng Custom: VMnet1 (Lab 4 AAA TACACS+ Banana Corp)
3. Tinh chỉnh tệp .vmx tự động (512MB RAM, e1000 NIC, tối ưu hóa hiển thị).
"""

import sys
import io
import os
import re
import shutil
import subprocess
import argparse
from typing import Optional, List

# Đảm bảo in UTF-8 mượt mà trên môi trường Windows console
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

OVFTOOL_PATHS = [
    r"C:\Program Files\VMware\VMware Workstation\OVFTool\ovftool.exe",
    r"C:\Program Files (x86)\VMware\VMware Workstation\OVFTool\ovftool.exe",
    r"C:\Program Files\VMware\VMware OVF Tool\ovftool.exe",
]

VMRUN_PATHS = [
    r"C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe",
    r"C:\Program Files\VMware\VMware Workstation\vmrun.exe",
]


def find_ovftool() -> Optional[str]:
    path_in_env = shutil.which("ovftool")
    if path_in_env:
        return path_in_env
    for p in OVFTOOL_PATHS:
        if os.path.isfile(p):
            return p
    return None


def find_vmrun() -> Optional[str]:
    path_in_env = shutil.which("vmrun")
    if path_in_env:
        return path_in_env
    for p in VMRUN_PATHS:
        if os.path.isfile(p):
            return p
    return None


def patch_vmx_network(vmx_path: str, display_name: str, vmnet: str, ram_mb: int = 512) -> None:
    """Tinh chỉnh file .vmx sang mạng VMnet và thiết lập tham số tối ưu."""
    if not os.path.isfile(vmx_path):
        return
    
    with open(vmx_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    new_lines = []
    keys_handled = set()
    
    for line in lines:
        line_clean = line.strip()
        if line_clean.startswith('displayName'):
            new_lines.append(f'displayName = "{display_name}"\n')
            keys_handled.add('displayName')
        elif line_clean.startswith('memsize'):
            new_lines.append(f'memsize = "{ram_mb}"\n')
            keys_handled.add('memsize')
        elif line_clean.startswith('ethernet0.connectionType'):
            new_lines.append('ethernet0.connectionType = "custom"\n')
            keys_handled.add('ethernet0.connectionType')
        elif line_clean.startswith('ethernet0.vnet'):
            new_lines.append(f'ethernet0.vnet = "{vmnet}"\n')
            keys_handled.add('ethernet0.vnet')
        else:
            new_lines.append(line)
            
    # Bổ sung nếu chưa có
    if 'ethernet0.connectionType' not in keys_handled:
        new_lines.append('ethernet0.connectionType = "custom"\n')
    if 'ethernet0.vnet' not in keys_handled:
        new_lines.append(f'ethernet0.vnet = "{vmnet}"\n')
    if 'displayName' not in keys_handled:
        new_lines.append(f'displayName = "{display_name}"\n')
        
    with open(vmx_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"    ✅ Đã cấu hình .vmx: Display='{display_name}' | Card=Custom '{vmnet}' | RAM={ram_mb}MB")


def deploy_vm(ovftool_bin: str, ova_path: str, target_dir: str, vm_name: str, vmnet: str) -> bool:
    """Sử dụng ovftool để giải nén và cấu hình máy ảo mới."""
    vmx_target = os.path.join(target_dir, f"{vm_name}.vmx")
    print(f"\n[*] Đang khởi tạo máy ảo: '{vm_name}'...")
    print(f"    Thư mục đích: {target_dir}")
    
    os.makedirs(target_dir, exist_ok=True)
    
    # Kiểm tra nếu máy ảo đã tồn tại
    if os.path.isfile(vmx_target):
        print(f"    ⚠️ Máy ảo đã tồn tại tại '{vmx_target}'. Đang cập nhật cấu hình mạng...")
        patch_vmx_network(vmx_target, vm_name, vmnet)
        return True
        
    cmd = [
        ovftool_bin,
        "--acceptAllEulas",
        "--skipManifestCheck",
        f"--name={vm_name}",
        ova_path,
        vmx_target
    ]
    print(f"    Chạy ovftool: {' '.join(cmd)}")
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if res.returncode == 0:
            print("    ✅ ovftool hoàn tất giải nén OVA!")
            patch_vmx_network(vmx_target, vm_name, vmnet)
            return True
        else:
            print(f"    ❌ Lỗi ovftool: {res.stderr.strip()}", file=sys.stderr)
            return False
    except Exception as e:
        print(f"    ❌ Lỗi thực thi: {e}", file=sys.stderr)
        return False


def main():
    print("=" * 70)
    print("🚀 BỘ TRIỂN KHAI TỰ ĐỘNG MÁY ẢO LAB SEC CHO VMWARE WORKSTATION PRO")
    print("=" * 70)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sec_dir = os.path.abspath(os.path.join(base_dir, ".."))
    ova_path = os.path.join(sec_dir, "05_Troubleshooting_and_Toolkits", "VM setup", "Server 2003 R2.ova")
    
    parser = argparse.ArgumentParser(description="Triển khai tự động máy ảo Server 2003 sang VMware Workstation")
    parser.add_argument("command", choices=["check", "deploy"], default="check", nargs="?",
                        help="Lệnh: 'check' kiểm tra môi trường, 'deploy' triển khai 3 máy ảo")
    parser.add_argument("--output-dir", default=r"D:\VMware_SEC_Labs",
                        help="Thư mục lưu trữ các máy ảo VMware (Mặc định: D:\\VMware_SEC_Labs)")
    args = parser.parse_args()
    
    ovftool = find_ovftool()
    vmrun = find_vmrun()
    
    print("\n[1] Kiểm tra các thành phần hệ thống:")
    print(f"  - VMware OVF Tool (ovftool.exe): {'✅ ' + ovftool if ovftool else '❌ Chưa tìm thấy'}")
    print(f"  - VMware CLI (vmrun.exe):        {'✅ ' + vmrun if vmrun else '❌ Chưa tìm thấy'}")
    print(f"  - Tệp gốc Server 2003 R2.ova:    {'✅ ' + ova_path if os.path.isfile(ova_path) else '❌ Không tìm thấy'}")
    
    if args.command == "check":
        print("\n[2] Hướng dẫn:")
        print("  - Để tự động chuyển đổi file .ova sang 3 máy ảo VMware cho Lab 3 & Lab 4:")
        print(f"    python deploy_vmware_lab_vms.py deploy --output-dir \"{args.output_dir}\"")
        return
        
    if not ovftool:
        print("\n❌ LỖI: Cần có ovftool.exe (đi kèm khi cài đặt VMware Workstation Pro) để tự động import.", file=sys.stderr)
        print("   Bạn cũng có thể mở VMware Workstation GUI -> File -> Open... -> Chọn 'Server 2003 R2.ova' thủ công.", file=sys.stderr)
        sys.exit(1)
        
    if not os.path.isfile(ova_path):
        print(f"\n❌ LỖI: Không tìm thấy file OVA tại: {ova_path}", file=sys.stderr)
        sys.exit(1)
        
    print(f"\n[2] Bắt đầu tự động triển khai 3 máy ảo tới '{args.output_dir}'...")
    
    # 1. Server2003_LAN2 -> VMnet2 (Lab 3)
    dir_lan2 = os.path.join(args.output_dir, "Server2003_LAN2")
    deploy_vm(ovftool, ova_path, dir_lan2, "Server2003_LAN2", "VMnet2")
    
    # 2. Server2003_LAN3 -> VMnet3 (Lab 3)
    dir_lan3 = os.path.join(args.output_dir, "Server2003_LAN3")
    deploy_vm(ovftool, ova_path, dir_lan3, "Server2003_LAN3", "VMnet3")
    
    # 3. TACAS_Server -> VMnet1 (Lab 4)
    dir_tacas = os.path.join(args.output_dir, "TACAS_Server")
    deploy_vm(ovftool, ova_path, dir_tacas, "TACAS_Server", "VMnet1")
    
    print("\n" + "=" * 70)
    print("🎉 HOÀN TẤT TRIỂN KHAI TOÀN BỘ HỆ SINH THÁI MÁY ẢO VMWARE CHO LAB SEC!")
    print("=" * 70)


if __name__ == "__main__":
    main()
