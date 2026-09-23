#!/usr/bin/env python3
"""
🔐 HỌC PHẦN: AN TOÀN MẠNG & MẬT MÃ HỌC ỨNG DỤNG (CORP-04-SEC)
Tuần 3: Mật Mã Khóa Công Khai RSA & Chữ Ký Số Từ Scratch (Không Dùng Thư Viện Crypto)
Công cụ: Pure Python RSA Implementation (Miller-Rabin, Extended GCD, Square & Multiply)
Tác giả: DUT Cyber Security Mentor

Đặc tính:
- Cài đặt 100% từ nền tảng toán học lý thuyết số sơ cấp.
- Sinh số nguyên tố lớn ngẫu nhiên bằng phép thử xác suất Miller-Rabin.
- Tìm nghịch đảo Modulo bằng giải thuật Euclid mở rộng.
- Mã hóa, giải mã và ký số, xác thực chữ ký số.
"""

import sys
import io
import hashlib
import secrets
from typing import Tuple

# Đảm bảo in UTF-8 mượt mà trên môi trường Windows console
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# ==============================================================================
# PHẦN 1: LÝ THUYẾT SỐ & KIỂM TRA SỐ NGUYÊN TỐ MILLER-RABIN
# ==============================================================================

def square_and_multiply(base: int, exponent: int, modulus: int) -> int:
    """
    Thuật toán Bình phương và Nhân liên tiếp (Square-and-Multiply)
    Tính (base^exponent) % modulus với độ phức tạp O(log(exponent)).
    """
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent & 1:  # Nếu bit cuối là 1
            result = (result * base) % modulus
        exponent >>= 1    # Dịch phải 1 bit (chia 2)
        base = (base * base) % modulus
    return result


