#!/usr/bin/env python3
"""
🔐 HỌC PHẦN: AN TOÀN MẠNG & MẬT MÃ HỌC ỨNG DỤNG (CORP-04-SEC)
Tuần 1: Classical Cryptography & Cryptanalysis
Công cụ: Vigenère Cipher Encryption, Decryption & Automated IoC Cracker
Tác giả: DUT Cyber Security Mentor
"""

import sys
import io
import string
import collections
from typing import List, Tuple, Dict

# Đảm bảo in UTF-8 mượt mà trên môi trường Windows console
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Tần suất xuất hiện chữ cái tiếng Anh chuẩn (Nguồn: Beker & Piper, 1982)
ENGLISH_FREQ: Dict[str, float] = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702,
    'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153,
    'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507,
    'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
    'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974,
    'Z': 0.00074
}

# Chỉ số trùng lặp lý thuyết (Index of Coincidence):
# Tiếng Anh tự nhiên ~ 0.0667 | Văn bản ngẫu nhiên hoàn toàn ~ 0.0385
ENGLISH_IOC = 0.0667
RANDOM_IOC = 0.0385


def clean_text(text: str) -> str:
    """Loại bỏ ký tự đặc biệt, dấu cách, đưa về chữ in hoa A-Z."""
    return ''.join(c.upper() for c in text if c.isalpha())


def vigenere_encrypt(plaintext: str, key: str) -> str:
    """Mã hóa văn bản rõ bằng thuật toán Vigenère."""
    pt = clean_text(plaintext)
    k = clean_text(key)
    if not k:
        raise ValueError("Khóa không được để trống!")
    
    ciphertext = []
    key_len = len(k)
    for i, char in enumerate(pt):
        shift = ord(k[i % key_len]) - ord('A')
        encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        ciphertext.append(encrypted_char)
    return ''.join(ciphertext)


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """Giải mã bản mã bằng thuật toán Vigenère khi đã biết khóa."""
    ct = clean_text(ciphertext)
    k = clean_text(key)
    if not k:
        raise ValueError("Khóa không được để trống!")
    
    plaintext = []
    key_len = len(k)
    for i, char in enumerate(ct):
        shift = ord(k[i % key_len]) - ord('A')
        decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        plaintext.append(decrypted_char)
    return ''.join(plaintext)


def calculate_ioc(text: str) -> float:
    """
    Tính Chỉ số Trùng lặp (Index of Coincidence - IoC):
    IC = sum(f_i * (f_i - 1)) / (N * (N - 1))
    """
    cleaned = clean_text(text)
    n = len(cleaned)
    if n <= 1:
        return 0.0
    
    counts = collections.Counter(cleaned)
    numerator = sum(count * (count - 1) for count in counts.values())
    denominator = n * (n - 1)
    return numerator / denominator


def guess_key_length(ciphertext: str, max_key_len: int = 12) -> List[Tuple[int, float]]:
    """
    Xác định độ dài khóa khả dĩ bằng cách chia văn bản thành k dòng con
    và tính trung bình cộng IoC của các dòng con.
    """
    cleaned = clean_text(ciphertext)
    results = []
    
    for k in range(1, max_key_len + 1):
        ioc_substreams = []
        for i in range(k):
            substream = cleaned[i::k]
            if len(substream) > 1:
                ioc_substreams.append(calculate_ioc(substream))
        
        avg_ioc = sum(ioc_substreams) / len(ioc_substreams) if ioc_substreams else 0.0
        results.append((k, avg_ioc))
    
    # Sắp xếp theo mức độ gần với English IoC (0.0667)
    results.sort(key=lambda item: abs(item[1] - ENGLISH_IOC))
    return results


def chi_squared_distance(observed_text: str) -> float:
    """Tính khoảng cách Chi-Squared giữa tần suất chuỗi quan sát và tiếng Anh chuẩn."""
    n = len(observed_text)
    if n == 0:
        return float('inf')
    
    counts = collections.Counter(observed_text)
    chi2 = 0.0
    for char, expected_freq in ENGLISH_FREQ.items():
        expected_count = n * expected_freq
        observed_count = counts.get(char, 0)
        chi2 += ((observed_count - expected_count) ** 2) / expected_count
    return chi2


