## I. XUẤT PHÁT ĐIỂM & BÀI TOÁN THỰC TẾ (TẠI SAO LẠI LÀM DỰ ÁN NÀY?)

### 1. Nỗi niềm của sinh viên với môn Pháp luật Đại cương
Ở tất cả các trường đại học tại Việt Nam, từ trường kinh tế, xã hội cho đến các trường khối kỹ thuật như Đại học Bách Khoa, **Pháp luật Đại cương** là môn học bắt buộc đối với 100% sinh viên năm nhất và năm hai. Môn học này trang bị cho sinh viên những hiểu biết cơ bản nhất về nhà nước và hệ thống pháp luật để sống và làm việc theo pháp luật.

Tuy nhiên, trong thực tế thi cử, có một nghịch lý rất lớn mà hầu như sinh viên nào cũng gặp phải:
* Sinh viên học khối kỹ thuật thường quen với tư duy logic toán học, rành mạch, ngắn gọn, nên khi tiếp cận với văn phong pháp lý dài dòng, nhiều thuật ngữ chuyên môn thì cảm thấy rất khó nhớ và dễ nhầm lẫn.
* Khi làm bài thi cuối kỳ, sinh viên đọc một tình huống thực tế thì trong đầu biết ngay ai đúng ai sai, nhưng **đặt bút viết vào bài thi thì điểm lại rất thấp**. 
* **Nguyên nhân chính:** Thầy cô bộ môn chấm điểm không chấm theo cảm tính hay văn xuôi tự do, mà chấm theo **từng barem điểm cố định quy định trong giáo trình**. Ví dụ: một bài phân tích hành vi vi phạm pháp luật bắt buộc phải mổ xẻ đủ 4 yếu tố (Mặt khách quan, Mặt chủ quan, Khách thể, Chủ thể). Sinh viên chỉ cần thiếu phân tích về "Lỗi cố ý hay vô ý" là bị trừ ngay 1 điểm; xác định sai một chi tiết trong bài tập chia thừa kế là mất trắng toàn bộ bài làm.

### 2. Sự bất lực của các công cụ AI hiện tại
Nhiều sinh viên thử dùng ChatGPT hoặc Gemini để nhờ giải đề thi, nhưng kết quả nhận được thường không dùng được cho bài thi:
* **Trả lời chung chung:** Các mô hình ngôn ngữ lớn trả lời theo phong cách đàm thoại, tóm tắt tự do, không biết và không tuân theo các khung cấu trúc sư phạm chặt chẽ của Giáo trình Bộ Giáo dục & Đào tạo Việt Nam.
* **Hiện tượng "bịa điều luật" (Ảo giác pháp lý):** AI thông thường hay tự nghĩ ra một số điều, số khoản không có thật hoặc trích dẫn các văn bản đã hết hiệu lực. Nếu sinh viên chép nguyên văn vào bài thi sẽ bị trừ điểm rất nặng.
* **Không phân biệt được đối tượng:** Đề thi của sinh viên khối kỹ thuật cần lời giải gãy gọn, bám sát hành vi và chế tài cụ thể; trong khi đề thi khối xã hội lại cần phân tích sâu về nguồn gốc giai cấp và bản chất nhà nước. AI phổ thông không phân định được ranh giới này.

👉 **VietLawAssist ra đời để giải quyết triệt để nỗi đau đó:** Xây dựng một "người gia sư AI chuyên biệt" cho môn Pháp luật Đại cương, hiểu rõ từng dạng đề thi, nắm vững các điều luật thực định của Việt Nam, và tự động trình bày câu trả lời theo đúng từng barem điểm của giảng viên chấm thi.

---

## II. MỤC TIÊU CỐT LÕI MÀ DỰ ÁN HƯỚNG TỚI

Dự án đặt ra 3 mục tiêu rõ ràng và đo lường được:

1. **Về mặt ứng dụng cho người học (Sinh viên):**  
   Trở thành công cụ tự học, ôn thi và kiểm tra bài làm đáng tin cậy. Khi sinh viên nhập vào một câu hỏi lý thuyết, một câu nhận định hay một bài tập tình huống, hệ thống sẽ trả về một bài giải mẫu chi tiết từng mục, chỉ rõ từng căn cứ pháp lý, giúp sinh viên không chỉ có đáp án để đối chiếu mà còn học được cách tư duy và cách trình bày chuẩn chỉnh để đi thi đạt điểm 9–10.

