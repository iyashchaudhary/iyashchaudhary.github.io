const fs = require('fs');
const vm = require('vm');

const index = fs.readFileSync('index.html', 'utf8');
const admin = fs.readFileSync('admin.html', 'utf8');
const checks = {
  journeyStudioMarkup: index.includes('id="journey-studio"'),
  journeyStudioCss: index.includes('PREMIUM_JOURNEY_STUDIO_V1'),
  journeyStudioScript: index.includes('PREMIUM_JOURNEY_STUDIO_SCRIPT_V1'),
  appleMotion: index.includes('APPLE_MOTION_V1_START') && index.includes('APPLE_MOTION_V1_END'),
  storyMode: index.includes('STORY_MODE_SCRIPT_V1'),
  ambientDecor: index.includes('AMBIENT BACKGROUND DECOR') && index.includes('fireflies') && index.includes('petal-field'),
  backgroundParallax: index.includes('Mesh background — gentle mouse parallax'),
  performanceCleanupAbsent: !index.includes('PERFORMANCE_CLEANUP_V1') && !index.includes('performance-cleanup-v2'),
  reducedMotion: index.includes('prefers-reduced-motion:reduce') || index.includes('prefers-reduced-motion: reduce'),
  currentAdminFix: admin.includes('entriesForPublish') && !admin.includes('value.trim()||uploadedPhotoFilename'),
};
for (const [label, ok] of Object.entries(checks)) if (!ok) throw new Error(`Failed restoration check: ${label}`);

for (const [file, text] of [['index.html', index], ['admin.html', admin]]) {
  const scripts = [...text.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/gi)].filter(m => !/src\s*=/.test(m[1]) && !/application\/ld\+json/i.test(m[1])).map(m => m[2]);
  scripts.forEach((body, i) => { try { new Function(body); } catch (e) { throw new Error(`${file} inline script ${i + 1}: ${e.message}`); } });
}

const context = {window: {}};
vm.createContext(context);
vm.runInContext(fs.readFileSync('entries-data.js', 'utf8'), context);
const dates = ['2026-08-18','2026-08-19','2026-08-20','2026-08-21'];
for (const date of dates) {
  const entry = (context.window.UNFILTERED_ENTRIES || []).find(e => e.date === date);
  if (!entry || !entry.journal) throw new Error(`Journal data missing after restoration: ${date}`);
}
console.log(JSON.stringify({checks, recentJournalDates: dates, result:'PASS'}, null, 2));
