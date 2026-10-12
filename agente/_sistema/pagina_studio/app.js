/* Quaderno di ripasso v2: logica della pagina. DATA arriva da data.json; GEN (gen.js) è inserito dalla build. */
let DATA = null;
const LS_KEY = 'quaderno-ripasso-v2';
let S = { v: 2, qs: {}, th: {}, hist: [], cards: {}, exams: {}, probs: {} };
try {
  const x = JSON.parse(localStorage.getItem(LS_KEY) || 'null');
  if (x && x.v === 2) S = Object.assign(S, x);
  else { const old = JSON.parse(localStorage.getItem('quaderno-ripasso-v1') || 'null'); if (old) { S.hist = old.hist || []; S.exams = old.exams || {}; } }
} catch (e) {}
let SERVER = false, saveT = null;
const save = () => {
  S.ts = Date.now();
  try { localStorage.setItem(LS_KEY, JSON.stringify(S)); } catch (e) {}
  if (SERVER) { clearTimeout(saveT); saveT = setTimeout(() => fetch('api/stato', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(S) }).catch(() => {}), 400); }
};
async function loadServerState() { // se la pagina è servita da serve.py, i progressi stanno anche in _sistema/progressi.json
  try {
    const r = await fetch('api/stato'); if (!r.ok) return; SERVER = true; const x = await r.json();
    if (x && x.v === 2 && (x.ts || 0) > (S.ts || 0)) { S = Object.assign({ v: 2, qs: {}, th: {}, hist: [], cards: {}, exams: {}, probs: {} }, x); try { localStorage.setItem(LS_KEY, JSON.stringify(S)); } catch (e) {} }
    else if (S.ts) save();
  } catch (e) {}
}
const $ = (s, r = document) => r.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const pad = n => String(n).padStart(2, '0');
const isoLocal = d => d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
const todayStr = () => isoLocal(new Date());
const parseD = s => { const [y, m, d] = s.split('-').map(Number); return new Date(y, m - 1, d, 12); };
const addDays = (s, n) => { const d = parseD(s); d.setDate(d.getDate() + n); return isoLocal(d); };
const daysTo = s => Math.round((parseD(s) - parseD(todayStr())) / 864e5);
const itDate = s => s.split('-').reverse().join('/');
const say = t => { const l = $('#live'); if (l) l.textContent = t; };
function inline(s) { return esc(s).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/`(.+?)`/g, '<code>$1</code>'); }
function fmt(t) {
  let h = '', ul = false;
  for (const l of String(t).split('\n')) {
    if (/^\s*[-•]\s/.test(l)) { if (!ul) { h += '<ul>'; ul = true; } h += '<li>' + inline(l.replace(/^\s*[-•]\s/, '')) + '</li>'; }
    else { if (ul) { h += '</ul>'; ul = false; } if (l.trim()) h += '<p>' + inline(l) + '</p>'; }
  }
  return h + (ul ? '</ul>' : '');
}

/* ---------- temi, esami, scadenze ---------- */
const themeOf = tags => { for (const t of DATA.priorita) if (tags.some(a => DATA.tagTema[a] === t)) return t; return tags.length ? (DATA.tagTema[tags[0]] || 'Altro') : 'Altro'; };
const themeWeak = t => Math.min(3, S.th[t] || 0);
const weakThemes = () => Object.entries(S.th).filter(e => e[1] > 0.4).sort((a, b) => b[1] - a[1]);
const examOf = m => S.exams[m] || (DATA.esami || {})[m] || '';
function capInterval(days, mat) { // a ridosso dell'esame gli intervalli si accorciano
  const e = examOf(mat); if (!e) return days; const left = daysTo(e); if (left < 0) return days;
  return Math.max(1, Math.min(days, Math.floor(left / 3)));
}
function bumpTheme(theme, ok) { S.th[theme] = Math.max(0, (S.th[theme] || 0) + (ok ? -0.5 : 1)); }
function chapterHint(theme) {
  const t = DATA.temi[theme];
  if (!t) return '';
  return t.capitoli ? `<p class="hint">Rivedi: Matematica discreta, ${esc(t.capitoli)} del tuo Word.</p>` : '<p class="hint">Tema non ancora nel Word: arriva con le prossime lezioni.</p>';
}