def crack_vigenere(ciphertext: str, key_len: int) -> Tuple[str, str]:
    """
    Thám mã phục hồi từng ký tự khóa bằng kiểm định Chi-Squared cho từng cột,
    sau đó giải mã hoàn chỉnh văn bản.
    """
    cleaned = clean_text(ciphertext)
    recovered_key = []
    
    for i in range(key_len):
        substream = cleaned[i::key_len]
        best_shift = 0
        min_chi2 = float('inf')
        
        # Thử dịch vòng 26 khả năng (Caesar shift) cho cột hiện tại
        for shift in range(26):
            shifted_stream = ''.join(
                chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
                for c in substream
            )
            chi2 = chi_squared_distance(shifted_stream)
            if chi2 < min_chi2:
                min_chi2 = chi2
                best_shift = shift
        
        recovered_key.append(chr(best_shift + ord('A')))
    
    key_str = ''.join(recovered_key)
    decrypted_text = vigenere_decrypt(cleaned, key_str)
    return key_str, decrypted_text


def main():
    print("=" * 70)
    print("🛡️ DUT CYBERDEFENSE CORP — AUTOMATED VIGENÈRE CRYPTANALYSIS ENGINE")
    print("=" * 70)
    
    sample_secret_doc = (
        "Network security consists of the policies, processes and practices adopted "
        "to prevent, detect and monitor unauthorized access, misuse, modification, "
        "or denial of a computer network and network-accessible resources. "
        "CyberDefense Corporation at Danang University of Science and Technology "
        "focuses on cryptographic principles including symmetric block ciphers, "
        "public key infrastructures, digital signatures, hash algorithms, "
        "firewalls and packet inspections using Wireshark to ensure total CIA triad protection."
    )
    secret_key = "DUTSEC"
    
    print(f"\n[1] Văn bản rõ ban đầu (Plaintext):\n{sample_secret_doc[:120]}...\n")
    print(f"[*] Khóa bí mật sử dụng: '{secret_key}' (Độ dài: {len(secret_key)})")
    
    ciphertext = vigenere_encrypt(sample_secret_doc, secret_key)
    print(f"\n[2] Bản mã tạo ra (Ciphertext):\n{ciphertext[:120]}...\n")
    
    # 1. Thám mã dò độ dài khóa
    print("[3] Phân tích Chỉ số Trùng lặp (IoC) tìm độ dài khóa...")
    top_candidates = guess_key_length(ciphertext, max_key_len=10)
    for rank, (cand_len, cand_ioc) in enumerate(top_candidates[:4], 1):
        marker = "⭐ (Khả dĩ nhất!)" if rank == 1 else ""
        print(f"   Top {rank}: Độ dài k = {cand_len:<2} | IoC trung bình = {cand_ioc:.5f} {marker}")
    
    best_key_len = top_candidates[0][0]
    
    # 2. Bẻ khóa tự động bằng Chi-Squared
    print(f"\n[4] Tự động bẻ khóa từng vị trí với độ dài k = {best_key_len}...")
    recovered_key, recovered_pt = crack_vigenere(ciphertext, best_key_len)
    
    print(f"\n[5] KẾT QUẢ THÁM MÃ THÀNH CÔNG:")
    print(f"   🔑 Khóa bí mật phục hồi được: '{recovered_key}'")
    print(f"   📄 Văn bản giải mã (150 ký tự đầu):\n   {recovered_pt[:150]}...")
    
    assert recovered_key == secret_key, "Khóa thám mã không khớp!"
    print("\n✅ KIỂM TRA ĐỊNH TÍNH: THÁM MÃ THÀNH CÔNG 100% VỚI ĐỘ CHÍNH XÁC TUYỆT ĐỐI!")
    print("=" * 70)


if __name__ == "__main__":
    main()
