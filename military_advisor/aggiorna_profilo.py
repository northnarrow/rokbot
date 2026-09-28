"""Ricostruisce account_profile.json dai comandanti letti sul client PC.

I dati vengono dai fogli in test_pc/comandanti_*.png, letti a vista. Ogni
comandante viene agganciato alla base per nome: se un nome non esiste, lo
script lo dice invece di scrivere un profilo con un comandante inventato.
"""

import json
from pathlib import Path

# (nome nella base, epiteto italiano, livello, stelle, abilita', capacita', potere)
LETTI = [
    ("Scipio Africanus Prime", "Eroe di Zama",                     60, 6, [5, 5, 5, 5], 200000, 134400),
    ("Sun Tzu Prime",          "Artista della guerra",             60, 6, [5, 5, 1, 1], 200000,  87200),
    ("Guan Yu",                "Il Signore della Barba Magnifica", 60, 6, [5, 5, 3, 1], 200000,  94000),
    ("Sun Tzu",                "Genio tattico",                    60, 6, [5, 5, 5, 5], 200000,  90400),
    ("Alexander the Great",    "Conquistatore del Mondo",          53, 6, [5, 4, 1, 1], 196500,  81900),
    ("Minamoto no Yoshitsune", "Signore della guerra di Kamakura", 50, 5, [5, 5, 5, 5], 195000, 103450),
    ("Aethelflaed",            "Signora della Mercia",             50, 5, [5, 5, 5, 5], 200850,  97900),
    ("Liu Che",                "Imperatore Wu di Han",             45, 5, [1, 1, 1, 1], 184000,  40100),
    ("Alexander Nevsky",       "L'eroe del fiume Neva",            44, 5, [5, 1, 1, 1], 182000,  65400),
    ("Huo Qubing",             "Marchese di Guanjun",              44, 5, [4, 1, 1, 1], 182000,  51300),
    ("Scipio Africanus",       "Lame di Guerra",                   43, 5, [5, 5, 5, 5], 199100,  61200),
    ("Belisarius",             "L'ultimo dei Romani",              42, 5, [5, 5, 5, 5], 180000,  60400),
    ("Boudica",                "Rosa celtica",                     41, 5, [5, 5, 5, 5], 179000,  64900),
    ("Cao Cao",                "Conquistatore del caos",           40, 4, [5, 1, 2, 1], 178000,  49400),
    ("Cleopatra VII",          "Regina d'Egitto",                  39, 4, [5, 5, 1, 1], 177000,  46400),
    ("Richard I",              "Il cuor di leone",                 37, 4, [1, 1, 1, 1], 175000,  31100),
    ("Yi Seong-Gye",           "Arco della rivoluzione",           33, 4, [1, 1, 1, 1], 171000,  28700),
    ("Charles Martel",         "Il Martello Immortale",            30, 4, [4, 3, 2, 1], 168000,  43400),
    ("Boudica Prime",          "Regina degli Iceni",               30, 4, [1, 1, 1, 1], 168000,  28600),
    ("Belisarius Prime",       "Rinnovatore Imperii",              26, 3, [1, 1, 1, 1], 164000,  23200),
    ("Hannibal Barca",         "Guardiano di Cartagine",           20, 3, [1, 1, 1, 1], 159000,  18100),
    ("Bjorn Ironside",         "Re di Kattegat",                   10, 4, [5, 5, 5, 5], 154000,  39800),
    ("Mehmed II",              "Conquistatore di Istanbul",         9, 1, [5, 0, 0, 0], 153500,  21500),
    ("Julius Caesar",          "Imperatore senza corona",           7, 1, [5, 0, 0, 0], 152500,  20700),
    ("Ragnar Lodbrok",         "Forza di Odino",                    7, 1, [3, 0, 0, 0], 152500,  15700),
    ("William Wallace",        "Guardiano di Scozia",               7, 1, [1, 0, 0, 0], 152500,   7700),
]


def main() -> int:
    kb = {c["name"]: c for c in json.loads(
        Path("military_advisor/data/commanders.json").read_text(encoding="utf-8"))["commanders"]}

    mancanti = [n for n, *_ in LETTI if n not in kb]
    if mancanti:
        print("NON trovati nella base:", mancanti)
        return 1

    comandanti = []
    for nome, epiteto, lv, st, sk, cap, pot in LETTI:
        c = kb[nome]
        comandanti.append({
            "name": nome, "epithet_it": epiteto,
            "rarity": c.get("rarity"), "is_prime": c.get("is_prime"),
            "level": lv, "stars": st, "skills": sk,
            "unit_capacity": cap, "commander_power": pot,
        })

    p = Path("account_profile.json")
    profilo = json.loads(p.read_text(encoding="utf-8"))
    profilo["read_at"] = "2026-09-28T20:10:00"
    profilo["_fonte"] = ("Comandanti letti dal client PC (1796x1040) il 28/09/2026 con "
                         "pc_cattura_comandanti; il resto dal telefono via ADB nella stessa "
                         "giornata. Fogli in test_pc/comandanti_*.png.")
    profilo["commanders"] = comandanti
    note = [n for n in profilo.get("reader_notes", [])
            if not n.startswith("Comandanti:") and not n.startswith("expertise")]
    note.insert(0, f"Comandanti: catturati tutti i 78 posseduti; qui sono riportati i {len(comandanti)} "
                   "sviluppati, cioe' quelli che entrano nelle classifiche. La coda a livello 1-10 "
                   "con abilita' 1/1/1/1 non cambia nessuna raccomandazione.")
    note.insert(1, "La deduplica delle schede e' tarata sul numero dichiarato dal gioco (78) ma non e' "
                   "esatta: nei fogli Aleksandr Nevskij compare due volte, quindi almeno un comandante "
                   "della coda manca. Non incide sui comandanti sviluppati, letti e verificati a vista.")
    note.append("expertise non letta: il quinto riquadro abilita' non e' distinguibile con sicurezza.")
    profilo["reader_notes"] = note

    p.write_text(json.dumps(profilo, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"scritti {len(comandanti)} comandanti in account_profile.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
