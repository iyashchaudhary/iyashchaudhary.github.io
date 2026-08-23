const fs = require('fs');
const vm = require('vm');
const root = __dirname;

function loadEntries(file) {
  const context = {window: {}};
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(file, 'utf8'), context, {filename: file});
  return context.window.UNFILTERED_ENTRIES || [];
}

const currentFile = `${root}/entries-data.js`;
const currentText = fs.readFileSync(currentFile, 'utf8');
const header = currentText.slice(0, currentText.indexOf('const UNFILTERED_ENTRIES = '));
const current = loadEntries(currentFile);
const backup18 = loadEntries(`${root}/backups/2026-08-23T13-18-05-526Z-entries-data.js`).find(e => e.date === '2026-08-18');
const backup20 = loadEntries(`${root}/backups/2026-08-23T13-21-06-571Z-entries-data.js`).find(e => e.date === '2026-08-20');
if (!backup18 || !backup20) throw new Error('Protected backups do not contain both missing entries.');

const byDate = new Map(current.map(e => [e.date, e]));
byDate.set('2026-08-18', backup18);
byDate.set('2026-08-20', backup20);
for (const date of ['2026-08-18', '2026-08-19', '2026-08-20', '2026-08-21']) {
  const entry = byDate.get(date);
  if (!entry) throw new Error(`Entry ${date} is unavailable.`);
  // A thumbnail is opt-in. Scrapbook media remains independent and is not touched.
  delete entry.photo;
}
const repaired = [...byDate.values()].sort((a, b) => Number(a.day || 0) - Number(b.day || 0));
const output = `${header}const UNFILTERED_ENTRIES = ${JSON.stringify(repaired, null, 2)};\nwindow.UNFILTERED_ENTRIES = UNFILTERED_ENTRIES;\n`;
fs.writeFileSync(currentFile, output, 'utf8');
console.log(JSON.stringify(repaired.filter(e => ['2026-08-18','2026-08-19','2026-08-20','2026-08-21'].includes(e.date)).map(e => ({day:e.day,date:e.date,hasThumbnail:!!e.photo,photos:(e.photos||[]).length,videos:(e.videos||[]).length,journalLength:(e.journal||'').length})), null, 2));
