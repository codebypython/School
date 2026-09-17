# 🔬 NGHIÊN CỨU CHUYÊN SÂU: KIẾN TRÚC & TỐI ƯU HÓA PROMPT CHO GEMINI
## Nghiên cứu hành vi nhận thức của Gemini 3.1 Pro & Gemini 3.8 Flash

> **Mã tài liệu:** `RES-GEMINI-01` | **Khối nghiên cứu:** `01_Model_Intelligence_Research`  
> **Chuyên viên phụ trách:** Agent `MIR-01` (Model Intelligence Researcher)  
> **Đối tượng mô hình:** Google DeepMind Gemini 3.1 Pro (Deep Reasoning) & Gemini 3.8 Flash (High-throughput / Low-latency)

---

## 1. PHÂN TÍCH KIẾN TRÚC & ĐẶC TÍNH NHẬN THỨC CỐT LÕI

### 1.1. Cửa sổ ngữ cảnh 2 Triệu Tokens (2M Context Window) & Cơ chế Chú ý (Attention Dynamics)
* **Thế mạnh vượt trội**: Gemini có khả năng nuốt trọn toàn bộ một kho tri thức (Toàn bộ 5 bộ luật Việt Nam, hoặc toàn bộ codebase dự án, hoặc hàng chục file pcap Wireshark) mà không cần phải chunking quá nhỏ.
* **Hiện tượng "Lost-in-the-Middle" (Lạc lối giữa ngữ cảnh)**: Mặc dù điểm số Needle-in-a-Haystack (NIAH) đạt > 99%, khi ngữ cảnh vượt quá 500K tokens, sự chú ý (Attention Weight) ở phần giữa của prompt có xu hướng giảm nhẹ nếu không có các mốc neo.
  - 🛠️ **Giải pháp tối ưu**: Kỹ thuật **Anchor Markers (Thẻ neo vị trí)**. Sử dụng các thẻ định danh rõ ràng như `[CORE_SPEC_ANCHOR_1]`, `[INPUT_DATA_STREAM]`, `[VERIFICATION_CRITERIA]` ở đầu và cuối văn bản dài.
  - Đặt các nguyên tắc quan trọng nhất (**Hard Constraints**) ở **cuối cùng** của prompt (Recency Bias) hoặc trong khối **System Instructions**.

### 1.2. So sánh Gemini 3.1 Pro vs Gemini 3.8 Flash

| Đặc tính kỹ thuật | Gemini 3.1 Pro (Heavyweight Reasoner) | Gemini 3.8 Flash (Lightweight Speedster) |
|:---|:---|:---|
| **Đặc thù tính toán** | Suy luận sâu đa bước, phân tích kiến trúc, giải bài toán toán học phức tạp (Đạo hàm ma trận ML, Chứng minh mật mã SEC). | Tốc độ cực nhanh, phản hồi tức thì, tối ưu cho tra cứu tài liệu, rà soát lỗi cú pháp và chạy smoke tests. |
| **Xu hướng hành vi** | Thích giải thích cặn kẽ cơ chế nền tảng trước khi viết code. Ít khi bỏ sót chi tiết. | Có xu hướng tóm tắt hoặc viết code ngắn gọn nếu không bị ép buộc. Rất nhạy với độ dài đầu ra. |
| **Chiến lược Prompting** | Cung cấp tài liệu kinh điển, yêu cầu phân tích đa chiều: $\text{Lý thuyết} \rightarrow \text{Kiến trúc} \rightarrow \text{Mã nguồn}$. | Dùng mệnh lệnh ngắn gọn, dứt khoát, ép kiểu output bằng danh sách gạch đầu dòng hoặc Schema cụ thể. |

---

## 2. CÁC QUY TẮC VÀNG KHI VIẾT PROMPT CHO DÒNG GEMINI

### Quy tắc 1: Khai thác Triệt để Khối `System Instructions`
Gemini ưu tiên cực cao các chỉ dẫn nằm trong `System Instructions` hơn là chỉ dẫn nằm rải rác trong `User Prompt`.
- Mọi quy định về vai trò Mentor (`Role Persona`), ngôn ngữ lập trình, giới hạn phần cứng (RTX 3050 4GB) phải được đặt trong System Directives.