2. **Về mặt học thuật và khoa học (Đối với đồ án tốt nghiệp PBL6):**  
   Chứng minh năng lực ứng dụng công nghệ trí tuệ nhân tạo hiện đại để giải quyết bài toán hẹp trong đời sống. Dự án không đi theo lối mòn "dùng một API có sẵn để tạo chatbot", mà xây dựng một **Bậc thang So sánh 4 Tầng công nghệ** (từ thuật toán tìm kiếm từ khóa cổ điển BM25, đến tìm kiếm vector ngữ nghĩa PhoBERT, rồi đến mô hình ngôn ngữ tạo sinh RAG và kỹ thuật tinh chỉnh chuyên sâu LoRA). Bậc thang này giúp đánh giá và chứng minh rõ ràng: *Mỗi bước cải tiến công nghệ đã giúp câu trả lời của AI tiến bộ về độ chính xác và độ chuẩn barem như thế nào.*

3. **Về mặt tối ưu hóa kỹ thuật (Tính thực tiễn):**  
   Toàn bộ hệ thống được tính toán và thiết kế để vận hành trơn tru ngay trên máy tính cá nhân thông thường của sinh viên (laptop có card đồ họa RTX 3050 4GB) hoặc các môi trường miễn phí như Google Colab, không phụ thuộc vào các siêu máy chủ đắt đỏ.

---

## III. NỘI DUNG VÀ PHẠM VI NGHIỆP VỤ CỦA HỆ THỐNG

Để đảm bảo chất lượng câu trả lời đạt mức sâu và chính xác tuyệt đối, dự án giới hạn phạm vi vào đúng phần lõi của chương trình đào tạo Pháp luật Đại cương tại các trường đại học:

### 1. Kho ngữ liệu pháp luật và giáo trình chuẩn
Hệ thống được nạp và làm chủ hai nguồn tri thức chính:
* **Kho văn bản luật thực định (gồm 5 bộ luật cốt lõi nhất):**  
  - *Hiến pháp năm 2013:* Nền tảng về chế độ chính trị, quyền con người, quyền và nghĩa vụ cơ bản của công dân, cơ cấu bộ máy nhà nước.
  - *Bộ luật Dân sự năm 2015:* Năng lực chủ thể, tài sản, hợp đồng và chế định thừa kế.
  - *Bộ luật Hình sự năm 2015 (sửa đổi, bổ sung 2017):* Tội phạm, các yếu tố cấu thành tội phạm, độ tuổi chịu trách nhiệm hình sự và hệ thống hình phạt.
  - *Luật Hôn nhân và Gia đình năm 2014:* Điều kiện kết hôn, tài sản chung/riêng của vợ chồng, ly hôn.
  - *Bộ luật Lao động năm 2019:* Hợp đồng lao động, thời giờ làm việc, kỷ luật lao động.
* **Kho lý luận Giáo trình Pháp luật Đại cương (Bộ GD&ĐT):**  
  Bao gồm các định nghĩa mang tính nguyên lý không nằm trực tiếp trong điều luật: thế nào là lỗi cố ý trực tiếp, lỗi vô ý vì quá tự tin; công thức xác định quan hệ nhân quả; ba bộ phận của một quy phạm pháp luật; các điều kiện của một quan hệ pháp luật.

### 2. Năm dạng bài tập trọng tâm mà hệ thống xử lý thuần thục
Hệ thống được rèn luyện để giải quyết trọn vẹn 5 dạng đề thi thường xuyên xuất hiện trong các kỳ thi cuối kỳ:
* **Dạng 1 — Phân tích Cấu trúc Quy phạm pháp luật:** Tách bạch một điều luật thành 3 bộ phận: Giả định (áp dụng cho ai, khi nào?), Quy định (phải làm gì, được làm gì, cấm làm gì?), và Chế tài (nếu vi phạm thì bị xử lý ra sao?). Nhận diện được cả các quy phạm khuyết thành phần.
* **Dạng 2 — Phân tích 4 Yếu tố Cấu thành Vi phạm pháp luật:** Đứng trước một hành vi vi phạm thực tế, hệ thống mổ xẻ rành mạch: Mặt khách quan (hành vi, hậu quả, nhân quả), Mặt chủ quan (phân tích rõ lý trí và ý chí để chỉ ra đúng loại lỗi), Khách thể (quan hệ xã hội nào bị xâm hại) và Chủ thể (độ tuổi và năng lực nhận thức).
* **Dạng 3 — Câu hỏi Nhận định Đúng / Sai và Giải thích:** Đưa ra kết luận dứt khoát là ĐÚNG hay SAI, sau đó dùng nguyên lý giáo trình để lập luận giải thích và trích dẫn điều luật hoặc đưa phản ví dụ thực tế để chứng minh.
* **Dạng 4 — Bài tập Tình huống Chia Di sản Thừa kế:** Dạng bài tập tính toán phức tạp nhất của môn học. Hệ thống thực hiện từng bước: xác định tài sản chung của vợ chồng để tìm ra di sản người chết để lại, xét tính hợp pháp của di chúc, tính 1 suất thừa kế theo luật, trích $2/3$ suất thừa kế cho những người được bảo vệ theo Điều 644 (dù di chúc không cho), xét thừa kế thế vị theo Điều 652 và ra con số phân chia cụ thể cho từng người.
* **Dạng 5 — Bài tập Xác định Tuổi chịu Trách nhiệm hình sự:** Đối chiếu độ tuổi của người vi phạm (từ 14 đến dưới 16 tuổi) với mức độ nghiêm trọng của tội phạm theo Điều 9 và danh mục tội danh quy định tại Điều 12 Bộ luật Hình sự để đưa ra kết luận chính xác có phải đi tù hay không.