def is_prime_miller_rabin(n: int, k: int = 25) -> bool:
    """
    Kiểm tra tính nguyên tố bằng thuật toán xác suất Miller-Rabin (k vòng thử).
    Xác suất sai số tối đa: (1/4)^k (với k=25, xác suất sai số < 10^-15).
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Phân tích n - 1 = (2^s) * d (với d là số lẻ)
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Thực hiện k vòng thử với các cơ số ngẫu nhiên 'a'
    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2  # a thuộc [2, n - 2]
        x = square_and_multiply(a, d, n)
        if x == 1 or x == n - 1:
            continue
        
        composite = True
        for _ in range(s - 1):
            x = square_and_multiply(x, 2, n)
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True


def generate_prime(bits: int) -> int:
    """Sinh một số nguyên tố ngẫu nhiên có độ dài chính xác 'bits' bits."""
    while True:
        # Đảm bảo bit đầu và bit cuối là 1 để đủ độ dài và là số lẻ
        candidate = (secrets.randbits(bits) | (1 << (bits - 1)) | 1)
        if is_prime_miller_rabin(candidate):
            return candidate


# ==============================================================================
# PHẦN 2: THUẬT TOÁN EUCLID MỞ RỘNG & NGHỊCH ĐẢO MODULO
# ==============================================================================

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Thuật toán Euclid mở rộng:
    Trả về (gcd, x, y) thỏa mãn đẳng thức Bézout: a*x + b*y = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(e: int, phi: int) -> int:
    """
    Tìm nghịch đảo Modulo: d = e^(-1) mod phi
    sao cho (e * d) = 1 (mod phi).
    """
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError(f"Không tồn tại nghịch đảo modulo vì gcd({e}, {phi}) != 1")
    return (x % phi + phi) % phi


# ==============================================================================
# PHẦN 3: KHUNG KHÓA RSA, MÃ HÓA, GIẢI MÃ & KÝ SỐ
# ==============================================================================

class RSACipher:
    """Hệ mật mã RSA thuần túy toán học."""

    def __init__(self, key_bits: int = 512):
        self.key_bits = key_bits
        self.p = 0
        self.q = 0
        self.n = 0
        self.phi = 0
        self.e = 65537  # Số mũ công khai chuẩn Fermat F4
        self.d = 0
        self._generate_keys()

    def _generate_keys(self) -> None:
        """Quy trình sinh khóa RSA chuẩn."""
        half_bits = self.key_bits // 2
        while True:
            self.p = generate_prime(half_bits)
            self.q = generate_prime(half_bits)
            if self.p != self.q:
                break
        
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        
        # Đảm bảo gcd(e, phi) == 1
        gcd, _, _ = extended_gcd(self.e, self.phi)
        if gcd != 1:
            return self._generate_keys()
        
        self.d = mod_inverse(self.e, self.phi)

    def get_public_key(self) -> Tuple[int, int]:
        """Khóa công khai: (e, n)."""
        return self.e, self.n

    def get_private_key(self) -> Tuple[int, int]:
        """Khóa bí mật: (d, n)."""
        return self.d, self.n

    def encrypt(self, message: bytes) -> int:
        """Mã hóa văn bản: C = M^e mod n."""
        m_int = int.from_bytes(message, byteorder='big')
        if m_int >= self.n:
            raise ValueError("Kích thước thông điệp vượt quá module n!")
        return square_and_multiply(m_int, self.e, self.n)

    def decrypt(self, ciphertext: int) -> bytes:
        """Giải mã bản mã: M = C^d mod n."""
        m_int = square_and_multiply(ciphertext, self.d, self.n)
        byte_len = (m_int.bit_length() + 7) // 8
        return m_int.to_bytes(byte_len, byteorder='big')

    def sign(self, message: bytes) -> int:
        """
        Ký số điện tử: S = H(M)^d mod n.
        Băm thông điệp bằng SHA-256 rồi mã hóa mã băm bằng Private Key.
        """
        digest = hashlib.sha256(message).digest()
        digest_int = int.from_bytes(digest, byteorder='big')
        return square_and_multiply(digest_int, self.d, self.n)

    @staticmethod
    def verify(message: bytes, signature: int, public_key: Tuple[int, int]) -> bool:
        """
        Xác thực chữ ký số: So sánh H(M) với S^e mod n.
        """
        e, n = public_key
        recovered_digest_int = square_and_multiply(signature, e, n)
        expected_digest = hashlib.sha256(message).digest()
        expected_digest_int = int.from_bytes(expected_digest, byteorder='big')
        return recovered_digest_int == expected_digest_int


def main():
    print("=" * 70)
    print("🛡️ DUT CYBERDEFENSE CORP — PURE RSA FROM SCRATCH ENGINE")
    print("=" * 70)
    
    print("\n[1] Đang sinh cặp số nguyên tố lớn 512-bit (Miller-Rabin 25 rounds)...")
    rsa = RSACipher(key_bits=512)
    e, n = rsa.get_public_key()
    d, _ = rsa.get_private_key()
    
    print(f"    ⭐ Số nguyên tố p ({rsa.p.bit_length()} bits): {str(rsa.p)[:20]}...")
    print(f"    ⭐ Số nguyên tố q ({rsa.q.bit_length()} bits): {str(rsa.q)[:20]}...")
    print(f"    🔑 Module n = p * q ({n.bit_length()} bits): {str(n)[:30]}...")
    print(f"    🔑 Số mũ công khai e: {e}")
    print(f"    🔐 Số mũ bí mật d = e^-1 mod phi(n): {str(d)[:30]}...")
    
    # 2. Thử nghiệm mã hóa & giải mã bảo mật
    secret_text = "DUT_CONFIDENTIAL_CYBER_REPORT_2026"
    print(f"\n[2] Văn bản bảo mật cần gửi: '{secret_text}'")
    
    c = rsa.encrypt(secret_text.encode('utf-8'))
    print(f"    🔒 Bản mã C = M^e mod n:\n       {str(c)[:60]}...")
    
    recovered_bytes = rsa.decrypt(c)
    recovered_text = recovered_bytes.decode('utf-8')
    print(f"    🔓 Bản rõ phục hồi sau khi dùng Private Key (d):\n       '{recovered_text}'")
    assert recovered_text == secret_text, "Giải mã RSA thất bại!"
    print("    ✅ Kiểm thử Mã hóa & Giải mã: HOÀN TOÀN TRÙNG KHỚP!")

    # 3. Thử nghiệm Ký số điện tử & Xác thực toàn vẹn (Digital Signature)
    document = b"Lenh dieu dong nhan su An toan Mang DUT - Khong duoc gia mao!"
    print(f"\n[3] Văn bản hành chính cần ký số:\n    '{document.decode('utf-8')}'")
    
    signature = rsa.sign(document)
    print(f"    ✍️ Chữ ký điện tử S = SHA256(Doc)^d mod n:\n       {str(signature)[:60]}...")
    
    is_valid = RSACipher.verify(document, signature, (e, n))
    print(f"    🔍 Xác thực chữ ký số với Public Key (e, n): {'✅ HỢP LỆ (VERIFIED)' if is_valid else '❌ KHÔNG HỢP LỆ'}")
    assert is_valid, "Xác thực chữ ký thất bại!"
    
    # Giả lập kẻ gian thay đổi 1 ký tự trong văn bản
    tampered_doc = b"Lenh dieu dong nhan su An toan Mang DUT - BI SUA DOI ROI!"
    is_tampered_valid = RSACipher.verify(tampered_doc, signature, (e, n))
    print(f"    ⚠️ Thử nghiệm phát hiện văn bản bị làm giả / sửa đổi: "
          f"{'❌ ĐÃ BỊ PHÁT HIỆN & BÁC BỎ!' if not is_tampered_valid else 'Lỗi bảo mật!'}")
    assert not is_tampered_valid, "Không phát hiện được văn bản bị giả mạo!"
    
    print("\n" + "=" * 70)
    print("✅ KIỂM TRA ĐỊNH TÍNH & ĐỊNH LƯỢNG: RSA THUẦN TOÁN HỌC CHÍNH XÁC 100%!")
    print("=" * 70)


if __name__ == "__main__":
    main()
