# Mappa degli edifici della citta' (Rise of Kingdoms, aggiornata al 2026-09-28)

Documento per il bot: per ogni edificio funzione, pulsanti/schede, sblocco, livello massimo e pericoli. Dati in `data/fragments/mappa_edifici.json`. Legenda pericolo: **sicuro** = il bot puo' agire; **CONFERMA** = solo con conferma dell'utente; **MAI** = gemme, scudi, acquisti.

Avvertenza principale: nessuna fonte accessibile riporta testualmente le etichette del menu contestuale degli edifici; i nomi dei pulsanti qui sotto sono descrittivi (in inglese, dalle guide) e vanno confermati con screenshot del client italiano. L'unico nome italiano certo e' **Mercato = Trading Post** (fonte: proprietario, `riferimenti_ui/README.md`; conferma indiretta da rok.guide 2020: 'Lucerne Scrolls is located in the Trading Post building'). Il client del proprietario mostra 'Eta' del ferro', cioe' City Hall 10-15 secondo la [tabella wiki](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04).

Fonti principali: wiki fandom via API (date = ultima revisione), patch note del forum ufficiale Lilith 1.0.87-1.1.09 (dic 2024 - giu 2026), riseofkingdomsguides.com (dateModified 2026-01-02), heaven-guardian.com (2026-09-02). Le schermate gia' descritte in `automazione.json` e le regole R1-R12 di `strategia_routine.json` non sono ripetute ma citate.

## Riepilogo sblocchi

| Edificio | Nome IT | Sblocco | Liv. max |
|---|---|---|---|
| City Hall | — | Presente dall'inizio (livello 1). | 25 |
| Wall | — | Presente dall'inizio (CH1). | 25 |
| Watchtower | — | Presente dall'inizio (CH1). | 25 |
| Academy | — | City Hall 4 (tabella sblocchi CH); pagina edificio indica 1stUnlockCH=6 -> vedi conflicts. | 25 |
| Barracks | — | Presente dall'inizio (CH1). | 25 |
| Archery Range | — | City Hall 2. | 25 |
| Stable | — | City Hall 4 (tabella sblocchi CH); pagina edificio 1stUnlockCH=3 -> vedi conflicts. | 25 |
| Siege Workshop | — | City Hall 5 (tabella sblocchi CH); pagina edificio 1stUnlockCH=4 -> vedi conflicts. | 25 |
| Hospital | — | 1° CH1, 2° CH4, 3° CH9, 4° CH15. | 25 |
| Storehouse | — | Presente dall'inizio (CH1). | 25 |
| Trading Post | Mercato | City Hall 10 (tabella sblocchi CH e riseofkingdomsguides); la pagina edificio indica 1stUnlockCH=12 -> vedi conflicts. | 25 |
| Tavern | — | Presente dall'inizio (CH1). | 25 |
| Courier Station | — | City Hall 6. | 25 |
| Scout Camp | — | City Hall 2. | 25 |
| Alliance Center | — | City Hall 3 (tabella sblocchi CH e riseofkingdomsguides); pagina edificio 1stUnlockCH=5 -> vedi conflicts. | 25 |
| Blacksmith | — | City Hall 16 (e ricezione del primo equipaggiamento). | 1 (la wiki elenca solo il livello 1; nessun upgrade documentato) |
| Castle | — | City Hall 7. | 25 |
| Farm | — | 1a CH1, 2a CH3, 3a CH6, 4a CH9 (tabella CH; la 1a e' presente dal CH1 secondo la tabella requisiti Farm) | 25 |
| Lumber Mill | — | 1a CH2, 2a CH5, 3a CH8, 4a CH11 | 25 |
| Quarry | — | 1a CH6, 2a CH7, 3a CH10, 4a CH13 (pagina edificio); la tabella CH elenca 2a CH7, 3a CH10, 4a CH13 | 25 |
| Goldmine | — | 1a CH10, 2a CH12, 3a CH14, 4a CH16 | 25 |
| Builder's Hut | — | City Hall 5? (wiki con punto interrogativo). | 1 |
| Monument | — | City Hall 8 (tabella CH e tabella requisiti Monument); la pagina edificio indica 1stUnlockCH=9 -> vedi conflicts. | 1 |
| Bulletin Board | — | City Hall 1? (wiki con punto interrogativo). | n.d. |
| Shop | — | City Hall 5. | n.d. |
| Lyceum of Wisdom | — | City Hall 10. | 1 |
| State Forum | — | n.d. | n.d. |
| Hall of Heroes | — | n.d. | n.d. |
| Crystal Research Center | — | n.d. | n.d. |
| Decorazioni (Decorative: strade, alberi, lanterne ecc.) e cosmetici citta' | — | n.d. | n.d. |
| Commander Statue / Commander Hall | — | n.d. | n.d. |
| Market (edificio separato) | Mercato | n.d. | n.d. |

## City Hall

**Funzione.** Edificio centrale: il suo livello e' il livello del giocatore e il tetto di livello di tutti gli altri edifici; aumenta capacita' truppe, code di marcia, sblocca edifici e tier truppe. Dopo ogni upgrade arriva una mail con risorse/oggetti da riscuotere.

**Sblocco:** Presente dall'inizio (livello 1). — **Livello massimo:** 25

**Pulsanti / azioni**

- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall) (2023-07-16); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04)
- **Pulsante grafico (chart) -> Economics Buff** [sicuro] — Mostra i bonus economici della citta' (es. Building Speed). Citato in una nota degli editor wiki: 'click City Hall > then the chart button'. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04)
- **Quick Replenish** [MAI] — Rifornisce rapidamente le risorse mancanti per ricerca/costruzione/addestramento (aggiunto in 1.0.87). Non documentato se usa oggetti risorsa o gemme. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1817043) (2024-12-17)
- **Completamento istantaneo / velocizzazione con gemme (icona gemma)** [MAI] — Le gemme possono velocizzare costruzione, ricerca e addestramento; qualunque pulsante con icona gemma spende gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Resources) (2025-05-31); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Schede interne**

- **Economics Buff (via chart button)** — Elenco bonus economici (velocita' costruzione ecc.) Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04)
- **Queue management (dashboard code)** — Da CH8: panoramica di costruzione, addestramento, ricerca, cure, scouting, donazioni d'alleanza con azioni rapide; disattivabile in Settings. Posizione (HUD o City Hall) non indicata. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2161435) (2025-11-14)
- **Switch Civilization (buff)** — Da CH16 si puo' cambiare il buff di civilta' nella pagina 'switch civilization' (1.1.01). Posizione non indicata. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2161435) (2025-11-14)

**Per il bot**

- Leggere il livello (serve a sapere cosa e' sbloccato: vedi tabella sblocchi in docs).
- Leggere i requisiti del prossimo livello (quasi sempre Wall al livello precedente + un secondo edificio).
- Upgrade solo su ordine confermato; mai finire con gemme.
- Riscuotere la mail di ricompensa dopo l'upgrade (azione sicura).

**Lacune:** Etichette esatte del menu contestuale (Upgrade/Details/altro) non documentate: da mappare con screenshot del client italiano. Nome italiano non trovato (Google Play e App Store IT non elencano gli edifici).

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall) (2023-07-16); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Rewards) (2023-03-24); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1868790) (2024-12-17); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2161435) (2025-11-14); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)

