# Consigliere militare (military_advisor) — Rise of Kingdoms

Modulo Python autonomo da agganciare al bot. Non fa rete e non tocca il
telefono: legge una **knowledge base** (KB) costruita dalla ricerca online
(ogni dato con fonte e data) e un **profilo account** prodotto dal bot, e
restituisce raccomandazioni per raccolta, barbari, difesa e attacco più un
piano di addestramento eseguibile. Vincoli codificati: **mai gemme**,
**conferma prima di attaccare giocatori o consumare materiali rari**.

## Stato dei 5 punti richiesti

| # | Richiesta | Stato | Dove |
|---|---|---|---|
| 1 | Ricerca online su comandanti e armamenti, fonti e date | **fatto** (ricerca automatica su tutti i comandanti + verifica su seconda fonte) | `data/commanders.json`, `data/armamenti.json`, `data/equipaggiamento.json`, `data/truppe_pve.json`, `data/sources.json`, `data/kb_index.json` |
| 2 | Leggere dal mio account comandanti, livelli, skill, formazioni, equipaggiamento, armamenti | **bloccato in questa sessione**: il telefono è collegato al PC, la sessione cloud non lo vede | contratto pronto in `account_reader.py`, formato in `account_profile.example.json` |
| 3 | Esplorare l'officina/armamenti sul telefono e spiegarla prima di automatizzare | **spiegazione fatta dalle guide**, esplorazione sul telefono da fare dal PC | `OFFICINA_ARMAMENTI.md` |
| 4 | Consigli comandanti/formazione/truppe per raccolta, barbari, difesa, attacco | **motore fatto**; il report reale esce appena c'è il profilo del tuo account | `advisor.py`, `python -m military_advisor report` |
| 5 | Addestrare in automatico le truppe che servono | **piano fatto** (ordini di addestramento senza gemme); l'esecuzione sul telefono va agganciata al bot | `training_plan` nel risultato di `recommend()` |

## Uso

```bash
cd <cartella che contiene military_advisor/>
python -m military_advisor phone-check                      # PRIMO TEST: telefono via ADB, sola lettura, salva uno screenshot
python -m military_advisor build-kb                         # unisce data/fragments -> KB
python -m military_advisor kb-stats                         # comandanti, fonti, regole caricate
python -m military_advisor commander "Cao Cao"              # scheda con skill, build, coppie, fonti
python -m military_advisor rules                            # tutte le regole if/then per il bot (con flag di conferma)
python -m military_advisor daily                            # routine giornaliera ordinata
python -m military_advisor validate --profile account_profile.json
python -m military_advisor report --profile account_profile.json --json raccomandazioni.json
```

Il controllo telefono non tocca lo schermo. Verifica nell'ordine:
- adb installato;
- telefono collegato e autorizzato;
- modello, versione Android, risoluzione e densità;
- schermo acceso;
- Rise of Kingdoms installato e in primo piano;
- screenshot salvato in `test_telefono/`.

Se un passo fallisce, il messaggio dice cosa sistemare.

## Libro delle strategie

Oltre ai comandanti, la KB contiene guide operative ricercate online. Ogni guida ha il suo file in `data/` e una versione leggibile in `docs/`:

| Argomento | Dati | Guida |
|---|---|---|
| Difesa città e guarnigione | `strategia_difesa.json` | `docs/difesa.md` |
| Attacco, meta 2026, rally, canyon | `strategia_attacco.json` | `docs/attacco.md` |
| Routine giornaliera, crescita, eventi | `strategia_routine.json` | `docs/routine.md` |
| Alberi dei talenti | `talenti.json` | `docs/talenti.md` |
| Eventi PvE | `eventi_pve.json` | `docs/eventi_pve.md` |
| Meccaniche di combattimento | `meccaniche.json` | `docs/meccaniche.md` |
| KvK e alleanza | `kvk_alleanza.json` | `docs/kvk_alleanza.md` |
| Schermate, ADB, rischi, piano di test | `automazione.json` | `docs/automazione.md` |

Tutte le `bot_rules` hanno la forma `quando / allora / perché / requires_confirmation / fonti`. Il consigliere le raccoglie in `result["bot_rules"]`. Il bot deve fermarsi e chiedere quando `requires_confirmation` è vero.

