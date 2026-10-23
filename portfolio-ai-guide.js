/* Section-aware guide for the existing offline portfolio assistant. */
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
    hello: { message: "Hey, welcome. Scroll with me and I'll point out the useful bits about Yash.", question: 'Who is Yash?' },
    'yash-os': { message: "Here's Yash's quick snapshot: what he's studying, building, and focusing on.", question: "What is Yash's current state and focus?" },
    journey: { message: "This is Yash's journey timeline. Open a year to see the full story.", question: "Give me a quick tour of Yash's journey." },
    experience: { message: "Here you'll find his college-society roles and freelance creative work. Tap to explore the details.", question: "What experience roles does Yash have?" },
    focus: { message: "This section covers Yash's current priorities and projects.", question: "What is Yash focused on right now?" },
    credentials: { message: "Browse Yash's public credentials and project proof here.", question: "Show me Yash's credentials and projects." },
    skills: { message: "Yash's skills and tools are grouped here for a quick scan.", question: "What skills and tools does Yash use?" },
    contact: { message: "Want to connect with Yash? His public contact links are here.", question: "How can I contact Yash?" }
  };

  let activeId = '';
  let sectionTimer = 0;
  let hideTimer = 0;
  let lastSpokenId = '';
  const clamp = (value, min, max) => Math.min(max, Math.max(min, value));

  function hideBubble() {
    bubble.classList.remove('ai-guide-visible');
    bubble.setAttribute('aria-hidden', 'true');
    window.clearTimeout(hideTimer);
    hideTimer = window.setTimeout(() => { bubble.hidden = true; }, 230);
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
    if (!sectionCopy[id]) return;
    activeId = id;
    positionGuide(id);
    const current = sectionCopy[id];
    askButton.dataset.question = current.question;
    trigger.setAttribute('aria-label', `Open portfolio guide: ${id.replace(/-/g, ' ')} section`);
    if (!announce || window.scrollY < 80 || document.hidden || window.isYashAssistantOpen?.()) return;

    copy.textContent = current.message;
    bubble.hidden = false;
    bubble.setAttribute('aria-hidden', 'false');
    window.requestAnimationFrame(() => bubble.classList.add('ai-guide-visible'));
    window.clearTimeout(hideTimer);
    hideTimer = window.setTimeout(hideBubble, 8200);

    if (lastSpokenId !== id && window.portfolioAssistantVoiceEnabled?.()) {
      lastSpokenId = id;
      window.speakPortfolioAssistant?.(current.message);
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
    requestSection(root.dataset.activeChapter || '');
  });
  sectionObserver.observe(root, { attributes: true, attributeFilter: ['data-active-chapter'] });

  if (root.dataset.activeChapter) activateSection(root.dataset.activeChapter, false);
  else if (sections[0]) activateSection(sections[0].id, false);
  root.classList.add('ai-guide-ready');
})();
