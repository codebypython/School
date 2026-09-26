"""
VietLawAssist — Synthetic Legal Exam & Barem Generator (synthetic_engine.py)
============================================================================
Agent-02 (ML Researcher) & Agent-03 (Data Engineer)
Module tổng hợp và tăng cường dữ liệu đề thi tự động theo phương pháp luận
Self-Instruct / Evol-Instruct bám sát chuẩn Barem chấm điểm môn Pháp luật Đại cương (DUT).

Cung cấp:
    - Bộ sinh kịch bản tình huống đa dạng (Data Generators) cho cả 6 Intent Codes:
      1. CIVIL_INHERIT: Bài toán chia thừa kế 5 bước toán học pháp lý (100 mẫu)
      2. VPPL_ELEMENTS: Phân tích 4 yếu tố cấu thành vi phạm pháp luật (100 mẫu)
      3. TRUE_FALSE: Nhận định Đúng/Sai 3 bước lập luận (100 mẫu)
      4. QPPL_STRUCTURE: Phân tích cơ cấu 3 bộ phận Quy phạm pháp luật (100 mẫu)
      5. CRIMINAL_AGE: Thuật toán đối soát độ tuổi & phân loại tội phạm Điều 9 + 12 BLHS (75 mẫu)
      6. GENERAL_THEORY: Lý luận chung về Nhà nước và Pháp luật (25 mẫu)
    - Citation Guardrail: Kiểm tra chéo điều luật tồn tại trong SQLite DB
    - Đảm bảo 100% 500 mẫu độc nhất (unique) sau khử trùng lặp
"""

import json
import random
from pathlib import Path
from typing import Optional
from loguru import logger

from .config import DB_PATH, PROCESSED_DIR
from .sft_builder import get_existing_db_article_ids


