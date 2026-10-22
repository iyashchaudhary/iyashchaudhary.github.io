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
  let pointerTargetX = 0, pointerTargetY = 0, pointerX = 0, pointerY = 0;

  function paint() {
    queued = false;
    const y = Math.max(0, window.scrollY || window.pageYOffset || 0);
    const viewport = Math.max(1, window.innerHeight || 1);
    const isMobile = window.matchMedia('(max-width:760px), (pointer:coarse)').matches;
    document.body.classList.toggle('portfolio-scrolled', y > viewport * 0.55);
    document.body.classList.toggle('portfolio-detail-mode', y > (hero?.offsetHeight || viewport) * 0.78);

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
      pointerTargetX = pointerTargetY = pointerX = pointerY = 0;
      stage.style.setProperty('--parallax-x', '0px');
      stage.style.setProperty('--parallax-y', '0px');
      stage.style.setProperty('--parallax-depth-x', '0px');
      stage.style.setProperty('--parallax-depth-y', '0px');
      stage.style.setProperty('--parallax-depth-yaw', '0deg');
      stage.style.setProperty('--parallax-depth-pitch', '0deg');
      stage.style.setProperty('--scene-scroll-x', '0px');
      stage.style.setProperty('--scene-scroll-y', '0px');
      stage.style.setProperty('--scene-scroll-scale', '0');
      stage.style.setProperty('--scene-scroll-yaw', '0deg');
      stage.style.setProperty('--scene-scroll-pitch', '0deg');
      stage.style.setProperty('--parallax-yaw', '0deg');
      stage.style.setProperty('--parallax-pitch', '0deg');
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
    const sceneProgress = clamp(y / Math.max(1, document.documentElement.scrollHeight - viewport), 0, 1);
    const sceneSway = Math.sin(sceneProgress * Math.PI * 1.35);

    stage.style.setProperty('--sen-stage-progress', clamp(y / Math.max(viewport, hero?.offsetHeight || viewport), 0, 1).toFixed(4));
    stage.style.setProperty('--scene-scroll-x', `${(sceneSway * (isMobile ? 8 : 18)).toFixed(2)}px`);
    stage.style.setProperty('--scene-scroll-y', `${((sceneProgress - 0.5) * (isMobile ? 8 : 14)).toFixed(2)}px`);
    stage.style.setProperty('--scene-scroll-scale', `${(smooth(sceneProgress) * 0.02).toFixed(4)}`);
    stage.style.setProperty('--scene-scroll-yaw', `${(sceneSway * (isMobile ? 1.2 : 1.7)).toFixed(2)}deg`);
    stage.style.setProperty('--scene-scroll-pitch', `${(sceneSway * (isMobile ? 0.35 : 0.6)).toFixed(2)}deg`);
    stage.style.setProperty('--portrait-scale', scale.toFixed(4));
    stage.style.setProperty('--portrait-y', `${floatY.toFixed(2)}px`);
    stage.style.setProperty('--portrait-x', `${driftX.toFixed(2)}px`);
    stage.style.setProperty('--portrait-rz', `${tilt.toFixed(2)}deg`);
    stage.style.setProperty('--portrait-opacity', portraitOpacity.toFixed(3));
    stage.style.setProperty('--expression-opacity', expressionOpacity.toFixed(3));

    // Ease toward the pointer/touch target so the character feels like a separate 3D layer.
    const pointerEase = isMobile ? 0.16 : 0.12;
    pointerX += (pointerTargetX - pointerX) * pointerEase;
    pointerY += (pointerTargetY - pointerY) * pointerEase;
    stage.style.setProperty('--parallax-x', `${pointerX.toFixed(2)}px`);
    stage.style.setProperty('--parallax-y', `${pointerY.toFixed(2)}px`);
    stage.style.setProperty('--parallax-depth-x', `${(pointerX * 0.58).toFixed(2)}px`);
    stage.style.setProperty('--parallax-depth-y', `${(pointerY * 0.54).toFixed(2)}px`);
    stage.style.setProperty('--parallax-depth-yaw', `${(pointerX * (isMobile ? 0.05 : 0.047)).toFixed(2)}deg`);
    stage.style.setProperty('--parallax-depth-pitch', `${(-pointerY * 0.025).toFixed(2)}deg`);
    stage.style.setProperty('--parallax-yaw', `${(pointerX * (isMobile ? 0.12 : 0.13)).toFixed(2)}deg`);
    stage.style.setProperty('--parallax-pitch', `${(-pointerY * 0.06).toFixed(2)}deg`);
    if (Math.abs(pointerTargetX - pointerX) > 0.25 || Math.abs(pointerTargetY - pointerY) > 0.25) requestPaint();

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

  function moveParallax(clientX, clientY, mobile = false) {
    if (reduceMotion.matches) return;
    const nx = clamp((clientX / Math.max(1, window.innerWidth) - 0.5) * 2, -1, 1);
    const ny = clamp((clientY / Math.max(1, window.innerHeight) - 0.5) * 2, -1, 1);
    pointerTargetX = nx * (mobile ? 28 : 42);
    pointerTargetY = ny * (mobile ? 12 : 18);
    requestPaint();
  }
  function resetParallax() { pointerTargetX = pointerTargetY = 0; requestPaint(); }

  window.addEventListener('scroll', requestPaint, { passive: true });
  window.addEventListener('resize', requestPaint, { passive: true });
  window.addEventListener('pointermove', (event) => {
    if (event.pointerType === 'mouse') moveParallax(event.clientX, event.clientY, false);
  }, { passive: true });
  window.addEventListener('pointerleave', resetParallax, { passive: true });
  window.addEventListener('blur', resetParallax, { passive: true });
  window.addEventListener('touchmove', (event) => {
    const touch = event.touches && event.touches[0];
    if (touch) moveParallax(touch.clientX, touch.clientY, true);
  }, { passive: true });
  window.addEventListener('touchend', resetParallax, { passive: true });
  window.addEventListener('touchcancel', resetParallax, { passive: true });
  reduceMotion.addEventListener?.('change', requestPaint);
  requestPaint();
})();
