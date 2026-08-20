from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"

text = INDEX.read_text(encoding="utf-8")
original = text

# Remove the complete guided-starting-point section by using the next real section as
# the boundary; this safely handles the nested <section> elements inside the studio.
start_marker = '<section class="journey-studio scene" id="journey-studio"'
end_marker = '<section class="section bento-card bento-span-7 scene" id="journey"'
if start_marker in text and end_marker in text:
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    text = text[:start] + text[end:]

# Remove its dedicated renderer script.
text = re.sub(
    r'\s*<script>\s*/\* PREMIUM_JOURNEY_STUDIO_SCRIPT_V1 \*/.*?</script>\s*',
    '\n', text, flags=re.S | re.I
)

# Remove the dedicated Premium Journey Studio CSS block.
text = re.sub(r'\s*<style>\s*/\* PREMIUM_JOURNEY_STUDIO_V1 \*/.*?</style>\s*', '\n', text, flags=re.S | re.I)

# Remove standalone layout rules that only served the deleted studio section.
text = re.sub(r'\n\s*\.journey-studio \{ grid-column: 1 / -1; width: 100%; min-width: 0; \}\n', '\n', text)
text = re.sub(r'\n\s*@media \(max-width:760px\) \{ html \{ scroll-padding-top: max\(4\.5rem, calc\(3\.75rem \+ env\(safe-area-inset-top\)\)\); \} body \{ -webkit-overflow-scrolling: touch; overscroll-behavior-x: none; \} \.journey-studio,\.studio-grid,\.studio-map,\.studio-focus,\.studio-bottom \{ width:100%; min-width:0; max-width:100%; \} \.studio-grid \{ grid-template-columns:minmax\(0,1fr\)!important; \} \.hero-heading,.hero-bigtext \{ font-size:clamp\(2\.25rem,13vw,4\.8rem\); line-height:\.98; letter-spacing:-\.045em; \} \.dock-wrap \{ padding-bottom:max\(\.55rem,env\(safe-area-inset-bottom\)\); \} \}', '\n  @media (max-width:760px) { html { scroll-padding-top: max(4.5rem, calc(3.75rem + env(safe-area-inset-top))); } body { -webkit-overflow-scrolling: touch; overscroll-behavior-x: none; } .hero-heading,.hero-bigtext { font-size:clamp(2.25rem,13vw,4.8rem); line-height:.98; letter-spacing:-.045em; } .dock-wrap { padding-bottom:max(.55rem,env(safe-area-inset-bottom)); } }', text)

# Remove studio-only selectors from shared rules, without changing the rules' behavior
# for the remaining hero, bento, folio, skill, and pursuit elements.
replacements = {
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
}
for old, new in replacements.items():
    text = text.replace(old, new)
text = text.replace('section[id],.journey-studio[id]', 'section[id]')
text = text.replace('.studio-head h2,', '')
text = text.replace('.studio-head p,', '')
text = text.replace('.studio-head h2', '')
text = text.replace('.studio-head p', '')

# Remove now-empty studio-only declarations left inside selector lists.
text = re.sub(r'\n\s*\.studio-(?:node|focus-card|progress-fill|map-item|list-item|replay|kicker)[^{]*\{[^}]*\}', '', text, flags=re.S)

if text != original:
    INDEX.write_text(text, encoding="utf-8")

print(f"updated index.html: {text != original}")
print(f"guided_section_present: {start_marker in text}")
print(f"studio_renderer_present: {'PREMIUM_JOURNEY_STUDIO_SCRIPT_V1' in text}")
if __name__ == "__main__":
    pass
