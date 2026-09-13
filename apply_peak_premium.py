from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "index.html"
STYLE_START = "<!-- PEAK_PREMIUM_V1_START -->"
STYLE_END = "<!-- PEAK_PREMIUM_V1_END -->"
SCRIPT_START = "<!-- PEAK_PREMIUM_RUNTIME_V1_START -->"
SCRIPT_END = "<!-- PEAK_PREMIUM_RUNTIME_V1_END -->"

STYLE = r'''<!-- PEAK_PREMIUM_V1_START -->
<style id="peak-premium-v1">
:root{--peak-mx:50%;--peak-my:35%;}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;opacity:0;background:radial-gradient(34rem 24rem at var(--peak-mx) var(--peak-my),rgba(255,255,255,.16),transparent 68%);mix-blend-mode:screen;transition:opacity .35s ease}
.hero-glass,.section.bento-card,.folio,.skill-card,.pursuing-card{transform-style:preserve-3d}
.peak-tilt{--peak-card-x:0deg;--peak-card-y:0deg;--peak-sheen:0;transition:transform .42s cubic-bezier(.16,1.22,.3,1),box-shadow .42s cubic-bezier(.22,1,.36,1)}
.peak-tilt::before{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;opacity:var(--peak-sheen);background:radial-gradient(18rem 14rem at var(--peak-light-x,50%) var(--peak-light-y,28%),rgba(255,255,255,.2),transparent 70%);transition:opacity .3s ease}
@media (hover:hover) and (pointer:fine){
.peak-tilt:hover{transform:perspective(1100px) rotateX(var(--peak-card-y)) rotateY(var(--peak-card-x)) translateY(-6px) scale(1.006);box-shadow:0 28px 70px -34px rgba(8,24,58,.58),0 1px 0 rgba(255,255,255,.7) inset}
.peak-magnetic{transition:transform .36s cubic-bezier(.16,1.22,.3,1),box-shadow .28s ease;will-change:transform}
.peak-magnetic:hover{transform:translateY(-2px) scale(1.015);box-shadow:0 16px 34px -22px rgba(12,42,92,.7)}
}
html[data-theme="dark"] body::after{background:radial-gradient(34rem 24rem at var(--peak-mx) var(--peak-my),rgba(157,194,255,.11),transparent 70%)}
html[data-theme="dark"] .peak-tilt:hover{box-shadow:0 28px 70px -34px rgba(0,0,0,.9),0 1px 0 rgba(255,255,255,.1) inset}
@media (max-width:760px),(pointer:coarse){body::after{display:none!important}.peak-tilt{transform:none!important;transition:box-shadow .25s ease}.peak-tilt::before{display:none}.peak-magnetic{transform:none!important;will-change:auto}}
@media (prefers-reduced-motion:reduce){body::after{display:none}.peak-tilt,.peak-magnetic{transform:none!important;transition:none!important}.peak-tilt::before{display:none}}
</style>
<!-- PEAK_PREMIUM_V1_END -->'''

SCRIPT = r'''<!-- PEAK_PREMIUM_RUNTIME_V1_START -->
<script id="peak-premium-runtime-v1">
(() => {
  const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  const desktop = window.matchMedia?.('(hover: hover) and (pointer: fine)').matches && window.innerWidth > 760;
  const cards = [...document.querySelectorAll('.hero-glass,.section.bento-card,.folio,.skill-card,.pursuing-card')];
  cards.forEach(card => card.classList.add('peak-tilt'));
  document.querySelectorAll('.btn-primary,.btn-ghost,.dock-item,.topnav button,.play-journey-btn').forEach(el => el.classList.add('peak-magnetic'));
  if (reduce || !desktop) return;
  let raf = 0;
  let pointerX = 0;
  let pointerY = 0;
  let active = null;
  const paint = () => {
    raf = 0;
    document.documentElement.style.setProperty('--peak-mx', `${pointerX}px`);
    document.documentElement.style.setProperty('--peak-my', `${pointerY}px`);
    if (!active) return;
    const box = active.getBoundingClientRect();
    const nx = Math.max(-1, Math.min(1, (pointerX - (box.left + box.width / 2)) / Math.max(1, box.width / 2)));
    const ny = Math.max(-1, Math.min(1, (pointerY - (box.top + box.height / 2)) / Math.max(1, box.height / 2)));
    active.style.setProperty('--peak-card-x', `${(nx * 3).toFixed(2)}deg`);
    active.style.setProperty('--peak-card-y', `${(-ny * 3).toFixed(2)}deg`);
    active.style.setProperty('--peak-light-x', `${((nx + 1) * 50).toFixed(1)}%`);
    active.style.setProperty('--peak-light-y', `${((ny + 1) * 50).toFixed(1)}%`);
    active.style.setProperty('--peak-sheen', '.72');
    document.documentElement.style.setProperty('--peak-sheen', '.7');
  };
  document.addEventListener('pointermove', event => {
    pointerX = event.clientX;
    pointerY = event.clientY;
    const next = event.target.closest?.('.peak-tilt');
    if (active && active !== next) {
      active.style.setProperty('--peak-sheen', '0');
      active.style.setProperty('--peak-card-x', '0deg');
      active.style.setProperty('--peak-card-y', '0deg');
    }
    active = next;
    if (!raf) raf = requestAnimationFrame(paint);
  }, {passive:true});
  document.addEventListener('pointerleave', () => {
    if (active) active.style.setProperty('--peak-sheen', '0');
    active = null;
    document.documentElement.style.setProperty('--peak-sheen', '0');
  }, {passive:true});
  const hero = document.querySelector('.hero-glass');
  if (hero) hero.dataset.peakStage = 'active';
})();
</script>
<!-- PEAK_PREMIUM_RUNTIME_V1_END -->'''

def remove_block(text, start, end):
    while start in text and end in text:
        begin = text.index(start)
        finish = text.index(end, begin) + len(end)
        text = text[:begin].rstrip() + "\n" + text[finish:].lstrip()
    return text

html = TARGET.read_text(encoding="utf-8")
html = remove_block(html, STYLE_START, STYLE_END)
html = remove_block(html, SCRIPT_START, SCRIPT_END)
html = html.replace("</head>", STYLE + "\n</head>", 1)
html = html.replace("</body>", SCRIPT + "\n</body>", 1)
TARGET.write_text(html, encoding="utf-8")
if html.count(STYLE_START) != 1 or html.count(STYLE_END) != 1 or html.count(SCRIPT_START) != 1 or html.count(SCRIPT_END) != 1:
    raise SystemExit("Premium markers are missing or duplicated")
print("Applied canonical peak-premium layer")
