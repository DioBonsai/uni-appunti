# Stato dei riassunti (aggiornato 8 ott 2026)

Legenda: ✅ nel Word | ⏳ da fare | ❓ da decidere

## Algebra lineare (Buzano/Radeschi) – `Riassunto Algebra lineare.docx`
Il Word ha 13 capitoli (aggiunti 10-13 il 12 ott). Prossima numerazione: **14**. Il 13 ott 2026 (su richiesta di Emanuele) sono state inserite 14 figure nei capitoli 1-13 (`_sistema/scripts/figure_alg.py` + `inserisci_figure.py`, piano in `_sistema/figure/alg/piano.json`); testo invariato.
| Lez. | Data | Argomenti | Word | Fonti disponibili |
|---|---|---|---|---|
| L1 | 30 set | Vettori/mappe lineari, insiemi numerici, campi | ✅ cap. 1-2 | appunti, nota, audio, dispense cap.1 |
| L2 | 5 ott | Complessi: forma algebrica, campo, coniugato/modulo/inverso, piano di Argand | ✅ cap. 3-6 | appunti (foto quaderno), audio 2A/2B, dispense cap.2 |
| L3 | 7 ott | Coordinate polari, e^{iθ}, prodotto, inverso, potenze, radici n-esime | ✅ cap. 7-9 | appunti, scheda, dispense cap.3 (audio non presente) |
| L4 | 12 ott | Polinomi: monomi, grado, ℝ[x]/ℂ[x]/ℝₖ[x], divisione con resto, radici e molteplicità, al più n radici (induzione), discriminante, teorema fondamentale dell'algebra | ✅ cap. 10-13 | appunti 12 ott, audio 4A/4B, dispense cap.4 |
Dispense: 26 lezioni; prossime L4 Polinomi, L5-7 Spazi vettoriali.

## Matematica discreta (Mori) – `Riassunto Matematica discreta.docx`
Il Word ha 19 capitoli. Prossima numerazione: **20**. Il 13 ott 2026 (su richiesta di Emanuele) sono state inserite 39 figure nei capitoli 1-19 con `_sistema/scripts/inserisci_figure.py` (piano in `_sistema/figure/mate/piano.json`, generatore `figure_mate.py`); testo ed evidenziazioni invariati.
| Lez. | Data | Argomenti | Word |
|---|---|---|---|
| L1 | 1 ott | Insiemi, operazioni, prodotto cartesiano | ✅ cap. 1-3 |
| L2 | 2 ott | Differenza, De Morgan, insieme delle parti, Peano, induzione, partizioni | ✅ cap. 4-6 |
| L3 | 6 ott | Quoziente, relazioni, equivalenze, classi, funzioni come grafico | ✅ cap. 7-9 |
| L4 | 8 ott | Funzioni: notazioni, notevoli, restrizione, quoziente, immagine/controimmagine, iniettiva/suriettiva, composizione, inversa | ✅ cap. 10-15 (il cap. 15 da appunti e scheda, non in audio) |
| L5 | 9 ott | Esempi inietti/suriett., rendere biettiva (x², seno), composizione e associatività, composte e inverse | ✅ cap. 16-19 (audio 5B incompleto: ~30 min mancanti coperti dagli appunti) |
Fonti: appunti a mano, schede, libro Mori (scansione), audio L1-L2 (manca L3).
Nota: negli appunti del 2 ott la condizione delle partizioni è scritta `Ai ∩ Aj ≠ ∅` (typo, deve essere `= ∅`).

