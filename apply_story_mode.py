from pathlib import Path

path = Path('/home/ubuntu/iyashchaudhary.github.io/index.html')
html = path.read_text()

css_marker = '/* STORY_MODE_V1 */'
css = '''
  /* STORY_MODE_V1 — lightweight cinematic story mode */
  :root{--story-progress:0%;}
  body::before{content:"";position:fixed;inset:0 0 auto 0;height:3px;z-index:220;background:linear-gradient(90deg,var(--primary),var(--accent));transform:scaleX(var(--story-progress));transform-origin:left center;box-shadow:0 0 18px color-mix(in srgb,var(--primary) 55%,transparent);pointer-events:none;}
  .story-rail{position:fixed;right:18px;top:50%;transform:translateY(-50%);z-index:80;display:flex;flex-direction:column;align-items:flex-end;gap:9px;}
  .story-rail a{display:flex;align-items:center;gap:8px;color:var(--text-dim);text-decoration:none;font-size:10px;letter-spacing:.1em;text-transform:uppercase;opacity:.62;transition:opacity .2s ease,color .2s ease,transform .2s ease;}
  .story-rail a::after{content:"";width:7px;height:7px;border:1px solid currentColor;border-radius:50%;background:var(--bg);transition:transform .2s ease,background .2s ease;}
  .story-rail a:hover,.story-rail a.active{opacity:1;color:var(--primary);transform:translateX(-2px);}
  .story-rail a.active::after{transform:scale(1.45);background:var(--primary);box-shadow:0 0 0 4px color-mix(in srgb,var(--primary) 18%,transparent);}
  .story-kicker{display:inline-flex;align-items:center;gap:8px;margin:0 0 18px;color:var(--text-dim);font-size:11px;letter-spacing:.12em;text-transform:uppercase;}
  .story-kicker::before{content:"";width:24px;height:1px;background:var(--primary);}
  .story-note{margin:0 0 28px;max-width:52ch;color:var(--text-dim);font-size:.9rem;}
  .story-depth{transform:translate3d(0,var(--story-y,0px),0);transition:transform .18s linear;}
  .learning-strip{display:grid;grid-template-columns:1.1fr 1fr;gap:18px;margin-top:28px;padding:20px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(135deg,color-mix(in srgb,var(--primary) 8%,var(--bg)),color-mix(in srgb,var(--accent) 5%,var(--bg)));}
  .learning-strip h3{font-family:'Fraunces',serif;font-size:1.25rem;color:var(--text);margin:0 0 7px;}
  .learning-strip p{margin:0;color:var(--text-dim);font-size:.9rem;}
  .learning-list{display:flex;flex-wrap:wrap;gap:8px;align-content:center;}
  .learning-list span{padding:8px 10px;border:1px solid var(--line);border-radius:999px;color:var(--text);font-size:11px;background:color-mix(in srgb,var(--card) 78%,transparent);}
  .chapter-label{display:block;margin:0 0 8px;color:var(--primary);font:600 11px/1 'IBM Plex Mono',monospace;letter-spacing:.12em;text-transform:uppercase;}
  @media (max-width:900px){.story-rail{right:10px}.learning-strip{grid-template-columns:1fr}}
  @media (max-width:600px){.story-rail{display:none}.story-depth{transform:none}.learning-strip{padding:16px}.story-kicker{margin-bottom:13px}}
  @media (prefers-reduced-motion:reduce){.story-depth{transform:none!important;transition:none}body::before{box-shadow:none}}
'''
if css_marker not in html:
    html = html.replace('</style>', css + '\n  ' + css_marker + '\n</style>', 1)

