# 📝 BAREM 5 DẠNG ĐỀ THI PHÁP LUẬT ĐẠI CƯƠNG — Template Chuẩn Hóa

> **Mục đích**: Định nghĩa cấu trúc output chuẩn barem cho từng dạng đề thi PLĐC.
> Agent đọc file này khi cần biết format trả lời đúng barem → sinh prompt template → xây dựng JSON schema.

---

## Phân biệt 2 Hệ Đào tạo

| Tiêu chí | Hệ Không chuyên (ĐHBK, Kỹ thuật) | Hệ Chuyên (Luật, Xã hội) |
|:---|:---|:---|
| **Trọng tâm** | Bài tập tình huống, tính toán thừa kế, VPPL | Phân tích nguồn gốc, bản chất nhà nước |
| **Phong cách** | Ngắn gọn, logic, bám sát barem điểm | Văn xuôi phân tích, luận điểm dài |
| **VietLawAssist target** | ✅ ĐỐI TƯỢNG CHÍNH | Hỗ trợ bổ sung (toggle mode) |

---

## Dạng 1: Phân tích Quy phạm Pháp luật (QPPL)

**Intent code**: `QPPL_STRUCTURE`  
**Trigger keywords**: "phân tích quy phạm", "giả định", "quy định", "chế tài", "cấu trúc QPPL"

### Template Output (Barem 10/10)

```
1. BỘ PHẬN GIẢ ĐỊNH:
   - Trả lời: Ai? Khi nào? Trong hoàn cảnh nào?
   - Trích dẫn: [Trích nguyên văn phần giả định từ điều luật]

2. BỘ PHẬN QUY ĐỊNH:
   - Trả lời: Phải làm gì? Được làm gì? Không được làm gì?
   - Phân loại: Quy định bắt buộc / Quy định cấm đoán / Quy định cho phép

3. BỘ PHẬN CHẾ TÀI:
   - Trả lời: Hậu quả pháp lý bất lợi gì nếu vi phạm?
   - Phân loại chế tài: Hình sự / Dân sự / Hành chính / Kỷ luật
   - Lưu ý: Chế tài có thể nằm ở điều luật khác (QPPL viện dẫn)

4. NHẬN XÉT:
   - Quy phạm thuộc loại: Dứt khoát hay Tùy nghi?
   - Quy phạm có khuyết thành phần nào không? (VD: thiếu chế tài trực tiếp)
```

### JSON Schema
```json
{
  "intent": "QPPL_STRUCTURE",
  "output_schema": {
    "gia_dinh": { "ai": "", "khi_nao": "", "hoan_canh": "", "trich_dan": "" },
    "quy_dinh": { "noi_dung": "", "phan_loai": "bat_buoc|cam_doan|cho_phep" },
    "che_tai": { "hau_qua": "", "loai": "hinh_su|dan_su|hanh_chinh|ky_luat", "dieu_luat_ap_dung": "" },
    "nhan_xet": { "loai_qppl": "dut_khoat|tuy_nghi", "khuyet_thanh_phan": "" }
  }
}
```

---

## Dạng 2: Phân tích Cấu thành Vi phạm Pháp luật (VPPL)

**Intent code**: `VPPL_ELEMENTS`  
**Trigger keywords**: "vi phạm pháp luật", "cấu thành", "mặt khách quan", "mặt chủ quan", "4 yếu tố"

### Template Output (Barem 10/10)

```
I. KẾT LUẬN TÍNH CHẤT:
   - Hành vi CÓ/KHÔNG thỏa mãn 4 dấu hiệu Vi phạm pháp luật.

II. BẢNG PHÂN TÍCH 4 YẾU TỐ CẤU THÀNH:

   1. MẶT KHÁCH QUAN:
      a) Hành vi trái pháp luật: [Hành động / Không hành động] — mô tả cụ thể
      b) Hậu quả nguy hiểm cho xã hội: [Mô tả thiệt hại thực tế]
      c) Mối quan hệ nhân quả: [Chứng minh hành vi là nguyên nhân trực tiếp]
      d) Công cụ, phương tiện, thời gian, địa điểm: [Chi tiết]

   2. MẶT CHỦ QUAN:
      a) Hình thức lỗi: [Cố ý trực tiếp / Cố ý gián tiếp / Vô ý vì quá tự tin / Vô ý do cẩu thả]
         - Về lý trí: [Nhận thức được/không được tính nguy hiểm]
         - Về ý chí: [Mong muốn / Để mặc / Tự tin ngăn / Không thấy trước]
      b) Động cơ: [Lý do thúc đẩy hành vi]
      c) Mục đích: [Kết quả mà chủ thể mong muốn đạt được]

   3. KHÁCH THỂ:
      - Quan hệ xã hội bị xâm hại: [VD: quyền bất khả xâm phạm về sức khỏe]
      - Được bảo vệ bởi: [Trích dẫn điều luật cụ thể]

   4. CHỦ THỂ:
      - Độ tuổi: [≥ 16 / 14-16 / < 14] — đối chiếu Điều 12 BLHS
      - Năng lực nhận thức: [Bình thường / Hạn chế / Mất năng lực]
      - Kết luận năng lực TNPL: [Có đủ / Không đủ]

III. KẾT LUẬN TRÁCH NHIỆM PHÁP LÝ:
   - Phân loại vi phạm: [Hình sự / Hành chính / Dân sự / Kỷ luật]
   - Căn cứ: [Điều X, Khoản Y, Bộ luật Z]
```