## Wall

**Funzione.** Principale edificio difensivo; ogni livello e' requisito per il City Hall successivo. Dopo un attacco riuscito la citta' brucia e la durabilita' cala: va riparata manualmente; a durabilita' 0 la citta' viene teletrasportata in un punto casuale. Toccandolo si assegnano i comandanti che difendono la citta'.

**Sblocco:** Presente dall'inizio (CH1). — **Livello massimo:** 25

**Pulsanti / azioni**

- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Wall) (2023-12-02)
- **Assegna comandanti difensori (garrison)** [CONFERMA] — 'When you click on your wall ... you can put commanders that will defend the city' (riseofkingdomsguides). Fonti: [riseofkingdomsguides.com](https://riseofkingdomsguides.com/wall/) (2026-01-02)
- **Repair (riparazione durabilita')** [sicuro] — Ripara la durabilita' del Wall: 500 ogni 30 minuti (wiki War). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/War) (2020-09-06)
- **Spegnere l'incendio con gemme** [MAI] — 'Burning structures can be stopped using gems once every 15 minutes'. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/War) (2020-09-06)
- **Completamento istantaneo / velocizzazione con gemme (icona gemma)** [MAI] — Le gemme possono velocizzare costruzione, ricerca e addestramento; qualunque pulsante con icona gemma spende gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Resources) (2025-05-31); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Per il bot**

- Se la citta' brucia: segnalare subito all'utente; usare solo il Repair gratuito se abilitato.
- Mai spegnere l'incendio con gemme.
- Cambiare i comandanti in difesa solo su ordine confermato.

**Lacune:** Nome esatto del pulsante di riparazione e dell'eventuale scheda 'Defenders' non verificato. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Wall) (2023-12-02); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Wall/Requirements) (2023-12-02); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/wall/) (2026-01-02); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/War) (2020-09-06)

## Watchtower

**Funzione.** Secondo edificio difensivo: aumenta danni agli attaccanti e assorbe parte dei danni alla guarnigione. Gli upgrade richiedono Arrow of Resistance.

**Sblocco:** Presente dall'inizio (CH1). — **Livello massimo:** 25

**Pulsanti / azioni**

- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Watchtower) (2020-04-30); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Watchtower/Requirements) (2024-09-07)
- **Completamento istantaneo / velocizzazione con gemme (icona gemma)** [MAI] — Le gemme possono velocizzare costruzione, ricerca e addestramento; qualunque pulsante con icona gemma spende gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Resources) (2025-05-31); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Per il bot**

- Upgrade SOLO con conferma: consuma Arrow of Resistance (materiale raro, fino a decine per livello).

**Lacune:** Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Watchtower) (2020-04-30); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Watchtower/Requirements) (2024-09-07); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/watchtower/) (2026-01-02); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)

## Academy

**Funzione.** Ricerca tecnologie (Economic e Military Technology); upgrade aumenta la velocita' di ricerca e sblocca nuove tecnologie.

**Sblocco:** City Hall 4 (tabella sblocchi CH); pagina edificio indica 1stUnlockCH=6 -> vedi conflicts. — **Livello massimo:** 25

**Pulsanti / azioni**

- **Research** [CONFERMA] — Apre gli alberi tecnologici e avvia una ricerca (costa risorse, occupa la coda ricerca). Etichetta esatta non verificata. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Academy) (2026-01-04)
- **Help (richiesta Alliance Help)** [sicuro] — Dopo l'avvio, la ricerca puo' ricevere aiuti dall'alleanza (riduce il timer). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) (2026-09-26)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Academy) (2026-01-04)
- **Quick Replenish** [MAI] — Rifornisce rapidamente le risorse mancanti per ricerca/costruzione/addestramento (aggiunto in 1.0.87). Non documentato se usa oggetti risorsa o gemme. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1817043) (2024-12-17)
- **Completamento istantaneo / velocizzazione con gemme (icona gemma)** [MAI] — Le gemme possono velocizzare costruzione, ricerca e addestramento; qualunque pulsante con icona gemma spende gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Resources) (2025-05-31); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Schede interne**

- **Economic Technology** — Sviluppo, raccolta, produzione, velocita' di ricerca Fonti: [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)
- **Military Technology** — Truppe, fino alla ricerca Tier 5 Fonti: [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)

**Per il bot**

- Tenere la coda ricerca sempre occupata con la ricerca decisa dall'advisor/utente.
- Premere Help dopo l'avvio.
- Velocizzare solo con speedup (non gemme) e solo se l'utente lo abilita.

**Lacune:** Nome italiano non trovato. Etichette pulsanti non verificate.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Academy) (2026-01-04); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Academy/Unlocks) (2020-12-22); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/academy/) (2026-01-02)

## Barracks

**Funzione.** Addestra e promuove (upgrade di un tier alla volta) le unita' di fanteria (infantry); 5 tier sbloccati con la ricerca. Coda di addestramento propria.

**Sblocco:** Presente dall'inizio (CH1). — **Livello massimo:** 25

**Pulsanti / azioni**

- **Train** [CONFERMA] — Addestra N unita' del tier scelto consumando risorse; occupa la coda dell'edificio. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Barracks) (2020-04-29); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)
- **Upgrade (promozione unita')** [CONFERMA] — Promuove unita' esistenti al tier successivo (costo complessivo maggiore dell'addestramento diretto). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Barracks) (2020-04-29)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Barracks) (2020-04-29)
- **Quick Replenish** [MAI] — Rifornisce rapidamente le risorse mancanti per ricerca/costruzione/addestramento (aggiunto in 1.0.87). Non documentato se usa oggetti risorsa o gemme. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1817043) (2024-12-17)
- **Completamento istantaneo / velocizzazione con gemme (icona gemma)** [MAI] — Le gemme possono velocizzare costruzione, ricerca e addestramento; qualunque pulsante con icona gemma spende gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Resources) (2025-05-31); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Per il bot**

- Addestrare solo quantita'/tier gia' confermati dall'utente.
- L'Alliance Help NON riduce l'addestramento: non cercare il pulsante Help qui.
- Raccogliere le truppe pronte (tocco sull'icona sopra l'edificio: posizione da verificare).

**Lacune:** Etichette esatte Train/Upgrade e slider quantita' non documentate. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Barracks) (2020-04-29); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/barracks/) (2026-01-02); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

## Archery Range

**Funzione.** Addestra e promuove (upgrade di un tier alla volta) le unita' di arcieri (archer); 5 tier sbloccati con la ricerca. Coda di addestramento propria.

**Sblocco:** City Hall 2. — **Livello massimo:** 25

**Pulsanti / azioni**

