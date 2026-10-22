/* Scroll-led portrait direction and accessible character motion for Yash's portfolio. */
(() => {
  const stage = document.getElementById('sen-stage');
  const portrait = stage?.querySelector('.sen-stage-portrait');
  const hero = document.getElementById('hello');
  const bodyLayer = stage?.querySelector('.sen-stage-body');
  const gestureVideo = stage?.querySelector('.sen-stage-gesture-source');
  const gestureCanvas = stage?.querySelector('.sen-stage-gesture-canvas');
  if (!stage || !portrait) return;

  const frames = Array.from(portrait.querySelectorAll('[data-portrait]'));
  const stickers = Array.from(stage.querySelectorAll('.sen-sticker'));
  const closeupFrames = Array.from(stage.querySelectorAll('.sen-stage-closeup [data-scene-portrait]'));
  const chapters = Array.from(document.querySelectorAll('#main-content .section[data-scene]'));
  if (!frames.length) return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const clamp = (value, min, max) => Math.max(min, Math.min(max, value));
  const smooth = (value) => {
    const t = clamp(value, 0, 1);
    return t * t * (3 - 2 * t);
  };
  const SCENES = {
    'yash-os':      { portrait: 'curious',   x: -4.8, y: -1.8, scale: 1.10, roll: -1.2 },
    'currently':    { portrait: 'surprised', x:  4.6, y: -3.2, scale: 1.08, roll:  1.4 },
    'journey':      { portrait: 'cheeky',    x: -2.2, y:  1.1, scale: 1.16, roll: -2.0 },
    'experience':   { portrait: 'curious',   x:  3.8, y: -2.2, scale: 1.06, roll:  1.0 },
    'focus':        { portrait: 'surprised', x: -4.0, y:  1.4, scale: 1.18, roll: -1.6 },
    'credentials':  { portrait: 'cheeky',    x:  4.5, y: -1.6, scale: 1.12, roll:  1.8 },
    'skills':       { portrait: 'curious',   x: -3.2, y:  0.4, scale: 1.08, roll: -0.8 },
    'contact':      { portrait: 'surprised', x:  3.2, y: -2.4, scale: 1.12, roll:  1.3 }
  };

  let queued = false;
  let pointerTargetX = 0, pointerTargetY = 0, pointerX = 0, pointerY = 0;
  let idleRaf = 0;
  let idleStartedAt = performance.now();
  let activeScene = '';
  let gestureGL = null;
  let gestureTexture = null;
  let gestureProgram = null;
  let gestureRenderRaf = 0;
  let gesturePlaying = false;
  let motionReady = false;
  let gestureVideoFrame = 0;
  let lastSceneCheck = 0;
  let lastPaintAt = 0;
  let cameraCurrent = { ...SCENES['yash-os'] };
  let cameraTarget = { ...SCENES['yash-os'] };
  let lastGestureTime = -1;
  let scrollStopTimer = 0;
  let cachedHeroHeight = hero?.offsetHeight || window.innerHeight;

  function clearIdleMotion() {
    stage.style.setProperty('--idle-x', '0px');
    stage.style.setProperty('--idle-y', '0px');
    stage.style.setProperty('--idle-tilt', '0deg');
    stage.style.setProperty('--idle-breath', '1');
    stage.style.setProperty('--idle-face-x', '0px');
    stage.style.setProperty('--idle-face-y', '0px');
    stage.style.setProperty('--idle-face-scale', '0');
    stage.style.setProperty('--idle-face-yaw', '0deg');
    stage.style.setProperty('--idle-face-pitch', '0deg');
    stage.style.setProperty('--idle-face-roll', '0deg');
  }

  function idleMotion(now) {
    idleRaf = 0;
    if (reduceMotion.matches || document.visibilityState === 'hidden' || document.body.classList.contains('portfolio-detail-mode')) {
      clearIdleMotion();
      return;
    }
    const t = (now - idleStartedAt) / 1000;
    const homeStrength = document.body.classList.contains('portfolio-detail-mode') ? 0.18 : 1;
    stage.style.setProperty('--idle-x', `${(Math.sin(t * 0.43) * 1.8 * homeStrength).toFixed(2)}px`);
    stage.style.setProperty('--idle-y', `${(Math.sin(t * 0.82) * 2.8 * homeStrength).toFixed(2)}px`);
    stage.style.setProperty('--idle-tilt', `${(Math.sin(t * 0.36) * 0.36 * homeStrength).toFixed(2)}deg`);
    stage.style.setProperty('--idle-breath', `${(1 + Math.sin(t * 1.12) * 0.0028).toFixed(4)}`);
    stage.style.setProperty('--idle-face-x', `${(Math.sin(t * 0.27) * 4.5).toFixed(2)}px`);
    stage.style.setProperty('--idle-face-y', `${(Math.cos(t * 0.32) * 3.5).toFixed(2)}px`);
    stage.style.setProperty('--idle-face-scale', `${(Math.sin(t * 0.29) * 0.008).toFixed(4)}`);
    stage.style.setProperty('--idle-face-yaw', `${(Math.sin(t * 0.25) * 0.42).toFixed(2)}deg`);
    stage.style.setProperty('--idle-face-pitch', `${(Math.cos(t * 0.31) * 0.28).toFixed(2)}deg`);
    stage.style.setProperty('--idle-face-roll', `${(Math.sin(t * 0.22) * 0.24).toFixed(2)}deg`);
    idleRaf = window.requestAnimationFrame(idleMotion);
  }

  function startIdleMotion() {
    if (!idleRaf && !reduceMotion.matches && document.visibilityState !== 'hidden') {
      idleStartedAt = performance.now();
      idleRaf = window.requestAnimationFrame(idleMotion);
    }
  }

  function stopIdleMotion() {
    if (idleRaf) window.cancelAnimationFrame(idleRaf);
    idleRaf = 0;
    clearIdleMotion();
  }

  function compileShader(gl, type, source) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
      const error = gl.getShaderInfoLog(shader) || 'shader compilation failed';
      gl.deleteShader(shader);
      throw new Error(error);
    }
    return shader;
  }

  function setupGestureRenderer() {
    if (!gestureVideo || !gestureCanvas) return false;
    try {
      const gl = gestureCanvas.getContext('webgl', {
        alpha: true,
        premultipliedAlpha: false,
        preserveDrawingBuffer: false,
        antialias: false
      });
      if (!gl) return false;
      const vertexSource = 'attribute vec2 a_position; attribute vec2 a_uv; varying vec2 v_uv; void main(){ gl_Position=vec4(a_position,0.0,1.0); v_uv=a_uv; }';
      const fragmentSource = `
        precision mediump float;
        uniform sampler2D u_video;
        varying vec2 v_uv;
        void main(){
          vec4 sampleColor = texture2D(u_video, v_uv);
          vec3 color = sampleColor.rgb;
          float greenDominance = min(color.g - color.r * 1.16, color.g - color.b * 1.10);
          float key = smoothstep(0.045, 0.19, greenDominance);
          float alpha = 1.0 - key;
          float edgeDespill = smoothstep(0.008, 0.15, greenDominance);
          float neutralGreen = min(color.g, max(color.r, color.b) + 0.035);
          color.g = mix(color.g, neutralGreen, edgeDespill * 0.94);
          gl_FragColor = vec4(color, alpha);
        }`;
      const vertex = compileShader(gl, gl.VERTEX_SHADER, vertexSource);
      const fragment = compileShader(gl, gl.FRAGMENT_SHADER, fragmentSource);
      const program = gl.createProgram();
      gl.attachShader(program, vertex);
      gl.attachShader(program, fragment);
      gl.linkProgram(program);
      if (!gl.getProgramParameter(program, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(program) || 'program link failed');
      gl.useProgram(program);

      const vertices = new Float32Array([
        -1, -1, 0, 1,  1, -1, 1, 1,
        -1,  1, 0, 0,  1,  1, 1, 0
      ]);
      const buffer = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
      gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
      const position = gl.getAttribLocation(program, 'a_position');
      const uv = gl.getAttribLocation(program, 'a_uv');
      gl.enableVertexAttribArray(position);
      gl.vertexAttribPointer(position, 2, gl.FLOAT, false, 16, 0);
      gl.enableVertexAttribArray(uv);
      gl.vertexAttribPointer(uv, 2, gl.FLOAT, false, 16, 8);

      const texture = gl.createTexture();
      gl.activeTexture(gl.TEXTURE0);
      gl.bindTexture(gl.TEXTURE_2D, texture);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      gl.uniform1i(gl.getUniformLocation(program, 'u_video'), 0);
      gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);
      gl.clearColor(0, 0, 0, 0);
      gl.viewport(0, 0, gestureCanvas.width, gestureCanvas.height);
      gl.clear(gl.COLOR_BUFFER_BIT);

      gestureGL = gl;
      gestureProgram = program;
      gestureTexture = texture;
      return true;
    } catch (error) {
      console.warn('Character motion renderer unavailable; using the still illustration.', error);
      return false;
    }
  }

  function drawGestureFrame() {
    gestureRenderRaf = 0;
    gestureVideoFrame = 0;
    if (!gesturePlaying || !gestureGL || !gestureVideo || document.visibilityState === 'hidden' || reduceMotion.matches) return;
    if (gestureVideo.readyState >= HTMLMediaElement.HAVE_CURRENT_DATA && gestureVideo.currentTime !== lastGestureTime) {
      lastGestureTime = gestureVideo.currentTime;
      try {
        gestureGL.useProgram(gestureProgram);
        gestureGL.activeTexture(gestureGL.TEXTURE0);
        gestureGL.bindTexture(gestureGL.TEXTURE_2D, gestureTexture);
        gestureGL.pixelStorei(gestureGL.UNPACK_FLIP_Y_WEBGL, false);
        gestureGL.texImage2D(gestureGL.TEXTURE_2D, 0, gestureGL.RGBA, gestureGL.RGBA, gestureGL.UNSIGNED_BYTE, gestureVideo);
        gestureGL.viewport(0, 0, gestureCanvas.width, gestureCanvas.height);
        gestureGL.drawArrays(gestureGL.TRIANGLE_STRIP, 0, 4);
        if (!motionReady) {
          motionReady = true;
          bodyLayer?.classList.add('is-motion-ready');
        }
      } catch (error) {
        console.warn('Character motion frame could not be rendered.', error);
      }
    }
    if (typeof gestureVideo.requestVideoFrameCallback === 'function') {
      gestureVideoFrame = gestureVideo.requestVideoFrameCallback(drawGestureFrame);
    } else {
      gestureRenderRaf = window.requestAnimationFrame(drawGestureFrame);
    }
  }

  function setGesturePlayback(shouldPlay) {
    const active = Boolean(shouldPlay && gestureGL && gestureVideo && !reduceMotion.matches && document.visibilityState !== 'hidden');
    if (active === gesturePlaying) return;
    gesturePlaying = active;
    if (!active) {
      if (gestureRenderRaf) window.cancelAnimationFrame(gestureRenderRaf);
      if (gestureVideoFrame && typeof gestureVideo?.cancelVideoFrameCallback === 'function') gestureVideo.cancelVideoFrameCallback(gestureVideoFrame);
      gestureRenderRaf = 0;
      gestureVideoFrame = 0;
      gestureVideo?.pause();
      lastGestureTime = -1;
      motionReady = false;
      bodyLayer?.classList.remove('is-motion-ready');
      return;
    }
    const playPromise = gestureVideo.play();
    if (playPromise && typeof playPromise.catch === 'function') {
      playPromise.catch(() => {
        gesturePlaying = false;
        motionReady = false;
        bodyLayer?.classList.remove('is-motion-ready');
      });
    }
    if (typeof gestureVideo.requestVideoFrameCallback === 'function') {
      if (!gestureVideoFrame) gestureVideoFrame = gestureVideo.requestVideoFrameCallback(drawGestureFrame);
    } else if (!gestureRenderRaf) {
      gestureRenderRaf = window.requestAnimationFrame(drawGestureFrame);
    }
  }

  function setChapterScene(id) {
    const config = SCENES[id] || SCENES['yash-os'];
    if (id === activeScene) return;
    activeScene = id;
    stage.dataset.activeScene = id;
    closeupFrames.forEach((frame) => frame.classList.toggle('is-active', frame.dataset.scenePortrait === config.portrait));
    cameraTarget = config;
  }

  function updateChapterScene(viewport) {
    if (!chapters.length) return;
    const anchorY = viewport * 0.46;
    const anchorX = window.innerWidth * 0.5;
    let chosen = null;
    let bestScore = Infinity;
    let currentScore = Infinity;
    chapters.forEach((chapter) => {
      const rect = chapter.getBoundingClientRect();
      if (rect.bottom <= 0 || rect.top >= viewport) return;
      const dy = anchorY < rect.top ? rect.top - anchorY : anchorY > rect.bottom ? anchorY - rect.bottom : 0;
      const centerX = rect.left + rect.width / 2;
      const dx = Math.abs(centerX - anchorX) * 0.22;
      const score = dy + dx;
      if ((chapter.dataset.scene || chapter.id) === activeScene) currentScore = score;
      if (score < bestScore) { bestScore = score; chosen = chapter; }
    });
    if (chosen) {
      const nextId = chosen.dataset.scene || chosen.id;
      const switchMargin = Math.min(92, Math.max(42, viewport * 0.075));
      if (activeScene && nextId !== activeScene && currentScore < Infinity && bestScore + switchMargin >= currentScore) return;
      setChapterScene(nextId);
    }
  }

  function paint() {
    queued = false;
    const now = performance.now();
    const y = Math.max(0, window.scrollY || window.pageYOffset || 0);
    const viewport = Math.max(1, window.innerHeight || 1);
    const isMobile = window.matchMedia('(max-width:760px), (pointer:coarse)').matches;
    document.body.classList.toggle('portfolio-scrolled', y > viewport * 0.55);
    const detailMode = y > cachedHeroHeight * 0.78;
    document.body.classList.toggle('portfolio-detail-mode', detailMode);
    if (detailMode) { if (idleRaf) stopIdleMotion(); }
    else if (!idleRaf && !reduceMotion.matches) startIdleMotion();
    if (!activeScene || now - lastSceneCheck >= 72) {
      updateChapterScene(viewport);
      lastSceneCheck = now;
    }
    const frameDelta = Math.min(50, lastPaintAt ? now - lastPaintAt : 16.7);
    lastPaintAt = now;
    const cameraEase = reduceMotion.matches ? 1 : 1 - Math.exp(-frameDelta / 190);
    let cameraMoving = false;
    ['x', 'y', 'scale', 'roll'].forEach((key) => {
      const difference = cameraTarget[key] - cameraCurrent[key];
      if (Math.abs(difference) > 0.012) {
        cameraCurrent[key] += difference * cameraEase;
        cameraMoving = true;
      } else {
        cameraCurrent[key] = cameraTarget[key];
      }
    });
    stage.style.setProperty('--chapter-camera-x', `${cameraCurrent.x.toFixed(3)}vw`);
    stage.style.setProperty('--chapter-camera-y', `${cameraCurrent.y.toFixed(3)}vh`);
    stage.style.setProperty('--chapter-camera-scale', cameraCurrent.scale.toFixed(4));
    stage.style.setProperty('--chapter-camera-roll', `${cameraCurrent.roll.toFixed(3)}deg`);
    if (cameraMoving && !reduceMotion.matches) requestPaint();

    const heroRect = hero?.getBoundingClientRect();
    const heroVisible = Boolean(heroRect && heroRect.bottom > 0 && heroRect.top < viewport && !document.body.classList.contains('portfolio-detail-mode'));
    setGesturePlayback(heroVisible);

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

    // The first scroll beat still transitions hello → focus → joy over the full-body artwork.
    const expressionProgress = clamp(y / (viewport * 0.92), 0, 1) * (frames.length - 1);
    const first = Math.min(frames.length - 1, Math.floor(expressionProgress));
    const blend = expressionProgress - first;
    frames.forEach((frame, index) => {
      const opacity = index === first ? 1 - blend : index === first + 1 ? blend : 0;
      frame.classList.toggle('is-active', opacity > 0.025);
      frame.style.opacity = String(opacity);
      frame.setAttribute('aria-hidden', 'true');
    });

    // Ease from the complete figure into a clean, face-first close-up during the first scroll beat.
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

    stage.style.setProperty('--sen-stage-progress', clamp(y / Math.max(viewport, cachedHeroHeight || viewport), 0, 1).toFixed(4));
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

    // Inertial pointer/touch parallax remains independent from the scroll-directed face camera.
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
    stickers.forEach((sticker, index) => sticker.style.setProperty('--sticker-delay', `${index * 45}ms`));
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

  function handleScroll() {
    document.body.classList.add('portfolio-scrolling');
    window.clearTimeout(scrollStopTimer);
    scrollStopTimer = window.setTimeout(() => {
      document.body.classList.remove('portfolio-scrolling');
      scrollStopTimer = 0;
    }, 150);
    requestPaint();
  }
  function handleResize() {
    cachedHeroHeight = hero?.offsetHeight || window.innerHeight;
    requestPaint();
  }

  if (!setupGestureRenderer()) bodyLayer?.classList.remove('is-motion-ready');
  window.addEventListener('scroll', handleScroll, { passive: true });
  window.addEventListener('resize', handleResize, { passive: true });
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
  reduceMotion.addEventListener?.('change', () => {
    if (reduceMotion.matches) { stopIdleMotion(); setGesturePlayback(false); }
    else { startIdleMotion(); requestPaint(); }
    requestPaint();
  });
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') { stopIdleMotion(); setGesturePlayback(false); }
    else { startIdleMotion(); requestPaint(); }
  });
  startIdleMotion();
  requestPaint();
})();
