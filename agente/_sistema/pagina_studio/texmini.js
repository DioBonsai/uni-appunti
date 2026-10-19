/* Mini convertitore LaTeX -> HTML/Unicode per i quiz (nessuna libreria, funziona offline).
   Converte solo i comandi noti; i backslash di altro tipo (percorsi Windows, "\n" in C) restano com'e'. */
const TEXSYM = {
  wedge: '∧', land: '∧', vee: '∨', lor: '∨', neg: '¬', lnot: '¬', to: '→', rightarrow: '→', Rightarrow: '⇒', Leftrightarrow: '⟺',
  leftrightarrow: '↔', implies: '⟹', iff: '⟺', forall: '∀', exists: '∃', in: '∈', notin: '∉', subseteq: '⊆', supseteq: '⊇', subset: '⊂',
  cap: '∩', cup: '∪', times: '×', cdot: '·', ldots: '…', dots: '…', lambda: 'λ', sigma: 'σ', alpha: 'α', beta: 'β', gamma: 'γ',
  delta: 'δ', epsilon: 'ε', varepsilon: 'ε', pi: 'π', omega: 'ω', theta: 'θ', mu: 'μ', emptyset: '∅', leq: '≤', le: '≤', geq: '≥',
  ge: '≥', neq: '≠', ne: '≠', sim: '∼', mid: '∣', therefore: '∴', quad: '  ', qquad: '    ', oplus: '⊕', equiv: '≡', infty: '∞',
  approx: '≈', circ: '∘', setminus: '∖', Sigma: 'Σ', Delta: 'Δ'
};
const TEXBB = { R: 'ℝ', N: 'ℕ', Z: 'ℤ', Q: 'ℚ', C: 'ℂ' };
const TEXCAL = { P: '𝒫', A: '𝒜', C: '𝒞', F: 'ℱ', L: 'ℒ' };
const TEXRE = /\\[(\[]|\\(?:overline|wedge|land|lor|vee|neg|lnot|to|rightarrow|Rightarrow|Leftrightarrow|leftrightarrow|implies|iff|forall|exists|subseteq|supseteq|cap|cup|times|cdot|ldots|lambda|sigma|mathbf|mathbb|mathcal|frac|therefore|emptyset|leq|geq|neq|mid|text|sim|oplus|equiv|setminus|circ)(?![a-zA-Z])/;
function texGroup(s, i) {
  while (s[i] === ' ') i++;
  if (s[i] === '{') {
    let d = 1, j = i + 1;
    while (j < s.length && d) { if (s[j] === '{') d++; else if (s[j] === '}') d--; j++; }
    return [s.slice(i + 1, d ? j : j - 1), j];
  }
  if (s[i] === '\\') { const m = /^\\[a-zA-Z]+/.exec(s.slice(i)); if (m) return [m[0], i + m[0].length]; }
  return [s[i] || '', i + 1];
}
function texConv(s) {
  let o = '', i = 0;
  while (i < s.length) {
    const c = s[i];
    if (c === '\\') {
      if ('()[]'.includes(s[i + 1] || 'x')) { i += 2; continue; }
      const m = /^\\([a-zA-Z]+)/.exec(s.slice(i));
      if (!m) { o += c; i++; continue; }
      const n = m[1]; i += m[0].length;
      if (n === 'overline') { const [g, j] = texGroup(s, i); i = j; o += '<span class="ov">' + texConv(g) + '</span>'; }
      else if (n === 'mathbf' || n === 'textbf') { const [g, j] = texGroup(s, i); i = j; o += '<b>' + texConv(g) + '</b>'; }
      else if (n === 'mathbb') { const [g, j] = texGroup(s, i); i = j; o += TEXBB[g] || texConv(g); }
      else if (n === 'mathcal') { const [g, j] = texGroup(s, i); i = j; o += TEXCAL[g] || texConv(g); }
      else if (n === 'text' || n === 'mathrm') { const [g, j] = texGroup(s, i); i = j; o += texConv(g); }
      else if (n === 'frac') { const [a, j1] = texGroup(s, i); const [b, j2] = texGroup(s, j1); i = j2; const wrap = t => (t.length > 1 ? '(' + t + ')' : t); o += wrap(texConv(a)) + '/' + wrap(texConv(b)); }
      else if (n === 'not') { const [g, j] = texGroup(s, i); const sym = { '\\in': '∉', '\\subseteq': '⊄', '\\supseteq': '⊉', '\\equiv': '≢' }[g]; if (sym) { i = j; o += sym; } else o += '¬'; }
      else if (n === 'bf') { /* dichiarazione di grassetto: ignorata */ }
      else if (TEXSYM[n]) o += TEXSYM[n];
      else o += '\\' + n;
    } else if ((c === '_' || c === '^') && s[i + 1] === '{') {
      const [g, j] = texGroup(s, i + 1); i = j; o += (c === '_' ? '<sub>' : '<sup>') + texConv(g) + (c === '_' ? '</sub>' : '</sup>');
    } else if (c === '_' && /[A-Za-z0-9]/.test(s[i + 1] || '') && /[A-Za-z)]/.test(s[i - 1] || '')) {
      o += '<sub>' + s[i + 1] + '</sub>'; i += 2;
    } else if (c === '{' || c === '}') { i++; }
    else { o += c; i++; }
  }
  return o;
}
const tex = s => TEXRE.test(s) ? texConv(s) : s;
const tx = s => tex(esc(s));
