/* Section-aware, bilingual guide companion for the public portfolio assistant. */
(() => {
  const root = document.documentElement;
  const guide = document.getElementById('ai-guide');
  const trigger = document.getElementById('ai-guide-trigger');
  const bubble = document.getElementById('ai-guide-bubble');
  const copy = document.getElementById('ai-guide-copy');
  const askButton = document.getElementById('ai-guide-ask');
  const dismiss = document.getElementById('ai-guide-dismiss');
  if (!guide || !trigger || !bubble || !copy || !askButton) return;

  const sections = Array.from(document.querySelectorAll('#main-content section[id]'));
  const sectionCopy = {
    hello: {
      en: { message: "Welcome. Scroll through the chapters and I'll point out the useful details about Yash.", question: 'Who is Yash?' },
      hi: { message: 'नमस्ते! इन सेक्शनों में Yash की पढ़ाई, काम और रुचियों की जानकारी देखें।', question: 'Yash कौन हैं?' }
    },
    'yash-os': {
      en: { message: "Here's Yash's quick snapshot: what he's studying, building, and focusing on.", question: "What is Yash's current state and focus?" },
      hi: { message: 'यहाँ Yash की पढ़ाई, काम और मौजूदा फोकस का छोटा परिचय है।', question: 'Yash का मौजूदा फोकस क्या है?' }
    },
    currently: {
      en: { message: "A quick look at what Yash is exploring and working on right now.", question: 'What is Yash working on right now?' },
      hi: { message: 'यहाँ देखें कि Yash अभी किन चीज़ों पर काम और सीख रहे हैं।', question: 'Yash अभी किस पर काम कर रहे हैं?' }
    },
    journey: {
      en: { message: "This is Yash's journey timeline. Open a year to read the full story.", question: "Give me a quick tour of Yash's journey." },
      hi: { message: 'यह Yash की यात्रा है—पूरी कहानी पढ़ने के लिए कोई वर्ष खोलें।', question: 'Yash की यात्रा के बारे में बताइए।' }
    },
    experience: {
      en: { message: "Here you'll find Yash's public roles and creative work. Open a card to explore the details.", question: 'What experience does Yash have?' },
      hi: { message: 'यहाँ Yash की भूमिकाएँ और रचनात्मक काम हैं—विवरण खोलकर पढ़ें।', question: 'Yash का अनुभव क्या है?' }
    },
    focus: {
      en: { message: "This section covers Yash's current priorities and projects.", question: 'What is Yash focused on right now?' },
      hi: { message: 'इस सेक्शन में Yash की मौजूदा प्राथमिकताएँ और प्रोजेक्ट हैं।', question: 'Yash का अभी मुख्य फोकस क्या है?' }
    },
    credentials: {
      en: { message: "Browse Yash's public credentials and project proof here.", question: "Show me Yash's credentials and projects." },
      hi: { message: 'यहाँ Yash के सार्वजनिक प्रमाणपत्र और प्रोजेक्ट देखें।', question: 'Yash के प्रमाणपत्र और प्रोजेक्ट बताइए।' }
    },
    skills: {
      en: { message: "Yash's skills and tools are grouped here for a quick scan.", question: 'What skills and tools does Yash use?' },
      hi: { message: 'Yash के कौशल और टूल्स यहाँ जल्दी देखने के लिए दिए हैं।', question: 'Yash कौन से कौशल और टूल्स इस्तेमाल करते हैं?' }
    },
    contact: {
      en: { message: "Want to connect with Yash? His public contact links are here.", question: 'How can I contact Yash?' },
      hi: { message: 'Yash से जुड़ना चाहते हैं? उनके सार्वजनिक संपर्क लिंक यहाँ हैं।', question: 'मैं Yash से कैसे संपर्क करूँ?' }
    }
  };

  let activeId = '';
  let sectionTimer = 0;
  let hideTimer = 0;
  let lastSpokenId = '';
  const clamp = (value, min, max) => Math.min(max, Math.max(min, value));
  const isHindi = () => root.lang === 'hi';

  function hideBubble() {
    bubble.classList.remove('ai-guide-visible');
    bubble.setAttribute('aria-hidden', 'true');
    window.clearTimeout(hideTimer);
    hideTimer = window.setTimeout(() => { bubble.hidden = true; }, 200);
  }
  window.hidePortfolioGuideBubble = hideBubble;

  function positionGuide(id) {
    const section = document.getElementById(id);
    if (!section) return;
    const rect = section.getBoundingClientRect();
    const index = Math.max(0, sections.indexOf(section));
    const side = index % 2 === 0 ? 'right' : 'left';
    const mobile = window.matchMedia('(max-width: 720px)').matches;
    const size = mobile ? 54 : 68;
    const edge = mobile ? 9 : 14;
    const x = side === 'right' ? window.innerWidth - size - edge : edge;
    const preferredTop = rect.top + Math.min(150, Math.max(76, rect.height * .18));
    const maxTop = Math.max(104, window.innerHeight - (mobile ? 170 : 142));
    const y = clamp(preferredTop, 104, maxTop);
    guide.dataset.side = side;
    guide.style.left = `${clamp(x, 8, Math.max(8, window.innerWidth - size - 8))}px`;
    guide.style.top = `${y}px`;
  }

  function activateSection(id, announce = true) {
    const current = sectionCopy[id];
    if (!current) return;
    activeId = id;
    positionGuide(id);
    const localized = isHindi() ? current.hi : current.en;
    askButton.dataset.question = localized.question;
    askButton.textContent = isHindi() ? 'इस सेक्शन के बारे में पूछें ↗' : 'Ask about this section ↗';
    trigger.setAttribute('aria-label', isHindi() ? `${id.replace(/-/g, ' ')} सेक्शन के बारे में पूछें` : `Ask about the ${id.replace(/-/g, ' ')} section`);
    if (dismiss) dismiss.setAttribute('aria-label', isHindi() ? 'टिप बंद करें' : 'Dismiss guide tip');
    copy.textContent = localized.message;

    if (!announce || window.scrollY < 80 || document.hidden || window.isYashAssistantOpen?.()) return;
    bubble.hidden = false;
    bubble.setAttribute('aria-hidden', 'false');
    window.requestAnimationFrame(() => bubble.classList.add('ai-guide-visible'));
    window.clearTimeout(hideTimer);
    hideTimer = window.setTimeout(hideBubble, 8200);

    if (lastSpokenId !== id && window.portfolioAssistantVoiceEnabled?.()) {
      lastSpokenId = id;
      window.speakPortfolioAssistant?.(localized.message);
    }
  }

  function requestSection(id) {
    if (!sectionCopy[id] || id === activeId) return;
    window.clearTimeout(sectionTimer);
    sectionTimer = window.setTimeout(() => activateSection(id, true), 260);
  }

  trigger.addEventListener('click', () => window.toggleYashAssistant?.());
  askButton.addEventListener('click', () => {
    const question = askButton.dataset.question;
    hideBubble();
    window.openYashAssistant?.(question);
  });
  dismiss?.addEventListener('click', hideBubble);
  root.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') hideBubble();
  });
  document.addEventListener('visibilitychange', () => { if (document.hidden) hideBubble(); });
  window.addEventListener('resize', () => { if (activeId) positionGuide(activeId); }, { passive: true });

  const sectionObserver = new MutationObserver(() => {
    const id = root.dataset.activeChapter || sections[0]?.id || '';
    if (!id) return;
    if (id === activeId) activateSection(id, false);
    else requestSection(id);
  });
  sectionObserver.observe(root, { attributes: true, attributeFilter: ['data-active-chapter', 'lang'] });

  if (root.dataset.activeChapter) activateSection(root.dataset.activeChapter, false);
  else if (sections[0]) activateSection(sections[0].id, false);
  root.classList.add('ai-guide-ready');
})();
