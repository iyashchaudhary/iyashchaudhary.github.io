from pathlib import Path

ROOT = Path(__file__).parent
INDEX = ROOT / 'index.html'
ADMIN = ROOT / 'admin.html'

INDEX_CSS = r'''
/* PREMIUM_JOURNEY_STUDIO_V1 */
.journey-studio{position:relative;margin:28px 0 34px;padding:clamp(22px,4vw,42px);border:1px solid var(--line);border-radius:24px;background:linear-gradient(135deg,color-mix(in srgb,var(--card) 96%,var(--primary)),color-mix(in srgb,var(--bg) 90%,var(--accent)));overflow:hidden;box-shadow:0 22px 60px -42px rgba(0,0,0,.55)}
.journey-studio:before{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(circle at 90% 10%,color-mix(in srgb,var(--primary) 17%,transparent),transparent 32%),linear-gradient(115deg,transparent 0 48%,color-mix(in srgb,var(--accent) 5%,transparent) 49% 50%,transparent 51%)}
.studio-head,.studio-grid,.studio-bottom{position:relative;z-index:1}
.studio-kicker{margin:0 0 8px;color:var(--primary);font:600 11px/1 'IBM Plex Mono',monospace;letter-spacing:.14em;text-transform:uppercase}
.studio-head h2{margin:0;color:var(--text);font-family:'Fraunces',serif;font-size:clamp(1.7rem,4vw,2.7rem);max-width:760px}
.studio-head p{max-width:680px;color:var(--text-dim);margin:12px 0 0;line-height:1.7}
.studio-replay{display:flex;flex-wrap:wrap;gap:9px;margin-top:20px}
.studio-replay a{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);border-radius:999px;padding:8px 12px;color:var(--text-dim);text-decoration:none;font:600 10px/1 'IBM Plex Mono',monospace;transition:transform .18s ease,border-color .18s ease,color .18s ease}
.studio-replay a:hover,.studio-replay a:focus-visible{transform:translateY(-2px);border-color:var(--primary);color:var(--primary);outline:none}
.studio-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:16px;margin-top:24px}
.studio-panel{border:1px solid var(--line);border-radius:18px;background:color-mix(in srgb,var(--bg) 42%,transparent);padding:18px}
.studio-panel h3{margin:0 0 13px;color:var(--text);font-size:1.05rem}
.studio-map{display:grid;gap:10px}
.studio-map-item{display:grid;grid-template-columns:28px 1fr;gap:10px;align-items:start;padding:10px;border-radius:12px;background:color-mix(in srgb,var(--card) 70%,transparent);border:1px solid transparent}
.studio-map-item strong{color:var(--text);font-size:.94rem}.studio-map-item span{display:block;color:var(--text-dim);font-size:.78rem;margin-top:3px;line-height:1.45}.studio-node{width:24px;height:24px;border-radius:50%;display:grid;place-items:center;background:color-mix(in srgb,var(--primary) 18%,transparent);color:var(--primary);font:600 10px 'IBM Plex Mono',monospace}
.studio-focus{display:grid;gap:10px}.studio-focus-card{padding:12px;border-left:2px solid var(--primary);background:color-mix(in srgb,var(--primary) 5%,transparent)}.studio-focus-card b{display:block;color:var(--text);font-size:.86rem}.studio-focus-card span{display:block;color:var(--text-dim);font-size:.76rem;margin-top:3px;line-height:1.45}
.studio-progress{margin-top:16px}.studio-progress-head{display:flex;justify-content:space-between;gap:12px;color:var(--text-dim);font:600 10px 'IBM Plex Mono',monospace;text-transform:uppercase;letter-spacing:.08em}.studio-progress-track{height:8px;border-radius:99px;background:color-mix(in srgb,var(--line) 80%,transparent);overflow:hidden;margin-top:9px}.studio-progress-fill{height:100%;width:0;background:linear-gradient(90deg,var(--primary),var(--accent));border-radius:inherit;transition:width .6s cubic-bezier(.23,1,.32,1)}
.studio-bottom{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px}.studio-list{display:grid;gap:9px}.studio-list-item{padding:11px 12px;border:1px solid var(--line);border-radius:12px;background:color-mix(in srgb,var(--card) 76%,transparent)}.studio-list-item b{display:block;color:var(--text);font-size:.86rem}.studio-list-item span{display:block;color:var(--text-dim);font-size:.75rem;line-height:1.45;margin-top:3px}.studio-proof-link{color:var(--primary);text-decoration:none;font-size:.72rem;display:inline-block;margin-top:7px}
.studio-leave{margin-top:16px;padding:15px;border-radius:15px;border:1px dashed color-mix(in srgb,var(--primary) 45%,var(--line));color:var(--text-dim);font-size:.84rem;line-height:1.6}.studio-leave strong{color:var(--text)}
@media (max-width:760px){.studio-grid,.studio-bottom{grid-template-columns:1fr}.studio-replay{gap:7px}.studio-replay a{font-size:9px;padding:7px 9px}}
@media (prefers-reduced-motion:reduce){.studio-replay a,.studio-progress-fill{transition:none}}
'''