Da codice, nel bot:

```python
from military_advisor import MilitaryAdvisor
adv = MilitaryAdvisor()
result = adv.recommend(profile)          # profile = dict letto dal telefono
print(adv.render_report(result))        # testo in italiano
for order in result["training_plan"]["orders"]:
    bot.train(order["troop_type"], order["tier"], order["count"])   # mai gemme

# prima di QUALSIASI azione:
g = adv.gate({"kind": "attack", "target": "player"})
if g["requires_confirmation"]:
    chiedi_conferma_all_utente(g["reason"])
```

## Come ragiona il motore (advisor.py)

Per ogni ruolo assegna a ogni comandante posseduto un punteggio =
rating delle tier list per quel ruolo + specialità (Gathering, Peacekeeping,
Garrison, Conquering…) + bonus numerici estratti dalle skill (es. "+50% danno
ai barbari", "+25% carico") + sviluppo reale (livello, skill, expertise,
stelle) + tier di truppe disponibili del tipo giusto + coerenza
dell'equipaggiamento. Poi cerca una **coppia documentata** nelle fonti tra i
comandanti che possiedi; se non c'è, sceglie per tipo di truppa e lo dice
(`documented: false`). Formazione: Line per raccolta; Delta per Combo, Pincer
per Smite, Arch per danno normale, Wedge altrimenti; Hollow Square/Tercio in
difesa. Truppe: T1 assedio per la raccolta, altrimenti il **tier più alto
sbloccato** del tipo del primario (meno perdite a parità di danno).

Il piano di addestramento calcola, per ogni ruolo, una marcia piena del
tipo/tier consigliato (per la raccolta: marce − 1 di T1 assedio), confronta
con le truppe che hai e produce ordini `train` con `no_gems: true`,
suggerendo l'upgrade dal tier inferiore quando c'è un evento che lo premia.

## Struttura

```
military_advisor/
  __init__.py, __main__.py        # API e CLI
  advisor.py                      # motore + gate di sicurezza
  kb.py                           # caricamento KB, normalizzazione nomi, rating
  merge_kb.py                     # unisce data/fragments/*.verified.json -> data/*.json
  account_reader.py               # contratto per la lettura dal telefono (da implementare nel bot)
  account_profile.example.json    # formato del profilo (valori d'esempio, NON il tuo account)
  OFFICINA_ARMAMENTI.md           # spiegazione del sistema formazioni/armamenti/iscrizioni
  data/sources.json               # tutte le fonti con url, data pagina, data lettura
  data/fragments/                 # output grezzo della ricerca (per gruppo) + versioni verificate + _gaps.json
  data/commanders.json            # KB comandanti unita
  data/armamenti.json, equipaggiamento.json, truppe_pve.json
  tests/test_advisor.py           # test del motore con mini-KB
```

Ogni record della KB ha `sources: [{url, site, page_date, retrieved, fields}]`,
`conflicts` (fonti in disaccordo, con entrambi i valori) e `verification`
(`checked_with`, `status`). Le fonti irraggiungibili dalla sessione sono in
`data/sources.json → unreachable_from_this_session`.

## Cosa manca e come chiuderlo (dal PC, con il telefono collegato)

1. Copiare la cartella `military_advisor/` dentro il progetto del bot.
2. Implementare `AccountReader` (ADB + OCR, già presenti nel bot) seguendo
   il docstring in `account_reader.py`; salvare `account_profile.json`.
3. Fare il giro manuale della schermata Formazione/Armamenti e confrontarlo
   con `OFFICINA_ARMAMENTI.md`; correggere `data/armamenti.json → ui_flow`.
4. Lanciare `python -m military_advisor report --profile account_profile.json`
   e leggere le raccomandazioni.
5. Collegare `training_plan.orders` alla routine di addestramento del bot,
   passando sempre da `adv.gate()`.

Nota sulla sessione precedente sul PC: l'avvio del bot con pannello web era
fallito con `exit code 127` (comando non trovato nel PATH, tipicamente
`python`/`node` non risolto dallo script di avvio). Va ricontrollato lì.
