from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
CONVERSIONS = [
    ('assets/portfolio-scenic-blue-hero.jpg', 'assets/portfolio-scenic-blue-hero.webp', 82),
    ('photos/day07.png', 'photos/day07.webp', 86),
]
for source_rel, target_rel, quality in CONVERSIONS:
    source = ROOT / source_rel
    target = ROOT / target_rel
    if not source.exists():
        raise SystemExit(f'Missing source: {source_rel}')
    with Image.open(source) as image:
        image = image.convert('RGB')
        image.save(target, 'WEBP', quality=quality, method=6)
    print(f'{source_rel} -> {target_rel}: {source.stat().st_size} -> {target.stat().st_size} bytes')
