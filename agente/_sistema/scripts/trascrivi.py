"""Trascrive gli audio delle lezioni con faster-whisper (CPU, italiano).

Uso:
    python trascrivi.py                 # tutti gli audio in _sistema/audio non ancora trascritti
    python trascrivi.py algebra_L1.m4a  # un solo file
    python trascrivi.py --model medium  # modello piu' accurato (piu' lento)

Output: _sistema/trascrizioni/<nome>.txt con un blocco ogni ~30 secondi: [mm:ss] testo
I file gia' trascritti vengono saltati, quindi lo script si puo' rilanciare e riprende.
"""
import argparse
import sys
import time
from pathlib import Path

from faster_whisper import WhisperModel

BASE = Path(__file__).resolve().parent.parent
AUDIO = BASE / "audio"
OUT = BASE / "trascrizioni"
EXT = {".m4a", ".mp3", ".wav", ".mp4", ".ogg", ".flac"}

# Termini del corso: aiutano Whisper a scrivere correttamente il lessico tecnico.
PROMPT = (
    "Lezione universitaria di informatica in italiano: algebra lineare, numeri complessi, "
    "spazi vettoriali, matematica discreta, insiemi, relazioni di equivalenza, induzione, "
    "fondamenti dell'informatica, bit, complemento a due, virgola mobile, programmazione in C, "
    "variabili, stack, CPU, memoria."
)


def load_glossary() -> str:
    """Aggiunge al prompt i termini di `glossario.txt` (uno per riga), cosi' Whisper li scrive bene."""
    g = BASE / "glossario.txt"
    if not g.exists():
        return PROMPT
    terms = [l.strip() for l in g.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    return PROMPT + " Termini: " + ", ".join(terms[:150]) + "."


def fmt(sec: float) -> str:
    sec = int(sec)
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}" if sec >= 3600 else f"{sec // 60:02d}:{sec % 60:02d}"


def transcribe(model: WhisperModel, src: Path) -> None:
    dst = OUT / (src.stem + ".txt")
    tmp = dst.with_suffix(".part")
    t0 = time.time()
    segments, info = model.transcribe(
        str(src),
        language="it",
        vad_filter=True,
        beam_size=5,
        initial_prompt=load_glossary(),
        condition_on_previous_text=False,
    )
    print(f"{src.name}: durata {fmt(info.duration)}", flush=True)
    block_start, block = 0.0, []
    with tmp.open("w", encoding="utf-8") as f:
        for seg in segments:
            if not block:
                block_start = seg.start
            block.append(seg.text.strip())
            if seg.end - block_start >= 30:
                f.write(f"[{fmt(block_start)}] {' '.join(block)}\n")
                f.flush()
                block = []
                done = seg.end / info.duration * 100
                print(f"  {done:5.1f}%  ({int(time.time() - t0)}s)", end="\r", flush=True)
        if block:
            f.write(f"[{fmt(block_start)}] {' '.join(block)}\n")
    tmp.replace(dst)
    print(f"\n  fatto in {int(time.time() - t0)}s -> {dst.name}", flush=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--model", default="small", help="tiny|base|small|medium|large-v3 (default small)")
    args = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    if args.files:
        todo = [AUDIO / f if not Path(f).is_absolute() else Path(f) for f in args.files]
    else:
        todo = sorted(p for p in AUDIO.iterdir() if p.suffix.lower() in EXT)
    todo = [p for p in todo if not (OUT / (p.stem + ".txt")).exists()]
    if not todo:
        print("Niente da trascrivere.")
        return

    print(f"Carico il modello '{args.model}' (la prima volta lo scarica)...", flush=True)
    model = WhisperModel(args.model, device="cpu", compute_type="int8", cpu_threads=0)
    for p in todo:
        if not p.exists():
            print(f"manca: {p}", file=sys.stderr)
            continue
        transcribe(model, p)


if __name__ == "__main__":
    main()
