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

BOTTONI = ('<a class="icon-btn" href="riassunti/" title="Riassunti" aria-label="Riassunti" '
           'style="width:auto;padding:0 12px;font:600 .9rem var(--font-body);text-decoration:none;display:inline-flex;align-items:center">Riassunti</a>'
           '<button class="icon-btn" id="logout-btn" title="Esci (__QUSER__)" aria-label="Esci" '
           'style="width:auto;padding:0 12px;font:600 .9rem var(--font-body)">Esci</button>')
LOGOUT_JS = ("<script>document.addEventListener('DOMContentLoaded',function(){var b=document.getElementById('logout-btn');"
             "if(b)b.addEventListener('click',function(){fetch('/api/logout',{method:'POST'}).then(function(){location.href='/login.html'})})});</script>")


def adatta(html):
    n0 = len(html)
    # memoria del browser separata per utente (sullo stesso computer possono entrare più persone)
    html, k = re.subn(r"const LS_KEY = '([^']+)';", r"const LS_KEY = '\1:__QUSER__';", html, count=1)
    assert k == 1, "LS_KEY non trovato in index.html"
    html, k = re.subn(r"\$\{greeting\(\)\} Emanuele", "${greeting()} __QNOME__", html, count=1)
    assert k == 1, "saluto non trovato"
    html, k = re.subn(r'<div class="tools">', '<div class="tools">' + BOTTONI, html, count=1)
    assert k == 1, "contenitore .tools non trovato"
    if "robots" not in html.lower():
        html = html.replace("<head>", '<head><meta name="robots" content="noindex,nofollow,noarchive">', 1)
    html = html.replace("</body>", LOGOUT_JS + "</body>", 1)
    return html


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
    print(r.stdout.strip());
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