rail_marker = '<!-- STORY_RAIL_V1 -->'
rail = '''<aside class="story-rail" id="story-rail" aria-label="Story chapters">
    <a href="#hello" data-story-link><span>Meet Yash</span></a>
    <a href="#journey" data-story-link><span>The Journey</span></a>
    <a href="#experience" data-story-link><span>Experience</span></a>
    <a href="#pursuing" data-story-link><span>Learning</span></a>
    <a href="#credentials" data-story-link><span>Proof</span></a>
    <a href="#skills" data-story-link><span>Skills</span></a>
    <a href="#contact" data-story-link><span>Connect</span></a>
  </aside>
  <!-- STORY_RAIL_V1 -->'''
if rail_marker not in html:
    html = html.replace('  <!-- ===================== SYSTEM 1: FLOATING DOCK NAVIGATION ===================== -->', rail + '\n\n  <!-- ===================== SYSTEM 1: FLOATING DOCK NAVIGATION ===================== -->', 1)

hero_marker = '<div class="visitor-greeting" id="visitor-greeting"></div>'
hero_insert = hero_marker + '\n            <div class="story-kicker hero-entrance-el">Chapter 01 · Meet Yash</div>'
if 'Chapter 01 · Meet Yash' not in html:
    html = html.replace(hero_marker, hero_insert, 1)

journey_marker = "      <p class=\"sec-desc reveal\">College didn't go in a straight line — and that's worth showing, not hiding. Tap any entry to read the full story.</p>"
journey_insert = journey_marker + '\n      <p class="story-note reveal">A real timeline of choices, changes and the direction I am building toward.</p>'
if 'A real timeline of choices' not in html:
    html = html.replace(journey_marker, journey_insert, 1)

pursuing_marker = '<div class="pursuing-grid" id="pursuing-grid">'
learning = '''<div class="learning-strip reveal" aria-label="Currently learning and building">
        <div><span class="chapter-label">Currently learning</span><h3>Building the next version of myself.</h3><p>These are real directions I am actively exploring—not finished claims. Progress belongs in the journal; this is the honest snapshot.</p></div>
        <div class="learning-list" aria-label="Current learning areas"><span>ACCA direction</span><span>AI automation</span><span>Video editing</span><span>Social media marketing</span><span>Personal systems</span></div>
      </div>

      ''' + pursuing_marker
if 'Building the next version of myself.' not in html and pursuing_marker in html:
    html = html.replace(pursuing_marker, learning, 1)

js_marker = '/* STORY_MODE_SCRIPT_V1 */'
js = '''<script>
  /* STORY_MODE_SCRIPT_V1 */
  (() => {
    const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const links = [...document.querySelectorAll('[data-story-link]')];
    const sections = links.map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
    const root = document.documentElement;
    const update = () => {
      const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      root.style.setProperty('--story-progress', `${Math.min(100, Math.max(0, window.scrollY / max * 100))}%`);
      if (!sections.length) return;
      let current = sections[0];
      sections.forEach(section => { if (section.getBoundingClientRect().top <= window.innerHeight * .42) current = section; });
      links.forEach(link => link.classList.toggle('active', link.getAttribute('href') === `#${current.id}`));
      if (!reduce && window.innerWidth > 600) document.querySelectorAll('[data-story-depth]').forEach(el => {
        const r = el.getBoundingClientRect();
        const y = Math.max(-12, Math.min(12, (window.innerHeight * .5 - (r.top + r.height * .5)) * .018));
        el.style.setProperty('--story-y', `${y.toFixed(2)}px`);
      });
    };
    let ticking = false;
    window.addEventListener('scroll', () => { if (!ticking) { window.requestAnimationFrame(() => { update(); ticking = false; }); ticking = true; } }, {passive:true});
    links.forEach(link => link.addEventListener('click', () => { links.forEach(x => x.classList.remove('active')); link.classList.add('active'); }));
    document.querySelectorAll('.hero-glass,.section.bento-card').forEach(el => el.setAttribute('data-story-depth',''));
    update();
  })();
</script>'''
if js_marker not in html:
    html = html.replace('</body>', js + '\n</body>', 1)

path.write_text(html)
print('story mode patch applied')
