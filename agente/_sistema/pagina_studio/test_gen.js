// Collaudo indipendente del generatore: ricalcola ogni risposta a forza bruta leggendo il testo della domanda.
const GEN = require('./gen.js');
const sup = { '⁰': 0, '¹': 1, '²': 2, '³': 3, '⁴': 4, '⁵': 5, '⁶': 6, '⁷': 7, '⁸': 8, '⁹': 9 };
const sub = { '₀': 0, '₁': 1, '₂': 2, '₃': 3, '₄': 4, '₅': 5, '₆': 6, '₇': 7, '₈': 8, '₉': 9 };
const num = (s, m) => Number([...s].map(c => m[c]).join(''));
const gcd = (a, b) => (b ? gcd(b, a % b) : a);
const pl = t => { t = t.replace(/−/g, '-').replace(/\s+/g, ''); const k = t.match(/^(-?\d*)n([+-]\d+)?$/); if (k) return [k[1] === '' ? 1 : (k[1] === '-' ? -1 : +k[1]), k[2] ? +k[2] : 0]; return [0, +t]; };
let bad = 0, n = 0; const kinds = {};
function fail(q, why) { bad++; if (bad < 8) console.log('ERRORE', why, JSON.stringify(q, null, 1)); }
function check(q) {
  const txt = q.q, ans = q.o[q.a - 1];
  if (new Set(q.o).size !== 5) return fail(q, 'opzioni duplicate');
  if (q.a < 1 || q.a > 5) return fail(q, 'indice');
  let m;
  if ((m = txt.match(/Quante soluzioni modulo (\d+) ha la congruenza (\d+)X ≡ (\d+) mod/))) {
    const N = +m[1], a = +m[2], b = +m[3]; let c = 0; for (let x = 0; x < N; x++) if ((a * x - b) % N === 0) c++;
    if (String(c) !== ans) return fail(q, 'cong ' + c);
  } else if ((m = txt.match(/In ℤ([₀-₉]+) l'inverso moltiplicativo di \[(\d+)\] è/))) {
    const N = num(m[1], sub), a = +m[2]; let x = 0; for (let k = 1; k < N; k++) if ((a * k) % N === 1) x = k;
    if (String(x) !== ans) return fail(q, 'inverso ' + x);
  } else if ((m = txt.match(/φ\((\d+)\) =/)) || (m = txt.match(/generatori del gruppo additivo ℤ([₀-₉]+)/)) || (m = txt.match(/classi invertibili in \(ℤ([₀-₉]+)/))) {
    const N = m[1][0] >= '0' && m[1][0] <= '9' ? +m[1] : num(m[1], sub); let c = 0; for (let k = 1; k <= N; k++) if (gcd(k, N) === 1) c++;
    if (String(c) !== ans) return fail(q, 'phi ' + c);
  } else if ((m = txt.match(/non genera \(ℤ([₀-₉]+), \+\)/))) {
    const N = num(m[1], sub), k = +ans.slice(1, -1);
    if (gcd(k, N) === 1) return fail(q, 'nongen');
    for (const o of q.o) if (o !== ans && gcd(+o.slice(1, -1), N) !== 1) return fail(q, 'nongen: distrattore non coprimo');
  } else if ((m = txt.match(/In ℤ([₀-₉]+) la classe \[(\d+)\]([⁰¹²³⁴⁵⁶⁷⁸⁹]+) è/))) {
    const N = num(m[1], sub), a = +m[2], e = num(m[3], sup); let r = 1; for (let i = 0; i < e; i++) r = (r * a) % N;
    if (`[${r}]` !== ans) return fail(q, 'pow ' + r);
  } else if ((m = txt.match(/scrittura di (\d+) in base 2/))) {
    if (parseInt(ans, 2) !== +m[1]) return fail(q, 'base2');
  } else if ((m = txt.match(/\|A\| = (\d+) e \|B\| = (\d+)\. Quanti .* (\d+) elementi di A e (\d+) di B/))) {
    const [n1, n2, r, s] = m.slice(1).map(Number); const C = (n, k) => { let t = 1; for (let i = 1; i <= k; i++) t = (t * (n - k + i)) / i; return t; };
    const m2 = ans.match(/C\((\d+), (\d+)\) · C\((\d+), (\d+)\)/); if (!m2 || C(+m2[1], +m2[2]) * C(+m2[3], +m2[4]) !== C(n1, r) * C(n2, s) || +m2[1] !== n1 || +m2[3] !== n2) return fail(q, 'conteggio');
  } else if ((m = txt.match(/Sia π = ((?:\([\d ]+\))+) ∈ S([₀-₉]+)/))) {
    const N = num(m[2], sub), cycles = [...m[1].matchAll(/\(([\d ]+)\)/g)].map(x => x[1].split(' ').map(Number));
    const apply = x => { for (let i = cycles.length - 1; i >= 0; i--) { const c = cycles[i], j = c.indexOf(x); if (j >= 0) x = c[(j + 1) % c.length]; } return x; }; // destra→sinistra
    const pi = [0]; for (let x = 1; x <= N; x++) pi[x] = apply(x);
    const cyc = []; const seen = new Set();
    for (let x = 1; x <= N; x++) { if (seen.has(x)) continue; const c = []; let y = x; while (!seen.has(y)) { seen.add(y); c.push(y); y = pi[y]; } if (c.length > 1) cyc.push(c); }
    const typ = cyc.map(c => c.length).sort((a, b) => b - a); const ord = typ.reduce((a, l) => (a / gcd(a, l)) * l, 1);
    const par = typ.reduce((s, l) => s + l - 1, 0) % 2 === 0 ? 'pari' : 'dispari';
    if (/decomposizione di π in cicli disgiunti/.test(txt)) { const exp = cyc.length ? cyc.map(c => '(' + c.join(' ') + ')').join('') : '(id)'; if (exp !== ans) return fail(q, 'dec ' + exp); }
    else if (/Il tipo di π/.test(txt)) { if ('(' + (typ.length ? typ.join(', ') : '1') + ')' !== ans) return fail(q, 'tipo'); }
    else if (/Allora π$/.test(txt)) { if (ans !== `è ${par} ed ha periodo ${ord}`) return fail(q, 'pp'); }
    else if ((m = txt.match(/Allora π([⁰¹²³⁴⁵⁶⁷⁸⁹]+)\((\d+)\) =/))) { const k = num(m[1], sup); let x = +m[2]; for (let i = 0; i < k; i++) x = pi[x]; if (String(x) !== ans) return fail(q, 'pot'); }
    else return fail(q, 'perm non riconosciuta');
  } else if ((m = txt.match(/(\d+) amici ordinano .* tra (\d+) tipi/))) {
    const k = +m[1], t = +m[2]; if (ans !== `${t}${[...String(k)].map(d => '⁰¹²³⁴⁵⁶⁷⁸⁹'[d]).join('')}`) return fail(q, 'rip');
  } else if ((m = txt.match(/far sedere (\d+) persone in una fila di (\d+) sedie/))) {
    if (ans !== `${m[2]}!/${m[2] - m[1]}!`) return fail(q, 'sem');
  } else if ((m = txt.match(/^Siano f, g : ℤ → ℤ le funzioni f\(n\) = (.*) e g\(n\) = (.*)\. Allora \(g ∘ f\)\(n\) =$/))) {
    const F = pl(m[1]), G = pl(m[2]), R = pl(ans); for (let n = -6; n <= 6; n++) if (G[0] * (F[0] * n + F[1]) + G[1] !== R[0] * n + R[1]) return fail(q, 'comp');
  } else if ((m = txt.match(/^Sia f : ℝ → ℝ la funzione biettiva f\(x\) = (.*)\. Allora f⁻¹\((.*)\) =$/))) {
    const F = pl(m[1].replace(/x/g, 'n')), k = +m[2].replace('−', '-'), v = +ans.replace('−', '-'); if (F[0] * v + F[1] !== k) return fail(q, 'invaff');
  } else if ((m = txt.match(/^La funzione f : ℤ → ℤ, f\(n\) = (.*), è$/))) {
    const F = pl(m[1]), a = F[0]; const exp = a === 0 ? 'né iniettiva né suriettiva' : (Math.abs(a) === 1 ? 'iniettiva e suriettiva' : 'iniettiva ma non suriettiva');
    let inj = true, img = new Set(); for (let n = -50; n <= 50; n++) { const v = a * n + F[1]; if (img.has(v)) inj = false; img.add(v); } let sur = true; for (let t = -20; t <= 20; t++) if (!img.has(t)) sur = false;
    const real = !inj ? (sur ? 'suriettiva ma non iniettiva' : 'né iniettiva né suriettiva') : (sur ? 'iniettiva e suriettiva' : 'iniettiva ma non suriettiva');
    if (ans !== real || ans !== exp) return fail(q, 'class ' + real);
  } else if ((m = txt.match(/^Sia f : ℝ → ℝ, f\(x\) = x²\. Allora f⁻¹\(\[(\d+), (\d+)\]\) è$/))) {
    const lo = +m[1], hi = +m[2], iv = ans.split(' ∪ ').map(t => t.match(/\[(−?\d+), (−?\d+)\]/).slice(1).map(v => +v.replace('−', '-')));
    for (let x = -40; x <= 40; x += 0.25) { const inA = iv.some(([p, r]) => x >= p && x <= r), real = x * x >= lo && x * x <= hi; if (inA !== real) return fail(q, 'preim x=' + x); }
  } else if ((m = txt.match(/^Se \|A\| = (\d+) e \|B\| = (\d+), quanti elementi ha il prodotto cartesiano A × B\?$/))) { if (+ans !== m[1] * m[2]) return fail(q, 'prod'); }
  else if ((m = txt.match(/^Quanti sottoinsiemi \(vuoto e insieme stesso compresi\) ha un insieme di (\d+) elementi\?$/))) { if (+ans !== 2 ** +m[1]) return fail(q, 'parti'); }
  else if ((m = txt.match(/^Siano A = (.*) e B = (.*)\. Allora A (∪|∩|∖) B =$/))) {
    const ps = t => t === '∅' ? [] : t.replace(/[{}]/g, '').split(', ').map(Number), A = ps(m[1]), B = ps(m[2]); const U = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    const r = m[3] === '∪' ? U.filter(v => A.includes(v) || B.includes(v)) : m[3] === '∩' ? U.filter(v => A.includes(v) && B.includes(v)) : A.filter(v => !B.includes(v));
    if (ans !== (r.length ? '{' + r.join(', ') + '}' : '∅')) return fail(q, 'setop');
  } else return fail(q, 'domanda non riconosciuta: ' + txt);
}
for (let i = 0; i < 6000; i++) { const q = GEN.make(); if (!q) { fail({ q: 'null' }, 'null'); continue; } n++; kinds[q.args[0]] = (kinds[q.args[0]] || 0) + 1; check(q); }
console.log(`${n} domande generate, ${bad} errori`, kinds);

// ---------- Algebra lineare e Fondamenti ----------
const supd = s => Number([...s].map(c => '⁰¹²³⁴⁵⁶⁷⁸⁹'.indexOf(c)).join(''));
const pc = s => { // "3 − 2i", "−i", "5", "i" -> [re, im]
  s = s.replace(/−/g, '-').replace(/\s+/g, '').replace(/^\(|\)$/g, '');
  const m = s.match(/^(-?\d+)?(?:([+-])(\d*)i)?$/); if (m && (m[1] !== undefined || m[2])) return [m[1] ? +m[1] : 0, m[2] ? (m[2] === '-' ? -1 : 1) * (m[3] === '' ? 1 : +m[3]) : 0];
  const k = s.match(/^(-?)(\d*)i$/); if (k) return [0, (k[1] ? -1 : 1) * (k[2] === '' ? 1 : +k[2])];
  throw new Error('cx? ' + s);
};
const mul = (p, q) => [p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0]];
const eq = (p, q) => Math.abs(p[0] - q[0]) < 1e-9 && Math.abs(p[1] - q[1]) < 1e-9;
function checkAlg(q) {
  const t = q.q, ans = q.o[q.a - 1]; let m;
  if (new Set(q.o).size !== 5) return fail(q, 'alg opzioni duplicate');
  if ((m = t.match(/^Il prodotto \((.*)\)·\((.*)\) è$/))) { if (!eq(mul(pc(m[1]), pc(m[2])), pc(ans))) return fail(q, 'mul'); }
  else if ((m = t.match(/^Il quoziente \((.*)\) \/ \((.*)\) è$/))) { if (!eq(mul(pc(ans), pc(m[2])), pc(m[1]))) return fail(q, 'div'); }
  else if ((m = t.match(/^Il modulo di z = (.*) è$/))) { const z = pc(m[1]); if (Math.abs(Math.hypot(z[0], z[1]) - +ans) > 1e-9) return fail(q, 'mod'); }
  else if ((m = t.match(/^L'inverso moltiplicativo di z = (.*) è$/))) { const mm = ans.match(/^\((.*)\)\/(\d+)$/); const w = pc(mm[1]); w[0] /= +mm[2]; w[1] /= +mm[2]; if (!eq(mul(pc(m[1]), w), [1, 0])) return fail(q, 'inv'); }
  else if ((m = t.match(/^Il valore di i([⁰¹²³⁴⁵⁶⁷⁸⁹]+) è$/))) { let z = [1, 0]; for (let i = 0; i < supd(m[1]); i++) z = mul(z, [0, 1]); if (!eq(z, pc(ans === '0' ? '0' : ans))) return fail(q, 'ipow'); }
  else if ((m = t.match(/^\((.*)\)² =$/))) { const z = pc(m[1]); if (!eq(mul(z, z), pc(ans))) return fail(q, 'sq'); }
  else if ((m = t.match(/^Quanto vale \(1 \+ i\)([⁰¹²³⁴⁵⁶⁷⁸⁹]+)\?$/))) { let z = [1, 0]; for (let i = 0; i < supd(m[1]); i++) z = mul(z, [1, 1]); if (!eq(z, [+ans.replace('−', '-'), 0])) return fail(q, '1+i'); }
  else return fail(q, 'alg non riconosciuta: ' + t);
}
const tc = s => { const v = s.replace(/−/g, '-'); return +v; };
function checkFond(q) {
  const t = q.q, ans = q.o[q.a - 1]; let m;
  if (new Set(q.o).size !== 5) return fail(q, 'fond opzioni duplicate');
  if ((m = t.match(/^Il numero binario ([01]+) vale in decimale$/))) { if (parseInt(m[1], 2) !== +ans) return fail(q, 'bin2dec'); }
  else if ((m = t.match(/^Il numero decimale (\d+) in esadecimale è$/))) { if (parseInt(ans, 16) !== +m[1] || ans !== ans.toUpperCase()) return fail(q, 'dec2hex'); }
  else if ((m = t.match(/^Il numero esadecimale ([0-9A-F]+) vale in decimale$/))) { if (parseInt(m[1], 16) !== +ans) return fail(q, 'hex2dec'); }
  else if ((m = t.match(/^In complemento a due su 8 bit, −(\d+) si scrive$/))) { const v = parseInt(ans, 2); if (ans.length !== 8 || ((v + +m[1]) & 255) !== 0) return fail(q, 'c2 neg'); }
  else if ((m = t.match(/^Il pattern ([01]{8}), letto in complemento a due su 8 bit, rappresenta il numero$/))) { let v = parseInt(m[1], 2); if (v > 127) v -= 256; if (v !== tc(ans)) return fail(q, 'c2 pos'); }
  else if ((m = t.match(/^Qual è la distanza di Hamming tra ([01]+) e ([01]+)\?$/))) { let d = 0; for (let i = 0; i < m[1].length; i++) if (m[1][i] !== m[2][i]) d++; if (d !== +ans) return fail(q, 'hamming'); }
  else if ((m = t.match(/^Aggiungendo in fondo un bit di parità pari al pattern ([01]+), si ottiene$/))) { const ones = [...ans].filter(c => c === '1').length; if (!ans.startsWith(m[1]) || ans.length !== m[1].length + 1 || ones % 2 !== 0) return fail(q, 'parita'); }
  else if ((m = t.match(/^Una memoria principale ha indirizzi di (\d+) bit e celle da 1 byte\. Quante celle ha\?$/))) { if (!ans.endsWith('= ' + 2 ** +m[1])) return fail(q, 'celle'); }
  else if ((m = t.match(/^Quanti bit servono per indirizzare (\d+) celle di memoria\?$/))) { if (2 ** +ans !== +m[1]) return fail(q, 'bit indirizzi'); }
  else if ((m = t.match(/scrittura di (\d+) in base 2/))) { if (parseInt(ans, 2) !== +m[1]) return fail(q, 'base2'); }
  else return fail(q, 'fond non riconosciuta: ' + t);
}
let na = 0, nf = 0;
for (let i = 0; i < 4000; i++) { const q = GEN.make('Algebra lineare'); if (!q) { fail({ q: 'null' }, 'alg null'); continue; } na++; checkAlg(q); }
for (let i = 0; i < 4000; i++) { const q = GEN.make('Fondamenti Info'); if (!q) { fail({ q: 'null' }, 'fond null'); continue; } nf++; checkFond(q); }
console.log(`Algebra: ${na}, Fondamenti: ${nf} domande generate; errori totali ${bad}; Programmazione generabile: ${GEN.disponibile('Programmazione')}`);
process.exit(bad ? 1 : 0);
