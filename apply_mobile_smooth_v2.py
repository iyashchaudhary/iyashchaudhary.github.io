from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / 'index.html'
text = INDEX.read_text(encoding='utf-8')
original = text

# Use the existing optimized delivery asset without changing the visual composition.
text = text.replace('portfolio-scenic-blue-hero.jpg', 'portfolio-scenic-blue-hero.webp')

# Stop expensive touch-device visual work at its runtime source.
text = text.replace(
    "    if(prefersReducedGlobal) return;\n    const scenes = Array.from(document.querySelectorAll('.scene'));",
    "    if(prefersReducedGlobal || window.matchMedia('(pointer:coarse)').matches || window.innerWidth < 760) return;\n    const scenes = Array.from(document.querySelectorAll('.scene'));",
    1,
)
text = text.replace(
    "    const beams = document.querySelectorAll('.light-beam[data-target]');\n    if(!beams.length) return;",
    "    const beams = document.querySelectorAll('.light-beam[data-target]');\n    if(!beams.length || window.matchMedia('(pointer:coarse)').matches || window.innerWidth < 760) return;",
    1,
)
text = text.replace(
    "  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;\n  const count = window.innerWidth < 720 ? 10 : 18;",
    "  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;\n  if(window.matchMedia('(pointer:coarse)').matches || window.innerWidth < 720) return;\n  const count = 18;",
    1,
)
text = text.replace(
    "  const field = document.getElementById('petal-field');\n  if(!field) return;\n  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;\n  const PETAL_IMAGES",
    "  const field = document.getElementById('petal-field');\n  if(!field || window.matchMedia('(pointer:coarse)').matches || window.innerWidth < 720) return;\n  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;\n  const PETAL_IMAGES",
    1,
)
# Story progress remains useful, but mobile does not need a scroll-linked depth pipeline.
text = text.replace(
    "    const root = document.documentElement;\n    const update = () => {",
    "    const root = document.documentElement;\n    const lite = window.matchMedia('(pointer:coarse)').matches || window.innerWidth < 760;\n    const update = () => {",
    1,
)
text = text.replace(
    "      if (!reduce && window.innerWidth > 600) document.querySelectorAll('[data-story-depth]').forEach(el => {",
    "      if (!reduce && !lite && window.innerWidth > 600) document.querySelectorAll('[data-story-depth]').forEach(el => {",
    1,
)
text = text.replace(
    "    window.addEventListener('scroll', () => { if (!ticking) { window.requestAnimationFrame(() => { update(); ticking = false; }); ticking = true; } }, {passive:true});",
    "    if(!lite) window.addEventListener('scroll', () => { if (!ticking) { window.requestAnimationFrame(() => { update(); ticking = false; }); ticking = true; } }, {passive:true});",
    1,
)

# Add one final, low-cost mobile layer after all historical style blocks.
mobile_css = '''<style id="mobile-smooth-v2">
  @media (max-width:760px), (pointer:coarse){
    html{scroll-behavior:auto!important;overscroll-behavior-y:auto!important;}
    body{touch-action:pan-y!important;overscroll-behavior-y:auto!important;-webkit-overflow-scrolling:touch!important;}
    #particle-universe,#mesh-bg,#light-engine,#cursor-glow,#fireflies,#petal-field{display:none!important;}
    #tree-bg{animation:none!important;background-attachment:scroll!important;will-change:auto!important;}
    #tree-bg::after,.tree-bg-glow,.tree-bg-glow-2{display:none!important;animation:none!important;will-change:auto!important;}
    .hero-glass,.glass-card,.section.bento-card,.topnav,.dock,.folio,.skill-card,.pursuing-card,.ai-panel{backdrop-filter:none!important;-webkit-backdrop-filter:none!important;}
    html[data-theme="light"] .hero-glass,html[data-theme="light"] .section.bento-card,html[data-theme="light"] .topnav,html[data-theme="light"] .dock{background:rgba(247,251,255,.94)!important;}
    html[data-theme="dark"] .hero-glass,html[data-theme="dark"] .section.bento-card,html[data-theme="dark"] .topnav,html[data-theme="dark"] .dock{background:rgba(10,20,36,.94)!important;}
    #hello .hero-glass{opacity:1!important;transform:none!important;}
    .apple-reveal{will-change:auto!important;transition:opacity .36s var(--apple-ease),transform .36s var(--apple-spring)!important;}
    .apple-float{will-change:auto!important;}
    :where(img){content-visibility:auto;}
  }
  @media (prefers-reduced-motion:reduce){.apple-reveal{opacity:1!important;transform:none!important;transition:none!important;}}
</style>
'''
if 'id="mobile-smooth-v2"' not in text:
    text = text.replace('</head>', mobile_css + '</head>', 1)

if text == original:
    print('no changes needed')
else:
    INDEX.write_text(text, encoding='utf-8')
    print('updated index.html')
print('mobile_smooth_v2:', 'id="mobile-smooth-v2"' in text)
print('scene_touch_guard:', "window.matchMedia('(pointer:coarse)').matches || window.innerWidth < 760" in text)
print('decor_touch_guard:', "window.matchMedia('(pointer:coarse)').matches || window.innerWidth < 720" in text)