---

## IV. CÁC THÀNH PHẦN HỢP THÀNH HỆ THỐNG (BÊN TRONG CHƯƠNG TRÌNH CÓ GÌ?)

Nếu nhìn vào hệ thống khi vận hành, ta có thể hình dung nó giống như một cỗ máy gồm **6 bộ phận liên kết chặt chẽ với nhau**:

```
[Người dùng nhập câu hỏi] 
           │
           ▼
  ┌────────────────────────────────────────────────────────┐
  │ 1. BỘ PHẬN TIẾP NHẬN & PHÂN LOẠI DẠNG ĐỀ (Router)      │ ──► Nhận biết dạng bài để chọn cách giải
  └────────────────────────┬───────────────────────────────┘
                           │
                           ▼
  ┌────────────────────────────────────────────────────────┐
  │ 2. BỘ PHẬN THƯ VIỆN & TRA CỨU ĐIỀU LUẬT (Retrieval)   │ ──► Tìm đúng điều luật và lý luận cần thiết
  └────────────────────────┬───────────────────────────────┘
                           │
                           ▼
  ┌────────────────────────────────────────────────────────┐
  │ 3. BỘ PHẬN NÃO BỘ TẠO LẬP BÀI GIẢI (Generator)        │ ──► Áp dụng khung barem điểm để viết lời giải
  └────────────────────────┬───────────────────────────────┘
                           │
                           ▼
  ┌────────────────────────────────────────────────────────┐
  │ 4. BỘ PHẬN KIỂM ĐỊNH & CHỐNG BỊA LUẬT (Guardrail)      │ ──► Soát lại số Điều, Khoản với kho dữ liệu gốc
  └────────────────────────┬───────────────────────────────┘
                           │
                           ▼
  ┌────────────────────────────────────────────────────────┐
  │ 5. BỘ PHẬN ĐỐI SÁNH 4 TẦNG CÔNG NGHỆ (Benchmarking)    │ ──► So sánh BM25 vs PhoBERT vs Base RAG vs LoRA
  └────────────────────────┬───────────────────────────────┘
                           │
                           ▼
  ┌────────────────────────────────────────────────────────┐
  │ 6. GIAO DIỆN HIỂN THỊ THÔNG MINH (Dual-Mode Web UI)    │ ──► Hiển thị bài giải đẹp mắt, có xuất file PDF
  └────────────────────────────────────────────────────────┘
```