### JSON Schema
```json
{
  "intent": "VPPL_ELEMENTS",
  "output_schema": {
    "ket_luan_so_bo": "co_vppl|khong_vppl",
    "mat_khach_quan": {
      "hanh_vi": "", "loai": "hanh_dong|khong_hanh_dong",
      "hau_qua": "", "nhan_qua": "", "cong_cu": ""
    },
    "mat_chu_quan": {
      "loi": "co_y_truc_tiep|co_y_gian_tiep|vo_y_qua_tu_tin|vo_y_cau_tha",
      "ly_tri": "", "y_chi": "", "dong_co": "", "muc_dich": ""
    },
    "khach_the": { "quan_he_xa_hoi": "", "bao_ve_boi": "" },
    "chu_the": { "do_tuoi": 0, "nang_luc": "", "ket_luan_tnpl": "" },
    "ket_luan": { "loai_vi_pham": "", "dieu_luat": "" }
  }
}
```

---

## Dạng 3: Nhận định Đúng / Sai

**Intent code**: `TRUE_FALSE`  
**Trigger keywords**: "nhận định", "đúng hay sai", "đúng sai", "nhận xét"

### Template Output (Barem 10/10)

```
KẾT LUẬN: [ĐÚNG / SAI]

CĂN CỨ PHÁP LÝ / LÝ LUẬN:
- [Trích dẫn nguyên tắc từ giáo trình hoặc điều luật cụ thể]

GIẢI THÍCH:
- [Phân tích tại sao đúng/sai dựa trên nguyên tắc trên]
- [Nếu SAI: đưa phản ví dụ hoặc chỉ ra điều kiện ngoại lệ]
- [Nếu ĐÚNG: khẳng định lại bằng ví dụ minh họa]
```

### JSON Schema
```json
{
  "intent": "TRUE_FALSE",
  "output_schema": {
    "ket_luan": "dung|sai",
    "can_cu": { "nguon": "giao_trinh|dieu_luat", "trich_dan": "" },
    "giai_thich": "",
    "vi_du_minh_hoa": ""
  }
}
```

---

## Dạng 4: Bài tập Chia Di sản Thừa kế

**Intent code**: `CIVIL_INHERIT`  
**Trigger keywords**: "thừa kế", "di sản", "di chúc", "chia tài sản", "Điều 644", "Điều 652"

### Template Output (Barem 10/10)

```
BƯỚC 1: XÁC ĐỊNH DI SẢN THỪA KẾ
   - Tổng tài sản chung vợ chồng: [X] triệu
   - Phần của người còn sống: [X/2] triệu
   - Di sản người chết để lại: [X/2 + tài sản riêng] triệu
   - Trừ chi phí mai táng, nợ (nếu có)

BƯỚC 2: XÉT DI CHÚC (nếu có)
   - Di chúc có hợp pháp không? (Điều 630 BLDS 2015)
   - Phân chia theo di chúc: [Liệt kê từng người được hưởng]

BƯỚC 3: TÍNH 1 SUẤT THỪA KẾ THEO LUẬT
   - Hàng thừa kế thứ nhất (Điều 651): [Liệt kê]
   - 1 suất = Di sản ÷ Số người hàng 1 = [Y] triệu

BƯỚC 4: BẢO VỆ NGƯỜI ĐƯỢC BẢO VỆ (Điều 644 BLDS)
   - Ai thuộc diện bảo vệ? (Con chưa thành niên, cha mẹ già, vợ/chồng không có KNLĐ)
   - Mỗi người được ≥ 2/3 × 1 suất = [Z] triệu
   - Nếu di chúc cho ít hơn → bổ sung đủ 2/3

BƯỚC 5: THỪA KẾ THẾ VỊ (Điều 652 BLDS, nếu có)
   - Nếu con của người chết đã chết trước → Cháu được hưởng thay

BẢNG PHÂN CHIA CUỐI CÙNG:
| Người thừa kế | Căn cứ | Số tiền được hưởng |
|:---|:---|---:|
| ... | Di chúc / Theo luật / Điều 644 | ... triệu |
```

