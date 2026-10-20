---
description: Ricostruisce il Quaderno (riassunti, pagina, controlli) e ripubblica la pagina su claude.ai
---

Aggiorna e ripubblica il Quaderno di ripasso.

1. `python _sistema/scripts/aggiorna_tutto.py` (Anki, riassunti web, pagina, controllo Word, collaudo). Se qualcosa dà ERRORE, fermati e dillo.
2. Se Emanuele ha sottolineature in attesa (`_sistema/sottolineature.json` non vuoto o voci nel database), proponi prima `/sottolineature`.
3. Commit e push di quello che è cambiato (regola 10 di CLAUDE.md). Non committare `_sistema/progressi.json` se non l'ha cambiato Emanuele.
4. Ripubblica l'artefatto con lo strumento Artifact, stesso link https://claude.ai/artifact/NJSpDPQSeDAmcpXqw9ahNA:
   `file_path` = `_sistema/pagina_studio/index.html`, `root` = `_sistema/pagina_studio`, `files` = `data.json`, `img/*` e tutto `riassunti/**`
   (HTML e `media/*`). Il database `db` resta dichiarato (non passare `capabilities`). Pubblica i file nuovi o cambiati; al massimo 255 per chiamata.
5. Dì in una riga cosa hai ripubblicato.
