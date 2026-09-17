# 📜 ĐIỀU LỆ PHÒNG NGHIỆP VỤ PHÁP LÝ & ĐẶC TẢ KỸ THUẬT (DOMAIN & SPECIFICATIONS DIVISION)
## Phòng 02 — Dự Án VietLawAssist Legal AI (VENTURE-06-PBL6)

> **Mã Phòng Ban:** `PBL6-DEPT-02`  
> **Dự án:** VietLawAssist — Hệ thống Trợ lý Thông minh Ôn thi Môn Pháp luật Đại cương  
> **Trưởng phòng phụ trách:** Ban Kỹ Thuật & Kiến Trúc Hệ Thống (Role Handmade) & `PSD-04`  
> **Cấp bậc quản trị:** Cấp 2 — Đặc tả kỹ thuật chi tiết 4 tầng ML, cơ sở dữ liệu luật thực định, JSON Schema barem đề thi và runbooks

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `PBL6-DEPT-02` chịu trách nhiệm lưu trữ toàn bộ các tài liệu đặc tả kiến trúc kỹ thuật, thiết kế dữ liệu và bộ tiêu chuẩn barem chấm thi của môn Pháp luật Đại cương:
1. **Quản lý Khái niệm Dự án & Đối tượng Thụ hưởng (Project Concept)**: Làm rõ nỗi đau của sinh viên khi ôn thi môn Pháp luật Đại cương (khó nhớ số Điều, khó áp dụng lý thuyết vào tình huống thực tế) và định hình giá trị sư phạm của hệ thống.
2. **Đặc tả Kiến Trúc 4 Tầng AI & Hạ Tầng Dữ Liệu (Technical Specifications)**:
   - *Tầng 1 (Sparse Retrieval)*: Thuật toán BM25 trên tập từ khóa pháp lý (phân tích n-gram tiếng Việt).
   - *Tầng 2 (Dense Retrieval)*: Mô hình nhúng ngữ nghĩa PhoBERT-v2 / BGE-M3 kết hợp vector index FAISS (FlatL2 / HNSW).
   - *Tầng 3 (Cross-Encoder Re-ranking)*: Mô hình tái xếp hạng chấm điểm độ tương quan trực tiếp giữa câu hỏi tình huống và đoạn văn bản luật.
   - *Tầng 4 (LLM LoRA Generation)*: Mô hình sinh văn bản giải đề có cấu trúc, chuẩn hóa theo phương pháp IRAC (Issue - Rule - Analysis - Conclusion).
3. **Chuẩn Hóa Barem 5 Dạng Đề Thi (Exam Barem Templates)**: Thiết lập cấu trúc JSON Schema chuẩn hóa cho 5 dạng bài tập cốt lõi (Xử phạt vi phạm hành chính, Phân tích cấu thành tội phạm, Hợp đồng dân sự vô hiệu, Tranh chấp lao động, Thừa kế theo pháp luật) và dạng câu hỏi lý thuyết.

---

## 2. BỘ QUY TẮC BẤT BIẾN (DOMAIN & TECHNICAL INVARIANTS)
1. **Nguyên tắc Khớp Barem Tuyệt Đối (Strict JSON Schema Invariant)**: Mọi câu trả lời sinh ra từ hệ thống bắt buộc phải khớp 100% với JSON Schema quy định trong `03_EXAM_BAREM_TEMPLATES.md`. Cấm tuyệt đối việc sinh văn bản tự do không có cấu trúc.
2. **Nguyên tắc "Có Dẫn Chứng Mới Được Kết Luận" (Evidence-First Invariant)**: Trong phương pháp IRAC, phần Kết luận (Conclusion) và Phân tích (Analysis) bắt buộc phải viện dẫn số hiệu Điều, Khoản, Điểm và tên Văn bản Quy phạm Pháp luật cụ thể từ tập Retrieval.
3. **Nguyên tắc Ngân Sách VRAM Cục Bộ $\le 3.5\text{GB}$**: Mọi mô hình embedding, re-ranker và generator khi nạp đồng thời vào bộ nhớ phải được tối ưu bằng lượng tử hóa (Quantization 8-bit / 4-bit) hoặc offloading để không gây tràn VRAM trên GPU RTX 3050 (4GB).
4. **Nguyên tắc Toàn Vẹn CSDL Pháp Luật (Immutable Corpus Rule)**: Dữ liệu luật trong SQLite phải được chuẩn hóa theo phân cấp: `Văn bản` $\rightarrow$ `Chương` $\rightarrow$ `Điều` $\rightarrow$ `Khoản` $\rightarrow$ `Điểm`. Không chia nhỏ văn bản làm đứt gãy tính toàn vẹn của điều luật.

---

## 3. BỘ LỆNH & TOOLCHAIN KỸ THUẬT (TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Kiểm tra cấu trúc CSDL SQLite văn bản luật
sqlite3 data/legal_corpus.db ".tables"
sqlite3 data/legal_corpus.db "SELECT count(*) FROM articles;"

# 2. Kiểm tra chỉ mục vector FAISS và kích thước embedding
python -c "import faiss; index = faiss.read_index('data/faiss_phobert.index'); print(f'Total Vectors: {index.ntotal} | Dimension: {index.d}')"

# 3. Chạy kiểm thử tự động API giải bài tập pháp luật bằng pytest
pytest tests/test_legal_rag_pipeline.py -v

