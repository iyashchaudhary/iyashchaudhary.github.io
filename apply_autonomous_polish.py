from pathlib import Path

ROOT = Path(__file__).resolve().parent
CSS_MARKER = "autonomous-polish-css-v1"
RUNTIME_MARKER = "autonomous-polish-runtime-v1"

INDEX_CSS = """/* autonomous-polish-css-v1 */
:root { --autonomous-spring: cubic-bezier(.22,1,.36,1); --autonomous-focus: rgba(137,190,255,.96); }
html { scroll-padding-top: max(5rem, calc(4rem + env(safe-area-inset-top))); text-rendering: optimizeLegibility; -webkit-font-smoothing: antialiased; }
body { overflow-x: clip; }
:where(h1,h2,h3,h4,.hero-bigtext,.story-kicker,.studio-kicker) { text-wrap: balance; }
:where(button,a,input,textarea,select) { -webkit-tap-highlight-color: transparent; }
:where(button,a,input,textarea,select,.bento-card,.glass-card,.studio-map-item,.studio-focus-card,.skill-card,.story-rail a,.dock-item):focus-visible { outline: 2px solid var(--autonomous-focus); outline-offset: 4px; }
:where(button,.dock-item,.story-rail a,.play-journey-btn):active { transform: scale(.97); }
@media (hover:hover) and (pointer:fine) { :where(.bento-card,.glass-card,.studio-map-item,.studio-focus-card,.skill-card):hover { transform: translateY(-3px); } :where(.dock-item,.story-rail a,.play-journey-btn):hover { transform: translateY(-2px); } }
.hero-heading,.hero-bigtext { max-width: 100%; overflow-wrap: anywhere; }
.journey-studio { grid-column: 1 / -1; width: 100%; min-width: 0; }
@media (max-width:760px) { html { scroll-padding-top: max(4.5rem, calc(3.75rem + env(safe-area-inset-top))); } body { -webkit-overflow-scrolling: touch; overscroll-behavior-x: none; } .journey-studio,.studio-grid,.studio-map,.studio-focus,.studio-bottom { width:100%; min-width:0; max-width:100%; } .studio-grid { grid-template-columns:minmax(0,1fr)!important; } .hero-heading,.hero-bigtext { font-size:clamp(2.25rem,13vw,4.8rem); line-height:.98; letter-spacing:-.045em; } .dock-wrap { padding-bottom:max(.55rem,env(safe-area-inset-bottom)); } }
@media (prefers-reduced-motion:reduce) { :where(*,*::before,*::after) { scroll-behavior:auto!important; animation-duration:.001ms!important; animation-iteration-count:1!important; transition-duration:.001ms!important; } }
"""

JOURNAL_CSS = """/* autonomous-polish-css-v1 */
:root { --autonomous-focus: rgba(255,214,232,.98); }
html { scroll-padding-top:max(4rem,calc(3.5rem + env(safe-area-inset-top))); text-rendering:optimizeLegibility; -webkit-font-smoothing:antialiased; }
body { overflow-x:clip; -webkit-overflow-scrolling:touch; overscroll-behavior-x:none; }
:where(h1,h2,h3,h4,.day-num,.entry-title,.section-title) { text-wrap:balance; }
:where(button,a,input,textarea,select) { -webkit-tap-highlight-color:transparent; }
:where(button,a,input,textarea,select,.media-card,.lt-card,.random-note,.day-chip):focus-visible { outline:2px solid var(--autonomous-focus); outline-offset:3px; }
:where(.media-card img,.entry-thumbnail img,.random-note img) { display:block; max-width:100%; height:auto; }
@media (max-width:760px) { :where(.media-collage,.media-board,.lt-grid,.random-grid) { min-width:0; max-width:100%; } .entry-thumbnail { max-width:100%; overflow:hidden; } }
@media (prefers-reduced-motion:reduce) { :where(*,*::before,*::after) { scroll-behavior:auto!important; animation-duration:.001ms!important; animation-iteration-count:1!important; transition-duration:.001ms!important; } }
"""

ADMIN_CSS = """/* autonomous-polish-css-v1 */
html { scroll-padding-top:max(1.5rem,env(safe-area-inset-top)); text-rendering:optimizeLegibility; -webkit-font-smoothing:antialiased; }
body { overflow-x:clip; }
:where(button,a,input,textarea,select):focus-visible { outline:2px solid #7db7ff; outline-offset:3px; }
@media (max-width:760px) { body { -webkit-overflow-scrolling:touch; overscroll-behavior-x:none; } :where(input,textarea,select,button) { font-size:16px; } }
"""

RUNTIME = """<script>/* autonomous-polish-runtime-v1 */
(() => {
  const root = document.documentElement;
  root.dataset.autonomousPolish = 'ready';
  Array.from(document.images).forEach((img, index) => { if (!img.decoding) img.decoding = 'async'; if (index > 2 && !img.loading) img.loading = 'lazy'; });
  const chapters = Array.from(document.querySelectorAll('section[id],.journey-studio[id]'));
  const links = Array.from(document.querySelectorAll('.story-rail a[href^="#"]'));
  if ('IntersectionObserver' in window && chapters.length) {
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter(e => e.isIntersecting).sort((a,b) => b.intersectionRatio-a.intersectionRatio)[0];
      if (!visible) return;
      root.dataset.activeChapter = visible.target.id;
      links.forEach(link => { const active = link.getAttribute('href') === `#${visible.target.id}`; if (active) link.setAttribute('aria-current','location'); else link.removeAttribute('aria-current'); });
    }, { rootMargin:'-18% 0px -58% 0px', threshold:[0,.2,.55] });
    chapters.forEach(chapter => observer.observe(chapter));
  }
  requestAnimationFrame(() => root.classList.add('autonomous-polish-ready'));
})();
</script>"""


def add_once(text, close, payload, marker):
    if marker in text:
        return text
    pos = text.rfind(close)
    if pos < 0:
        raise ValueError(f'Missing {close}')
    return text[:pos] + '\n' + payload.strip() + '\n' + text[pos:]


def patch(path, css, runtime=False):
    text = path.read_text(encoding='utf-8')
    text = add_once(text, '</style>', css, CSS_MARKER)
    if runtime:
        text = add_once(text, '</body>', RUNTIME, RUNTIME_MARKER)
    path.write_text(text, encoding='utf-8')

patch(ROOT/'index.html', INDEX_CSS, True)
patch(ROOT/'unfiltered.html', JOURNAL_CSS, True)
patch(ROOT/'admin.html', ADMIN_CSS, False)
print('Applied autonomous polish layer.')
# end