/* ---------- navigazione ---------- */
const TABS = ['oggi', 'quiz', 'problemi', 'schede'];
function showTab(name) {
  if (!TABS.includes(name)) name = 'oggi';
  TABS.forEach(t => { $('#tab-' + t).hidden = t !== name; $('#t-' + t).setAttribute('aria-selected', String(t === name)); });
  if (name === 'oggi') renderOggi();
  if (name === 'quiz') setupQuiz();
  if (name === 'problemi') renderProbSetup();
  if (name === 'schede') renderCardSetup();
  try { history.replaceState(null, '', '#' + name); } catch (e) {}
}
document.querySelectorAll('.tab').forEach(b => b.addEventListener('click', () => showTab(b.dataset.tab)));

/* ---------- Oggi ---------- */
const dueCards = (mat) => DATA.cards.filter(c => (!mat || mat === '*' || c.m === mat) && isDue(c));
function renderOggi() {
  $('#agg').textContent = itDate(DATA.oggi);
  const mats = Object.keys(DATA.materie);
  const nc = dueCards('*').length, nq = DATA.quiz.filter(q => { const s = S.qs[q.id]; return s && s.due <= todayStr(); }).length;
  $('#sessione-card').innerHTML = `<h2>Sessione di oggi</h2>
    <p>Circa 20 minuti: prima le schede in scadenza, poi domande scelte tra i tuoi punti deboli e il peso all'esame, poi qualche esercizio nuovo.</p>
    <p class="muted"><span class="mono">${nc}</span> schede da ripassare · <span class="mono">${nq}</span> domande da rivedere${weakThemes().length ? ' · punto debole: ' + esc(weakThemes()[0][0]) : ''}</p>
    <div class="row"><button class="btn" id="go-session">Inizia la sessione</button></div>`;
  $('#go-session').addEventListener('click', startSession);
  if (DATA.piano) { $('#piano-card').hidden = false; $('#piano').innerHTML = fmt(DATA.piano); }
  $('#exams').innerHTML = mats.map((m, i) => {
    const d = examOf(m); let txt = '<span class="muted">data non ancora nota</span>';
    if (d) { const left = daysTo(d); txt = left >= 0 ? `<span class="big mono">${left}</span> <span class="muted">giorni</span>` : '<span class="pill bad">data passata</span>'; }
    return `<div class="row" style="justify-content:space-between"><label for="ex${i}">${esc(m)}<input type="date" id="ex${i}" data-m="${esc(m)}" value="${d || ''}"></label><div>${txt}</div></div>`;
  }).join('');
  document.querySelectorAll('#exams input').forEach(inp => inp.addEventListener('change', e => { S.exams[e.target.dataset.m] = e.target.value; save(); renderOggi(); }));
  $('#materie').innerHTML = mats.map(m => {
    const x = DATA.materie[m], pct = x.capitoli ? Math.round(100 * x.studiati / x.capitoli) : 0;
    const chips = (x.elenco || []).map(c => `<span class="chip ${c.s === 2 ? 'done' : (c.s === 1 ? 'part' : '')}" title="${esc(c.t)}">${c.n}</span>`).join('');
    return `<div class="card"><div class="row" style="justify-content:space-between"><h3>${esc(m)}</h3><span class="pill ${pct === 100 ? 'good' : (pct === 0 ? 'warn' : '')}">${x.studiati} di ${x.capitoli} capitoli studiati</span></div>
      <div class="bar" role="img" aria-label="${pct}% studiato"><i style="width:${pct}%"></i></div><div class="chips" aria-label="Capitoli: verde studiato, arancio in parte">${chips}</div>
      <p class="muted">Lezioni nel Word: ${esc(x.lezioni)}</p><p>${esc(x.prossimo)}</p></div>`;
  }).join('');
  const max = Math.max(...DATA.freq.map(f => f[1] / 150 + f[2] / 30));
  $('#freq').innerHTML = DATA.freq.slice().sort((a, b) => (b[1] / 150 + b[2] / 30) - (a[1] / 150 + a[2] / 30)).map(f => {
    const w = Math.round(100 * (f[1] / 150 + f[2] / 30) / max);
    return `<span>${esc(f[0])}</span><div class="bar" role="img" aria-label="peso ${w}%"><i style="width:${w}%"></i></div><span class="pill ${f[3] ? 'good' : 'warn'}">${f[3] ? 'nel Word' : 'non ancora'}</span>
      <span class="nums mono" style="grid-column:1/-1;margin-top:-6px">quiz ${f[1]}/150 · problemi ${f[2]}/30</span>`;
  }).join('');
  const weak = weakThemes().slice(0, 6);
  $('#deboli').innerHTML = weak.length ? '<ul class="plain">' + weak.map(([k, v]) => `<li>${esc(k)} <span class="mono muted">(${Math.round(v)})</span> <button class="btn ghost small" data-tr="${esc(k)}">Allena</button></li>`).join('') + '</ul>' : '<p class="muted">Nessun errore registrato. Fai un quiz o un problema e qui compaiono i temi da rivedere.</p>';
  document.querySelectorAll('[data-tr]').forEach(b => b.addEventListener('click', () => { showTab('quiz'); $('#q-topic').value = b.dataset.tr; startQuiz(false); }));
  $('#storico').innerHTML = S.hist.length ? '<ul class="plain">' + S.hist.slice(-5).reverse().map(h => `<li><span class="mono">${h.score}/${h.n}</span> · ${esc(h.topic)} · <span class="muted">${itDate(h.date)}</span></li>`).join('') + '</ul>' : '<p class="muted">Ancora nessuna prova su questo dispositivo.</p>';
}

