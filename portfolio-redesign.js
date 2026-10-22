/* Scroll-led portrait direction for Yash's portfolio. Native scrolling stays untouched. */
(() => {
  const stage = document.getElementById('sen-stage');
  const portrait = stage?.querySelector('.sen-stage-portrait');
  const hero = document.getElementById('hello');
  if (!stage || !portrait) return;

  const frames = Array.from(portrait.querySelectorAll('[data-portrait]'));
  const stickers = Array.from(stage.querySelectorAll('.sen-sticker'));
  if (!frames.length) return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const clamp = (value, min, max) => Math.max(min, Math.min(max, value));
  const smooth = (value) => {
    const t = clamp(value, 0, 1);
    return t * t * (3 - 2 * t);
  };
  let queued = false;

  function paint() {
    queued = false;
    const y = Math.max(0, window.scrollY || window.pageYOffset || 0);
    const viewport = Math.max(1, window.innerHeight || 1);
    const isMobile = window.matchMedia('(max-width:760px), (pointer:coarse)').matches;
    document.body.classList.toggle('portfolio-scrolled', y > viewport * 0.55);

    if (reduceMotion.matches) {
      frames.forEach((frame, index) => {
        const selected = index === 0;
        frame.classList.toggle('is-active', selected);
        frame.style.opacity = selected ? '1' : '0';
        frame.setAttribute('aria-hidden', 'true');
      });
      stage.style.setProperty('--portrait-scale', '0.94');
      stage.style.setProperty('--portrait-y', '0px');
      stage.style.setProperty('--portrait-x', '0px');
      stage.style.setProperty('--portrait-rz', '0deg');
      stage.style.setProperty('--portrait-opacity', '1');
      stage.style.setProperty('--expression-opacity', '0');
      stage.style.setProperty('--sticker-reveal', '0.7');
      stage.style.setProperty('--sticker-opacity', '0.7');
      return;
    }

    // Let the existing face artwork tell a short hello → focus → joy story in the hero.
    const expressionProgress = clamp(y / (viewport * 0.92), 0, 1) * (frames.length - 1);
    const first = Math.min(frames.length - 1, Math.floor(expressionProgress));
    const blend = expressionProgress - first;
    frames.forEach((frame, index) => {
      const opacity = index === first ? 1 - blend : index === first + 1 ? blend : 0;
      frame.classList.toggle('is-active', opacity > 0.025);
      frame.style.opacity = String(opacity);
      frame.setAttribute('aria-hidden', 'true');
    });

    // Start with the complete illustration; zoom toward the face during the first scroll beat,
    // then ease the portrait back so later content remains the focus.
    const zoomIn = smooth(y / (viewport * 0.94));
    const zoomOut = smooth((y - viewport * 0.9) / (viewport * 0.8));
    const maxZoom = isMobile ? 1.46 : 1.38;
    const scale = 0.94 + (maxZoom - 0.94) * zoomIn - (maxZoom - 1.04) * zoomOut;
    const fade = smooth((y - viewport * 0.9) / (viewport * 0.86));
    const portraitOpacity = 1 - fade * 0.74;
    const expressionIn = smooth(y / (viewport * 0.13));
    const expressionOut = smooth((y - viewport * 0.84) / (viewport * 0.42));
    const expressionOpacity = expressionIn * (1 - expressionOut);
    const floatY = (smooth(y / (viewport * 1.1)) - 0.2) * (isMobile ? -12 : -18);
    const driftX = Math.sin(clamp(y / (viewport * 1.2), 0, 1) * Math.PI) * (isMobile ? 5 : 13);
    const tilt = Math.sin(clamp(y / (viewport * 1.2), 0, 1) * Math.PI) * (isMobile ? 0.55 : 1.05);

    stage.style.setProperty('--sen-stage-progress', clamp(y / Math.max(viewport, hero?.offsetHeight || viewport), 0, 1).toFixed(4));
    stage.style.setProperty('--portrait-scale', scale.toFixed(4));
    stage.style.setProperty('--portrait-y', `${floatY.toFixed(2)}px`);
    stage.style.setProperty('--portrait-x', `${driftX.toFixed(2)}px`);
    stage.style.setProperty('--portrait-rz', `${tilt.toFixed(2)}deg`);
    stage.style.setProperty('--portrait-opacity', portraitOpacity.toFixed(3));
    stage.style.setProperty('--expression-opacity', expressionOpacity.toFixed(3));

    const stickerIn = 0.38 + 0.62 * smooth(y / (viewport * 0.44));
    const stickerOut = smooth((y - viewport * 1.0) / (viewport * 0.58));
    const stickerReveal = stickerIn * (1 - stickerOut * 0.82);
    const stickerOpacity = stickerReveal * portraitOpacity;
    stage.style.setProperty('--sticker-reveal', stickerReveal.toFixed(3));
    stage.style.setProperty('--sticker-opacity', stickerOpacity.toFixed(3));
    stickers.forEach((sticker, index) => {
      sticker.style.setProperty('--sticker-delay', `${index * 45}ms`);
    });
  }

  function requestPaint() {
    if (!queued) {
      queued = true;
      window.requestAnimationFrame(paint);
    }
  }

  window.addEventListener('scroll', requestPaint, { passive: true });
  window.addEventListener('resize', requestPaint, { passive: true });
  reduceMotion.addEventListener?.('change', requestPaint);
  requestPaint();
})();
