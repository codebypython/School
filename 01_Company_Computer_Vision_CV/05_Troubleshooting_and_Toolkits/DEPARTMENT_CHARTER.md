# 📜 ĐIỀU LỆ PHÒNG CÔNG CỤ & KIỂM SOÁT SỰ CỐ (TROUBLESHOOTING & TOOLKITS DEPT)
## Phòng 05 — Công Ty Công Nghệ Thị Giác Máy Tính (CORP-01-CV)

> **Mã Phòng Ban:** `CV-DEPT-05`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (Role Handmade) & `PSD-04` (Pedagogical Systems Designer)  
> **Cấp bậc quản trị:** Cấp 2 — Vận hành kỹ thuật, công cụ chẩn đoán & ứng cứu sự cố phần cứng/mô hình AI

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `CV-DEPT-05` chịu trách nhiệm thiết lập tiêu chuẩn công cụ chẩn đoán, giám sát tài nguyên phần cứng máy tính (GPU/CUDA/VRAM), quản lý bộ công cụ tiền xử lý và gán nhãn ảnh (LabelImg, CVAT, Roboflow), và thiết lập các quy trình xử lý sự cố kinh điển trong Computer Vision:
1. **Quản lý hạ tầng tính toán & gia tốc GPU**: Cung cấp script kiểm tra tương thích CUDA, PyTorch, cuDNN, TensorRT và cơ chế dọn dẹp cache GPU.
2. **Cẩm nang ứng cứu sự cố huấn luyện & suy luận**: Chuẩn hóa quy trình khắc phục lỗi kinh điển: CUDA Out of Memory (OOM), NaN loss do gradient explosion, kênh màu BGR vs RGB, tensor stride/contiguous error khi permute.
3. **Bộ công cụ chuyển đổi & tối ưu hóa mô hình**: Hướng dẫn export PyTorch sang ONNX, TensorRT engine, quantization FP16/INT8 và profiling inference latency.

---

## 2. BỘ QUY TẮC BẤT BIẾN (DEBUGGING INVARIANTS & HARD CONSTRAINTS)
Mọi kỹ sư và sinh viên khi triển khai code CV phải tuân thủ 5 nguyên tắc bất biến sau:
1. **Nguyên tắc Quản lý VRAM Tuyệt đối (`torch.no_grad()` & Detach)**: Mọi khối mã đánh giá (evaluation, validation, test) hoặc inference bắt buộc phải bọc trong context `with torch.no_grad():`. Không bao giờ tích lũy `loss` tensor vào list mà không gọi `.item()` (tránh giữ computation graph gây rò rỉ bộ nhớ VRAM).
2. **Nguyên tắc Thứ tự Kênh Màu (Color Space Invariant)**: OpenCV đọc ảnh mặc định theo thứ tự `BGR`. PyTorch models và Matplotlib/PIL mong đợi định dạng `RGB`. Mọi hàm load ảnh phải có bước chuyển đổi rõ ràng `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` trước khi đưa vào tensor.
3. **Nguyên tắc Chuẩn hóa Dữ liệu (Normalization Protocol)**: Dữ liệu ảnh dạng `uint8` [0, 255] phải được chuyển sang `float32` [0.0, 1.0] trước khi áp dụng chuẩn hóa ImageNet mean/std (`mean=[0.485, 0.456, 0.406]`, `std=[0.229, 0.224, 0.225]`). Không chuẩn hóa hai lần.
4. **Nguyên tắc Tensor Layout & Contiguous Memory**: Khi thực hiện biến đổi kích thước ma trận bằng `.permute(0, 2, 3, 1)` hoặc `.transpose()`, bắt buộc gọi `.contiguous()` trước khi áp dụng `.view()` để tránh `RuntimeError: input is not contiguous`.
5. **Nguyên tắc Bounding Box Coordinate Format**: Mọi nhãn bounding box phải định danh rõ ràng quy ước tọa độ: `xyxy` (xmin, ymin, xmax, ymax), `xywh` (xmin, ymin, width, height) hay `cxcywh` (normalized center x, center y, w, h). Tuyệt đối cấm pha trộn quy ước.

---

## 3. BỘ LỆNH & CÔNG CỤ CHẨN ĐOÁN (DIAGNOSTIC TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Kiểm tra driver NVIDIA và tiến trình chiếm dụng VRAM
nvidia-smi
nvidia-smi --query-gpu=timestamp,name,pci.bus_id,utilization.gpu,memory.used,memory.total --format=csv -l 1

# 2. Kiểm tra tính khả dụng của CUDA và cuDNN trong môi trường Python
python -c "import torch; print(f'CUDA Available: {torch.cuda.is_available()} | Devices: {torch.cuda.device_count()} | Device Name: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"} | cuDNN: {torch.backends.cudnn.version()}')"

