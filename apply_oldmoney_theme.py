from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"

OLD_STYLE_RE = re.compile(r'<style id="saturated-visual-theme"[^>]*>.*?</style>\s*', re.S | re.I)
NEW_STYLE_RE = re.compile(r'<style id="oldmoney-visual-theme"[^>]*>.*?</style>\s*', re.S | re.I)
MOTION_SCRIPT_RE = re.compile(r'<script>\s*/\* OLD_MONEY_MOTION_V1.*?</script>\s*', re.S | re.I)

OLD_MONEY_CSS = r'''<style id="oldmoney-visual-theme" data-visual-theme="oldmoney-v1">
  /* OLD_MONEY_THEME_V1 — white, deep navy, champagne; static, editorial, and restrained. */
  :root{
    --bg:#f7f5ef;
    --card:#ffffff;
    --primary:#0b1d3a;
    --accent:#b89a63;
    --cyan:#71839b;
    --text:#0b1d3a;
    --text-dim:#5b687d;
    --line:rgba(11,29,58,.15);
    --shadow:0 24px 64px -30px rgba(11,29,58,.30);
    --glass-hl:rgba(255,255,255,.92);
    --glass-hl-soft:rgba(255,255,255,.48);
    --glass-shadow:rgba(11,29,58,.22);
    --glass-tint:#0b1d3a;
  }
  html[data-theme="light"],html[data-theme="morning"]{
    --bg:#f7f5ef;--card:#fffdfa;--primary:#0b1d3a;--accent:#b89a63;
    --cyan:#71839b;--text:#0b1d3a;--text-dim:#5b687d;--line:rgba(11,29,58,.15);
    --shadow:0 24px 64px -30px rgba(11,29,58,.30);--glass-hl:rgba(255,255,255,.94);
    --glass-hl-soft:rgba(255,255,255,.52);--glass-shadow:rgba(11,29,58,.20);
  }
  html[data-theme="dark"],html[data-theme="evening"]{
    --bg:#0b1d3a;--card:#132b4d;--primary:#f6f1e7;--accent:#c9ab70;
    --cyan:#9aabc0;--text:#f6f1e7;--text-dim:#c1cad6;--line:rgba(246,241,231,.18);
    --shadow:0 24px 64px -30px rgba(0,0,0,.58);--glass-hl:rgba(255,255,255,.16);
    --glass-hl-soft:rgba(255,255,255,.07);--glass-shadow:rgba(0,0,0,.42);
  }

  body{
    background:linear-gradient(180deg,#fffdfa 0%,#f7f5ef 68%,#edf1f5 100%) !important;
    color:var(--text);
  }
  body::after{
    content:"";position:fixed;inset:0;z-index:1;pointer-events:none;opacity:.56;
    background:
      radial-gradient(36% 28% at 8% 7%,rgba(11,29,58,.06),transparent 72%),
      radial-gradient(30% 26% at 94% 18%,rgba(184,154,99,.08),transparent 74%),
      linear-gradient(180deg,transparent 0%,rgba(11,29,58,.035) 100%);
  }
  html[data-theme="dark"] body,html[data-theme="evening"] body{
    background:linear-gradient(180deg,#0b1d3a 0%,#102746 100%) !important;
  }

  /* Keep the real scenic hero, but grade it into navy rather than neon color. */
  .tree-bg{
    background-image:
      linear-gradient(180deg,rgba(8,22,46,.34),rgba(11,29,58,.58) 52%,rgba(7,17,36,.78)),
      url("assets/portfolio-scenic-blue-hero.webp") !important;
    background-color:#0b1d3a !important;
    filter:saturate(.70) contrast(1.04);
  }
  .tree-bg-scrim{
    background:linear-gradient(180deg,rgba(8,22,46,.08) 0%,rgba(11,29,58,.30) 53%,rgba(7,17,36,.82) 100%) !important;
  }
  html[data-theme="light"] .tree-bg-scrim,html[data-theme="morning"] .tree-bg-scrim{
    background:linear-gradient(180deg,rgba(11,29,58,.04) 0%,rgba(11,29,58,.20) 53%,rgba(7,17,36,.70) 100%) !important;
  }

  .topnav{
    border-color:rgba(255,255,255,.62) !important;
    background:linear-gradient(105deg,rgba(255,255,255,.90),rgba(247,245,239,.72)) !important;
    box-shadow:0 18px 48px rgba(11,29,58,.16),inset 0 1px 0 rgba(255,255,255,.98) !important;
  }
  .topnav .brand,.hero h1,.section h2,.studio-head h2{color:var(--text) !important;}
  .topnav button,.topnav select,.cmdk-trigger-btn,.lang-toggle,.theme-select,.admin-trigger{
    border-color:rgba(11,29,58,.16) !important;background:rgba(255,255,255,.72) !important;color:#0b1d3a !important;
  }
  .hero-glass{
    border-color:rgba(255,255,255,.78) !important;
    background:linear-gradient(135deg,rgba(255,255,255,.90),rgba(247,245,239,.70)) !important;
    box-shadow:0 30px 90px rgba(11,29,58,.20),inset 0 1px 0 rgba(255,255,255,.98) !important;
  }
  .hero-glass::before{
    background:radial-gradient(circle at 82% 20%,rgba(184,154,99,.14),transparent 19%),radial-gradient(circle at 92% 65%,rgba(11,29,58,.08),transparent 29%) !important;
  }
  .hero .eyebrow,.section-kicker,.studio-kicker,.chapter-label{color:#8c6f3f !important;}
  .hero .lede,.section p,.studio-head p{color:var(--text-dim);}
  .btn-primary,.cta-row a.primary,.play-journey-btn{
    background:linear-gradient(135deg,#0b1d3a,#16345b) !important;color:#fffdfa !important;
    border-color:#0b1d3a !important;box-shadow:0 14px 30px -18px rgba(11,29,58,.72) !important;
  }
  .btn-ghost{background:rgba(255,255,255,.68) !important;border-color:rgba(11,29,58,.18) !important;color:#0b1d3a !important;}
  .btn-primary:hover,.cta-row a.primary:hover,.play-journey-btn:hover{box-shadow:0 16px 34px -16px rgba(11,29,58,.68),0 0 0 1px rgba(184,154,99,.45) inset !important;}
  .stat-card,.bento-card,.journey-studio,.studio-panel,.card,.skill-card,.folio,.pursuing-card{
    border-color:rgba(11,29,58,.14) !important;
    box-shadow:0 18px 44px -24px var(--glass-shadow),0 1px 0 var(--glass-hl) inset !important;
  }
  .stat-card,.bento-card,.journey-studio{background:linear-gradient(145deg,rgba(255,255,255,.92),rgba(247,245,239,.78)) !important;}
  .studio-panel,.card,.skill-card,.folio,.pursuing-card{background:rgba(255,255,255,.78) !important;}
  .stat-card .num{color:#0b1d3a !important;-webkit-text-fill-color:#0b1d3a !important;}
  .stat-card .label,.dock-item,.story-rail a{color:#5b687d;}
  .dock{border-color:rgba(255,255,255,.86) !important;background:rgba(255,253,250,.90) !important;box-shadow:0 20px 48px rgba(11,29,58,.20),inset 0 1px 0 #fff !important;}
  .dock-item.dock-active,.dock-item:hover,.story-rail a:hover,.story-rail a.active{color:#8c6f3f !important;}
  .ai-orb{background:linear-gradient(145deg,#fffdfa,#f1eadc) !important;border-color:#b89a63 !important;box-shadow:0 16px 36px rgba(11,29,58,.22),inset 0 1px 0 #fff !important;}
  .ai-orb svg{color:#0b1d3a !important;}.ai-panel{border-color:rgba(11,29,58,.18) !important;background:rgba(255,253,250,.96) !important;box-shadow:0 28px 70px rgba(11,29,58,.22),inset 0 1px 0 #fff !important;}
  .learning-strip,.studio-panel,.studio-list-item,.studio-map-item{border-color:rgba(11,29,58,.12) !important;}
  .learning-strip{background:linear-gradient(135deg,rgba(11,29,58,.045),rgba(184,154,99,.07)) !important;}
  .studio-node{background:rgba(184,154,99,.18) !important;color:#8c6f3f !important;}
  .studio-focus-card{border-left-color:#b89a63 !important;background:rgba(184,154,99,.07) !important;}
  .studio-progress-fill{background:linear-gradient(90deg,#0b1d3a,#b89a63) !important;}

  /* Lightweight premium motion: reveal, press, hover depth. No loops, filters, or scroll-time work. */
  .oldmoney-motion-ready .oldmoney-reveal{opacity:0;transform:translate3d(0,18px,0) scale(.992);}
  .oldmoney-motion-ready .oldmoney-reveal.oldmoney-visible{opacity:1;transform:none;}
  .oldmoney-reveal{transition:opacity .46s cubic-bezier(.23,1,.32,1),transform .46s cubic-bezier(.16,1.12,.3,1) !important;transition-delay:var(--oldmoney-delay,0ms);}
  :where(.btn-primary,.btn-ghost,.play-journey-btn,.studio-replay a,.dock-item,.topnav button,.topnav select){transition:transform .16s cubic-bezier(.16,1.12,.3,1),box-shadow .24s cubic-bezier(.23,1,.32,1),background-color .22s ease,border-color .22s ease !important;}
  :where(.btn-primary,.btn-ghost,.play-journey-btn,.studio-replay a,.dock-item,.topnav button,.topnav select):active{transform:scale(.965) translateY(1px) !important;}
  @media (hover:hover) and (pointer:fine){
    .oldmoney-depth{transition:transform .30s cubic-bezier(.16,1.12,.3,1),box-shadow .30s cubic-bezier(.23,1,.32,1),border-color .22s ease !important;}
    .oldmoney-depth:hover{transform:translate3d(0,-4px,0) !important;box-shadow:0 24px 54px -28px rgba(11,29,58,.34),0 1px 0 rgba(255,255,255,.95) inset !important;border-color:rgba(184,154,99,.42) !important;}
  }
  @media (max-width:760px), (pointer:coarse){
    /* Mobile keeps native touch scrolling and only uses short opacity/transform reveals. */
    .oldmoney-motion-ready .oldmoney-reveal{transform:translate3d(0,10px,0) scale(.997);}
    .oldmoney-reveal{transition-duration:.34s !important;transition-delay:0ms !important;}
    .oldmoney-depth{transition:none !important;}
    body::after{opacity:.42;}
  }
  @media (prefers-reduced-motion:reduce){
    .oldmoney-motion-ready .oldmoney-reveal,.oldmoney-motion-ready .oldmoney-reveal.oldmoney-visible{opacity:1;transform:none;}
    .oldmoney-reveal,:where(.btn-primary,.btn-ghost,.play-journey-btn,.studio-replay a,.dock-item,.topnav button,.topnav select){transition:none !important;}
  }
</style>
<script>
/* OLD_MONEY_MOTION_V1 — a small observer for deliberate entrance motion. */
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
      el.style.setProperty('--oldmoney-delay', `${Math.min(i, 4) * 42}ms`);
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
    setTimeout(() => targets.forEach(el => el.classList.add('oldmoney-visible')), 1200);
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, {once:true});
  else init();
})();
</script>
'''


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
        text = re.sub(r'(<meta\s+name=["\']theme-color["\']\s+content=["\'])#[0-9A-Fa-f]{6}(["\'])', r'\g<1>#0b1d3a\2', text, count=1)
    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


if __name__ == "__main__":
    changed = migrate(INDEX)
    print(f"updated {INDEX.name}: {changed}")
