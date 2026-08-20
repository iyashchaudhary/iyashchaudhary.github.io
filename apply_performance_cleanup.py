from pathlib import Path

ROOT = Path(__file__).parent
INDEX = ROOT / 'index.html'
JOURNAL = ROOT / 'unfiltered.html'
MARKER = '/* PERFORMANCE_CLEANUP_V1 */'

performance_css = f'''\n<style id="performance-cleanup-v1">\n{MARKER}\nhtml{{scroll-behavior:auto!important}}\n@media (max-width:760px), (pointer:coarse){{\n  html{{scroll-behavior:auto!important;overscroll-behavior-y:auto!important}}\n  body{{background-attachment:scroll!important;touch-action:pan-y;-webkit-overflow-scrolling:touch}}\n  #fireflies,#petal-field,.firefly,.petal,.trail-petal{{display:none!important}}\n  .hero-scene,.hero-scene::before,.hero-scene::after{{animation:none!important;transform:none!important}}\n  :where(.glass,.hero-glass,.section.bento-card,.journey-studio,.studio-panel,.folio){{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}}\n  :where(*,*::before,*::after){{will-change:auto!important}}\n  .apple-float{{animation:none!important;transform:none!important}}\n}}\n@media (prefers-reduced-motion:reduce){{\n  :where(*,*::before,*::after){{scroll-behavior:auto!important;animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important}}\n}}\n</style>\n'''


def patch_index():
    text = INDEX.read_text(encoding='utf-8')
    text = text.replace("assets/portfolio-scenic-blue-hero.jpg", "assets/portfolio-scenic-blue-hero.webp")
    if 'id="portfolio-hero-preload"' not in text:
        text = text.replace('<head>', '<head>\n<link id="portfolio-hero-preload" rel="preload" as="image" href="assets/portfolio-scenic-blue-hero.webp" fetchpriority="high">', 1)
    if MARKER not in text:
        text = text.replace('</head>', performance_css + '</head>', 1)
    text = text.replace("const layer = document.getElementById('fireflies');\n  if(!layer) return;", "const layer = document.getElementById('fireflies');\n  if(!layer || window.matchMedia('(max-width:760px), (pointer:coarse)').matches) return;")
    text = text.replace("const field = document.getElementById('petal-field');\n  if(!field) return;\n  const prefersReduced", "const field = document.getElementById('petal-field');\n  if(!field || window.matchMedia('(max-width:760px), (pointer:coarse)').matches) return;\n  const prefersReduced", 1)
    text = text.replace("const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;\n    const links", "const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;\n    const lite = window.matchMedia && window.matchMedia('(max-width:760px), (pointer:coarse)').matches;\n    const links", 1)
    text = text.replace("let ticking = false;\n    window.addEventListener('scroll'", "if (lite) { root.style.setProperty('--story-progress', '0%'); return; }\n    let ticking = false;\n    window.addEventListener('scroll'", 1)
    text = text.replace("const reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;\n  const revealTargets", "const reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;\n  const lite=window.matchMedia('(max-width:760px), (pointer:coarse)').matches;\n  const revealTargets", 1)
    text = text.replace("if(reduce){revealTargets.forEach(el=>el.classList.add('is-visible'));return;}", "if(reduce || lite){revealTargets.forEach(el=>el.classList.add('is-visible'));return;}", 1)
    text = text.replace("const root = document.documentElement;\n  root.dataset.autonomousPolish", "const root = document.documentElement;\n  const lite = window.matchMedia && window.matchMedia('(max-width:760px), (pointer:coarse)').matches;\n  root.dataset.autonomousPolish", 1)
    text = text.replace("if ('IntersectionObserver' in window && chapters.length) {", "if (!lite && 'IntersectionObserver' in window && chapters.length) {", 1)
    text = text.replace("requestAnimationFrame(() => root.classList.add('autonomous-polish-ready'));", "if (!lite) requestAnimationFrame(() => root.classList.add('autonomous-polish-ready'));", 1)
    INDEX.write_text(text, encoding='utf-8')


def patch_journal():
    text = JOURNAL.read_text(encoding='utf-8')
    if MARKER not in text:
        text = text.replace('</head>', performance_css + '</head>', 1)
    JOURNAL.write_text(text, encoding='utf-8')

patch_index()
patch_journal()
print('Performance cleanup applied idempotently.')
