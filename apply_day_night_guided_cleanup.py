from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / 'index.html'
text = INDEX.read_text(encoding='utf-8')
original = text

# Remove the complete Guided Starting Point section up to the real Journey section.
start_marker = '<section class="journey-studio scene" id="journey-studio"'
end_marker = '<section class="section bento-card bento-span-7 scene" id="journey"'
if start_marker in text and end_marker in text:
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    text = text[:start] + text[end:]

# Remove the studio renderer and its dedicated CSS only.
text = re.sub(r'\s*<script>\s*/\* PREMIUM_JOURNEY_STUDIO_SCRIPT_V1 \*/.*?</script>\s*', '\n', text, flags=re.S | re.I)
text = re.sub(r'\s*<style>\s*/\* PREMIUM_JOURNEY_STUDIO_V1 \*/.*?</style>\s*', '\n', text, flags=re.S | re.I)

# Clean studio-only selectors from shared styles while preserving real cards and motion.
for old, new in {
    ',.journey-studio .studio-panel': '',
    ',.journey-studio': '',
    ',.studio-panel': '',
    ',.studio-replay a': '',
    ',.studio-kicker': '',
    ',.journey-studio[id]': '',
    ',.studio-head h2': '',
    ',.studio-head p': '',
    ',.studio-map-item': '',
    ',.studio-focus-card': '',
    ',.studio-list-item': '',
    ',.studio-head': '',
}.items():
    text = text.replace(old, new)
text = text.replace('section[id],.journey-studio[id]', 'section[id]')
for old, new in {'.studio-head h2,':'', '.studio-head p,':'', '.studio-head h2':'', '.studio-head p':''}.items():
    text = text.replace(old, new)

# Remove the remaining standalone studio-only declarations if present.
text = re.sub(r'\n\s*\.studio-(?:node|focus-card|progress-fill|map-item|list-item|replay|kicker)[^{]*\{[^}]*\}', '', text, flags=re.S)

# Remove the last standalone layout fragments that only served the deleted studio.
text = re.sub(r'\n\s*\.journey-studio \{ grid-column: 1 / -1; width: 100%; min-width: 0; \}\n', '\n', text)
text = re.sub(r'\n\s*@media \(max-width:760px\) \{ html \{ scroll-padding-top: max\(4\.5rem, calc\(3\.75rem \+ env\(safe-area-inset-top\)\)\); \} body \{ -webkit-overflow-scrolling: touch; overscroll-behavior-x: none; \} \.journey-studio,\.studio-grid,\.studio-map,\.studio-focus,\.studio-bottom \{ width:100%; min-width:0; max-width:100%; \} \.studio-grid \{ grid-template-columns:minmax\(0,1fr\)!important; \} \.hero-heading,.hero-bigtext \{ font-size:clamp\(2\.25rem,13vw,4\.8rem\); line-height:\.98; letter-spacing:-\.045em; \} \.dock-wrap \{ padding-bottom:max\(\.55rem,env\(safe-area-inset-bottom\)\); \} \}', '\n  @media (max-width:760px) { html { scroll-padding-top: max(4.5rem, calc(3.75rem + env(safe-area-inset-top))); } body { -webkit-overflow-scrolling: touch; overscroll-behavior-x: none; } .hero-heading,.hero-bigtext { font-size:clamp(2.25rem,13vw,4.8rem); line-height:.98; letter-spacing:-.045em; } .dock-wrap { padding-bottom:max(.55rem,env(safe-area-inset-bottom)); } }', text)

# Keep exactly two visible theme options.
old_options = '''        <option value="auto">Auto</option>\n        <option value="morning">Morning</option>\n        <option value="light">Day</option>\n        <option value="evening">Evening</option>\n        <option value="dark">Night</option>'''
new_options = '''        <option value="light">Day Mode</option>\n        <option value="dark">Night Mode</option>'''
text = text.replace(old_options, new_options)

# Replace the multi-mode runtime with a stable two-mode system.
old_runtime = re.compile(r'  /\* ============================================================\n     4-THEME SYSTEM .*?\n  const themeSelect = document\.getElementById\(\'theme-select\'\);.*?\n  /\* Scroll progress', re.S)
new_runtime = '''  /* ============================================================
     TWO-MODE THEME SYSTEM — Day Mode / Night Mode
     A stored choice drives the dropdown and the data-theme attribute.
  ============================================================ */
  const root = document.documentElement;
  const themeSelect = document.getElementById('theme-select');
  const THEME_COLORS = { light:'#F3F6FC', dark:'#0B0E1A' };
  function applyTheme(theme){
    const next = theme === 'dark' ? 'dark' : 'light';
    root.setAttribute('data-theme', next);
    if(themeSelect) themeSelect.value = next;
    localStorage.setItem('themeMode', next);
    const meta = document.getElementById('theme-color-meta');
    if(meta) meta.setAttribute('content', THEME_COLORS[next]);
  }
  let themeMode = localStorage.getItem('themeMode') === 'dark' ? 'dark' : 'light';
  applyTheme(themeMode);
  themeSelect.addEventListener('change', ()=>applyTheme(themeSelect.value));

  /* Scroll progress'''
