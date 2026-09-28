# rokbot

Bot personale per Rise of Kingdoms, con un **consigliere militare** che conosce comandanti, armamenti, equipaggiamento, truppe e strategie. Ogni dato ha la sua fonte e la data di lettura.

- **Oggi:** client ufficiale su PC Windows.
- **Poi:** porting su Android, cambiando risoluzione e modo di catturare lo schermo e toccare.

## Regole fisse del bot

- **Mai gemme**, per nessun motivo.
- **Mai scudi**: in caso di pericolo avvisa soltanto.
- **Conferma obbligatoria** prima di attaccare giocatori o consumare materiali rari: sculture, Sage's Testimony, pietre di trasmutazione e simili.
- Se compare una **verifica anti-bot**, il bot si ferma e avvisa. Non prova mai a risolverla.

## Contenuto

| Cartella | Cosa c'è |
|---|---|
| `military_advisor/` | consigliere, knowledge base, regole per il bot, strumenti di controllo per PC e telefono |
| `military_advisor/docs/` | guide in italiano: difesa, attacco, routine, talenti, eventi, meccaniche, KvK e alleanza, automazione |
| `military_advisor/data/` | dati con fonti: 142 comandanti (con come ottenere le sculture), armamenti, equipaggiamento, truppe, strategie |
| `extra/` | lista informativa di bug, exploit e truffe noti, **non usata dal bot** |

Dettagli e comandi: [`military_advisor/README.md`](military_advisor/README.md). Primi test: [`military_advisor/GUIDA_TEST.md`](military_advisor/GUIDA_TEST.md).

## Avvio rapido (PC Windows)

```
pip install mss pygetwindow pytest
python -m military_advisor pc-check
python -m military_advisor heads      # come ottenere le sculture di ogni comandante
python -m pytest -q military_advisor/tests
```

## Avvertenza

I termini di servizio di Lilith (15/04/2025, clausole 17.1.15 e 17.1.18) vietano bot e automazione. L'uso può portare alla sospensione dell'account. Fonti in `military_advisor/docs/automazione.md`.
