"""
VietLawAssist — Framework SFT Samples Generator
===============================================
Module biên soạn các mẫu huấn luyện SFT chuyên sâu từ tài liệu phương pháp luận
môn Pháp luật Đại cương (studocu_framework_phap_luat_dai_cuong_cleaned.md).
"""

import json
import hashlib
from pathlib import Path
from loguru import logger

from .config import PROCESSED_DIR, DATA_DIR, KAGGLE_BUNDLE_DIR
from .sft_builder import validate_sft_sample, get_existing_db_article_ids, convert_to_chatml
from .split_sft import split_sft_stratified
from .kaggle_bundle import compute_md5

def create_framework_sft_samples() -> list[dict]:
    """
    Biên soạn các mẫu câu hỏi - đáp SFT chuẩn mực cao, giải thích từng bước (Chain-of-Thought).
    """
    samples = [
        # MẪU 1: CẤU TRÚC QUY PHẠM PHÁP LUẬT & QUY ĐỊNH ẨN
        {
            "source_file": "studocu_framework_phap_luat_dai_cuong_cleaned.md",
            "question_number": 1,
            "intent_code": "QPPL_STRUCTURE",
            "instruction": "Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng QPPL_STRUCTURE.",
            "input": (
                "Cho quy phạm pháp luật sau:\n"
                "\"Người nào điều khiển xe mô tô, xe gắn máy mà không đội mũ bảo hiểm hoặc đội mũ bảo hiểm "
                "không cài quai đúng quy cách thì bị phạt tiền từ 400.000 đồng đến 600.000 đồng.\"\n"
                "Hãy phân tích cơ cấu của quy phạm pháp luật trên (chỉ rõ Giả định, Quy định, Chế tài). "
                "Xác định phương thức thể hiện của quy phạm này trong văn bản quy phạm pháp luật."
            ),
            "output": (
                "I. CƠ CẤU 3 BỘ PHẬN CỦA QUY PHẠM PHÁP LUẬT:\n\n"
                "1. Bộ phận Giả định:\n"
                "- Nội dung: \"Người nào điều khiển xe mô tô, xe gắn máy mà không đội mũ bảo hiểm hoặc đội mũ bảo hiểm không cài quai đúng quy cách\".\n"
                "- Ý nghĩa: Xác định chủ thể (người điều khiển xe mô tô, xe gắn máy) và hoàn cảnh, điều kiện thực tế mà quy phạm pháp luật dự liệu sẽ tác động.\n\n"
                "2. Bộ phận Quy định (Quy định ẩn):\n"
                "- Nội dung: Trong điều luật trên, bộ phận quy định bị ẩn đi. Quy định ngầm hiểu ở đây là: \"Phải đội mũ bảo hiểm và cài quai đúng quy cách khi điều khiển xe mô tô, xe gắn máy tham gia giao thông\".\n"
                "- Ý nghĩa: Xác định quy tắc xử sự mang tính mệnh lệnh bắt buộc mà Nhà nước yêu cầu chủ thể phải thực hiện.\n\n"
                "3. Bộ phận Chế tài:\n"
                "- Nội dung: \"thì bị phạt tiền từ 400.000 đồng đến 600.000 đồng\".\n"
                "- Ý nghĩa: Xác định biện pháp cưỡng chế hành chính bất lợi mà Nhà nước áp dụng đối với chủ thể vi phạm không thực hiện đúng bộ phận quy định.\n\n"
                "II. PHƯƠNG THỨC THỂ HIỆN CỦA QUY PHẠM:\n"
                "- Quy phạm trên được thể hiện theo phương thức: \"Quy định ẩn\".\n"
                "- Giải thích: Kỹ thuật lập pháp đã lồng ghép trực tiếp hành vi vi phạm vào phần giả định kèm theo chế tài xử phạt, ẩn đi mệnh lệnh xử sự bắt buộc (quy định) vì quy tắc này đã hiển nhiên hoặc được quy định chi tiết tại các điều khoản về quy tắc giao thông đường bộ."
            ),
            "has_answer": True,
        },

        # MẪU 2: PHÂN BIỆT 4 PHƯƠNG THỨC THỂ HIỆN QPPL
        {
            "source_file": "studocu_framework_phap_luat_dai_cuong_cleaned.md",
            "question_number": 2,
            "intent_code": "QPPL_STRUCTURE",
            "instruction": "Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng QPPL_STRUCTURE.",
            "input": (
                "Trong kỹ thuật lập pháp, các bộ phận của quy phạm pháp luật (Giả định, Quy định, Chế tài) "
                "được thể hiện qua những phương thức nào trong văn bản quy phạm pháp luật? Hãy trình bày bản chất "
                "và cho ví dụ minh họa ngắn gọn đối với từng phương thức."
            ),
            "output": (
                "Trong kỹ thuật xây dựng văn bản quy phạm pháp luật, có 4 phương thức thể hiện cơ bản:\n\n"
                "1. Phương thức Trực tiếp:\n"
                "- Bản chất: Điều luật trình bày trực tiếp, đầy đủ cả 3 bộ phận Giả định, Quy định và Chế tài ngay trong một điều khoản mà không cần dẫn chiếu hay suy đoán.\n"
                "- Ví dụ: Điều khoản quy định nếu công chức có hành vi nhũng nhiễu (giả định), phải báo cáo trung thực (quy định), nếu không báo cáo thì bị khiển trách hoặc cảnh cáo (chế tài).\n\n"
                "2. Phương thức Quy định ẩn:\n"
                "- Bản chất: Điều luật chỉ trực tiếp nêu Giả định và Chế tài xử phạt, bộ phận Quy định (quy tắc xử sự cho phép/bắt buộc/cấm đoán) bị ẩn đi và được suy ra từ điều cấm hoặc chế tài.\n"
                "- Ví dụ: \"Người nào trộm cắp tài sản của người khác có giá trị từ 2 triệu đồng đến dưới 50 triệu đồng thì bị phạt cải tạo không giam giữ đến 03 năm hoặc phạt tù từ 06 tháng đến 03 năm\" (Điều 173 BLHS 2015). Quy định ẩn là: Nghiêm cấm mọi hành vi chiếm đoạt tài sản của người khác.\n\n"
                "3. Phương thức Gửi chế tài:\n"
                "- Bản chất: Điều luật quy định rõ phần Giả định và Quy định (nghĩa vụ, trách nhiệm), nhưng phần Chế tài không nằm cùng điều khoản mà được chuyển sang một điều khoản khác ở phần cuối của văn bản hoặc văn bản xử phạt chuyên ngành.\n"
                "- Ví dụ: Luật Giao thông đường bộ quy định nghĩa vụ chấp hành hiệu lệnh đèn tín hiệu, còn mức phạt tiền khi vượt đèn đỏ được gửi sang Nghị định xử phạt vi phạm hành chính trong lĩnh vực giao thông.\n\n"
                "4. Phương thức Viện dẫn mẫu:\n"
                "- Bản chất: Điều luật không trực tiếp mô tả chi tiết quyền, nghĩa vụ hay chế tài mà dẫn chiếu sang điều khoản khác bằng các cụm từ như \"theo quy định tại Điều...\" hoặc \"theo quy định của pháp luật\".\n"
                "- Ví dụ: \"Hợp đồng mua bán tài sản phải tuân theo các điều kiện có hiệu lực của giao dịch dân sự quy định tại Điều 117 Bộ luật Dân sự 2015\"."
            ),
            "has_answer": True,
        },

        # MẪU 3: PHÂN TÍCH CƠ CẤU QUAN HỆ PHÁP LUẬT
        {
            "source_file": "studocu_framework_phap_luat_dai_cuong_cleaned.md",
            "question_number": 3,
            "intent_code": "GENERAL_THEORY",
            "instruction": "Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng GENERAL_THEORY.",
            "input": (
                "Tình huống: Công ty Cổ phần Công nghệ A (do ông Minh làm Giám đốc đại diện) ký kết hợp đồng "
                "mua bán 50 bộ máy vi tính với Công ty TNHH Thiết bị B (do bà Hoa làm Giám đốc đại diện) với tổng trị giá "
                "800 triệu đồng. Hai bên thỏa thuận bên B sẽ giao hàng sau 7 ngày kể từ khi ký hợp đồng và bên A thanh toán "
                "100% tiền hàng sau khi nghiệm thu.\n"
                "Bằng kiến thức môn Pháp luật Đại cương, hãy xác định và phân tích cơ cấu 3 thành phần của Quan hệ pháp luật "
                "phát sinh trong tình huống trên (Chủ thể, Khách thể, Nội dung)."
            ),
            "output": (
                "I. CĂN CỨ LÝ LUẬN VÀ PHÁP LÝ:\n"
                "- Lý luận về 3 thành phần của Quan hệ pháp luật: Chủ thể, Khách thể và Nội dung.\n"
                "- Quy định về Hợp đồng mua bán tài sản tại Điều 430 Bộ luật Dân sự 2015.\n\n"
                "II. PHÂN TÍCH CHI TIẾT CƠ CẤU 3 THÀNH PHẦN:\n\n"
                "1. Chủ thể của Quan hệ pháp luật:\n"
                "- Chủ thể gồm 2 pháp nhân thương mại: Công ty Cổ phần Công nghệ A (Bên mua) và Công ty TNHH Thiết bị B (Bên bán).\n"
                "- Năng lực chủ thể: Cả hai doanh nghiệp đều được thành lập hợp pháp theo Luật Doanh nghiệp, có năng lực pháp luật và năng lực hành vi dân sự đầy đủ, được thực hiện thông qua người đại diện theo pháp luật hợp pháp (ông Minh và bà Hoa).\n\n"
                "2. Khách thể của Quan hệ pháp luật:\n"
                "- Khách thể là những lợi ích vật chất và pháp lý mà hai bên hướng tới khi xác lập quan hệ hợp đồng:\n"
                "+ Đối với Bên mua (Công ty A): Hướng tới việc xác lập quyền sở hữu hợp pháp đối với 50 bộ máy vi tính để phục vụ hoạt động sản xuất kinh doanh.\n"
                "+ Đối với Bên bán (Công ty B): Hướng tới lợi ích kinh tế là số tiền thanh toán 800 triệu đồng từ việc bán tài sản.\n\n"
                "3. Nội dung của Quan hệ pháp luật (Quyền và Nghĩa vụ pháp lý):\n"
                "- Bên bán (Công ty B):\n"
                "+ Quyền chủ thể: Yêu cầu Công ty A nhận hàng đúng thời hạn và thanh toán đầy đủ số tiền 800 triệu đồng sau khi nghiệm thu.\n"
                "+ Nghĩa vụ pháp lý: Giao đúng số lượng (50 bộ), đúng chủng loại, bảo đảm chất lượng kỹ thuật và chuyển giao quyền sở hữu máy tính cho Công ty A sau 7 ngày.\n"
                "- Bên mua (Công ty A):\n"
                "+ Quyền chủ thể: Yêu cầu Công ty B giao 50 bộ máy tính đúng chất lượng, đúng hạn định và chuyển giao quyền sở hữu.\n"
                "+ Nghĩa vụ pháp lý: Tiến hành nghiệm thu và thanh toán đầy đủ 800 triệu đồng cho Công ty B theo đúng thỏa thuận hợp đồng."
            ),
            "has_answer": True,
        },

        # MẪU 4: PHÂN BIỆT HÀNH VI VÀ SỰ BIẾN PHÁP LÝ
        {
            "source_file": "studocu_framework_phap_luat_dai_cuong_cleaned.md",
            "question_number": 4,
            "intent_code": "GENERAL_THEORY",
            "instruction": "Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng GENERAL_THEORY.",
            "input": (
                "Thế nào là Sự kiện pháp lý? Hãy phân biệt Sự biến pháp lý và Hành vi pháp lý. "
                "Cho biết trong tình huống sau đâu là sự biến pháp lý, đâu là hành vi pháp lý và chúng làm phát sinh, "
                "thay đổi hay chấm dứt quan hệ pháp luật nào:\n"
                "\"Ông Nam ký hợp đồng vận chuyển 10 tấn nông sản cho bà Lan. Trên đường vận chuyển qua đèo, "
                "do gặp mưa lũ và sạt lở đất bất khả kháng, xe ô tô bị đất đá vùi lấp làm hư hỏng toàn bộ hàng hóa.\""
            ),
            "output": (
                "I. ĐỊNH NGHĨA SỰ KIỆN PHÁP LÝ & PHÂN LOẠI:\n"
                "- Sự kiện pháp lý: Là những tình huống, điều kiện, sự việc xảy ra trong thực tế đời sống xã hội mà việc xuất hiện hay mất đi của nó được pháp luật gắn liền với việc làm phát sinh, thay đổi hoặc chấm dứt quan hệ pháp luật cụ thể.\n"
                "- Phân loại thành 2 nhóm chính dựa vào ý chí con người:\n"
                "1. Hành vi pháp lý: Là những sự kiện xảy ra phụ thuộc vào ý chí chủ quan và nhận thức của con người (thể hiện qua hành động hoặc không hành động). Gồm hành vi hợp pháp (ký hợp đồng, lập di chúc) và hành vi bất hợp pháp (vi phạm hợp đồng, xâm phạm tài sản).\n"
                "2. Sự biến pháp lý: Là những hiện tượng tự nhiên hoặc biến cố khách quan xảy ra hoàn toàn không phụ thuộc vào ý chí chủ quan của con người, nhưng được quy phạm pháp luật dự liệu làm căn cứ phát sinh, thay đổi hoặc chấm dứt quyền và nghĩa vụ pháp lý (ví dụ: bão lũ, động đất, sét đánh, người chết tự nhiên).\n\n"
                "II. ÁP DỤNG VÀO TÌNH HUỐNG THỰC TẾ:\n"
                "1. Hành vi pháp lý trong tình huống:\n"
                "- Hành vi: Việc ông Nam và bà Lan thỏa thuận, ký kết hợp đồng vận chuyển 10 tấn nông sản.\n"
                "- Tác động: Đây là hành vi pháp lý hợp pháp làm PHÁT SINH Quan hệ pháp luật hợp đồng dịch vụ vận chuyển tài sản giữa ông Nam và bà Lan.\n\n"
                "2. Sự biến pháp lý trong tình huống:\n"
                "- Sự biến: Hiện tượng thiên tai \"mưa lũ và sạt lở đất bất khả kháng\" vùi lấp xe và hàng hóa trên đèo.\n"
                "- Tác động: Đây là sự biến pháp lý khách quan dẫn đến việc thay đổi hoặc chấm dứt nghĩa vụ hợp đồng vận chuyển. Căn cứ khoản 2 Điều 351 Bộ luật Dân sự 2015 về sự kiện bất khả kháng, sự biến này làm MIỄN TRỪ trách nhiệm bồi thường thiệt hại cho ông Nam đối với số hàng nông sản bị tiêu hủy."
            ),
            "has_answer": True,
        },

        # MẪU 5: PHÂN BIỆT 4 HÌNH THỨC THỰC HIỆN PHÁP LUẬT
        {
            "source_file": "studocu_framework_phap_luat_dai_cuong_cleaned.md",
            "question_number": 5,
            "intent_code": "GENERAL_THEORY",
            "instruction": "Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng GENERAL_THEORY.",
            "input": (
                "Hãy xác định hình thức thực hiện pháp luật (Tuân thủ, Chấp hành, Sử dụng, Áp dụng) trong từng trường hợp sau đây và giải thích ngắn gọn lý do:\n"
                "a) Anh Hưng đủ 18 tuổi đi đăng ký nghĩa vụ quân sự và tham gia khám tuyển theo lệnh gọi.\n"
                "b) Chị Mai từ chối không uống rượu bia khi biết mình sắp lái xe ô tô về nhà.\n"
                "c) Ông Bình nộp đơn khiếu nại quyết định thu hồi đất của cơ quan hành chính.\n"
                "d) Tòa án nhân dân ra bản án tuyên bố phạt tù 03 năm đối với bị cáo phạm tội trộm cắp tài sản."
            ),
            "output": (
                "I. CĂN CỨ LÝ LUẬN VỀ 4 HÌNH THỨC THỰC HIỆN PHÁP LUẬT:\n"
                "- Tuân thủ: Kiềm chế không làm điều pháp luật cấm (hành vi thụ động).\n"
                "- Chấp hành: Tích cực thực hiện nghĩa vụ pháp lý bắt buộc (hành vi chủ động).\n"
                "- Sử dụng: Chủ động thực hiện quyền chủ thể mà pháp luật trao cho (được làm gì).\n"
                "- Áp dụng: Cơ quan/người có thẩm quyền nhân danh Nhà nước cá biệt hóa quy phạm pháp luật vào trường hợp cụ thể.\n\n"
                "II. XÁC ĐỊNH VÀ GIẢI THÍCH CHO TỪNG TRƯỜNG HỢP:\n\n"
                "a) Anh Hưng đi đăng ký nghĩa vụ quân sự:\n"
                "- Hình thức: Chấp hành pháp luật.\n"
                "- Giải thích: Tham gia nghĩa vụ quân sự là nghĩa vụ bắt buộc của công dân nam đủ tuổi theo Luật Nghĩa vụ quân sự. Anh Hưng đã chủ động, tích cực thực hiện nghĩa vụ pháp lý bắt buộc mà pháp luật yêu cầu.\n\n"
                "b) Chị Mai không uống rượu bia khi lái xe ô tô:\n"
                "- Hình thức: Tuân thủ pháp luật.\n"
                "- Giải thích: Luật Phòng, chống tác hại của rượu, bia nghiêm cấm điều khiển phương tiện giao thông mà trong máu hoặc hơi thở có nồng độ cồn. Chị Mai đã kiềm chế bản thân không thực hiện hành vi mà pháp luật cấm đoán.\n\n"
                "c) Ông Bình nộp đơn khiếu nại quyết định thu hồi đất:\n"
                "- Hình thức: Sử dụng pháp luật.\n"
                "- Giải thích: Quyền khiếu nại là quyền của công dân theo quy định của Hiến pháp và Luật Khiếu nại. Ông Bình tự mình quyết định thực hiện quyền chủ thể do pháp luật trao cho để bảo vệ quyền lợi hợp pháp của mình.\n\n"
                "d) Tòa án nhân dân tuyên phạt tù 03 năm đối với bị cáo:\n"
                "- Hình thức: Áp dụng pháp luật.\n"
                "- Giải thích: Đây là hoạt động mang tính quyền lực nhà nước, do cơ quan xét xử có thẩm quyền (Tòa án) tiến hành theo đúng trình tự tố tụng hình sự nhằm cá biệt hóa quy phạm pháp luật hình sự đối với cá nhân người phạm tội cụ thể."
            ),
            "has_answer": True,
        },

        # MẪU 6: BÓC TÁCH 4 YẾU TỐ CẤU THÀNH VI PHẠM PHÁP LUẬT
        {
            "source_file": "studocu_framework_phap_luat_dai_cuong_cleaned.md",
            "question_number": 6,
            "intent_code": "VPPL_ELEMENTS",
            "instruction": "Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng VPPL_ELEMENTS.",
            "input": (
                "Tình huống: Trần Văn K (22 tuổi, có đầy đủ năng lực nhận thức và điều khiển hành vi) đột nhập vào nhà "
                "ông Tuấn vào lúc nửa đêm, dùng kìm cộng lực cắt khóa cửa và lấy cắp một chiếc xe máy SH trị giá 75 triệu đồng "
                "để bán lấy tiền tiêu xài cá nhân.\n"
                "Hãy phân tích 4 yếu tố cấu thành vi phạm pháp luật trong tình huống trên (Mặt khách quan, Mặt chủ quan, Chủ thể, Khách thể)."
            ),
            "output": (
                "I. CĂN CỨ PHÁP LÝ:\n"
                "- Điều 173 Bộ luật Hình sự 2015 (sửa đổi, bổ sung 2017) về Tội trộm cắp tài sản.\n"
                "- Lý luận cấu thành vi phạm pháp luật gồm 4 yếu tố.\n\n"
                "II. PHÂN TÍCH 4 YẾU TỐ CẤU THÀNH VI PHẠM PHÁP LUẬT:\n\n"
                "1. Mặt khách quan của vi phạm:\n"
                "- Hành vi trái pháp luật: Hành vi dùng kìm cộng lực cắt khóa, đột nhập lén lút vào nhà người khác và bí mật chiếm đoạt tài sản là chiếc xe máy SH.\n"
                "- Hậu quả nguy hại: Gây thiệt hại trực tiếp về tài sản cho ông Tuấn với giá trị tài sản bị chiếm đoạt là 75 triệu đồng.\n"
                "- Mối quan hệ nhân quả: Hành vi cắt khóa lén lút của K là nguyên nhân trực tiếp dẫn tới hậu quả ông Tuấn bị mất quyền quản lý và chiếm hữu tài sản.\n"
                "- Công cụ, thời gian: Kìm cộng lực, thực hiện vào ban đêm.\n\n"
                "2. Mặt chủ quan của vi phạm:\n"
                "- Lỗi: Lỗi Cố ý trực tiếp. K nhận thức rõ hành vi đột nhập trộm cắp xe của mình là trái pháp luật và nguy hiểm cho xã hội, thấy trước hậu quả ông Tuấn sẽ bị mất tài sản và mong muốn hậu quả chiếm đoạt được tài sản xảy ra.\n"
                "- Động cơ: Vụ lợi, muốn có tài sản bất chính.\n"
                "- Mục đích: Chiếm đoạt chiếc xe máy SH đem bán lấy tiền tiêu xài cá nhân.\n\n"
                "3. Chủ thể của vi phạm:\n"
                "- Trần Văn K, 22 tuổi (đạt độ tuổi luật định theo Điều 12 Bộ luật Hình sự).\n"
                "- K có năng lực trách nhiệm hình sự đầy đủ (không mắc bệnh tâm thần hoặc bệnh khác làm mất khả năng nhận thức và làm chủ hành vi).\n\n"
                "4. Khách thể của vi phạm:\n"
                "- Xâm phạm trực tiếp đến Quan hệ sở hữu tài sản hợp pháp của công dân (ông Tuấn) được Bộ luật Dân sự và Bộ luật Hình sự bảo vệ; đồng thời xâm phạm trật tự an toàn xã hội."
            ),
            "has_answer": True,
        },

        # MẪU 7: PHÂN BIỆT CỐ Ý GIÁN TIẾP VS VÔ Ý VÌ QUÁ TỰ TIN
        {
            "source_file": "studocu_framework_phap_luat_dai_cuong_cleaned.md",
            "question_number": 7,
            "intent_code": "VPPL_ELEMENTS",
            "instruction": "Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng VPPL_ELEMENTS.",
            "input": (
                "Bài tập tình huống về Lỗi:\n"
                "Ông Thành trồng vườn cây ăn quả thường xuyên bị trộm đột nhập hái trộm quả. Để đối phó, ông Thành đã lấy "
                "dây thép trần kéo xung quanh hàng rào rồi đấu nối trực tiếp vào mạng điện sinh hoạt 220V vào ban đêm mà không hề treo biển cảnh báo nguy hiểm.\n"
                "Hậu quả: Anh Sang đi soi ếch vào ban đêm vô tình chạm vào dây thép và bị điện giật tử vong tại chỗ.\n"
                "Hỏi: Hành vi của ông Thành cấu thành Lỗi gì trong các dạng lỗi của vi phạm pháp luật? "
                "Hãy giải thích chi tiết và phân biệt với lỗi Vô ý vì quá tự tin."
            ),
            "output": (
                "I. XÁC ĐỊNH DẠNG LỖI CỦA ÔNG THÀNH:\n"
                "- Hành vi của ông Thành thuộc dạng: LỖI CỐ Ý GIÁN TIẾP.\n\n"
                "II. GIẢI THÍCH CHI TIẾT DỰA TRÊN 2 YẾU TỐ LÝ TRÍ VÀ Ý CHÍ:\n"
                "1. Về mặt lý trí:\n"
                "- Ông Thành là người có năng lực nhận thức bình thường, nhận thức rõ mạng điện sinh hoạt 220V là nguồn nguy hiểm cao độ, có khả năng làm chết người ngay lập tức khi tiếp xúc.\n"
                "- Ông Thành hoàn toàn thấy trước được hậu quả chết người có thể xảy ra cho bất kỳ ai (kể cả người đi đường, người bắt ếch hay kẻ trộm) khi chạm vào hàng rào thép trần không có cảnh báo.\n\n"
                "2. Về mặt ý chí:\n"
                "- Ông Thành không mong muốn hậu quả làm chết người xảy ra (mục đích ban đầu chỉ là giữ vườn quả).\n"
                "- Tuy nhiên, ông Thành hoàn toàn không lắp đặt bất kỳ thiết bị bảo vệ (như rơ le chống giật, biển báo nguy hiểm), không có biện pháp ngăn ngừa mà có ý thức ĐỂ MẶC CHO HẬU QUẢ XẢY RA (hậu quả chết người xảy ra hay không thì ông vẫn chấp nhận để đạt được việc chống trộm).\n\n"
                "III. PHÂN BIỆT VỚI LỖI VÔ Ý VÌ QUÁ TỰ TIN:\n"
                "- Trong lỗi Vô ý vì quá tự tin: Chủ thể tuy thấy trước hậu quả nguy hại có thể xảy ra nhưng KHÔNG MONG MUỐN VÀ TIN TƯỞNG CHẮC CHẮN RẰNG hậu quả sẽ không xảy ra hoặc có thể ngăn chặn được dựa vào các biện pháp thực tế hoặc kinh nghiệm của mình.\n"
                "- Trong trường hợp này: Ông Thành không hề có bất kỳ căn cứ hợp lý hay biện pháp kỹ thuật nào để tin rằng sẽ không có người bị giật chết. Thái độ buông xuôi, phó mặc cho số phận chứng minh đây là thái độ \"để mặc\", đặc trưng cơ bản của Lỗi Cố ý gián tiếp."
            ),
            "has_answer": True,
        },

        # MẪU 8: PHÂN BIỆT VÔ Ý DO CẨU THẢ VS SỰ KIỆN BẤT NGỜ
        {
            "source_file": "studocu_framework_phap_luat_dai_cuong_cleaned.md",
            "question_number": 8,
            "intent_code": "VPPL_ELEMENTS",
            "instruction": "Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng VPPL_ELEMENTS.",
            "input": (
                "Tình huống: Y tá Phương được phân công tiêm thuốc giảm đau cho bệnh nhân H theo chỉ định của bác sĩ. "
                "Do mải nói chuyện điện thoại cá nhân trong phòng trực thuốc, Phương đã lấy nhầm ống thuốc gây tê liều cao "
                "(có hình dáng vỏ ngoài khá tương đồng với ống thuốc giảm đau) và tiêm cho bệnh nhân H mà không thực hiện "
                "nguyên tắc đối chiếu \"3 tra, 5 đối\" theo quy trình y tế. Hậu quả bệnh nhân H bị sốc thuốc và tử vong.\n"
                "Hãy xác định dạng lỗi của y tá Phương và phân tích dấu hiệu pháp lý."
            ),
            "output": (
                "I. XÁC ĐỊNH DẠNG LỖI CỦA Y TÁ PHƯƠNG:\n"
                "- Hành vi của y tá Phương cấu thành: LỖI VÔ Ý DO CẨU THẢ.\n\n"
                "II. PHÂN TÍCH DẤU HIỆU PHÁP LÝ CỦA LỖI:\n\n"
                "1. Về mặt lý trí:\n"
                "- Phương KHÔNG THẤY TRƯỚC được hành vi lấy nhầm thuốc của mình sẽ gây ra hậu quả bệnh nhân H bị sốc thuốc tử vong (khi tiêm, Phương vẫn tưởng đó là ống thuốc giảm đau bình thường do sơ suất).\n\n"
                "2. Về nghĩa vụ và điều kiện khách quan (phải thấy và có thể thấy trước):\n"
                "- Phương là nhân viên y tế đã qua đào tạo chuyên môn, theo quy chế ngành y bắt buộc phải tuân thủ nghiêm ngặt quy tắc an toàn \"3 tra, 5 đối\" (kiểm tra tên thuốc, nồng độ, liều dùng, hạn dùng, đường tiêm) trước khi tiêm cho bệnh nhân. Do đó, Phương PHẢI THẤY TRƯỚC việc lấy nhầm thuốc nguy hiểm sẽ đe dọa trực tiếp tính mạng bệnh nhân.\n"
                "- Hoàn cảnh thực tế: Vỏ thuốc có ghi rõ nhãn mác, thông tin, phòng trực đủ ánh sáng, Phương hoàn toàn CÓ THỂ THẤY TRƯỚC sự nhầm lẫn này nếu chú ý cẩn trọng quan sát thay vì mải nghe điện thoại cá nhân.\n\n"
                "III. KẾT LUẬN:\n"
                "- Hành vi của Phương không phải là Sự kiện bất ngờ (bởi sự kiện bất ngờ chỉ xảy ra khi chủ thể không thể thấy trước hoặc không buộc phải thấy trước).\n"
                "- Sự cẩu thả, tắc trách trong thực hiện nhiệm vụ chuyên môn đã dẫn tới hậu quả chết người, thỏa mãn đầy đủ cấu thành của Lỗi vô ý do cẩu thả."
            ),
            "has_answer": True,
        },

        # MẪU 9: PHÂN LOẠI MỨC ĐỘ TỘI PHẠM THEO ĐIỀU 9 BLHS 2015
        {
            "source_file": "studocu_framework_phap_luat_dai_cuong_cleaned.md",
            "question_number": 9,
            "intent_code": "CRIMINAL_AGE",
            "instruction": "Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng CRIMINAL_AGE.",
            "input": (
                "Căn cứ Điều 9 Bộ luật Hình sự 2015 (sửa đổi, bổ sung 2017), tội phạm được phân thành mấy loại? "
                "Nêu tiêu chí phân loại dựa trên mức cao nhất của khung hình phạt tù. "
                "Sau đó, hãy xác định mức độ nghiêm trọng của tội phạm trong các trường hợp sau:\n"
                "a) Điều khoản X quy định mức phạt tù từ 02 năm đến 07 năm.\n"
                "b) Điều khoản Y quy định mức phạt tù từ 07 năm đến 15 năm.\n"
                "c) Điều khoản Z quy định mức phạt tù từ 12 năm đến 20 năm, tù chung thân hoặc tử hình."
            ),
            "output": (
                "I. CĂN CỨ PHÁP LÝ & TIÊU CHÍ PHÂN LOẠI (ĐIỀU 9 BLHS 2015, SỬA ĐỔI 2017):\n"
                "Tội phạm được phân loại thành 4 mức độ dựa vào tính chất, mức độ nguy hiểm cho xã hội và MỨC CAO NHẤT của khung hình phạt do Bộ luật Hình sự quy định:\n"
                "1. Tội phạm ít nghiêm trọng: Mức cao nhất của khung hình phạt phạt tù là ĐẾN 03 NĂM TÙ (hoặc phạt tiền, cải tạo không giam giữ).\n"
                "2. Tội phạm nghiêm trọng: Mức cao nhất của khung hình phạt phạt tù là TỪ TRÊN 03 NĂM ĐẾN 07 NĂM TÙ.\n"
                "3. Tội phạm rất nghiêm trọng: Mức cao nhất của khung hình phạt phạt tù là TỪ TRÊN 07 NĂM ĐẾN 15 NĂM TÙ.\n"
                "4. Tội phạm đặc biệt nghiêm trọng: Mức cao nhất của khung hình phạt phạt tù là TỪ TRÊN 15 NĂM ĐẾN 20 NĂM TÙ, TÙ CHUNG THÂN HOẶC TỬ HÌNH.\n\n"
                "II. XÁC ĐỊNH MỨC ĐỘ NGHIÊM TRỌNG TRONG CÁC TRƯỜNG HỢP CỤ THỂ:\n\n"
                "a) Điều khoản X quy định khung phạt tù từ 02 năm đến 07 năm:\n"
                "- Mức cao nhất của khung hình phạt là 07 năm tù.\n"
                "- Căn cứ điểm b khoản 1 Điều 9 BLHS 2015, đây là: TỘI PHẠM NGHIÊM TRỌNG.\n\n"
                "b) Điều khoản Y quy định khung phạt tù từ 07 năm đến 15 năm:\n"
                "- Mức cao nhất của khung hình phạt là 15 năm tù.\n"
                "- Căn cứ điểm c khoản 1 Điều 9 BLHS 2015, đây là: TỘI PHẠM RẤT NGHIÊM TRỌNG.\n\n"
                "c) Điều khoản Z quy định khung phạt tù từ 12 năm đến 20 năm, tù chung thân hoặc tử hình:\n"
                "- Mức cao nhất của khung hình phạt là tù chung thân hoặc tử hình (vượt trên 15 năm tù).\n"
                "- Căn cứ điểm d khoản 1 Điều 9 BLHS 2015, đây là: TỘI PHẠM ĐẶC BIỆT NGHIÊM TRỌNG."
            ),
            "has_answer": True,
        },

        # MẪU 10: CÂU HỎI ĐÚNG/SAI VỀ CẤU THÀNH VPPL & HÌNH THỨC THỰC HIỆN PHÁP LUẬT
        {
            "source_file": "studocu_framework_phap_luat_dai_cuong_cleaned.md",
            "question_number": 10,
            "intent_code": "TRUE_FALSE",
            "instruction": "Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng TRUE_FALSE.",
            "input": (
                "Các nhận định dưới đây Đúng hay Sai? Giải thích ngắn gọn và viện dẫn căn cứ lý luận môn Pháp luật Đại cương:\n"
                "1. Mọi hành vi trái pháp luật đều là vi phạm pháp luật.\n"
                "2. Người không có năng lực trách nhiệm pháp lý thực hiện hành vi gây thiệt hại cho xã hội thì không bị coi là vi phạm pháp luật.\n"
                "3. Mọi quan hệ xã hội đều là quan hệ pháp luật.\n"
                "4. Áp dụng pháp luật là hình thức thực hiện pháp luật có thể do bất kỳ công dân nào tiến hành."
            ),
            "output": (
                "1. Nhận định Sai.\n"
                "- Giải thích: Hành vi trái pháp luật chỉ là điều kiện cần nhưng chưa đủ để cấu thành vi phạm pháp luật. Để là vi phạm pháp luật, hành vi đó phải đồng thời thỏa mãn 4 dấu hiệu: là hành vi xác định của con người, trái pháp luật, có lỗi, và do chủ thể có năng lực trách nhiệm pháp lý thực hiện. Nếu hành vi trái pháp luật được thực hiện trong tình thế cấp thiết, phòng vệ chính đáng hoặc do người mất năng lực hành vi dân sự thực hiện thì không cấu thành vi phạm pháp luật.\n\n"
                "2. Nhận định Đúng.\n"
                "- Giải thích: Chủ thể của vi phạm pháp luật bắt buộc phải là người có năng lực trách nhiệm pháp lý (đủ độ tuổi luật định và khả năng nhận thức, điều khiển hành vi). Nếu người mắc bệnh tâm thần hoặc trẻ em dưới độ tuổi luật định gây thiệt hại thì hành vi đó thiếu yếu tố chủ thể và lỗi, do đó không bị coi là vi phạm pháp luật.\n\n"
                "3. Nhận định Sai.\n"
                "- Giải thích: Quan hệ pháp luật chỉ là một bộ phận của quan hệ xã hội. Chỉ những quan hệ xã hội nào được các quy phạm pháp luật điều chỉnh, gắn với sự kiện pháp lý và các bên tham gia có quyền, nghĩa vụ pháp lý mới trở thành quan hệ pháp luật. Rất nhiều quan hệ xã hội khác (như tình bạn, tình yêu, quan hệ tín ngưỡng) chỉ được điều chỉnh bởi quy phạm đạo đức, tập quán hoặc tôn giáo.\n\n"
                "4. Nhận định Sai.\n"
                "- Giải thích: Trong 4 hình thức thực hiện pháp luật, chỉ có Tuân thủ, Chấp hành và Sử dụng pháp luật là do mọi công dân, cơ quan, tổ chức tiến hành. Riêng hình thức \"Áp dụng pháp luật\" là hoạt động mang tính quyền lực nhà nước, chỉ do các cơ quan nhà nước có thẩm quyền hoặc cá nhân được Nhà nước trao quyền lực công tiến hành theo trình tự, thủ tục luật định nhằm cá biệt hóa quy phạm pháp luật."
            ),
            "has_answer": True,
        }
    ]
    return samples