# 3. Chẩn đoán rò rỉ tensor VRAM trong PyTorch
python -c "import torch; print(f'Allocated: {torch.cuda.memory_allocated()/1024**2:.2f}MB | Reserved: {torch.cuda.memory_reserved()/1024**2:.2f}MB')"

# 4. Kiểm tra và xác thực file ONNX model
onnxruntime-check --model model.onnx || python -c "import onnx; model = onnx.load('model.onnx'); onnx.checker.check_model(model); print('ONNX Model is valid!')"

# 5. Profile latency của model CV với torch.profiler
python -m torch.utils.bottleneck train_cv_step.py
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
05_Troubleshooting_and_Toolkits/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── cuda_diagnostic_suite.py           # Script tự động quét phần cứng & benchmark CUDA
├── vram_leak_detector.py              # Decorator giám sát bộ nhớ GPU qua từng epoch
├── onnx_exporter_and_verifier.py      # Bộ công cụ xuất ONNX và kiểm thử sai số FP32/FP16
├── color_and_box_visualizer.py        # Utility vẽ bounding box & kiểm tra kênh RGB/BGR
└── runbooks/                          # Cẩm nang xử lý sự cố chi tiết
    ├── RUNBOOK_CUDA_OOM.md            # Khắc phục tràn bộ nhớ GPU
    ├── RUNBOOK_NAN_LOSS_EXPLOSION.md  # Khắc phục mất mát NaN / Gradient Exploding
    ├── RUNBOOK_OPENCV_DISPLAY_ERR.md  # Khắc phục ảnh bị ám xanh tím (BGR vs RGB)
    └── RUNBOOK_ONNX_EXPORT_TRAPS.md   # Khắc phục toán tử không hỗ trợ khi xuất ONNX
```

---

## 5. MẪU KHUNG CODE CHẨN ĐOÁN & ỨNG CỨU (GOLD MASTER BOILERPLATE)

### Bộ Script Chẩn đoán Phần cứng & Giám sát VRAM Chuẩn xác (`cuda_diagnostic_suite.py`)
```python
"""
GOLD MASTER: GPU & CUDA DIAGNOSTIC TOOLKIT FOR COMPUTER VISION
Tác giả: CORP-01-CV Engineering Team
Mô tả: Công cụ quét thiết bị, benchmark bộ nhớ và thu hồi VRAM an toàn.
"""

import gc
import sys
import torch
import torchvision


def run_gpu_health_check() -> dict:
    """Kiểm tra toàn diện trạng thái GPU, CUDA, cuDNN và phân bổ bộ nhớ."""
    report = {
        "python_version": sys.version.split()[0],
        "torch_version": torch.__version__,
        "torchvision_version": torchvision.__version__,
        "cuda_available": torch.cuda.is_available(),
        "gpu_count": torch.cuda.device_count() if torch.cuda.is_available() else 0,
        "devices": []
    }
    
    if not report["cuda_available"]:
        report["status"] = "WARNING: No CUDA device detected! Training will be slow on CPU."
        return report

    report["cudnn_version"] = torch.backends.cudnn.version()
    report["cudnn_enabled"] = torch.backends.cudnn.enabled

    for i in range(report["gpu_count"]):
        prop = torch.cuda.get_device_properties(i)
        alloc = torch.cuda.memory_allocated(i) / (1024 ** 2)
        reserv = torch.cuda.memory_reserved(i) / (1024 ** 2)
        total = prop.total_memory / (1024 ** 2)
        report["devices"].append({
            "device_id": i,
            "name": prop.name,
            "total_vram_mb": round(total, 2),
            "allocated_mb": round(alloc, 2),
            "reserved_mb": round(reserv, 2),
            "free_mb": round(total - reserv, 2),
            "compute_capability": f"{prop.major}.{prop.minor}"
        })
    report["status"] = "HEALTHY"
    return report


def safe_empty_cuda_cache():
    """Giải phóng toàn bộ cache không sử dụng khỏi CUDA allocator."""
    if torch.cuda.is_available():
        gc.collect()
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()
        print("[INFO] CUDA Cache cleared successfully.")


class GradientSanityCheckHook:
    """Hook kiểm tra đạo hàm để phát hiện sớm NaN / Inf trong backprop."""
    @staticmethod
    def inspect_gradients(model: torch.nn.Module) -> bool:
        for name, param in model.named_parameters():
            if param.grad is not None:
                if torch.isnan(param.grad).any():
                    print(f"[FATAL] NaN gradient detected in layer: {name}")
                    return False
                if torch.isinf(param.grad).any():
                    print(f"[FATAL] Inf gradient detected in layer: {name}")
                    return False
        return True