### JSON Schema
```json
{
  "intent": "CIVIL_INHERIT",
  "output_schema": {
    "di_san": { "tong_tai_san": 0, "phan_nguoi_song": 0, "di_san_thuoc_ke": 0, "chi_phi_tru": 0 },
    "di_chuc": { "co_di_chuc": false, "hop_phap": false, "phan_chia": [] },
    "suat_theo_luat": { "hang_1": [], "so_nguoi": 0, "gia_tri_1_suat": 0 },
    "dieu_644": [{ "nguoi": "", "duoc_huong_toi_thieu": 0 }],
    "the_vi": [{ "nguoi_chet_truoc": "", "nguoi_the_vi": "" }],
    "bang_phan_chia": [{ "nguoi": "", "can_cu": "", "so_tien": 0 }]
  }
}
```

---

## Dạng 5: Xác định Tuổi chịu TNHS

**Intent code**: `CRIMINAL_AGE`  
**Trigger keywords**: "tuổi chịu trách nhiệm", "Điều 12", "năng lực trách nhiệm hình sự", "14 tuổi", "16 tuổi"

### Template Output (Barem 10/10)

```
BƯỚC 1: XÁC ĐỊNH ĐỘ TUỔI CHÍNH XÁC
   - Người vi phạm: [Tên], [X] tuổi
   - Nhóm tuổi: [Dưới 14 / Từ đủ 14 đến dưới 16 / Từ đủ 16 đến dưới 18 / Từ đủ 18]

BƯỚC 2: XÁC ĐỊNH LOẠI TỘI PHẠM (Điều 9 BLHS 2015)
   - Tội danh: [Tên tội]
   - Phân loại: [Ít nghiêm trọng / Nghiêm trọng / Rất nghiêm trọng / Đặc biệt nghiêm trọng]
   - Căn cứ: Khung hình phạt tối đa [X] năm tù

BƯỚC 3: ĐỐI CHIẾU ĐIỀU 12 BLHS 2015
   - Khoản 1: Từ đủ 16 tuổi → Chịu TNHS về MỌI tội phạm
   - Khoản 2: Từ đủ 14 đến dưới 16 tuổi → CHỈ chịu TNHS về:
     + Tội phạm rất nghiêm trọng DO CỐ Ý
     + Tội phạm đặc biệt nghiêm trọng
   - Dưới 14 tuổi: KHÔNG chịu TNHS

BƯỚC 4: KẾT LUẬN
   - [Tên] [CÓ / KHÔNG] phải chịu trách nhiệm hình sự về [tội danh]
   - Căn cứ: Khoản [X] Điều 12 BLHS 2015
```

### JSON Schema
```json
{
  "intent": "CRIMINAL_AGE",
  "output_schema": {
    "chu_the": { "ten": "", "tuoi": 0, "nhom_tuoi": "duoi_14|14_den_16|16_den_18|tren_18" },
    "toi_pham": { "toi_danh": "", "phan_loai": "it_nghiem_trong|nghiem_trong|rat_nghiem_trong|dac_biet_nghiem_trong", "hinh_phat_toi_da": "" },
    "doi_chieu_dieu_12": { "khoan_ap_dung": 0, "dieu_kien_thoa_man": "" },
    "ket_luan": { "chiu_tnhs": true, "can_cu": "" }
  }
}
```

---

## Intent Router — Bảng Mapping

| Pattern trong câu hỏi | Intent Code | Template áp dụng |
|:---|:---|:---|
| "phân tích quy phạm", "giả định.*quy định.*chế tài" | `QPPL_STRUCTURE` | Dạng 1 |
| "vi phạm pháp luật", "4 yếu tố", "cấu thành", "mặt khách quan" | `VPPL_ELEMENTS` | Dạng 2 |
| "đúng hay sai", "nhận định", "nhận xét.*đúng" | `TRUE_FALSE` | Dạng 3 |
| "thừa kế", "di sản", "di chúc", "chia.*tài sản" | `CIVIL_INHERIT` | Dạng 4 |
| "tuổi.*trách nhiệm", "Điều 12", "14 tuổi.*16 tuổi" | `CRIMINAL_AGE` | Dạng 5 |
| *(không match pattern nào trên)* | `GENERAL_THEORY` | Trả lời theo logic lý thuyết chung |

> **Xử lý overlap**: Khi câu hỏi match nhiều dạng (VD: "Nhận định đúng sai: Người 14 tuổi chịu TNHS mọi tội"), ưu tiên dạng **bao trùm nhất** (Dạng 3 bao trùm Dạng 5 → dùng template Dạng 3, nhưng giải thích phải dùng logic Dạng 5 để chứng minh).