- **Train** [CONFERMA] — Addestra N unita' del tier scelto consumando risorse; occupa la coda dell'edificio. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Archery_Range) (2020-04-29); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)
- **Upgrade (promozione unita')** [CONFERMA] — Promuove unita' esistenti al tier successivo (costo complessivo maggiore dell'addestramento diretto). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Archery_Range) (2020-04-29)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Archery_Range) (2020-04-29)
- **Quick Replenish** [MAI] — Rifornisce rapidamente le risorse mancanti per ricerca/costruzione/addestramento (aggiunto in 1.0.87). Non documentato se usa oggetti risorsa o gemme. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1817043) (2024-12-17)
- **Completamento istantaneo / velocizzazione con gemme (icona gemma)** [MAI] — Le gemme possono velocizzare costruzione, ricerca e addestramento; qualunque pulsante con icona gemma spende gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Resources) (2025-05-31); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Per il bot**

- Addestrare solo quantita'/tier gia' confermati dall'utente.
- L'Alliance Help NON riduce l'addestramento: non cercare il pulsante Help qui.
- Raccogliere le truppe pronte (tocco sull'icona sopra l'edificio: posizione da verificare).

**Lacune:** Etichette esatte Train/Upgrade e slider quantita' non documentate. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Archery_Range) (2020-04-29); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/archery-range/) (2026-01-02); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

## Stable

**Funzione.** Addestra e promuove (upgrade di un tier alla volta) le unita' di cavalleria (cavalry); 5 tier sbloccati con la ricerca. Coda di addestramento propria.

**Sblocco:** City Hall 4 (tabella sblocchi CH); pagina edificio 1stUnlockCH=3 -> vedi conflicts. — **Livello massimo:** 25

**Pulsanti / azioni**

- **Train** [CONFERMA] — Addestra N unita' del tier scelto consumando risorse; occupa la coda dell'edificio. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Stable) (2026-01-04); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)
- **Upgrade (promozione unita')** [CONFERMA] — Promuove unita' esistenti al tier successivo (costo complessivo maggiore dell'addestramento diretto). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Stable) (2026-01-04)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Stable) (2026-01-04)
- **Quick Replenish** [MAI] — Rifornisce rapidamente le risorse mancanti per ricerca/costruzione/addestramento (aggiunto in 1.0.87). Non documentato se usa oggetti risorsa o gemme. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1817043) (2024-12-17)
- **Completamento istantaneo / velocizzazione con gemme (icona gemma)** [MAI] — Le gemme possono velocizzare costruzione, ricerca e addestramento; qualunque pulsante con icona gemma spende gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Resources) (2025-05-31); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Per il bot**

- Addestrare solo quantita'/tier gia' confermati dall'utente.
- L'Alliance Help NON riduce l'addestramento: non cercare il pulsante Help qui.
- Raccogliere le truppe pronte (tocco sull'icona sopra l'edificio: posizione da verificare).

**Lacune:** Etichette esatte Train/Upgrade e slider quantita' non documentate. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Stable) (2026-01-04); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/stable/) (2026-01-02); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

## Siege Workshop

**Funzione.** Addestra e promuove (upgrade di un tier alla volta) le unita' di assedio (siege); 5 tier sbloccati con la ricerca. Coda di addestramento propria.

**Sblocco:** City Hall 5 (tabella sblocchi CH); pagina edificio 1stUnlockCH=4 -> vedi conflicts. — **Livello massimo:** 25

**Pulsanti / azioni**

- **Train** [CONFERMA] — Addestra N unita' del tier scelto consumando risorse; occupa la coda dell'edificio. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Siege_Workshop) (2026-09-19); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)
- **Upgrade (promozione unita')** [CONFERMA] — Promuove unita' esistenti al tier successivo (costo complessivo maggiore dell'addestramento diretto). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Siege_Workshop) (2026-09-19)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Siege_Workshop) (2026-09-19)
- **Quick Replenish** [MAI] — Rifornisce rapidamente le risorse mancanti per ricerca/costruzione/addestramento (aggiunto in 1.0.87). Non documentato se usa oggetti risorsa o gemme. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1817043) (2024-12-17)
- **Completamento istantaneo / velocizzazione con gemme (icona gemma)** [MAI] — Le gemme possono velocizzare costruzione, ricerca e addestramento; qualunque pulsante con icona gemma spende gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Resources) (2025-05-31); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Per il bot**

- Addestrare solo quantita'/tier gia' confermati dall'utente.
- L'Alliance Help NON riduce l'addestramento: non cercare il pulsante Help qui.
- Raccogliere le truppe pronte (tocco sull'icona sopra l'edificio: posizione da verificare).

**Lacune:** Etichette esatte Train/Upgrade e slider quantita' non documentate. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Siege_Workshop) (2026-09-19); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/siege-workshop/) (2026-01-02); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

## Hospital

**Funzione.** Cura i feriti gravi; fino a 4 ospedali. Se l'ospedale e' pieno i feriti in eccesso muoiono. Nessuna cura durante un rally subito.

**Sblocco:** 1° CH1, 2° CH4, 3° CH9, 4° CH15. — **Livello massimo:** 25

**Pulsanti / azioni**

- **Heal** [CONFERMA] — Cura i feriti selezionati consumando risorse; la cura puo' ricevere Alliance Help. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Hospital) (2020-04-30); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/hospital/) (2026-01-02)
- **Help (Alliance Help)** [sicuro] — Richiede aiuto all'alleanza per ridurre il timer di cura. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) (2026-09-26)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Hospital/Requirements) (2022-09-14)
- **Completamento istantaneo / velocizzazione con gemme (icona gemma)** [MAI] — Le gemme possono velocizzare costruzione, ricerca e addestramento; qualunque pulsante con icona gemma spende gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Resources) (2025-05-31); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Per il bot**

- Controllare la capacita' prima/durante combattimenti e avvisare se vicino al pieno.
- Curare solo su ordine confermato (costo risorse); mai cura istantanea con gemme.

**Lacune:** Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Hospital) (2020-04-30); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/hospital/) (2026-01-02); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

## Storehouse

**Funzione.** Protegge una quota di risorse dal saccheggio; l'upgrade aumenta la protezione.

**Sblocco:** Presente dall'inizio (CH1). — **Livello massimo:** 25

**Pulsanti / azioni**

- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Storehouse) (2018-12-02)
- **Details (capacita' protetta)** [sicuro] — Mostra le quantita' protette per risorsa (dato presente nelle tabelle, etichetta non verificata). Fonti: [riseofkingdomsguides.com](https://riseofkingdomsguides.com/storehouse/) (2026-01-02)

**Per il bot**

- Leggere la capacita' protetta per decidere se aprire oggetti risorsa (preferire tenerli impacchettati).

**Lacune:** Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Storehouse) (2018-12-02); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/storehouse/) (2026-01-02); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)

## Trading Post
Nome italiano: **Mercato (dal client italiano del proprietario; coerente con rok.guide: le Lucerne Scrolls stanno nel Trading Post)**.

**Funzione.** Invia risorse ai membri d'alleanza tramite un mercante (trader) che occupa una coda di marcia; capacita' di trasporto sale e la tassa scende con i livelli. Ospita le Pergamene di Lucerna (Lucerne Scrolls) e, in Season of Conquest con TP 25, l'Oasis Bazaar.

**Sblocco:** City Hall 10 (tabella sblocchi CH e riseofkingdomsguides); la pagina edificio indica 1stUnlockCH=12 -> vedi conflicts. — **Livello massimo:** 25

