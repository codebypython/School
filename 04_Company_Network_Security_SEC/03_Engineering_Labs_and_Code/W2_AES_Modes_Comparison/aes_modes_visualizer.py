#!/usr/bin/env python3
"""
🔐 HỌC PHẦN: AN TOÀN MẠNG & MẬT MÃ HỌC ỨNG DỤNG (CORP-04-SEC)
Tuần 2: Chuẩn Mã Hóa Tiên Tiến AES & Nguy Cơ Rò Rỉ Dữ Liệu Của Chế Độ ECB
Công cụ: Pure Python AES-128 Engine & BMP Image Mode Visualizer
Tác giả: DUT Cyber Security Mentor

Đặc tính:
- Chạy 100% độc lập, không phụ thuộc bất kỳ thư viện bên thứ ba nào (Zero external dependency).
- Cài đặt đầy đủ 4 phép biến đổi của AES: SubBytes, ShiftRows, MixColumns, AddRoundKey.
- Tạo tệp ảnh BMP mẫu và mã hóa minh họa trực quan lỗ hổng rò rỉ mẫu dữ liệu (Pattern Leakage).
"""

import sys
import io
import os
import struct
import secrets
from typing import List

# Đảm bảo in UTF-8 mượt mà trên môi trường Windows console
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ==============================================================================
# PHẦN 1: HỆ THỐNG TOÁN HỌC AES-128 TỪ GỐC (RIJNDAEL S-BOX & GALOIS FIELD GF(2^8))
# ==============================================================================

S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

RCON = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


def xtime(a: int) -> int:
    """Nhân với x trong trường hữu hạn Galois GF(2^8) với đa thức tối giản m(x) = x^8 + x^4 + x^3 + x + 1."""
    return ((a << 1) ^ 0x1B) & 0xFF if (a & 0x80) else (a << 1) & 0xFF


