from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "index.html"
MARKER = 'data-visual-theme="saturated-v1"'

CSS = r'''
<style id="saturated-visual-theme" data-visual-theme="saturated-v1">
  /* Performance-safe visual refresh: richer color, static lighting, no new animation. */
  :root{
    --bg:#07142F;
    --card:#12264D;
    --primary:#79B7FF;
    --accent:#FFB35C;
    --cyan:#63E1FF;
    --text:#F7FAFF;
    --text-dim:#B8C8E4;
    --line:rgba(154,193,255,.24);
    --shadow:0 20px 52px -22px rgba(0,0,0,.62);
    --glass-hl:rgba(255,255,255,.18);
    --glass-hl-soft:rgba(255,255,255,.07);
    --glass-shadow:rgba(0,0,0,.66);
    --glass-tint:var(--primary);
  }
  html[data-theme="dark"]{
    --bg:#07142F; --card:#12264D; --primary:#79B7FF; --accent:#FFB35C;
    --cyan:#63E1FF; --text:#F7FAFF; --text-dim:#B8C8E4; --line:rgba(154,193,255,.24);
    --shadow:0 20px 52px -22px rgba(0,0,0,.66); --glass-hl:rgba(255,255,255,.18);
    --glass-hl-soft:rgba(255,255,255,.07); --glass-shadow:rgba(0,0,0,.66);
  }
  html[data-theme="evening"]{
    --bg:#0C0B2B; --card:#191744; --primary:#B7A4FF; --accent:#FFB96D;
    --cyan:#71E7FF; --text:#FBF9FF; --text-dim:#C2BEDF; --line:rgba(187,169,255,.25);
    --shadow:0 20px 52px -22px rgba(0,0,0,.72); --glass-hl:rgba(255,255,255,.16);
    --glass-hl-soft:rgba(255,255,255,.06); --glass-shadow:rgba(0,0,0,.72);
  }
  html[data-theme="light"]{
    --bg:#F2F6FF; --card:#FFFFFF; --primary:#285FD7; --accent:#D84F86;
    --cyan:#118EBA; --text:#10204A; --text-dim:#5D6D8B; --line:#C9D8F0;
    --shadow:0 20px 50px -24px rgba(32,68,145,.28); --glass-hl:rgba(255,255,255,.72);
    --glass-hl-soft:rgba(255,255,255,.42); --glass-shadow:rgba(35,56,102,.18);
  }
  html[data-theme="morning"]{
    --bg:#FFF5F1; --card:#FFFCFB; --primary:#A73573; --accent:#E98B43;
    --cyan:#2D8FBD; --text:#29172B; --text-dim:#765E6E; --line:#EFD6DC;
    --shadow:0 20px 50px -24px rgba(148,57,89,.22); --glass-hl:rgba(255,255,255,.78);
    --glass-hl-soft:rgba(255,255,255,.45); --glass-shadow:rgba(92,43,62,.16);
  }
  body{
    background:linear-gradient(180deg,var(--bg) 0%,color-mix(in srgb,var(--bg) 72%,#08132E) 100%);
  }
  body::after{
    content:""; position:fixed; inset:0; z-index:1; pointer-events:none;
    background:
      radial-gradient(42% 34% at 12% 8%, color-mix(in srgb,var(--accent) 19%,transparent), transparent 72%),
      radial-gradient(38% 32% at 88% 20%, color-mix(in srgb,var(--cyan) 15%,transparent), transparent 74%),
      linear-gradient(180deg,transparent 0%,color-mix(in srgb,var(--bg) 23%,transparent) 100%);
    opacity:.9;
  }
  .tree-bg{
    background-image:
      linear-gradient(135deg,rgba(7,11,38,.18),rgba(69,22,82,.14) 44%,rgba(7,45,73,.32) 100%),
      url("assets/portfolio-aurora-bg.webp") !important;
    background-color:#07142F !important;
    filter:saturate(1.2) contrast(1.07);
  }
  .tree-bg-scrim{
    background:linear-gradient(180deg,rgba(5,10,28,.10) 0%,rgba(9,15,42,.34) 53%,rgba(3,7,22,.82) 100%) !important;
  }
  html[data-theme="light"] .tree-bg-scrim,
  html[data-theme="morning"] .tree-bg-scrim{
    background:linear-gradient(180deg,rgba(244,248,255,.10) 0%,rgba(237,243,255,.40) 53%,rgba(225,233,249,.84) 100%) !important;
  }
  .bento-card,.journey-studio,.studio-panel,.card,.skill-card{
    border-color:color-mix(in srgb,var(--primary) 25%,var(--line)) !important;
    box-shadow:0 18px 44px -24px var(--glass-shadow),0 1px 0 var(--glass-hl) inset !important;
  }
  .bento-card,.journey-studio{
    background:linear-gradient(145deg,color-mix(in srgb,var(--card) 88%,var(--primary) 12%),color-mix(in srgb,var(--card) 94%,var(--accent) 6%)) !important;
  }
  .studio-panel,.card,.skill-card{
    background:linear-gradient(145deg,color-mix(in srgb,var(--card) 92%,var(--primary) 8%),color-mix(in srgb,var(--card) 96%,var(--accent) 4%)) !important;
  }
  .section-kicker,.studio-kicker,.eyebrow{color:var(--accent) !important;}
  .section h2,.studio-head h2,.hero h1{ text-shadow:0 3px 26px color-mix(in srgb,var(--primary) 24%,transparent); }
  .cta-row a,.cta-row button,.play-journey-btn,.studio-replay a{
    border-color:color-mix(in srgb,var(--accent) 54%,var(--line)) !important;
  }
  .cta-row a.primary,.play-journey-btn{
    background:linear-gradient(135deg,var(--primary),color-mix(in srgb,var(--accent) 48%,var(--primary))) !important;
    color:#08142F !important; box-shadow:0 12px 28px -16px color-mix(in srgb,var(--accent) 70%,transparent) !important;
  }
  @media (max-width:700px){
    body::after{opacity:.58;}
    .tree-bg{filter:saturate(1.08) contrast(1.03);}
    .bento-card,.journey-studio,.studio-panel,.card,.skill-card{box-shadow:0 12px 28px -20px var(--glass-shadow),0 1px 0 var(--glass-hl) inset !important;}
  }
  @media (prefers-reduced-motion:reduce){body::after{opacity:.7;}}
</style>
'''

html = PAGE.read_text()
html = re.sub(r'\s*<style id="saturated-visual-theme"[^>]*>.*?</style>\s*', '\n', html, count=1, flags=re.S)
html = html.replace('</head>', CSS + '\n</head>', 1)
html = html.replace('<meta name="theme-color" content="#FFF1F5" id="theme-color-meta">', '<meta name="theme-color" content="#07142F" id="theme-color-meta">', 1)
PAGE.write_text(html)
print("Applied saturated visual theme to index.html")
