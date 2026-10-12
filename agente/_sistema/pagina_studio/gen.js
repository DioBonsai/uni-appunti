/* Generatore di domande d'esame (permutazioni, aritmetica modulare, ℤ_N, binario, combinatoria).
   Ogni domanda ha 5 opzioni, una sola corretta, e una spiegazione. Collaudo: node gen.js */
const GEN = (() => {
  const ri = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
  const pick = a => a[ri(0, a.length - 1)];
  const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = ri(0, i); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const gcd = (a, b) => (b ? gcd(b, a % b) : Math.abs(a));
  const lcm = (a, b) => (a / gcd(a, b)) * b;
  const phi = n => { let r = n, m = n; for (let p = 2; p * p <= m; p++) if (m % p === 0) { while (m % p === 0) m /= p; r -= r / p; } if (m > 1) r -= r / m; return r; };
  const mod = (a, n) => ((a % n) + n) % n;
  const powmod = (b, e, n) => { let r = 1, x = mod(b, n); while (e > 0) { if (e & 1) r = (r * x) % n; x = (x * x) % n; e = Math.floor(e / 2); } return r; };
  const inv = (a, n) => { for (let x = 1; x < n; x++) if ((a * x) % n === 1) return x; return null; };
  const factorial = n => (n <= 1 ? 1 : n * factorial(n - 1));
  const C = (n, k) => { let r = 1; for (let i = 1; i <= k; i++) r = (r * (n - k + i)) / i; return Math.round(r); };

  /* costruisce la domanda: la risposta giusta e distrattori (unici, diversi dalla giusta) */
  function build(o) {
    const seen = new Set([o.correct]);
    const wrong = [];
    for (const d of o.wrong) if (!seen.has(d)) { seen.add(d); wrong.push(d); }
    let guard = 0;
    while (wrong.length < 4 && guard++ < 200) { const d = o.filler(); if (!seen.has(d)) { seen.add(d); wrong.push(d); } }
    if (wrong.length < 4) return null;
    const opts = shuffle([o.correct, ...wrong.slice(0, 4)]);
    return { id: 'gen-' + Date.now().toString(36) + '-' + ri(1000, 9999), prova: 'Esercizio generato', args: [o.kind], theme: o.theme, q: o.q, o: opts, a: opts.indexOf(o.correct) + 1, s: o.s, gen: 1 };
  }

  /* ---------- permutazioni ---------- */
  const compose = (p, q) => q.map(x => p[x]); // (p∘q)(i) = p[q[i]], indici 0..n-1
  function cycleToPerm(cyc, n) { const p = [...Array(n).keys()]; for (let i = 0; i < cyc.length; i++) p[cyc[i]] = cyc[(i + 1) % cyc.length]; return p; }
  function cyclesOf(p) { const seen = new Set(), out = []; for (let i = 0; i < p.length; i++) { if (seen.has(i)) continue; const c = []; let x = i; while (!seen.has(x)) { seen.add(x); c.push(x); x = p[x]; } if (c.length > 1) out.push(c); } return out; }
  const cycTxt = cs => (cs.length ? cs.map(c => '(' + c.map(x => x + 1).join(' ') + ')').join('') : '(id)');
  const typeOf = p => cyclesOf(p).map(c => c.length).sort((a, b) => b - a);
  const typeTxt = t => '(' + (t.length ? t.join(', ') : '1') + ')';
  const orderOf = p => typeOf(p).reduce((a, l) => lcm(a, l), 1);
  const parityOf = p => (typeOf(p).reduce((s, l) => s + l - 1, 0) % 2 === 0 ? 'pari' : 'dispari');
  function randomProduct() {
    for (;;) {
      const n = ri(6, 9), k = ri(2, 3), cycs = [], perms = [];
      for (let i = 0; i < k; i++) { const len = ri(2, 4), pool = shuffle([...Array(n).keys()]).slice(0, len); cycs.push(pool); perms.push(cycleToPerm(pool, n)); }
      let p = perms[k - 1]; for (let i = k - 2; i >= 0; i--) p = compose(perms[i], p); // da destra a sinistra
      let wrongOrder = perms[0]; for (let i = 1; i < k; i++) wrongOrder = compose(perms[i], wrongOrder);
      if (cyclesOf(p).length >= 1) return { n, cycs, p, wrongOrder };
    }
  }
  const prodTxt = cycs => cycs.map(c => '(' + c.map(x => x + 1).join(' ') + ')').join('');

  function q_perm() {
    const { n, cycs, p, wrongOrder } = randomProduct();
    const t = pick(['dec', 'tipo', 'pp', 'pot']);
    const head = `Sia π = ${prodTxt(cycs)} ∈ S${sub(n)} (le permutazioni si compongono da destra a sinistra).`;
    const dec = `Da destra a sinistra si ottiene π = ${cycTxt(cyclesOf(p))}.`;
    if (t === 'dec') {
      const correct = cycTxt(cyclesOf(p));
      const wrong = [cycTxt(cyclesOf(wrongOrder)), cycTxt(cyclesOf(wrongOrder).map(c => c.slice().reverse())), cycTxt(cyclesOf(p).map(c => c.slice().reverse()))];
      const filler = () => { const q = shuffle([...Array(n).keys()]); return cycTxt(cyclesOf(cycleToPerm(q.slice(0, 3), n).map((x, i) => x)).concat(cyclesOf(cycleToPerm(q.slice(3, 5), n)))); };
      return build({ kind: 'permutazioni', theme: 'Permutazioni', q: head + ' La decomposizione di π in cicli disgiunti è:', correct, wrong, filler, s: dec + ' Un errore frequente è comporre da sinistra a destra, che dà ' + cycTxt(cyclesOf(wrongOrder)) + '.' });
    }
    if (t === 'tipo') {
      const ty = typeOf(p), correct = typeTxt(ty);
      const wrong = [typeTxt(typeOf(wrongOrder)), typeTxt(cycs.map(c => c.length).sort((a, b) => b - a)), typeTxt(ty.concat([2])), typeTxt(ty.map(x => x + 1))];
      const filler = () => typeTxt([ri(2, 5), ri(2, 4)].sort((a, b) => b - a));
      return build({ kind: 'cicli-tipo-periodo', theme: 'Permutazioni', q: head + ' Il tipo di π (i punti fissi non si contano) è:', correct, wrong, filler, s: dec + ' Il tipo è la lista delle lunghezze dei cicli: ' + typeTxt(ty) + '.' });
    }
    if (t === 'pp') {
      const per = orderOf(p), par = parityOf(p), other = par === 'pari' ? 'dispari' : 'pari';
      const correct = `è ${par} ed ha periodo ${per}`;
      const wrong = [`è ${other} ed ha periodo ${per}`, `è ${par} ed ha periodo ${typeOf(p).reduce((a, b) => a + b, 0)}`, `è ${other} ed ha periodo ${Math.max(...typeOf(p))}`, `è ${par} ed ha periodo ${Math.max(...typeOf(p))}`];
      const filler = () => `è ${pick(['pari', 'dispari'])} ed ha periodo ${ri(2, 30)}`;
      return build({ kind: 'parita', theme: 'Permutazioni', q: head + ' Allora π', correct, wrong, filler, s: dec + ` Il periodo è l'mcm delle lunghezze dei cicli (${typeTxt(typeOf(p))}) = ${per}; la parità si ottiene da Σ(lunghezza − 1) = ${typeOf(p).reduce((s, l) => s + l - 1, 0)}, quindi π è ${par}.` });
    }
    const x = ri(0, n - 1), k = ri(5, 40);
    let r = x; for (let i = 0; i < k; i++) r = p[r];
    const correct = String(r + 1);
    const wrong = [...Array(n).keys()].map(v => String(v + 1));
    return build({ kind: 'cicli-tipo-periodo', theme: 'Permutazioni', q: head + ` Allora π${sup(k)}(${x + 1}) =`, correct, wrong: shuffle(wrong), filler: () => String(ri(1, n)), s: dec + ` Il periodo è ${orderOf(p)}, quindi π${sup(k)} = π${sup(k % orderOf(p))}; seguendo la freccia da ${x + 1} si arriva a ${r + 1}.` });
  }

  /* ---------- aritmetica modulare ---------- */
  function q_cong() {
    const n = ri(20, 90); let a, b, d;
    do { a = ri(2, n - 1); d = gcd(a, n); } while (d === 1 && Math.random() < 0.6);
    b = Math.random() < 0.65 ? d * ri(1, Math.max(1, Math.floor((n - 1) / d))) : ri(1, n - 1);
    b = mod(b, n); if (b === 0) b = d;
    const sol = b % d === 0 ? d : 0;
    const correct = String(sol);
    const wrong = [0, 1, d, d + 1, 2 * d, Math.max(1, d - 1)].map(String);
    return build({ kind: 'aritmetica-modulare', theme: 'Aritmetica modulare e ℤ_N', q: `Quante soluzioni modulo ${n} ha la congruenza ${a}X ≡ ${b} mod ${n}?`, correct, wrong, filler: () => String(ri(0, 8)),
      s: `MCD(${a}, ${n}) = ${d}. ${b % d === 0 ? `Poiché ${d} divide ${b}, ci sono esattamente ${d} soluzioni modulo ${n}.` : `Poiché ${d} non divide ${b}, la congruenza non ha soluzioni.`}` });
  }
  function q_inverso() {
    let n, a; do { n = ri(15, 80); a = ri(2, n - 1); } while (gcd(a, n) !== 1);
    const x = inv(a, n), correct = String(x);
    const wrong = [n - x, n - a, mod(a + 1, n), Math.floor(n / 2)].map(String);
    return build({ kind: 'Z_N-moltiplicativo', theme: 'Aritmetica modulare e ℤ_N', q: `In ℤ${sub(n)} l'inverso moltiplicativo di [${a}] è`, correct, wrong, filler: () => String(ri(2, n - 1)), s: `${a}·${x} = ${a * x} = ${Math.floor((a * x) / n)}·${n} + 1 ≡ 1 mod ${n}, e MCD(${a}, ${n}) = 1, quindi [${a}]⁻¹ = [${x}].` });
  }
  function q_phi() {
    const ps = [2, 3, 5, 7, 11, 13]; let n;
    do { const k = ri(2, 3), f = shuffle(ps).slice(0, k); n = f.reduce((m, p) => m * (Math.random() < 0.3 ? p * p : p), 1); } while (n < 30 || n > 400);
    const target = pick(['phi', 'gen', 'inv']), v = phi(n), correct = String(v);
    const wrong = [n - 1, n / 2, v + 2, v - 2, Math.round(n / 3), v * 2].filter(x => Number.isInteger(x) && x > 0).map(String);
    const fa = (() => { let m = n, parts = []; for (let p = 2; p * p <= m; p++) if (m % p === 0) { let e = 0; while (m % p === 0) { m /= p; e++; } parts.push(e > 1 ? `${p}${sup(e)}` : `${p}`); } if (m > 1) parts.push(String(m)); return parts.join('·'); })();
    const base = `${n} = ${fa}, quindi φ(${n}) = ${v}.`;
    if (target === 'phi') return build({ kind: 'Z_N-moltiplicativo', theme: 'Aritmetica modulare e ℤ_N', q: `Sia φ la funzione di Eulero. Allora φ(${n}) =`, correct, wrong, filler: () => String(ri(8, n)), s: base });
    if (target === 'gen') return build({ kind: 'generatori', theme: 'Aritmetica modulare e ℤ_N', q: `Il numero dei generatori del gruppo additivo ℤ${sub(n)} è`, correct, wrong, filler: () => String(ri(8, n)), s: `I generatori di ℤ_N sono le classi coprime con N. ${base}` });
    return build({ kind: 'Z_N-moltiplicativo', theme: 'Aritmetica modulare e ℤ_N', q: `Il numero delle classi invertibili in (ℤ${sub(n)}, ·) è`, correct, wrong, filler: () => String(ri(8, n)), s: `Le classi invertibili sono quelle coprime con N. ${base}` });
  }
  function q_nongen() {
    const n = pick([60, 70, 72, 84, 90, 105, 80, 66, 50, 120]);
    const coprime = [], not = [];
    for (let k = 2; k < n; k++) (gcd(k, n) === 1 ? coprime : not).push(k);
    const bad = pick(not), good = shuffle(coprime).slice(0, 4);
    return build({ kind: 'generatori', theme: 'Aritmetica modulare e ℤ_N', q: `Quale delle seguenti classi non genera (ℤ${sub(n)}, +)?`, correct: `[${bad}]`, wrong: good.map(g => `[${g}]`), filler: () => `[${pick(coprime)}]`, s: `[k] genera ℤ_${n} se e solo se MCD(k, ${n}) = 1. Qui MCD(${bad}, ${n}) = ${gcd(bad, n)} ≠ 1, mentre gli altri valori sono coprimi con ${n}.` });
  }
  function q_pow() {
    const n = pick([7, 11, 13, 17, 19, 23, 25, 26, 27, 29, 31]); let a;
    do { a = ri(2, n - 1); } while (gcd(a, n) !== 1);
    const e = ri(40, 400), v = powmod(a, e, n), ord = phi(n);
    return build({ kind: 'aritmetica-modulare', theme: 'Aritmetica modulare e ℤ_N', q: `In ℤ${sub(n)} la classe [${a}]${sup(e)} è`, correct: `[${v}]`, wrong: [powmod(a, e % ord + 1, n), powmod(a, e, n) + 1, mod(a * (e % n), n), mod(e, n), powmod(a, ord - e % ord, n)].map(x => `[${mod(x, n)}]`), filler: () => `[${ri(1, n - 1)}]`,
      s: `Per Eulero [${a}]${sup(ord)} = [1] (φ(${n}) = ${ord}), quindi l'esponente si riduce modulo ${ord}: ${e} ≡ ${e % ord}, e [${a}]${sup(e % ord)} = [${v}].` });
  }
  function q_base2() {
    const v = ri(40, 200), bin = v.toString(2), flip = i => { const b = bin.split(''); b[i] = b[i] === '1' ? '0' : '1'; return b.join(''); };
    const wrong = [flip(ri(0, bin.length - 1)), flip(bin.length - 1), flip(ri(0, bin.length - 2)), (v + ri(1, 9)).toString(2), (v - ri(1, 9)).toString(2)];
    return build({ kind: 'base-2', theme: 'Binario', q: `Quale delle seguenti è la scrittura di ${v} in base 2?`, correct: bin, wrong, filler: () => ri(40, 200).toString(2), s: `${v} = ${bin.split('').map((c, i) => (c === '1' ? 2 ** (bin.length - 1 - i) : null)).filter(x => x !== null).join(' + ')} = ${bin}₂.` });
  }
  function q_conteggio() {
    const n1 = ri(4, 12), n2 = ri(4, 12), r = ri(2, Math.min(4, n1 - 1)), s = ri(2, Math.min(4, n2 - 1));
    const correct = `C(${n1}, ${r}) · C(${n2}, ${s})`;
    const wrong = [`C(${n1}, ${r}) + C(${n2}, ${s})`, `C(${n1 + n2}, ${r + s})`, `C(${n1}, ${s}) · C(${n2}, ${r})`, `(${n1}!/${r}!) · (${n2}!/${s}!)`];
    return build({ kind: 'combinazioni', theme: 'Combinatoria', q: `Siano A e B insiemi disgiunti con |A| = ${n1} e |B| = ${n2}. Quanti sono i sottoinsiemi di A ∪ B formati da ${r} elementi di A e ${s} di B?`, correct, wrong, filler: () => `C(${ri(5, 20)}, ${ri(2, 5)})`, s: `Si scelgono gli ${r} elementi di A in C(${n1}, ${r}) modi e, indipendentemente, i ${s} di B in C(${n2}, ${s}): principio moltiplicativo. Valore: ${C(n1, r) * C(n2, s)}.` });
  }
  function q_dispos() {
    const k = ri(3, 6), m = ri(4, 9), t = pick(['rip', 'sem']);
    if (t === 'rip') return build({ kind: 'disposizioni', theme: 'Combinatoria', q: `${k} amici ordinano ciascuno una pizza scegliendo tra ${m} tipi (anche uguali). Quanti sono gli ordini possibili?`, correct: `${m}${sup(k)}`, wrong: [`${k}${sup(m)}`, `${m}!/${m - k > 0 ? m - k : 1}!`, `C(${m}, ${k})`, `${m}·${k}`], filler: () => `${ri(2, 9)}${sup(ri(2, 7))}`, s: `Ognuno sceglie indipendentemente tra ${m} tipi: ${m}${sup(k)} = ${m ** k}.` });
    const kk = Math.min(k, m - 1);
    return build({ kind: 'disposizioni', theme: 'Combinatoria', q: `In quanti modi si possono far sedere ${kk} persone in una fila di ${m} sedie?`, correct: `${m}!/${m - kk}!`, wrong: [`${m}${sup(kk)}`, `${kk}!`, `C(${m}, ${kk})`, `${m}!`], filler: () => `${ri(5, 12)}!/${ri(2, 4)}!`, s: `Sono disposizioni semplici: ${m}·${m - 1}·…·${m - kk + 1} = ${m}!/${m - kk}!.` });
  }

  function sub(n) { return String(n).split('').map(d => '₀₁₂₃₄₅₆₇₈₉'[d]).join(''); }
  function sup(n) { return String(n).split('').map(d => '⁰¹²³⁴⁵⁶⁷⁸⁹'[d]).join(''); }

  const MAKERS = [q_perm, q_perm, q_perm, q_cong, q_inverso, q_phi, q_nongen, q_pow, q_base2, q_conteggio, q_dispos];
  const make = () => { for (let i = 0; i < 20; i++) { const q = pick(MAKERS)(); if (q) return q; } return null; };
  const many = n => { const out = []; for (let i = 0; i < n * 4 && out.length < n; i++) { const q = make(); if (q) out.push(q); } return out; };

  return { make, many, _t: { gcd, lcm, phi, mod, powmod, inv, compose, cycleToPerm, cyclesOf, orderOf, parityOf, typeOf, C, factorial, MAKERS } };
})();
if (typeof module !== 'undefined') module.exports = GEN;