text, runtime_count = old_runtime.subn(new_runtime, text, count=1)
if runtime_count != 1 and 'TWO-MODE THEME SYSTEM' not in text:
    raise SystemExit('Theme runtime block was not found; migration stopped.')

# Add a coherent phone-style night surface without touching motion scripts.
night_css = '''<style id="day-night-mode-v1">
  :root{color-scheme:light;}
  html[data-theme="light"]{color-scheme:light;}
  html[data-theme="dark"]{color-scheme:dark;}
  html[data-theme="dark"] body{background:#070b14;color:#eef4ff;}
  html[data-theme="dark"] .topnav{background:rgba(10,18,32,.88)!important;border-color:rgba(177,201,235,.18)!important;box-shadow:0 16px 40px rgba(0,0,0,.34),inset 0 1px 0 rgba(255,255,255,.08)!important;}
  html[data-theme="dark"] .topnav .brand,html[data-theme="dark"] .topnav button,html[data-theme="dark"] .topnav select,html[data-theme="dark"] .cmdk-trigger-btn,html[data-theme="dark"] .lang-toggle,html[data-theme="dark"] .theme-select{color:#f3f7ff!important;background:rgba(20,34,57,.86)!important;border-color:rgba(177,201,235,.22)!important;}
  html[data-theme="dark"] .hero-glass,html[data-theme="dark"] .section.bento-card,html[data-theme="dark"] .glass-card,html[data-theme="dark"] .card,html[data-theme="dark"] .folio,html[data-theme="dark"] .skill-card,html[data-theme="dark"] .pursuing-card{background:rgba(12,24,43,.82)!important;border-color:rgba(177,201,235,.18)!important;box-shadow:0 24px 70px -30px rgba(0,0,0,.74),inset 0 1px 0 rgba(255,255,255,.06)!important;}
  html[data-theme="dark"] .hero h1,html[data-theme="dark"] .section h2,html[data-theme="dark"] .section h3,html[data-theme="dark"] .hero-bigtext,html[data-theme="dark"] .bento-card h3{color:#f4f7ff!important;}
  html[data-theme="dark"] .hero .lede,html[data-theme="dark"] .section p,html[data-theme="dark"] .card p,html[data-theme="dark"] .folio p,html[data-theme="dark"] .skill-card p,html[data-theme="dark"] .pursuing-card p{color:#b7c5d9!important;}
  html[data-theme="dark"] .btn-ghost,html[data-theme="dark"] .dock,html[data-theme="dark"] .dock-item{background:rgba(16,30,51,.84)!important;border-color:rgba(177,201,235,.22)!important;color:#eaf2ff!important;}
  html[data-theme="dark"] .btn-primary,html[data-theme="dark"] .play-journey-btn{background:#f0f5ff!important;color:#0a1425!important;box-shadow:0 14px 32px -18px rgba(0,0,0,.8)!important;}
  html[data-theme="dark"] .story-rail a{color:#b7c5d9!important;}
  html[data-theme="dark"] .story-rail a.active,html[data-theme="dark"] .story-rail a:hover,html[data-theme="dark"] .dock-item.dock-active,html[data-theme="dark"] .dock-item:hover{color:#a9caff!important;}
  html[data-theme="dark"] .ai-panel{background:#0d1a2e!important;border-color:rgba(177,201,235,.2)!important;color:#eef4ff!important;}
  html[data-theme="dark"] .tree-bg-scrim{background:linear-gradient(180deg,rgba(5,10,20,.12),rgba(5,10,20,.58) 64%,rgba(3,7,14,.94))!important;}
  @media (max-width:760px){html[data-theme="dark"] .topnav{background:rgba(8,15,27,.94)!important;}html[data-theme="dark"] .hero-glass,html[data-theme="dark"] .section.bento-card{backdrop-filter:blur(12px) saturate(112%)!important;-webkit-backdrop-filter:blur(12px) saturate(112%)!important;}}
  @media (prefers-reduced-motion:reduce){html[data-theme="dark"] *,html[data-theme="dark"] *::before,html[data-theme="dark"] *::after{transition:none!important;animation-duration:.001ms!important;}}
</style>
'''
if 'id="day-night-mode-v1"' not in text:
    text = text.replace('</head>', night_css + '</head>', 1)

if text != original:
    INDEX.write_text(text, encoding='utf-8')
print(f'updated index.html: {text != original}')
print(f'guided_present: {start_marker in text}')
print(f'theme_options: {text.count("<option value=\"light\">Day Mode</option>") + text.count("<option value=\"dark\">Night Mode</option>")}')
print(f'two_mode_runtime: {"TWO-MODE THEME SYSTEM" in text}')
