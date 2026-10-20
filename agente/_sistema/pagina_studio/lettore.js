/* Lettore dei riassunti dentro il Quaderno, con sottolineature.
   Le pagine riassunti/<materia>/index.html (pandoc) si leggono qui; si seleziona un testo e si preme «Sottolinea».
   Ogni sottolineatura {id, m, q, p, s, h, t} (m materia, q testo, p/s contesto nel blocco, h titolo vicino) si salva in:
   - localStorage (sempre), - api/sottolineature del server locale (file _sistema/sottolineature.json), - db «sottolineature» se la pagina è
   pubblicata. applica_sottolineature.py le riporta nei Word. */
(function () {
  const BLOCCHI = 'p,li,td,th,h1,h2,h3,h4,h5,h6,dd,dt,figcaption,blockquote,pre';
  const LS_SOTT = 'quaderno-sott';
  const lista = $('#riass-lista'), lettore = $('#riass-lettore'), art = $('#r-art'), ind = $('#r-indice'), pill = $('#r-pill');
  let slug = null, voci = new Map(), db = null, range = null, tolta = null;

  /* ---------- salvataggio ---------- */
  const hash = s => { let h = 5381; for (let i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) | 0; return (h >>> 0).toString(36); };
  const salvaLocale = () => { try { localStorage.setItem(LS_SOTT, JSON.stringify([...voci.values()])); } catch (e) {} };
  const postServer = body => SERVER ? fetch('api/sottolineature', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) }).catch(() => {}) : null;
  async function caricaVoci() {
    voci = new Map();
    try { (JSON.parse(localStorage.getItem(LS_SOTT) || '[]')).forEach(v => voci.set(v.id, v)); } catch (e) {}
    if (SERVER) { try { const r = await fetch('api/sottolineature'); if (r.ok) (await r.json()).items.forEach(v => voci.set(v.id, v)); } catch (e) {} }
    try {
      if (window.claude && claude.use) db = await claude.use('db');
      if (db) (await db.collection('sottolineature').get()).docs.forEach(d => { const v = d.data(); if (v && v.id) voci.set(v.id, v); });
    } catch (e) { db = null; }
    salvaLocale();
    // quello che c'è solo in un posto si copia anche negli altri
    if (SERVER && voci.size) postServer({ add: [...voci.values()], del: [] });
    if (db) { try { for (const v of voci.values()) await db.collection('sottolineature').doc(v.id).set(v); } catch (e) {} }
  }
  async function aggiungi(v) {
    voci.set(v.id, v); salvaLocale(); postServer({ add: [v], del: [] });
    if (db) { try { await db.collection('sottolineature').doc(v.id).set(v); } catch (e) { toast('Salvata solo su questo dispositivo'); } }
  }
  async function togli(id) {
    voci.delete(id); salvaLocale(); postServer({ add: [], del: [id] });
    if (db) { try { await db.collection('sottolineature').doc(id).delete(); } catch (e) {} }
  }

  /* ---------- testo dei blocchi (senza le formule: nel Word non ci sono come testo) ---------- */
  const fuoriFormule = n => !n.parentElement.closest('math,script,style');
  function nodiTesto(el) {
    const out = [], w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    for (let n = w.nextNode(); n; n = w.nextNode()) if (fuoriFormule(n) && n.parentElement.closest(BLOCCHI) === el) out.push(n);
    return out;
  }
  const testoDi = nodi => nodi.map(n => n.data).join('');
  const blocchi = () => [...art.querySelectorAll(BLOCCHI)].filter(b => nodiTesto(b).length);
  const titoloPrima = (el, tit) => { let t = ''; for (const h of tit) { if (h.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING) t = h.textContent.trim(); else break; } return t; };
  const norm = s => s.replace(/[\s ]+/g, ' ');

  /* ---------- selezione -> voci ---------- */
  function vociDaSelezione(r) {
    const tit = [...art.querySelectorAll('h1,h2,h3,h4')], out = [];
    for (const b of blocchi()) {
      if (!r.intersectsNode(b)) continue;
      const nodi = nodiTesto(b), tot = testoDi(nodi);
      let a = -1, z = -1, pos = 0;
      for (const n of nodi) {
        const len = n.data.length;
        if (r.intersectsNode(n)) {
          const ini = n === r.startContainer ? r.startOffset : 0, fin = n === r.endContainer ? r.endOffset : len;
          if (fin > ini) { if (a < 0) a = pos + ini; z = pos + fin; }
        }
        pos += len;
      }
      if (a < 0) continue;
      while (a < z && /\s/.test(tot[a])) a++;
      while (z > a && /\s/.test(tot[z - 1])) z--;
      if (z - a < 2) continue;
      const q = tot.slice(a, z), p = tot.slice(Math.max(0, a - 30), a), s = tot.slice(z, z + 30), h = titoloPrima(b, tit);
      out.push({ id: hash(slug + '|' + h + '|' + p + '|' + q + '|' + s), m: slug, q, p, s, h, t: new Date().toISOString().slice(0, 10) });
    }
    return out;
  }

  /* ---------- disegno ---------- */
  function avvolgi(b, a, z, id) {
    const nodi = nodiTesto(b); let pos = 0; const segm = [];
    for (const n of nodi) { const len = n.data.length, x = Math.max(a, pos), y = Math.min(z, pos + len); if (y > x) segm.push([n, x - pos, y - pos]); pos += len; }
    for (const [n, x, y] of segm.reverse()) {
      const r = document.createRange(); r.setStart(n, x); r.setEnd(n, y);
      const m = document.createElement('mark'); m.className = 'ut'; m.dataset.id = id; r.surroundContents(m);
    }
  }
  const giaEvidenziato = (b, a, z) => { // tutto il tratto sta già in un'evidenziazione del Word
    const nodi = nodiTesto(b); let pos = 0, tot = 0, hl = 0;
    for (const n of nodi) { const len = n.data.length, x = Math.max(a, pos), y = Math.min(z, pos + len); if (y > x) { tot += y - x; if (n.parentElement.closest('mark')) hl += y - x; } pos += len; }
    return tot > 0 && hl === tot;
  };
  function disegna(v, bl, tit) {
    const q = norm(v.q); if (!q) return false;
    let miglior = null;
    for (const b of bl) {
      const nodi = nodiTesto(b), tot = testoDi(nodi), n = norm(tot);
      if (n.indexOf(q) < 0) continue;
      // posizioni nel testo originale: si lavora sul testo non normalizzato quando coincide, altrimenti si cerca tollerando gli spazi
      const re = new RegExp(q.split(' ').map(x => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('[\\s\\u00a0]+'), 'g');
      let m; while ((m = re.exec(tot))) {
        const ctx = tot.slice(0, m.index).endsWith(v.p) && tot.slice(m.index + m[0].length).startsWith(v.s);
        const stessoTit = titoloPrima(b, tit) === v.h;
        const punti = (ctx ? 2 : 0) + (stessoTit ? 1 : 0);
        if (!miglior || punti > miglior.punti) miglior = { b, a: m.index, z: m.index + m[0].length, punti };
        if (m[0].length === 0) re.lastIndex++;
      }
    }
    if (!miglior) return false;
    if (giaEvidenziato(miglior.b, miglior.a, miglior.z)) return true;
    avvolgi(miglior.b, miglior.a, miglior.z, v.id);
    return true;
  }
  function ridisegna() {
    art.querySelectorAll('mark.ut').forEach(m => { const p = m.parentNode; while (m.firstChild) p.insertBefore(m.firstChild, m); p.removeChild(m); p.normalize(); });
    const bl = blocchi(), tit = [...art.querySelectorAll('h1,h2,h3,h4')];
    for (const v of voci.values()) if (v.m === slug) disegna(v, bl, tit);
  }

  /* ---------- apertura del lettore ---------- */
  async function apri(sl, titolo, ancora) {
    slug = sl; $('#r-titolo').textContent = titolo;
    lista.hidden = true; lettore.hidden = false; art.textContent = 'Carico…'; ind.textContent = '';
    try {
      const r = await fetch('riassunti/' + sl + '/index.html'); if (!r.ok) throw new Error(r.status);
      const d = new DOMParser().parseFromString(await r.text(), 'text/html');
      d.querySelectorAll('img').forEach(i => i.setAttribute('src', 'riassunti/' + sl + '/' + i.getAttribute('src').replace(/^\.\//, '')));
      art.innerHTML = d.querySelector('article').innerHTML; ind.innerHTML = d.querySelector('nav#indice').innerHTML;
    } catch (e) { art.textContent = 'Non riesco a caricare il riassunto (' + e.message + ').'; return; }
    await caricaVoci(); ridisegna();
    try { history.replaceState(null, '', '#riassunti'); localStorage.setItem('quaderno-riass', sl); } catch (e) {}
    window.scrollTo(0, 0);
    if (ancora) { const el = document.getElementById(ancora); if (el) el.scrollIntoView(); }
  }
  function chiudi() { lettore.hidden = true; lista.hidden = false; slug = null; nascondiPill(); window.scrollTo(0, 0); }

  lista.addEventListener('click', e => {
    const a = e.target.closest('a[data-slug]'); if (!a) return;
    e.preventDefault(); apri(a.dataset.slug, a.querySelector('b').textContent);
  });
  $('#r-indietro').addEventListener('click', chiudi);
  $('#r-btn-indice').addEventListener('click', () => { const o = ind.classList.toggle('aperto'); $('#r-btn-indice').textContent = o ? 'Chiudi' : 'Indice'; });
  ind.addEventListener('click', e => {
    const a = e.target.closest('a'); if (!a) return; e.preventDefault();
    const el = document.getElementById(decodeURIComponent((a.getAttribute('href') || '').replace(/^#/, '')));
    ind.classList.remove('aperto'); $('#r-btn-indice').textContent = 'Indice'; if (el) el.scrollIntoView();
  });
  // uscendo dalla scheda si torna all'elenco la volta dopo
  document.querySelectorAll('.tab, .bn').forEach(b => b.addEventListener('click', () => { if (b.dataset.tab !== 'riassunti') nascondiPill(); }));

  /* ---------- pulsante Sottolinea / Rimuovi ---------- */
  function mostraPill(testo, azione) { pill.textContent = testo; pill.hidden = false; pill.onclick = azione; }
  function nascondiPill() { pill.hidden = true; pill.onclick = null; range = null; tolta = null; }
  pill.addEventListener('pointerdown', e => e.preventDefault());   // non far sparire la selezione
  document.addEventListener('selectionchange', () => {
    if (!slug) return;
    const sel = getSelection();
    if (!sel || sel.isCollapsed || !sel.rangeCount || !art.contains(sel.anchorNode) || !art.contains(sel.focusNode)) { if (!tolta) nascondiPill(); return; }
    range = sel.getRangeAt(0).cloneRange(); tolta = null;
    mostraPill('Sottolinea', async () => {
      const nuove = vociDaSelezione(range); getSelection().removeAllRanges();
      if (!nuove.length) { nascondiPill(); return; }
      for (const v of nuove) await aggiungi(v);
      ridisegna(); nascondiPill(); toast(nuove.length === 1 ? 'Sottolineato' : 'Sottolineati ' + nuove.length + ' pezzi');
    });
  });
  art.addEventListener('click', e => {
    const m = e.target.closest('mark.ut'); if (!m || !getSelection().isCollapsed) return;
    tolta = m.dataset.id;
    mostraPill('Togli sottolineatura', async () => { await togli(tolta); ridisegna(); nascondiPill(); toast('Tolta'); });
  });
  document.addEventListener('click', e => { if (tolta && !e.target.closest('mark.ut') && e.target !== pill) nascondiPill(); });
})();
