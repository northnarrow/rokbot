"""Scrive nella base i dati trovati con la ricerca online del 28/09/2026.

Da lanciare dalla radice del repository:
    python -m military_advisor.aggiorna_da_ricerca

Idempotente: non sovrascrive un valore gia' presente, e registra fonte e data
accanto al dato come fanno le voci gia' esistenti.
"""

import json
from pathlib import Path

FONTE = "allclash, letto 2026-09-28"

TROVATI = {
    "Cleopatra VII": {
        "recommended_formation": f"Line ({FONTE})",
        "nota": "allclash indica il 'sweetspot' di abilita' 1551 per renderla utile. "
                "L'ordine esatto di sblocco delle abilita' e gli armamenti sono "
                f"dietro il paywall PRO ({FONTE}).",
    },
    "Richard I": {
        "recommended_formation": f"Arch ({FONTE})",
        "nota": f"Formazione visibile; armamenti dietro il paywall PRO ({FONTE}).",
    },
    "Charles Martel": {
        "recommended_formation": f"Pincer ({FONTE})",
        "nota": f"Formazione visibile; armamenti dietro il paywall PRO ({FONTE}).",
    },
    "Mulan": {
        "recommended_formation": f"Wedge ({FONTE})",
        "nota": f"Formazione visibile; armamenti dietro il paywall PRO ({FONTE}).",
    },
    "Tomoe Gozen": {
        "nota": "La guida allclash non ha la sezione formazione (verificato 2026-09-28).",
    },
    "Mehmed II": {
        "nota": "Formazione e armamenti entrambi dietro il paywall PRO di allclash "
                "(verificato 2026-09-28): la sezione 'Best Formation + Armaments' "
                "non mostra nulla ai non abbonati. Da prendere dal gioco.",
    },
}


# Alberi dei talenti ricavati leggendo l'immagine della build, non il testo:
# su riseofkingdomsguides la build e' pubblicata solo come screenshot. Dall'
# immagine si leggono con certezza gli alberi usati e i punti per nodo; NON i
# nomi dei singoli talenti, che sono solo icone senza legenda. Si registra
# quindi solo cio' che l'immagine sostiene davvero.
TALENTI = {
    "Narses": [{
        "purpose": "unico build pubblicato",
        "trees": ["Engineering", "Defense"],
        "key_talents": [],
        "stat_summary": None,
        "notes": "Letto dall'immagine della build (riseofkingdomsguides, "
                 "Narses-Talent-Tree-Build.jpg, letta 2026-09-28): la pagina non ha "
                 "testo, solo lo screenshot. Punti concentrati su Engineering (nodi "
                 "quasi tutti pieni, 5/5 in cima) e su Defense; l'albero Versatility "
                 "resta vuoto. I nomi dei singoli talenti non sono ricavabili "
                 "dall'immagine: servirebbe una legenda delle icone.",
    }],
}


def main() -> int:
    p = Path("military_advisor/data/commanders.json")
    d = json.loads(p.read_text(encoding="utf-8"))
    per_nome = {c["name"]: c for c in d["commanders"]}

    scritti, saltati, assenti = [], [], []
    for nome, campi in TROVATI.items():
        c = per_nome.get(nome)
        if c is None:
            assenti.append(nome)
            continue
        f = campi.get("recommended_formation")
        if f:
            if c.get("recommended_formation"):
                saltati.append(f"{nome}: formazione gia' presente ({c['recommended_formation']})")
            else:
                c["recommended_formation"] = f
                scritti.append(f"{nome}: formazione = {f}")
        nota = campi.get("nota")
        if nota:
            note = c.get("notes")
            if isinstance(note, list):
                if nota not in note:
                    note.append(nota)
                    scritti.append(f"{nome}: nota aggiunta")
            elif isinstance(note, str):
                if nota not in note:
                    c["notes"] = note.rstrip() + " " + nota
                    scritti.append(f"{nome}: nota aggiunta")
            else:
                c["notes"] = [nota]
                scritti.append(f"{nome}: nota creata")

    for nome, build in TALENTI.items():
        c = per_nome.get(nome)
        if c is None:
            assenti.append(nome)
        elif c.get("talent_builds"):
            saltati.append(f"{nome}: talenti gia' presenti")
        else:
            c["talent_builds"] = build
            scritti.append(f"{nome}: talenti = {', '.join(build[0]['trees'])}")

    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    for r in scritti:
        print("  scritto ", r)
    for r in saltati:
        print("  saltato ", r)
    for r in assenti:
        print("  ASSENTE ", r)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