**Pulsanti / azioni**

- **Trade / invio risorse a un alleato** [CONFERMA] — Invia risorse a un membro dell'alleanza (tassa 35% al liv.1, 8% al 25; capacita' 10M al 25). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Trading_Post) (2025-06-05); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Trading_Post/Requirements) (2026-08-11); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1896244) (2025-02-24)
- **Pergamene di Lucerna (Lucerne Scrolls) - voce con pulsante giallo** [sicuro] (IT: Pergamene di Lucerna) — Apre il pass stagionale: missioni -> Clues -> livelli con riga gratuita e righe a pagamento. Fonti: [rok.guide](https://web.archive.org/web/20231212210343/https://www.rok.guide/lucerne-scrolls/) (2020-07-23); [file](file:///home/user/military_advisor/data/fragments/quest_lucerna.json) (data n.d.); [file](file:///home/user/military_advisor/riferimenti_ui/README.md) (data n.d.)
- **Lucerne Scrolls: sblocco righe premium / acquisto livelli** [MAI] — Ancestor's Legacy e Divine Inheritance a pagamento in denaro; livelli acquistabili con 750 gemme. Fonti: [rok.guide](https://web.archive.org/web/20231212210343/https://www.rok.guide/lucerne-scrolls/) (2020-07-23)
- **Oasis Bazaar** [CONFERMA] — Compra risorse con Clamyks o VENDE risorse in cambio di gemme; limite settimanale. Si sblocca con Trading Post 25 in Season of Conquest (pioneer in alcuni regni). Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2219742) (2026-03-23); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2139649) (2025-11-14)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Trading_Post/Requirements) (2026-08-11)

**Schede interne**

- **Pergamene di Lucerna / Lucerne Scrolls** — Missioni settimanali e di stagione, ritiro ricompense della riga gratuita Fonti: [rok.guide](https://web.archive.org/web/20231212210343/https://www.rok.guide/lucerne-scrolls/) (2020-07-23); [file](file:///home/user/military_advisor/data/fragments/quest_lucerna.json) (data n.d.)
- **Oasis Bazaar** — Scambio risorse <-> Clamyks/gemme (solo SoC, TP 25) Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2219742) (2026-03-23)

**Per il bot**

- Nelle Pergamene di Lucerna: ritirare solo ricompense della riga gratuita e leggere le missioni.
- Mai toccare sblocchi premium o acquisto livelli.
- Invio risorse solo su ordine con destinatario e quantita' confermati (occupa una coda di marcia).

**Lacune:** Il nome 'Mercato' viene dal proprietario (client italiano), non da una fonte pubblica. Etichetta del pulsante di invio risorse non verificata.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Trading_Post) (2025-06-05); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Trading_Post/Requirements) (2026-08-11); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/trading-post/) (2026-01-02); [rok.guide](https://web.archive.org/web/20231212210343/https://www.rok.guide/lucerne-scrolls/) (2020-07-23); [file](file:///home/user/military_advisor/data/fragments/quest_lucerna.json) (data n.d.); [file](file:///home/user/military_advisor/riferimenti_ui/README.md) (data n.d.); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2219742) (2026-03-23); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1896244) (2025-02-24); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)

## Tavern

**Funzione.** Apertura forzieri Silver, Golden ed Equipment Chests con chiavi; aperture gratuite periodiche che aumentano con il livello. In Season of Conquest esiste anche la 'Legendary Tavern' (1.1.01).

**Sblocco:** Presente dall'inizio (CH1). — **Livello massimo:** 25

**Pulsanti / azioni**

- **Apertura gratuita (Silver / Golden)** [sicuro] — Apre un forziere senza costo quando il timer gratuito e' pronto. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Tavern) (2020-09-01); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/tavern/) (2026-01-02)
- **Apri con chiave / Open all (>=10 chiavi)** [CONFERMA] — Consuma Silver o Golden Keys; 'option to open all keys if you have 10 or more'. Fonti: [riseofkingdomsguides.com](https://riseofkingdomsguides.com/tavern/) (2026-01-02)
- **Apertura senza chiavi (prezzo in gemme)** [MAI] — Se il pulsante mostra l'icona gemma, apre il forziere spendendo gemme. Fonti: [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Tavern/Requirements) (2026-01-05)

**Schede interne**

- **Silver Chests** — Comandanti/sculture advanced-elite, risorse, speedup Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Tavern/Silver_Chests) (2020-12-02)
- **Gold Chests** — Comandanti/sculture fino a leggendari; dal 1.1.01 anche Pepin III e Casimir III Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Tavern/Gold_Chests) (2022-09-14); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2161435) (2025-11-14)
- **Equipment Chests** — Materiali/blueprint equipaggiamento; blueprint epici engineering dopo l'evento Season 2 Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Tavern/Equipment_Chests) (2023-11-23); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1935973) (2025-02-24)

**Per il bot**

- Aprire ogni giorno i forzieri gratuiti (routine sicura).
- Aprire con chiavi solo se l'utente lo abilita; fermarsi se compare l'icona gemma.

**Lacune:** Posizione/accesso della Legendary Tavern non documentati. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Tavern) (2020-09-01); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/tavern/) (2026-01-02); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2161435) (2025-11-14)

## Courier Station

**Funzione.** Casa del Mysterious Merchant: arriva alle 0:00 UTC (e piu' spesso dopo upgrade, addestramenti e barbari), icona sopra l'edificio; 16 oggetti a prezzo in gemme (sconto 30-90%) o in cibo/legno (10-40%). Dal 1.1.09 non vende piu' Deceptive Troops 24h ne' boost risorse.

**Sblocco:** City Hall 6. — **Livello massimo:** 25

**Pulsanti / azioni**

- **Acquisto con cibo/legno** [CONFERMA] — Compra un oggetto pagando risorse (utile per 'impacchettare' risorse). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station) (2020-01-11); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station/FoodWood) (2021-08-22)
- **Acquisto con gemme** [MAI] — Oggetti a prezzo in gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station) (2020-01-11)
- **Refresh (in alto a destra)** [CONFERMA] — 1° refresh gratis, poi 100/200/300/400 gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station) (2020-01-11); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/courier-station/) (2026-01-02)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station/Requirements) (2018-11-22)

**Per il bot**

- Controllare l'icona del mercante dopo le 0:00 UTC.
- Comprare solo voci in cibo/legno gia' approvate.
- Refresh solo se gratuito e abilitato; se mostra un costo in gemme: stop.

**Lacune:** Nome italiano non trovato; nel client il mercante potrebbe avere nome proprio italiano.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station) (2020-01-11); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/courier-station/) (2026-01-02); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2259768) (2026-06-23); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)

## Scout Camp

**Funzione.** Invia scout per rimuovere la nebbia, trovare Tribal Villages e Mysterious Caves; con la ricerca permette anche di spiare citta', truppe in marcia e guarnigioni. Dal 1.0.88 si possono mandare piu' scout insieme.

**Sblocco:** City Hall 2. — **Livello massimo:** 25

**Pulsanti / azioni**