/* ---------- Quiz ---------- */
let Q = null, timer = null;
function setupQuiz() {
  const counts = {}; DATA.quiz.forEach(q => counts[q.theme] = (counts[q.theme] || 0) + 1);
  const cur = $('#q-topic').value;
  $('#q-topic').innerHTML = '<option value="">Tutti i temi (' + DATA.quiz.length + ' domande)</option><option value="__gen__">Esercizi generati (senza limite)</option>' + Object.keys(counts).sort().map(a => `<option value="${esc(a)}">${esc(a)} (${counts[a]})</option>`).join('');
  if (cur) $('#q-topic').value = cur;
  $('#q-weak').hidden = !weakThemes().length;
  $('#q-min-l').hidden = $('#q-mode').value !== 'sim';
}
$('#q-mode').addEventListener('change', () => { $('#q-min-l').hidden = $('#q-mode').value !== 'sim'; });
const NOSHUF = /nessun|precedent|tutte le|entrambe|nessuna/i;
function prepare(q) { // mescola le opzioni (tranne "nessuna delle precedenti") così non si impara la posizione
  if (q.gen || q.o.some(o => NOSHUF.test(o)) || /opzion|risposta [1-5]/i.test(q.q)) return Object.assign({}, q);
  const idx = shuffle([0, 1, 2, 3, 4]);
  return Object.assign({}, q, { o: idx.map(i => q.o[i]), a: idx.indexOf(q.a - 1) + 1 });
}
function pickQuiz(n, { theme, weak, ignoreDue } = {}) {
  let pool = DATA.quiz;
  if (weak) { const w = weakThemes().map(e => e[0]); pool = pool.filter(q => w.includes(q.theme)); }
  else if (theme) pool = pool.filter(q => q.theme === theme);
  const today = todayStr();
  const scored = pool.map(q => {
    const s = S.qs[q.id]; let sc = s ? (s.due <= today ? 3 + Math.min(s.wrong || 0, 3) * 0.3 : -1) : 1.5;
    if (ignoreDue) sc = s && s.due > today ? 0 : 1;
    sc += themeWeak(q.theme) * 0.8 + (DATA.pesi[q.theme] || 0) * 1.2 + Math.random();
    return [sc, q];
  }).sort((a, b) => b[0] - a[0]);
  return scored.slice(0, n).map(x => x[1]);
}
function startQuiz(weak, opts = {}) {
  const topic = opts.topic !== undefined ? opts.topic : $('#q-topic').value, mode = $('#q-mode').value, n = opts.n || +$('#q-n').value;
  let list, label = topic || 'tutti i temi';
  if (opts.list) { list = opts.list; label = opts.label || label; }
  else if (topic === '__gen__') { list = GEN.many(n); label = 'esercizi generati'; }
  else if (weak) { list = pickQuiz(n, { weak: true }); label = 'punti deboli'; }
  else list = pickQuiz(n, { theme: topic, ignoreDue: mode === 'sim' });
  if (!list.length) return;
  const sim = !opts.list && mode === 'sim';
  Q = { list: list.map(prepare), i: 0, score: 0, wrong: [], fb: opts.fb !== undefined ? opts.fb : (!sim && mode === '1'), label: sim ? 'simulazione · ' + label : label, t0: Date.now(), answered: false, sim, limit: sim ? +$('#q-min').value * 60 : 0, onEnd: opts.onEnd || null };
  $('#quiz-setup').hidden = true; $('#quiz-run').hidden = false;
  clearInterval(timer); timer = setInterval(tick, 1000);
  renderQ();
}
function tick() {
  const el = $('#q-time'); if (!el || !Q) return; const s = Math.floor((Date.now() - Q.t0) / 1000);
  if (Q.sim) { const left = Q.limit - s; if (left <= 0) { endQuiz(); return; } el.textContent = pad(Math.floor(left / 60)) + ':' + pad(left % 60); el.classList.toggle('timer-low', left < 120); }
  else el.textContent = pad(Math.floor(s / 60)) + ':' + pad(s % 60);
}
function renderQ() {
  const q = Q.list[Q.i]; Q.answered = false;
  $('#quiz-run').innerHTML = `<div class="row" style="justify-content:space-between"><span class="pill">Domanda ${Q.i + 1} di ${Q.list.length}</span><span class="mono muted" id="q-time" aria-label="${Q.sim ? 'tempo rimasto' : 'tempo trascorso'}">00:00</span></div>
    <p class="muted">${esc(q.prova)} · ${esc(q.theme)}</p><div class="q-text">${fmt(q.q)}</div>
    <div class="opts" role="group" aria-label="Risposte">${q.o.map((o, k) => `<button class="opt" data-k="${k + 1}"><span class="n">${k + 1}</span><span>${esc(o)}</span></button>`).join('')}</div>
    <div id="q-fbk"></div><div class="row"><button class="btn" id="q-next" disabled>${Q.i + 1 === Q.list.length ? 'Vedi il risultato' : 'Avanti'}</button>${Q.sim ? '<button class="btn ghost" id="q-stop">Consegna ora</button>' : ''}</div>`;
  document.querySelectorAll('.opt').forEach(b => b.addEventListener('click', () => answer(+b.dataset.k)));
  $('#q-next').addEventListener('click', nextQ);
  if ($('#q-stop')) $('#q-stop').addEventListener('click', endQuiz);
  tick();
}
function nextQ() { if (!Q.answered) return; Q.i++; Q.i < Q.list.length ? renderQ() : endQuiz(); }
function answer(k) {
  if (!Q || Q.answered) return; Q.answered = true; const q = Q.list[Q.i]; const ok = k === q.a;
  if (ok) Q.score++; else Q.wrong.push(q);
  bumpTheme(q.theme, ok);
  if (!q.gen) { const s = S.qs[q.id] || { box: 0, wrong: 0 }; if (ok) { s.box = Math.min(s.box + 1, 4); s.due = addDays(todayStr(), capInterval([1, 3, 7, 14, 30][s.box], 'Matematica discreta')); } else { s.box = 0; s.wrong = (s.wrong || 0) + 1; s.due = todayStr(); } S.qs[q.id] = s; }
  save();
  document.querySelectorAll('.opt').forEach(b => { b.disabled = true; const n = +b.dataset.k; if (Q.fb) { if (n === q.a) b.classList.add('ok'); else if (n === k) b.classList.add('ko'); } else if (n === k) b.classList.add('sel'); });
  if (Q.fb) {
    $('#q-fbk').innerHTML = `<div class="note ${ok ? '' : 'warn'}"><strong>${ok ? 'Giusto.' : 'Sbagliato: la risposta è la ' + q.a + '.'}</strong> ${esc(q.s)}${ok ? '' : chapterHint(q.theme)}</div>` + (q.w ? `<div class="note warn" style="margin-top:8px"><strong>Attenzione, possibile errore nella soluzione ufficiale:</strong> ${esc(q.w)}</div>` : '');
    say(ok ? 'Giusto' : 'Sbagliato, la risposta è la ' + q.a);
  } else say('Risposta registrata');
  $('#q-next').disabled = false; $('#q-next').focus();
}
function endQuiz() {
  if (!Q) return; clearInterval(timer);
  const n = Q.list.length, answered = Q.i + (Q.answered ? 1 : 0), s = Math.floor((Date.now() - Q.t0) / 1000);
  if (Q.sim && answered < n) Q.list.slice(answered).forEach(q => { Q.wrong.push(q); bumpTheme(q.theme, false); });
  S.hist.push({ date: todayStr(), score: Q.score, n, topic: Q.label }); S.hist = S.hist.slice(-30); save();
  const done = Q.onEnd; const q0 = Q; Q = null;
  $('#quiz-run').innerHTML = `<h2>Risultato</h2><div class="row"><span class="big mono">${q0.score}/${n}</span><span class="muted">in ${Math.floor(s / 60)} min ${s % 60} s · ${esc(q0.label)}${q0.sim && answered < n ? ' · ' + (n - answered) + ' senza risposta' : ''}</span></div>
    ${q0.wrong.length ? '<h3>Da rivedere</h3>' + q0.wrong.map(q => `<div class="note warn"><div class="q-text">${fmt(q.q)}</div><p><strong>Risposta ${q.a}:</strong> ${esc(q.o[q.a - 1])}</p><p>${esc(q.s)}</p>${chapterHint(q.theme)}${q.w ? '<p><em>Possibile errore nella soluzione ufficiale: ' + esc(q.w) + '</em></p>' : ''}</div>`).join('') : '<p>Nessun errore. Ottimo.</p>'}
    <div class="row"><button class="btn" id="q-again">${done ? 'Concludi la sessione' : 'Un altro quiz'}</button></div>`;
  $('#q-again').addEventListener('click', () => { $('#quiz-run').hidden = true; $('#quiz-setup').hidden = false; setupQuiz(); if (done) done(); });
  $('#q-again').focus();
}
$('#q-start').addEventListener('click', () => startQuiz(false));
$('#q-weak').addEventListener('click', () => startQuiz(true));

