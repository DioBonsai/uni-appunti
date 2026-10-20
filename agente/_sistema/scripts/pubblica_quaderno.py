"""Prepara (e, con --push, pubblica) il Quaderno online: ricostruisce la pagina dai Word, quiz, problemi e schede,
converte i riassunti e copia tutto nella cartella protected/ del repo privato quaderno-privato.
Vercel pubblica da solo ogni volta che il repo riceve un nuovo commit.

Uso:  python pubblica_quaderno.py [--repo CARTELLA] [--push] [--no-build]
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
BASE = SCRIPTS.parent
PAG = BASE / "pagina_studio"
REPO_DEFAULT = Path.home() / "Documents" / "GitHub" / "quaderno-privato"

IC_LIBRO = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 19V5.5M8.5 7.5h7M8.5 11h5"/></svg>'
IC_ESCI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h3M16 8l4 4-4 4M20 12H9"/></svg>'

# voce "Riassunti" nel menu (schermi grandi), nella barra in basso (telefono) e pulsante Esci
TABLINK = f'<a class="tablink" href="riassunti/">{IC_LIBRO}<span>Riassunti</span></a>'
BNLINK = f'<a class="bnlink" href="riassunti/">{IC_LIBRO}<span>Riassunti</span></a>'
ESCI = f'<button class="icon-btn" id="logout-btn" title="Esci (__QUSER__)" aria-label="Esci">{IC_ESCI}</button>'
CSS_EXTRA = """<style>
.seg .tablink{position:relative;z-index:1;display:inline-flex;align-items:center;gap:8px;text-decoration:none;color:var(--muted);font:600 .98rem var(--font-body);min-height:44px;padding:0 18px;border-radius:10px;white-space:nowrap;transition:color .2s}
.seg .tablink svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.seg .tablink:hover{color:var(--accent)}
.seg .tablink::before{content:"";position:absolute;left:-2px;top:12px;bottom:12px;width:1px;background:var(--line)}
.icon-btn svg{fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.subj-read{display:inline-flex;align-items:center;gap:6px;margin:0 16px 12px;padding:6px 12px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font:700 .84rem var(--font-body);text-decoration:none}
.subj-read:hover{filter:brightness(.95)}
.sq-label a{font-weight:700;color:var(--accent)}
@media (max-width:719px){
  .sq{width:40px!important;height:40px!important}
  .subj-read{min-height:44px;margin-bottom:14px}
  .chips-pick > *,.tchip{min-height:44px}
  .bn span,.bnlink span{font-size:.75rem}
  .bottomnav{grid-template-columns:repeat(5,1fr)!important}
  .bnlink{appearance:none;border:0;background:none;color:var(--muted);font:600 .72rem var(--font-body);min-height:56px;display:grid;justify-items:center;align-content:center;gap:3px;border-radius:14px;text-decoration:none;position:relative}
  .bnlink svg{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .bnlink:active{transform:scale(.96)}
}
</style>"""
# meta per usare il Quaderno come app dalla schermata Home del telefono, e per non finire sui motori di ricerca
PWA = ('<meta name="robots" content="noindex,nofollow,noarchive">'
       '<link rel="manifest" href="/manifest.webmanifest"><link rel="apple-touch-icon" href="/apple-touch-icon.png">'
       '<meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-capable" content="yes">'
       '<meta name="apple-mobile-web-app-title" content="Quaderno">')
RSLUG = ('const RSLUG = {"Algebra lineare":"algebra","Matematica discreta":"matematica-discreta","Fondamenti Info":"fondamenti",'
         '"Programmazione":"programmazione","Programmazione, Laboratorio":"laboratorio"};')
LOGOUT_JS = ("<script>document.addEventListener('DOMContentLoaded',function(){var b=document.getElementById('logout-btn');"
             "if(b)b.addEventListener('click',function(){fetch('/api/logout',{method:'POST'}).then(function(){location.href='/login.html'})})});</script>")


def sostituisci(html, vecchio, nuovo, nome, regex=False):
    if regex:
        html, k = re.subn(vecchio, lambda m: nuovo(m) if callable(nuovo) else nuovo, html, count=1)
    else:
        k = html.count(vecchio)
        html = html.replace(vecchio, nuovo, 1)
    assert k >= 1, f"{nome}: punto di aggancio non trovato in index.html"
    return html


def adatta(html):
    # memoria del browser separata per utente (sullo stesso computer possono entrare più persone)
    html = sostituisci(html, r"const LS_KEY = '([^']+)';", lambda m: f"const LS_KEY = '{m.group(1)}:__QUSER__';", "LS_KEY", regex=True)
    html = sostituisci(html, r"\$\{greeting\(\)\} Emanuele", "${greeting()} __QNOME__", "saluto", regex=True)
    # "Riassunti" come voce del menu (schermi grandi) e della barra in basso (telefono)
    html = sostituisci(html, r"(Schede</button>\s*)(</nav>)", lambda m: m.group(1) + TABLINK + m.group(2), "menu", regex=True)
    html = sostituisci(html, r"(<span>Schede</span></button>\s*)(</nav>)", lambda m: m.group(1) + BNLINK + m.group(2), "barra in basso", regex=True)
    # pulsante Esci accanto al tema e alle impostazioni
    html = sostituisci(html, '<div class="tools">', '<div class="tools">' + ESCI, "strumenti")
    # link ai riassunti dalle carte delle materie e dai quadratini dei capitoli
    html = sostituisci(html, "let DATA = null;", "let DATA = null; " + RSLUG, "RSLUG")
    html = sostituisci(html, '<div class="squares" role="group"',
                       '<a class="subj-read" href="riassunti/${RSLUG[m] || \'\'}.html">Leggi il riassunto &rarr;</a><div class="squares" role="group"', "carta materia")
    html = sostituisci(html, "${esc(b.dataset.t)} · ${st}`;",
                       "${esc(b.dataset.t)} · ${st} · <a href=\"riassunti/${RSLUG[card.dataset.m] || ''}.html#cap${b.dataset.n}\">Leggi</a>`;", "etichetta capitolo")
    html = sostituisci(html, "</style>", "</style>" + CSS_EXTRA, "stile")
    # la pagina costruita è un frammento (niente <head>/<body>): meta noindex all'inizio, script di uscita in fondo
    if "robots" not in html.lower():
        html = PWA + chr(10) + html
    return html + chr(10) + LOGOUT_JS + chr(10)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(REPO_DEFAULT))
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--no-build", action="store_true")
    a = ap.parse_args()
    repo = Path(a.repo)
    if not (repo / "vercel.json").exists():
        print("Repo del sito non trovato:", repo); return 1
    py = sys.executable
    if not a.no_build:
        r = subprocess.run([py, "-X", "utf8", str(SCRIPTS / "costruisci_pagina_studio.py")], capture_output=True, text=True, encoding="utf-8")
        if r.returncode:
            print(r.stdout, r.stderr); return 1
        print((r.stdout.strip().splitlines() or ["build ok"])[0])
    dest = repo / "protected"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    (dest / "index.html").write_text(adatta((PAG / "index.html").read_text(encoding="utf-8")), encoding="utf-8")
    shutil.copy2(PAG / "data.json", dest / "data.json")
    if (PAG / "img").exists():
        shutil.copytree(PAG / "img", dest / "img")
    r = subprocess.run([py, "-X", "utf8", "-W", "ignore", str(SCRIPTS / "riassunti_html.py"), str(dest)], capture_output=True, text=True, encoding="utf-8")
    print(r.stdout.strip())
    if r.returncode:
        print(r.stderr); return 1
    tot = sum(f.stat().st_size for f in dest.rglob("*") if f.is_file()) / 1048576
    print(f"protected/ pronta: {tot:.1f} MB")
    if a.push:
        g = lambda *x: subprocess.run(["git", "-C", str(repo), *x], capture_output=True, text=True, encoding="utf-8")
        g("add", "-A")
        if not g("status", "--porcelain").stdout.strip():
            print("Nessuna modifica da pubblicare."); return 0
        msg = "Aggiornamento contenuti\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
        g("commit", "-q", "-m", msg)
        p = g("push", "-q")
        print("Pubblicato su GitHub (Vercel aggiorna il sito da solo)." if p.returncode == 0 else "Push non riuscito: " + p.stderr.strip())
        return p.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