- **Explore** [sicuro] — Seleziona il blocco di nebbia piu' vicino; ripremendo lo scout parte (gratuito). Fonti: [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1835007) (2024-12-17)
- **Scout su citta'/truppe/edifici di altri giocatori** [CONFERMA] — Ricognizione ostile (dalla mappa). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Scout_Camp) (2023-11-22)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Scout_Camp/Requirements) (2024-11-07)

**Per il bot**

- Esplorare con tutti gli scout liberi (azione sicura).
- Ritirare le ricompense dei villaggi (dal 1.0.89 esiste il 'claim all').
- Mai scout su giocatori senza conferma.

**Lacune:** Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Scout_Camp) (2023-11-22); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Scout_Camp/Requirements) (2024-11-07); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/scout-camp/) (2026-01-02); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1835007) (2024-12-17); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1868790) (2024-12-17); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

## Alliance Center

**Funzione.** Aiuti d'alleanza: ogni aiuto toglie max(1% del tempo residuo, 1 min; fino a 3 min con Together We Rise) a costruzioni, ricerche e cure (non addestramento ne' raccolta). Numero massimo di aiuti: 5 al liv.1, +1 per livello (30 al 25). Determina anche la capacita' di rinforzi.

**Sblocco:** City Hall 3 (tabella sblocchi CH e riseofkingdomsguides); pagina edificio 1stUnlockCH=5 -> vedi conflicts. — **Livello massimo:** 25

**Pulsanti / azioni**

- **Help (mano sopra l'edificio: aiutare gli alleati)** [sicuro] — Toccando la mano si aiutano tutti gli alleati; gratuito. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) (2026-09-26)
- **Rinforzi (reinforcement)** [sicuro] — Capacita' di truppe alleate in rinforzo nella citta'. Fonti: [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center/Requirements) (2019-02-06)

**Per il bot**

- Premere la mano 'Help' ogni volta che compare (azione sicura e utile alla routine).
- Prima di usare speedup su un timer, attendere il massimo degli aiuti.

**Lacune:** Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) (2026-09-26); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/alliance-center/) (2026-01-02); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)

## Blacksmith

**Funzione.** Sistema equipaggiamento: forgia equipaggiamento dai blueprint, produce materiali (10 materiali ogni 3 ore, coda di 5, ritiro manuale), combina 4 materiali uguali in uno di qualita' superiore, unisce 30 frammenti in un blueprint, smonta materiali (costa oro) ed equipaggiamento. Evento periodico 'Smithy Specials' (offerte).

**Sblocco:** City Hall 16 (e ricezione del primo equipaggiamento). — **Livello massimo:** 1 (la wiki elenca solo il livello 1; nessun upgrade documentato)

**Pulsanti / azioni**

- **Material Production (coda di 5) + ritiro** [sicuro] — Produce materiali gratuitamente; vanno ritirati a mano. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith) (2020-09-07)
- **Combine (materiali / blueprint)** [CONFERMA] — 4 materiali -> 1 superiore; 30 frammenti -> 1 blueprint. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith/Combining_Materials) (2020-04-30); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith) (2020-09-07)
- **Dismantle materiali** [CONFERMA] — 1 materiale -> 4 di qualita' inferiore; costa oro. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith) (2020-09-07)
- **Forge** [CONFERMA] — Forgia un pezzo di equipaggiamento consumando blueprint e materiali rari. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith) (2020-09-07)
- **Dismantle / Awaken equipaggiamento leggendario** [MAI] — Richiedono la password secondaria se impostata (1.0.83); smontare un leggendario con talento rimborsa 100% forgiatura e 50% risveglio (1.0.96). Fonti: [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2081453) (2025-11-14)
- **Smithy Specials (offerte a tempo)** [MAI] — Frammenti blueprint e materiali leggendari scontati (acquisto). Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1868790) (2024-12-17); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2219742) (2026-03-23)

**Schede interne**

- **Material Production** — coda materiali Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith) (2020-09-07)
- **Materials & Blueprint Combination** — combina/smonta Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith) (2020-09-07)
- **Forge (Weapons, Helms, Chest, Gloves, Legs, Boots, Accessories)** — forgia per slot Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith) (2020-09-07); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2030530) (2025-11-14)

**Per il bot**

- Tenere piena la coda di produzione materiali e ritirare i materiali (sicuro).
- Forge/Combine/Dismantle solo con conferma: consumano materiali rari o oro.
- Mai toccare le offerte Smithy Specials.

**Lacune:** Nome italiano non trovato. Livello massimo: la wiki mostra solo il livello 1 (tabella 2019).

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith) (2020-09-07); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith/Requirements) (2019-12-01); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1868790) (2024-12-17); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2030530) (2025-11-14); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2081453) (2025-11-14); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2219742) (2026-03-23); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-equipment-guide/) (2026-01-02); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)

## Castle

**Funzione.** Organizza i rally: ogni upgrade aumenta le truppe che il capo puo' comandare in un rally. Gli upgrade richiedono Book of Covenant.

**Sblocco:** City Hall 7. — **Livello massimo:** 25

**Pulsanti / azioni**

- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Castle/Requirements) (2021-06-23)
- **Rally / truppe in rally** [CONFERMA] — Lancio e gestione rally avvengono dal bersaglio sulla mappa; il Castle determina la capacita'. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Castle) (2018-12-02); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Per il bot**

- Upgrade solo con conferma (consuma Book of Covenant, materiale raro).
- Nessun rally contro giocatori senza conferma.

**Lacune:** Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Castle) (2018-12-02); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Castle/Requirements) (2021-06-23); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-castle-upgrade-requirements-cost-book-of-covenant/) (2026-01-02); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)

## Farm

**Funzione.** Produce cibo (food) nel tempo fino alla capacita' massima; va raccolto. Fino a 4 edifici. Dal 1.1.09 i boost di produzione come oggetto sono stati rimossi e i buff VIP di produzione aumentati.

