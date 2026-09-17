# 🧠 ĐẶC TẢ QUẢN TRỊ BỘ NHỚ LÀM VIỆC & NGÂN SÁCH NGỮ CẢNH AGENT
## Agent Working Memory Specification & Context Budgeting Protocol (AWMS-01)

> **Mã quy chuẩn:** `SPEC-MEMORY-01` | **Khối chuyên trách:** `03_Memory_and_Context_Ops`  
> **Chuyên viên phụ trách:** Agent `CMO-03` (Cognitive Memory Operator)  
> **Áp dụng cho:** Toàn bộ AI Agents tác nghiệp trong Hệ sinh thái School Holdings

---

## 1. MÔ HÌNH PHÂN CẤP BỘ NHỚ AGENT (3-TIER MEMORY ARCHITECTURE)

Để ngăn chặn tình trạng suy giảm trí nhớ (Context Degradation) và ngộ độc ngữ cảnh (Context Poisoning) trong các phiên làm việc dài, hệ thống phân chia bộ nhớ của Agent thành 3 vùng tách biệt:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  TIER 1: VÙNG BỘ NHỚ ĐIỀU HÀNH BẤT BIẾN (FIXED SYSTEM PROMPT)           │
│  ⭐ Identity, Hard Rules, Seed 42, VRAM Limit, Academic Tone            │
│  📏 Ngân sách: ~1.500 tokens (Cố định, không bị nén)                   │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  TIER 2: VÙNG BỘ NHỚ LÀM VIỆC TẠM THỜI (WORKING MEMORY / SCRATCHPAD)    │
│  ⭐ Active Task, State Snapshot, Các biến số trung gian, File đang mở    │
│  📏 Ngân sách: ~3.000 tokens (Cập nhật liên tục ở mỗi turn)            │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  TIER 3: VÙNG TRUY XUẤT THEO NHU CẦU (ON-DEMAND EPISODIC & LONG-TERM)  │
│  ⭐ Tài liệu giáo trình, Source Code, CSDL SQLite (Chỉ nạp khi cần)    │
│  📏 Ngân sách: Linh hoạt (Tùy thuộc độ lớn task)                       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. CẤU TRÚC BẢN CHỤP TRẠNG THÁI BỘ NHỚ (STATE SNAPSHOT SCHEMA)

Ở mỗi prompt chuyển giao hoặc khi chuyển pha công việc, Agent PHẢI duy trì một khối **Working Memory Snapshot** có cấu trúc chuẩn hóa để neo giữ tư duy:

### 2.1. Cấu trúc XML cho Claude (`<working_memory_snapshot>`)
```xml
<working_memory_snapshot>
  <session_meta>
    <company_id>VENTURE-06-PBL6</company_id>
    <academic_week>Week 1</academic_week>
    <lead_agent>MLR-02</lead_agent>
  </session_meta>
  
  <active_task_context>
    <goal>Xây dựng dịch vụ BM25Okapi và chuẩn hóa tokenization tiếng Việt</goal>
    <current_subtask>Tích hợp pyvi và viết 4 smoke tests kiểm tra</current_subtask>
    <active_files>
      <file status="modified">Project/app/services/bm25_service.py</file>
      <file status="read_only">02_Domain_and_Specifications/02_TECHNICAL_SPECIFICATIONS.md</file>
    </active_files>
  </active_task_context>

  <technical_state_variables>
    <variable name="BM25_K1">1.5</variable>
    <variable name="BM25_B">0.75</variable>
    <variable name="VRAM_BUDGET_REMAINING">3.5GB</variable>
  </technical_state_variables>

  <unresolved_blockers>
    <blocker severity="low">Cần thêm stopword tiếng Việt chuyên ngành luật</blocker>
  </unresolved_blockers>
</working_memory_snapshot>
```

### 2.2. Cấu trúc Markdown / JSON cho Gemini (`[WORKING_MEMORY_SNAPSHOT]`)
```markdown
```json
{
  "working_memory_snapshot": {
    "company_id": "CORP-01-CV",
    "academic_week": 1,
    "active_task": "Triển khai Sobel Filter từ scratch bằng NumPy",
    "in_memory_tensor_shapes": {
      "input_image": [1, 3, 512, 512],
      "grayscale": [1, 1, 512, 512],
      "sobel_kernel_x": [3, 3]
    },
    "completed_checkpoints": ["Đọc ảnh RGB", "Chuyển grayscale"],
    "current_blocker": null
  }
}
```
```

---

## 3. NGUYÊN TẮC NGÂN SÁCH NGỮ CẢNH (TOKEN ECONOMY RULES)

1. **Nguyên tắc "Just-In-Time Ingestion" (Nạp đúng lúc)**:
   - Tuyệt đối không đọc toàn bộ thư mục nếu task chỉ yêu cầu sửa 1 hàm trong 1 file.
   - Luôn sử dụng lệnh đọc file có giới hạn dòng (`StartLine` và `EndLine`) đối với các file trên 500 dòng.
2. **Nguyên tắc "Purge Context Pollution" (Thanh lọc rác ngữ cảnh)**:
   - Nếu trong cuộc hội thoại xuất hiện đoạn code bị lỗi hoặc giải thích sai, Agent ca sau **KHÔNG ĐƯỢC** lặp lại đoạn code sai đó.
   - Thay vào đó, ghi đè biến trạng thái bằng giải pháp chuẩn xác và đánh dấu `[DEPRECATED_SNIPPET]` để mô hình không bị thiên kiến chú ý (Attention Bias) vào lỗi cũ.
3. **Chiến lược Nén Ngữ Cảnh (Context Compaction)**:
   - Khi lịch sử hội thoại vượt quá 30 lượt trao đổi (hoặc khi token tiêu thụ chạm 40% giới hạn), Agent phải chủ động kích hoạt quy trình tóm tắt:
     $$\text{Lịch sử hội thoại 30 turns} \xrightarrow{\text{Compaction}} \text{1 Snapshot mục ## Last Session trong STATUS.md}$$
   - Mọi thông tin chi tiết được lưu vào file đĩa, giải phóng bộ nhớ RAM ngữ cảnh.