/* ---------- Problemi ---------- */
let P = null;
function renderProbSetup() {
  const cur = $('#p-topic').value, th = [...new Set(DATA.problemi.map(p => p.theme))].sort();
  $('#p-topic').innerHTML = '<option value="">Tutti i temi</option>' + th.map(t => `<option>${esc(t)}</option>`).join(''); if (cur) $('#p-topic').value = cur;
  const pool = probPool(); $('#p-count').textContent = `${pool.filter(p => !S.probs[p.id]).length} mai svolti su ${pool.length}`;
}
$('#p-topic').addEventListener('change', renderProbSetup);
const probPool = () => DATA.problemi.filter(p => !$('#p-topic').value || p.theme === $('#p-topic').value);
function pickProblem() {
  const sc = probPool().map(p => { const s = S.probs[p.id]; let v = !s ? 2 : (s.r === 0 ? 3 : (s.r === 1 ? 1 : -0.5)); v += themeWeak(p.theme) * 0.6 + (DATA.pesi[p.theme] || 0) + Math.random(); return [v, p]; }).sort((a, b) => b[0] - a[0]);
  return sc.length ? sc[0][1] : null;
}
$('#p-start').addEventListener('click', () => { const p = pickProblem(); if (!p) return; P = { p, t0: Date.now() }; $('#prob-setup').hidden = true; $('#prob-run').hidden = false; renderProb(); });
function renderProb() {
  const p = P.p;
  $('#prob-run').innerHTML = `<div class="row" style="justify-content:space-between"><span class="pill">${esc(p.theme)}</span><span class="muted">${esc(p.id)}</span></div>
    <div class="q-text">${fmt(p.testo)}</div><p class="hint">Prova a svolgerlo su carta, poi guarda la soluzione.</p>
    <div id="p-sol" hidden><hr style="border:0;border-top:1px solid var(--line);width:100%"><div class="sol">${fmt(p.soluzione)}</div>${p.concetti ? `<p class="hint">Concetti: ${esc(p.concetti)}</p>` : ''}${chapterHint(p.theme)}</div>
    <div class="row"><button class="btn" id="p-show">Mostra la soluzione</button></div>
    <div class="grades" id="p-grades" hidden><button class="btn bad" data-r="0">Non sono riuscito</button><button class="btn ghost" data-r="1">Con dubbi o errori</button><button class="btn good" data-r="2">Svolto bene</button></div>`;
  $('#p-show').addEventListener('click', () => { $('#p-sol').hidden = false; $('#p-show').hidden = true; $('#p-grades').hidden = false; });
  document.querySelectorAll('#p-grades button').forEach(b => b.addEventListener('click', () => {
    const r = +b.dataset.r; S.probs[p.id] = { r, date: todayStr() }; bumpTheme(p.theme, r === 2); save();
    $('#prob-run').hidden = true; $('#prob-setup').hidden = false; renderProbSetup(); say('Registrato');
  }));
}