**Sblocco:** 1a CH1, 2a CH3, 3a CH6, 4a CH9 (tabella CH; la 1a e' presente dal CH1 secondo la tabella requisiti Farm) — **Livello massimo:** 25

**Pulsanti / azioni**

- **Raccolta (icona risorsa sopra l'edificio)** [sicuro] — Riscuote la produzione accumulata; gratuito. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Farm) (2026-09-19)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Farm) (2026-09-19)

**Per il bot**

- Raccogliere periodicamente la produzione (azione sicura).

**Lacune:** Etichetta/forma esatta dell'icona di raccolta da verificare. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Farm) (2026-09-19); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2259768) (2026-06-23)

## Lumber Mill

**Funzione.** Produce legno (wood) nel tempo fino alla capacita' massima; va raccolto. Fino a 4 edifici. Dal 1.1.09 i boost di produzione come oggetto sono stati rimossi e i buff VIP di produzione aumentati.

**Sblocco:** 1a CH2, 2a CH5, 3a CH8, 4a CH11 — **Livello massimo:** 25

**Pulsanti / azioni**

- **Raccolta (icona risorsa sopra l'edificio)** [sicuro] — Riscuote la produzione accumulata; gratuito. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Lumber_Mill) (2026-09-19)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Lumber_Mill) (2026-09-19)

**Per il bot**

- Raccogliere periodicamente la produzione (azione sicura).

**Lacune:** Etichetta/forma esatta dell'icona di raccolta da verificare. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Lumber_Mill) (2026-09-19); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2259768) (2026-06-23)

## Quarry

**Funzione.** Produce pietra (stone) nel tempo fino alla capacita' massima; va raccolto. Fino a 4 edifici. Dal 1.1.09 i boost di produzione come oggetto sono stati rimossi e i buff VIP di produzione aumentati.

**Sblocco:** 1a CH6, 2a CH7, 3a CH10, 4a CH13 (pagina edificio); la tabella CH elenca 2a CH7, 3a CH10, 4a CH13 — **Livello massimo:** 25

**Pulsanti / azioni**

- **Raccolta (icona risorsa sopra l'edificio)** [sicuro] — Riscuote la produzione accumulata; gratuito. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Quarry) (2026-01-04)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Quarry) (2026-01-04)

**Per il bot**

- Raccogliere periodicamente la produzione (azione sicura).

**Lacune:** Etichetta/forma esatta dell'icona di raccolta da verificare. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Quarry) (2026-01-04); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2259768) (2026-06-23)

## Goldmine

**Funzione.** Produce oro (gold) nel tempo fino alla capacita' massima; va raccolto. Fino a 4 edifici. Dal 1.1.09 i boost di produzione come oggetto sono stati rimossi e i buff VIP di produzione aumentati.

**Sblocco:** 1a CH10, 2a CH12, 3a CH14, 4a CH16 — **Livello massimo:** 25

**Pulsanti / azioni**

- **Raccolta (icona risorsa sopra l'edificio)** [sicuro] — Riscuote la produzione accumulata; gratuito. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Goldmine) (2018-12-18)
- **Upgrade** [CONFERMA] — Avvia l'upgrade dell'edificio consumando risorse (e, per alcuni, materiali speciali); occupa una coda costruttore. Etichetta esatta del menu contestuale non documentata nelle fonti lette. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Goldmine) (2018-12-18)

**Per il bot**

- Raccogliere periodicamente la produzione (azione sicura).

**Lacune:** Etichetta/forma esatta dell'icona di raccolta da verificare. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Goldmine) (2018-12-18); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2259768) (2026-06-23)

## Builder's Hut

**Funzione.** Mostra in una schermata le code costruttore (edificio, livello, tempo residuo). Secondo costruttore: temporaneo con Builder Recruitment (2 giorni) o permanente a VIP 6.

**Sblocco:** City Hall 5? (wiki con punto interrogativo). — **Livello massimo:** 1

**Pulsanti / azioni**

- **Visualizza code costruzione** [sicuro] — Stato delle code. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Builder's_Hut) (2018-11-22)
- **Aggiungi coda con gemme** [MAI] — La descrizione in gioco: 'You can spend gems to add an additional queue'. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Builder's_Hut) (2018-11-22)
- **Usa Builder Recruitment** [CONFERMA] — Attiva/estende di 2 giorni la seconda coda. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Items/Builder_Recruitment) (2022-08-06); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Builder_queue) (2020-04-30)
- **Speedup items sulla costruzione** [CONFERMA] — Riduce i tempi con oggetti speedup. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Builder's_Hut) (2018-11-22)

**Per il bot**

- Leggere lo stato delle code per sapere se un costruttore e' libero.

**Lacune:** Livello di sblocco incerto (CH5? nella wiki). Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Builder's_Hut) (2018-11-22); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Builder's_Hut/Requirements) (2018-11-22); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Builder_queue) (2020-04-30)

## Monument

**Funzione.** Linea temporale del regno (Chronicle): obiettivi individuali, d'alleanza o di regno con ricompense (gemme, chiavi, sculture) e sblocchi di contenuti (forti barbari, sanctum, ecc.).

**Sblocco:** City Hall 8 (tabella CH e tabella requisiti Monument); la pagina edificio indica 1stUnlockCH=9 -> vedi conflicts. — **Livello massimo:** 1

**Pulsanti / azioni**

- **Claim (ricompense della timeline)** [sicuro] — Ritira le ricompense degli eventi completati. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Monument) (2025-02-21)

**Per il bot**

- Controllare e ritirare le ricompense del Monument (sicuro).

**Lacune:** Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Monument) (2025-02-21); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Monument/Requirements) (2020-04-27); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)

## Bulletin Board

**Funzione.** Mostra i messaggi dello sviluppatore (eventi e promozioni).

**Sblocco:** City Hall 1? (wiki con punto interrogativo). — **Livello massimo:** n.d.

**Pulsanti / azioni**

- **Leggi messaggi** [sicuro] — Solo lettura; i messaggi possono linkare offerte. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Bulletin_Board) (2018-11-23)

**Per il bot**

- Nessuna azione automatica; eventuali link a offerte = non toccare.

**Lacune:** Livello massimo e sblocco non confermati. Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Bulletin_Board) (2018-11-23); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings) (2020-05-11)

## Shop

**Funzione.** Acquisto con gemme di risorse, speedup, boost (incluso Peace Shield) e altri oggetti; contiene il VIP Shop (sconti per livello VIP, rinnovo lunedi 00:00 UTC). Con lo State Forum costruito vende Conversion Stones.

**Sblocco:** City Hall 5. — **Livello massimo:** n.d.

**Pulsanti / azioni**

- **Acquisto oggetti (gemme)** [MAI] — Qualsiasi acquisto con gemme. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Shop) (2023-10-12)
- **Peace Shield (8h/24h/3 giorni)** [MAI] — Attiva/compra uno scudo che protegge la citta'. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Items/Peace_Shield) (2020-04-30)
- **VIP Shop: voci pagate in risorse** [CONFERMA] — Alcune voci VIP Shop costano cibo (es. 100 AP per 12.000 cibo a VIP 2). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Shop) (2023-10-12); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/shop/) (2026-01-02)
- **VIP Shop: voci pagate in gemme** [MAI] —  Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Shop) (2023-10-12)

**Schede interne**

- **Resources / Speedups / Boosts / Other** — categorie della wiki Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Shop) (2023-10-12)
- **VIP Shop** — sconti settimanali per livello VIP Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Shop) (2023-10-12)

**Per il bot**

- Entrare solo per leggere; acquisti solo in risorse e solo con conferma.
- Mai Peace Shield (anche se richiesto: lo attiva l'utente).

**Lacune:** Livello massimo non documentato (pagina senza tabella livelli oltre il 1?). Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Shop) (2023-10-12); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/VIP_Shop) (2018-11-16); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/shop/) (2026-01-02); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1935973) (2025-02-24); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2259768) (2026-06-23)

## Lyceum of Wisdom

