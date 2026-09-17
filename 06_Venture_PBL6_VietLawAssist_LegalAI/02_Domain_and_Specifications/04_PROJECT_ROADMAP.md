## 1. BỐN KHỐI KIẾN TRÚC XỬ LÝ ĐỘT PHÁ

### 1. Khối Nhận diện Dạng Đề thi (Intent & Archetype Router) — `MLR-02` & `SA-04`
Khi nhận câu hỏi từ sinh viên, hệ thống phân loại câu hỏi thành 1 trong 5 nhóm:
- `QPPL_STRUCTURE`: Phân tích 3 bộ phận Quy phạm pháp luật (Giả định, Quy định, Chế tài).
- `VPPL_ELEMENTS`: Phân tích 4 yếu tố Cấu thành Vi phạm pháp luật (Mặt khách quan, Mặt chủ quan, Khách thể, Chủ thể).
- `TRUE_FALSE_REASONING`: Câu hỏi Nhận định Đúng/Sai & Giải thích căn cứ pháp lý/lý luận.
- `CIVIL_INHERITANCE`: Bài tập phân chia di sản thừa kế (theo di chúc, theo luật, Điều 644, Điều 652 BLDS).
- `CRIMINAL_AGE_LIABILITY`: Bài tập xác định năng lực trách nhiệm hình sự theo độ tuổi (Điều 12 BLHS).
- `GENERAL_THEORY`: Câu hỏi lý thuyết các ngành luật khác.

### 2. Khối Truy xuất Ngữ cảnh Kép (Hybrid Dual-Context Retrieval) — `DE-03` & `MLR-02`
Không chỉ truy xuất điều luật thô, hệ thống kết hợp 2 nguồn dữ liệu:
1. **Corpus Văn bản Luật thực định (`law_articles`):** Hiến pháp 2013, BLDS 2015, BLHS 2015 (sửa đổi 2017), Luật HNGĐ 2014, BLLĐ 2019.
2. **Corpus Lý luận Giáo trình Chuẩn (`textbook_principles`):** Trích đoạn lý luận từ Giáo trình PLĐC Bộ GD&ĐT (định nghĩa lỗi, quan hệ nhân quả, các hàng thừa kế, điều kiện giao dịch dân sự).
- **Cơ chế tìm kiếm:**
  - *Tầng 1:* BM25Okapi với bộ tách từ tiếng Việt Underthesea.
  - *Tầng 2:* Dense Search với `bkai-foundation-models/vietnamese-bi-encoder` + FAISS IndexFlatIP.

### 3. Khối Sinh Lời giải Chuẩn Barem (Template-Guided Generator) — `MLR-02`
- **Tầng 3 (Base RAG):** Áp dụng kỹ thuật **Few-Shot Structured Chain-of-Thought (CoT)** trên mô hình `Qwen2.5-1.5B-Instruct` lượng tử hóa 4-bit.
- **Tầng 4 (Fine-tuned RAG):** Nạp LoRA Adapter (Rank $r=16$, Alpha $\alpha=32$) được huấn luyện trên 500 cặp Q&A chuẩn barem.

### 4. Khối Hậu xử lý & Chống Ảo giác (Legal Citation Guardrail) — `EVAL-05`
- Module tự động dùng Regex bóc tách mọi trích dẫn `Điều \d+ (Khoản \d+)?` trong câu trả lời sinh ra.
- Truy vấn ngược vào CSDL SQLite:
  - Nếu điều luật tồn tại trong corpus $\rightarrow$ Đánh dấu tích xanh bảo đảm [Verified].
  - Nếu điều luật không tồn tại trong corpus $\rightarrow$ Đánh dấu cờ đỏ cảnh báo [Unverified] hoặc tự động gắn ghi chú hiệu chỉnh.

---

## 2. BAREM LỜI GIẢI MẪU 5 DẠNG BÀI KINH ĐIỂN

### Mẫu 1: Dạng Phân tích Quy phạm pháp luật (QPPL)
```markdown
1. BỘ PHẬN GIẢ ĐỊNH:
   - Trả lời: Ai? Khi nào? Trong hoàn cảnh nào?
   - Căn cứ văn bản: [Trích nguyên văn phần giả định]
2. BỘ PHẬN QUY ĐỊNH:
   - Trả lời: Phải làm gì? Được làm gì? Không được làm gì?
   - Nhận diện: Quy định trực tiếp / Mệnh lệnh cấm đoán ẩn
3. BỘ PHẬN CHẾ TÀI:
   - Trả lời: Hậu quả pháp lý bất lợi gì nếu vi phạm?
   - Phân loại chế tài: Hình sự / Dân sự / Hành chính / Kỷ luật
4. NHẬN XÉT:
   - Quy phạm thuộc loại dứt khoát hay tùy nghi? Có khuyết thành phần nào không?
```

