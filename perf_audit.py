from pathlib import Path
import re

ROOT = Path(__file__).parent
FILES = [ROOT / 'index.html', ROOT / 'unfiltered.html', ROOT / 'admin.html']
PATTERNS = {
    'animations': r'animation\s*:',
    'keyframes': r'@keyframes',
    'transitions': r'transition\s*:',
    'backdrop_filter': r'backdrop-filter',
    'blur': r'blur\s*\(',
    'scroll_listeners': r'addEventListener\s*\(\s*[\'\"]scroll',
    'raf': r'requestAnimationFrame',
    'timeouts': r'\bsetTimeout\s*\(',
    'intervals': r'\bsetInterval\s*\(',
    'observers': r'IntersectionObserver',
    'background_images': r'background-image\s*:',
}
for path in FILES:
    text = path.read_text(encoding='utf-8', errors='ignore')
    print(f'--- {path.name} bytes={len(text.encode())} lines={text.count(chr(10))+1} ---')
    for label, pattern in PATTERNS.items():
        print(f'{label}={len(re.findall(pattern, text, flags=re.I))}')
    for needle in ('<video', 'loading="lazy"', 'content-visibility', 'mobile-performance', 'autonomous-polish'):
        print(f'{needle}={text.lower().count(needle.lower())}')

print('--- largest tracked media ---')
media_ext = {'.png', '.jpg', '.jpeg', '.webp', '.mp4', '.webm'}
media = []
for rel in __import__('subprocess').check_output(['git', 'ls-files'], cwd=ROOT, text=True).splitlines():
    p = ROOT / rel
    if p.suffix.lower() in media_ext and p.exists():
        media.append((p.stat().st_size, rel))
for size, rel in sorted(media, reverse=True)[:20]:
    print(size, rel)

print('--- status ---')
print(__import__('subprocess').check_output(['git', 'status', '--short'], cwd=ROOT, text=True), end='')
