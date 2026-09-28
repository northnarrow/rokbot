# Stelle, promozione e sculture per classe di comandante

Aggiornato al 2026-09-28. Dati strutturati: `data/fragments/ottenimento_epic_elite_stelle.json`, che completa `data/fragments/sculture_stelle.json`.
I nomi tecnici sono in inglese, come nel gioco. Quando due fonti non concordano, la divergenza è riportata esplicitamente.

## 1. Regole comuni a tutte le rarità

- **Stelle e livello massimo.** Ogni stella alza il livello massimo di 10: 1★ = lv10, 2★ = lv20, 3★ = lv30, 4★ = lv40, 5★ = lv50, 6★ = lv60.
  Fonti: [heaven-guardian, 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-level-up-commanders-fast-guide/) e la [wiki Commander Guide](https://riseofkingdoms.fandom.com/wiki/Commander_Guide).
- **Sblocco delle skill.** Le stelle 1-4 sbloccano le skill 1-4: per ogni Epic ed Elite verificato, i dati di gioco riportano `unlockStar` = 1, 2, 3, 4 e `maxStar` = 6 ([app.rokstats.online](https://app.rokstats.online/commanders/boudica), gameVersion 1.1.12.20).
  Le stelle 5 e 6 non sbloccano skill: alzano il livello massimo e danno punti talento extra (wiki Commander Guide, che non indica quanti).
- **Secondario.** Un comandante può avere un secondario nella marcia solo da 3★ in su (wiki Commander Guide; [gamesguideinfo](https://www.gamesguideinfo.com/rise-of-kingdoms/guide/commanders)).
- **Promozione.** Per passare alla stella successiva bisogna aver raggiunto il livello massimo di quella attuale: 2★ richiede lv10, 3★ lv20, 4★ lv30, 5★ lv40 e, per analogia, 6★ lv50 (gamesguideinfo).
  La promozione consuma **Starlight Sculptures** della stessa rarità:
  - Legendary: *Dazzling*
  - Epic: *Brand-new*
  - Elite: *Ordinary*
  - Advanced: *Obsolete*
- **Star EXP e fortuna.** Ogni Starlight dà "Star EXP" e fortuna ([wiki Items/Starlight Sculpture](https://riseofkingdoms.fandom.com/wiki/Items/Starlight_Sculpture), rev. 2026-01-17):

  | Tipo | Star EXP | Luck |
  |---|---|---|
  | regular | 100 | +10% |
  | Blessed | 400 | +20% |
  | Bundle of | 800 | +5% |

  Il critico può raddoppiare l'EXP. La wiki descrive il "trucco delle 3 stelle": caricare la prima stella all'80% e poi aggiungere 6 Starlight insieme, sperando nel critico, per saltare direttamente a 3★.
- **EXP conservata al cap.** Secondo la patch ufficiale 1.0.50 (2021-09-06, [forum Lilith](https://forum-global.lilithgame.com/api/v2/posts?account_id=10000000)), un comandante bloccato al livello massimo della sua stella **conserva** l'EXP guadagnata e la applica dopo la promozione.
  Questo **contraddice** quanto scritto in `sculture_stelle.json` ("EXP persa"): vedi i conflitti nel JSON.
- **Upgrade delle skill.** Ogni upgrade sceglie **a caso** una skill sbloccata che non è ancora al massimo (wiki; gamesguideinfo). Per questo si resta a 1★ finché la skill 1 non arriva a 5.
  Il costo dipende dal **numero progressivo** dell'upgrade, non dalla skill: il calcolatore di [zoe-rok](https://zoe-rok.com/tools/calculators) somma (livello − 1) di tutte le skill.
- **Evocazione.** Servono 10 sculture specifiche per evocare un comandante di qualsiasi rarità ([heaven-guardian, 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-commander-sculptures-guide/); wiki).

## 2. Costo in sculture per upgrade (16 upgrade = 4 skill a livello 5)

Fonti: la tabella di heaven-guardian (2026-09-19) coincide con gli array del bundle JS di zoe-rok (`/_next/static/chunks/ef6276afd87c9c52.js`) ed è confermata dai totali della wiki e di [riseofkingdomsguides](https://riseofkingdomsguides.com/rise-of-kingdoms-sculptures-guide/).

| Upgrade n. | Legendary | Epic | Elite | Advanced |
|---|---|---|---|---|
| 1-4 | 10, 10, 15, 15 | 10, 10, 10, 20 | 10, 10, 10, 10 | 10, 10, 10, 10 |
| 5-8 | 30, 30, 40, 40 | 20, 20, 20, 30 | 10, 20, 20, 20 | 10, 10, 10, 10 |
| 9-12 | 45, 45, 50, 50 | 30, 30, 30, 40 | 20, 20, 30, 30 | 10, 20, 20, 20 |
| 13-16 | 75, 75, 80, 80 | 40, 40, 40, 50 | 30, 30, 30, 40 | 20, 20, 20, 30 |
| **Totale skill** | **690** | **440** | **340** | **240** |
| + evocazione | 700 | 450 | 350 | 250 |

Il costo cumulativo corrisponde al massimo che si può spendere a ogni stella, perché ogni stella sblocca 4 upgrade in più:

| Build | Stella minima | Legendary | Epic | Elite | Advanced |
|---|---|---|---|---|---|
| 5111 | 1★ | 50 | 50 | 40 | 40 |
| 5511 / 5151 / 5115 | 2★ | 190 | 140 | 110 | 80 |
| 5551 (e varianti) | 3★ | 380 | 270 | 210 | 150 |
| 5555 | 4★ | 690 | 440 | 340 | 240 |

**Expertise (skill 5, detta anche "risveglio").** Esiste solo per Epic e Legendary. Si sblocca quando le 4 skill sono a livello 5 e non costa sculture in più (heaven-guardian; wiki Commanders).
Nei dati di gioco rokstats l'expertise ha `unlockStar` = null e `replacesSlot` (potenzia o sostituisce una skill), e il ritratto ha una variante `awakened`. Per gli **Elite** rokstats restituisce `expertise` = null (Constance, Gaius Marius, Lancelot, Tomoe Gozen).

## 3. Promozione con le Starlight: valori noti

Dalla wiki Starlight (2026), valori uguali per tutte le rarità e calcolati senza fortuna:

| Stella da raggiungere | Star EXP | Regular / Blessed / Bundle |
|---|---|---|
| 2★ | non documentata ("?") | – |
| 3★ | non documentata ("?") | – |
| 4★ | 6.500 | 65 / 17 / 9 |
| 5★ | 16.000 | 160 / 40 / 20 |
| 6★ | non documentata ("?") | – |

**Dove si trovano le Starlight**

- Silver Chest: Brand-new, Ordinary, Obsolete.
- Golden Chest: Dazzling, Brand-new.
- Daily Objectives: Brand-new x2.
- Expedition Medal Store (wiki 2024):
  - Brand-new: 150 medaglie
  - Blessed Brand-new: 600 medaglie
  - Dazzling: 1.000 medaglie
  - Blessed Dazzling: 4.000 medaglie
  - Obsolete: 20 medaglie
- VIP Shop, pagando in risorse (vedi `sculture_stelle.json`):
  - Brand-new: 60k Food, x20 a settimana, da VIP 4
  - Dazzling: 400k Wood, x5 a settimana, da VIP 5
- Forti barbari: Brand-new, con probabilità bassa.

**Buchi nei dati.** Mancano la Star EXP per 2★, 3★ e 6★ e la probabilità del critico.

## 4. EXP per livello

Tabella della [wiki Commanders/Experience](https://riseofkingdoms.fandom.com/wiki/Commanders/Experience) (rev. 2023-03-20). Le proporzioni sono fisse: Legendary = 1,2 × Epic, Elite = 0,8 × Epic, Advanced = 0,6 × Epic.
La riga N sembra essere l'EXP per passare da N−1 a N, ma la tabella è **ambigua**: la riga 60 riporta "Max" e le righe 51-59 ripetono il valore della 50.
Non è stato possibile confrontarla con il calcolatore di riseofkingdomsguides, che è protetto da un anti-bot. La tabella completa è in `xp_table.rows` nel JSON.

Somme **derivate**, cioè calcolate da noi e non pubblicate dalla fonte:

| EXP da lv1 a | Legendary | Epic | Elite | Advanced |
|---|---|---|---|---|
| 10 | 56.400 | 47.000 | 37.600 | 28.200 |
| 20 | 561.000 | 467.500 | 374.000 | 280.500 |
| 30 | 1.794.600 | 1.495.500 | 1.196.400 | 897.300* |
| 40 | 5.442.600 | 4.535.500 | 3.628.400 | 2.721.300 |
| 50 | 22.482.600 | 18.735.500 | 14.988.400 | 11.196.300 |
| 60 (righe 2-59) | 47.862.600 | 39.885.500 | 31.908.400 | n.d. |

\* Per l'Advanced al livello 30 la wiki riporta "81,00": è corretto in 81.000 in base alla proporzione.
Per gli Advanced le righe 51-60 sono vuote e rokstats non ha dati su questa rarità.

## 5. Fonti di EXP

- **Tomes of Knowledge**: Lv1 = 100, Lv2 = 500, Lv3 = 1.000, Lv4 = 5.000, Lv5 = 10.000, Lv6 = 20.000, Lv7 = 50.000 EXP.
  I valori coincidono tra la wiki Tome of Knowledge e il calcolatore XP di zoe-rok. Si ottengono da barbari, Daily Objectives (Lv1 x40), stage Expedition, chest, VIP chest, eventi (Clarion Call, Hungry Turkey, Warpath…) e dal Medal Store dell'Expedition (Lv3).
- **Barbari**: l'EXP va sia al primario sia al secondario (wiki Barbarians). Livelli 1-10: 106 × livello; livelli 11-25: 100 × livello (lv25 = 2.500).
  Dal livello 26 in poi (fino al 40 nella Season of Conquest) la tabella non c'è. Il consiglio è attaccare il livello più alto che si batte senza perdite ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-how-to-level-up-commanders-fast)).
- **Guardiani dei Holy Sites**: non consumano Action Points (heaven-guardian). EXP per guardiano: Sanctum 2.500, Altar 4.000, Shrine 7.000, Temple 10.000.
  Il *Sanctum of Courage* dà +10% Commander EXP Gain (wiki Holy Sites).
- **Forti barbari** (solo in rally): Experience Books per ogni partecipante (wiki; handbook).
- **Expedition**: **nessuna EXP diretta** ai comandanti (regola del modo, wiki). Dà solo tomi.
- **Tema città Hedvig** (Season of Conquest): +5% Commander EXP (patch 1.1.02).
- **Comandanti con bonus EXP dai barbari** (valori da rokstats):
  - **Lohar**, skill 3: 10/20/30/50/70%.
  - **Boudica**, skill 2: 20% fisso. La wiki dice 25%: conflitto, prevale rokstats.
  - **Diaochan**, skill 2: 5/10/15/20/25%.
  - Leggendari già trattati in `sculture_stelle.json`: Mulan 15-95%, Aethelflaed 5-35%, Moctezuma I 5-25%.
  - Talento **Quick Study**: 5/10/15% (bundle JS di roktalents).

## 6. Come si ottengono le sculture Epic, Elite e Advanced

**Fonti comuni**

- **Silver Chest**: gratuite ogni giorno, 5 al giorno secondo handbook e da 3 a 10 in base al livello della Tavern secondo riseofkingdomsguides.
  - Epic: x1-3 sculture, esclusi Lohar e Keira.
  - Elite e Advanced: x1-10, oppure il comandante intero.
- **Golden Chest**: x1-10 sculture.
- **Expedition Medal Store**:
  - Epic in evidenza a rotazione settimanale: 1.000 medaglie ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-expedition-guide), wiki).
  - Constance: sempre disponibile, 400 medaglie.
- **Universali**:
  - Epic: Daily Objectives, Lord of War, VIP chest 7-9; il VIP Shop le vende a gemme.
  - Elite: VIP chest 4-6, Expedition 800 medaglie.
  - Advanced: VIP chest 1-3, Expedition 150 medaglie.

**Per comandante** (dettaglio con fonti nel JSON)

- **Tavern + Expedition + universali**: Baibars, Belisarius, Björn Ironside (anche eventi), Boudica, Catherine de' Medici, Eulji Mundeok, Hermann, Imhotep (anche eventi), Joan of Arc, Kusunoki Masashige, Matilda of Flanders, Narses, Osman I, Pelagius, Pericles (anche eventi), Queen Tamar (anche eventi), Scipio Africanus (anche Imperial Wealth), Sun Tzu.
  Dodici di loro sono anche i comandanti iniziali delle civiltà (wiki).
- **Keira**: solo dal negozio della Ceroli Crisis. Le universali **non** si possono usare.
- **Lohar**: Lohar's Trial (Junior x1-3, Dauntless x1-4) + universali. Non esce dalle Silver Chest.
- **Diaochan**: eventi, bundle "Intriguing Dancer" (a pagamento) e universali. Per zoe-rok esce anche dalle chest: conflitto, prevale rokstats.
- **Wak Chanil Ajaw**: eventi (zoe-rok: premi KvK1) e universali.
- **Constance**: Expedition (sempre) e universali elite. Per zoe-rok esce anche dalle chest: conflitto.
  Consiglio della wiki: spendere le universali elite **solo** su Constance.
- **Gaius Marius, Lancelot, Tomoe Gozen, Šárka**: Silver e Golden Chest, Expedition e universali. Šárka non è presente su rokstats.
- **Centurion, City Keeper, Dragon Lancer, Markswoman**: Silver Chest, Expedition e universali. Nessun dato di gioco su rokstats. Markswoman si riceve alla creazione dell'account.

## 7. Conflitti principali (dettaglio in `conflicts`)

1. **EXP oltre il cap di stella**: `sculture_stelle.json` la considera persa, la patch ufficiale 1.0.50 dice che viene conservata. Prevale la fonte ufficiale.
2. **Sculture specifiche come materiale per le stelle**: la wiki del 2022 dice di sì, le fonti del 2026 dicono che servono solo le Starlight. Non risolto.
3. **Universali epiche dai Daily Objectives**: x4 o x3. **VIP Shop per le sculture epiche**: VIP 8 o VIP 9.
4. **Boudica**: 20% (rokstats) o 25% (wiki).
5. **Ottenimento di Diaochan, Constance e Wak**: zoe-rok e rokstats non concordano. Prevale rokstats.

## Fonti irraggiungibili

- Calcolatori JS di riseofkingdomsguides: pagina anti-bot; WebFetch e wp-json non contengono lo script.
- web.archive.org: connessione interrotta (connection reset).
- rokstats per i comandanti Advanced e per Šárka: pagina non trovata (404).
- Pagine wiki per Imhotep, Narses, Pericles, Catherine, Tamar e Wak: non esistono.