1. **Bộ phận Tiếp nhận & Phân loại đề thi:** Khi người dùng gửi một câu hỏi vào, bộ phận này đóng vai trò như một người phân loại bưu phẩm. Nó đọc câu hỏi và xác định ngay: đây là bài tập phân tích vi phạm pháp luật, câu hỏi nhận định đúng sai, hay bài toán chia thừa kế. Việc này giúp hệ thống quyết định sẽ chọn "khung barem nào" để giải bài.
2. **Kho tri thức & Bộ phận Tra cứu:** Gồm toàn bộ 5 bộ luật và các chương giáo trình đã được chuyển hóa thành dạng dữ liệu số. Khi có câu hỏi, hệ thống sử dụng kết hợp hai cơ chế tìm kiếm: tìm chính xác theo từ khóa pháp lý (BM25) và tìm theo ý nghĩa nội dung (PhoBERT vector). Nhờ đó, dù sinh viên dùng từ ngữ đời thường (như "tông xe gãy chân"), hệ thống vẫn tự hiểu để tìm ra đúng điều luật về "Tội cố ý gây thương tích" hoặc "Bồi thường thiệt hại ngoài hợp đồng".
3. **Bộ phận Não bộ Tạo lập bài giải:** Đây là một mô hình ngôn ngữ lớn (Qwen2.5-1.5B) đã được nén gọn để chạy nhẹ nhàng nhưng thông minh. Mô hình này đã được "dạy riêng" (fine-tune) bằng 500 bài thi mẫu chuẩn của môn Pháp luật Đại cương. Nó biết cách sắp xếp câu chữ theo đúng trình tự chấm điểm của thầy cô: mở đầu là kết luận, tiếp theo là bảng phân tích 4 mục, và kết thúc là căn cứ điều khoản.
4. **Bộ phận Kiểm định & Chống bịa luật (Bộ lọc an toàn):** Đây là chốt kiểm soát chất lượng. Trước khi câu trả lời được gửi ra màn hình, bộ phận này sẽ dùng công cụ quét tự động tìm tất cả các cụm từ trích dẫn như "Điều 134", "Điều 644"... rồi tra ngược lại vào cơ sở dữ liệu luật gốc. Nếu điều luật đó thực sự tồn tại, hệ thống mới gắn nhãn "Đã kiểm chứng xác thực"; nếu có dấu hiệu trích dẫn sai, hệ thống lập tức cảnh báo để bảo vệ sinh viên.
5. **Bộ phận Đối sánh 4 tầng công nghệ:** Một phân hệ chuyên biệt phục vụ cho nghiên cứu khoa học và bảo vệ đồ án. Nó cho phép người dùng chạy thử câu hỏi qua cả 4 phương pháp từ đơn sơ đến tối tân để nhìn thấy rõ sự tiến hóa của trí tuệ nhân tạo.
6. **Giao diện Web hai chế độ (Dual-Mode UI):** 
   * *Chế độ Học tập:* Giao diện tinh tế, tập trung vào việc đọc bài giảng, hiển thị lời giải rõ ràng, làm nổi bật các điều luật và cho phép sinh viên tải về máy dưới dạng tệp PDF để in ra học bài.
   * *Chế độ Hội đồng:* Hiển thị màn hình chia 4 cột song song, cho phép các thầy cô hội đồng chấm thi cùng lúc nhìn thấy kết quả của 4 tầng công nghệ kèm biểu đồ đo đạc thời gian chạy và lượng bộ nhớ GPU tiêu thụ trực tiếp.

---

## V. KẾT QUẢ ĐẦU RA MONG MUỐN (KHI CHẠY THỰC TẾ TRÔNG NHƯ THẾ NÀO?)

Khi hoàn thành toàn bộ dự án, sản phẩm đầu ra sẽ là một hệ sinh thái hoàn chỉnh gồm 3 phần rõ rệt:

### 1. Đầu ra về mặt Sản phẩm Phần mềm (Trải nghiệm Người dùng)
Người dùng truy cập vào trang web trên trình duyệt. Khi nhập một câu hỏi cụ thể, ví dụ:  
> *"Tình huống: Nguyễn Văn A (19 tuổi, khỏe mạnh bình thường) do mâu thuẫn trong quán ăn đã dùng gậy gỗ đánh anh B gây thương tật 20%. Hành vi của A có vi phạm pháp luật không? Hãy phân tích các yếu tố cấu thành vi phạm pháp luật của A?"*

Chỉ sau khoảng **4 đến 5 giây**, màn hình sẽ hiển thị ra một bài giải hoàn chỉnh gồm các khối trực quan:

