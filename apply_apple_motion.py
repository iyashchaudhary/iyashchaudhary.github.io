from pathlib import Path

path = Path('index.html')
html = path.read_text()
start = '<!-- APPLE_MOTION_V1_START -->'
end = '<!-- APPLE_MOTION_V1_END -->'
if start in html and end in html:
    a = html.index(start)
    b = html.index(end, a) + len(end)
    html = html[:a] + html[b:]

css = '''<style>
<!-- APPLE_MOTION_V1_START -->
:root{--apple-ease:cubic-bezier(.22,1,.36,1);--apple-spring:cubic-bezier(.16,1.22,.3,1)}
body{font-kerning:normal;text-rendering:optimizeLegibility}
.hero h1,.studio-head h2,.section h2{letter-spacing:-.045em;text-wrap:balance}
.hero h1{font-size:clamp(2.8rem,7vw,5.8rem);line-height:.96}
.section h2{font-size:clamp(1.9rem,4.2vw,3.4rem);line-height:1.02}
.hero-glass,.journey-studio,.section.bento-card{isolation:isolate}
.hero-glass:after,.journey-studio:after,.section.bento-card:after{content:"";position:absolute;inset:-20%;z-index:-1;pointer-events:none;background:radial-gradient(circle at var(--apple-x,50%) var(--apple-y,30%),rgba(255,255,255,.32),transparent 21%);opacity:0;transition:opacity .35s var(--apple-ease)}
.hero-glass:hover:after,.journey-studio:hover:after,.section.bento-card:hover:after{opacity:1}
.btn-primary,.btn-ghost,.studio-replay a,.dock-item,.topnav button,.topnav select{transition:transform .18s var(--apple-spring),box-shadow .22s var(--apple-ease),background-color .22s var(--apple-ease),border-color .22s var(--apple-ease)}
.btn-primary:active,.btn-ghost:active,.studio-replay a:active,.dock-item:active,.topnav button:active{transform:scale(.96)}
.apple-reveal{opacity:0;transform:translate3d(0,24px,0) scale(.985);transition:opacity .72s var(--apple-ease),transform .72s var(--apple-spring);will-change:transform,opacity}
.apple-reveal.is-visible{opacity:1;transform:none}
.apple-reveal:nth-child(2){transition-delay:50ms}.apple-reveal:nth-child(3){transition-delay:100ms}.apple-reveal:nth-child(4){transition-delay:150ms}
@media (min-width:761px){.hero-glass,.journey-studio,.section.bento-card{transform-origin:50% 20%}.apple-float{transition:transform .28s var(--apple-spring);will-change:transform}}
@media (max-width:760px){.hero h1{font-size:clamp(2.45rem,13vw,4rem);letter-spacing:-.055em}.hero-glass,.journey-studio,.section.bento-card{overflow:hidden}.apple-reveal{transform:translate3d(0,16px,0) scale(.99);transition-duration:.52s}}
@media (prefers-reduced-motion:reduce){.apple-reveal{opacity:1;transform:none;transition:none}.hero-glass:after,.journey-studio:after,.section.bento-card:after{display:none}.btn-primary,.btn-ghost,.studio-replay a,.dock-item,.topnav button,.topnav select{transition:none}}
<!-- APPLE_MOTION_V1_END -->
</style>'''

js = '''<script>
<!-- APPLE_MOTION_V1_START -->
(function(){
  const reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const revealTargets=[...document.querySelectorAll('.hero-glass,.journey-studio,.journey-studio .studio-panel,.section.bento-card,.folio,.skill-card,.pursuing-card')];
  revealTargets.forEach((el,i)=>{el.classList.add('apple-reveal');if(i%4===0)el.classList.add('apple-float');});
  if(reduce){revealTargets.forEach(el=>el.classList.add('is-visible'));return;}
  const io=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');io.unobserve(entry.target);}}),{threshold:.12,rootMargin:'0px 0px -8%'});
  revealTargets.forEach(el=>io.observe(el));
  if(window.innerWidth<761)return;
  let raf=0,px=0,py=0;
  const cards=[...document.querySelectorAll('.hero-glass,.journey-studio,.section.bento-card')];
  function paint(){raf=0;cards.forEach(card=>{const r=card.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;const x=Math.max(0,Math.min(1,(px-r.left)/Math.max(1,r.width)));const y=Math.max(0,Math.min(1,(py-r.top)/Math.max(1,r.height)));card.style.setProperty('--apple-x',(x*100).toFixed(1)+'%');card.style.setProperty('--apple-y',(y*100).toFixed(1)+'%');});}
  addEventListener('pointermove',e=>{px=e.clientX;py=e.clientY;if(!raf)raf=requestAnimationFrame(paint)},{passive:true});
})();
<!-- APPLE_MOTION_V1_END -->
</script>'''

html = html.replace('</head>', css + '\n</head>', 1)
html = html.replace('</body>', js + '\n</body>', 1)
path.write_text(html)
print('Apple motion layer applied')
