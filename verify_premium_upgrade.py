from pathlib import Path
import re
from html.parser import HTMLParser

class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.hrefs=[]; self.ids=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag == 'a' and attrs.get('href','').startswith('#'): self.hrefs.append(attrs['href'][1:])
        if attrs.get('id'): self.ids.append(attrs['id'])


for name in ('index.html', 'admin.html'):
    text = Path(name).read_text()
    scripts = []
    for match in re.finditer(r'<script([^>]*)>(.*?)</script>', text, re.S | re.I):
        attrs, body = match.groups()
        if 'application/ld+json' in attrs.lower():
            continue
        scripts.append(body)
    Path('/tmp/' + name + '.js').write_text('\n'.join(scripts))
    print(name, 'inline scripts:', len(scripts))

index = Path('index.html').read_text()
admin = Path('admin.html').read_text()
checks = {
    'guided starting point removed': 'id="journey-studio"' not in index and 'A guided starting point' not in index,
    'studio renderer removed': 'PREMIUM_JOURNEY_STUDIO_V1' not in index and 'PREMIUM_JOURNEY_STUDIO_SCRIPT_V1' not in index,
    'day night theme options': index.count('<option value="light">Day Mode</option>') == 1 and index.count('<option value="dark">Night Mode</option>') == 1 and not any(f'<option value="{x}"' in index for x in ('auto','morning','evening')),
    'premium apple motion retained': 'APPLE_MOTION_V1_START' in index and 'APPLE_MOTION_V1_END' in index,
    'journey section retained': 'id="journey"' in index,
    'experience section retained': 'id="experience"' in index,
    'learning section retained': 'id="pursuing"' in index,
    'proof section retained': 'id="credentials"' in index,
    'skills section retained': 'id="skills"' in index,
    'contact section retained': 'id="contact"' in index,
    'entries data import': 'entries-data.js?v=journey-studio' in index or 'entries-data.js?v=' in index,
    'publish guard': 'PREMIUM_PUBLISH_GUARD_V1' in admin,
    'guard after serialization': "validatePublishPayload(filename, newContent);" in admin,
}
for label, ok in checks.items():
    if not ok:
        raise SystemExit('FAIL: ' + label)
parser = AnchorParser(); parser.feed(index)
missing = sorted(set(parser.hrefs) - set(parser.ids))
if missing:
    raise SystemExit('FAIL: broken internal anchors: ' + ', '.join(missing))
print('internal anchors: PASS')
print('structure checks: PASS')