* **Khối 1 — Kết luận sơ bộ:** Khẳng định dứt khoát hành vi của Nguyễn Văn A là vi phạm pháp luật hình sự vì hội tụ đủ 4 dấu hiệu cơ bản.
* **Khối 2 — Bảng Phân tích 4 Yếu tố Cấu thành (Trọng tâm ăn điểm):**
  * *Mặt khách quan:* Chỉ rõ hành vi dùng gậy gỗ là hành động nguy hiểm; hậu quả thực tế là anh B bị thương tật 20%; chỉ rõ mối quan hệ nhân quả trực tiếp giữa cú đánh và vết thương; công cụ là gậy gỗ.
  * *Mặt chủ quan:* Khẳng định A phạm lỗi **Cố ý trực tiếp** và giải thích rõ theo giáo trình: về lý trí A biết đánh người là nguy hiểm, về ý chí A mong muốn hoặc để mặc cho hậu quả xảy ra; động cơ là mâu thuẫn cá nhân; mục đích là gây tổn hại sức khỏe của B.
  * *Khách thể:* Hành vi đã xâm phạm đến quyền bất khả xâm phạm về sức khỏe, thân thể của con người được Hiến pháp và pháp luật hình sự bảo vệ.
  * *Chủ thể:* A đã 19 tuổi (đã qua tuổi chịu trách nhiệm hình sự theo Điều 12 BLHS), có nhận thức bình thường, do đó A có đầy đủ năng lực trách nhiệm pháp lý.
* **Khối 3 — Căn cứ pháp lý & Chế tài áp dụng:** Trích dẫn chính xác Điểm đ Khoản 1 Điều 134 Bộ luật Hình sự năm 2015 (sửa đổi 2017) về tội cố ý gây thương tích có dùng hung khí nguy hiểm.
* **Khối 4 — Huy hiệu xác thực an toàn:** Một dấu tích xanh hiển thị bên cạnh điều luật thông báo: *"Căn cứ Điều 134 BLHS 2015 đã được kiểm chứng tồn tại chính xác trong CSDL luật quốc gia"*.
* **Khối 5 — Bảng văn bản luật tham khảo:** Bên cạnh bài giải là một khung nhỏ trích nguyên văn lời của Điều 134 để sinh viên đọc lại và hiểu sâu hơn.

### 2. Đầu ra về mặt Dữ liệu và Trí tuệ nhân tạo (Tài sản Nghiên cứu)
* **Một bộ cơ sở dữ liệu chuẩn:** Gồm toàn văn 1.588 điều luật của 5 bộ luật lớn đã được làm sạch, bóc tách cấu trúc Điều/Khoản và lưu trữ trong CSDL SQLite.
* **Một bộ dữ liệu huấn luyện độc quyền (500 cặp câu hỏi - đáp án):** Được nhóm tự xây dựng dựa trên đề thi thật các năm của Đại học Bách Khoa và giáo trình chuẩn, được gán nhãn từng dạng bài thi. Đây là bộ dữ liệu cực kỳ có giá trị cho cộng đồng nghiên cứu NLP tiếng Việt về sau.
* **Một mô hình AI chuyên gia:** Bản trọng số LoRA nhỏ gọn (~65 MB) nhưng chứa đựng toàn bộ tri thức về cấu trúc bài thi Pháp luật Đại cương, có thể dễ dàng chia sẻ, nạp vào bất kỳ máy tính cá nhân nào mà không cần cài đặt phức tạp.

### 3. Đầu ra về mặt Báo cáo & Hồ sơ Đồ án (Nghiệm thu học phần PBL6)
* **Quyển Báo cáo Đồ án Chuyên ngành hoàn chỉnh:** Trình bày khoa học gồm 5 chương: Tổng quan đề tài; Cơ sở lý thuyết (BM25, Transformer, RAG, LoRA); Thiết kế kiến trúc hệ thống; Thực nghiệm đối sánh 4 tầng và đo lường định lượng; Kết luận và hướng phát triển.
* **Bảng số liệu thực nghiệm chứng minh sự tiến bộ:** Cung cấp đầy đủ các con số thuyết phục: Độ phủ tìm kiếm (Recall@5) tăng từ 58% ở Tầng 1 lên 82% ở Tầng 2; Điểm tương đồng ngữ nghĩa (BERTScore) tăng từ 0.72 ở Tầng 3 lên 0.85 ở Tầng 4; Tỷ lệ trích dẫn chính xác điều luật đạt 90%.

---

## VI. BỨC TRANH TOÀN CẢNH KHI HOÀN TẤT (TỔNG KẾT MỘT CÂU)

> **VietLawAssist** là một sản phẩm công nghệ hoàn chỉnh từ dữ liệu, mô hình học máy cho đến giao diện người dùng, biến một mô hình trí tuệ nhân tạo thông thường trở thành **người trợ lý học tập đắc lực, hiểu luật Việt Nam và biết cách giải bài thi môn Pháp luật Đại cương chuẩn xác đến từng barem điểm như một giảng viên đại học**, sẵn sàng vận hành thực tế và tự tin chinh phục điểm số xuất sắc trước hội đồng phản biện.
