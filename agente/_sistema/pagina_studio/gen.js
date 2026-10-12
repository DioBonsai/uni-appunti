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

  /* ---------- Algebra lineare: numeri complessi ---------- */
  const cx = (a, b) => { // testo di a + bi, con segni e coefficienti 1/0 sistemati
    const im = b === 0 ? '' : (Math.abs(b) === 1 ? 'i' : Math.abs(b) + 'i');
    if (b === 0) return String(a);
    if (a === 0) return (b < 0 ? '−' : '') + im;
    return `${a < 0 ? '−' + Math.abs(a) : a} ${b < 0 ? '−' : '+'} ${im}`;
  };
  const cxOpts = (a, b, extra) => [cx(a, -b), cx(-a, b), cx(-a, -b), cx(b, a), ...(extra || [])];
  const T = 'Numeri complessi';
  function q_cxmul() {
    const a = ri(-5, 5), b = ri(-5, 5) || 2, c = ri(-5, 5), d = ri(-5, 5) || 3, re = a * c - b * d, im = a * d + b * c;
    return build({ kind: 'numeri-complessi', theme: T, q: `Il prodotto (${cx(a, b)})·(${cx(c, d)}) è`, correct: cx(re, im), wrong: [cx(a * c + b * d, a * d - b * c), cx(a * c - b * d, a * d - b * c), cx(a * c + b * d, a * d + b * c), cx(re, -im), cx(a * c, b * d)], filler: () => cx(ri(-20, 20), ri(-20, 20)),
      s: `(${cx(a, b)})(${cx(c, d)}) = ${a * c} + ${a * d}i + ${b * c}i + ${b * d}i² = (${a * c} − ${b * d}) + (${a * d} + ${b * c})i = ${cx(re, im)}.` });
  }
  function q_cxdiv() {
    const x = ri(-4, 4), y = ri(-4, 4) || 1, c = ri(-3, 3) || 2, d = ri(-3, 3) || 1, re = x * c - y * d, im = x * d + y * c;
    return build({ kind: 'numeri-complessi', theme: T, q: `Il quoziente (${cx(re, im)}) / (${cx(c, d)}) è`, correct: cx(x, y), wrong: [cx(x, -y), cx(-x, y), cx(y, x), cx(-x, -y), cx(x + 1, y)], filler: () => cx(ri(-6, 6), ri(-6, 6)),
      s: `Si moltiplica numeratore e denominatore per il coniugato ${cx(c, -d)}: il denominatore diventa ${c * c + d * d} e il risultato è ${cx(x, y)} (verifica: (${cx(x, y)})(${cx(c, d)}) = ${cx(re, im)}).` });
  }
  function q_cxmod() {
    const tr = pick([[3, 4], [5, 12], [8, 15], [6, 8], [7, 24], [9, 12]]), sg = () => (Math.random() < 0.5 ? -1 : 1), a = tr[0] * sg(), b = tr[1] * sg(), n = a * a + b * b, m = Math.sqrt(n);
    return build({ kind: 'coniugato-modulo', theme: 'Coniugato e modulo', q: `Il modulo di z = ${cx(a, b)} è`, correct: String(m), wrong: [String(n), String(Math.abs(a) + Math.abs(b)), String(Math.abs(a * b)), `√${m}`, String(m + 1)], filler: () => String(ri(2, 30)),
      s: `|z| = √(${a}² + ${b}²) = √${n} = ${m}.` });
  }
  function q_cxinv() {
    const a = ri(-4, 4) || 2, b = ri(-4, 4) || 3, n = a * a + b * b, f = (x, y) => `(${cx(x, y)})/${n}`;
    return build({ kind: 'coniugato-modulo', theme: 'Coniugato e modulo', q: `L'inverso moltiplicativo di z = ${cx(a, b)} è`, correct: f(a, -b), wrong: [f(a, b), f(-a, b), f(-a, -b), `(${cx(a, -b)})/${Math.sqrt(n) % 1 ? n + 1 : n - 1}`, f(b, a)], filler: () => `(${cx(ri(-5, 5), ri(-5, 5))})/${ri(2, 30)}`,
      s: `1/z = z̄/|z|² = (${cx(a, -b)})/${n}, perché z·z̄ = a² + b² = ${n}.` });
  }
  function q_cxipow() {
    const n = ri(3, 99), r = n % 4, correct = ['1', 'i', '−1', '−i'][r];
    return build({ kind: 'potenze-radici', theme: 'Potenze e radici', q: `Il valore di i${sup(n)} è`, correct, wrong: ['1', 'i', '−1', '−i', '0'].filter(x => x !== correct), filler: () => String(ri(2, 9)),
      s: `Le potenze di i si ripetono con periodo 4 (i⁰ = 1, i¹ = i, i² = −1, i³ = −i): ${n} = 4·${Math.floor(n / 4)} + ${r}, quindi i${sup(n)} = ${correct}.` });
  }
  function q_cxsq() {
    const a = ri(-6, 6) || 3, b = ri(-6, 6) || 2, re = a * a - b * b, im = 2 * a * b;
    return build({ kind: 'numeri-complessi', theme: T, q: `(${cx(a, b)})² =`, correct: cx(re, im), wrong: [cx(a * a + b * b, im), cx(re, -im), cx(re, im + 2), cx(a * a, b * b), cx(a * a - b * b, a * b)], filler: () => cx(ri(-30, 30), ri(-30, 30)),
      s: `(a + bi)² = a² − b² + 2abi = ${re} + ${im}i ⟹ ${cx(re, im)}.` });
  }
  function q_cx1i() {
    const k = pick([4, 8, 12]), v = (-4) ** (k / 4);
    return build({ kind: 'potenze-radici', theme: 'Potenze e radici', q: `Quanto vale (1 + i)${sup(k)}?`, correct: String(v), wrong: [String(-v), String(2 ** k), String(2 ** (k / 2)), String(v * 2), '0'], filler: () => String(ri(-80, 80)),
      s: `(1 + i)² = 2i, quindi (1 + i)⁴ = (2i)² = −4 e (1 + i)${sup(k)} = (−4)${sup(k / 4)} = ${v}.` });
  }

  /* ---------- Fondamenti: binario, complemento a due, Hamming, memoria ---------- */
  const TF = 'Rappresentazione binaria';
  const bits = (v, n) => (v >>> 0).toString(2).padStart(n, '0').slice(-n);
  function q_bin2dec() {
    const v = ri(20, 255), b = v.toString(2);
    return build({ kind: 'binario', theme: TF, q: `Il numero binario ${b} vale in decimale`, correct: String(v), wrong: [v + 1, v - 1, v ^ 1, parseInt(b.split('').reverse().join(''), 2), v + ri(2, 9)].map(String), filler: () => String(ri(20, 255)),
      s: `${b}₂ = ${b.split('').map((c, i) => (c === '1' ? 2 ** (b.length - 1 - i) : null)).filter(x => x !== null).join(' + ')} = ${v}.` });
  }
  function q_hex() {
    const v = ri(32, 4095), h = v.toString(16).toUpperCase(), up = Math.random() < 0.5;
    if (up) return build({ kind: 'binario', theme: TF, q: `Il numero decimale ${v} in esadecimale è`, correct: h, wrong: [(v + 1).toString(16), (v - 1).toString(16), (v ^ 16).toString(16), (v + 16).toString(16)].map(x => x.toUpperCase()), filler: () => ri(32, 4095).toString(16).toUpperCase(), s: `${v} = ${h}₁₆ (si divide per 16 e si leggono i resti dal basso).` });
    return build({ kind: 'binario', theme: TF, q: `Il numero esadecimale ${h} vale in decimale`, correct: String(v), wrong: [v + 1, v - 1, v + 16, v - 16, v ^ 256].map(String), filler: () => String(ri(32, 4095)), s: `${h}₁₆ = ${[...h].map((c, i) => parseInt(c, 16) + '·16' + sup(h.length - 1 - i)).join(' + ')} = ${v}.` });
  }
  function q_c2() {
    const n = ri(1, 127), neg = Math.random() < 0.6, N = 8;
    if (neg) { const c = bits(256 - n, N); return build({ kind: 'complemento-eccesso', theme: TF, q: `In complemento a due su 8 bit, −${n} si scrive`, correct: c, wrong: ['1' + bits(n, 7), bits(~n & 255, N), bits(n, N), bits(256 - n + 1, N), bits(256 - n - 1, N)], filler: () => bits(ri(0, 255), N), s: `${n} = ${bits(n, N)}; si invertono i bit (${bits(~n & 255, N)}) e si somma 1: ${c}.` }); }
    const c = bits(ri(128, 255), N), v = parseInt(c, 2) - 256;
    return build({ kind: 'complemento-eccesso', theme: TF, q: `Il pattern ${c}, letto in complemento a due su 8 bit, rappresenta il numero`, correct: String(v), wrong: [String(parseInt(c, 2)), String(-(parseInt(c, 2) - 128)), String(v + 1), String(v - 1), String(-v)], filler: () => String(ri(-128, 127)), s: `Il bit più a sinistra è 1, quindi il numero è negativo: ${parseInt(c, 2)} − 256 = ${v}.` });
  }
  function q_hamming() {
    const n = ri(6, 10), x = ri(0, 2 ** n - 1), y = ri(0, 2 ** n - 1), a = bits(x, n), b = bits(y, n), d = [...a].filter((c, i) => c !== b[i]).length;
    return build({ kind: 'errori-hamming', theme: 'Compressione ed errori', q: `Qual è la distanza di Hamming tra ${a} e ${b}?`, correct: String(d), wrong: [d + 1, d - 1, d + 2, n - d, n].map(String).filter(x => +x >= 0), filler: () => String(ri(0, n)), s: `La distanza di Hamming è il numero di posizioni in cui i due pattern differiscono: ${d}.` });
  }
  function q_parita() {
    const n = 7, x = ri(0, 127), a = bits(x, n), ones = [...a].filter(c => c === '1').length, bit = ones % 2, correct = a + bit;
    return build({ kind: 'errori-hamming', theme: 'Compressione ed errori', q: `Aggiungendo in fondo un bit di parità pari al pattern ${a}, si ottiene`, correct, wrong: [a + (1 - bit), bits(x ^ 1, n) + bit, (1 - bit) + a, a.slice(1) + a[0] + bit], filler: () => bits(ri(0, 255), 8), s: `Il pattern contiene ${ones} uni; per avere un numero pari di uni complessivo il bit aggiunto è ${bit}: ${correct}.` });
  }
  function q_mem() {
    const k = ri(8, 20);
    if (Math.random() < 0.5) return build({ kind: 'memoria', theme: 'Circuiti e memoria', q: `Una memoria principale ha indirizzi di ${k} bit e celle da 1 byte. Quante celle ha?`, correct: `2${sup(k)} = ${2 ** k}`, wrong: [`${k}²`, `2·${k}`, `2${sup(k - 1)}`, `2${sup(k + 1)}`, `${k}!`].map(x => x), filler: () => `2${sup(ri(4, 24))}`, s: `Con ${k} bit si formano 2${sup(k)} indirizzi diversi, quindi ${2 ** k} celle.` });
    return build({ kind: 'memoria', theme: 'Circuiti e memoria', q: `Quanti bit servono per indirizzare ${2 ** k} celle di memoria?`, correct: String(k), wrong: [k + 1, k - 1, 2 ** k, k * 2, 2 ** (k - 1)].map(String), filler: () => String(ri(4, 30)), s: `Servono k bit con 2^k ≥ ${2 ** k}: k = ${k}.` });
  }

  /* ---------- Matematica discreta: insiemi e funzioni (argomenti già trattati) ---------- */
  const lin = (a, b, v) => { // testo di a·v + b
    const A = a === 1 ? v : a === -1 ? '−' + v : (a < 0 ? '−' + Math.abs(a) : a) + v;
    if (a === 0) return String(b < 0 ? '−' + Math.abs(b) : b);
    if (b === 0) return A;
    return `${A} ${b < 0 ? '−' : '+'} ${Math.abs(b)}`;
  };
  function q_comp() {
    const a = pick([-3, -2, -1, 1, 2, 3, 4]), b = ri(-5, 5), c = pick([-3, -2, -1, 2, 3]), d = ri(-6, 6), A = c * a, B = c * b + d;
    return build({ kind: 'composizione', theme: 'Funzioni', q: `Siano f, g : ℤ → ℤ le funzioni f(n) = ${lin(a, b, 'n')} e g(n) = ${lin(c, d, 'n')}. Allora (g ∘ f)(n) =`, correct: lin(A, B, 'n'),
      wrong: [lin(A, a * d + b, 'n'), lin(A, c * b - d, 'n'), lin(c + a, B, 'n'), lin(A, c * b, 'n'), lin(A + 1, B, 'n')], filler: () => lin(ri(-12, 12) || 2, ri(-12, 12), 'n'),
      s: `(g ∘ f)(n) = g(f(n)) = ${c < 0 ? c : c}·(${lin(a, b, 'n')}) ${d < 0 ? '−' : '+'} ${Math.abs(d)} = ${lin(A, B, 'n')}. Si applica prima f, poi g (f ∘ g darebbe ${lin(A, a * d + b, 'n')}).` });
  }
  function q_invaff() {
    const a = pick([2, 3, 4, 5, -2, -3]), b = pick([-7, -5, -3, -1, 2, 4, 6]), x0 = ri(-6, 6), k = a * x0 + b;
    return build({ kind: 'iniettiva-suriettiva-inversa', theme: 'Funzioni', q: `Sia f : ℝ → ℝ la funzione biettiva f(x) = ${lin(a, b, 'x')}. Allora f⁻¹(${k < 0 ? '−' + Math.abs(k) : k}) =`, correct: String(x0).replace('-', '−'),
      wrong: [x0 + 1, x0 - 1, -x0, a * k + b, k - b].map(v => String(v).replace('-', '−')), filler: () => String(ri(-20, 20)).replace('-', '−'),
      s: `f⁻¹(k) è l'unico x con f(x) = k: ${lin(a, b, 'x')} = ${k} ⟹ x = (${k} ${b < 0 ? '+' : '−'} ${Math.abs(b)})/${a} = ${x0}.` });
  }
  function q_class() {
    const a = pick([-3, -2, -1, 1, 2, 3, 5, 0]), b = ri(-5, 5);
    const inj = a !== 0, sur = Math.abs(a) === 1;
    const lab = ['iniettiva e suriettiva', 'iniettiva ma non suriettiva', 'suriettiva ma non iniettiva', 'né iniettiva né suriettiva', 'non è una funzione'];
    const correct = inj ? (sur ? lab[0] : lab[1]) : lab[3];
    return build({ kind: 'iniettiva-suriettiva-inversa', theme: 'Funzioni', q: `La funzione f : ℤ → ℤ, f(n) = ${lin(a, b, 'n')}, è`, correct, wrong: lab.filter(x => x !== correct), filler: () => lab[ri(0, 4)],
      s: a === 0 ? `f è costante: due interi diversi hanno la stessa immagine (non iniettiva) e l'immagine è un solo valore (non suriettiva).` : (sur ? `f è iniettiva (da ${a}x + b = ${a}y + b segue x = y) e ogni intero m è immagine di ${a === 1 ? 'm − b' : 'b − m'}, intero: biettiva.` : `f è iniettiva, ma i valori assunti sono solo ${lin(a, b, 'n').replace('n', 'k')} con k intero: non si raggiunge ogni intero (si dividerebbe per ${Math.abs(a)} uscendo da ℤ), quindi non è suriettiva.`) });
  }
  function q_preim() {
    const k = ri(2, 6), m = ri(0, k - 1), correct = m === 0 ? `[−${k}, ${k}]` : `[−${k}, −${m}] ∪ [${m}, ${k}]`;
    return build({ kind: 'iniettiva-suriettiva-inversa', theme: 'Funzioni', q: `Sia f : ℝ → ℝ, f(x) = x². Allora f⁻¹([${m * m}, ${k * k}]) è`, correct, wrong: [`[${m}, ${k}]`, `[${m * m}, ${k * k}]`, `[−${k}, ${k}]`, `[${m}, ${k}] ∪ [${m * m}, ${k * k}]`, `[−${k * k}, −${m * m}] ∪ [${m * m}, ${k * k}]`], filler: () => `[−${ri(1, 9)}, ${ri(1, 9)}]`,
      s: `x² ∈ [${m * m}, ${k * k}] equivale a ${m} ≤ |x| ≤ ${k}, cioè x ∈ ${correct}: la controimmagine contiene sia i valori positivi sia i negativi.` });
  }
  function q_card() {
    const n = ri(2, 8), m = ri(2, 8);
    if (Math.random() < 0.5) return build({ kind: 'prodotto-cartesiano', theme: 'Insiemi', q: `Se |A| = ${n} e |B| = ${m}, quanti elementi ha il prodotto cartesiano A × B?`, correct: String(n * m), wrong: [n + m, n ** m, m ** n, n * m + n, n * m - 1].map(String), filler: () => String(ri(2, 70)), s: `Le coppie (a, b) sono ${n}·${m} = ${n * m}.` });
    return build({ kind: 'insiemi', theme: 'Insiemi', q: `Quanti sottoinsiemi (vuoto e insieme stesso compresi) ha un insieme di ${n} elementi?`, correct: String(2 ** n), wrong: [2 * n, n * n, 2 ** n - 1, 2 ** (n - 1), 2 ** (n + 1)].map(String), filler: () => String(ri(3, 300)), s: `Ogni elemento sta dentro o fuori dal sottoinsieme: 2${sup(n)} = ${2 ** n} scelte.` });
  }
  const stext = a => (a.length ? '{' + a.join(', ') + '}' : '∅');
  function q_setop() {
    const U = [1, 2, 3, 4, 5, 6, 7, 8, 9], A = U.filter(() => Math.random() < 0.5), B = U.filter(() => Math.random() < 0.5), op = pick(['∪', '∩', '∖']);
    if (!A.length || !B.length) return null;
    const f = { '∪': (x, y) => U.filter(v => x.includes(v) || y.includes(v)), '∩': (x, y) => U.filter(v => x.includes(v) && y.includes(v)), '∖': (x, y) => x.filter(v => !y.includes(v)) };
    const correct = stext(f[op](A, B));
    return build({ kind: 'operazioni-insiemi', theme: 'Insiemi', q: `Siano A = ${stext(A)} e B = ${stext(B)}. Allora A ${op} B =`, correct, wrong: [f['∪'](A, B), f['∩'](A, B), f['∖'](A, B), f['∖'](B, A), A.filter(v => !B.includes(v)).concat(B.filter(v => !A.includes(v))).sort((x, y) => x - y)].map(stext), filler: () => stext(U.filter(() => Math.random() < 0.4)),
      s: `${op === '∪' ? "A ∪ B contiene gli elementi che stanno in A o in B." : (op === '∩' ? "A ∩ B contiene gli elementi che stanno sia in A sia in B." : "A ∖ B contiene gli elementi di A che non stanno in B.")} Risultato: ${correct}.` });
  }

  const BYMAT = {
    'Matematica discreta': [q_comp, q_comp, q_invaff, q_class, q_class, q_preim, q_card, q_setop, q_setop,
      q_perm, q_perm, q_perm, q_cong, q_inverso, q_phi, q_nongen, q_pow, q_base2, q_conteggio, q_dispos],
    'Algebra lineare': [q_cxmul, q_cxdiv, q_cxmod, q_cxinv, q_cxipow, q_cxsq, q_cx1i],
    'Fondamenti Info': [q_bin2dec, q_hex, q_c2, q_c2, q_hamming, q_parita, q_mem, q_base2],
  };
  const MAKERS = BYMAT['Matematica discreta'];
  /* covered = insieme dei temi già trattati nei Word (se omesso, tutti): le domande di temi non coperti vengono scartate */
  const make = (mat, covered) => {
    const ms = BYMAT[mat || 'Matematica discreta']; if (!ms) return null;
    for (let i = 0; i < 80; i++) { const q = pick(ms)(); if (q && (!covered || covered.has(q.theme))) return q; }
    return null;
  };
  const many = (n, mat, covered) => { const out = []; for (let i = 0; i < n * 6 && out.length < n; i++) { const q = make(mat, covered); if (q) out.push(q); } return out; };
  const disponibile = (mat, covered) => !!BYMAT[mat] && (!covered || BYMAT[mat].some(f => { for (let i = 0; i < 6; i++) { const q = f(); if (q && covered.has(q.theme)) return true; } return false; }));

  return { make, many, disponibile, _t: { gcd, lcm, phi, mod, powmod, inv, compose, cycleToPerm, cyclesOf, orderOf, parityOf, typeOf, C, factorial, MAKERS } };
})();
if (typeof module !== 'undefined') module.exports = GEN;
