from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"

OLD_STYLE_RE = re.compile(r'<style id="saturated-visual-theme"[^>]*>.*?</style>\s*', re.S | re.I)
NEW_STYLE_RE = re.compile(r'<style id="oldmoney-visual-theme"[^>]*>.*?</style>\s*', re.S | re.I)
MOTION_SCRIPT_RE = re.compile(r'<script>\s*/\* OLD_MONEY_MOTION_V[12].*?</script>\s*', re.S | re.I)

OLD_MONEY_CSS = r"""<style id="oldmoney-visual-theme" data-visual-theme="oldmoney-v2">
  /* OLD_MONEY_THEME_V2 — clean white, ink navy, restrained brass. */
  :root{
    --bg:#f8f8f5;--card:#ffffff;--primary:#071a33;--accent:#ad8b55;
    --cyan:#60748e;--text:#071a33;--text-dim:#506078;--line:rgba(7,26,51,.16);
    --shadow:0 24px 56px -30px rgba(7,26,51,.28);--glass-hl:#ffffff;
    --glass-hl-soft:rgba(255,255,255,.72);--glass-shadow:rgba(7,26,51,.20);
    --glass-tint:#071a33;
  }
  html[data-theme="light"],html[data-theme="morning"]{
    --bg:#f8f8f5;--card:#ffffff;--primary:#071a33;--accent:#ad8b55;
    --cyan:#60748e;--text:#071a33;--text-dim:#506078;--line:rgba(7,26,51,.16);
    --shadow:0 24px 56px -30px rgba(7,26,51,.28);--glass-hl:#ffffff;
    --glass-hl-soft:rgba(255,255,255,.72);--glass-shadow:rgba(7,26,51,.20);
  }
  html[data-theme="dark"],html[data-theme="evening"]{
    --bg:#071a33;--card:#0d2749;--primary:#fffdf7;--accent:#c4a56e;
    --cyan:#aab8c9;--text:#fffdf7;--text-dim:#c4cfdb;--line:rgba(255,253,247,.18);
    --shadow:0 24px 56px -30px rgba(0,0,0,.58);--glass-hl:rgba(255,255,255,.13);
    --glass-hl-soft:rgba(255,255,255,.06);--glass-shadow:rgba(0,0,0,.40);
  }

  body{background:#f8f8f5 !important;color:var(--text);}
  body::after{content:none !important;background:none !important;opacity:0 !important;}
  html[data-theme="dark"] body,html[data-theme="evening"] body{background:#071a33 !important;}

  /* The real hero image stays, but becomes a quiet navy editorial texture. */
  .tree-bg{
    background-image:linear-gradient(180deg,rgba(7,26,51,.82),rgba(7,26,51,.90) 60%,rgba(4,15,31,.96)),url("assets/portfolio-scenic-blue-hero.webp") !important;
    background-color:#071a33 !important;filter:grayscale(.82) saturate(.32) contrast(1.08);
  }
  .tree-bg-scrim{background:linear-gradient(180deg,rgba(7,26,51,.10),rgba(7,26,51,.52) 64%,rgba(4,15,31,.92)) !important;}
  html[data-theme="light"] .tree-bg-scrim,html[data-theme="morning"] .tree-bg-scrim{background:linear-gradient(180deg,rgba(7,26,51,.08),rgba(7,26,51,.44) 64%,rgba(4,15,31,.88)) !important;}

  .topnav{border:1px solid rgba(7,26,51,.16) !important;background:#ffffff !important;box-shadow:0 14px 34px -24px rgba(7,26,51,.42),0 1px 0 #fff inset !important;}
  .topnav .brand,.hero h1,.section h2,.studio-head h2{color:var(--text) !important;}
  .topnav button,.topnav select,.cmdk-trigger-btn,.lang-toggle,.theme-select,.admin-trigger{border-color:rgba(7,26,51,.18) !important;background:#ffffff !important;color:#071a33 !important;}
  .hero-glass{border:1px solid rgba(7,26,51,.18) !important;background:#ffffff !important;box-shadow:0 32px 72px -30px rgba(7,26,51,.42),0 1px 0 #fff inset !important;}
  .hero-glass::before{background:linear-gradient(110deg,transparent 0%,rgba(255,255,255,.72) 42%,transparent 72%) !important;opacity:.22 !important;}
  .hero .eyebrow,.section-kicker,.studio-kicker,.chapter-label{color:#8b6b35 !important;}
  .hero .lede,.section p,.studio-head p{color:var(--text-dim);}
  .btn-primary,.cta-row a.primary,.play-journey-btn{background:#071a33 !important;color:#ffffff !important;border-color:#071a33 !important;box-shadow:0 14px 28px -18px rgba(7,26,51,.78) !important;}
  .btn-ghost{background:#ffffff !important;border-color:rgba(7,26,51,.22) !important;color:#071a33 !important;}
  .btn-primary:hover,.cta-row a.primary:hover,.play-journey-btn:hover{background:#102d50 !important;box-shadow:0 18px 34px -18px rgba(7,26,51,.72),0 0 0 1px rgba(173,139,85,.48) inset !important;}

  .stat-card,.bento-card,.journey-studio,.studio-panel,.card,.skill-card,.folio,.pursuing-card{border-color:rgba(7,26,51,.16) !important;background:#ffffff !important;box-shadow:0 18px 44px -26px var(--glass-shadow),0 1px 0 #fff inset !important;}
  .stat-card .num{color:#071a33 !important;-webkit-text-fill-color:#071a33 !important;}
  .stat-card .label,.dock-item,.story-rail a{color:#506078;}
  .dock{border-color:rgba(7,26,51,.16) !important;background:#ffffff !important;box-shadow:0 20px 44px -22px rgba(7,26,51,.34),0 1px 0 #fff inset !important;}
  .dock-item.dock-active,.dock-item:hover,.story-rail a:hover,.story-rail a.active{color:#8b6b35 !important;}
  .ai-orb{background:#071a33 !important;border-color:#071a33 !important;box-shadow:0 16px 34px -16px rgba(7,26,51,.62),0 0 0 2px rgba(173,139,85,.68) inset !important;}
  .ai-orb svg{color:#ffffff !important;}.ai-panel{border-color:rgba(7,26,51,.18) !important;background:#ffffff !important;box-shadow:0 28px 62px -24px rgba(7,26,51,.36),0 1px 0 #fff inset !important;}
  .learning-strip,.studio-panel,.studio-list-item,.studio-map-item{border-color:rgba(7,26,51,.14) !important;}
  .learning-strip{background:#f4f1e9 !important;}
  .studio-node{background:#071a33 !important;color:#ffffff !important;}
  .studio-focus-card{border-left-color:#ad8b55 !important;background:#f4f1e9 !important;}
  .studio-progress-fill{background:#071a33 !important;}

  /* Apple-inspired motion: depth is deliberate on desktop and compact on touch devices. */
  .hero-glass,.journey-studio,.section.bento-card,.folio,.skill-card,.pursuing-card{transform-style:preserve-3d;}
  .oldmoney-motion-ready .oldmoney-reveal{opacity:0;transform:translate3d(0,26px,0) scale(.975) rotateX(1.2deg);}
  .oldmoney-motion-ready .oldmoney-reveal.oldmoney-visible{opacity:1;transform:none;}
  .oldmoney-reveal{transition:opacity .56s cubic-bezier(.23,1,.32,1),transform .56s cubic-bezier(.16,1.12,.3,1) !important;transition-delay:var(--oldmoney-delay,0ms);}
  :where(.btn-primary,.btn-ghost,.play-journey-btn,.studio-replay a,.dock-item,.topnav button,.topnav select){transition:transform .16s cubic-bezier(.16,1.12,.3,1),box-shadow .24s cubic-bezier(.23,1,.32,1),background-color .22s ease,border-color .22s ease !important;}
  :where(.btn-primary,.btn-ghost,.play-journey-btn,.studio-replay a,.dock-item,.topnav button,.topnav select):active{transform:scale(.965) translateY(1px) !important;}
  @media (hover:hover) and (pointer:fine){
    .oldmoney-depth{will-change:transform;transition:transform .32s cubic-bezier(.16,1.12,.3,1),box-shadow .32s cubic-bezier(.23,1,.32,1),border-color .22s ease !important;}
    .oldmoney-depth:hover{transform:perspective(1100px) translate3d(0,-8px,0) rotateX(1deg) rotateY(.35deg) !important;box-shadow:0 28px 58px -28px rgba(7,26,51,.38),0 1px 0 #fff inset !important;border-color:rgba(173,139,85,.48) !important;}
    .hero-glass.oldmoney-depth:hover{transform:perspective(1400px) translate3d(0,-5px,0) rotateX(.5deg) !important;}
    .oldmoney-tilt{--tilt-x:0deg;--tilt-y:0deg;}
    .oldmoney-motion-ready .hero-glass.oldmoney-tilt{transform:perspective(1400px) rotateX(var(--tilt-x)) rotateY(var(--tilt-y)) !important;}
    .oldmoney-motion-ready .hero-glass.oldmoney-tilt.oldmoney-visible{transform:perspective(1400px) rotateX(var(--tilt-x)) rotateY(var(--tilt-y)) !important;}
  }
  @media (max-width:760px), (pointer:coarse){
    .oldmoney-motion-ready .oldmoney-reveal{transform:translate3d(0,10px,0) scale(.995);}
    .oldmoney-reveal{transition-duration:.32s !important;transition-delay:0ms !important;}
    .oldmoney-depth{will-change:auto;transform-style:flat;transition:none !important;}
    .oldmoney-tilt,.oldmoney-motion-ready .hero-glass.oldmoney-tilt,.oldmoney-motion-ready .hero-glass.oldmoney-tilt.oldmoney-visible{transform:none !important;}
    body::after{display:none !important;}
  }
  @media (prefers-reduced-motion:reduce){
    .oldmoney-motion-ready .oldmoney-reveal,.oldmoney-motion-ready .oldmoney-reveal.oldmoney-visible{opacity:1;transform:none;}
    .oldmoney-reveal,:where(.btn-primary,.btn-ghost,.play-journey-btn,.studio-replay a,.dock-item,.topnav button,.topnav select){transition:none !important;}
  }
</style>
<script>
/* OLD_MONEY_MOTION_V2 — DOM-ready observer for deliberate entrance motion. */
(() => {
  const init = () => {
    const root = document.documentElement;
    const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const compact = window.matchMedia && window.matchMedia('(max-width:760px), (pointer:coarse)').matches;
    const selector = compact
      ? '.hero-glass,.journey-studio,.section.bento-card'
      : '.hero-glass,.journey-studio,.journey-studio .studio-panel,.section.bento-card,.folio,.skill-card,.pursuing-card';
    const targets = [...document.querySelectorAll(selector)];
    if (!targets.length) return;
    targets.forEach((el, i) => {
      el.classList.add('oldmoney-reveal','oldmoney-depth');
      el.style.setProperty('--oldmoney-delay', `${Math.min(i, 5) * 48}ms`);
    });
    if (reduce || !('IntersectionObserver' in window)) {
      targets.forEach(el => el.classList.add('oldmoney-visible'));
      return;
    }
    root.classList.add('oldmoney-motion-ready');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('oldmoney-visible');
        observer.unobserve(entry.target);
      });
    }, {threshold: compact ? .08 : .14, rootMargin: '0px 0px -7% 0px'});
    targets.forEach(el => observer.observe(el));
    setTimeout(() => targets.forEach(el => el.classList.add('oldmoney-visible')), 1400);

    const finePointer = window.matchMedia && window.matchMedia('(hover:hover) and (pointer:fine)').matches;
    if (!reduce && finePointer) {
      const hero = document.querySelector('.hero-glass');
      if (hero) {
        hero.classList.add('oldmoney-tilt');
        let frame = 0;
        let nextX = 0;
        let nextY = 0;
        const render = () => {
          frame = 0;
          hero.style.setProperty('--tilt-x', `${nextX.toFixed(2)}deg`);
          hero.style.setProperty('--tilt-y', `${nextY.toFixed(2)}deg`);
        };
        hero.addEventListener('pointermove', (event) => {
          const rect = hero.getBoundingClientRect();
          const px = (event.clientX - rect.left) / rect.width - .5;
          const py = (event.clientY - rect.top) / rect.height - .5;
          nextX = py * -2.2;
          nextY = px * 2.8;
          if (!frame) frame = requestAnimationFrame(render);
        }, {passive:true});
        hero.addEventListener('pointerleave', () => {
          nextX = 0; nextY = 0;
          if (!frame) frame = requestAnimationFrame(render);
        }, {passive:true});
      }
    }
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, {once:true});
  else init();
})();
</script>
"""


def migrate(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = OLD_STYLE_RE.sub("", text)
    text = NEW_STYLE_RE.sub("", text)
    text = MOTION_SCRIPT_RE.sub("", text)
    if "</head>" not in text:
        raise RuntimeError(f"Missing </head> in {path}")
    text = text.replace("</head>", OLD_MONEY_CSS + "\n</head>", 1)
    if path.name == "index.html":
        text = re.sub(r'(<meta\s+name=["\']theme-color["\']\s+content=["\'])#[0-9A-Fa-f]{6}(["\'])', r'\g<1>#071a33\2', text, count=1)
        text = re.sub(r"const THEME_COLORS = \{[^}]+\};", "const THEME_COLORS = { morning:'#F8F8F5', light:'#F8F8F5', evening:'#071A33', dark:'#071A33' };", text, count=1)
    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


if __name__ == "__main__":
    changed = migrate(INDEX)
    print(f"updated {INDEX.name}: {changed}")