def integrate_framework_samples():
    """
    Tích hợp các mẫu SFT mới vào master dataset và đồng bộ toàn hệ thống.
    """
    new_samples = create_framework_sft_samples()
    logger.info(f"Đã tạo {len(new_samples)} mẫu SFT chuẩn hóa từ file Framework mới.")

    # Đọc master sft_vietlaw_500.json
    sft_file = PROCESSED_DIR / "sft_vietlaw_500.json"
    if not sft_file.exists():
        sft_file = DATA_DIR.parent / "kaggle" / "dataset" / "sft_vietlaw_500.json"
    
    with open(sft_file, "r", encoding="utf-8") as f:
        existing_data = json.load(f)

    logger.info(f"Số lượng mẫu hiện có: {len(existing_data)}")

    # Gán ID duy nhất tiếp nối
    start_idx = len(existing_data) + 1
    for i, s in enumerate(new_samples):
        s["sample_id"] = f"SFT_{s['intent_code'][:6]}_{start_idx + i:03d}"

    updated_data = existing_data + new_samples
    logger.info(f"Tổng số mẫu sau khi bổ sung: {len(updated_data)}")

    # Lưu lại cả 2 vị trí processed và kaggle/dataset
    target_paths = [
        PROCESSED_DIR / "sft_vietlaw_500.json",
        DATA_DIR.parent / "kaggle" / "dataset" / "sft_vietlaw_500.json"
    ]
    for p in target_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(updated_data, f, ensure_ascii=False, indent=2)
        logger.success(f"Đã lưu file: {p}")

    # Chạy lại split_sft_stratified
    train_out = PROCESSED_DIR / "train_sft.json"
    val_out = PROCESSED_DIR / "val_sft.json"
    train_data, val_data = split_sft_stratified(
        input_file=PROCESSED_DIR / "sft_vietlaw_500.json",
        train_output=train_out,
        val_output=val_out,
        val_ratio=0.2,
        seed=42
    )

    # Đồng bộ sang kaggle/dataset/
    kaggle_dir = DATA_DIR.parent / "kaggle" / "dataset"
    sync_files = [
        (train_out, kaggle_dir / "train_sft.json"),
        (val_out, kaggle_dir / "val_sft.json"),
        (PROCESSED_DIR / "train_sft_chatml.json", kaggle_dir / "train_sft_chatml.json"),
        (PROCESSED_DIR / "val_sft_chatml.json", kaggle_dir / "val_sft_chatml.json"),
    ]
    for src, dst in sync_files:
        if src.exists():
            import shutil
            shutil.copy2(src, dst)
            logger.info(f"Đã đồng bộ {src.name} -> {dst}")

    # Cập nhật dataset_manifest.json
    manifest_items = []
    for f in kaggle_dir.glob("*.json"):
        if f.name in ["dataset-metadata.json", "dataset_manifest.json"]:
            continue
        size_kb = f.stat().st_size / 1024
        manifest_items.append({
            "file": f.name,
            "size": f"{size_kb:.1f} KB",
            "md5": compute_md5(f)
        })

    manifest_path = kaggle_dir / "dataset_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_items, f, ensure_ascii=False, indent=2)
    logger.success(f"Đã cập nhật {manifest_path.name} thành công!")

if __name__ == "__main__":
    integrate_framework_samples()