/* ---------- Schede ---------- */
const STEPS = [0, 1, 3, 7, 14, 30];
let C = null;
const isDue = c => { const s = S.cards[c.id]; return !s || s.due <= todayStr(); };
function renderCardSetup() {
  const mats = ['*', ...Object.keys(DATA.materie)], sel = $('#c-mat').value || '*';
  $('#c-mat').innerHTML = mats.map(m => `<option value="${esc(m)}" ${m === sel ? 'selected' : ''}>${m === '*' ? 'Tutte' : esc(m)}</option>`).join('');
  const all = DATA.cards.filter(c => sel === '*' || c.m === sel), due = all.filter(isDue);
  $('#c-count').textContent = `${due.length} da ripassare su ${all.length}`; $('#c-start').disabled = !due.length;
}
$('#c-mat').addEventListener('change', renderCardSetup);
$('#c-start').addEventListener('click', () => startCards(+$('#c-max').value));
function startCards(max, onEnd) {
  const mat = $('#c-mat').value || '*';
  const due = shuffle(DATA.cards.filter(c => (mat === '*' || c.m === mat) && isDue(c) && !c.lungo)).concat(shuffle(DATA.cards.filter(c => (mat === '*' || c.m === mat) && isDue(c) && c.lungo))).slice(0, max);
  if (!due.length) { if (onEnd) onEnd(); return; }
  C = { q: due, i: 0, known: 0, redo: new Set(), onEnd };
  $('#cards-setup').hidden = true; $('#cards-run').hidden = false; renderCard();
}
function renderCard() {
  if (C.i >= C.q.length) {
    const cb = C.onEnd, k = C.known, n = C.q.length; C = null;
    $('#cards-run').innerHTML = `<h2>Sessione finita</h2><p>Sapevi ${k} schede su ${n}. Quelle sbagliate ricompaiono tra poco e poi domani.</p><div class="row"><button class="btn" id="c-done">${cb ? 'Continua' : 'Torna alle schede'}</button></div>`;
    $('#c-done').addEventListener('click', () => { $('#cards-run').hidden = true; $('#cards-setup').hidden = false; renderCardSetup(); if (cb) cb(); }); $('#c-done').focus(); return;
  }
  const c = C.q[C.i];
  $('#cards-run').innerHTML = `<div class="row" style="justify-content:space-between"><span class="pill">${C.i + 1} di ${C.q.length}</span><span class="muted">${esc(c.t)}</span></div>
    <div class="flash">${fmt(c.d)}</div><div id="c-ans" hidden><hr style="border:0;border-top:1px solid var(--line);width:100%"><div class="flash">${fmt(c.r)}</div></div>
    <div class="row"><button class="btn" id="c-show">Mostra la risposta</button></div>
    <div class="grades" id="c-grades" hidden><button class="btn bad" data-g="0">1 · Da rivedere</button><button class="btn ghost" data-g="1">2 · Difficile</button><button class="btn good" data-g="2">3 · Bene</button><button class="btn good" data-g="3">4 · Facile</button></div>`;
  $('#c-show').addEventListener('click', showCardAnswer); $('#c-show').focus();
  document.querySelectorAll('#c-grades button').forEach(b => b.addEventListener('click', () => gradeCard(+b.dataset.g)));
}
function showCardAnswer() { if (!C || !$('#c-show') || $('#c-show').hidden) return; $('#c-ans').hidden = false; $('#c-show').hidden = true; $('#c-grades').hidden = false; $('#c-grades button').focus(); }
function gradeCard(g) {
  if (!C || $('#c-grades').hidden) return; const c = C.q[C.i];
  const s = S.cards[c.id] || { box: 0 };
  if (g === 0) { s.box = 0; s.due = todayStr(); if (!C.redo.has(c.id)) { C.redo.add(c.id); C.q.push(c); } }
  else { C.known++; s.box = g === 1 ? Math.max(1, s.box) : Math.min(s.box + (g === 3 ? 2 : 1), STEPS.length - 1); s.due = addDays(todayStr(), g === 1 ? 1 : capInterval(STEPS[s.box], c.m)); }
  S.cards[c.id] = s; save(); C.i++; renderCard();
}

