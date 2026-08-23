const fs = require('fs');
const vm = require('vm');
const index = fs.readFileSync('index.html', 'utf8');
const admin = fs.readFileSync('admin.html', 'utf8');
const checks = {
  guidedRemoved: !index.includes('id="journey-studio"') && !index.includes('PREMIUM_JOURNEY_STUDIO'),
  dayOption: index.includes('<option value="light">Day Mode</option>'),
  nightOption: index.includes('<option value="dark">Night Mode</option>'),
  oldThemeOptionsAbsent: !/<option value="(auto|morning|evening)">/.test(index),
  twoModeRuntime: index.includes('TWO-MODE THEME SYSTEM') && index.includes("theme === 'dark' ? 'dark' : 'light'"),
  phoneNightCss: index.includes('id="day-night-mode-v1"') && index.includes('color-scheme:dark') && index.includes('rgba(8,15,27,.94)'),
  premiumMotionRetained: index.includes('APPLE_MOTION_V1_START') && index.includes('STORY_MODE_SCRIPT_V1') && index.includes('fireflies') && index.includes('petal-field'),
  reducedMotion: /prefers-reduced-motion:\s*reduce/.test(index),
  cmsMergeFixPreserved: admin.includes('entriesForPublish') && !admin.includes('value.trim()||uploadedPhotoFilename'),
};
for (const [label, ok] of Object.entries(checks)) if (!ok) throw new Error(`Failed check: ${label}`);
for (const [file, text] of [['index.html', index], ['admin.html', admin]]) {
  const scripts = [...text.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/gi)].filter(m => !/src\s*=/.test(m[1]) && !/application\/ld\+json/i.test(m[1])).map(m => m[2]);
  scripts.forEach((body, i) => { try { new Function(body); } catch (e) { throw new Error(`${file} inline script ${i + 1}: ${e.message}`); } });
}
const ctx = {window: {}};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync('entries-data.js', 'utf8'), ctx);
for (const date of ['2026-08-18','2026-08-19','2026-08-20','2026-08-21']) {
  if (!(ctx.window.UNFILTERED_ENTRIES || []).some(e => e.date === date && e.journal)) throw new Error(`Journal date missing: ${date}`);
}
console.log(JSON.stringify({checks, result:'PASS'}, null, 2));