if __name__ == "__main__":
    health = run_gpu_health_check()
    print("=== GPU HEALTH REPORT ===")
    for k, v in health.items():
        print(f"{k}: {v}")
    safe_empty_cuda_cache()
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
Tài sản, công cụ và script thuộc `CV-DEPT-05` chỉ được xem là hoàn tất khi đạt đủ các điều kiện:
- [x] **Độ tin cậy môi trường (Environment Reliability)**: Mọi script chẩn đoán phải chạy được trên cả 2 môi trường: có GPU CUDA và chỉ có CPU mà không bị throw exception đột ngột (`AttributeError` hoặc crash).
- [x] **Xử lý triệt để VRAM**: Các runbook hướng dẫn OOM phải chỉ ra tối thiểu 4 giải pháp thực tế: giảm `batch_size`, tăng `gradient_accumulation_steps`, kích hoạt `torch.cuda.amp.autocast()`, và sử dụng `checkpointing`.
- [x] **Xác thực kênh màu 100%**: Mọi hàm load/xử lý ảnh cung cấp mẫu phải có assertion hoặc kiểm tra kích thước shape `(H, W, C)` và range `[0, 255]` hoặc `[0.0, 1.0]`.
- [x] **Được kiểm định bởi auditor**: File `DEPARTMENT_CHARTER.md` đạt điểm 100% khi chạy `scripts/holding_system_auditor.py`.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ KHẨN CẤP (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: `RuntimeError: CUDA out of memory` trong quá trình huấn luyện
- **Hiện tượng**: Quá trình train dừng đột ngột sau vài iteration hoặc ngay ở epoch đầu tiên kèm thông báo tràn VRAM.
- **Nguyên nhân gốc rễ**:
  1. `batch_size` hoặc `image_resolution` quá lớn so với dung lượng VRAM thực tế của GPU.
  2. Tích lũy computation graph: Code có dòng `history.append(loss)` thay vì `history.append(loss.item())`.
  3. Quên context `with torch.no_grad():` trong vòng lặp validation.
- **Quy trình xử lý 4 bước**:
  1. *Bước 1 (Cô lập bộ nhớ)*: Gọi `safe_empty_cuda_cache()` và kill các tiến trình Python ma đang giữ VRAM: `fuser -v /dev/nvidia*` hoặc `Get-Process python | Stop-Process` trên Windows.
  2. *Bước 2 (Kiểm tra Graph Leak)*: Rà soát toàn bộ code train loop, đảm bảo không có tensor mang graph được append vào mảng global.
  3. *Bước 3 (Bật Mixed Precision)*:
     ```python
     scaler = torch.cuda.amp.GradScaler()
     with torch.cuda.amp.autocast():
         outputs = model(inputs)
         loss = criterion(outputs, targets)
     scaler.scale(loss).backward()
     scaler.step(optimizer)
     scaler.update()
     ```
  4. *Bước 4 (Gradient Accumulation)*: Nếu batch size thực tế phải là 32 nhưng VRAM chỉ chịu được 8, đặt `batch_size=8`, chia `loss = loss / 4`, và chỉ gọi `optimizer.step()` sau mỗi 4 iterations.

### Sự cố 2: `Loss = NaN` hoặc đạo hàm phát nổ (Gradient Exploding)
- **Hiện tượng**: Loss giảm trong vài epoch đầu, sau đó bất ngờ hiển thị `nan` và accuracy rớt về 0.
- **Nguyên nhân gốc rễ**: Learning rate quá lớn; hàm loss (vd: CrossEntropy, Focal Loss, IoU Loss) gặp log của số 0 hoặc chia cho 0 (`eps` quá nhỏ); ảnh đầu vào chưa chuẩn hóa hoặc chứa giá trị NaN.
- **Quy trình xử lý**:
  1. Kiểm tra dữ liệu đầu vào: `assert not torch.isnan(images).any()`.
  2. Bổ sung Gradient Clipping ngay trước bước optimizer:
     ```python
     torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
     ```
  3. Giảm Learning Rate xuống 5 đến 10 lần, hoặc sử dụng Learning Rate Warmup trong 3 epoch đầu.

### Sự cố 3: Ảnh hiển thị bị ám xanh dương/tím (Blue Tint Bug)
- **Hiện tượng**: Khi dùng `matplotlib.pyplot.imshow(img)` ảnh người hoặc phong cảnh bị đổi màu xanh da trời kỳ dị.
- **Nguyên nhân**: Ảnh được nạp bằng `cv2.imread()`, lưu dữ liệu dạng BGR, nhưng Matplotlib diễn giải byte đầu tiên là Red.
- **Cách khắc phục chuẩn**:
  ```python
  import cv2
  import matplotlib.pyplot as plt

  # Sai:
  # img = cv2.imread("face.jpg")
  # plt.imshow(img) # Ám xanh

  # Đúng:
  img = cv2.imread("face.jpg")
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  plt.imshow(img_rgb)
  plt.axis("off")
  plt.show()
  ```