/* ---------- Sessione di oggi ---------- */
function startSession() {
  showTab('schede'); $('#c-mat').value = '*';
  const finishQuiz = () => { showTab('oggi'); say('Sessione completata'); };
  const quizPhase = () => {
    showTab('quiz');
    const list = pickQuiz(6, {}).concat(GEN.many(3));
    startQuiz(false, { list, label: 'sessione di oggi', fb: true, onEnd: finishQuiz });
  };
  startCards(10, quizPhase);
}

/* ---------- salvataggio / spostamento progressi ---------- */
$('#exp').addEventListener('click', () => {
  const t = $('#xfer'); t.hidden = false; t.value = JSON.stringify(S); t.select();
  try { navigator.clipboard.writeText(t.value).then(() => { $('#xfer-msg').textContent = 'Copiato negli appunti.'; }, () => { $('#xfer-msg').textContent = 'Seleziona il testo e copialo a mano.'; }); } catch (e) { $('#xfer-msg').textContent = 'Seleziona il testo e copialo a mano.'; }
});
$('#imp').addEventListener('click', () => {
  const t = $('#xfer'); if (t.hidden) { t.hidden = false; t.value = ''; $('#xfer-msg').textContent = 'Incolla qui il testo copiato dall’altro dispositivo e premi di nuovo Importa.'; return; }
  try { const x = JSON.parse(t.value); if (!x || x.v !== 2) throw 0; S = Object.assign({ v: 2, qs: {}, th: {}, hist: [], cards: {}, exams: {}, probs: {} }, x); save(); $('#xfer-msg').textContent = 'Progressi importati.'; renderOggi(); }
  catch (e) { $('#xfer-msg').textContent = 'Testo non valido.'; }
});

