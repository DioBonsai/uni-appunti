"""Controllo della migrazione: gli intervalli evidenziati, applicati al testo dei blocchi (letto come lo legge il browser),
devono ricadere esattamente sul testo che era evidenziato nel Word. Uso: python verifica_migrazione.py [--repo CARTELLA]"""
import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path

REPO = Path.home() / "Documents" / "GitHub" / "quaderno-privato"


class Testo(HTMLParser):
    """Testo di un frammento HTML come textContent del DOM (entità decodificate, <br> senza caratteri)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.t = []

    def handle_data(self, d):
        self.t.append(d)


def testo_html(h):
    p = Testo()
    p.feed(h)
    return "".join(p.t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(REPO))
    a = ap.parse_args()
    cont = Path(a.repo) / "contenuti"
    seed = json.loads((cont / "_seed_evidenziazioni.json").read_text(encoding="utf-8"))["evid"]
    ver = json.loads((cont / "_verifica_testi.json").read_text(encoding="utf-8"))
    tot = ok = 0
    errori = []
    for slug, evid in seed.items():
        data = json.loads((cont / f"{slug}.json").read_text(encoding="utf-8"))
        blocchi = {}
        for c in [{"blocks": data["preambolo"]}] + data["capitoli"]:
            for b in c["blocks"]:
                if b.get("b"):
                    blocchi[b["b"]] = b
        for bid, rng in evid.items():
            b = blocchi.get(bid)
            tot += 1
            if b is None:
                errori.append(f"{slug} {bid}: blocco mancante"); continue
            tx = testo_html(b["h"])
            enc = tx.encode("utf-16-le")
            letti = [enc[x * 2:y * 2].decode("utf-16-le", errors="replace") for x, y in rng]
            if letti == ver[slug][bid]:
                ok += 1
            else:
                errori.append(f"{slug} {bid}: atteso {ver[slug][bid][:2]!r} letto {letti[:2]!r}")
    print(f"blocchi evidenziati: {tot}, coerenti: {ok}, errori: {len(errori)}")
    for e in errori[:15]:
        print(" -", e[:200])
    return 0 if not errori else 1


if __name__ == "__main__":
    sys.exit(main())
