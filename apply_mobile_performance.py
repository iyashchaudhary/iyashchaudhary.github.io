from pathlib import Path

files = [Path('index.html'), Path('unfiltered.html')]
start = '<!-- MOBILE_PERFORMANCE_V1_START -->'
end = '<!-- MOBILE_PERFORMANCE_V1_END -->'
css = '''<style>\n<!-- MOBILE_PERFORMANCE_V1_START -->\n@media (max-width:760px){\n  html{scroll-behavior:auto!important;overscroll-behavior-y:auto!important}\n  body{touch-action:pan-y;overscroll-behavior-y:auto;-webkit-overflow-scrolling:touch}\n  #tree-bg,.tree-bg{animation:none!important;background-attachment:scroll!important;will-change:auto!important}\n  #tree-bg::after,.tree-bg::after,.tree-bg-glow,.tree-bg-glow-2,.particle-layer{animation:none!important;will-change:auto!important}\n  .scene{transition:none!important;transform:none!important;filter:none!important;opacity:1!important}\n  .hero-glass,.glass-card,.section.bento-card,.topnav,.dock,.journey-studio,.studio-panel,.consistency-graph{backdrop-filter:blur(6px) saturate(118%)!important;-webkit-backdrop-filter:blur(6px) saturate(118%)!important}\n  .apple-reveal{will-change:opacity,transform;transition-duration:.38s!important}\n  .apple-float{will-change:auto!important}\n  img{content-visibility:auto}\n}\n@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto!important}.apple-reveal{will-change:auto!important}}\n<!-- MOBILE_PERFORMANCE_V1_END -->\n</style>'''
for path in files:
    html = path.read_text()
    if start in html and end in html:
        a = html.index(start)
        b = html.index(end, a) + len(end)
        html = html[:a] + html[b:]
    html = html.replace('</head>', css + '\n</head>', 1)
    path.write_text(html)
print('Mobile performance layer applied to', ', '.join(str(p) for p in files))
