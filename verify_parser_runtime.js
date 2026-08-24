const fs = require('fs');
const vm = require('vm');
const admin = fs.readFileSync('admin.html', 'utf8');
const match = admin.match(/function parseEntriesSource\(raw\)\{([\s\S]*?)\n  \}\n  async function githubJson/);
if (!match) throw new Error('parseEntriesSource function not found');
const parser = new Function('return function parseEntriesSource(raw){' + match[1] + '\n  }')();
const raw = fs.readFileSync('entries-data.js', 'utf8');
const entries = parser(raw);
if (!Array.isArray(entries) || entries.length !== 8) throw new Error('Parser did not return all 8 entries');
for (const date of ['2026-08-18','2026-08-19','2026-08-20','2026-08-21']) {
  const entry = entries.find(e => e.date === date);
  if (!entry || !entry.journal || entry.photo) throw new Error(`Invalid parsed entry ${date}`);
}
console.log(JSON.stringify({result:'PASS', count:entries.length, dates:entries.filter(e=>e.date>='2026-08-18').map(e=>({date:e.date,chars:e.journal.length,thumbnail:!!e.photo}))}, null, 2));
