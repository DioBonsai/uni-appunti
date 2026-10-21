"""Genera orario_lezioni_B.ics (importabile in Google Calendar) da orario_lezioni_B.txt.
Righe: AAAA-MM-GGTHH:MM|fine HH:MM|sigla|docenti. Fuso Europe/Rome. Nessun laboratorio (solo mattina)."""
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
NOMI = {
    "FDA B": "Fondamenti dell'Informatica",
    "Prog I B": "Programmazione I",
    "MDAG-B modA": "Matematica discreta, Algebra e Geometria (mod. A)",
    "MDAG-B modB": "Matematica discreta, Algebra e Geometria (mod. B)",
}
VTZ = """BEGIN:VTIMEZONE
TZID:Europe/Rome
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE"""


def main():
    righe = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Quaderno//Orario B//IT", "CALSCALE:GREGORIAN", VTZ]
    n = 0
    for r in (BASE / "orario_lezioni_B.txt").read_text(encoding="utf-8").splitlines():
        if not r.strip():
            continue
        ini, fine, sigla, doc = r.split("|")
        g = ini[:10].replace("-", "")
        h1 = ini[11:].replace(":", "") + "00"
        h2 = fine.replace(":", "") + "00"
        n += 1
        righe += [
            "BEGIN:VEVENT",
            f"UID:lez-{g}-{h1}-{sigla.replace(' ', '')}@quaderno",
            "DTSTAMP:20261021T080000Z",
            f"DTSTART;TZID=Europe/Rome:{g}T{h1}",
            f"DTEND;TZID=Europe/Rome:{g}T{h2}",
            f"SUMMARY:{NOMI[sigla]}",
            "LOCATION:Aula B\\, Dipartimento di Informatica\\, Via Pessinetto 12\\, Torino",
            f"DESCRIPTION:Docenti: {doc.replace(',', ', ')}. Canale B (cognomi E-O).",
            "END:VEVENT",
        ]
    righe.append("END:VCALENDAR")
    out = BASE / "orario_lezioni_B.ics"
    out.write_text("\r\n".join(righe) + "\r\n", encoding="utf-8")
    print(f"{n} lezioni -> {out}")


if __name__ == "__main__":
    main()
