# 🏛️ KHO TÀI LIỆU KINH ĐIỂN NGOẠI SINH ĐÃ QUA THẨM ĐỊNH
## Master Canonical External Knowledge Vault (AOC Vetted Tier)

> **Cơ quan giám định:** Agent `EKC-03` (Knowledge Curator & Quality Sentinel)  
> **Thước đo áp dụng:** [ER-QVR Rubric (100 Điểm)](file:///d:/User/7th/School/.agents/rules/external_resource_rubric.md)  
> **Mục đích:** Cung cấp nguồn tri thức chuẩn xác, nền tảng toán học vững chắc và mã nguồn tái lập được cho toàn bộ 6 môn học kỳ 7 khi slide trên lớp chưa có giáo trình chi tiết.

---

## 🧭 TỔNG QUAN XẾP HẠNG TÀI LIỆU CÁC MÔN HỌC

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 🏆 TIER A+ (>= 90đ): NGUỒN CỐT LÕI (Bắt buộc đọc để hiểu sâu bản chất lý thuyết & toán) │
│ ⭐ TIER A  (80-89đ): NGUỒN XUẤT SẮC (Dùng cho thực hành, code template và cẩm nang lab)│
│ 📚 TIER B  (70-79đ): NGUỒN BỔ TRỢ (Đọc thêm khi làm đồ án hoặc tra cứu nhanh)         │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. 👁️ COMPUTER VISION (THỊ GIÁC MÁY TÍNH)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :---: | :---: | :---: | :--- |
| **Stanford CS231n & Michigan EECS 498-007**<br/>*(Fei-Fei Li, Justin Johnson, Andrej Karpathy)* | Bài giảng ĐH | **96 / 100** | 🏆 Tier A+ | **Bản chất Backpropagation trên Tensor Conv2D**, trực quan hóa Feature Map, Gradient-weighted CAM, và kiến trúc mạng nơ-ron tích chập từ gốc rễ. |
| **Computer Vision: Algorithms and Applications (2nd ed, 2022)**<br/>*(Richard Szeliski - Springer)* | Sách giáo trình | **94 / 100** | 🏆 Tier A+ | **Hình học thị giác & Xử lý ảnh cổ điển**: Phép biến đổi không gian/tần số (2D Fourier, Sobel, Canny), Biến đổi Homography, SVD, SIFT/ORB, Camera Calibration. |
| **PyTorch Official Vision Architecture & Albumentations Docs**<br/>*(PyTorch Core Team)* | Tài liệu kỹ thuật | **92 / 100** | 🏆 Tier A+ | **Code chuẩn công nghiệp**: Viết custom PyTorch Dataset/DataLoader, Huấn luyện tăng tốc với Mixed Precision (`torch.cuda.amp`), data pipeline với Albumentations. |
| **Deep Learning (Chương 9: Convolutional Networks)**<br/>*(Ian Goodfellow, Yoshua Bengio - MIT Press)* | Sách giáo trình | **90 / 100** | 🏆 Tier A+ | Nền tảng toán học: Phép tích chập ma trận (Cross-correlation vs Convolution), Receptive Field, Tính bất biến tịnh tiến (Equivariance to translation). |

---

## 2. 🧠 HỌC MÁY VÀ ỨNG DỤNG (MACHINE LEARNING)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :---: | :---: | :---: | :--- |
| **Machine Learning Cơ Bản (machinelearningcoban.com)**<br/>*(Vũ Hữu Tiệp - Tiệp Vũ)* | Sách & Blog chuẩn | **95 / 100** | 🏆 Tier A+ | **Nguồn tiếng Việt xuất sắc nhất**: Dẫn dắt toán học giải tích/đại số tuyến tính mạch lạc; cung cấp code Numpy "From Scratch" từng bước cho Linear Regression, Logistic, Softmax, SVM, K-Means, PCA. |
| **Pattern Recognition and Machine Learning (PRML)**<br/>*(Christopher M. Bishop - Springer)* | Sách giáo trình | **96 / 100** | 🏆 Tier A+ | **Toán học xác suất chuyên sâu**: Bản chất ước lượng hợp lý cực đại (MLE), MAP, suy diễn Bayes, thuật toán Expectation-Maximization (EM) cho Gaussian Mixture Models (GMM), và điều kiện KKT trong SVM. |
| **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (3rd ed)**<br/>*(Aurélien Géron - O'Reilly)* | Sách thực chiến | **94 / 100** | 🏆 Tier A+ | **Quy trình ML Pipeline thực tế**: Xử lý dữ liệu khuyết, Feature Scaling, Pipeline tuning bằng GridSearchCV, Mô hình Cây & Ensemble (Random Forest, XGBoost, LightGBM). |
| **CS229: Machine Learning Lecture Notes**<br/>*(Andrew Ng - Stanford University)* | Bài giảng ĐH | **93 / 100** | 🏆 Tier A+ | Trực quan hóa đạo hàm Gradient Descent, hàm mất mát lồi (Convex Loss), và kỹ thuật chuẩn hóa L1/L2 regularization. |

---

## 3. 📡 QUẢN TRỊ MẠNG (NETWORK MANAGEMENT - NMA-DUT)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :---: | :---: | :---: | :--- |
| **Cisco CCNA 200-301 Official Cert Guide (Vol 1 & 2)**<br/>*(Wendell Odom - Cisco Press)* | Sách chuyên môn | **97 / 100** | 🏆 Tier A+ | **Khung lệnh CLI Cisco chuẩn mực**: Thiết kế VLAN, Trunking 802.1Q, EtherChannel, Router-on-a-stick, DHCP Relay Agent, OSPF single-area, Standard/Extended ACL. |
| **Computer Networking: A Top-Down Approach (8th ed)**<br/>*(James Kurose & Keith Ross - Pearson)* | Sách giáo trình | **95 / 100** | 🏆 Tier A+ | **Bản chất giao thức mạng**: Quy trình bắt tay 4 bước DHCP DORA, Kiến trúc phân cấp DNS và Resource Records (A, CNAME, MX, PTR), Cơ chế bẫy gói tin SNMPv2c/v3. |
| **Red Hat Enterprise Linux 9 System Administration Guide & Microsoft Learn Server 2022**<br/>*(Red Hat & Microsoft Official)* | Tài liệu hãng | **93 / 100** | 🏆 Tier A+ | **Vận hành máy chủ doanh nghiệp**: Cấu hình BIND9 DNS, isc-dhcp-server, Samba chia sẻ tệp, Active Directory Domain Services (AD DS), Group Policy Objects (GPO). |
| **RFC 2131 (DHCP), RFC 1035 (DNS), RFC 1157 (SNMP)**<br/>*(Internet Engineering Task Force - IETF)* | Tiêu chuẩn quốc tế | **91 / 100** | 🏆 Tier A+ | Tiêu chuẩn gốc về cấu trúc bản tin, mã lỗi và cờ hiệu giao thức mạng. |

---

## 4. 🔐 AN TOÀN MẠNG (NETWORK SECURITY)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :---: | :---: | :---: | :--- |
| **Cryptography and Network Security: Principles and Practice (8th ed)**<br/>*(William Stallings - Pearson)* | Sách giáo trình | **96 / 100** | 🏆 Tier A+ | **Toán mật mã ứng dụng**: Cấu trúc khối AES (SubBytes, ShiftRows, MixColumns), Mã công khai RSA và đường cong Elliptic (ECC), Hàm băm SHA-256/SHA-3, Chữ ký số, Hạ tầng PKI/X.509. |
| **NIST Special Publications (SP 800-52r2, SP 800-77r1, SP 800-115)**<br/>*(National Institute of Standards and Technology)* | Tiêu chuẩn an ninh | **94 / 100** | 🏆 Tier A+ | **Chuẩn an toàn công nghiệp**: Hướng dẫn cấu hình an toàn TLS 1.3, Triển khai VPN IPsec (IKEv2, ESP Tunnel Mode, Diffie-Hellman Group 14/19), Quy trình kiểm thử an toàn mạng. |
| **Wireshark Network Analysis: The Official WCNA Study Guide**<br/>*(Laura Chappell - Wireshark Press)* | Sách thực hành | **93 / 100** | 🏆 Tier A+ | **Kỹ thuật phân tích gói tin chuyên sâu**: Soi byte bắt tay TCP 3 bước, Nhận diện tấn công ARP Poisoning, SYN Flood, Bẻ khóa handshake WPA2, Display Filters nâng cao. |
| **Cisco Network Security & Zone-Based Policy Firewall Guide**<br/>*(Cisco Systems)* | Cẩm nang hãng | **90 / 100** | 🏆 Tier A+ | Cấu hình tường lửa trạng thái (Stateful Firewall), Phân vùng DMZ, Kiểm soát truy cập AAA (RADIUS, TACACS+). |

---

## 5. 🇯🇵 TIẾNG NHẬT N3 (JAPANESE JLPT N3)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :---: | :---: | :---: | :--- |
| **Shinkanzen Master N3 (Trọn bộ 4 cuốn: Ngữ pháp, Từ vựng, Hán tự, Đọc hiểu)**<br/>*(3A Corporation)* | Bộ sách luyện thi | **97 / 100** | 🏆 Tier A+ | **Bộ sách luyện tư duy phản biện số 1**: Phân biệt triệt để các mẫu ngữ pháp đồng nghĩa dễ nhầm lẫn; bẫy đọc hiểu đảo ngược ý; phương pháp phân tích câu dài. |
| **Mimi Kara Oboeru N3 (Từ vựng & Nghe hiểu)**<br/>*(ALC Press)* | Sách phản xạ âm | **94 / 100** | 🏆 Tier A+ | **Học từ vựng theo cụm (Collocation)**: Đi kèm file âm thanh giúp kích hoạt trí nhớ thính giác và phản xạ câu hỏi ngắn tức thì trong đề thi JLPT. |
| **Nihongo Soumatome N3 (Trọn bộ 5 kỹ năng)**<br/>*(Ask Publishing)* | Bộ sách theo tuần | **88 / 100** | ⭐ Tier A | Phân bổ lộ trình học theo tuần (6 tuần hoàn thành), nhiều hình ảnh trực quan sinh động giúp nắm bắt từ vựng và chữ Hán ban đầu. |
| **Shin Nihongo 500 Mon N3**<br/>*(Ask Publishing)* | Sách luyện đề nhanh | **91 / 100** | 🏆 Tier A+ | Drill 500 câu hỏi ngắn trắc nghiệm tổng hợp (Chữ Hán - Từ vựng - Ngữ pháp) làm bài test hàng ngày. |

---

## 6. 🤖 ĐỒ ÁN CHUYÊN NGÀNH PBL6 (VIETLAWASSIST - LEGAL AI)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :---: | :---: | :---: | :--- |
| **Retrieval-Augmented Generation for Large Language Models: A Survey (2023)**<br/>*(Yunfan Gao et al.)* | Bài báo khoa học | **96 / 100** | 🏆 Tier A+ | **Kiến trúc RAG chuẩn doanh nghiệp**: Chunking văn bản luật phân cấp, So sánh Sparse (BM25) vs Dense (Embedding), Cosine Similarity, Cross-Encoder Reranking. |
| **QLoRA: Efficient Finetuning of Quantized LLMs (2023)**<br/>*(Tim Dettmers et al. - NeurIPS 2023)* | Bài báo khoa học | **95 / 100** | 🏆 Tier A+ | **Kỹ thuật tối ưu trên phần cứng giới hạn (GPU 4GB VRAM)**: NF4 Quantization, Double Quantization, Paged Optimizers, LoRA adapters cho mô hình ngôn ngữ tiếng Việt. |
| **TruLens & Ragas Evaluation Framework Documentation**<br/>*(TruEra & Ragas AI)* | Tài liệu mã nguồn | **92 / 100** | 🏆 Tier A+ | Bộ 3 thước đo RAG Triad: Context Relevance, Groundedness (Faithfulness), và Answer Relevance để đánh giá định lượng hệ sinh thái VietLawAssist. |

---

## 7. ⚡ ALGORITHMS & SYSTEMS ENGINEERING (C++ & DSA — CORP-07-ALGO)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :--- | :---: | :---: | :--- |
| **Introduction to Algorithms - CLRS (4th ed, 2022)**<br/>*(Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein - MIT Press)* | Sách giáo trình kinh điển | **98 / 100** | 🏆 Tier A+ | **"Kinh thánh Thuật toán"**: Nền tảng phân tích tiệm cận Big-O, Đồ thị (Dijkstra, Bellman-Ford, MST), Quy hoạch động (DP Memoization & Tabulation), B-Tree, Cây Đỏ-Đen (Red-Black Tree), và chứng minh toán học bất biến. |
| **The Algorithm Design Manual (3rd ed, 2020)**<br/>*(Steven S. Skiena - Springer)* | Sách cẩm nang giải thuật | **95 / 100** | 🏆 Tier A+ | **Tư duy nhận diện bài toán thực tế**: Danh mục tra cứu thuật toán ("The Hitchhiker's Guide to Algorithms"), chiến lược giải quyết bài toán NP-đầy đủ, heuristic tìm kiếm cục bộ và kinh nghiệm phỏng vấn kỹ thuật thực chiến. |
| **A Tour of C++ (3rd ed, C++20, 2022) & C++ Core Guidelines**<br/>*(Bjarne Stroustrup, Herb Sutter - Addison-Wesley / Standard C++ Foundation)* | Sách tiêu chuẩn & Hướng dẫn | **97 / 100** | 🏆 Tier A+ | **Kỹ thuật C++ hiện đại**: Quản lý bộ nhớ an toàn qua RAII, Smart Pointers (`std::unique_ptr`, `std::shared_ptr`), Move Semantics, Khái niệm Concepts, Ranges, và triệt tiêu toàn bộ việc dùng con trỏ trần (`raw pointer`) gây rò rỉ. |
| **Computer Systems: A Programmer's Perspective - CS:APP (3rd ed)**<br/>*(Randal E. Bryant & David R. O'Hallaron - Pearson)* | Sách hệ thống phần cứng | **96 / 100** | 🏆 Tier A+ | **Tư duy hệ thống dưới góc nhìn lập trình viên**: Thứ bậc bộ nhớ (Memory Hierarchy), Cache Locality (L1/L2/L3), Chi phí hoán đổi ngữ cảnh (Context Switch), Tối ưu hóa pipeline CPU và kiến trúc phân bổ bộ nhớ động. |

---

## 8. 📐 SOFTWARE ARCHITECTURE, OOAD & TDD (CORP-08-CRAFT)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :--- | :---: | :---: | :--- |
| **Design Patterns: Elements of Reusable Object-Oriented Software (GoF)**<br/>*(Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides - Addison-Wesley)* | Sách kinh điển nền tảng | **94 / 100** | 🏆 Tier A+ | **Nền móng 23 mẫu thiết kế phần mềm**: Tư duy lập trình với Interface/Abstractions, phân loại Creational, Structural, Behavioral patterns. *(Lưu ý: Thanh lọc bỏ anti-pattern Singleton và kế thừa sâu; cập nhật sang Modern C++/Python/TS)*. |
| **Dive Into Design Patterns (2020+)**<br/>*(Alexander Shvets - Refactoring.Guru)* | Sách trực quan hiện đại | **96 / 100** | 🏆 Tier A+ | **Minh họa trực quan đa ngôn ngữ**: Mổ xẻ 23 mẫu thiết kế bằng sơ đồ sinh động, chỉ rõ sự tiến hóa từ Clean Code $\rightarrow$ Refactoring $\rightarrow$ Patterns, và cẩm nang nhận diện khi nào nên áp dụng, khi nào tránh lạm dụng. |
| **Unit Testing Principles, Practices, and Patterns (2020)**<br/>*(Vladimir Khorikov - Manning)* | Sách kiểm thử hiện đại | **97 / 100** | 🏆 Tier A+ | **"Kinh thánh Kiểm thử Hiện đại"**: Phân định trường phái Classicist vs Mockist testing; 4 trụ cột của một Unit Test tốt; Triệt tiêu Flaky Tests; Kỹ thuật tái cấu trúc code an toàn dựa trên độ tin cậy của test suite. |
| **Refactoring: Improving the Design of Existing Code (2nd ed, 2018)**<br/>*(Martin Fowler - Addison-Wesley)* | Sách thực nghiệm tái cấu trúc | **96 / 100** | 🏆 Tier A+ | **Danh mục Code Smells & Kỹ thuật chuyển dịch mã nguồn**: Sử dụng ví dụ JavaScript/Modern; kỹ thuật refactor từng bước nhỏ bảo tồn hành vi; kết hợp chặt chẽ với kiểm thử tự động để bảo vệ chất lượng phần mềm dài hạn. |

---

## 9. 🚀 AGILE, SCRUM & ENTERPRISE SDLC (CORP-09-AGILE)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :--- | :---: | :---: | :--- |
| **The 2020 Scrum Guide (Official)**<br/>*(Ken Schwaber & Jeff Sutherland - Scrum.org)* | Hướng dẫn định chuẩn thế giới | **98 / 100** | 🏆 Tier A+ | **Quy tắc gốc rễ của Scrum**: 3 Vai trò (PO, SM, Developers), 5 Sự kiện, 3 Hiện vật (Product Backlog, Sprint Backlog, Increment); cam kết Product Goal, Sprint Goal và Definition of Done (DoD) tinh gọn, loại bỏ nghi thức rườm rà. |
| **User Stories Applied: For Agile Software Development**<br/>*(Mike Cohn - Addison-Wesley)* | Sách nghiệp vụ Agile | **94 / 100** | 🏆 Tier A+ | **Kỹ thuật phân rã yêu cầu phần mềm**: Tiêu chuẩn **INVEST** cho User Story; Kỹ thuật ước lượng tương đối Planning Poker & Story Points; Lập bản đồ hành trình người dùng và quản trị Backlog. |
| **Pro Git (2nd ed, Cập nhật liên tục)**<br/>*(Scott Chacon & Ben Straub - Apress)* | Sách kỹ thuật mã nguồn mở | **97 / 100** | 🏆 Tier A+ | **Bản chất quản trị mã nguồn**: Kiến trúc bên trong của Git (Blobs, Trees, Commits, Tags); So sánh chiến lược phân nhánh GitFlow vs Trunk-Based; Giải quyết xung đột Merge/Rebase; Quản trị bảo mật qua GPG Commit signing. |
| **Accelerate: The Science of Lean Software and DevOps (2018)**<br/>*(Nicole Forsgren, Jez Humble, Gene Kim - IT Revolution)* | Nghiên cứu thực nghiệm khoa học | **95 / 100** | 🏆 Tier A+ | **Bộ 4 chỉ số DORA Metrics**: Tần suất triển khai (Deployment Frequency), Thời gian thay đổi (Lead Time for Changes), Thời gian phục hồi (MTTR), Tỷ lệ lỗi thay đổi (Change Failure Rate); kết nối Agile với văn hóa CI/CD tự động. |

---

## 10. 🌐 WEBSCALE FULL-STACK TECHNOLOGIES (JS/TS — CORP-10-WEB)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :--- | :---: | :---: | :--- |
| **You Don't Know JS Yet (YDKJSY - 2nd ed)**<br/>*(Kyle Simpson - Getify)* | Bộ sách chuyên sâu ngôn ngữ | **97 / 100** | 🏆 Tier A+ | **Đáy sâu của JavaScript**: Cơ chế hoạt động của V8 Engine, Scope & Closures, Con trỏ `this` & Object Prototypes, Quản lý bất đồng bộ (Event Loop, Macrotask, Microtask, Promises). |
| **TypeScript Official Documentation & Handbook (v5+)**<br/>*(Microsoft TypeScript Team)* | Tài liệu chuẩn công nghiệp | **96 / 100** | 🏆 Tier A+ | **Hệ thống kiểu tĩnh cho ứng dụng quy mô lớn**: Type Inference, Structural Typing, Generics nâng cao, Conditional Types, Mapped Types, Template Literal Types, Decorators và Type Narrowing an toàn. |
| **React Official Documentation (react.dev - Modern Hooks & RSC)**<br/>*(Meta Open Source Team)* | Tài liệu kiến trúc giao diện | **95 / 100** | 🏆 Tier A+ | **Tư duy giao diện hiện đại**: Kiến trúc Reconciliation (React Fiber), Mô hình dữ liệu một chiều (Unidirectional Data Flow), Custom Hooks, React Server Components (RSC) và quản lý trạng thái hiệu năng cao. |
| **NestJS Enterprise Architecture Documentation (v10+)**<br/>*(Kamil Myśliwiec & NestJS Team)* | Khung kiến trúc Backend | **94 / 100** | 🏆 Tier A+ | **Kỹ nghệ Backend Node.js doanh nghiệp**: Ứng dụng toàn diện OOP, Dependency Injection (IoC Container), Mô hình phân lớp Controller-Service-Repository, Modular Architecture, Guards, Interceptors và Pipes. |

---

## 11. 🐍 PYSCALE BACKEND & DISTRIBUTED SYSTEMS (PYTHON — CORP-11-PY)

| Tên Tài Liệu & Tác Giả | Loại Hình | Điểm ER-QVR | Phân Cấp | Giá Trị Cốt Lõi Chắt Lọc |
| :--- | :--- | :---: | :---: | :--- |
| **Fluent Python: Clear, Concise, and Effective Programming (2nd ed, 2022)**<br/>*(Luciano Ramalho - O'Reilly)* | Sách chuyên sâu ngôn ngữ | **98 / 100** | 🏆 Tier A+ | **"Kinh thánh Pythonic"**: Python Data Model (`__dunder__` methods), Cấu trúc dữ liệu nâng cao, Generators & Coroutines, Type Hints, Decorators, Metaprogramming và AsyncIO hiện đại. |
| **Robust Python: Write Clean and Maintainable Code (2021)**<br/>*(Patrick Viafore - O'Reilly)* | Sách chất lượng phần mềm | **95 / 100** | 🏆 Tier A+ | **Xây dựng hệ thống Python chuẩn doanh nghiệp**: Kiểm soát kiểu tĩnh với Mypy & Pydantic, Định nghĩa Domain Model bất biến (Data Classes, TypedDict), Kỹ thuật phòng ngừa lỗi lúc chạy (Defensive Programming). |
| **FastAPI Documentation & Asynchronous Python Web Guide**<br/>*(Sebastián Ramírez - Tiangolo)* | Tài liệu framework hiện đại | **96 / 100** | 🏆 Tier A+ | **Backend API hiệu năng cực hạn**: Lập trình bất đồng bộ với `async`/`await`, Tự động xác thực dữ liệu qua Pydantic v2, Hệ thống Dependency Injection mạnh mẽ, Tích hợp chuẩn OpenAPI/Swagger tự động. |
| **SQLAlchemy 2.0 Documentation & Distributed Task Queues (Celery/Redis)**<br/>*(Michael Bayer & Celery Project)* | Tài liệu dữ liệu & phân tán | **94 / 100** | 🏆 Tier A+ | **Truy xuất dữ liệu bất đồng bộ & Hàng đợi công việc**: Kiến trúc SQLAlchemy 2.0 AsyncSession, Ngăn ngừa N+1 queries, Quản lý transaction, Hàng đợi xử lý tác vụ ngầm Celery + Redis, Caching và Worker scaling. |

---

## 🔗 HƯỚNG DẪN TRA CỨU NHANH
Khi cần mở rộng bất kỳ chủ đề nào trong các tuần học, hãy đối chiếu cột `Tên Tài Liệu` ở trên với thư mục giáo trình của môn học đó (`ROADMAP_AND_CURRICULUM.md`). Mọi module bài học đều được đính kèm chú thích trỏ trực tiếp đến các chương sách kinh điển này!
