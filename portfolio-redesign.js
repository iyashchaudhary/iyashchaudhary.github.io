/* Scroll-led portrait direction for Yash's portfolio. Native scrolling stays untouched. */
(() => {
  const stage = document.getElementById('sen-stage');
  const portrait = stage?.querySelector('.sen-stage-portrait');
  if (!stage || !portrait) return;

  const frames = Array.from(portrait.querySelectorAll('[data-portrait]'));
  if (!frames.length) return;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const clamp = (n, min, max) => Math.max(min, Math.min(max, n));
  let queued = false;

  function paint() {
    queued = false;
    const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    const progress = clamp(window.scrollY / maxScroll, 0, 1);
    const framePosition = progress * (frames.length - 1);
    const first = Math.floor(framePosition);
    const blend = framePosition - first;

    frames.forEach((frame, index) => {
      const opacity = index === first ? 1 - blend : index === first + 1 ? blend : 0;
      frame.classList.toggle('is-active', opacity > 0.02);
      frame.style.opacity = String(opacity);
      frame.setAttribute('aria-hidden', 'true');
    });

    stage.style.setProperty('--sen-stage-progress', progress.toFixed(4));
    if (!reduceMotion.matches) {
      const eased = progress * progress * (3 - 2 * progress);
      const mobile = window.matchMedia('(max-width:760px), (pointer:coarse)').matches;
      stage.style.setProperty('--portrait-scale', (0.91 + eased * (mobile ? 0.27 : 0.35)).toFixed(4));
      stage.style.setProperty('--portrait-y', `${(progress - 0.48) * (mobile ? -28 : -72)}px`);
      stage.style.setProperty('--portrait-x', `${Math.sin(progress * Math.PI * 1.35) * (mobile ? 5 : 24)}px`);
      stage.style.setProperty('--portrait-rz', `${Math.sin(progress * Math.PI * 1.7) * (mobile ? 1.2 : 2.4)}deg`);
      stage.style.setProperty('--portrait-ry', `${Math.sin(progress * Math.PI) * (mobile ? 0 : 8)}deg`);
      stage.style.setProperty('--portrait-rx', `${Math.sin(progress * Math.PI * 1.3) * (mobile ? 0 : -3)}deg`);
    } else {
      frames.forEach((frame, index) => {
        const selected = index === 0;
        frame.classList.toggle('is-active', selected);
        frame.style.opacity = selected ? '1' : '0';
      });
      stage.style.setProperty('--portrait-scale', '1');
      stage.style.setProperty('--portrait-y', '0px');
      stage.style.setProperty('--portrait-x', '0px');
      stage.style.setProperty('--portrait-rz', '0deg');
      stage.style.setProperty('--portrait-ry', '0deg');
      stage.style.setProperty('--portrait-rx', '0deg');
    }
  }

  function requestPaint() {
    if (!queued) {
      queued = true;
      requestAnimationFrame(paint);
    }
  }

  window.addEventListener('scroll', requestPaint, { passive: true });
  window.addEventListener('resize', requestPaint, { passive: true });
  reduceMotion.addEventListener?.('change', requestPaint);
  requestPaint();
})();
