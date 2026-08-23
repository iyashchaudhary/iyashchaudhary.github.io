const fs = require('fs');
const vm = require('vm');

function loadEntries(file) {
  const context = {window: {}};
  vm.createContext(context);
  vm.runInContext(fs.readFileSync(file, 'utf8'), context, {filename: file});
  return context.window.UNFILTERED_ENTRIES || [];
}

const entries = loadEntries('entries-data.js');
for (const date of ['2026-08-18', '2026-08-19', '2026-08-20', '2026-08-21']) {
  const found = entries.find(e => e.date === date);
  if (!found) throw new Error(`Missing ${date}`);
  if (found.photo) throw new Error(`Unexpected thumbnail remains on ${date}`);
  if (!found.journal || found.journal.length < 100) throw new Error(`Journal text is incomplete on ${date}`);
}

for (const file of ['admin.html', 'unfiltered.html']) {
  const html = fs.readFileSync(file, 'utf8');
  const scripts = [...html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/gi)]
    .filter(m => !/src\s*=/.test(m[1]))
    .map(m => m[2]);
  scripts.forEach((body, i) => { try { new Function(body); } catch (e) { throw new Error(`${file} inline script ${i + 1}: ${e.message}`); } });
}

const admin = fs.readFileSync('admin.html', 'utf8');
const required = [
  'const photoSrc=document.getElementById(\'f-photo-src\').value.trim();',
  'const entriesForPublish = filename === \'entries-data.js\' ? parseEntriesSource(content) : null;',
  'const duplicate = entriesForPublish.findIndex(x => x.day === nextEntry.day || x.date === nextEntry.date);',
  'Date changed — previous thumbnail was cleared.',
];
for (const marker of required) if (!admin.includes(marker)) throw new Error(`Missing repair marker: ${marker}`);
if (admin.includes('value.trim()||uploadedPhotoFilename')) throw new Error('Legacy thumbnail fallback still present');

console.log(JSON.stringify({
  totalEntries: entries.length,
  recentEntries: entries.filter(e => e.date >= '2026-08-18').map(e => ({day:e.day,date:e.date,hasThumbnail:!!e.photo,journalLength:e.journal.length})),
  adminScripts: [...admin.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/gi)].filter(m => !/src\s*=/.test(m[1])).length,
  result: 'PASS'
}, null, 2));