/* ---------- scorciatoie da tastiera ---------- */
document.addEventListener('keydown', e => {
  const tag = (e.target && e.target.tagName) || ''; if (/INPUT|TEXTAREA|SELECT/.test(tag) || e.ctrlKey || e.metaKey || e.altKey) return;
  if (Q && !$('#quiz-run').hidden) {
    if (/^[1-5]$/.test(e.key) && !Q.answered) { if (+e.key <= Q.list[Q.i].o.length) answer(+e.key); }
    else if ((e.key === 'Enter' || e.key === ' ') && Q.answered && document.activeElement !== $('#q-next')) { e.preventDefault(); nextQ(); }
  } else if (C && !$('#cards-run').hidden) {
    if ((e.key === 'Enter' || e.key === ' ') && $('#c-show') && !$('#c-show').hidden && document.activeElement !== $('#c-show')) { e.preventDefault(); showCardAnswer(); }
    else if (/^[1-4]$/.test(e.key) && $('#c-grades') && !$('#c-grades').hidden) gradeCard(+e.key - 1);
  }
});

/* ---------- avvio ---------- */
function boot(d) {
  DATA = d;
  if (SERVER) { const m = $('#xfer-p'); if (m) m.textContent = 'I progressi sono salvati anche nel file progressi.json del computer, quindi restano cambiando browser. Qui puoi comunque copiarli a mano.'; }
  DATA.quiz.forEach(q => { q.theme = themeOf(q.args); });
  DATA.problemi.forEach(p => { p.theme = themeOf(p.args); });
  showTab((location.hash || '').replace('#', '') || 'oggi');
}
loadServerState().then(() => fetch('data.json')).then(r => { if (!r.ok) throw new Error(r.status); return r.json(); }).then(boot).catch(err => {
  const e = $('#load-err'); e.hidden = false; e.textContent = 'Non riesco a caricare i dati (' + err.message + '). Ricarica la pagina; se resta così, avvisa chi l\'ha pubblicata.';
});
