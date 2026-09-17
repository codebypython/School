(() => {
  let posts = [];

  // 1. Tìm các thẻ bài đăng dựa trên mỏ neo nút Reply
  const replyButtons = Array.from(document.querySelectorAll('button')).filter(b => 
    b.innerText.trim().toLowerCase().includes('reply')
  );

  let cards = [];
  if (replyButtons.length > 0) {
    cards = replyButtons.map(btn => 
      btn.closest('[class*="fui-Card"]') || 
      btn.closest('div[tabindex]') || 
      btn.parentElement.parentElement.parentElement
    );
  } else {
    cards = Array.from(document.querySelectorAll('[data-tid="thread-item"], [data-tid="channel-post"], [role="article"]'));
  }

  cards = [...new Set(cards)].filter(Boolean);

  // 2. Trích xuất văn bản kèm toàn bộ Hyperlink
  cards.forEach((card, index) => {
    // Nhân bản card để can thiệp cấu trúc mà không ảnh hưởng UI hiển thị
    const clone = card.cloneNode(true);
    const linksFound = [];

    // Quét và chuyển đổi tất cả thẻ <a> thành định dạng [Text](URL)
    clone.querySelectorAll('a').forEach(a => {
      const text = a.innerText.trim() || 'Liên kết';
      let href = a.getAttribute('href') || a.href;

      if (href && !href.startsWith('javascript:')) {
        // Chuẩn hóa nếu là đường dẫn nội bộ tương đối
        if (href.startsWith('/')) {
          href = `${window.location.origin}${href}`;
        }
        linksFound.push({ text, href });
        
        // Dùng createTextNode để không bị TrustedHTML chặn
        a.replaceWith(document.createTextNode(` [${text}](${href}) `));
      }
    });

    // Quét thêm các tệp đính kèm có thuộc tính data-href (nếu có)
    clone.querySelectorAll('[data-href]').forEach(el => {
      const href = el.getAttribute('data-href');
      const text = el.innerText.trim() || 'Tệp đính kèm';
      if (href) {
        linksFound.push({ text, href });
        el.replaceWith(document.createTextNode(` [${text}](${href}) `));
      }
    });

    // Làm sạch các dòng thừa, nút bấm UI và reaction
    const rawText = clone.innerText.trim();
    const cleanedLines = rawText
      .split('\n')
      .map(line => line.trim())
      .filter(line => line && !line.match(/^(Reply|Post in channel|Edited|Đã chỉnh sửa|👍|❤️|🔥|😆|😮|😢|😡|\d+)$/i));

    if (cleanedLines.length > 0) {
      let postEntry = `## Bài đăng ${index + 1}\n\n${cleanedLines.join('\n\n')}`;

      // Bổ sung mục tổng hợp liên kết ở cuối mỗi bài viết cho AI agent dễ truy vấn
      if (linksFound.length > 0) {
        postEntry += `\n\n** Danh mục liên kết & tệp trong bài:**\n`;
        const uniqueLinks = Array.from(new Set(linksFound.map(l => JSON.stringify(l)))).map(s => JSON.parse(s));
        uniqueLinks.forEach(l => {
          postEntry += `* [${l.text}](${l.href})\n`;
        });
      }

      posts.push(postEntry);
    }
  });

  // 3. Fallback nếu không gom được qua card
  let finalContent = posts.join('\n\n---\n\n');
  if (!finalContent) {
    const mainViewport = document.querySelector('[data-tid="message-pane-list-viewport"]') || document.querySelector('[role="main"]');
    finalContent = mainViewport ? mainViewport.innerText : document.body.innerText;
  }

  // 4. Tạo Blob và tải file .md về máy
  const blob = new Blob([finalContent], { type: 'text/markdown;charset=utf-8;' });
  const downloadUrl = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = downloadUrl;

  const channelName = document.querySelector('h1, [data-tid="channel-name"]')?.innerText?.trim() || 'Teams_Channel';
  a.download = `${channelName.replace(/[^\w\s-]/gi, '_')}_Posts_With_Links.md`;

  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(downloadUrl);

  console.log(` Đã trích xuất thành công ${posts.length} bài đăng kèm hyperlink đầy đủ!`);
})();