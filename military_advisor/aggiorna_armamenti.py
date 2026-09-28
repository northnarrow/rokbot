"""Riempie recommended_armaments nella base, partendo dalla formazione.

Gli armamenti non si scelgono per comandante: ogni formazione ha 4 slot, uno
per tipo (Pergamena, Strumento, Bandiera, Emblema), e ogni slot accetta un
solo pezzo. Quindi sapere la formazione del comandante basta a sapere quali 4
armamenti gli servono, e il campo si riempie unendo i dati invece di cercarlo
142 volte.

Tabella letta dalla schermata Codice del client il 28/09/2026. Le voci
marcate "verificata" sono confermate anche dall'inventario, dove il gioco
scrive la formazione sotto il nome dell'armamento.

    python -m military_advisor.aggiorna_armamenti
"""

import json
import re
from pathlib import Path

FONTE = "schermata Codice del client, letta 2026-09-28"

# formazione -> (pergamena, strumento, bandiera, emblema), verificata?
TABELLA = {
    "Arch":        (("Pergamena del nord", "Corno del nord",
                     "Stendardo di battaglia del Nord", "Emblema del Nord"), True),
    "Wedge":       (("Epopee di Olimpia", "Direttore del coro di Olimpia",
                     "Stendardo del Pantheon", "Onori del Pantheon"), True),
    "Wedge II":    (("Messaggio dell'araldo", "Strumento dell'araldo",
                     "Insegna dell'araldo", "Marchio dell'araldo"), False),
    "V-Formation": (("Cronache del drago", "Tamburo di guerra imperiale",
                     "Stendardo del drago", "Decreto imperiale"), False),
    "Staggered":   (("Un record di vendetta", "Ode al guerriero",
                     "Gloria di battaglia", "Sigillo di guerra"), False),
    "Hollow Square": (("Tomo di Fleur de Lys", "Luto di Fleur de Lys",
                       "Stendardo Fleur de Lys", "Scudo Fleur de Lys"), False),
    "Line":        (("Libro di Horus", "Arpa di Horus",
                     "Taglia di Horus", "Occhio di Horus"), False),
}

TIPI = ("Pergamena", "Strumento", "Bandiera", "Emblema")

# Come riconoscere la formazione dentro il testo del campo, che spesso porta
# anche la fonte: "Wedge (allclash)", "allclash: Arch (le formazioni...)".
ALIAS = {
    "Wedge II": ("wedge ii", "cuneo ii"),
    "Wedge": ("wedge", "cuneo"),
    "Arch": ("arch", "arco"),
    "Line": ("line", "linea"),
    "Hollow Square": ("hollow square", "quadrat"),
    "V-Formation": ("v formation", "v-formation", "formazione a v"),
    "Staggered": ("staggered", "sfalsat"),
}


def riconosci(testo: str):
    t = testo.lower()
    if "triple line" in t or "linea tripla" in t:
        return None                      # tabella incompleta per questa
    for nome, chiavi in ALIAS.items():   # Wedge II prima di Wedge
        if any(k in t for k in chiavi):
            return nome
    return None


def main() -> int:
    p = Path("military_advisor/data/commanders.json")
    d = json.loads(p.read_text(encoding="utf-8"))

    scritti = saltati = senza = 0
    for c in d["commanders"]:
        if c.get("recommended_armaments"):
            saltati += 1
            continue
        f = c.get("recommended_formation")
        if not isinstance(f, str):
            senza += 1
            continue
        nome = riconosci(f)
        if nome is None or nome not in TABELLA:
            senza += 1
            continue
        pezzi, verificata = TABELLA[nome]
        c["recommended_armaments"] = {
            "formation": nome,
            "slots": [{"type": t, "name": n} for t, n in zip(TIPI, pezzi)],
            "source": FONTE,
            "verified_in_inventory": verificata,
            "note": "Gli slot sono fissi: ogni formazione ha una Pergamena, uno Strumento, "
                    "una Bandiera e un Emblema, e ogni slot accetta solo quel pezzo. La "
                    "scelta sta nella copia: attributi casuali e iscrizioni.",
        }
        scritti += 1

    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    tot = len(d["commanders"])
    pieni = sum(1 for c in d["commanders"] if c.get("recommended_armaments"))
    print(f"scritti {scritti}, gia' presenti {saltati}, senza formazione nota {senza}")
    print(f"armamenti consigliati: {pieni}/{tot}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
