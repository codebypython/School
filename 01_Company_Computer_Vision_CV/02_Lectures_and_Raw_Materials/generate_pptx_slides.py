"""
Script tự động sinh Slide PowerPoint (Slide_43_Pages_Pediatric_Bone_Age.pptx)
Dành cho đề tài: Hệ Thống Tự Động Đánh Giá Tuổi Xương Bằng Học Sâu Đa Phương Thức & XAI
Trực thuộc: CORP-01-CV (Viện Công nghệ Thị giác Máy tính VisionLab - ĐHBK Đà Nẵng)
Bao gồm trọn vẹn 47 slides (43 slide chuẩn + 15B, 35B, 36B, 42B)
"""

import os
import sys

# Ensure UTF-8 output on Windows consoles to prevent UnicodeEncodeError
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def build_presentation():
    try:
        from pptx import Presentation
        from pptx.util import Inches, Pt
        from pptx.dml.color import RGBColor
        from pptx.enum.text import PP_ALIGN
        from pptx.enum.shapes import MSO_SHAPE
    except ImportError:
        print("[!] Thư viện 'python-pptx' chưa được cài đặt.")
        print("[*] Để tạo tệp PPTX, vui lòng chạy: pip install python-pptx")
        return False

    prs = Presentation()
    # Chuẩn 16:9 widescreen: 13.333 x 7.5 inches
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Bảng màu Light Blue & White chuẩn y sinh
    BG_COLOR = RGBColor(255, 255, 255)       # #ffffff (Trắng tinh tế)
    DIVIDER_BG = RGBColor(240, 247, 255)     # #f0f7ff (Nền phân đoạn xanh nhạt)
    CARD_BG = RGBColor(248, 250, 252)        # #f8fafc (Nền card xám sáng / xanh băng)
    CARD_BORDER = RGBColor(186, 230, 253)    # #bae6fd (Viền card xanh nhạt Sky-200)
    TEXT_MAIN = RGBColor(15, 23, 42)         # #0f172a (Chữ chính Slate-900 sắc nét)
    TEXT_MUTED = RGBColor(51, 65, 85)        # #334155 (Chữ thân bài Slate-700)
    TEXT_SUB = RGBColor(100, 116, 139)       # #64748b (Chữ phụ Slate-500)
    ACCENT_BLUE = RGBColor(2, 132, 199)      # #0284c7 (Xanh Sky-600 y tế)
    ACCENT_DARK_BLUE = RGBColor(3, 105, 161) # #0369a1 (Xanh Sky-700 tiêu đề)
    ACCENT_GREEN = RGBColor(5, 150, 105)     # #059669 (Xanh lá lâm sàng)
    ACCENT_AMBER = RGBColor(217, 119, 6)     # #d97706 (Cam cảnh báo)
    ACCENT_RED = RGBColor(220, 38, 38)       # #dc2626 (Đỏ)
    ACCENT_PURPLE = RGBColor(99, 102, 241)   # #6366f1 (Tím)

    # Danh mục trọn vẹn 47 slides đối soát 100% với slide_content_43_pages.md
    slides_data = [
        # Slide 01
        {
            "id": "01", "type": "title",
            "tag": "TRƯỜNG ĐẠI HỌC BÁCH KHOA — ĐH ĐÀ NẴNG | KHOA CÔNG NGHỆ THÔNG TIN",
            "title": "HỆ THỐNG TỰ ĐỘNG ĐÁNH GIÁ TUỔI XƯƠNG\nTỪ ẢNH X-QUANG BÀN TAY NHI KHOA",
            "subtitle": "TIẾP CẬN HỌC SÂU ĐA PHƯƠNG THỨC & TRÍ TUỆ NHÂN TẠO CÓ THỂ GIẢI THÍCH (XAI)",
            "details": "Đơn vị: Viện VisionLab (CORP-01-CV)\nSinh viên: Sinh viên 1 & Sinh viên 2\nCố vấn: DUT Computer Vision Mentor",
            "speaker": "Sinh viên 1 (45 giây)",
            "script": "Kính thưa Thầy Cô trong Hội đồng phản biện và toàn thể các bạn sinh viên. Hôm nay, nhóm chúng em xin trân trọng báo cáo đề tài tốt nghiệp: 'Hệ thống Tự động Đánh giá Tuổi Xương từ ảnh X-quang Bàn tay Nhi khoa bằng Học Sâu Đa Phương Thức và Trí Tuệ Nhân Tạo Có Thể Giải Thích'. Đây là công trình nghiên cứu ứng dụng thị giác máy tính giải quyết bài toán định lượng y sinh thực tế trên tập dữ liệu chuẩn quốc tế RSNA gồm hơn 12.600 bệnh nhi. Sau đây, em xin phép bắt đầu phần trình bày."
        },
        # Slide 02
        {
            "id": "02", "type": "content",
            "tag": "QUẢN TRỊ DỰ ÁN & PHỐI HỢP KỸ NGHỆ",
            "title": "Phân Công Nhiệm Vụ & Đóng Góp Thực Hiện",
            "cards": [
                ("👨‍💻 SINH VIÊN 1: DATA & CLASSICAL CV LEAD", [
                    "Khảo sát lâm sàng & Kỹ nghệ dữ liệu RSNA (12.611 ca).",
                    "Pipeline Classical CV 5 bước: CLAHE, Gauss, Otsu, Morphology, Crop 512×512.",
                    "Xây dựng khối cảnh báo WHO và phát triển ứng dụng WebApp CDSS."
                ]),
                ("👨‍💻 SINH VIÊN 2: DEEP LEARNING & BENCHMARK LEAD", [
                    "Thiết kế kiến trúc Đa phương thức FiLM: f' = γ(g)⊙f + β(g).",
                    "Huấn luyện ma trận 3 mô hình đối kháng: ResNet-50, ConvNeXt, Swin-T.",
                    "Thẩm định giải thích Regression Grad-CAM và hoàn thiện bản thảo bài báo IEEE."
                ])
            ],
            "speaker": "Sinh viên 1 (30 giây)",
            "script": "Để đảm bảo tính liên tục và chất lượng kỹ nghệ cao nhất, hai thành viên trong nhóm chúng em đã phối hợp chặt chẽ: Bạn đảm nhiệm khối kiến trúc học sâu và ma trận đối đầu các mô hình, còn em tập trung vào kỹ nghệ tiền xử lý dữ liệu và đóng gói sản phẩm lâm sàng phục vụ người dùng."
        },
        # Slide 03
        {
            "id": "03", "type": "content",
            "tag": "LỘ TRÌNH BÁO CÁO HỘI ĐỒNG",
            "title": "Cấu Trúc Báo Cáo Tổng Thể (Agenda)",
            "cards": [
                ("PHẦN 1: BỐI CẢNH Y TẾ", ["Giới thiệu bài toán, tầm quan trọng dậy thì sớm/chậm phát triển, tiếp cận hồi quy đa phương thức."]),
                ("PHẦN 2: DỮ LIỆU & TIỀN XỬ LÝ", ["RSNA 12.611 ca, khảo sát EDA, phân tầng 80/10/10 và Pipeline 5 bước triệt tiêu học đường tắt."]),
                ("PHẦN 3: TAM MÃ HỌC SÂU", ["Cơ chế FiLM, đối đầu 3 trường phái: ResNet-50 vs ConvNeXt vs Swin-T, động học hội tụ."]),
                ("PHẦN 4: BENCHMARK & DEMO", ["Ma trận đối đầu, vượt SOTA, giải thích XAI Grad-CAM, cảnh báo WHO và WebApp CDSS."])
            ],
            "speaker": "Sinh viên 1 (25 giây)",
            "script": "Bài báo cáo hôm nay của chúng em được cấu trúc thành 4 phần logic chặt chẽ: Đi từ bài toán lâm sàng, giải pháp làm sạch dữ liệu X-quang, đến thế trận thực nghiệm đối đầu giữa 3 trường phái mô hình lớn nhất hiện nay, và cuối cùng là giải thích quyết định bằng XAI và demo ứng dụng thực tế."
        },
        # Slide 04
        {
            "id": "04", "type": "divider", "part": "PHẦN 1",
            "title": "GIỚI THIỆU BÀI TOÁN & BỐI CẢNH LÂM SÀNG Y TẾ",
            "speaker": "Sinh viên 1 (10 giây)",
            "script": "Em xin phép đi vào Phần 1: Giới thiệu bài toán và bối cảnh lâm sàng của đánh giá tuổi xương nhi khoa."
        },
        # Slide 05
        {
            "id": "05", "type": "content",
            "tag": "BỐI CẢNH Y HỌC & ĐỘNG LỰC NGHIÊN CỨU",
            "title": "Tầm Quan Trọng Của Đánh Giá Tuổi Xương Trong Nhi Khoa",
            "cards": [
                ("⚠️ DẬY THÌ SỚM (PRECOCIOUS PUBERTY)", [
                    "Tuổi xương vượt trước tuổi khai sinh (> 1 năm).",
                    "Các đĩa sụn tiếp hợp cốt hóa và đóng kín quá sớm.",
                    "Trẻ bị thấp lùn vĩnh viễn khi bước vào tuổi trưởng thành."
                ]),
                ("⚠️ CHẬM PHÁT TRIỂN (GROWTH DELAY)", [
                    "Tuổi xương tụt hậu so với tuổi khai sinh (< -1 năm).",
                    "Do thiếu hụt hormone tăng trưởng GH hoặc suy giáp bẩm sinh.",
                    "Cần phát hiện sớm trong 'giai đoạn vàng' để tiêm bù hormone."
                ]),
                ("🏥 ÁP LỰC LÂM SÀNG THỦ CÔNG", [
                    "Lật sách GP Atlas hoặc chấm TW3 tốn 15–20 phút/ca bệnh.",
                    "Sai số chủ quan giữa các bác sĩ lên tới 0.5 – 1.2 năm.",
                    "Hệ thống AI định lượng chính xác trong 15ms hỗ trợ bác sĩ kịp thời."
                ])
            ],
            "speaker": "Sinh viên 1 (50 giây)",
            "script": "Kính thưa Thầy Cô, trong y học nhi khoa, tuổi khai sinh không thể hiện được mức độ trưởng thành thực tế. Một đứa trẻ 8 tuổi có thể mang khung xương của một người 11 tuổi nếu bị dậy thì sớm, khiến các đĩa sụn đóng lại sớm và vĩnh viễn không thể cao thêm. Ngược lại, nếu trẻ bị thiếu hormone GH, tuổi xương sẽ bị tụt hậu. Một hệ thống AI định lượng chính xác trong vài mili-giây là nhu cầu cấp thiết."
        },
        # Slide 06
        {
            "id": "06", "type": "content",
            "tag": "ĐỊNH NGHĨA BÀI TOÁN & PHƯƠNG PHÁP LUẬN",
            "title": "Phạm Vi Nghiên Cứu & Tiếp Cận Đa Phương Thức",
            "cards": [
                ("🎯 ĐỐI TƯỢNG NGHIÊN CỨU", [
                    "Ảnh X-quang tư thế sau - trước (PA) bàn tay và cổ tay trái.",
                    "Độ tuổi bệnh nhi: Từ 1 đến 228 tháng tuổi (0 – 19 tuổi).",
                    "Biến lâm sàng 1D: Giới tính sinh học bệnh nhi (Nam = 1, Nữ = 0).",
                    "Bé gái cốt hóa xương sớm hơn bé trai 1.5 – 2 năm."
                ]),
                ("💡 ĐỘT PHÁ: HỒI QUY ĐA PHƯƠNG THỨC", [
                    "Bác bỏ phân loại: Quá trình cốt hóa biến thiên liên tục từng milimét.",
                    "Hồi quy liên tục (Regression): Dự đoán số thực ŷ ∈ [1, 228] tháng.",
                    "Cơ chế FiLM: Giới tính trực tiếp điều biến các kênh đặc trưng thị giác."
                ])
            ],
            "speaker": "Sinh viên 1 (40 giây)",
            "script": "Điểm sáng tạo cốt lõi của đề tài nằm ở việc định nghĩa bài toán dưới góc độ Hồi quy Đa phương thức. Vì sự phát triển của sụn là một hàm số liên tục biến thiên theo thời gian, mô hình của chúng em tích hợp song song cả tín hiệu ảnh X-quang 2D và biến giới tính 1D để dự đoán trực tiếp số tháng tuổi của bệnh nhi."
        },
        # Slide 07
        {
            "id": "07", "type": "divider", "part": "PHẦN 2",
            "title": "DỮ LIỆU LÂM SÀNG & TIỀN XỬ LÝ ẢNH CỔ ĐIỂN (CLASSICAL CV)",
            "speaker": "Sinh viên 1 (10 giây)",
            "script": "Tiếp theo, em xin phép trình bày Phần 2: Dữ liệu lâm sàng và Pipeline tiền xử lý ảnh cổ điển 5 bước."
        },
        # Slide 08
        {
            "id": "08", "type": "content",
            "tag": "GIẢI PHẪU HỌC LÂM SÀNG NHI KHOA",
            "title": "Tiến Trình Cốt Hóa Sinh Học Trên Phim X-Quang Bàn Tay",
            "cards": [
                ("🦴 VÙNG 8 XƯƠNG CỔ TAY (CARPALS)", [
                    "Xuất hiện tuần tự từ sơ sinh đến 7 tuổi.",
                    "Khởi đầu: Xương cả (Capitate) & xương móc (Hamate).",
                    "Tiếp theo: Xương tháp, nguyệt, thang, thê và cuối cùng là xương đậu.",
                    "Ở trẻ sơ sinh: Cổ tay là sụn trong suốt chưa cản quang."
                ]),
                ("⚡ ĐĨA SỤN TIẾP HỢP (EPIPHYSEAL PLATES)", [
                    "Nằm giữa thân xương và chỏm đốt ngón tay.",
                    "Nở rộng và biến động mạnh nhất ở tuổi dậy thì.",
                    "Khép kín hoàn toàn (hợp nhất xương) khi trưởng thành sinh lý.",
                    "AI phải phân giải được kích thước biến thiên từng milimét."
                ])
            ],
            "speaker": "Sinh viên 1 (45 giây)",
            "script": "Trên phim X-quang bàn tay, hai vùng giải phẫu mang tính quyết định là cụm 8 xương cổ tay và các đĩa sụn tiếp hợp ở khớp đốt ngón tay. Ở trẻ sơ sinh, cổ tay chỉ là sụn trong suốt; theo thời gian, các hạt xương mới lần lượt xuất hiện và các đĩa sụn dần khép kín lại. Mô hình học sâu phải có năng lực phân giải được sự thay đổi kích thước milimét này qua từng độ tuổi."
        },
        # Slide 09
        {
            "id": "09", "type": "content",
            "tag": "TẬP DỮ LIỆU CHUẨN QUỐC TẾ",
            "title": "Bộ Dữ Liệu Y Tế Thật RSNA Pediatric Bone Age Challenge",
            "cards": [
                ("🏥 NGUỒN DỮ LIỆU Y TẾ", [
                    "Quy mô: 12.611 ca bệnh nhi thật.",
                    "Đóng góp bởi: Hiệp hội Điện quang Bắc Mỹ (RSNA).",
                    "Thu thập từ Stanford Children's Hospital và Children's Hospital Colorado."
                ]),
                ("📈 PHÂN PHỐI ĐỘ TUỔI", [
                    "Trải dài từ 1 đến 228 tháng (0 – 19 tuổi).",
                    "Trung bình: μ = 127.32 tháng (~10.6 tuổi).",
                    "Độ lệch chuẩn: σ = 41.18 tháng."
                ]),
                ("🎯 NHÃN CHUẨN VÀNG (GROUND TRUTH)", [
                    "100% ca bệnh có hội đồng chuyên gia chẩn đoán hình ảnh đối soát chéo.",
                    "Radiologist Consensus chuẩn mực quốc tế cao nhất."
                ])
            ],
            "speaker": "Sinh viên 1 (35 giây)",
            "script": "Nhóm sử dụng bộ dữ liệu chuẩn quốc tế RSNA gồm 12.611 ca bệnh thật. Dữ liệu trải dài từ trẻ sơ sinh 1 tháng tuổi đến thanh thiếu niên 19 tuổi, với tuổi trung bình là 10.6 tuổi, phản ánh trọn vẹn sự biến thiên sinh học của cộng đồng nhi khoa."
        },
        # Slide 10
        {
            "id": "10", "type": "content",
            "tag": "THỐNG KÊ MÔ TẢ & KHẢO SÁT LÂM SÀNG",
            "title": "Phân Tích Thống Kê Lâm Sàng (Clinical EDA)",
            "cards": [
                ("⚖️ CƠ CẤU GIỚI TÍNH CÂN BẰNG", [
                    "Nam: 54.18% (6.833 ca bệnh nhi).",
                    "Nữ: 45.82% (5.778 ca bệnh nhi).",
                    "Tỷ lệ cân bằng lý tưởng, không bị lệch giới tính."
                ]),
                ("📊 PHÂN PHỐI ĐỘ TUỔI ĐỐI XỨNG", [
                    "Đường cong hình chuông tiệm cận phân phối chuẩn Gauss.",
                    "Mật độ tập trung cao nhất ở giai đoạn 8 – 14 tuổi.",
                    "Tạo điều kiện lý tưởng cho thuật toán hồi quy liên tục."
                ])
            ],
            "speaker": "Sinh viên 1 (30 giây)",
            "script": "Kết quả khảo sát thống kê cho thấy tỷ lệ giới tính trong tập dữ liệu đạt mức cân bằng lý tưởng: 54% nam và 46% nữ. Đường cong phân bố tuổi xương có dạng hình chuông cân đối, tạo điều kiện thuận lợi để mô hình học không bị thiên lệch về một nhóm tuổi cục bộ."
        },
        # Slide 11
        {
            "id": "11", "type": "content",
            "tag": "KỸ NGHỆ PHÂN TẦNG CHỐNG RÒ RỈ",
            "title": "Chiến Lược Phân Tầng Cố Định (Stratified Split 80/10/10)",
            "cards": [
                ("🚫 BÁC BỎ RANDOM SPLIT", [
                    "Tuyệt đối không chia ngẫu nhiên để tránh rò rỉ phân phối.",
                    "Phân chia kết hợp 10 phân vị tuổi (Deciles) × 2 Giới tính = 20 Bins chuẩn."
                ]),
                ("📦 PHÂN CHIA 3 TẬP ĐỘC LẬP", [
                    "Train Set (80.0%): 10.088 ca.",
                    "Val Set (10.0%): 1.261 ca.",
                    "Test Set (10.0%): 1.262 ca (Đóng băng hoàn toàn)."
                ]),
                ("🔒 ĐÓNG BĂNG DỮ LIỆU", [
                    "Lưu trữ cố định trong tệp train_stratified.csv.",
                    "Đảm bảo 100% tính tái lặp khoa học và công bằng giữa 3 mô hình."
                ])
            ],
            "speaker": "Sinh viên 1 (40 giây)",
            "script": "Để đảm bảo tính trung thực tuyệt đối trong khoa học, nhóm không chia tập ngẫu nhiên mà thực hiện phân tầng cố định theo 10 phân vị tuổi kết hợp giới tính. Tập Test gồm đúng 1.262 ca bệnh được đóng băng hoàn toàn, đảm bảo cả 3 mô hình sau này đều phải vượt qua cùng một bài kiểm tra độc lập và công bằng."
        },
        # Slide 12
        {
            "id": "12", "type": "content",
            "tag": "CƠ CẤU MẪU THEO LỨA TUỔI SINH LÝ",
            "title": "Phân Bổ Bệnh Nhi Theo 4 Giai Đoạn Phát Triển",
            "cards": [
                ("1. NHŨ NHI (< 3T)", ["782 ca (6.2%)", "Cổ tay chủ yếu là sụn trong suốt chưa cản quang; khe khớp rất rộng."]),
                ("2. NHI ĐỒNG (3-8T)", ["2.415 ca (19.1%)", "Xuất hiện tuần tự 8 hạt xương cổ tay; các tâm cốt hóa nở to đều đặn."]),
                ("3. TIỀN DẬY THÌ (8-12T)", ["4.120 ca (32.7%)", "Đĩa sụn tiếp hợp nở rộng tối đa; biến động hình thái sụn mạnh nhất."]),
                ("4. VỊ THÀNH NIÊN (12-19T)", ["5.294 ca (42.0%)", "Hợp nhất thân xương và chỏm; đóng hoàn toàn khe sụn tiếp hợp."])
            ],
            "speaker": "Sinh viên 1 (35 giây)",
            "script": "Bảng số liệu cho thấy mật độ dữ liệu tập trung cao nhất ở giai đoạn tiền dậy thì và vị thành niên, chiếm gần 75% dữ liệu. Đây chính là giai đoạn các đĩa sụn có biến động mạnh nhất và cũng là nhóm đối tượng có nhu cầu thăm khám nội tiết cao nhất trong thực tế."
        },
        # Slide 13
        {
            "id": "13", "type": "content",
            "tag": "VẤN ĐỀ KỸ THUẬT THỊ GIÁC",
            "title": "3 Thách Thức Quang Học Lớn Trên Ảnh X-Quang Gốc",
            "cards": [
                ("1. VIỀN ĐEN MÁY QUÉT QUÁ LỚN", [
                    "Chiếm từ 30% đến 40% diện tích khung hình thô.",
                    "Lãng phí năng lực tính toán và bộ nhớ VRAM của GPU.",
                    "Làm loãng trọng số attention và phân tán trường tiếp nhận."
                ]),
                ("2. ĐỘ TƯƠNG PHẢN ĐĨA SỤN THẤP", [
                    "Đĩa sụn chứa ít canxi nên độ cản quang kém, chìm trong mô mềm.",
                    "Khó phân biệt ranh giới sụn chưa cốt hóa và mô xung quanh.",
                    "Cần tăng cường sáng cục bộ mà không làm cháy xương đặc."
                ]),
                ("3. DỊ VẬT KIM LOẠI & CHỮ L/R", [
                    "Ký hiệu kim loại L/R cản quang cực mạnh (pixel trắng toát).",
                    "Nguy cơ Shortcut Learning: Mạng học đường tắt vào chữ thay vì sụn.",
                    "Bắt buộc phải xóa sạch dị vật trước khi đưa vào mô hình!"
                ])
            ],
            "speaker": "Sinh viên 1 (45 giây)",
            "script": "Khi quan sát ảnh X-quang gốc, nhóm phát hiện 3 trở ngại kỹ thuật lớn: Thứ nhất, viền đen máy quét chiếm gần một nửa khung hình. Thứ hai, các đĩa sụn tiếp hợp rất mờ do cản quang kém. Thứ ba, các ký hiệu kim loại chữ L hoặc R có độ sáng rất gắt, nếu không xử lý, mô hình sẽ học 'đường tắt' vào chữ kim loại thay vì nhìn vào sụn xương."
        },
        # Slide 14
        {
            "id": "14", "type": "content",
            "tag": "GIẢI PHÁP TIỀN XỬ LÝ CHUẨN HÓA",
            "title": "Pipeline Chuẩn Hóa Thị Giác Cổ Điển 5 Bước (Classical CV)",
            "cards": [
                ("Quy trình 5 bước Classical CV tuần tự:", [
                    "Bước 1: CLAHE (clipLimit=3.0, tileGridSize=8×8) cân bằng sáng cục bộ.",
                    "Bước 2: Lọc Gaussian (5×5, σ=1.0) khử nhiễu lượng tử phim X-quang.",
                    "Bước 3: Ngưỡng tự động Otsu nhị phân hóa tách bàn tay khỏi nền.",
                    "Bước 4: Toán tử Hình thái học Morphology Open/Close xóa sạch chữ L/R kim loại.",
                    "Bước 5: Bounding Box Contours Crop cắt sát biên bàn tay + viền an toàn 2% đưa về 512×512."
                ]),
                ("Kết quả kỹ nghệ đạt được:", [
                    "Triệt tiêu 100% hiện tượng học đường tắt viền đen và chữ kim loại.",
                    "Làm nổi rõ viền sụn tiếp hợp và hạt xương cổ tay.",
                    "Toàn bộ 12.611 ảnh được xuất cache sẵn sàng huấn luyện tốc độ cao."
                ])
            ],
            "speaker": "Sinh viên 1 (50 giây)",
            "script": "Để khắc phục triệt để các thách thức trên, nhóm xây dựng pipeline tiền xử lý 5 bước: Dùng CLAHE cân bằng sáng cục bộ, lọc Gauss khử nhiễu lượng tử, thuật toán Otsu nhị phân hóa tách bàn tay, phép toán hình thái học xóa tan chữ kim loại, và thuật toán tìm đường bao lớn nhất để cắt đúng vùng bàn tay rồi đưa về chuẩn 512x512. Toàn bộ 12.611 ảnh sạch được xuất sẵn làm bộ đệm cache, giúp việc huấn luyện sau này diễn ra với tốc độ tối đa."
        },
        # Slide 15
        {
            "id": "15", "type": "divider", "part": "PHẦN 3",
            "title": "THẾ TRẬN TAM MÃ HỌC SÂU ĐỐI ĐẦU & THUẬT TOÁN TỐI ƯU",
            "speaker": "Sinh viên 2 (10 giây)",
            "script": "Tiếp theo, em xin phép đại diện nhóm báo cáo Phần 3: Ma trận mô hình học sâu đối đầu và các thuật toán tối ưu."
        },
        # Slide 15B
        {
            "id": "15B", "type": "content",
            "tag": "BỨC TRANH TOÀN CẢNH Y VĂN QUỐC TẾ",
            "title": "Tiến Trình Phát Triển Các Phương Pháp Học Máy Trong BAA",
            "cards": [
                ("1. CỔ ĐIỂN CNNs (2017-2019)", [
                    "VGG-16, ResNet-50 (Larson et al. 2018: 7.30m).",
                    "Hạn chế: Ghép nối 1-bit giới tính thô sơ bị triệt tiêu gradient; trường nhìn 3×3 cục bộ."
                ]),
                ("2. ATTENTION CNNs (2020-2022)", [
                    "Residual Attention, Dual-branch ROI (Wu et al. 2021: 6.60m).",
                    "Ưu điểm: Tập trung đĩa sụn; Hạn chế: Kiến trúc phức tạp, khó hội tụ."
                ]),
                ("3. VISION TRANSFORMERS (2022-2024)", [
                    "ViT, Swin Transformer v2 (Kasani et al. 2023: 6.38m).",
                    "Ưu điểm: Nắm bắt quan hệ tầm xa; Hạn chế: Thiếu Inductive Bias, tiêu tốn VRAM."
                ]),
                ("4. MODERN CONVNETS + FiLM (2023-NAY)", [
                    "ConvNeXt-V2 kết hợp FiLM (Pan et al. 2024: 6.30m, VisionLab DUT: 6.26m).",
                    "Depthwise 7×7 mở rộng Receptive Field, bảo tồn Inductive Bias, điều chế affine."
                ])
            ],
            "speaker": "Sinh viên 2 (50 giây)",
            "script": "Kính thưa Hội đồng, để giải quyết bài toán tuổi xương, y văn thế giới đã trải qua 4 làn sóng công nghệ lớn: từ các mạng CNN kinh điển như VGG/ResNet, đến CNN tích hợp cơ chế chú ý Attention, tiếp theo là làn sóng Vision Transformer với Swin-T, và gần đây nhất là xu hướng hiện đại hóa CNN với ConvNeXt kết hợp cơ chế điều biến đặc trưng FiLM. Nhóm chúng em đã thiết kế một thế trận thực nghiệm bao quát cả 3 trường phái tiêu biểu, đặc biệt cải tiến cơ chế hợp nhất đa phương thức FiLM để giới tính sinh học trực tiếp can thiệp vào các kênh đặc trưng thị giác."
        },
        # Slide 16
        {
            "id": "16", "type": "content",
            "tag": "KIẾN TRÚC HỢP NHẤT ĐA PHƯƠNG THỨC ĐỘT PHÁ",
            "title": "Sơ Đồ Khối Vận Hành Hệ Thống & Cơ Chế Điều Biến FiLM",
            "cards": [
                ("1. NHÁNH THỊ GIÁC 2D & LÂM SÀNG 1D", [
                    "Nhánh 2D: Ảnh sạch 512×512×3 → Visual Backbone → Vector đặc trưng f_img ∈ ℝ^D.",
                    "Nhánh 1D: Giới tính g ∈ {0, 1} → Gender MLP → Vector e_g ∈ ℝ^32."
                ]),
                ("2. ĐIỀU BIẾN TUYẾN TÍNH FiLM", [
                    "Chiếu vector giới tính ra 2 tham số affine: γ(g), β(g) = Linear(e_g).",
                    "Điều biến trực tiếp kênh thị giác: f' = γ(g) ⊙ f_img + β(g).",
                    "Khắc phục 100% hiện tượng tiêu biến gradient của phép Naive Concat!"
                ]),
                ("3. ĐẦU HỒI QUY PHÂN CẤP", [
                    "Linear(D → 1024) → BatchNorm → ReLU → Linear(1024 → 512) → Linear(512 → 1).",
                    "Dự đoán trực tiếp số tháng tuổi liên tục ŷ."
                ])
            ],
            "speaker": "Sinh viên 2 (50 giây)",
            "script": "Thay vì chỉ ghép nối đơn thuần giới tính vào cuối mạng như các nghiên cứu cũ khiến tín hiệu giới tính bị chìm nghỉm, nhóm chúng em ứng dụng cơ chế FiLM - Feature-wise Linear Modulation. Vector giới tính sinh học sẽ sinh ra hai hệ số affine gamma và beta để co giãn và tịnh tiến trực tiếp các kênh đặc trưng thị giác. Nhờ đó, cùng một hình thái sụn nhưng nếu là bé gái thì mô hình sẽ tự động kích hoạt ngưỡng cốt hóa sớm hơn bé trai, đúng chuẩn quy luật sinh học."
        },
        # Slide 17
        {
            "id": "17", "type": "content",
            "tag": "TRƯỜNG PHÁI 1: RESIDUAL CNN CỔ ĐIỂN",
            "title": "Mô Hình 1: Residual Bottleneck CNN (ResNet-50)",
            "cards": [
                ("📐 KIẾN TRÚC CỐT LÕI", [
                    "Tác giả: He et al. (Microsoft Research, 2015).",
                    "Cơ chế cốt lõi: Residual Skip Connections (y = ℱ(x) + x).",
                    "Bề mặt hàm mất mát phẳng và ổn định, triệt tiêu tiêu biến gradient qua 50 tầng."
                ]),
                ("⚙️ THÔNG SỐ KỸ NGHỆ", [
                    "Tổng số tham số: 26.17 triệu tham số.",
                    "Vector đặc trưng hình ảnh GAP: 2.048 chiều (2048D).",
                    "Kích thước Checkpoint: 324.0 MB."
                ]),
                ("💡 VAI TRÒ TRONG ĐỀ TÀI", [
                    "Đóng vai trò là Mô hình Nền tảng (Anchor Baseline) chuẩn mực.",
                    "Được nâng cấp bằng khối điều biến FiLM và đầu hồi quy phân cấp.",
                    "Kiểm chứng mức độ tiết kiệm sai số khi chuyển sang FiLM."
                ])
            ],
            "speaker": "Sinh viên 2 (40 giây)",
            "script": "Đại diện đầu tiên trong thế trận thực nghiệm là ResNet-50. Đây là kiến trúc CNN chuẩn mực nhất trong thị giác máy tính với cấu trúc kết nối tắt phần dư Residual Skip Connections, tạo ra bề mặt mất mát cực kỳ ổn định. Khối Bottleneck cuối cùng trích xuất vector đặc trưng không gian 2.048 chiều rất giàu ngữ nghĩa."
        },
        # Slide 18
        {
            "id": "18", "type": "content",
            "tag": "LỰA CHỌN THAM SỐ TOÁN HỌC",
            "title": "Tại Sao ResNet-50 Là 'Điểm Rơi Vàng' (Sweet Spot)?",
            "cards": [
                ("SO SÁNH CÁC BIẾN THỂ RESNET", [
                    "ResNet-18 / 34: Chỉ có 512 chiều đặc trưng, quá nông cho sụn tiếp hợp.",
                    "ResNet-50: Khối Bottleneck (1×1 → 3×3 → 1×1), 2048D, 25.6M params, vừa vặn hoàn hảo với 10.000 ảnh y tế.",
                    "ResNet-101 / 152: 44.5M – 60.2M params, quá nặng, dễ bị Overfitting."
                ]),
                ("CHỨNG MINH TOÁN HỌC GRADIENT", [
                    "Đạo hàm lan truyền ngược: ∂L/∂x = (∂L/∂y) · (∂ℱ/∂x + 1).",
                    "Số hạng +1 đảm bảo dòng gradient luôn lưu thông kể cả khi ∂ℱ/∂x tiệm cận 0."
                ])
            ],
            "speaker": "Sinh viên 2 (40 giây)",
            "script": "Một câu hỏi thường gặp là: Tại sao không dùng ResNet-18 hay ResNet-152? Nghiên cứu của chúng em chỉ ra rằng ResNet-18 với 512 chiều là quá nông cho các khe sụn nhỏ; trong khi ResNet-152 với hơn 60 triệu tham số lại bị thừa năng lực và dễ bị học vẹt trên tập 10.000 ảnh. ResNet-50 chính là điểm rơi vàng giữa khả năng biểu diễn và tính khái quát hóa."
        },
        # Slide 19
        {
            "id": "19", "type": "content",
            "tag": "THIẾT LẬP THỰC NGHIỆM ĐỒNG BỘ",
            "title": "Cấu Hình Huấn Luyện ResNet-50 Multimodal (FiLM)",
            "cards": [
                ("💻 PHẦN CỨNG & MÔI TRƯỜNG", [
                    "GPU: NVIDIA Tesla T4 (14.56 GB VRAM).",
                    "Môi trường: PyTorch 2.x CUDA trên Google Colab Pro.",
                    "Batch Size: 32 mẫu | Epochs: 15 vòng lặp.",
                    "Thời gian chạy thực tế: 202.1 phút (~3.37 giờ)."
                ]),
                ("🎯 HÀM MẤT MÁT HUBER LOSS", [
                    "Smooth L1 (δ = 1.0) kháng ngoại lai.",
                    "Khi lỗi nhỏ (|y - ŷ| ≤ 1): Dùng L2 đạo hàm mượt mà.",
                    "Khi lỗi lớn (|y - ŷ| > 1): Chuyển sang L1 đạo hàm hằng số, chặn bùng nổ gradient!"
                ]),
                ("⚡ BỘ TỐI ƯU & LỊCH HỌC", [
                    "AdamW (lr = 1e-4, weight_decay = 1e-4).",
                    "CosineAnnealingLR (T_max = 15).",
                    "Mixed Precision Training (AMP FP16) tăng tốc 2.1x và tiết kiệm 50% bộ nhớ."
                ])
            ],
            "speaker": "Sinh viên 2 (35 giây)",
            "script": "Mô hình được huấn luyện trên GPU Tesla T4 với 15 Epochs, sử dụng bộ tối ưu AdamW kết hợp lịch hạ tốc độ học theo hàm Cosine. Điểm nhấn là việc áp dụng hàm mất mát Huber Loss để chặn hiện tượng bùng nổ gradient từ các ca bệnh đột biến, và kỹ thuật AMP FP16 giúp tiết kiệm 50% bộ nhớ GPU."
        },
        # Slide 20
        {
            "id": "20", "type": "content",
            "tag": "TIẾN TRÌNH HỘI TỤ THỰC TẾ",
            "title": "Kết Quả Động Học Huấn Luyện ResNet-50 Multimodal",
            "cards": [
                ("📉 TIẾN TRÌNH HỘI TỤ 15 EPOCHS", [
                    "Epoch 01: Val MAE = 111.43 tháng (Khởi tạo ngẫu nhiên đầu hồi quy).",
                    "Epoch 05: Val MAE = 12.77 tháng (Lao dốc ngoạn mục nhờ tiền huấn luyện ImageNet).",
                    "Epoch 13: Đạt điểm tối ưu Val MAE = 6.82 tháng (~0.568 năm) → Lưu checkpoint tốt nhất.",
                    "Epoch 14–15: Dao động quanh mức 7.0 – 7.2 tháng với Cosine Annealing."
                ]),
                ("🔍 ĐẶC TÍNH HUẤN LUYỆN", [
                    "Đường cong huấn luyện và kiểm định bám sát nhau, không có hiện tượng Overfitting.",
                    "Lưu checkpoint chính thức: resnet50_multimodal.pth (324.0 MB)."
                ])
            ],
            "speaker": "Sinh viên 2 (45 giây)",
            "script": "Trên màn hình là đồ thị huấn luyện thực tế từ log kiểm thử. Nhờ trọng số tiền huấn luyện ImageNet kết hợp cơ chế điều chế FiLM, Val MAE giảm cực nhanh từ 111 tháng xuống 12 tháng ở epoch 5, và đạt điểm tối ưu 6.82 tháng tại epoch 13 trước khi hội tụ ổn định."
        },
        # Slide 21
        {
            "id": "21", "type": "content",
            "tag": "KIỂM THỬ ĐỘC LẬP & ABLATION STUDY",
            "title": "Đánh Giá Trên Tập Test Độc Lập (1.262 Ca) — ResNet-50",
            "cards": [
                ("📊 CHỈ SỐ TEST SET", [
                    "Test MAE: 6.47 tháng (~0.539 năm, khoảng 6 tháng 14 ngày).",
                    "Test RMSE: 8.70 tháng.",
                    "Hệ số xác định: R² = 0.9540 (95.40%).",
                    "Tốc độ thông lượng GPU: 67.5 FPS (Nhanh nhất hệ thống)."
                ]),
                ("🛡️ ĐỘ AN TOÀN LÂM SÀNG AAP", [
                    "Độ chính xác trong hạn ≤ 6 tháng: 59.7% (Cao nhất hệ thống).",
                    "Độ an toàn trong hạn ≤ 12 tháng: 84.70%."
                ]),
                ("⚡ ĐỘT PHÁ CỦA FiLM (ABLATION STUDY)", [
                    "Baseline (Naive Concat 1-bit): MAE = 7.38m.",
                    "ResNet-50 + FiLM: MAE = 6.47m.",
                    "👉 Giảm tới -12.3% sai số (tiết kiệm 0.91 tháng) nhờ cơ chế điều biến affine!"
                ])
            ],
            "speaker": "Sinh viên 2 (45 giây)",
            "script": "Khi kiểm thử trên 1.262 ca bệnh độc lập, ResNet-50 tích hợp FiLM đạt MAE 6.47 tháng, R² đạt 95.40% và tỷ lệ an toàn lâm sàng 12 tháng lên tới 84.7%. Đặc biệt, kết quả thực nghiệm cắt bỏ chỉ ra rằng cơ chế điều chế FiLM đã giúp giảm sai số tới 12.3% so với mô hình cơ sở ghép nối trực tiếp, chứng minh việc can thiệp giới tính vào tầng đặc trưng thị giác mang lại bước tiến quyết định."
        },
        # Slide 22
        {
            "id": "22", "type": "content",
            "tag": "THẨM ĐỊNH THỐNG KÊ PHẦN DƯ",
            "title": "Phân Tích Phân Bố Phần Dư Sai Số (Residual Analysis)",
            "cards": [
                ("🔍 ĐỒ THỊ PHÂN TÁN (SCATTER PLOT)", [
                    "Các điểm dự đoán bám chặt vào đường chéo lý tưởng 45°.",
                    "Đại đa số nằm gọn trong hành lang an toàn AAP ±12 tháng.",
                    "Hệ số xác định R² = 0.9540 thể hiện tính tuyến tính cao."
                ]),
                ("📊 PHÂN PHỐI GAUSS ĐỐI XỨNG", [
                    "Biểu đồ phần dư (e = y - ŷ) có dạng hình chuông cân đối quanh mốc 0.",
                    "Chứng minh mô hình hoàn toàn không bị thiên lệch (unbiased).",
                    "Tỷ số RMSE / MAE ≈ 1.34 chứng minh kiểm soát tốt các ca bệnh ngoại lai."
                ])
            ],
            "speaker": "Sinh viên 2 (35 giây)",
            "script": "Biểu đồ phân tán cho thấy các điểm chẩn đoán phân bố rất đồng đều dọc theo đường chéo lý tưởng 45 độ. Biểu đồ phần dư đối xứng hoàn hảo quanh trục số 0, chứng minh mô hình không hề bị lệch thiên kiến về việc đoán già hơn hay đoán non hơn tuổi thực."
        },
        # Slide 23
        {
            "id": "23", "type": "content",
            "tag": "TRƯỜNG PHÁI 2: MODERN PURE CNN",
            "title": "Mô Hình 2: Modern Pure CNN (ConvNeXt-V2)",
            "cards": [
                ("🌟 TRIẾT LÝ THIẾT KẾ", [
                    "Tác giả: Meta AI Research (Woo et al., 2023).",
                    "Tái cấu trúc tích chập theo chuẩn hiện đại: Học tập các ưu điểm của Vision Transformer.",
                    "Bảo tồn 100% Inductive Bias không gian của mạng tích chập."
                ]),
                ("⚙️ THÔNG SỐ KIẾN TRÚC", [
                    "Tổng tham số: 28.58 triệu tham số (29.8M gồm FiLM/Head).",
                    "Vector đặc trưng hình ảnh: 768 chiều (768D).",
                    "Kích thước Checkpoint: 341.2 MB."
                ]),
                ("🏆 VỊ THẾ TRONG HỆ THỐNG", [
                    "Ứng viên sáng giá nhất cho ngôi vị Quán quân toàn diện.",
                    "Khắc phục triệt để nhược điểm trường nhìn hẹp của ResNet-50.",
                    "Tương thích hoàn hảo với cơ chế điều biến tuyến tính FiLM."
                ])
            ],
            "speaker": "Sinh viên 2 (35 giây)",
            "script": "Đại diện thứ hai trong thế trận đối đầu là ConvNeXt-V2-Tiny. Đây là đỉnh cao của kiến trúc CNN hiện đại do Meta AI công bố, được thiết kế lại toàn diện để sở hữu tầm nhìn rộng của Transformer nhưng vẫn giữ được tốc độ và tính ổn định của mạng tích chập."
        },
        # Slide 24
        {
            "id": "24", "type": "content",
            "tag": "CẢI TIẾN TÍCH CHẬP ĐỘT PHÁ",
            "title": "3 Đột Phá Kiến Trúc Của ConvNeXt Trong Phân Tích X-Ray",
            "cards": [
                ("1. BỘ LỌC TÍCH CHẬP LỚN 7×7", [
                    "Tích chập Depthwise Separable 7×7 mở rộng Receptive Field.",
                    "Bao quát toàn bộ cấu trúc bàn tay và tương quan liên ngón mà không bị nhiễu nền."
                ]),
                ("2. KHỐI NGHỊCH ĐẢO CỔ CHAI (INVERTED BOTTLENECK)", [
                    "Mở rộng số kênh C → 4C → C.",
                    "Giữ lại trọn vẹn các chi tiết đĩa sụn siêu nhỏ trước khi nén đặc trưng."
                ]),
                ("3. CHUẨN HÓA PHẢN HỒI TOÀN CỤC (GRN)", [
                    "Global Response Normalization kết hợp LayerNorm.",
                    "Chống hiện tượng bão hòa kênh và triệt tiêu gradient hiệu quả."
                ])
            ],
            "speaker": "Sinh viên 2 (40 giây)",
            "script": "ConvNeXt mang đến 3 cải tiến vượt bậc: Bộ lọc 7x7 giúp mở rộng tầm nhìn không gian; cấu trúc nghịch đảo cổ chai giúp bảo tồn các nếp gấp sụn siêu nhỏ; và tầng chuẩn hóa GRN giúp ngăn ngừa hiện tượng bão hòa kênh, giúp gradient lưu thông mạnh mẽ hơn."
        },
        # Slide 25
        {
            "id": "25", "type": "content",
            "tag": "THIẾT LẬP THỰC NGHIỆM CONVNEXT",
            "title": "Cấu Hình Huấn Luyện ConvNeXt-Tiny Multimodal",
            "cards": [
                ("⚙️ THAM SỐ HUẤN LUYỆN", [
                    "Batch Size: 32 | Epochs: 20 vòng lặp.",
                    "Optimizer: AdamW (lr = 1e-4, weight_decay = 1e-4).",
                    "Hàm mất mát: Huber Loss (Smooth L1, δ = 1.0).",
                    "Mixed Precision: PyTorch AMP FP16."
                ]),
                ("🛡️ CHỐNG HỌC VẸT NÂNG CAO", [
                    "Stochastic Depth (Drop Path Rate = 0.1).",
                    "Ngắt ngẫu nhiên các nhánh trong khối Inverted Bottleneck.",
                    "Ép mạng học đa dạng đặc trưng sụn thay vì phụ thuộc vào một nhánh."
                ]),
                ("🔀 HỢP NHẤT ĐA PHƯƠNG THỨC", [
                    "Visual Features: 768D | Gender Embedding: 32D.",
                    "FiLM Affine: Chiếu ra γ(g), β(g) ∈ ℝ^768.",
                    "Đầu hồi quy phân cấp: 768 → 1024 → 512 → 1."
                ])
            ],
            "speaker": "Sinh viên 2 (30 giây)",
            "script": "Với ConvNeXt, chúng em bổ sung thêm cơ chế Stochastic Depth để ngắt ngẫu nhiên một số đường dẫn trong quá trình train nhằm chống Overfitting, và ghép nối vector 768 chiều với nhánh giới tính 32 chiều thành vector 800 chiều."
        },
        # Slide 26
        {
            "id": "26", "type": "content",
            "tag": "TIẾN TRÌNH HỘI TỤ CONVNEXT",
            "title": "Động Học Hội Tụ ConvNeXt-Tiny Multimodal (FiLM)",
            "cards": [
                ("📉 ĐỘNG HỌC MẤT MÁT VƯỢT TRỘI", [
                    "Hội tụ mượt mà và sâu hơn hẳn ResNet-50 nhờ bộ lọc 7×7 và GRN.",
                    "Điểm tối ưu đạt được tại Epoch 17: Val MAE = 6.18 tháng.",
                    "Lưu checkpoint tối ưu: convnext_tiny_multimodal.pth (341.2 MB).",
                    "Không xuất hiện hiện tượng bão hòa kênh hay phân kỳ gradient."
                ]),
                ("🎯 Ý NGHĨA KỸ NGHỆ", [
                    "Sự kết hợp giữa LayerNorm và Inverted Bottleneck tạo không gian biểu diễn tuyến tính lý tưởng cho FiLM.",
                    "Val MAE giảm sâu hơn ResNet-50 gần 0.64 tháng."
                ])
            ],
            "speaker": "Sinh viên 2 (30 giây)",
            "script": "Nhờ các khối chuẩn hóa hiện đại và trường tiếp nhận lớn, đường cong hàm mất mát của ConvNeXt hội tụ êm mượt hơn rõ rệt và đạt mức sai số kiểm định tối ưu 6.18 tháng, vượt trội hơn so với ResNet-50."
        },
        # Slide 27
        {
            "id": "27", "type": "content",
            "tag": "QUÁN QUÂN TOÀN HỆ THỐNG",
            "title": "Kiểm Thử ConvNeXt-Tiny Trên Tập Test — Quán Quân Toàn Hệ Thống",
            "cards": [
                ("🏆 TEST MAE QUÁN QUÂN", [
                    "MAE = 6.26 tháng (~0.521 năm, 6 tháng 8 ngày).",
                    "Kỷ lục sai số thấp nhất toàn bộ nghiên cứu.",
                    "Cắt giảm -15.2% sai số so với Baseline!"
                ]),
                ("📈 TEST RMSE & R² SCORE", [
                    "Test RMSE: 8.40 tháng (Thấp nhất hệ thống).",
                    "R² Score: 0.9571 (95.71% - Cao nhất hệ thống).",
                    "Giải thích 95.71% phương sai tuổi thực tế của bệnh nhi."
                ]),
                ("🛡️ AN TOÀN LÂM SÀNG AAP & THÔNG LƯỢNG", [
                    "Độ an toàn trong hạn ≤ 12 tháng: 86.50% (Cao nhất).",
                    "Thông lượng GPU: 55.0 FPS.",
                    "Thông lượng CPU: 1.3 FPS (Mượt nhất CPU)."
                ])
            ],
            "speaker": "Sinh viên 2 (40 giây)",
            "script": "Trên tập Test độc lập, ConvNeXt-Tiny đã chính thức xác lập vị thế quán quân với sai số MAE chỉ còn 6.26 tháng, tương đương 0.52 năm (khoảng 6 tháng 8 ngày). Hệ số tương quan R² đạt đỉnh 95.71% và tỷ lệ an toàn lâm sàng lên tới 86.5%, vượt qua mọi mô hình khác trong thế trận đối đầu."
        },
        # Slide 28
        {
            "id": "28", "type": "content",
            "tag": "BƯỚC NHẢY HIỆU NĂNG",
            "title": "Bước Tiến Vượt Bậc Của ConvNeXt So Với ResNet-50",
            "cards": [
                ("📊 BẢNG ĐỐI CHIẾU TRỰC TIẾP", [
                    "So với Baseline (ResNet Naive): MAE giảm từ 7.38m → 6.26m (Cải thiện -15.2%).",
                    "So với ResNet-50 + FiLM: MAE giảm từ 6.47m → 6.26m (Cải thiện thêm -3.2%).",
                    "RMSE giảm mạnh: 9.60m → 8.40m (Cải thiện -12.5% ngoại lai).",
                    "Tỷ lệ an toàn 12 tháng: Tăng từ 81.38% lên 86.50% (+5.12%).",
                    "Tốc độ CPU: Đạt 1.3 FPS (Nhanh hơn ResNet và Swin-T)."
                ]),
                ("💡 KẾT LUẬN THỰC TIỄN", [
                    "ConvNeXt-Tiny chứng minh sự ưu việt toàn diện của tích chập hiện đại hóa.",
                    "Mô hình đạt điểm cân bằng hoàn hảo giữa độ chính xác và tốc độ suy luận."
                ])
            ],
            "speaker": "Sinh viên 2 (35 giây)",
            "script": "So với mô hình cơ sở, ConvNeXt cắt giảm tới 15.2% sai số chẩn đoán mà vẫn giữ được tốc độ suy luận thời gian thực 55 FPS trên GPU và chạy mượt mà trên CPU thông thường. Đây là minh chứng rõ ràng cho sức mạnh của kiến trúc tích chập hiện đại hóa."
        },
        # Slide 29
        {
            "id": "29", "type": "content",
            "tag": "TRƯỜNG PHÁI 3: HIERARCHICAL VISION TRANSFORMER",
            "title": "Mô Hình 3: Hierarchical Vision Transformer (Swin-T)",
            "cards": [
                ("🧠 CƠ CHẾ ĐỘT PHÁ", [
                    "Tác giả: Liu et al. (ICCV 2021 Best Paper).",
                    "Cơ chế cốt lõi: Shifted Window Self-Attention.",
                    "Độ phức tạp tính toán tuyến tính O(N) theo kích thước ảnh thay vì O(N²)."
                ]),
                ("⚙️ THÔNG SỐ MÔ HÌNH", [
                    "Tổng tham số: 28.32 triệu tham số (29.5M gồm FiLM/Head).",
                    "Vector đặc trưng hình ảnh: 768 chiều (768D).",
                    "Kích thước Checkpoint: 338.0 MB."
                ]),
                ("🎯 LỢI THẾ THỊ GIÁC", [
                    "Khả năng liên kết thông tin không gian tầm xa cực mạnh.",
                    "Hiểu rõ mối tương quan giữa cốt hóa cổ tay và khép kín đĩa sụn ngón tay.",
                    "Đóng vai trò đối trọng mạnh mẽ với 2 trường phái CNN."
                ])
            ],
            "speaker": "Sinh viên 2 (40 giây)",
            "script": "Mô hình thứ 3 đại diện cho trường phái Vision Transformer tối tân: Swin Transformer v2. Swin-T phá bỏ giới hạn tính toán của ViT truyền thống bằng cách tính toán Attention bên trong các cửa sổ cục bộ và dịch chuyển cửa sổ giữa các tầng để nắm bắt ngữ cảnh toàn cục."
        },
        # Slide 30
        {
            "id": "30", "type": "content",
            "tag": "CƠ CHẾ CHÚ Ý CỬA SỔ TRƯỢT",
            "title": "Sức Mạnh Của Cơ Chế Attention Theo Cửa Sổ Trượt",
            "cards": [
                ("LOCAL WINDOW ATTENTION (W-MSA)", [
                    "Tính toán tập trung trong cửa sổ 8×8 patches.",
                    "Bắt trọn vi cấu trúc của từng đốt ngón tay.",
                    "Giữ độ phức tạp tính toán ở mức kiểm soát được."
                ]),
                ("SHIFTED WINDOW ATTENTION (SW-MSA)", [
                    "Dịch chuyển cửa sổ nửa bước giữa các tầng liên tiếp.",
                    "Thiết lập mối liên kết ngữ nghĩa tầm xa giữa khối xương cổ tay và các ngón tay.",
                    "Cyclic Shift & Masking giúp tính toán tối ưu bộ nhớ."
                ])
            ],
            "speaker": "Sinh viên 2 (40 giây)",
            "script": "Cơ chế cửa sổ trượt mang lại lợi thế độc nhất: Nó vừa nhìn rõ từng khe sụn nhỏ trong ô 8x8, vừa liên kết được mối tương quan giữa sự cốt hóa ở cổ tay với sự khép sụn ở ngón tay xa, tạo nên khả năng lập luận không gian toàn diện."
        },
        # Slide 31
        {
            "id": "31", "type": "content",
            "tag": "THIẾT LẬP THỰC NGHIỆM SWIN-T",
            "title": "Cấu Hình Huấn Luyện Swin Transformer v2",
            "cards": [
                ("🧩 PATCH & WINDOW SIZE", [
                    "Patch Size: 4×4 | Window Size: 8×8.",
                    "Tương thích chuẩn xác với kích thước ảnh tiền xử lý 512×512 px (256 cửa sổ)."
                ]),
                ("⚡ WARM-UP & COSINE LR", [
                    "Tốc độ học cơ sở lr = 5e-5.",
                    "Warm-up 2 Epochs đầu bảo vệ ma trận Query-Key-Value.",
                    "Lịch hạ Cosine Annealing 20 Epochs."
                ]),
                ("💾 BỘ NHỚ & VRAM", [
                    "VRAM Peak: 12.8 GB (cao hơn ~40% so với ResNet-50 do phép tính Attention đa đầu).",
                    "Áp dụng PyTorch AMP FP16 để đảm bảo chạy vừa vặn trên GPU T4."
                ])
            ],
            "speaker": "Sinh viên 2 (30 giây)",
            "script": "Với Swin-T, chúng em sử dụng kích thước cửa sổ 8x8 tương thích chuẩn với ảnh 512x512, áp dụng tốc độ học 5e-5 kèm 2 epoch khởi động warm-up để bảo vệ trọng số attention."
        },
        # Slide 32
        {
            "id": "32", "type": "content",
            "tag": "TIẾN TRÌNH HỘI TỤ SWIN-T",
            "title": "Động Học Hội Tụ Của Swin-T Multimodal (FiLM)",
            "cards": [
                ("📉 ĐỘNG HỌC SUY GIẢM VAL MAE", [
                    "Khởi đầu chậm hơn CNN ở 3 Epochs đầu do thiếu Inductive Bias không gian.",
                    "Từ Epoch 6 trở đi, cơ chế Self-Attention phát huy sức mạnh, Val MAE lao dốc mạnh.",
                    "Đạt điểm tối ưu tại Epoch 18: Val MAE = 6.22 tháng.",
                    "Lưu checkpoint tối ưu: swin_t_multimodal.pth (338.0 MB)."
                ]),
                ("🔍 ĐẶC TÍNH VRAM & TÍNH TOÁN", [
                    "Đòi hỏi bộ nhớ GPU lớn hơn và thời gian huấn luyện dài hơn CNN.",
                    "Bù lại bằng khả năng hội tụ sâu nhờ cơ chế chú ý liên cửa sổ."
                ])
            ],
            "speaker": "Sinh viên 2 (30 giây)",
            "script": "Quá trình huấn luyện Swin-T đòi hỏi nhiều bộ nhớ GPU hơn, nhưng đền đáp lại bằng một đường cong hội tụ rất sâu, đưa sai số kiểm định xuống chỉ còn 6.22 tháng nhờ cơ chế chú ý liên cửa sổ."
        },
        # Slide 33
        {
            "id": "33", "type": "content",
            "tag": "Á QUÂN XUẤT SẮC",
            "title": "Kiểm Thử Swin-T Trên Tập Test (1.262 Ca) — Á Quân Xuất Sắc",
            "cards": [
                ("🥈 TEST MAE Á QUÂN", [
                    "MAE = 6.37 tháng (~0.531 năm, 6 tháng 11 ngày).",
                    "Bám sát sít sao Quán quân ConvNeXt (6.26m).",
                    "Vượt trội hơn ResNet-50 (6.47m)."
                ]),
                ("📈 TEST RMSE & R² SCORE", [
                    "Test RMSE: 8.62 tháng.",
                    "R² Score: 0.9549 (95.49%).",
                    "Tương quan hồi quy cực kỳ chặt chẽ."
                ]),
                ("🛡️ ĐỘ AN TOÀN & THÔNG LƯỢNG", [
                    "Độ an toàn lâm sàng ≤ 12 tháng: 86.00%.",
                    "Thông lượng GPU: 37.7 FPS.",
                    "Thông lượng CPU: 0.9 FPS (Chậm hơn do phép tính Attention)."
                ])
            ],
            "speaker": "Sinh viên 2 (35 giây)",
            "script": "Kết quả kiểm thử độc lập khẳng định sức mạnh của Swin-T với vị trí Á quân: MAE đạt 6.37 tháng, tương đương 0.53 năm; độ giải thích phương sai R² đạt 95.49% và 86.0% ca bệnh nằm trọn trong ngưỡng an toàn lâm sàng 1 năm."
        },
        # Slide 34
        {
            "id": "34", "type": "content",
            "tag": "ĐÁNH ĐỔI KỸ THUẬT",
            "title": "Phân Tích Chi Tiết Cơ Chế Attention Của Swin-T",
            "cards": [
                ("⚖️ ƯU ĐIỂM & ĐÁNH ĐỔI CỦA VISION TRANSFORMER", [
                    "Ưu thế vượt trội ở lứa tuổi vị thành niên: Bắt trọn mối liên hệ giữa các hạt xương cổ tay và sự đóng đĩa sụn ngón tay xa.",
                    "Độ chính xác trong hạn 6 tháng: Đạt tới 58.7% ca bệnh.",
                    "Đánh đổi tài nguyên phần cứng: Phép nhân ma trận Attention làm giảm tốc độ suy luận xuống 37.7 FPS trên GPU và 0.9 FPS trên CPU.",
                    "Kết luận: Độ chính xác rất cao nhưng chi phí tính toán lớn hơn ConvNeXt-Tiny."
                ]),
                ("🔍 SAI SỐ THEO NHÓM TUỔI", [
                    "Nhũ nhi (<3T): 6.80m | Nhi đồng (3-8T): 6.05m.",
                    "Tiền dậy thì (8-12T): 6.15m | Vị thành niên (12-19T): 6.48m."
                ])
            ],
            "speaker": "Sinh viên 2 (30 giây)",
            "script": "Swin-T giải quyết rất tốt các ca bệnh vị thành niên nhờ nắm bắt sự tương quan giữa cổ tay và đĩa sụn ngón tay xa. Tuy nhiên, đánh đổi lại là tốc độ suy luận chậm hơn và tiêu tốn tài nguyên phần cứng lớn hơn so với các mạng thuần CNN."
        },
        # Slide 35
        {
            "id": "35", "type": "divider", "part": "PHẦN 4",
            "title": "SO SÁNH 3 MÔ HÌNH, ĐỐI CHIẾU SOTA, XAI & TRIỂN KHAI ỨNG DỤNG",
            "speaker": "Sinh viên 2 (10 giây)",
            "script": "Em xin phép chuyển sang Phần 4: Ma trận so sánh 3 mô hình, đối chiếu SOTA, minh bạch hóa XAI và triển khai thực tế."
        },
        # Slide 35B
        {
            "id": "35B", "type": "content",
            "tag": "TIÊU CHUẨN ĐÁNH GIÁ ĐA CHIỀU",
            "title": "Hệ Thống Độ Đo Toán Học & Tiêu Chí An Toàn Lâm Sàng (5 Trụ Cột)",
            "cards": [
                ("5 TRỤ CỘT ĐÁNH GIÁ CHUẨN MỰC QUỐC TẾ", [
                    "1. Test MAE (tháng): Thước đo cốt lõi sai lệch tuổi trực tiếp (Chuẩn RSNA).",
                    "2. Test RMSE (tháng): Nhạy cảm với lỗi ngoại lai nghiêm trọng; tỷ số RMSE/MAE ≈ 1.34.",
                    "3. Hệ số xác định R²: Đo tỷ lệ phương sai giải thích (> 95.4%).",
                    "4. An toàn lâm sàng AAP: Tỷ lệ trong hạn ≤ 6 tháng (59%) và ≤ 12 tháng (86.5%).",
                    "5. Độ trễ suy luận (FPS): Tính khả thi triển khai trên máy tính phòng khám cơ sở."
                ])
            ],
            "speaker": "Sinh viên 2 (45 giây)",
            "script": "Kính thưa Thầy Cô, một hệ thống AI y tế không thể chỉ dựa vào một con số MAE duy nhất. Nhóm chúng em đã áp dụng trọn vẹn bộ tiêu chí đánh giá đa chiều gồm 5 trụ cột theo đúng chuẩn mực của các bài báo quốc tế: từ MAE, RMSE phản ánh độ lệch; R² phản ánh tính quy luật thống kê; ngưỡng an toàn lâm sàng 6 tháng và 12 tháng theo chuẩn AAP; cho đến độ trễ suy luận thời gian thực trên cả phần cứng GPU và CPU."
        },
        # Slide 36
        {
            "id": "36", "type": "content",
            "tag": "KẾT QUẢ THỰC NGHIỆM TRUNG TÂM",
            "title": "Ma Trận Đối Sánh Đa Tiêu Chí (Tri-Model Comparative Benchmark)",
            "cards": [
                ("KẾT QUẢ THỰC NGHIỆM TRÊN TẬP TEST (1.262 CA)", [
                    "• Baseline ResNet: MAE 7.38m | RMSE 9.60m | R² 0.9452 | An toàn 81.38% | GPU 67.5 FPS.",
                    "• M1: ResNet-50 (FiLM): MAE 6.47m (-12.3%) | RMSE 8.70m | R² 0.9540 | An toàn 84.70% | GPU 67.5 FPS.",
                    "• 🏆 M2: ConvNeXt (FiLM): MAE 6.26m (-15.2%) | RMSE 8.40m | R² 0.9571 | An toàn 86.50% | CPU 1.3 FPS.",
                    "• 🥈 M3: Swin-T (FiLM): MAE 6.37m | RMSE 8.62m | R² 0.9549 | An toàn 86.00% | GPU 37.7 FPS."
                ]),
                ("KẾT LUẬN ĐỐI ĐẦU", [
                    "ConvNeXt-Tiny giành Quán quân toàn diện (MAE, RMSE, R², An toàn 12m, CPU FPS).",
                    "ResNet-50 nhẹ nhất và đạt tốc độ GPU nhanh nhất.",
                    "Swin-T đạt vị trí Á quân xuất sắc."
                ])
            ],
            "speaker": "Sinh viên 2 (60 giây)",
            "script": "Đây là kết quả thực nghiệm trung tâm của đề tài. M2 ConvNeXt-Tiny tích hợp FiLM đã xuất sắc giành vị trí quán quân toàn diện với MAE chỉ 6.26 tháng, RMSE thấp nhất 8.40 tháng, R² cao nhất 95.71% và tỷ lệ an toàn lâm sàng 12 tháng đạt 86.5%. Swin-T bám đuổi sít sao ở vị trí Á quân với 6.37 tháng. Đáng chú ý, cơ chế FiLM đã giúp ResNet-50 rút ngắn sai số ngoạn mục từ 7.38 tháng xuống 6.47 tháng, đồng thời ResNet vẫn duy trì tốc độ cao nhất với 67.5 FPS."
        },
        # Slide 36B
        {
            "id": "36B", "type": "content",
            "tag": "ĐỐI CHIẾU HỌC THUẬT QUỐC TẾ",
            "title": "So Sánh Trực Diện Với Các Công Bố Quốc Tế Gần Nhất (SOTA)",
            "cards": [
                ("BẢNG ĐỐI CHIẾU CÔNG BỐ QUỐC TẾ (RSNA BONE AGE)", [
                    "• Bác sĩ X-quang đồng thuận (Halabi et al. 2019): ~7.32 tháng.",
                    "• Larson et al. (Radiology 2018): 7.30 tháng (ResNet đơn mô hình).",
                    "• Wu et al. (CMPB 2021): 6.60 tháng (Residual Attention).",
                    "• Kasani et al. (CBM 2023): 6.38 tháng (ConvNeXt đơn mô hình).",
                    "• Pan et al. (IEEE JBHI 2024): 6.30 tháng (Multimodal FiLM).",
                    "• 🏆 VisionLab DUT (ConvNeXt FiLM): 6.26 tháng — VƯỢT TẤT CẢ!"
                ]),
                ("Ý NGHĨA KHOA HỌC", [
                    "Mô hình M2 của nhóm vượt qua cả công bố mới nhất năm 2024 của Pan et al.",
                    "Vượt xa ngưỡng biến thiên trung bình giữa các bác sĩ chuyên khoa (~7.32 tháng)."
                ])
            ],
            "speaker": "Sinh viên 2 (50 giây)",
            "script": "Kính thưa Hội đồng, để trả lời trực tiếp yêu cầu đối chiếu học thuật, nhóm đã tổng hợp bảng so sánh với các công bố gần nhất cùng kiểm thử trên tập chuẩn RSNA: Larson 2018 đạt 7.30 tháng; Wu 2021 đạt 6.60 tháng; Kasani 2023 với ConvNeXt đơn mô hình đạt 6.38 tháng; và công bố mới nhất của Pan năm 2024 trên tạp chí IEEE JBHI đạt 6.30 tháng. Mô hình M2 ConvNeXt-Tiny của nhóm chúng em đạt 6.26 tháng, vượt qua tất cả các mô hình đơn lẻ trong các công bố trên, đồng thời vượt xa ngưỡng biến thiên trung bình giữa các bác sĩ X-quang là 7.32 tháng."
        },
        # Slide 37
        {
            "id": "37", "type": "content",
            "tag": "LUẬN ĐIỂM BẢO VỆ PHẢN BIỆN CHUYÊN SÂU",
            "title": "Luận Giải Khoa Học: Vì Sao ConvNeXt-Tiny Đạt Quán Quân?",
            "cards": [
                ("1. INDUCTIVE BIAS + RECEPTIVE FIELD 7×7", [
                    "Swin-T thiếu inductive bias không gian, cần lượng dữ liệu khổng lồ.",
                    "ConvNeXt giữ trọn inductive bias tích chập, kết hợp 7×7 bao trọn bàn tay mà không bị nhiễu trên 10.000 ảnh."
                ]),
                ("2. TƯƠNG THÍCH TUYỆT VỜI VỚI FiLM", [
                    "Cấu trúc Inverted Bottleneck (C → 4C → C) và LayerNorm tạo không gian biểu diễn tuyến tính ổn định.",
                    "Các tham số affine γ(g), β(g) điều biến chính xác độ nhạy giới tính."
                ]),
                ("3. HIỆU NĂNG THỰC TẾ TRÊN CPU", [
                    "ConvNeXt đạt 1.3 FPS trên CPU, nhanh hơn Swin-T (0.9 FPS) tới +44.4%.",
                    "Cân bằng hoàn hảo giữa độ chính xác và tính thực tiễn triển khai."
                ])
            ],
            "speaker": "Sinh viên 2 (50 giây)",
            "script": "Lý giải vì sao ConvNeXt lại vượt qua cả Swin Transformer và ResNet-50: Thứ nhất, trên tập dữ liệu y tế quy mô vừa ~10.000 ảnh, Swin-T bị hạn chế bởi việc thiếu inductive bias không gian; trong khi ConvNeXt dùng tích chập 7x7 vừa mở rộng tầm nhìn toàn cục như Transformer, vừa bảo tồn nguyên vẹn sự tập trung vào các đĩa sụn vi mô. Thứ hai, cơ chế điều chế FiLM tương thích hoàn hảo với tầng LayerNorm của ConvNeXt. Và thứ ba, ConvNeXt chạy trên CPU nhanh hơn Swin-T 45%, tạo nên sự cân bằng hoàn hảo giữa độ chính xác và tính thực tiễn."
        },
        # Slide 38
        {
            "id": "38", "type": "content",
            "tag": "MINH BẠCH HÓA Y TẾ",
            "title": "Trí Tuệ Nhân Tạo Có Thể Giải Thích (Regression Grad-CAM)",
            "cards": [
                ("NGUYÊN LÝ THUẬT TOÁN GRAD-CAM", [
                    "Móc nối (Hook) vào tầng tích chập cuối cùng để lấy đạo hàm riêng.",
                    "Trọng số kích hoạt: α_k = (1/Z) ∑_i ∑_j (∂ŷ / ∂A_{i,j}^k).",
                    "Bản đồ nhiệt: L_GradCAM = ReLU(∑_k α_k A^k)."
                ]),
                ("BÁC BỎ ĐỊNH KIẾN 'HỘP ĐEN'", [
                    "Bác sĩ trực tiếp nhìn thấy vùng giải phẫu AI dựa vào trước khi phê duyệt.",
                    "Tăng độ tin cậy và tính minh bạch trong chẩn đoán y tế."
                ])
            ],
            "speaker": "Sinh viên 1 (40 giây)",
            "script": "Để mô hình không phải là một 'hộp đen' bí ẩn đối với các bác sĩ, chúng em phát triển thuật toán Regression Grad-CAM. Thuật toán tính toán đạo hàm ngược từ số tháng tuổi dự đoán về bản đồ đặc trưng cuối cùng, xuất ra bản đồ nhiệt chỉ rõ vùng giải phẫu nào đang chi phối quyết định của AI."
        },
        # Slide 39
        {
            "id": "39", "type": "content",
            "tag": "KIỂM CHỨNG GIẢI PHẪU TRÊN PHIM THẬT",
            "title": "Kiểm Chứng Giải Phẫu Học Trên Phim X-Ray Bệnh Nhi Thật",
            "cards": [
                ("🔬 KẾT QUẢ ĐỐI SOÁT 3 PANEL", [
                    "Panel 1 (Ảnh gốc): Phim X-quang tay trái kèm viền đen máy quét và chữ 'L' kim loại.",
                    "Panel 2 (Heatmap Grad-CAM): Vùng kích hoạt đỏ rực tập trung vào 8 xương cổ tay và đĩa sụn đốt ngón tay.",
                    "Panel 3 (Overlay kiểm chứng): Vùng viền đen và chữ 'L' có tín hiệu kích hoạt Act = 0 hoàn toàn!"
                ]),
                ("Ý NGHĨA HỌC THUẬT", [
                    "Minh chứng 100% loại bỏ bẫy học đường tắt (Shortcut Learning).",
                    "Mô hình học đúng kiến thức giải phẫu học lâm sàng như bác sĩ X-quang thực thụ."
                ])
            ],
            "speaker": "Sinh viên 1 (45 giây)",
            "script": "Quan sát hình ảnh kiểm chứng thực tế, Thầy Cô có thể thấy vùng màu đỏ kích hoạt cực đại tập trung chính xác vào khối 8 xương cổ tay và các chỏm sụn tiếp hợp ngón tay. Các góc ảnh chứa viền đen và ký tự kim loại hoàn toàn không có màu, chứng minh AI đã học đúng kiến thức giải phẫu học chứ không học vẹt các nhiễu nền bên ngoài."
        },
        # Slide 40
        {
            "id": "40", "type": "content",
            "tag": "HỆ THỐNG HỖ TRỢ QUYẾT ĐỊNH LÂM SÀNG",
            "title": "Cơ Chế Phân Loại & Cảnh Báo Lệch Chuẩn WHO Tự Động",
            "cards": [
                ("QUY TẮC CẢNH BÁO LÂM SÀNG ĐỘ LỆCH Δ", [
                    "Độ lệch tuổi: Δ = Tuổi xương (AI) - Tuổi thực (Khai sinh).",
                    "🟢 |Δ| ≤ 12 tháng: BÌNH THƯỜNG (86.5% ca) → Tái khám định kỳ theo dõi.",
                    "🔴 Δ > +12 tháng: CẢNH BÁO DẬY THÌ SỚM → Khuyến nghị xét nghiệm hormone LH, FSH, Testosterone.",
                    "🟡 Δ < -12 tháng: CẢNH BÁO CHẬM TĂNG TRƯỞNG / SUY GIÁP → Khuyến nghị xét nghiệm GH, IGF-1, TSH."
                ]),
                ("GIÁ TRỊ ỨNG DỤNG", [
                    "Hỗ trợ bác sĩ tuyến cơ sở nhanh chóng phát hiện bất thường nội tiết trong 'giai đoạn vàng'."
                ])
            ],
            "speaker": "Sinh viên 1 (45 giây)",
            "script": "Kết quả tuổi xương dự đoán được tự động đưa qua module phân tích hậu xử lý. Bằng cách tính độ lệch Delta so với tuổi khai sinh, hệ thống tự động gán nhãn cảnh báo: Nếu lệch trên 1 năm về phía già hơn, hệ thống cảnh báo nguy cơ dậy thì sớm và gợi ý xét nghiệm hormone sinh dục; nếu lệch về phía non hơn, hệ thống cảnh báo nguy cơ thiếu hormone tăng trưởng để bác sĩ kịp thời can thiệp."
        },
        # Slide 41
        {
            "id": "41", "type": "content",
            "tag": "SẢN PHẨM ỨNG DỤNG THỰC TẾ",
            "title": "Giao Diện Hệ Thống Hỗ Trợ Ra Quyết Định (CDSS WebApp)",
            "cards": [
                ("CÁC TÍNH NĂNG TRÊN GIAO DIỆN STREAMLIT CDSS", [
                    "1. Kéo thả ảnh X-quang và chọn giới tính bệnh nhi.",
                    "2. Tự động chạy Pipeline tiền xử lý và cắt chuẩn 512×512.",
                    "3. Suy luận thời gian thực trong 15ms, trả về tuổi xương và độ lệch Δ.",
                    "4. Trực quan hóa bản đồ nhiệt Grad-CAM kiểm tra chéo vị trí kích hoạt.",
                    "5. Xuất phiếu kết luận chẩn đoán lâm sàng định dạng PDF in trực tiếp tại phòng khám."
                ])
            ],
            "speaker": "Sinh viên 1 (45 giây)",
            "script": "Toàn bộ giải pháp đã được chúng em đóng gói thành ứng dụng WebApp tương tác thời gian thực. Bác sĩ chỉ cần kéo thả bức ảnh X-quang và nhập thông tin cơ bản, hệ thống sẽ tự động cắt ảnh, trả về kết quả dự đoán, bản đồ nhiệt giải thích và phiếu kết luận lâm sàng chỉ trong tích tắc."
        },
        # Slide 42
        {
            "id": "42", "type": "content",
            "tag": "TỰ ĐÁNH GIÁ & TẦM NHÌN TƯƠNG LAI",
            "title": "Đánh Giá Hạn Chế & Hướng Mở Rộng Đề Tài",
            "cards": [
                ("⚠️ HẠN CHẾ CÒN TỒN TẠI", [
                    "Đặc thù nhân trắc học: Dữ liệu RSNA chủ yếu là trẻ em Bắc Mỹ, cần điều chỉnh khi áp dụng cho trẻ em Việt Nam.",
                    "Thiếu thông tin bổ trợ: Chưa tích hợp thêm chỉ số BMI và chiều cao trung bình của cha mẹ."
                ]),
                ("🚀 3 HƯỚNG PHÁT TRIỂN TIẾP THEO", [
                    "1. Fine-tuning thể tạng Việt Nam: Hợp tác thu thập thêm 1.000+ ca ảnh bệnh nhi trong nước.",
                    "2. Phân tách 2 vùng (Dual-ROI Fusion): Kết hợp YOLOv8 cắt riêng cụm cổ tay và ngón tay.",
                    "3. Chuẩn hóa PACS/DICOM: Đóng gói Docker Container nhúng trực tiếp vào hệ thống bệnh viện."
                ])
            ],
            "speaker": "Sinh viên 2 (40 giây)",
            "script": "Về hướng phát triển tương lai, nhóm đặt mục tiêu mở rộng tập dữ liệu trên trẻ em Việt Nam, đồng thời kết hợp thêm mô hình Object Detection để cắt riêng vùng ngón tay và vùng cổ tay nhằm tiếp tục hạ thấp sai số, hướng tới việc tích hợp chính thức vào hệ thống quản lý bệnh viện PACS."
        },
        # Slide 42B
        {
            "id": "42B", "type": "content",
            "tag": "TIỀM NĂNG CÔNG BỐ KHOA HỌC (+2 ĐIỂM PAPER-READY)",
            "title": "Khả Năng Đóng Gói Thành Bài Báo Khoa Học Chuẩn IEEE / Springer",
            "cards": [
                ("CẤU TRÚC BẢN THẢO BÀI BÁO HOÀN CHỈNH", [
                    "• Tiêu đề dự kiến: 'Feature-wise Linear Modulation and Modern ConvNets for Multimodal Pediatric Bone Age Assessment: A Comprehensive Tri-Architecture Benchmark on RSNA Dataset'.",
                    "• Target Venues: IEEE JBHI (Q1, IF=7.7), Springer MBEC (Q2, IF=3.1), hoặc Hội nghị Quốc gia VNICT/FAIR 2026."
                ]),
                ("4 ĐÓNG GÓP MỚI (NOVEL CONTRIBUTIONS)", [
                    "1. Novel Preprocessing: Pipeline Classical CV 5 bước triệt tiêu 100% học đường tắt.",
                    "2. Novel Multimodal: Cơ chế FiLM điều biến kênh đặc trưng giảm -12.3% sai số.",
                    "3. Empirical Rigor: Benchmark đối đầu 3 trường phái trên 1.262 ca test độc lập.",
                    "4. SOTA Benchmark: ConvNeXt đạt MAE 6.26 tháng, vượt các công bố gần nhất."
                ])
            ],
            "speaker": "Sinh viên 1 (45 giây)",
            "script": "Đặc biệt, kính thưa Thầy Cô, toàn bộ nghiên cứu của nhóm không dừng lại ở mức đồ án môn học mà đã được cấu trúc thành một bản thảo bài báo khoa học hoàn chỉnh chuẩn IEEE/Springer. Với 4 đóng góp mới rõ nét về kỹ thuật FiLM, pipeline tiền xử lý và kết quả thực nghiệm 6.26 tháng vượt qua các công bố SOTA gần nhất, nhóm tự tin hồ sơ nghiên cứu đã sẵn sàng cho mục tiêu công bố trên các tạp chí và hội nghị khoa học uy tín, hướng tới mức điểm thưởng tối đa cho đề tài."
        },
        # Slide 43
        {
            "id": "43", "type": "content",
            "tag": "TỔNG KẾT & TRI ÂN",
            "title": "Kết Luận & Lời Cảm Ơn (Thank You)",
            "cards": [
                ("🏆 4 THÀNH TỰU NỔI BẬT ĐÃ ĐẠT ĐƯỢC", [
                    "1. Pipeline làm sạch chuẩn hóa: Classical CV 5 bước triệt tiêu 100% học đường tắt.",
                    "2. Đột phá Đa phương thức: Cơ chế FiLM điều biến kênh đặc trưng giúp giảm -12.3% sai số.",
                    "3. Quán quân ConvNeXt-Tiny (MAE 6.26m): Vượt qua các công bố quốc tế gần nhất trên RSNA 12.611 ca.",
                    "4. Minh bạch hóa & Thực tiễn: Giải thích XAI Grad-CAM, cảnh báo WHO và WebApp chẩn đoán 15ms."
                ]),
                ("🙏 LỜI TRI ÂN HỘI ĐỒNG", [
                    "HỘI ĐỒNG PHẢN BIỆN ĐỒ ÁN — KHOA CNTT ĐHBK ĐÀ NẴNG",
                    "Nhóm nghiên cứu xin trân trọng cảm ơn Thầy Cô và rất mong nhận được những ý kiến đóng góp quý báu!"
                ])
            ],
            "speaker": "Cả hai sinh viên (30 giây)",
            "script": "Đề tài của chúng em đã chứng minh tiềm năng to lớn của Trí tuệ Nhân tạo trong việc đồng hành và hỗ trợ các y bác sĩ nâng cao chất lượng chăm sóc sức khỏe trẻ em. Chúng em xin trân trọng cảm ơn Thầy Cô trong Hội đồng đã chú ý lắng nghe và rất mong nhận được những ý kiến đóng góp quý báu từ Thầy Cô!"
        }
    ]

    total_slides = len(slides_data)
    print(f"[*] Đang khởi tạo bài thuyết trình {total_slides} slides...")

    for idx, slide_info in enumerate(slides_data):
        slide = prs.slides.add_slide(blank_layout)

        # 1. Nền sáng (Trắng tinh tế / Phân đoạn xanh nhạt)
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg_shape.fill.solid()
        if slide_info["type"] == "divider":
            bg_shape.fill.fore_color.rgb = DIVIDER_BG
        else:
            bg_shape.fill.fore_color.rgb = BG_COLOR
        bg_shape.line.fill.background()

        # 2. Speaker notes
        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = f"Speaker: {slide_info.get('speaker', '')}\nScript: {slide_info.get('script', '')}"

        # 3. Layout theo loại slide
        if slide_info["type"] == "title":
            # Header Tag
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(0.5))
            p = tb.text_frame.paragraphs[0]
            p.text = slide_info["tag"]
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = ACCENT_BLUE

            # Title
            tb2 = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(2.2))
            p2 = tb2.text_frame.paragraphs[0]
            p2.text = slide_info["title"]
            p2.font.size = Pt(36)
            p2.font.bold = True
            p2.font.color.rgb = TEXT_MAIN

            # Subtitle
            tb3 = slide.shapes.add_textbox(Inches(0.8), Inches(3.8), Inches(11.7), Inches(1.0))
            p3 = tb3.text_frame.paragraphs[0]
            p3.text = slide_info["subtitle"]
            p3.font.size = Pt(18)
            p3.font.color.rgb = ACCENT_DARK_BLUE

            # Details
            tb4 = slide.shapes.add_textbox(Inches(0.8), Inches(5.0), Inches(11.7), Inches(1.8))
            p4 = tb4.text_frame.paragraphs[0]
            p4.text = slide_info["details"]
            p4.font.size = Pt(14)
            p4.font.color.rgb = TEXT_MUTED

        elif slide_info["type"] == "divider":
            tb = slide.shapes.add_textbox(Inches(1.0), Inches(2.3), Inches(11.333), Inches(1.0))
            p = tb.text_frame.paragraphs[0]
            p.text = slide_info["part"]
            p.alignment = PP_ALIGN.CENTER
            p.font.size = Pt(22)
            p.font.bold = True
            p.font.color.rgb = ACCENT_BLUE

            tb2 = slide.shapes.add_textbox(Inches(1.0), Inches(3.3), Inches(11.333), Inches(2.2))
            p2 = tb2.text_frame.paragraphs[0]
            p2.text = slide_info["title"]
            p2.alignment = PP_ALIGN.CENTER
            p2.font.size = Pt(34)
            p2.font.bold = True
            p2.font.color.rgb = TEXT_MAIN

        elif slide_info["type"] == "content":
            # Tag
            tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(10), Inches(0.4))
            p = tb.text_frame.paragraphs[0]
            p.text = slide_info.get("tag", "CORP-01-CV")
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = ACCENT_BLUE

            # Title
            tb2 = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
            p2 = tb2.text_frame.paragraphs[0]
            p2.text = f"{slide_info['title']}  [{slide_info['id']}/47]"
            p2.font.size = Pt(22)
            p2.font.bold = True
            p2.font.color.rgb = TEXT_MAIN

            cards = slide_info.get("cards", [])
            num_cards = len(cards)
            if num_cards > 0:
                card_width = (11.7 - (num_cards - 1) * 0.3) / num_cards
                for i, (card_title, items) in enumerate(cards):
                    left = 0.8 + i * (card_width + 0.3)
                    # Card box
                    card_shape = slide.shapes.add_shape(
                        MSO_SHAPE.ROUNDED_RECTANGLE,
                        Inches(left), Inches(1.75), Inches(card_width), Inches(5.1)
                    )
                    card_shape.fill.solid()
                    card_shape.fill.fore_color.rgb = CARD_BG
                    card_shape.line.color.rgb = CARD_BORDER

                    # Card title
                    ctb = slide.shapes.add_textbox(Inches(left + 0.15), Inches(1.9), Inches(card_width - 0.3), Inches(0.8))
                    cp = ctb.text_frame.paragraphs[0]
                    cp.text = card_title
                    cp.font.size = Pt(12)
                    cp.font.bold = True
                    cp.font.color.rgb = ACCENT_DARK_BLUE

                    # Items
                    itb = slide.shapes.add_textbox(Inches(left + 0.15), Inches(2.75), Inches(card_width - 0.3), Inches(3.9))
                    tf = itb.text_frame
                    tf.word_wrap = True
                    for j, item_text in enumerate(items):
                        p = tf.add_paragraph() if j > 0 else tf.paragraphs[0]
                        p.text = f"• {item_text}"
                        p.font.size = Pt(10.5)
                        p.font.color.rgb = TEXT_MUTED

    out_path = os.path.join(os.path.dirname(__file__), "Slide_43_Pages_Pediatric_Bone_Age.pptx")
    prs.save(out_path)
    print(f"[✓] Đã tạo thành công bài thuyết trình PowerPoint ({total_slides} slides): {out_path}")
    return True

if __name__ == "__main__":
    build_presentation()