## Fondamenti dell'Informatica (Brookshear) – `Riassunto Fondamenti Informatica.docx`
Word con 15 capitoli (cap. 12-15 aggiunti il 12 ott: logica proposizionale, lezione 4 del corso) (rinumerati l'8 ott: era "6." due volte). Contenuto duplicato unito l'8 ott: memoria di massa solo nel cap. 3 (con i dettagli del cap. 5 aggiunti), ASCII/Unicode e RGB solo nel cap. 4; i cap. 5 e 6 rimandano. Refusi corretti l'8 ott. Cap. 3-4 e 8-10 hanno le evidenziazioni di Emanuele (non toccarle). Il 13 ott 2026 (su richiesta di Emanuele) inserite 13 figure (`figure_info.py`, piano in `_sistema/figure/fond/piano.json`); testo ed evidenziazioni invariati.
Coperti: 1.1-1.7, 1.9, 1.10. La sez. 1.8 (Python) è OMESSA dal docente nel 2026: nulla da fare. Audio L1, L3.
| L4 (corso) | 12 ott | Logica proposizionale: proposizioni, connettivi (and, or, xor, not, equivalenza), tavole di verità, equivalenze, tautologie e contraddizioni (PDF «Parte 2, 1.2 Propositions» + audio) | ✅ cap. 12-15 (restano da fare: implicazione e regole di inferenza, prossima lezione) |

## Programmazione I (Amparore) – `Riassunto Programmazione.docx`
Word con 20 capitoli (aggiunti 13-16 il 14 ott dalle slide 03A/03B del 13 ott: scambio di variabili, float/double e formati, math.h, conversioni di tipo; aggiunti 17-20 il 14 ott dalle slide 03C e 03D: espressioni booleane, intervalli/cortocircuitazione/ternario, controllo di flusso e if, errori comuni/visibilità/schemi con if). Prossima numerazione: **21** (iterazione: while/for/do-while quando escono le slide). Nota: la registrazione di Programmazione del 13 ott (ProgI-13ott.mp4, Moodle) ha l audio quasi vuoto, quindi non e usabile; trascrizione parziale in _sistema/trascrizioni. Resta Lab01 (laboratorio) da decidere. Il 13 ott 2026 (su richiesta di Emanuele) inserite 12 figure (`figure_info.py`, piano in `_sistema/figure/prog/piano.json`); testo ed evidenziazioni invariati.
Corretti l'8 ott: ALU (Arithmetic Logic Unit) e titoli dei capitoli 6-7 ("Capitolo N:"). I numeri spuri visti nell'XML non erano nel testo visibile.

## Programmazione, Laboratorio – `Riassunto Laboratorio.docx` (riassunto a parte, numerazione propria)
Creato il 9 ott 2026 dalle slide `Lab01 - Introduzione` (laboratorio n. 1). 5 capitoli: 1 organizzazione del laboratorio, 2 interfaccia a riga di comando, 3 ambiente per programmare in C (gcc, MinGW, PATH, editor), 4 compilazione (gcc -c, linker, -Wall -Werror, objdump), 5 primi programmi (scrivi_intero.c, tabella_moltiplicazioni.c, esercizi). Il 14 ott aggiunti i cap. 6-7 dalle slide Lab02 «Operatori e Tipi» (operatori, ordine di valutazione, errori; tipi, documentazione, esercizi mercato e scambio4; le soluzioni degli esercizi sono dedotte e verificate, non nelle slide). Prossima numerazione: **8** (lab n. 3). Nessuna evidenziazione: da studiare.

## Pulizie da fare (fase 2)
- [x] Fondamenti: rinumerato, corretti refusi ("Nascosto", "dell me", "movement", frase spezzata "all'addizionatore") [8 ott]; [x] contenuto duplicato unito [8 ott]
- [x] Programmazione: correzioni [8 ott]
- [x] Algebra: aggiunti cap. 7-9 (L3) [8 ott]
- [x] Stili Titolo 1/2 veri su tutti e 4 i Word (navigazione e indice automatico) [8 ott]
- [ ] Mate discreta: controllo notazione partizioni
- [x] Git + GitHub privato (DioBonsai/uni-appunti) [8 ott]

## Cosa ha già studiato Emanuele (le evidenziazioni gialle nei Word = studiato a mano)
Regola: i capitoli/paragrafi con evidenziazioni gialle sono già studiati; mai rimuovere né spostare le evidenziazioni; il testo nuovo si aggiunge SENZA evidenziazione. Stato ricontrollato il 13 ott 2026 (verifica diretta delle evidenziazioni nei Word, capitolo per capitolo):
- **Algebra lineare**: 0/13 studiati. Nessun segno → cap. 1-13 ancora da studiare (10-13 sui polinomi).
- **Matematica discreta**: 7/19 studiati (cap. 1-7, compreso il cap. 5 «Induzione», evidenziato il 13 ott con +16 paragrafi). Da studiare: 8-19 (relazioni, equivalenze, funzioni, composizione, iniettività/suriettività).
- **Fondamenti Info**: 11/15 studiati (cap. 1-11). Da studiare: 12-15 (logica proposizionale, appena scritti).
- **Programmazione**: 8/12 studiati (cap. 1-8). Da studiare: 9-12 (referenziamento, scanf, puntatori, dereferenziamento).
- **Programmazione, Laboratorio**: nessun segno → cap. 1-5 ancora da studiare.

## Novita' Moodle
- 8 ott 2026: prima esecuzione controllo automatico. Scaricati `RiassuntoLezione1.pdf` e `ProspettoCorsoB.pdf` (Mate discreta), `20260928-Presentazione-Testo-Fondamenti-Pearson.pdf` (Fondamenti). ⚠ Il link Moodle "Lezione 3: Numeri Complessi, II" (Algebra) punta a una registrazione Webex del 2025, non del 2026: verificare con il docente.
- 13 ott 2026: scaricati `RiassuntoLezione2.pdf` (Mate, scansione da trascrivere), `Lab02 - Operatori e Tipi.pdf` e `slide_tabella_tipi_e_specificatori_conversione.pdf` (Programmazione). Webex Fondamenti L07 (12 ott) x2 da non scaricare; `codice_di_partenza.zip` da scaricare a mano.
- 13 ott 2026 (sera): scaricate slide Programmazione `03A_scambio variabili.pdf` e `03B_floats.pdf`. Registrazione lezione ProgI-13ott (MP4, 65 MB) non scaricata. Da riassumere con /riassunto.