### Quy tắc 2: Kỹ thuật Ràng Buộc Phủ Định (Negative Constraints)
Gemini có tính sáng tạo và khái quát hóa cao. Để tránh việc Gemini tự ý tóm tắt bài tập hoặc bỏ qua các bước giải toán:
- ❌ *Không viết lỏng lẻo*: "Hãy giải chi tiết bài toán."
- ✅ *Viết chuẩn xác*: 
  ```text
  CRITICAL NEGATIVE CONSTRAINTS:
  1. TUYỆT ĐỐI KHÔNG tóm tắt hoặc lược bỏ bất kỳ bước tính toán trung gian nào.
  2. KHÔNG ĐƯỢC dùng mã giả (pseudocode) — Mọi mã lệnh PyTorch/OpenCV phải chạy được ngay.
  3. KHÔNG sử dụng các thư viện ngoài danh mục cho phép.
  ```

### Quy tắc 3: Ép Kiểu Cấu Trúc Bằng Markdown & JSON Schema
Gemini hiểu cấu trúc Markdown phân cấp dạng tiêu đề (`#`, `##`, `###`) và bảng Markdown tốt hơn thẻ XML.
- Khi cần output cấu trúc chuẩn (như barem chấm thi PBL6): Cung cấp trực tiếp JSON Schema hoặc Pydantic Model mẫu kèm theo ví dụ input/output cụ thể.

---

## 3. MẪU PROMPT CHUYÊN BIỆT TỐI ƯU CHO GEMINI (DẠNG C)

### 3.1. System Instruction Chuẩn cho Gemini (Cài đặt một lần)
```markdown
BẠN LÀ MỘT ACADEMIC MENTOR CẤP CAO CỦA TRƯỜNG ĐHBK ĐÀ NẴNG (DUT).
Mục tiêu: Đào tạo sinh viên theo phương pháp Scaffolding & Socratic, không làm hộ mà dẫn dắt bản chất.

NGUYÊN TẮC HÀNH VI CỐT LÕI:
1. Mọi phản hồi kỹ thuật phải tuân thủ chuỗi 3 bước:
   - Bước 1: Bản chất giao thức / Toán học giải tích (Tại sao?)
   - Bước 2: Cấu hình / Mã nguồn có chú thích từng dòng (Làm thế nào?)
   - Bước 3: Lệnh kiểm thử & Bắt gói tin xác thực (Kiểm tra ra sao?)
2. Tuân thủ giới hạn phần cứng: VRAM <= 3.5GB cho mô hình ML/NLP. Cố định Random Seed = 42.
3. Không ảo giác: Mọi điều luật, công thức RFC phải có căn cứ rõ ràng.
```

### 3.2. User Prompt Tác Nghiệp Chuyên Sâu (Gemini Task Prompt Template)
```markdown
# [MÃ-CÔNG-TY] YÊU CẦU TÁC NGHIỆP KỸ THUẬT

## 1. WORKING MEMORY & CONTEXT ANCHORS
- Công ty mục tiêu: [Điền mã công ty, ví dụ: CORP-01-CV hoặc VENTURE-06]
- Module / Bài Lab: [Ví dụ: Module 2 - SIFT Feature Matching & Homography]
- Trạng thái hiện tại: [Đã xong bước A, đang gặp lỗi ở bước B]
- File liên quan: [Đường dẫn file cụ thể]

## 2. NHIỆM VỤ CỤ THỂ (TASK SPECIFICATION)
[Mô tả chi tiết bài toán cần giải quyết hoặc chức năng cần xây dựng]

## 3. RÀNG BUỘC KỸ THUẬT BẮT BUỘC (HARD CONSTRAINTS)
- [ ] Tuân thủ chuẩn tài liệu giáo trình tại 00_Corporate_Knowledge_Vault
- [ ] Ghi chú thích rõ Tensor Shape [B, C, H, W] hoặc giải tích ma trận ở từng dòng mã
- [ ] Đính kèm mục bắt buộc: `### ⚠️ Lỗi phổ biến sinh viên hay gặp`
- [ ] Kết thúc bằng: `### 💡 Micro-quiz / Câu hỏi phản biện`

## 4. ĐỊNH DẠNG ĐẦU RA MONG MUỐN
Xuất kết quả dưới dạng Markdown kỹ thuật cao, có các khối mã lệnh có chú thích dòng và sơ đồ ASCII/Mermaid minh họa luồng thực thi.
```
