# Sculture leggendarie: quantità per fonte (aggiornato al 2026-09-28)

Dati strutturati: `data/fragments/sculture_quantita.json`. Tutte le fonti sono state consultate il 2026-09-28. Dove un dato manca è `null` ed è elencato nei gap.

> **Avvertenza generale.** La pagina ufficiale delle probabilità ([rok.lilith.com/probability](https://rok.lilith.com/probability/)) oggi contiene **solo** tabelle sugli Armament (inscription, bonus, Formation Choice Chest, "Armament, Reveal Thyself"). Non ci sono tabelle ufficiali per Tavern, Golden Chest o Wheel of Fortune. Le cifre qui sotto vengono quindi dalla wiki fandom (non datata o vecchia) e da guide della community, e vanno trattate come stime.

## 1. The Mightiest Governor (MGE)

### Premi in classifica (sculture del comandante dell'evento)
Fonte: [fandom Events/The Mightiest Governor](https://riseofkingdoms.fandom.com/wiki/Events/The_Mightiest_Governor). La tabella è stata modificata l'ultima volta nel contenuto il 2021-02-06, come risulta dalla cronologia delle revisioni.

| Posizione | Sculture |
|---|---|
| 1° | 180 |
| 2° | 90 |
| 3° | 60 |
| 4° | 50 |
| 5° | 40 |
| 6° | 30 |
| 7°–10° | 20 |
| 11°–15° | 10 |
| 16°–25° | 5 |
| 26°–35° | 3 |
| 36°–45° | 2 |
| 46°–50° | 1 |

In totale la classifica distribuisce 685 sculture. Nessuna fonte ufficiale del 2026 conferma questa tabella.

- **Premi a milestone (soglie di punti):** nessun dato trovato (`null`). Il [Handbook (2026-09-09)](https://riseofkingdomshandbook.com/guides/riseofkingdoms-mightiest-governor-guide) conferma solo che esistono "routine milestone rewards" utili anche a chi non punta alla classifica.
- **Punti per entrare in classifica:** `null`. Secondo il Handbook "there is no universal cheap winning score": dipende da regno, roster e scorte. Inoltre molti regni assegnano i posti MGE o impongono un tetto ai punteggi.

### Fasi
- Nel 2020 le fasi erano 5: Training, Barbarians, Gathering, Power (1 giorno ciascuna) ed Eliminating Enemies (2 giorni). Fonte: forum ufficiale, [Developer's Feedback 2020-09-01](https://forum-global.lilithgame.com/api/v2/posts/1000050).
- La patch 1.0.41 (2020-12) ha aggiunto la fase 6 "Sprint for the Win" (1 giorno) e ha ridotto la fase 5 a 1 giorno. Il primo MGE di ogni regno resta a 5 fasi. Fonte: [forum 1030636](https://forum-global.lilithgame.com/api/v2/posts/1030636).
- Secondo il Handbook 2026 il formato consolidato ha 6 fasi. Alcune guide commerciali più recenti parlano di una fase di "commander development", non verificata (vedi conflitti).

### Punteggi per attività
Fonte: wiki fandom, non datata. I punti del training sono confermati da [zoe-rok.com](https://zoe-rok.com/tools/calculators) (bundle JS) e dal Handbook 2026.

- **Training:** T1 5, T2 10, T3 20, T4 40, T5 100. Un upgrade vale la differenza di punti tra i due tier.
- **Barbari:** da 300 (lv1-6) a 3600 (lv25); lv26-30 4000, lv31-35 4500, lv36-40 5000, lv41-55 10000.
- **Gathering (ogni 100 unità):** food 1, wood 1, stone 2, gold 5; 1 gem = 150.
- **Power:** +2 punti per ogni punto di power (truppe, edifici, tecnologia).
- **Kill:** T1 1, T2 2, T3 4, T4 8, T5 20.
- **Final Sprint:** circa l'80% dei valori delle fasi precedenti.

### Differenze tra stagioni
Fonte: forum ufficiale.

- **Fino alla Season 3:** i comandanti MGE seguono una rotazione fissa (wiki).
- **Dalla 1.0.44 (2021-03):** dopo "Light and Darkness" (S3) si sceglie il comandante ("Commander of Choice") [1055096](https://forum-global.lilithgame.com/api/v2/posts/1055096).
- **Dalla 1.0.91 (2025-02):** nei regni in Season 3, MGE e Wheel of Fortune includono tutti i comandanti [1935973](https://forum-global.lilithgame.com/api/v2/posts/1935973).
- **Dalla 1.0.94 (2025-05):** Bertrand du Guesclin è stato rimosso dall'MGE della SoC [2030530](https://forum-global.lilithgame.com/api/v2/posts/2030530).
- **Ragnar Prime:** non compare né in MGE né nella Wheel [1801215](https://forum-global.lilithgame.com/api/v2/posts/1801215).

## 2. Wheel of Fortune (solo informativo: il bot non usa gemme)

- **Frequenza e durata:** circa ogni 2 settimane secondo la [wiki](https://riseofkingdoms.fandom.com/wiki/Events/Wheel_of_Fortune), in media ogni 3 settimane (fino a 6) secondo la [guida RG](https://riseofkingdomsguides.com/wheel-of-fortune-guide-in-rise-of-kingdoms/). L'evento dura 3 giorni.
- **Sculture per spin:** la guida RG indica un premio massimo di 8 sculture del comandante. Le quantità per singolo spin e le probabilità sono `null`, perché non sono pubblicate ufficialmente.
- **Milestone:** la guida RG, con un testo poco chiaro, parla di 5 sculture al primo forziere (10 spin) e di circa 45 sculture dai premi extra in 100 spin. Il Handbook 2026 dice che i forzieri milestone sono la parte garantita e che non bisogna dare per scontato che 10 spin bastino per il reclutamento.
- **Costi (guida RG, dati contraddittori):**
  - uno spin gratuito;
  - spin scontato al 50% a 400 gemme;
  - 10 spin per 5.600 gemme;
  - 100 spin per 70.400 gemme (circa 1.564 gemme per scultura).
- **Spin Ticket:** dalla 1.0.92 (2025-03) in S3 e SoC, e dalla 1.0.94 in S2, per girare la ruota servono gli Spin Ticket, che si comprano con gemme o bundle ([1963188](https://forum-global.lilithgame.com/api/v2/posts/1963188), [2030530](https://forum-global.lilithgame.com/api/v2/posts/2030530)). Il costo di un ticket in gemme non è stato trovato.
- **Multi-spin:** aggiunto con la 1.1.03 (2026-01) [2197960](https://forum-global.lilithgame.com/api/v2/posts/2197960).
- **Pool per stagione:**
  - S2: aggiunti Takeda Shingen, Cyrus the Great, Cheok Jun-gyeong, Bertrand du Guesclin, Archimedes e Mary I.
  - SoC: speedup di costruzione sostituiti da healing speedup; rimossi Takeda, Cyrus e Cheok.

## 3. Golden Chest della Tavern

Tabella dalla [wiki (rev. 2022)](https://riseofkingdoms.fandom.com/wiki/Buildings/Tavern/Gold_Chests):

| Premio | Probabilità |
|---|---|
| Legendary Commander (10 sculture se già posseduto) | 0.80566% |
| Legendary Commander Sculpture | 3.07422% |
| Epic Commander | 2.34762% |
| Elite Commander | 3.41472% |
| Epic Sculpture | 8.45411% |
| Elite Sculpture | 15.97166% |
| Dazzling Starlight | 4.88385% |
| Brand-new Starlight | 9.7677% |
| Resource Item | 17.09348% |
| Speedup | 12.82011% |
| Tome of Knowledge | 21.36685% |

Il numero di sculture per ogni drop "Legendary Commander Sculpture" è `null`. Secondo la wiki ogni forziere contiene 4 oggetti.

- **Pool comandanti:** sono esclusi i leggendari della Wheel, i premi KvK e gli esclusivi di MGE, Expedition e VIP. Aggiunte ufficiali: Pyrrhus (1.0.71), Pepin III e Casimir III (1.1.01). Il Handbook cita come esempi Julius Caesar, Charles Martel, El Cid, Cao Cao, Cleopatra VII, Mehmed II, Mulan, Ragnar Lodbrok e Seondeok.
- **Forziere gratuito e Golden Key:**
  - il forziere gratuito si ricarica ogni 3 giorni con la Tavern al lv1 e ogni 2 giorni al lv25 ([RG Tavern](https://riseofkingdomsguides.com/tavern/));
  - nessuna fonte parla di tabelle di drop diverse tra forziere gratuito e Golden Key;
  - secondo il [Handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-tavern-keys-guide) accumulare chiavi non dà vantaggi, se non durante gli eventi che contano le aperture.
- **Pity:** non documentata per il Golden Chest.
- **Legendary Tavern / Legendary Chest (SoC):**
  - 1.0.44: evento Legendary Tavern.
  - 1.0.55/56: evento Heart's Desire, con Sovereign Key.
  - 1.0.60 (2022-07): l'evento viene chiuso e sostituito dal Legendary Chest nella Tavern, che si apre con Sovereign Key o gemme ([1359527](https://forum-global.lilithgame.com/api/v2/posts/1359527)).
  - Da dove arrivano le Sovereign Key: Silk Road (1.0.79) e, dalla 1.1.02, il Daily Objective Chest da 100 Activity Points in SoC.
  - Guide RG ([1](https://riseofkingdomsguides.com/legendary-tavern-guide-rise-of-kingdoms/), [2](https://riseofkingdomsguides.com/legendary-tavern-event-guide-rok/)), forse non più attuali:
    - almeno 1 scultura leggendaria ogni 10 chest;
    - scelta del premio al chest numero 200;
    - limite di 2000 chest al giorno;
    - i doppioni di comandanti già al massimo diventano Legendary Marks, da spendere nell'Exchange Shop (dove si trovano anche universali).

## 4. Scambio delle sculture universali leggendarie

- Una Legendary Commander Sculpture si può scambiare con una scultura di qualsiasi leggendario **già posseduto**. Il rapporto è 1:1, ma questo si ricava dalla descrizione dell'oggetto e non è indicato come numero da una fonte ufficiale ([wiki](https://riseofkingdoms.fandom.com/wiki/Items/Commander_Sculpture)).
- **Eccezioni (wiki 2022):** Minamoto no Yoshitsune, Æthelflæd, Hannibal Barca.
- Ragnar Prime accetta le universali ([1801215](https://forum-global.lilithgame.com/api/v2/posts/1801215)).
- Dopo un Commander Swap le sculture restano ([1904121](https://forum-global.lilithgame.com/api/v2/posts/1904121)).
- Nel Commander Trial le universali potenziano direttamente le skill (1.0.88).
- L'evento "A Will to Skill" premia l'uso di universali su comandanti specifici (1.0.88, 1.1.00).
- La reversibilità dello scambio non è documentata (`null`).
- **Costo totale di un leggendario:** 690 sculture per portare le skill da 1-1-1-1 a 5-5-5-5, oltre alle 10 per il reclutamento ([RG sculptures](https://riseofkingdomsguides.com/rise-of-kingdoms-sculptures-guide/)).

## Regole per il bot
1. **Mai gemme:** niente spin a pagamento, Spin Ticket, Golden Key, Legendary Chest o Sovereign Key acquistati con gemme.
2. **Spendere sculture solo con conferma esplicita:** vale sia per lo scambio delle universali sia per gli upgrade delle skill.
3. **Aprire da soli solo le risorse gratuite:** il Golden Chest gratuito sì. Golden Key, Sovereign Key e ticket posseduti si usano solo con conferma.
4. **MGE:** nessuna previsione sulla soglia di classifica. Rispettare le regole del regno sui cap di punteggio.

## Conflitti principali
- **Fase finale MGE:** la patch 1.0.41 dice 1 giorno, la guida RG dice 48 ore.
- **Frequenza della Wheel:** 2 settimane secondo la wiki, 3–6 settimane secondo la guida RG.
- **Garanzia del Legendary Tavern ogni 10 chest:** una guida parla di una scultura, l'altra di un comandante.
- **Esistenza dell'evento Legendary Tavern oggi:** il forum lo dà per chiuso nel 2022, ma le guide aggiornate nel 2026 lo descrivono ancora e le patch 2025 citano ancora la "Legendary Tavern".

## Gap e fonti non raggiungibili
- **Gap:** sculture per le milestone MGE; tabella ufficiale della classifica 2026; soglie di punteggio; probabilità e quantità della Wheel; costo degli Spin Ticket; probabilità ufficiali del Golden Chest e del Legendary Chest; pity; reversibilità dello scambio universali.
- **Fonti non raggiungibili o non utili:**
  - heaven-guardian.com: connessione resettata, e la home è un marketplace di account;
  - appgamer.com: errore 403;
  - rok.guide: errore 503;
  - rok.wiki: errore 502;
  - fandom Legendary_Tavern: la pagina non esiste.