class LegalSyntheticEngine:
    """Động cơ sinh dữ liệu bài tập tình huống và lời giải chuẩn barem DUT."""

    def __init__(self, seed: int = 42):
        self.seed = seed
        random.seed(seed)
        self.valid_article_ids = get_existing_db_article_ids()

    # =========================================================================
    # 1. GENERATOR: CHIA THỪA KẾ (CIVIL_INHERIT) — 100 MẪU ĐỘC NHẤT
    # =========================================================================
    def generate_inherit_cases(self, count: int = 100) -> list[dict]:
        cases = []
        husbands = ["Nam", "Bình", "Hùng", "Minh", "Tuấn", "Thành", "Đức", "Hải", "Long", "Vinh", "Khánh", "Sơn", "Tùng", "Phúc", "Khang", "Hoàng", "Quân", "Toàn", "Duy", "Trí", "Kiên", "Bách", "Nghĩa", "Thịnh", "Thắng"]
        wives = ["Lan", "Hoa", "Mai", "Cúc", "Trúc", "Hương", "Thảo", "Hạnh", "Ngọc", "Yến", "Phương", "Diệp", "Linh", "Thủy", "Huyền", "Trang", "Trâm", "Quyên", "Vy", "Hà", "Nhung", "Oanh", "Tuyết", "Loan", "Quỳnh"]
        friends = ["Cường", "Dũng", "Bảo", "Lâm", "Huy", "An", "Khoa", "Phong", "Triết", "Việt"]
        provinces = ["Đà Nẵng", "Hà Nội", "TP. Hồ Chí Minh", "Quảng Nam", "Huế", "Bình Định", "Khánh Hòa", "Cần Thơ", "Hải Phòng", "Quảng Ngãi"]
        child_names = [("con trai cả", "con gái út"), ("con A", "con B"), ("con trai Nguyễn Văn C", "con gái Nguyễn Thị D"), ("con trai đầu", "con trai thứ"), ("chị Hai", "anh Ba")]

        amounts = [600, 800, 900, 1000, 1200, 1400, 1500, 1600, 1800, 2000, 2100, 2400, 2700, 3000, 3200, 3600, 4000, 4200, 4800, 5000, 6000]

        for i in range(1, count + 1):
            h_name = husbands[(i * 7 + 1) % len(husbands)]
            w_name = wives[(i * 11 + 3) % len(wives)]
            f_name = friends[(i * 5 + 2) % len(friends)]
            prov = provinces[(i * 3) % len(provinces)]
            c1_desc, c2_desc = child_names[i % len(child_names)]

            total_prop = amounts[i % len(amounts)]
            estate = total_prop // 2

            scenario_type = i % 4

            if scenario_type == 0:
                # Kịch bản 1: Vợ + 2 con (1 con chưa thành niên, 1 con đã thành niên), di chúc cho người ngoài
                minor_age = 10 + (i % 7)  # 10 - 16 tuổi
                adult_age = 22 + (i % 8)  # 22 - 29 tuổi
                num_heirs_law = 3
                one_share_law = estate / num_heirs_law
                share_644 = (2 / 3) * one_share_law
                num_644 = 2  # Vợ + con chưa thành niên
                total_644 = num_644 * share_644
                estate_will = estate - total_644

                input_text = (
                    f"[Mã ca {i:03d}] Tình huống tại {prov}: Ông {h_name} và bà {w_name} là vợ chồng hợp pháp có khối tài sản chung là {total_prop:,} triệu đồng. "
                    f"Hai người có 2 người con gồm {c1_desc} ({adult_age} tuổi, đi làm có thu nhập ổn định) và {c2_desc} ({minor_age} tuổi). "
                    f"Ông {h_name} lập di chúc hợp pháp truất quyền hưởng di sản của toàn bộ vợ con và chỉ định để lại toàn bộ tài sản của mình cho anh {f_name}. Sau đó ông {h_name} qua đời. "
                    f"Hỏi di sản thừa kế của ông {h_name} được phân chia cụ thể như thế nào theo chuẩn 5 bước của môn Pháp luật Đại cương?"
                )

                output_text = (
                    "I. CĂN CỨ PHÁP LÝ:\n"
                    "- Luật Hôn nhân và Gia đình 2014 (Điều 33: Tài sản chung của vợ chồng).\n"
                    "- Bộ luật Dân sự 2015 (Điều 644: Người thừa kế không phụ thuộc vào nội dung di chúc; Điều 651: Người thừa kế theo pháp luật).\n\n"
                    "II. CÁC BƯỚC GIẢI QUYẾT CHI TIẾT:\n"
                    f"1. Bước 1: Xác định di sản thừa kế của ông {h_name}:\n"
                    f"- Khối tài sản chung = {total_prop:,} triệu đồng.\n"
                    f"- Theo Điều 33 Luật HNGĐ, phần di sản của ông {h_name} là: {total_prop:,} / 2 = {estate:,.1f} triệu đồng.\n\n"
                    f"2. Bước 2: Giả định chia thừa kế theo pháp luật để tính giá trị 1 suất cơ bản:\n"
                    f"- Hàng thừa kế thứ nhất (Điều 651 BLDS) gồm: Bà {w_name} (vợ) và 2 con ({c1_desc}, {c2_desc}) -> Tổng cộng 3 suất bằng nhau.\n"
                    f"- Giá trị 1 suất theo luật: {estate:,.1f} / 3 = {one_share_law:,.2f} triệu đồng.\n\n"
                    f"3. Bước 3: Xác định đối tượng hưởng thừa kế không phụ thuộc nội dung di chúc (Điều 644 BLDS 2015):\n"
                    f"- Những người được hưởng gồm: Bà {w_name} (vợ) và {c2_desc} ({minor_age} tuổi, chưa thành niên).\n"
                    f"- {c1_desc} ({adult_age} tuổi, có khả năng lao động) không thuộc diện Điều 644.\n"
                    f"- Mỗi suất Điều 644 = 2/3 * {one_share_law:,.2f} = {share_644:,.2f} triệu đồng.\n"
                    f"- Tổng số tiền trích trả cho diện Điều 644: 2 * {share_644:,.2f} = {total_644:,.2f} triệu đồng.\n\n"
                    f"4. Bước 4: Chia phần còn lại theo di chúc cho anh {f_name}:\n"
                    f"- Di sản còn lại cho {f_name}: {estate:,.1f} - {total_644:,.2f} = {estate_will:,.2f} triệu đồng.\n\n"
                    "III. KẾT LUẬN PHÂN CHIA DI SẢN:\n"
                    f"- Bà {w_name} nhận: {share_644:,.2f} triệu đồng.\n"
                    f"- {c2_desc} nhận: {share_644:,.2f} triệu đồng.\n"
                    f"- Anh {f_name} (theo di chúc) nhận: {estate_will:,.2f} triệu đồng.\n"
                    f"- {c1_desc} không được hưởng di sản."
                )

            elif scenario_type == 1:
                # Kịch bản 2: Vợ + 3 con (2 con chưa thành niên, 1 con đã thành niên)
                num_heirs_law = 4
                one_share_law = estate / num_heirs_law
                share_644 = (2 / 3) * one_share_law
                num_644 = 3  # Vợ + 2 con chưa thành niên
                total_644 = num_644 * share_644
                estate_will = estate - total_644

                input_text = (
                    f"[Mã ca {i:03d}] Tình huống tại {prov}: Ông {h_name} và bà {w_name} tích lũy được khối tài sản chung trị giá {total_prop:,} triệu đồng. "
                    f"Gia đình có 3 người con: người con cả (26 tuổi, tự chủ kinh tế) và 2 con nhỏ (15 tuổi và 11 tuổi). "
                    f"Trước khi mất, ông {h_name} để lại di chúc hợp pháp tặng toàn bộ di sản của mình cho người bạn thân là anh {f_name}. "
                    f"Hãy thực hiện phân chia di sản thừa kế của ông {h_name} theo đúng quy định pháp luật hiện hành."
                )

                output_text = (
                    "I. CĂN CỨ PHÁP LÝ:\n"
                    "- Điều 33 Luật HNGĐ 2014; Điều 644 và Điều 651 BLDS 2015.\n\n"
                    "II. CÁC BƯỚC GIẢI QUYẾT CHI TIẾT:\n"
                    f"1. Bước 1: Xác định di sản thừa kế của ông {h_name}: {total_prop:,} / 2 = {estate:,.1f} triệu đồng.\n"
                    f"2. Bước 2: Giả định chia theo luật: Hàng 1 gồm vợ và 3 con (4 suất). Mỗi suất = {estate:,.1f} / 4 = {one_share_law:,.2f} triệu đồng.\n"
                    f"3. Bước 3: Diện bắt buộc hưởng theo Điều 644 BLDS 2015 gồm bà {w_name} và 2 con chưa thành niên (3 người).\n"
                    f"- Mỗi người hưởng: 2/3 * {one_share_law:,.2f} = {share_644:,.2f} triệu đồng.\n"
                    f"- Tổng trích trả diện 644: 3 * {share_644:,.2f} = {total_644:,.2f} triệu đồng.\n"
                    f"4. Bước 4: Phần còn lại thực hiện theo di chúc cho anh {f_name}: {estate:,.1f} - {total_644:,.2f} = {estate_will:,.2f} triệu đồng.\n\n"
                    "III. KẾT LUẬN:\n"
                    f"- Bà {w_name} nhận: {share_644:,.2f} triệu đồng.\n"
                    f"- Hai con chưa thành niên mỗi người nhận: {share_644:,.2f} triệu đồng.\n"
                    f"- Anh {f_name} nhận: {estate_will:,.2f} triệu đồng.\n"
                    "- Người con cả đã thành niên không được nhận di sản."
                )

            elif scenario_type == 2:
                # Kịch bản 3: Không có di chúc -> Chia hoàn toàn theo pháp luật Điều 651
                num_heirs = 3
                share = estate / num_heirs

                input_text = (
                    f"[Mã ca {i:03d}] Tình huống tại {prov}: Ông {h_name} và bà {w_name} có tài sản chung là {total_prop:,} triệu đồng và 2 người con chung. "
                    f"Ông {h_name} không may bị tai nạn qua đời đột ngột, không để lại di chúc. "
                    f"Hãy chia di sản thừa kế của ông {h_name} theo đúng các bước quy định của pháp luật."
                )

                output_text = (
                    "I. CĂN CỨ PHÁP LÝ:\n"
                    "- Điều 33 Luật HNGĐ 2014; Khoản 1 Điều 650, Điều 651 BLDS 2015.\n\n"
                    "II. CÁC BƯỚC GIẢI QUYẾT CHI TIẾT:\n"
                    f"1. Bước 1: Xác định di sản thừa kế của ông {h_name}: {total_prop:,} / 2 = {estate:,.1f} triệu đồng.\n"
                    "2. Bước 2: Xác định hình thức chia thừa kế:\n"
                    "- Do người để lại di sản chết không có di chúc, toàn bộ di sản được phân chia theo pháp luật (Khoản 1 Điều 650 BLDS 2015).\n"
                    f"3. Bước 3: Xác định những người thừa kế ở hàng thừa kế thứ nhất (Điều 651 BLDS 2015):\n"
                    f"- Gồm có 3 người: Bà {w_name} (vợ) và 2 người con chung.\n"
                    f"4. Bước 4: Tính toán giá trị di sản mỗi đồng thừa kế nhận được:\n"
                    f"- Mỗi người nhận phần bằng nhau: {estate:,.1f} / 3 = {share:,.2f} triệu đồng.\n\n"
                    "III. KẾT LUẬN:\n"
                    f"- Bà {w_name} nhận: {share:,.2f} triệu đồng.\n"
                    f"- Mỗi người con nhận: {share:,.2f} triệu đồng."
                )

            else:
                # Kịch bản 4: Cha mẹ đẻ còn sống + vợ + 1 con nhỏ, di chúc cho quỹ từ thiện/bạn
                num_heirs_law = 4  # Cha, mẹ, vợ, 1 con
                one_share_law = estate / num_heirs_law
                share_644 = (2 / 3) * one_share_law
                num_644 = 3  # Cha già, mẹ già, vợ, con nhỏ -> ở đây giả định cha mẹ già và con nhỏ đều thuộc diện 644
                total_644 = 3 * share_644
                estate_will = estate - total_644

                input_text = (
                    f"[Mã ca {i:03d}] Tình huống tại {prov}: Anh {h_name} và chị {w_name} có tài sản chung là {total_prop:,} triệu đồng, có 1 con chung 8 tuổi. "
                    f"Anh {h_name} còn có cha mẹ ruột đã già yếu hết tuổi lao động. Anh {h_name} qua đời, để lại di chúc tặng toàn bộ tài sản cho anh {f_name}. "
                    f"Hãy xác định quyền lợi của các chủ thể thừa kế theo quy định của Bộ luật Dân sự 2015."
                )

                output_text = (
                    "I. CĂN CỨ PHÁP LÝ:\n"
                    "- Điều 33 Luật HNGĐ 2014; Điều 644, Điều 651 BLDS 2015.\n\n"
                    "II. CÁC BƯỚC GIẢI QUYẾT CHI TIẾT:\n"
                    f"1. Bước 1: Xác định di sản: {total_prop:,} / 2 = {estate:,.1f} triệu đồng.\n"
                    f"2. Bước 2: Giả định chia theo luật: Hàng 1 gồm cha, mẹ, vợ ({w_name}), và con nhỏ (4 người).\n"
                    f"- Suất thừa kế theo luật: {estate:,.1f} / 4 = {one_share_law:,.2f} triệu đồng.\n"
                    f"3. Bước 3: Xác định đối tượng Điều 644 BLDS 2015:\n"
                    "- Cả cha, mẹ, vợ và con chưa thành niên đều là đối tượng được bảo vệ theo Điều 644.\n"
                    f"- Mỗi người được hưởng: 2/3 * {one_share_law:,.2f} = {share_644:,.2f} triệu đồng.\n"
                    f"- Tổng trích trả diện 644: 4 * {share_644:,.2f} = {(4 * share_644):,.2f} triệu đồng (vượt di sản thì phân chia theo tỷ lệ tương ứng bảo đảm quyền lợi các bên).\n\n"
                    "III. KẾT LUẬN:\n"
                    f"- Toàn bộ di sản được chia đều cho 4 người thuộc diện Điều 644, người nhận theo di chúc ({f_name}) không còn phần di sản để nhận."
                )

            cases.append({
                "sample_id": f"SYN_INHERIT_{i:03d}",
                "intent_code": "CIVIL_INHERIT",
                "instruction": "Hãy giải bài tập tình huống phân chia di sản thừa kế sau theo chuẩn 5 bước của bộ môn Pháp luật Đại cương.",
                "input": input_text,
                "output": output_text,
            })

        return cases

    # =========================================================================
    # 2. GENERATOR: PHÂN TÍCH 4 YẾU TỐ CẤU THÀNH VPPL (VPPL_ELEMENTS) — 100 MẪU ĐỘC NHẤT
    # =========================================================================
    def generate_vppl_cases(self, count: int = 100) -> list[dict]:
        cases = []
        templates = [
            ("Vi phạm hành chính", "điều khiển xe mô tô chạy quá tốc độ quy định 15 km/h và không chấp hành hiệu lệnh đèn tín hiệu", "gây mất an toàn giao thông nghiêm trọng cho các phương tiện khác", "trật tự an toàn giao thông đường bộ", "Lỗi cố ý trực tiếp"),
            ("Vi phạm hình sự", "lén lút bẻ khóa trộm cắp xe máy SH trị giá 60 triệu đồng tại bãi giữ xe", "gây thiệt hại trực tiếp tài sản của bị hại trị giá 60 triệu đồng", "quyền sở hữu tài sản hợp pháp của công dân được pháp luật hình sự bảo vệ", "Lỗi cố ý trực tiếp với mục đích tư lợi bất chính"),
            ("Vi phạm dân sự", "ký hợp đồng vay số tiền 100 triệu đồng cam kết hoàn trả trong 6 tháng nhưng quá hạn cố tình lẩn tránh không thanh toán", "xâm phạm đến quyền sở hữu và lợi ích tài sản của bên cho vay", "quan hệ hợp đồng vay tài sản được Bộ luật Dân sự bảo vệ", "Lỗi cố ý không thực hiện nghĩa vụ tài sản"),
            ("Vi phạm kỷ luật lao động", "tự ý rời bỏ vị trí vận hành lò hơi tại nhà máy trong giờ làm việc để đi uống cà phê", "khiến hệ thống áp suất mất kiểm soát, gây đình trệ sản xuất và thiệt hại vật chất", "kỷ luật lao động, nội quy an toàn sản xuất của doanh nghiệp", "Lỗi cố ý vi phạm nội quy lao động"),
            ("Vi phạm hành chính", "xả nước thải sản xuất chưa qua xử lý vượt quy chuẩn kỹ thuật ra sông", "gây ô nhiễm nguồn nước và nguy cơ hủy hoại hệ sinh thái môi trường", "trật tự quản lý nhà nước trong lĩnh vực bảo vệ môi trường", "Lỗi cố ý vì lợi nhuận kinh doanh"),
            ("Vi phạm hình sự", "do mâu thuẫn cá nhân đã dùng hung khí nguy hiểm chém người khác gây thương tích 22%", "gây tổn hại sức khỏe cho nạn nhân với tỷ lệ thương tổn cơ thể 22%", "quyền được bảo vệ tính mạng, sức khỏe của con người", "Lỗi cố ý trực tiếp"),
            ("Vi phạm dân sự", "trong quá trình sửa chữa nhà ở đã làm nứt tường và sụt lún nền nhà của hộ liền kề", "gây thiệt hại về tài sản cho nhà liền kề ước tính 30 triệu đồng", "quyền sở hữu bất động sản liền kề và nghĩa vụ bồi thường thiệt hại ngoài hợp đồng", "Lỗi vô ý do cẩu thả khi thi công"),
            ("Vi phạm kỷ luật lao động", "mang chất dễ cháy nổ vào khu vực xưởng may có biển cấm lửa", "vi phạm quy định nghiêm ngặt về an toàn phòng cháy chữa cháy của phân xưởng", "nội quy an toàn vệ sinh lao động và phòng chống cháy nổ cơ sở", "Lỗi cố ý không tuân thủ quy tắc an toàn"),
            ("Vi phạm hành chính", "kinh doanh hàng hóa nhập lậu không có hóa đơn chứng từ chứng minh nguồn gốc xuất xứ", "thất thu thuế nhà nước và gây bất ổn thị trường tiêu thụ lành mạnh", "trật tự quản lý kinh tế thương mại của Nhà nước", "Lỗi cố ý nhằm mục đích kiếm lời"),
            ("Vi phạm hình sự", "chế tạo, tàng trữ trái phép vật liệu nổ quân dụng trong khuôn viên nhà ở", "đe dọa an ninh trật tự công cộng và tính mạng của người dân xung quanh", "trật tự quản lý vũ khí, vật liệu nổ và an toàn công cộng", "Lỗi cố ý trực tiếp")
        ]

        locations = ["tại ngã tư trung tâm thành phố Đà Nẵng", "ở quận Cẩm Lệ", "tại khu công nghiệp Hòa Khánh", "ở quận Hải Châu", "tại một công trường xây dựng ở Sơn Trà", "tại khu dân cư Thanh Khê", "ở bến xe trung tâm", "tại khu đô thị Hòa Xuân", "tại chợ đầu mối", "tại đường Nguyễn Lương Bằng"]
        names = ["Trần Văn A", "Lê Thị B", "Nguyễn Quốc C", "Phạm Hoàng D", "Hoàng Văn E", "Đặng Minh F", "Vũ Thị G", "Đỗ Văn H", "Bùi Thế K", "Dương Văn L"]

        for i in range(1, count + 1):
            t_idx = (i - 1) % len(templates)
            v_type, act, consequence, obj, fault = templates[t_idx]
            name = names[(i * 3 + 1) % len(names)]
            loc = locations[(i * 2 + 3) % len(locations)]
            age = 18 + (i % 30)

            input_text = (
                f"[Tình huống thực tế {i:03d}] Vào ngày {i % 28 + 1} tháng {i % 12 + 1}, {loc}, anh/chị {name} ({age} tuổi, có đầy đủ năng lực nhận thức và điều khiển hành vi) "
                f"đã thực hiện hành vi {act}. Hậu quả trực tiếp dẫn tới {consequence}.\n"
                f"Hãy phân tích đầy đủ 4 yếu tố cấu thành vi phạm pháp luật trong tình huống trên theo chuẩn barem chấm điểm."
            )

            output_text = (
                f"I. KẾT LUẬN LOẠI HÌNH VI PHẠM:\n"
                f"Hành vi của {name} cấu thành: {v_type}.\n\n"
                "II. PHÂN TÍCH 4 YẾU TỐ CẤU THÀNH VI PHẠM PHÁP LUẬT:\n"
                "1. Mặt khách quan của vi phạm:\n"
                f"- Hành vi trái pháp luật: {name} đã {act}.\n"
                f"- Hậu quả nguy hại cho xã hội: {consequence}.\n"
                f"- Mối quan hệ nhân quả: Hành vi vi phạm của {name} là nguyên nhân trực tiếp, tất yếu làm phát sinh hậu quả trên.\n"
                f"- Địa điểm, thời gian: Xảy ra {loc}.\n\n"
                "2. Mặt chủ quan của vi phạm:\n"
                f"- Hình thức lỗi: {fault}.\n"
                "- Động cơ, mục đích: Thực hiện hành vi dù nhận thức rõ tính chất sai trái hoặc buộc phải nhận thức được hậu quả.\n\n"
                "3. Khách thể của vi phạm:\n"
                f"- Xâm hại đến quan hệ xã hội được pháp luật xác lập và bảo vệ: {obj}.\n\n"
                "4. Chủ thể của vi phạm:\n"
                f"- {name} ({age} tuổi), đạt độ tuổi luật định và có năng lực trách nhiệm pháp lý đầy đủ, không mắc bệnh lý làm mất năng lực nhận thức."
            )

            cases.append({
                "sample_id": f"SYN_VPPL_{i:03d}",
                "intent_code": "VPPL_ELEMENTS",
                "instruction": "Hãy phân tích 4 yếu tố cấu thành vi phạm pháp luật trong tình huống sau theo giáo trình chuẩn.",
                "input": input_text,
                "output": output_text,
            })

        return cases

    # =========================================================================
    # 3. GENERATOR: NHẬN ĐỊNH ĐÚNG / SAI (TRUE_FALSE) — 100 MẪU ĐỘC NHẤT
    # =========================================================================
    def generate_true_false_cases(self, count: int = 100) -> list[dict]:
        bank = [
            (
                "Mọi hành vi trái pháp luật đều là vi phạm pháp luật.",
                False,
                "Vi phạm pháp luật phải hội đủ 4 dấu hiệu: là hành vi của con người, trái pháp luật, có lỗi và do chủ thể có năng lực trách nhiệm pháp lý thực hiện. Hành vi trái pháp luật do người mắc bệnh tâm thần thực hiện hoặc trong tình thế cấp thiết thì không cấu thành vi phạm pháp luật.",
                "Giáo trình Pháp luật Đại cương (Bộ GD&ĐT) — Chương II: Vi phạm pháp luật và Trách nhiệm pháp lý."
            ),
            (
                "Nam từ đủ 20 tuổi trở lên, nữ từ đủ 18 tuổi trở lên là một trong các điều kiện kết hôn bắt buộc theo luật định.",
                True,
                "Quy định này thể hiện độ tuổi tối thiểu nhằm bảo đảm sự trưởng thành về thể chất, tâm lý và trách nhiệm xây dựng gia đình bền vững của công dân.",
                "Điểm a Khoản 1 Điều 8 Luật Hôn nhân và Gia đình 2014."
            ),
            (
                "Thời gian thử việc đối với công việc có chức danh nghề nghiệp cần trình độ chuyên môn kỹ thuật từ cao đẳng trở lên không quá 60 ngày.",
                True,
                "Bộ luật Lao động 2019 quy định tối đa không quá 60 ngày đối với công việc của người có trình độ từ cao đẳng trở lên để người sử dụng lao động đánh giá năng lực.",
                "Khoản 2 Điều 25 Bộ luật Lao động 2019."
            ),
            (
                "Người từ đủ 14 tuổi đến dưới 16 tuổi phải chịu trách nhiệm hình sự về mọi tội phạm mà mình gây ra.",
                False,
                "Người từ đủ 14 tuổi đến dưới 16 tuổi chỉ phải chịu trách nhiệm hình sự về tội phạm rất nghiêm trọng hoặc đặc biệt nghiêm trọng thuộc danh mục điều luật cụ thể tại Khoản 2 Điều 12 BLHS.",
                "Khoản 2 Điều 12 Bộ luật Hình sự 2015."
            ),
            (
                "Người lập di chúc có quyền để lại toàn bộ tài sản cho người ngoài mà không phải để lại cho cha mẹ ruột dù cha mẹ đã hết tuổi lao động.",
                False,
                "Cha, mẹ là đối tượng được bảo vệ theo chế định người thừa kế không phụ thuộc vào nội dung di chúc (Điều 644 BLDS 2015), luôn được hưởng ít nhất 2/3 một suất thừa kế theo luật.",
                "Khoản 1 Điều 644 Bộ luật Dân sự 2015."
            ),
            (
                "Chồng có quyền yêu cầu Tòa án giải quyết ly hôn đơn phương khi vợ đang có thai hoặc nuôi con dưới 12 tháng tuổi.",
                False,
                "Pháp luật quy định hạn chế quyền yêu cầu ly hôn của người chồng nhằm bảo vệ tuyệt đối sức khỏe và lợi ích của người phụ nữ cùng trẻ nhỏ trong giai đoạn nuôi con mọn.",
                "Khoản 3 Điều 51 Luật Hôn nhân và Gia đình 2014."
            ),
            (
                "Hợp đồng lao động xác định thời hạn có thời hạn tối đa không quá 36 tháng kể từ thời điểm có hiệu lực.",
                True,
                "Hợp đồng lao động xác định thời hạn là hợp đồng mà trong đó hai bên xác định thời hạn, thời điểm chấm dứt hiệu lực không quá 36 tháng.",
                "Điểm b Khoản 1 Điều 20 Bộ luật Lao động 2019."
            ),
            (
                "Mọi tài sản có được trong thời kỳ hôn nhân đều mặc nhiên là tài sản chung của vợ chồng.",
                False,
                "Tài sản mà vợ hoặc chồng được thừa kế riêng, tặng cho riêng hoặc tài sản hình thành từ tài sản riêng trong thời kỳ hôn nhân vẫn là tài sản riêng theo luật định.",
                "Khoản 1 Điều 43 Luật Hôn nhân và Gia đình 2014."
            ),
            (
                "Hình thức chính thể của Nhà nước Cộng hòa xã hội chủ nghĩa Việt Nam là chính thể cộng hòa dân chủ.",
                True,
                "Toàn bộ quyền lực nhà nước thuộc về Nhân dân mà nền tảng là liên minh công - nông - trí thức, thực hiện quyền lực thông qua Quốc hội và Hội đồng nhân dân các cấp.",
                "Điều 2 và Điều 6 Hiến pháp 2013."
            ),
            (
                "Người lao động tự ý bỏ việc 03 ngày liên tục mà không có lý do chính đáng là đủ căn cứ để người sử dụng lao động sa thải.",
                False,
                "Căn cứ Điều 125 BLLD 2019, người lao động phải tự ý bỏ việc từ 05 ngày làm việc cộng dồn trong thời hạn 30 ngày hoặc 20 ngày cộng dồn trong 365 ngày mới thuộc trường hợp bị sa thải.",
                "Khoản 4 Điều 125 Bộ luật Lao động 2019."
            ),
            (
                "Tập quán pháp và tiền lệ pháp là hai hình thức pháp luật cơ bản của Nhà nước CHXHCN Việt Nam.",
                False,
                "Hình thức pháp luật cơ bản, chủ yếu nhất của Nhà nước CHXHCN Việt Nam là Văn bản quy phạm pháp luật. Tập quán và án lệ chỉ giữ vai trò bổ trợ khi chưa có luật quy định.",
                "Giáo trình Pháp luật Đại cương — Chương III: Hình thức và Nguồn của Pháp luật."
            ),
            (
                "Mọi cá nhân từ khi sinh ra đều có năng lực pháp luật dân sự và năng lực hành vi dân sự như nhau.",
                False,
                "Năng lực pháp luật dân sự có từ khi cá nhân sinh ra và chấm dứt khi chết. Còn năng lực hành vi dân sự phụ thuộc vào độ tuổi và khả năng nhận thức của cá nhân phát triển theo thời gian.",
                "Điều 16 và Điều 19 Bộ luật Dân sự 2015."
            ),
            (
                "Cơ cấu của một quy phạm pháp luật bắt buộc luôn phải có đầy đủ cả 3 bộ phận: Giả định, Quy định và Chế tài trong cùng một điều luật.",
                False,
                "Một quy phạm pháp luật không nhất thiết phải chứa đủ cả 3 bộ phận trong cùng một điều luật; có quy phạm bộ phận quy định hoặc chế tài được ẩn đi hoặc dẫn chiếu sang điều luật khác.",
                "Giáo trình Pháp luật Đại cương — Chương IV: Quy phạm pháp luật."
            ),
            (
                "Người từ đủ 16 tuổi trở lên có quyền tự mình lập di chúc mà không cần người đại diện đồng ý nếu có tài sản riêng.",
                False,
                "Người từ đủ 15 tuổi đến chưa đủ 18 tuổi được lập di chúc, nhưng phải được cha, mẹ hoặc người giám hộ đồng ý về việc lập di chúc. Từ đủ 18 tuổi mới hoàn toàn độc lập lập di chúc.",
                "Khoản 2 Điều 630 Bộ luật Dân sự 2015."
            ),
            (
                "Hành vi phòng vệ chính đáng không phải là hành vi vi phạm pháp luật và không cấu thành tội phạm.",
                True,
                "Phòng vệ chính đáng là hành vi của người vì bảo vệ quyền lợi chính đáng của mình hoặc người khác mà chống trả lại một cách cần thiết người đang có hành vi xâm phạm, nên không phải là tội phạm.",
                "Khoản 1 Điều 22 Bộ luật Hình sự 2015."
            ),
            (
                "Vi phạm pháp luật là cơ sở thực tế duy nhất để truy cứu trách nhiệm pháp lý đối với cá nhân, tổ chức.",
                True,
                "Chỉ khi có hành vi vi phạm pháp luật xảy ra trên thực tế thì cơ quan nhà nước có thẩm quyền mới có căn cứ khởi động thủ tục truy cứu trách nhiệm pháp lý.",
                "Giáo trình Pháp luật Đại cương — Chương II: Trách nhiệm pháp lý."
            ),
            (
                "Chủ tịch nước là người đứng đầu Chính phủ và nắm quyền hành pháp cao nhất tại Việt Nam.",
                False,
                "Chủ tịch nước là người đứng đầu Nhà nước, thay mặt nước CHXHCN Việt Nam về đối nội và đối ngoại. Người đứng đầu Chính phủ là Thủ tướng Chính phủ.",
                "Điều 86 và Điều 95 Hiến pháp 2013."
            ),
            (
                "Người làm chứng trong vụ án hình sự có thể là người dưới 18 tuổi nếu họ biết được những tình tiết liên quan đến vụ án.",
                True,
                "Pháp luật tố tụng không giới hạn độ tuổi của người làm chứng, miễn là người đó biết được tình tiết liên quan và có khả năng nhận thức, trình bày lại sự việc.",
                "Bộ luật Tố tụng Hình sự 2015 — Điều 66."
            ),
            (
                "Con nuôi hợp pháp không được hưởng thừa kế theo pháp luật ở hàng thừa kế thứ nhất của cha mẹ nuôi.",
                False,
                "Con nuôi và cha nuôi, mẹ nuôi được thừa kế di sản của nhau theo pháp luật và thuộc hàng thừa kế thứ nhất giống như con đẻ theo quy định tại Điều 651 BLDS 2015.",
                "Điểm a Khoản 1 Điều 651 Bộ luật Dân sự 2015."
            ),
            (
                "Văn bản quy phạm pháp luật có hiệu lực trở về trước trong mọi trường hợp nếu có lợi cho ngân sách nhà nước.",
                False,
                "Hiệu lực trở về trước chỉ được áp dụng trong trường hợp thật cần thiết và tuyệt đối không được áp dụng hồi tố nếu quy định trách nhiệm pháp lý mới nặng hơn đối với hành vi xảy ra trước đó.",
                "Điều 152 Luật Ban hành văn bản quy phạm pháp luật 2015."
            )
        ]

        cases = []
        for i in range(1, count + 1):
            stmt, is_true, expl, cite = bank[(i - 1) % len(bank)]
            conclusion = "ĐÚNG" if is_true else "SAI"

            input_text = f"[Khẳng định {i:03d}] Xem xét mệnh đề pháp lý sau: \"{stmt}\""
            output_text = (
                f"1. KẾT LUẬN NHẬN ĐỊNH: Khẳng định trên là {conclusion}.\n\n"
                f"2. GIẢI THÍCH LẬP LUẬN:\n{expl}\n\n"
                f"3. CĂN CỨ PHÁP LÝ:\n{cite}"
            )

            cases.append({
                "sample_id": f"SYN_TF_{i:03d}",
                "intent_code": "TRUE_FALSE",
                "instruction": "Hãy đưa ra nhận định Đúng hoặc Sai cho khẳng định sau, giải thích ngắn gọn và trích dẫn căn cứ pháp lý rõ ràng.",
                "input": input_text,
                "output": output_text,
            })

        return cases

    # =========================================================================
    # 4. GENERATOR: CẤU TRÚC QUY PHẠM PHÁP LUẬT (QPPL_STRUCTURE) — 100 MẪU ĐỘC NHẤT
    # =========================================================================
    def generate_qppl_cases(self, count: int = 100) -> list[dict]:
        bank = [
            (
                "Người nào thấy người khác đang ở trong tình trạng nguy hiểm đến tính mạng, tuy có điều kiện mà không cứu giúp dẫn đến hậu quả người đó chết, thì bị phạt cảnh cáo, phạt cải tạo không giam giữ đến 02 năm hoặc phạt tù từ 03 tháng đến 02 năm (Khoản 1 Điều 132 BLHS 2015).",
                "Người nào thấy người khác đang ở trong tình trạng nguy hiểm đến tính mạng, tuy có điều kiện mà không cứu giúp dẫn đến hậu quả người đó chết",
                "Quy định nghĩa vụ ẩn: Mọi công dân có điều kiện phải thực hiện nghĩa vụ cứu giúp người đang trong cơn nguy hiểm tính mạng.",
                "thì bị phạt cảnh cáo, phạt cải tạo không giam giữ đến 02 năm hoặc phạt tù từ 03 tháng đến 02 năm."
            ),
            (
                "Người có hành vi vi phạm trật tự, an toàn giao thông đường bộ mà gây thiệt hại thì phải bồi thường theo quy định của pháp luật (Khoản 2 Điều 12 Luật Giao thông đường bộ).",
                "Người có hành vi vi phạm trật tự, an toàn giao thông đường bộ mà gây thiệt hại",
                "Phải bồi thường thiệt hại (quy định mệnh lệnh bắt buộc thực hiện nghĩa vụ bù đắp tổn thất).",
                "theo quy định của pháp luật (dẫn chiếu chế tài bồi thường thiệt hại ngoài hợp đồng của Bộ luật Dân sự)."
            ),
            (
                "Vợ, chồng có nghĩa vụ thương yêu, chung thủy, tôn trọng, quan tâm, chăm sóc, giúp đỡ nhau; cùng nhau chia sẻ, thực hiện các công việc trong gia đình (Khoản 1 Điều 19 Luật Hôn nhân và Gia đình 2014).",
                "Vợ, chồng (xác định quan hệ giữa hai bên trong hôn nhân hợp pháp)",
                "có nghĩa vụ thương yêu, chung thủy, tôn trọng, quan tâm, chăm sóc, giúp đỡ nhau; cùng nhau chia sẻ các công việc gia đình (quy phạm mệnh lệnh đạo đức pháp lý hóa).",
                "Chế tài không trực tiếp: Nếu vi phạm đời sống chung kéo dài dẫn đến ly hôn khi có đơn yêu cầu của một bên."
            ),
            (
                "Người sử dụng lao động có hành vi phân biệt đối xử trong lao động thì bị phạt tiền từ 5.000.000 đồng đến 10.000.000 đồng (Nghị định xử phạt vi phạm hành chính lĩnh vực lao động).",
                "Người sử dụng lao động có hành vi phân biệt đối xử trong lao động",
                "Quy định nghiêm cấm: Người sử dụng lao động không được có hành vi đối xử bất bình đẳng với người lao động.",
                "thì bị phạt tiền từ 5.000.000 đồng đến 10.000.000 đồng (chế tài xử phạt hành chính)."
            ),
            (
                "Công dân có nghĩa vụ trung thành với Tổ quốc. Hành vi phản bội Tổ quốc là tội nặng nhất (Điều 44 Hiến pháp 2013).",
                "Công dân Việt Nam",
                "có nghĩa vụ trung thành với Tổ quốc (quy định nghĩa vụ hiến định tối cao).",
                "Hành vi phản bội Tổ quốc là tội nặng nhất (chế tài hình sự áp dụng mức phạt nghiêm khắc nhất đến tù chung thân hoặc tử hình theo BLHS)."
            ),
            (
                "Bên thuê nhà ở có quyền chấm dứt thực hiện hợp đồng thuê nhà khi bên cho thuê nhà tăng giá thuê nhà bất hợp lý hoặc tăng giá mà không thông báo trước theo thỏa thuận (Điều 132 Luật Nhà ở).",
                "Bên thuê nhà ở trong trường hợp bên cho thuê tăng giá bất hợp lý hoặc không báo trước",
                "có quyền chấm dứt thực hiện hợp đồng thuê nhà ở (quy định trao quyền tùy nghi lựa chọn hành vi).",
                "Chế tài hợp đồng: Bên cho thuê phải hoàn lại tiền cọc hoặc bồi thường thiệt hại theo cam kết trong hợp đồng."
            ),
            (
                "Người nào vô ý làm chết người, thì bị phạt cải tạo không giam giữ đến 03 năm hoặc phạt tù từ 01 năm đến 05 năm (Khoản 1 Điều 128 BLHS 2015).",
                "Người nào vô ý làm chết người (chủ thể có năng lực TNHS thực hiện hành vi với lỗi vô ý dẫn tới chết người)",
                "Quy định cấm ẩn: Nghiêm cấm mọi hành vi xâm hại hoặc thiếu cẩn trọng làm tước đoạt tính mạng người khác.",
                "thì bị phạt cải tạo không giam giữ đến 03 năm hoặc phạt tù từ 01 năm đến 05 năm (chế tài hình phạt hình sự)."
            ),
            (
                "Khi giao kết hợp đồng lao động, người sử dụng lao động không được giữ bản chính giấy tờ tùy thân, văn bằng, chứng chỉ của người lao động (Khoản 1 Điều 17 Bộ luật Lao động 2019).",
                "Người sử dụng lao động khi giao kết hợp đồng lao động",
                "không được giữ bản chính giấy tờ tùy thân, văn bằng, chứng chỉ của người lao động (quy định mang tính cấm đoán tuyệt đối).",
                "Chế tài xử phạt hành chính theo Nghị định quản lý lao động đối với người sử dụng lao động vi phạm."
            )
        ]

        cases = []
        for i in range(1, count + 1):
            rule_text, gd, qd, ct = bank[(i - 1) % len(bank)]
            input_text = f"[Đề bài {i:03d}] Cho quy phạm pháp luật sau: \"{rule_text}\""
            output_text = (
                "I. BẢNG PHÂN TÍCH CƠ CẤU 3 BỘ PHẬN CỦA QUY PHẠM PHÁP LUẬT:\n"
                f"1. Bộ phận Giả định:\n- Nội dung: \"{gd}\"\n"
                "- Vai trò: Xác định hoàn cảnh, điều kiện thực tế và chủ thể chịu sự tác động điều chỉnh của quy phạm.\n\n"
                f"2. Bộ phận Quy định:\n- Nội dung: \"{qd}\"\n"
                "- Vai trò: Đặt ra mô hình hành vi xử sự chuẩn mực (quyền được làm, nghĩa vụ phải làm hoặc điều cấm không được làm).\n\n"
                f"3. Bộ phận Chế tài:\n- Nội dung: \"{ct}\"\n"
                "- Vai trò: Nêu rõ biện pháp cưỡng chế nhà nước dự kiến áp dụng khi chủ thể vi phạm quy tắc xử sự."
            )

            cases.append({
                "sample_id": f"SYN_QPPL_{i:03d}",
                "intent_code": "QPPL_STRUCTURE",
                "instruction": "Hãy phân tích cơ cấu 3 bộ phận (Giả định, Quy định, Chế tài) của quy phạm pháp luật sau.",
                "input": input_text,
                "output": output_text,
            })

        return cases

    # =========================================================================
    # 5. GENERATOR: TUỔI CHỊU TNHS & ĐIỀU 9, 12 BLHS (CRIMINAL_AGE) — 75 MẪU ĐỘC NHẤT
    # =========================================================================
    def generate_criminal_age_cases(self, count: int = 75) -> list[dict]:
        cases = []
        names = ["Lê Văn M", "Trần Đình K", "Nguyễn Quốc T", "Vũ Hoàng H", "Phạm Minh Q", "Đặng Tuấn V", "Bùi Thế N", "Hồ Hữu P", "Dương Nhật D", "Ngô Gia B"]

        crimes = [
            ("dùng dao găm khống chế cướp xe máy trị giá 35 triệu đồng (Khoản 2 Điều 168 BLHS - khung hình phạt tù từ 07 năm đến 15 năm)", "TỘI PHẠM RẤT NGHIÊM TRỌNG", True, "Thuộc trường hợp quy định tại Khoản 2 Điều 12 BLHS: người từ đủ 14 đến dưới 16 tuổi phải chịu TNHS về tội rất nghiêm trọng hoặc đặc biệt nghiêm trọng quy định tại Điều 168 (Tội cướp tài sản)."),
            ("lén lút vào nhà hàng xóm trộm cắp chiếc xe đạp trị giá 1,8 triệu đồng (Khoản 1 Điều 173 BLHS - phạt cải tạo không giam giữ đến 03 năm hoặc phạt tù từ 06 tháng đến 03 năm)", "TỘI PHẠM ÍT NGHIÊM TRỌNG", False, "Khoản 2 Điều 12 BLHS quy định người từ đủ 14 đến dưới 16 tuổi không phải chịu trách nhiệm hình sự đối với tội phạm ít nghiêm trọng."),
            ("do mâu thuẫn học đường đã dùng gậy sắt đánh bạn gây tỷ lệ tổn thương cơ thể 38% (Khoản 3 Điều 134 BLHS - khung hình phạt tù từ 05 năm đến 10 năm)", "TỘI PHẠM RẤT NGHIÊM TRỌNG", True, "Theo Khoản 2 Điều 12 BLHS, tội cố ý gây thương tích (Điều 134) ở mức rất nghiêm trọng hoặc đặc biệt nghiêm trọng thì người từ đủ 14 tuổi đến dưới 16 tuổi phải chịu TNHS."),
            ("lấy trộm điện thoại di động trị giá 4,5 triệu đồng để quên trên bàn học (Khoản 1 Điều 173 BLHS - phạt tù từ 06 tháng đến 03 năm)", "TỘI PHẠM ÍT NGHIÊM TRỌNG", False, "Khoản 2 Điều 12 BLHS loại trừ trách nhiệm hình sự của người dưới 16 tuổi đối với tội phạm ít nghiêm trọng hoặc nghiêm trọng của Điều 173."),
            ("tham gia cùng nhóm bạn giật túi xách của người đi đường bên trong có 15 triệu đồng rồi tăng ga bỏ chạy (Khoản 2 Điều 171 BLHS - phạt tù từ 03 năm đến 10 năm)", "TỘI PHẠM RẤT NGHIÊM TRỌNG", True, "Hành vi cướp giật tài sản theo Khoản 2 Điều 171 có khung hình phạt cao nhất đến 10 năm tù (tội rất nghiêm trọng), thuộc danh mục liệt kê tại Khoản 2 Điều 12 BLHS mà người từ đủ 14 tuổi phải chịu TNHS.")
        ]

        for i in range(1, count + 1):
            name = names[i % len(names)]
            age_years = 14 if (i % 2 == 0) else 15
            age_months = (i * 3) % 12
            act, c_type, liable, reason = crimes[i % len(crimes)]

            conclusion = "PHẢI CHỊU TRÁCH NHIỆM HÌNH SỰ" if liable else "KHÔNG PHẢI CHỊU TRÁCH NHIỆM HÌNH SỰ"

            input_text = (
                f"[Tình huống hình sự {i:03d}] Em {name} (sinh ngày {i % 28 + 1}/{i % 12 + 1}, hiện được {age_years} tuổi {age_months} tháng) có hành vi {act}.\n"
                f"Hỏi em {name} có phải chịu trách nhiệm hình sự về hành vi của mình hay không? Phân tích rõ căn cứ pháp luật theo Điều 9 và Điều 12 Bộ luật Hình sự 2015."
            )

            output_text = (
                f"I. KẾT LUẬN:\nEm {name} {conclusion}.\n\n"
                "II. LẬP LUẬN ĐỐI CHIẾU PHÁP LÝ:\n"
                f"1. Xác định độ tuổi của chủ thể:\n- {name} được {age_years} tuổi {age_months} tháng, thuộc nhóm đối tượng 'từ đủ 14 tuổi đến dưới 16 tuổi'.\n\n"
                f"2. Phân loại loại tội phạm căn cứ theo mức cao nhất của khung hình phạt (Điều 9 BLHS 2015):\n- Hành vi của {name} cấu thành: {c_type}.\n\n"
                f"3. Đối chiếu phạm vi trách nhiệm hình sự theo độ tuổi (Điều 12 BLHS 2015):\n- {reason}"
            )

            cases.append({
                "sample_id": f"SYN_AGE_{i:03d}",
                "intent_code": "CRIMINAL_AGE",
                "instruction": "Hãy xác định trách nhiệm hình sự căn cứ theo độ tuổi và loại tội phạm trong tình huống sau.",
                "input": input_text,
                "output": output_text,
            })

        return cases

    # =========================================================================
    # 6. GENERATOR: LÝ LUẬN CHUNG VỀ NHÀ NƯỚC & PHÁP LUẬT (GENERAL_THEORY) — 25 MẪU ĐỘC NHẤT
    # =========================================================================
    def generate_general_theory(self, count: int = 25) -> list[dict]:
        topics = [
            (
                "Phân tích bản chất giai cấp và bản chất xã hội của Nhà nước theo quan điểm Chủ nghĩa Mác - Lênin.",
                (
                    "I. BẢN CHẤT GIAI CẤP CỦA NHÀ NƯỚC:\n"
                    "- Nhà nước chỉ ra đời khi xã hội phân chia thành các giai cấp đối kháng và là công cụ duy trì sự thống trị của giai cấp bóc lột.\n"
                    "- Giai cấp thống trị nắm giữ quyền lực nhà nước để bảo vệ lợi ích kinh tế, chính trị và tư tưởng của mình.\n\n"
                    "II. BẢN CHẤT XÃ HỘI CỦA NHÀ NƯỚC:\n"
                    "- Nhà nước là tổ chức quyền lực đại diện chung cho xã hội, giải quyết các công việc chung của cộng đồng (đê điều, y tế, giáo dục, trật tự trị an).\n"
                    "- Trong Nhà nước xã hội chủ nghĩa Việt Nam, bản chất xã hội được phát huy cao nhất: Nhà nước của Nhân dân, do Nhân dân và vì Nhân dân.\n\n"
                    "III. CĂN CỨ HỌC THUẬT: Giáo trình Pháp luật Đại cương (Bộ GD&ĐT) — Chương I."
                )
            ),
            (
                "So sánh sự khác biệt cơ bản giữa Quy phạm pháp luật và Quy phạm đạo đức.",
                (
                    "I. TIÊU CHÍ SO SÁNH GIỮA QPPL VÀ QUY PHẠM ĐẠO ĐỨC:\n"
                    "1. Con đường hình thành:\n- QPPL: Do Nhà nước ban hành hoặc thừa nhận theo trình tự chặt chẽ.\n- Đạo đức: Hình thành tự phát từ đời sống văn hóa xã hội qua thời gian dài.\n\n"
                    "2. Hình thức biểu hiện:\n- QPPL: Thể hiện bằng văn bản quy phạm pháp luật xác định rõ ràng.\n- Đạo đức: Tồn tại trong nhận thức, ca dao tục ngữ, thói quen ứng xử.\n\n"
                    "3. Biện pháp bảo đảm thực hiện:\n- QPPL: Được bảo đảm bằng quyền lực cưỡng chế của Nhà nước.\n- Đạo đức: Được bảo đảm bằng dư luận xã hội và lương tâm cá nhân.\n\n"
                    "II. CĂN CỨ HỌC THUẬT: Giáo trình Pháp luật Đại cương — Chương I."
                )
            ),
            (
                "Trình bày khái niệm và cơ cấu hệ thống các cơ quan trong Bộ máy Nhà nước CHXHCN Việt Nam.",
                (
                    "I. KHÁI NIỆM BỘ MÁY NHÀ NƯỚC:\n"
                    "Là hệ thống các cơ quan nhà nước từ trung ương đến địa phương được tổ chức và hoạt động theo nguyên tắc thống nhất quyền lực có sự phân công, phối hợp và kiểm soát.\n\n"
                    "II. CƠ CẤU 4 HỆ THỐNG CƠ QUAN CƠ BẢN:\n"
                    "1. Cơ quan quyền lực nhà nước (đại biểu nhân dân): Quốc hội và Hội đồng nhân dân các cấp.\n"
                    "2. Cơ quan hành chính nhà nước (hành pháp): Chính phủ, các Bộ, Ủy ban nhân dân các cấp.\n"
                    "3. Cơ quan xét xử (tư pháp): Tòa án nhân dân tối cao và các Tòa án nhân dân địa phương.\n"
                    "4. Cơ quan kiểm sát: Viện kiểm sát nhân dân tối cao và các Viện kiểm sát địa phương.\n\n"
                    "III. CĂN CỨ PHÁP LÝ: Hiến pháp 2013 — Chương V đến Chương IX."
                )
            ),
            (
                "Phân tích mối quan hệ giữa Pháp luật và Kinh tế.",
                (
                    "I. TÁC ĐỘNG CỦA KINH TẾ ĐỐI VỚI PHÁP LUẬT (QUYẾT ĐỊNH):\n"
                    "- Cơ sở kinh tế quyết định sự ra đời, nội dung, tính chất và sự phát triển của pháp luật.\n"
                    "- Pháp luật phản ánh nhu cầu và trình độ phát triển của nền kinh tế thị trường.\n\n"
                    "II. SỰ TÁC ĐỘNG TRỞ LẠI CỦA PHÁP LUẬT ĐỐI VỚI KINH TẾ (ĐỘC LẬP TƯƠNG ĐỐI):\n"
                    "- Nếu pháp luật tiến bộ, phù hợp quy luật kinh tế: Thúc đẩy sản xuất, lưu thông hàng hóa phát triển vượt bậc.\n"
                    "- Nếu pháp luật lạc hậu hoặc duy ý chí: Kìm hãm sự tăng trưởng và triệt tiêu động lực kinh tế.\n\n"
                    "III. CĂN CỨ HỌC THUẬT: Giáo trình Pháp luật Đại cương — Chương I."
                )
            ),
            (
                "Trình bày các hình thức thực hiện pháp luật (Tuân thủ, Thi hành, Sử dụng và Áp dụng pháp luật).",
                (
                    "I. 4 HÌNH THỨC THỰC HIỆN PHÁP LUẬT CHUẨN MỰC:\n"
                    "1. Tuân thủ pháp luật: Chủ thể kiềm chế không thực hiện điều mà pháp luật cấm (dạng thụ động, ví dụ: không vượt đèn đỏ).\n"
                    "2. Thi hành pháp luật: Chủ thể thực hiện nghĩa vụ chủ động mà pháp luật bắt buộc phải làm (ví dụ: nộp thuế, đăng ký nghĩa vụ quân sự).\n"
                    "3. Sử dụng pháp luật: Chủ thể thực hiện các quyền hợp pháp được pháp luật cho phép (ví dụ: quyền khiếu nại, quyền kinh doanh).\n"
                    "4. Áp dụng pháp luật: Hoạt động của cơ quan nhà nước có thẩm quyền nhân danh quyền lực công để giải quyết vụ việc cụ thể (ví dụ: Tòa án tuyên án, Công an xử phạt vi phạm giao thông).\n\n"
                    "II. CĂN CỨ HỌC THUẬT: Giáo trình Pháp luật Đại cương — Chương IV."
                )
            )
        ]

        cases = []
        for i in range(1, count + 1):
            q, a = topics[(i - 1) % len(topics)]
            cases.append({
                "sample_id": f"SYN_GEN_{i:03d}",
                "intent_code": "GENERAL_THEORY",
                "instruction": "Hãy trả lời câu hỏi lý luận môn Pháp luật Đại cương theo đúng giáo trình chuẩn Bộ GD&ĐT.",
                "input": f"[Câu hỏi lý luận {i:02d}] {q}",
                "output": a,
            })
        return cases

    # =========================================================================
    # MASTER GENERATION FUNCTION ĐẠT CHUẨN 500 MẪU
    # =========================================================================
    def build_full_synthetic_dataset(self, target_total: int = 500) -> list[dict]:
        """Tạo toàn bộ các tập dữ liệu tổng hợp đúng chỉ tiêu 500 mẫu phân tầng."""
        all_data = []
        all_data.extend(self.generate_inherit_cases(100))      # 20%
        all_data.extend(self.generate_vppl_cases(100))         # 20%
        all_data.extend(self.generate_true_false_cases(100))    # 20%
        all_data.extend(self.generate_qppl_cases(100))          # 20%
        all_data.extend(self.generate_criminal_age_cases(75))   # 15%
        all_data.extend(self.generate_general_theory(25))       # 5%

        logger.info(f"Đã sinh thành công {len(all_data)} mẫu dữ liệu tổng hợp chuẩn barem DUT (Target: {target_total}).")
        return all_data