# 4. Đo lường chỉ số RAGAS (Faithfulness, Answer Relevance)
python scripts/evaluate_ragas_metrics.py --test-set data/golden_test_cases.json
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
02_Domain_and_Specifications/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── 01_PROJECT_CONCEPT.md              # Bối cảnh ra đời, nỗi đau sinh viên và giải pháp sư phạm
├── 02_TECHNICAL_SPECIFICATIONS.md     # Đặc tả kiến trúc 4 tầng ML, SQLite, FAISS & FastAPI
├── 03_EXAM_BAREM_TEMPLATES.md         # Khung barem 5 dạng đề thi cốt lõi & JSON Schemas
├── 04_PROJECT_ROADMAP.md              # Lộ trình kỹ thuật 15 tuần theo từng sprint
└── runbooks/                          # Cẩm nang xử lý sự cố kỹ thuật hệ thống
    ├── RUNBOOK_RAG_LOW_RECALL.md      # Khắc phục độ phủ truy xuất thấp ở Tầng 1 và 2
    ├── RUNBOOK_CUDA_VRAM_OVERFLOW.md  # Khắc phục tràn bộ nhớ khi chạy PhoBERT + LLM
    └── RUNBOOK_JSON_SCHEMA_MISMATCH.md# Xử lý phản hồi LLM bị vỡ cấu trúc JSON
```

---

## 5. MẪU KHUNG CODE & BAREM JSON SCHEMA (GOLD MASTER BOILERPLATE)

### Bộ Khung JSON Schema Barem Chấm Đề Thi Phương Pháp IRAC (`irac_barem_schema.json`)
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "VietLawAssistIRACResponse",
  "type": "object",
  "required": [
    "issue_identification",
    "legal_basis",
    "legal_analysis",
    "final_conclusion",
    "exam_tips"
  ],
  "properties": {
    "issue_identification": {
      "type": "string",
      "description": "Xác định rõ vấn đề pháp lý cần giải quyết trong tình huống (Issue)"
    },
    "legal_basis": {
      "type": "array",
      "description": "Danh sách các căn cứ pháp luật viện dẫn chính xác (Rule)",
      "items": {
        "type": "object",
        "required": ["law_name", "article", "clause", "quote_summary"],
        "properties": {
          "law_name": { "type": "string", "example": "Bộ luật Dân sự 2015" },
          "article": { "type": "integer", "example": 122 },
          "clause": { "type": "integer", "example": 1 },
          "quote_summary": { "type": "string", "example": "Điều kiện có hiệu lực của giao dịch dân sự" }
        }
      }
    },
    "legal_analysis": {
      "type": "string",
      "description": "Lập luận đối chiếu hành vi thực tế với điều kiện quy định trong luật (Analysis)"
    },
    "final_conclusion": {
      "type": "string",
      "description": "Kết luận dứt khoát câu trả lời: Hợp pháp/Bất hợp pháp, Mức xử phạt, Quyền lợi (Conclusion)"
    },
    "exam_tips": {
      "type": "string",
      "description": "Lời khuyên sư phạm giúp sinh viên không bị trừ điểm khi viết bài thi trên giấy"
    }
  }
}
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Chuẩn hóa 5 dạng đề thi**: Barem bao quát đầy đủ 5 dạng bài tập tình huống lớn trong chương trình thi Pháp luật Đại cương tại DUT.
- [x] **Kiến trúc 4 tầng khả thi**: Có thông số cụ thể về mô hình (PhoBERT, FAISS Index, Cross-Encoder, LoRA) tương thích với cấu hình RTX 3050.
- [x] **Schema JSON hợp lệ 100%**: Các schema định nghĩa trong tài liệu đều vượt qua kiểm tra `jsonschema.validate()`.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ KỸ THUẬT (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: Truy xuất RAG bị sót điều luật quan trọng (Low Recall)
- **Hiện tượng**: Câu hỏi tình huống về thừa kế nhưng Tầng 1 và 2 chỉ trả về các điều luật về giao dịch dân sự chung, không tìm thấy Điều 651 (Người thừa kế theo pháp luật).
- **Nguyên nhân**: Sự khác biệt từ vựng giữa ngôn ngữ đời thường trong đề thi ("chia tài sản cho con riêng") và ngôn ngữ pháp lý hàn lâm ("hàng thừa kế thứ nhất").
- **Quy trình xử lý 3 bước**:
  1. Kích hoạt Query Expansion: Dùng mô hình ngôn ngữ sinh 3 câu truy vấn tương đương chứa các thuật ngữ pháp lý chuẩn hóa.
  2. Bổ sung từ điển đồng nghĩa pháp lý (Legal Synonym Thesaurus) vào bộ tokenizer BM25.
  3. Kết hợp điểm lai (Hybrid Search Score): $\text{Score} = 0.4 \times \text{BM25} + 0.6 \times \text{PhoBERT\_Dense}$.

### Sự cố 2: Đầu ra của LLM bị vỡ định dạng JSON (JSON Decode Error)
- **Hiện tượng**: `json.loads(response)` quăng lỗi `JSONDecodeError: Expecting ',' delimiter` do LLM tự động chèn thêm văn bản chào hỏi hoặc quên đóng dấu ngoặc.
- **Cách khắc phục chuẩn**:
  1. Sử dụng tính năng Grammar-Constrained Decoding (sử dụng JSON mode của vLLM / llama-cpp-python).
  2. Triển khai bộ lọc hậu xử lý Regex trích xuất khối JSON nằm giữa ```json ... ```:
     ```python
     import re, json
     match = re.search(r"```json\s*(\{.*?\})\s*```", raw_text, re.DOTALL)
     if match:
         parsed_json = json.loads(match.group(1))
     ```