### Mẫu 2: Dạng Phân tích Cấu thành Vi phạm pháp luật (VPPL)
```markdown
I. KẾT LUẬN TÍNH CHẤT HÀNH VI:
   - Hành vi có thỏa mãn 4 dấu hiệu của Vi phạm pháp luật hay không?
II. BẢNG PHÂN TÍCH 4 YẾU TỐ CẤU THÀNH:
   1. MẶT KHÁCH QUAN:
      - Hành vi trái pháp luật (Hành động/Không hành động).
      - Hậu quả nguy hiểm cho xã hội.
      - Mối quan hệ nhân quả tất yếu.
      - Thời gian, địa điểm, công cụ, phương tiện vi phạm.
   2. MẶT CHỦ QUAN:
      - Lỗi: Xác định rõ (Cố ý trực tiếp / Cố ý gián tiếp / Vô ý vì quá tự tin / Vô ý do cẩu thả) kèm phân tích về mặt lý trí và ý chí.
      - Động cơ và Mục đích vi phạm.
   3. KHÁCH THỂ:
      - Quan hệ xã hội được pháp luật bảo vệ bị xâm hại.
   4. CHỦ THỂ:
      - Độ tuổi chịu trách nhiệm theo luật định.
      - Khả năng nhận thức và điều khiển hành vi (Năng lực TNPL).
III. KẾT LUẬN TRÁCH NHIỆM PHÁP LÝ:
   - Phân loại vi phạm: Hình sự / Hành chính / Dân sự / Kỷ luật.
   - Căn cứ điều khoản áp dụng cụ thể.
```

---

## 3. LỘ TRÌNH THỰC THI 15 TUẦN HIỆU CHỈNH (EXECUTION ROADMAP)

| Tuần | Trọng tâm ML / NLP | Trọng tâm Hệ thống / Web | Trọng tâm Dữ liệu & Đánh giá | Mốc nghiệm thu (Milestone) |
|:---:|:---|:---|:---|:---|
| **W1** | Nghiên cứu Intent Router & Prompt CoT | Setup FastAPI + Docker + SQLite | Crawl 5 bộ luật + Bóc tách Giáo trình PLĐC | ✅ Corpus kép sẵn sàng |
| **W2** | Triển khai BM25Okapi + Underthesea | API endpoint `/api/retrieve/bm25` | Thiết lập bộ 20 Test Queries chuẩn barem | ✅ Tầng 1 hoàn tất |
| **W3** | PhoBERT Embedding + FAISS Index | API endpoint `/api/retrieve/dense` | Xây dựng FAISS index offline |  |
| **W4** | Đánh giá so sánh Recall@5 T1 vs T2 | UI React: Khung nhập liệu & Query Inspector | **Viết Báo Cáo Tiến Độ Đợt 1 nộp GV** | ✅ Tầng 2 & Báo cáo 1 |
| **W5** | Tích hợp Qwen2.5-1.5B 4-bit (BitsAndBytes)| API endpoint `/api/generate/rag` | Thiết kế Prompt Template theo 5 dạng đề |  |
| **W6** | Tinh chỉnh RAG pipeline sinh chuẩn barem | UI React: Thẻ hiển thị câu trả lời cấu trúc | Đo lường ROUGE-L & BERTScore Tầng 3 | ✅ Tầng 3 hoàn tất |
| **W7** | Chuẩn bị Colab T4 script cho LoRA | API endpoint `/api/compare` (4 tầng) | **Biên soạn 500 cặp Q&A chuẩn barem thi** | ✅ Dataset SFT sẵn sàng |
| **W8** | Huấn luyện LoRA Adapter trên Colab T4 | Serve LoRA Adapter trên Backend | Kiểm thử độ chính xác trích dẫn Tầng 4 | ✅ Tầng 4 hoàn tất |
| **W9** | Fine-tuning nâng cao & Error Analysis | UI React: Tab "Chế độ Đối sánh Hội đồng" | Đo lường trọn bộ metrics cả 4 tầng | ✅ Full 4-Tier Ladder |
| **W10**| Hoàn thiện Legal Citation Guardrail | Kiểm thử chịu tải hệ thống bằng Artillery | **Viết Báo Cáo Tiến Độ Đợt 2 nộp GV** | ✅ Báo cáo 2 & Load Test |
| **W11**| Viết Chương 3 Thuyết minh (Phần ML/NLP) | Viết Chương 2 Thuyết minh (Kiến trúc Web) | Lập bảng số liệu và biểu đồ radar |  |
| **W12**| Rà soát lỗi suy diễn pháp lý | Kiểm thử E2E giao diện bằng Selenium | Bổ sung 50 câu hỏi test thực tế |  |
| **W13**| Đóng băng mã nguồn & cố định seed (42) | Hoàn thiện Docker-compose & Server Deploy | Biên tập toàn bộ báo cáo đồ án |  |
| **W14**| Chuẩn bị Slide thuyết trình bảo vệ | Quay video demo backup kịch bản | Tổng duyệt phản biện nội bộ nhóm | ✅ Báo cáo & Slide xong |
| **W15**| **BẢO VỆ ĐỒ ÁN PBL6 TRƯỚC HỘI ĐỒNG** | **BẢO VỆ ĐỒ ÁN PBL6 TRƯỚC HỘI ĐỒNG** | **BẢO VỆ ĐỒ ÁN PBL6 TRƯỚC HỘI ĐỒNG** | 🎯 ĐẠT ĐIỂM 10/10 |

---

## 4. QUY CHUẨN AN TOÀN & BÀN GIAO (AAP PROTOCOL)
- Mọi script kiểm thử và huấn luyện đều phải khai báo `torch.manual_seed(42)` và `np.random.seed(42)` để đảm bảo tính tái lập kết quả 100%.
- Kiểm soát tài nguyên VRAM nghiêm ngặt $\le 3.5\text{GB}$ để tương thích tuyệt đối với laptop GPU RTX 3050 4GB.
- Báo cáo bàn giao phiên (Session Handover) phải được cập nhật đều đặn theo quy chế quản trị doanh nghiệp.