INDEX_HTML = r'''
<section class="journey-studio scene" id="journey-studio" data-scene="journey-studio" aria-labelledby="studio-title">
  <div class="studio-head">
    <p class="studio-kicker">A guided starting point</p>
    <h2 id="studio-title">This is not a finished portfolio. It is a public record of becoming better.</h2>
    <p>Start here for the short version of Yash's real journey. Every card below is generated from the same journal, experience, learning, and proof data already used across the site.</p>
    <nav class="studio-replay" aria-label="Story replay">
      <a href="#journey">01 Journey</a><a href="#experience">02 Experience</a><a href="#learning">03 Learning</a><a href="#credentials">04 Proof</a><a href="#skills">05 Skills</a><a href="#contact">06 Connect</a>
    </nav>
  </div>
  <div class="studio-grid">
    <section class="studio-panel" aria-labelledby="map-title"><h3 id="map-title">Journey map</h3><div class="studio-map" id="studio-map"></div></section>
    <section class="studio-panel" aria-labelledby="focus-title"><h3 id="focus-title">Current direction</h3><div class="studio-focus" id="studio-focus"></div><div class="studio-progress"><div class="studio-progress-head"><span>Documented momentum</span><span id="studio-progress-label">—</span></div><div class="studio-progress-track" role="progressbar" aria-label="Average documented discipline" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><div class="studio-progress-fill" id="studio-progress-fill"></div></div></div></section>
  </div>
  <div class="studio-bottom">
    <section class="studio-panel" aria-labelledby="learning-vault-title"><h3 id="learning-vault-title">Learning vault</h3><div class="studio-list" id="studio-learning"></div></section>
    <section class="studio-panel" aria-labelledby="proof-wall-title"><h3 id="proof-wall-title">Proof wall</h3><div class="studio-list" id="studio-proof"></div></section>
  </div>
  <div class="studio-leave"><strong>Before you leave:</strong> <span id="studio-leave-copy">The latest work is documented in the journal. Come back as the record grows.</span></div>
</section>
'''