**Funzione.** Quiz mensile Peerless Scholar (preliminari feriali 0:00-23:00 UTC, midterm sabato 2:30 e 12:30 UTC, finale ultimo sabato 14:30 UTC; montepremi in gemme) e Kingdom Newspaper acquistabile per 1000 oro (a volte da' buff). Legato anche a World Wanderer.

**Sblocco:** City Hall 10. — **Livello massimo:** 1

**Pulsanti / azioni**

- **Peerless Scholar** [CONFERMA] — Risposte al quiz; 3 richieste di aiuto all'alleanza nei preliminari. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Peerless_Scholar) (2023-04-15)
- **Kingdom Newspaper** [CONFERMA] — Acquisto per 1000 oro. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Lyceum_of_Wisdom) (2022-05-07)

**Per il bot**

- Nessuna risposta automatica al quiz senza conferma (le risposte errate riducono le ricompense).

**Lacune:** Nome italiano non trovato.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Lyceum_of_Wisdom) (2022-05-07); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Peerless_Scholar) (2023-04-15); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/lyceum-of-wisdom-rok-answers/) (2026-09-03)

## State Forum

**Funzione.** Sistema formazioni e armamenti: Travel (20 AP, 'Travel x10' = 200 AP), Dispatch dal livello 10 (30-150 AP), Quick Dispatch, auto-recycle degli armamenti; abilita l'acquisto di Conversion Stones nello Shop.

**Sblocco:** n.d. — **Livello massimo:** n.d.

**Pulsanti / azioni**

- **Travel / Travel x10** [CONFERMA] — Consuma AP; esauriti gli AP puo' costare gemme. Fonti: [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1935973) (2025-02-24)
- **Travel pagato in gemme** [MAI] —  Fonti: [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)
- **Dispatch / Quick Dispatch** [CONFERMA] — Consuma AP. Fonti: [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1935973) (2025-02-24)
- **Recycle / Transmute / Convert / Inscribe** [MAI] — Consumano materiali rari; richiedono password secondaria. Fonti: [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.)

**Per il bot**

- Vedi automazione.json (schermata State Forum): fermarsi all'icona gemma; operazioni con password secondaria = manuali.

**Lacune:** Nessuna pagina wiki; livello di sblocco (CH) e livello massimo non trovati. Nome italiano non trovato.

Fonti: [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1935973) (2025-02-24); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1817043) (2024-12-17)

## Hall of Heroes

**Funzione.** Funzione del Lost Kingdom / Season of Conquest: restituisce una parte delle unita' perse (tasso che sale con il livello del Lost Kingdom) e, dal 1.0.89, parte delle risorse spese in cure alla fine del Lost Kingdom.

**Sblocco:** n.d. — **Livello massimo:** n.d.

**Per il bot**

- Nessuna azione nota; solo lettura.

**Lacune:** Non verificato se sia un edificio della citta' o solo un'interfaccia KvK; pulsanti ignoti.

Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1868790) (2024-12-17); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2030530) (2025-11-14)

## Crystal Research Center

**Funzione.** Ricerca con Crystal (tecnologie Crystal) nel Lost Kingdom / Season of Conquest; 'instant research' sbloccabile acquistando la Premium Season Crystal Supply.

**Sblocco:** n.d. — **Livello massimo:** n.d.

**Pulsanti / azioni**

- **Instant research (Premium Season Crystal Supply)** [MAI] — Funzione a pagamento. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1935973) (2025-02-24)

**Per il bot**

- Nessuna azione senza conferma.

**Lacune:** Non verificato se sia un edificio della citta'; sblocco e pulsanti ignoti.

Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1935973) (2025-02-24); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2124406) (2025-11-14)

## Decorazioni (Decorative: strade, alberi, lanterne ecc.) e cosmetici citta'

**Funzione.** Oggetti decorativi piazzabili (Road, King's Road, alberi, Pedestal Lantern, Stone Drum...), quest 'The Beauty of the City'. City Hall Decor (temi citta' con bonus/malus). Dal 1.0.92 Cosmetic Shop; SVIP Shop con effetti citta'; City Hall 25 espande l'area edificabile.

**Sblocco:** n.d. — **Livello massimo:** n.d.

**Pulsanti / azioni**

- **Costruisci decorazione (costo in risorse o gemme)** [MAI] — Alcune decorazioni costano gemme (es. King's Road 100, Pedestal Lantern 100 nella wiki: valore nel campo gemme del template). Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings) (2020-05-11)
- **Cosmetic Shop / SVIP Shop** [MAI] — Acquisto cosmetici. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1963188) (2025-11-14); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1817043) (2024-12-17)

**Per il bot**

- Nessuna azione: puramente estetico o a pagamento.

**Lacune:** Interpretazione dei costi decorativi dal template wiki (5=100 interpretato come gemme) non verificata in gioco.

Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings) (2020-05-11); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Quests/BuildDecorations) (2020-04-30); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Items/City_Hall_Decor) (2018-12-04); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1963188) (2025-11-14); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1868790) (2024-12-17); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1817043) (2024-12-17)

## Commander Statue / Commander Hall

**Funzione.** non documentata

**Sblocco:** n.d. — **Livello massimo:** n.d.

**Lacune:** Nessuna fonte consultata (wiki API, forum ufficiale 2024-2026, riseofkingdomsguides, heaven-guardian) documenta un edificio con questo nome. Ricerca wiki 'Commander Statue' restituisce solo Sculture.

Fonti: nessuna

## Market (edificio separato)
Nome italiano: **Mercato**.

**Funzione.** Non risulta un edificio separato: 'Mercato' nel client italiano corrisponde al Trading Post (Pergamene di Lucerna dentro). Vedi voce Trading Post.

**Sblocco:** n.d. — **Livello massimo:** n.d.

**Per il bot**

- Mappare 'Mercato' -> Trading Post.

**Lacune:** Verificare con screenshot che il titolo dell'edificio sia 'Mercato'.

