// Collaudo indipendente del generatore: ricalcola ogni risposta a forza bruta leggendo il testo della domanda.
const GEN = require('./gen.js');
const sup = { '⁰': 0, '¹': 1, '²': 2, '³': 3, '⁴': 4, '⁵': 5, '⁶': 6, '⁷': 7, '⁸': 8, '⁹': 9 };
const sub = { '₀': 0, '₁': 1, '₂': 2, '₃': 3, '₄': 4, '₅': 5, '₆': 6, '₇': 7, '₈': 8, '₉': 9 };
const num = (s, m) => Number([...s].map(c => m[c]).join(''));
const gcd = (a, b) => (b ? gcd(b, a % b) : a);
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
  } else return fail(q, 'domanda non riconosciuta: ' + txt);
}
for (let i = 0; i < 6000; i++) { const q = GEN.make(); if (!q) { fail({ q: 'null' }, 'null'); continue; } n++; kinds[q.args[0]] = (kinds[q.args[0]] || 0) + 1; check(q); }
console.log(`${n} domande generate, ${bad} errori`, kinds);
process.exit(bad ? 1 : 0);
