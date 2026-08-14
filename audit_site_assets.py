from pathlib import Path
from urllib.parse import urlparse
import re

root = Path('.')
files = [Path('index.html'), Path('unfiltered.html'), Path('entries-data.js'), Path('portfolio-data.js')]
refs = []
for file in files:
    if not file.exists():
        continue
    text = file.read_text(errors='ignore')
    for match in re.findall(r'(?:src|image|thumb|thumbnail|certImg)\s*[:=]\s*["\']([^"\']+)', text):
        if match.startswith(('http://','https://','data:','/')):
            continue
        refs.append((file.name, match.split('?')[0].split('#')[0]))
unique = sorted(set(refs))
missing = [(source, ref) for source, ref in unique if not (root / ref).exists()]
print('asset references:', len(unique))
print('missing local assets:', len(missing))
for source, ref in missing[:50]:
    print(f'MISSING {source}: {ref}')