INDEX_JS = r'''
/* PREMIUM_JOURNEY_STUDIO_SCRIPT_V1 */
(() => {
  const esc = (v) => String(v ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const map = document.getElementById('studio-map');
  const focus = document.getElementById('studio-focus');
  const learning = document.getElementById('studio-learning');
  const proof = document.getElementById('studio-proof');
  if (!map || !focus || !learning || !proof) return;
  const journey = Array.isArray(window.JOURNEY_DATA) ? window.JOURNEY_DATA : [];
  const focusData = window.FOCUS_DATA?.items || [];
  const learned = Array.isArray(window.THINGS_LEARNED) ? window.THINGS_LEARNED : [];
  const built = Array.isArray(window.THINGS_BUILT) ? window.THINGS_BUILT : [];
  const creds = Object.values(window.CREDENTIALS_DATA || {}).flat().filter(Boolean);
  map.innerHTML = journey.slice(0, 6).map((x, i) => `<div class="studio-map-item"><div class="studio-node">${String(i+1).padStart(2,'0')}</div><div><strong>${esc(x.title || 'Journey chapter')}</strong><span>${esc(x.date || x.paragraphs?.[0]?.slice(0,105) || 'Documented chapter')}</span></div></div>`).join('') || '<div class="studio-list-item"><span>The map will grow with the next real chapter.</span></div>';
  focus.innerHTML = focusData.slice(0, 4).map(x => `<div class="studio-focus-card"><b>${esc(x.label)} · ${esc(x.value)}</b><span>${esc(x.desc)}</span></div>`).join('') || '<div class="studio-list-item"><span>Current focus will appear when it is documented.</span></div>';
  learning.innerHTML = learned.concat((window.SKILLS_DATA || []).filter(x => /AI|automation|Excel|Finance/i.test(`${x.title} ${x.desc}`)).slice(0, 3)).slice(0, 4).map(x => `<div class="studio-list-item"><b>${esc(x.course || x.title)}</b><span>${esc(x.usedFor || x.desc || 'Learning in progress')}</span></div>`).join('') || '<div class="studio-list-item"><span>No learning record added yet.</span></div>';
  proof.innerHTML = creds.concat(built).slice(0, 5).map(x => `<div class="studio-list-item"><b>${esc(x.title || 'Proof item')}</b><span>${esc(x.issuer || x.outcome || x.learned || x.date || '')}</span>${x.verifyUrl ? `<a class="studio-proof-link" href="${esc(x.verifyUrl)}" target="_blank" rel="noopener">View verification ↗</a>` : ''}</div>`).join('') || '<div class="studio-list-item"><span>Proof wall will grow with verified work.</span></div>';
  const entries = Array.isArray(window.UNFILTERED_ENTRIES) ? window.UNFILTERED_ENTRIES : [];
  const avg = entries.length ? Math.round(entries.reduce((sum, e) => sum + Number(e.discipline || 0), 0) / entries.length) : 0;
  const fill = document.getElementById('studio-progress-fill'); const label = document.getElementById('studio-progress-label'); const bar = fill?.parentElement?.parentElement;
  if (fill) fill.style.width = `${Math.max(0, Math.min(100, avg))}%`;
  if (label) label.textContent = entries.length ? `${avg}% average across ${entries.length} documented day${entries.length === 1 ? '' : 's'}` : 'No days documented yet';
  if (bar) bar.setAttribute('aria-valuenow', String(avg));
  const latest = entries.slice().sort((a,b) => String(b.date).localeCompare(String(a.date)))[0];
  const leave = document.getElementById('studio-leave-copy');
  if (leave && latest) leave.textContent = `Latest documented chapter: Day ${esc(latest.day)} · ${esc(latest.date)}. The record is still being built.`;
})();
'''

ADMIN_GUARD = r'''
/* PREMIUM_PUBLISH_GUARD_V1 */
function validatePublishPayload(filename, payload){
  if(!payload || typeof payload !== 'string') throw new Error('Publish stopped: generated content is empty.');
  try { new Function(payload); } catch(e) { throw new Error('Publish stopped: generated JavaScript is invalid. ' + e.message); }
  if(filename === 'entries-data.js'){
    const assets = [...payload.matchAll(/(?:src|poster):\s*["']([^"']+)["']/g)].map(m=>m[1]).filter(x=>x && !x.startsWith('data:') && !/^https?:/i.test(x));
    const missing = assets.filter(x => /^media\//.test(x) && !((window._publishedAssetNames||[]).includes(x)));
    if(missing.length) throw new Error('Publish stopped: media reference is missing from the selected upload list: ' + missing[0]);
    if(/photos:\s*\[\s*\]/.test(payload) && /journal-/.test(payload)) throw new Error('Publish stopped: a journal media array appears empty while media assets are present. Check the selected photos before publishing.');
  }
}
'''


def inject_once(text, marker, payload, anchor):
    if marker in text:
        return text
    return text.replace(anchor, payload + '\n' + anchor, 1)

index = INDEX.read_text()
index = inject_once(index, 'PREMIUM_JOURNEY_STUDIO_V1', '<style>\n' + INDEX_CSS + '\n</style>', '</head>')
index = inject_once(index, 'id="journey-studio"', INDEX_HTML, '<section class="section bento-card bento-span-7 scene" id="journey"')
index = inject_once(index, 'PREMIUM_JOURNEY_STUDIO_SCRIPT_V1', '<script>\n' + INDEX_JS + '\n</script>', '</body>')
if 'entries-data.js' not in index:
    index = index.replace('</head>', '<script src="entries-data.js?v=journey-studio"></script>\n</head>', 1)
INDEX.write_text(index)

admin = ADMIN.read_text()
admin = inject_once(admin, 'PREMIUM_PUBLISH_GUARD_V1', '<script>\n' + ADMIN_GUARD + '\n</script>', '</head>')
needle = "setCmsStatus('Checking selected media before publishing…','info');"
if 'validatePublishPayload(filename, newContent)' not in admin:
    admin = admin.replace(needle, needle + "\n      validatePublishPayload(filename, newContent);", 1)
ADMIN.write_text(admin)
print('Applied premium journey studio and publish guard.')
print('Index bytes:', INDEX.stat().st_size, 'Admin bytes:', ADMIN.stat().st_size)