Fonti: [rok.guide](https://web.archive.org/web/20231212210343/https://www.rok.guide/lucerne-scrolls/) (2020-07-23); [file](file:///home/user/military_advisor/data/fragments/quest_lucerna.json) (data n.d.); [file](file:///home/user/military_advisor/riferimenti_ui/README.md) (data n.d.)

## Regole per il bot (edifici)

- **E1_gem_icon_any_building** — Quando: In qualunque menu di edificio compare un pulsante con icona gemma (finire subito, spegnere incendio, refresh a pagamento, apertura forziere senza chiave, Travel oltre AP, coda costruttore extra) Allora: Non toccare; chiudere il menu; loggare. Perche': Le gemme non si spendono mai in automatico. Conferma: si. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Resources) (2025-05-31); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/War) (2020-09-06); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Builder's_Hut) (2018-11-22); [file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.); [file](file:///home/user/military_advisor/data/fragments/strategia_routine.json) (data n.d.)
- **E2_shield_never** — Quando: Shop o inventario mostrano Peace Shield Allora: Mai attivare o comprare scudi; notificare l'utente se la citta' e' minacciata. Perche': Regola del proprietario: mai scudi. Conferma: si. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Items/Peace_Shield) (2020-04-30)
- **E3_rare_material_upgrades** — Quando: Upgrade di Watchtower (Arrow of Resistance), Castle (Book of Covenant), edifici al 25 (Master's Blueprint), Forge/Combine/Dismantle nel Blacksmith Allora: Solo con conferma esplicita. Perche': Consumano materiali rari. Conferma: si. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Watchtower) (2020-04-30); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Castle) (2018-12-02); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Hospital/Requirements) (2022-09-14); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith) (2020-09-07)
- **E4_safe_collect** — Quando: Icone di raccolta su Farm/Lumber Mill/Quarry/Goldmine, materiali pronti nel Blacksmith, ricompense Monument, forzieri gratuiti Tavern, mano Help sull'Alliance Center Allora: Eseguire automaticamente. Perche': Azioni gratuite senza rischio. Conferma: no. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Farm) (2026-09-19); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Blacksmith) (2020-09-07); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) (2026-09-26); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/tavern/) (2026-01-02)
- **E5_help_before_speedup** — Quando: Costruzione, ricerca o cura avviata Allora: Premere Help (Alliance Help) e attendere gli aiuti prima di proporre speedup. Perche': Ogni aiuto toglie 1% o 1-3 minuti; l'addestramento non ne beneficia. Conferma: no. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) (2026-09-26); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/alliance-center/) (2026-01-02)
- **E6_mercato_is_trading_post** — Quando: Il bot deve aprire le Pergamene di Lucerna Allora: Toccare l'edificio 'Mercato' (Trading Post) e la voce con pulsante giallo; ritirare solo la riga gratuita. Perche': Mappatura dal client italiano + rok.guide. Conferma: no. Fonti: [rok.guide](https://web.archive.org/web/20231212210343/https://www.rok.guide/lucerne-scrolls/) (2020-07-23); [file](file:///home/user/military_advisor/data/fragments/quest_lucerna.json) (data n.d.); [file](file:///home/user/military_advisor/riferimenti_ui/README.md) (data n.d.)
- **E7_trading_post_send** — Quando: Invio risorse o Oasis Bazaar Allora: Solo con destinatario/quantita' confermati; mai vendere risorse per gemme senza ordine. Perche': Tassa, coda di marcia occupata, scambi irreversibili. Conferma: si. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Trading_Post) (2025-06-05); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2219742) (2026-03-23)
- **E8_wall_fire** — Quando: La citta' brucia (Wall) Allora: Avvisare l'utente; usare solo Repair gratuito; mai spegnimento con gemme. Perche': A durabilita' 0 teletrasporto casuale. Conferma: si. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Wall) (2023-12-02); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/War) (2020-09-06)
- **E9_hospital_capacity** — Quando: Ospedale oltre ~90% o sotto rally Allora: Avvisare; curare solo su ordine; durante un rally subito la cura non e' possibile. Perche': Feriti oltre capacita' muoiono. Conferma: si. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Hospital) (2020-04-30); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/hospital/) (2026-01-02)
- **E10_courier_food_wood_only** — Quando: Mysterious Merchant presente Allora: Solo acquisti in cibo/legno gia' approvati; refresh solo se gratuito. Perche': Refresh 100-400 gemme; voci in gemme vietate. Conferma: si. Fonti: [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station) (2020-01-11)
- **E11_offers_in_buildings** — Quando: Smithy Specials, Lucerne premium, Cosmetic/SVIP Shop, Crystal Supply, Kingdom Newspaper Allora: Non toccare offerte a pagamento; Kingdom Newspaper (1000 oro) solo su conferma. Perche': Acquisti reali o gemme. Conferma: si. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1868790) (2024-12-17); [rok.guide](https://web.archive.org/web/20231212210343/https://www.rok.guide/lucerne-scrolls/) (2020-07-23); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1963188) (2025-11-14); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1935973) (2025-02-24); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Lyceum_of_Wisdom) (2022-05-07)
- **E12_misclick_commanders** — Quando: Tocco su un edificio in citta' Allora: Verificare il titolo del pannello aperto prima del secondo tocco (comandanti che passeggiano possono sovrapporsi agli edifici). Perche': Patch 1.0.87 e 1.1.01 riducono ma non eliminano i misclick. Conferma: no. Fonti: [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/1817043) (2024-12-17); [forum-global.lilithgame.com](https://forum-global.lilithgame.com/post/2161435) (2025-11-14)

## Fonti in conflitto

- **Sblocco Trading Post**: City Hall 10 ([riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [riseofkingdomsguides.com](https://riseofkingdomsguides.com/trading-post/) (2026-01-02)) vs City Hall 12 (1stUnlockCH) ([riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Trading_Post) (2025-06-05)) — Tabelle requisiti piu' recenti -> CH10 piu' probabile.
- **Sblocco Monument**: City Hall 8 ([riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Monument/Requirements) (2020-04-27)) vs City Hall 9 ([riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Monument) (2025-02-21))
- **Sblocco Academy / Stable / Siege Workshop / Alliance Center**: Tabella CH: Academy CH4, Stable CH4, Siege Workshop CH5, Alliance Center CH3 ([riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04)) vs Pagine edificio: Academy 6, Stable 3, Siege Workshop 4, Alliance Center 5 ([riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Academy) (2026-01-04); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Stable) (2026-01-04); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Siege_Workshop) (2026-09-19); [riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) (2026-09-26)) — riseofkingdomsguides conferma Alliance Center a CH3.
- **Sblocco Tier 5**: City Hall 25 (tabella CH) + Academy 25 e ricerche ([riseofkingdoms.fandom.com](https://riseofkingdoms.fandom.com/wiki/Buildings/City_Hall/Requirements) (2026-01-04); [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) (2026-09-02)) vs 'Upgrading Watchtower to level 25 is needed to unlock Tier 5 units' ([riseofkingdomsguides.com](https://riseofkingdomsguides.com/watchtower/) (2026-01-02)) — Compatibili come catena di requisiti (Watchtower 25 e' prerequisito indiretto).
- **Aperture gratuite Tavern**: vedi automazione.json (handbook vs riseofkingdomsguides) ([file](file:///home/user/military_advisor/data/fragments/automazione.json) (data n.d.))

## Lacune generali

- Le etichette esatte dei menu contestuali degli edifici (Upgrade/Details/Train/Heal/Research/Help/Speed Up...) non sono documentate testualmente in nessuna fonte accessibile: i label in inglese qui sono descrittivi. Vanno confermati con screenshot del client italiano.
- Nomi italiani degli edifici: non presenti in Google Play IT, App Store IT, ne' in una wiki italiana (it.riseofkingdoms.fandom.com non raggiungibile). Unico nome certo: 'Mercato' = Trading Post (dal proprietario).
- Nessun post del forum ufficiale dopo 1.1.09 (2026-06-23) nei 300 piu' recenti: cambiamenti luglio-settembre 2026 non coperti.
- State Forum, Hall of Heroes, Crystal Research Center, Commander Statue: nessuna pagina wiki; sblocco/livelli ignoti.
- Bulletin Board e Shop: livello massimo non documentato.

## Non raggiungibili

- https://heaven-guardian.com/rise-of-kingdoms-buildings-guide/: curl: connection reset; WebFetch restituisce un'immagine WebP. Recuperata invece la guida via API WordPress.
- https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide: HTTP 404
- https://it.riseofkingdoms.fandom.com/api.php: SSL handshake failure (wiki italiana non disponibile)