class PureAES128:
    """Cài đặt thuật toán mã hóa khối chuẩn AES-128 theo đặc tả NIST FIPS PUB 197."""
    
    def __init__(self, key: bytes):
        if len(key) != 16:
            raise ValueError("AES-128 yêu cầu độ dài khóa chính xác là 16 bytes (128 bits).")
        self.round_keys = self._key_expansion(key)

    def _key_expansion(self, key: bytes) -> List[List[List[int]]]:
        """Thuật toán sinh 11 khóa vòng con (Round Keys) từ khóa chính."""
        w = [list(key[4*i : 4*(i+1)]) for i in range(4)]
        for i in range(4, 44):
            temp = list(w[i - 1])
            if i % 4 == 0:
                # RotWord
                temp = temp[1:] + temp[:1]
                # SubWord
                temp = [S_BOX[b] for b in temp]
                # XOR với Rcon
                temp[0] ^= RCON[i // 4]
            w.append([w[i - 4][j] ^ temp[j] for j in range(4)])
        
        round_keys = []
        for r in range(11):
            matrix = [[w[4 * r + c][row] for c in range(4)] for row in range(4)]
            round_keys.append(matrix)
        return round_keys

    def _sub_bytes(self, state: List[List[int]]) -> None:
        """Phép biến đổi phi tuyến SubBytes tra cứu qua S-Box."""
        for r in range(4):
            for c in range(4):
                state[r][c] = S_BOX[state[r][c]]

    def _shift_rows(self, state: List[List[int]]) -> None:
        """Phép biến đổi dịch vòng các hàng: Hàng 0 giữ nguyên, Hàng 1 dịch 1, Hàng 2 dịch 2, Hàng 3 dịch 3."""
        state[1] = state[1][1:] + state[1][:1]
        state[2] = state[2][2:] + state[2][:2]
        state[3] = state[3][3:] + state[3][:3]

    def _mix_columns(self, state: List[List[int]]) -> None:
        """Phép nhân ma trận trong trường hữu hạn Galois GF(2^8)."""
        for c in range(4):
            s0, s1, s2, s3 = state[0][c], state[1][c], state[2][c], state[3][c]
            state[0][c] = xtime(s0) ^ (xtime(s1) ^ s1) ^ s2 ^ s3
            state[1][c] = s0 ^ xtime(s1) ^ (xtime(s2) ^ s2) ^ s3
            state[2][c] = s0 ^ s1 ^ xtime(s2) ^ (xtime(s3) ^ s3)
            state[3][c] = (xtime(s0) ^ s0) ^ s1 ^ s2 ^ xtime(s3)

    def _add_round_key(self, state: List[List[int]], round_key: List[List[int]]) -> None:
        """Phép toán XOR giữa State và Round Key."""
        for r in range(4):
            for c in range(4):
                state[r][c] ^= round_key[r][c]

    def encrypt_block(self, block: bytes) -> bytes:
        """Mã hóa một khối 16 bytes qua 10 vòng (Rounds)."""
        if len(block) != 16:
            raise ValueError("Khối đầu vào phải đúng 16 bytes.")
        
        # Nạp dữ liệu vào ma trận trạng thái State 4x4 (theo thứ tự cột trước)
        state = [[block[r + 4 * c] for c in range(4)] for r in range(4)]
        
        # Vòng khởi tạo (Round 0)
        self._add_round_key(state, self.round_keys[0])
        
        # 9 vòng biến đổi tiêu chuẩn (Round 1 -> 9)
        for r in range(1, 10):
            self._sub_bytes(state)
            self._shift_rows(state)
            self._mix_columns(state)
            self._add_round_key(state, self.round_keys[r])
            
        # Vòng cuối cùng (Round 10: Bỏ qua MixColumns)
        self._sub_bytes(state)
        self._shift_rows(state)
        self._add_round_key(state, self.round_keys[10])
        
        # Xuất State ra dạng bytes
        output = bytearray(16)
        for c in range(4):
            for r in range(4):
                output[r + 4 * c] = state[r][c]
        return bytes(output)


# ==============================================================================
# PHẦN 2: CÁC CHẾ ĐỘ MÃ KHỐI (CIPHER MODES: ECB VS CBC)
# ==============================================================================

def encrypt_ecb(cipher: PureAES128, data: bytes) -> bytes:
    """Mã hóa Electronic Codebook (ECB): Các khối mã hóa độc lập hoàn toàn."""
    # Padding PKCS#7
    pad_len = 16 - (len(data) % 16)
    padded_data = data + bytes([pad_len] * pad_len)
    
    result = bytearray()
    for i in range(0, len(padded_data), 16):
        block = padded_data[i : i + 16]
        result.extend(cipher.encrypt_block(block))
    return bytes(result)


def encrypt_cbc(cipher: PureAES128, data: bytes, iv: bytes) -> bytes:
    """Mã hóa Cipher Block Chaining (CBC): Khối sau XOR với bản mã khối trước."""
    if len(iv) != 16:
        raise ValueError("IV phải đúng 16 bytes.")
    
    pad_len = 16 - (len(data) % 16)
    padded_data = data + bytes([pad_len] * pad_len)
    
    result = bytearray()
    prev_cipher_block = iv
    for i in range(0, len(padded_data), 16):
        block = padded_data[i : i + 16]
        # XOR với khối ciphertext trước đó (hoặc IV)
        xored_block = bytes(b ^ p for b, p in zip(block, prev_cipher_block))
        encrypted_block = cipher.encrypt_block(xored_block)
        result.extend(encrypted_block)
        prev_cipher_block = encrypted_block
    return bytes(result)


# ==============================================================================
# PHẦN 3: TẠO ẢNH BMP MẪU & MÃ HÓA MINH HỌA LỖ HỔNG
# ==============================================================================

def create_sample_bmp(width: int = 128, height: int = 128) -> bytes:
    """Tạo một file ảnh BMP 24-bit màu chuẩn có hình khối họa tiết DUT ở trung tâm."""
    row_bytes = width * 3
    padding_bytes = (4 - (row_bytes % 4)) % 4
    image_size = (row_bytes + padding_bytes) * height
    file_size = 54 + image_size
    
    # BMP Header 14 bytes
    bmp_header = struct.pack('<2sIHHI', b'BM', file_size, 0, 0, 54)
    # DIB Header 40 bytes (BITMAPINFOHEADER)
    dib_header = struct.pack('<IIIHHIIIIII', 40, width, height, 1, 24, 0, image_size, 2835, 2835, 0, 0)
    
    pixel_data = bytearray()
    for y in range(height):
        row = bytearray()
        for x in range(width):
            # Tạo nền đen, ở giữa vẽ hình vuông đỏ và chữ thập xanh ngọc
            dist_center = max(abs(x - width//2), abs(y - height//2))
            if dist_center < width // 4:
                # Vùng trung tâm: Màu đỏ rực
                row.extend(b'\x00\x00\xFF')  # B, G, R
            elif abs(x - width//2) < 4 or abs(y - height//2) < 4:
                # Đường chữ thập: Màu vàng
                row.extend(b'\x00\xFF\xFF')
            else:
                # Nền màu đen tuyền
                row.extend(b'\x00\x00\x00')
        row.extend(b'\x00' * padding_bytes)
        pixel_data.extend(row)
        
    return bmp_header + dib_header + bytes(pixel_data)


def main():
    print("=" * 70)
    print("🛡️ DUT CYBERDEFENSE CORP — AES-128 CIPHER MODES VISUALIZER")
    print("=" * 70)
    
    output_dir = os.path.dirname(os.path.abspath(__file__))
    orig_path = os.path.join(output_dir, "sample_original.bmp")
    ecb_path = os.path.join(output_dir, "sample_ecb_encrypted.bmp")
    cbc_path = os.path.join(output_dir, "sample_cbc_encrypted.bmp")
    
    # 1. Tạo ảnh gốc
    print("\n[1] Đang sinh file ảnh BMP kiểm nghiệm 128x128 pixels...")
    bmp_data = create_sample_bmp(128, 128)
    header = bmp_data[:54]
    pixels = bmp_data[54:]
    with open(orig_path, "wb") as f:
        f.write(bmp_data)
    print(f"    ✅ Đã tạo ảnh gốc: '{os.path.basename(orig_path)}' ({len(bmp_data)} bytes)")
    
    # 2. Khởi tạo khóa bí mật AES
    key = b"DUT_SEC_KEY_2026"
    iv = secrets.token_bytes(16)
    aes = PureAES128(key)
    print(f"[*] Khóa bí mật (16 bytes): {key.decode()}")
    print(f"[*] Vector khởi tạo IV (CBC mode): {iv.hex()[:16]}...")
    
    # 3. Mã hóa với chế độ ECB
    print("\n[2] Đang mã hóa dữ liệu điểm ảnh bằng chế độ AES-128-ECB...")
    ecb_encrypted_pixels = encrypt_ecb(aes, pixels)
    # Giữ nguyên BMP Header, chỉ ghi đè pixel ciphertext (cắt đúng chiều dài gốc để BMP hợp lệ)
    ecb_bmp = header + ecb_encrypted_pixels[:len(pixels)]
    with open(ecb_path, "wb") as f:
        f.write(ecb_bmp)
    print(f"    ⚠️ Đã tạo ảnh ECB: '{os.path.basename(ecb_path)}'")
    print("       (KẾT QUẢ: Họa tiết hình học vẫn lộ rõ mồn một do các khối pixel đen lặp lại!)")
    
    # 4. Mã hóa với chế độ CBC
    print("\n[3] Đang mã hóa dữ liệu điểm ảnh bằng chế độ AES-128-CBC...")
    cbc_encrypted_pixels = encrypt_cbc(aes, pixels, iv)
    cbc_bmp = header + cbc_encrypted_pixels[:len(pixels)]
    with open(cbc_path, "wb") as f:
        f.write(cbc_bmp)
    print(f"    🛡️ Đã tạo ảnh CBC: '{os.path.basename(cbc_path)}'")
    print("       (KẾT QUẢ: Ảnh biến thành nhiễu trắng ngẫu nhiên hoàn toàn, tính khuếch tán cực đại!)")
    
    print("\n" + "=" * 70)
    print("📌 KẾT LUẬN SƯ PHẠM BẮT BUỘC:")
    print("1. Chế độ ECB mã hóa từng khối 16 bytes độc lập mà không dùng IV.")
    print("   -> Hai khối dữ liệu giống hệt nhau luôn cho ra Ciphertext giống hệt nhau.")
    print("   -> Lỗ hổng: Rò rỉ mẫu dữ liệu cấu trúc (Data Pattern Leakage) - CẤM DÙNG TRONG THỰC TẾ!")
    print("2. Chế độ CBC kết hợp XOR với khối trước và sử dụng IV ngẫu nhiên.")
    print("   -> Đạt tính chất khuếch tán (Diffusion) và hỗn loạn (Confusion) theo chuẩn Shannon.")
    print("=" * 70)


if __name__ == "__main__":
    main()
