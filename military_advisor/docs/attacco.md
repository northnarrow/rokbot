# Consigliere militare — ATTACCO (meta settembre 2026)

Ricerca del **28/09/2026**. Dati strutturati per il bot: `data/fragments/strategia_attacco.json` (coppie, meccaniche, tattiche, rally, canyon, Ark, regole per il bot, fonti, conflitti, lacune).
Nomi tecnici in inglese. Accanto a ogni affermazione c'è la fonte con la data della pagina. Dove le fonti non concordano lo trovi scritto nel testo e nella sezione *conflicts* del JSON. I dati marcati "(KB)" vengono da `data/commanders.json`, `data/armamenti.json` o `data/truppe_pve.json`, sempre con la loro fonte originale.

> **Vincoli del bot, sempre validi:** qualsiasi attacco, rally, swarm, scout o sfida contro un **giocatore** richiede la **conferma dell'utente**. Le **gemme non si spendono mai**, per nessun motivo: né teleport a gemme, né "Rapid Retreat", né acquisto di speedup o ticket.

---

## 1. Meta 2026: quali coppie usare

### 1.1 Regole di base per formare una coppia
- Alla marcia si applicano **solo i talenti e l'equipaggiamento del primario**. Il secondario contribuisce solo con le sue skill ([handbook – Commanders hub, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-commanders-guide-hub) · [handbook – Best pairs, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-commander-pairs)).
- Non usare la stessa secondaria in due marce. Conviene pianificare **tutta la lineup** invece di una sola coppia perfetta ([heaven-guardian, 12/08/2026](https://heaven-guardian.com/rise-of-kingdoms-best-commander-pairings/)).
- Scegli in base al **tipo di danno** della coppia (skill, smite/normale, combo) prima di decidere formazione, iscrizioni e accessori ([handbook – Formations, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-formations-armaments-inscriptions-guide)).
- "New does not automatically mean better": le liste meta sono istantanee e cambiano con ogni nuovo comandante ([ldshop, 31/08/2026](https://www.ldshop.gg/blog/rise-of-kingdoms/best-commander-pairings.html)).

### 1.2 Campo aperto per numero di marce ([allclash, 04/08/2026, agg. 08/09/2026](https://www.allclash.com/best-commander-pairings-defense-rally-open-field-canyon-barbarians/))

| Marce | Lineup (primario + secondario) |
|---|---|
| **3** (una per tipo) | Qin Shi Huang + Zhuge Liang (arcieri) · Sun Tzu Prime + Liu Che (fanteria) · Arthur Pendragon + Achilles (cavalleria) |
| **5** (1 cavalleria) | QSH + Yi Seong-Gye · Sun Tzu Prime + Bai Qi · Arthur + Achilles · Hermann Prime + Alp Arslan · Liu Che + Philip II |
| **7** | QSH + Zhuge Liang · Sun Tzu Prime + Liu Che · Achilles + Gang Gamchan · Hermann Prime + Alp Arslan · Philip II + Bai Qi · Arthur + Hector · Scipio Africanus Prime + Ragnar Prime |

- heaven-guardian riporta le stesse lineup a 5 e a 7 marce e avverte: *"Five well-equipped armies can perform better than seven weak ones"* ([12/08/2026](https://heaven-guardian.com/rise-of-kingdoms-best-commander-pairings/)).
- ldshop propone uno schema a 5 marce con **QSH + Zhuge Liang** al posto di QSH + YSG ([31/08/2026](https://www.ldshop.gg/blog/rise-of-kingdoms/best-commander-pairings.html)). È un conflitto minore: allclash mette YSG dietro QSH proprio per lasciare Zhuge libero per un'altra marcia.
- Code di marcia ordinarie: 1 all'inizio, poi 2 con il Municipio al livello 5, 3 all'11, 4 al 17 e 5 al 22. Le marce extra stagionali, come i nodi Crystal Tech *Expanded Formations I/II* (+1 ciascuno), si sommano a parte ([handbook – Troop capacity](https://riseofkingdomshandbook.com/guides/riseofkingdoms-troop-capacity-march-queues-guide), [simulatore Crystal Tech](https://rok-technology-simulator.netlify.app/)).

### 1.3 Coppie per tipo di truppa e budget

La colonna budget è una sintesi delle fonti (heaven-guardian "new players", ldshop "early game", handbook "investment limit", priorità di investimento allclash), non un'etichetta ufficiale.

| Budget | Truppa | Primario + secondario | Perché (fonte) | Formazione |
|---|---|---|---|---|
| high | arcieri | **Qin Shi Huang + Zhuge Liang** | Coppia di arcieri più forte, con AoE e pressione nelle grandi battaglie ([allclash QSH](https://www.allclash.com/best-bai-qin-shi-huang-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/), [ldshop](https://www.ldshop.gg/blog/rise-of-kingdoms/best-commander-pairings.html)) | Wedge |
| high | fanteria | **Sun Tzu Prime + Bai Qi** | Smite in AoE con il true damage di Military Sage. Allclash dà Sun Tzu Prime S+ ([tier 10/09/2026](https://www.allclash.com/best-commanders-tier-list-in-rise-of-kingdoms-with-talents/)) | **Pincer** (allclash indica Wedge: vedi §2.2) |
| high | cavalleria | **Arthur Pendragon + Achilles** | Combo; *"one of the safest high-end Cavalry recommendations"* (ldshop) | **Delta** (allclash indica Wedge) |
| high | arcieri | **Hermann Prime + Alp Arslan** | Il poison e la riduzione di difesa di Hermann alimentano Pierce e Parthian Shot di Alp; *"Hermann (Prime) is THE pairing"* ([allclash Alp](https://www.allclash.com/best-alp-arslan-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/)) | Wedge |
| high | fanteria | **Liu Che + Philip II** | Da usare quando Sun Tzu Prime e Bai Qi sono già occupati (ldshop) | Pincer (alt. Wedge) |
| high | cavalleria | Achilles + Gang Gamchan | Seconda marcia di cavalleria combo ([allclash GG](https://www.allclash.com/best-gang-gamchan-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/)) | Delta |
| high | cavalleria | Arthur + Ivan IV | Coppia premium emergente: Ivan IV esce a fine agosto 2026 ed è S+ per allclash ([allclash Ivan](https://www.allclash.com/best-ivan-iv-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/), ldshop) | Delta |
| high | cavalleria | Arthur + Subutai | *"literally designed to go along Arthur"* ([allclash Arthur](https://www.allclash.com/best-arthur-paragon-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/)); funziona anche nei rally | Delta |
| high | cavalleria | Gang Gamchan + William Marshal | Single target in campo aperto. Marshal **mai primario** ([allclash Marshal, 29/08/2026](https://www.allclash.com/best-william-marshal-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/)) | Delta |
| mid | arcieri | Boudica Prime + Zhuge Liang (o YSG) | *"a perfect pair"* ([allclash Zhuge](https://www.allclash.com/best-zhuge-liang-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/)); secondo il [handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-commander-pairs) è una coppia consolidata | Wedge |
| mid | fanteria | Guan Yu + Scipio Africanus Prime | AoE e silence di Guan Yu con gli scudi di Scipio. Allclash invertirebbe l'ordine | Wedge |
| mid | cavalleria | Alexander Nevsky + Joan of Arc Prime | Coppia consolidata. Nevsky sceso ad A per allclash, ancora S+ nella tier SoC di ldshop (luglio 2026) | Wedge |
| mid | fanteria | Bai Qi + Liu Che · William Wallace + Liu Che · Sargon + Liu Che | Smite consolidato; allclash: Sargon + Liu Che *"can even give top meta setup a hard time"* | Pincer / Wedge |
| F2P | misto | **Aethelflaed + Sun Tzu** | Aethelflaed si ottiene dall'Expedition e porta debuff AoE ([heaven-guardian](https://heaven-guardian.com/rise-of-kingdoms-best-commander-pairings/), ldshop) | Wedge |
| F2P | fanteria | **Bjorn Ironside + Sun Tzu** | Bjorn applica la vulnerabilità prima dell'AoE di Sun Tzu (ldshop; [handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-commander-pairs)) | Wedge |
| F2P | cavalleria | Pelagius + Baibars | Non consuma sculture universali (ldshop); heaven-guardian la scrive in ordine inverso | Wedge |
| F2P | arcieri | Kusunoki + Imhotep (o Kusunoki + Hermann epico) | Handbook e heaven-guardian | Wedge |
| low | fanteria/cav. | Charles Martel + Sun Tzu · Minamoto + Cao Cao | Solo se li hai già sviluppati. Per allclash conviene investirci solo prima di KvK4/SoC | Wedge |

**Equipaggiamento.** Le pagine build di allclash mostrano 4 livelli di elmo, corazza e arma. Guanti, gambali, stivali e accessori non sono indicati.
- **Arcieri:** Helm of Phoenix + Milanese Plate + Blessed Blade → Revival Helm/Plate + Golden Age → set Dragon's Breath → Ancestral Mask of Night + Dragon's Breath Plate + The Hydra's Blast.
- **Fanteria:** Helm of Phoenix + Infantry Breastplate + Blessed Blade → Witch's Lineage + Hope Cloak + Gatekeeper's Shield → Gold Helm/Shield of the Eternal Empire + Hope Cloak → Helm of the Conqueror + Hope Cloak + Hammer of the Sun and Moon.
- **Cavalleria:** Windswept War Helm + Windswept Breastplate + Vanguard Halberd → Expedition War Helm + Heart of the Saint → Heavy Armor of the Hellish Wasteland → Pride of the Khan + Hellish Wasteland + Sacred Dominion.

Fonti: [allclash, pagine build agg. 22-23/08/2026](https://www.allclash.com/best-sun-tzu-prime-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/).

**Armamenti.** Slot 1 attacco del tipo di truppa, slot 2 difesa, slot 3 salute oppure All Damage. Le iscrizioni vanno scelte in base al tipo di danno. Non rinunciare a molte statistiche utili solo per il nome di una formazione ([handbook – Formations](https://riseofkingdomshandbook.com/guides/riseofkingdoms-formations-armaments-inscriptions-guide); KB: [touchscreengaming](https://touchscreengaming.com/formations-guide/), [rok.lilith.com](https://rok.lilith.com/probability/)).

### 1.4 Rally e Canyon
- **Rally** (rating allclash, 10/09/2026):
  - S+: William Marshal, Ivar the Boneless, Subutai, Shapur, Tariq ibn Ziyad, Justinian.
  - S: Alp Arslan, Huo Qubing, Siyaj K'ak', Sargon, Nebuchadnezzar, Boudica Prime, Xiang Yu, Henry, Pakal II, Gilgamesh.
  - Coppie: Ivar + Bai Qi (fanteria: [heaven-guardian](https://heaven-guardian.com/rise-of-kingdoms-best-commander-pairings/), [ldshop](https://www.ldshop.gg/blog/rise-of-kingdoms/best-commander-pairings.html)), Subutai + William Marshal (combo di cavalleria), Arthur + Subutai, Shapur + Ashurbanipal (arcieri; Shapur *"can neutralize shields"*, [ldshop difesa 22/09/2026](https://www.ldshop.gg/blog/rise-of-kingdoms/kvk-defense-guide.html)), Nebuchadnezzar II + Gilgamesh, Scipio Prime + Tariq.
- **Canyon:**
  - S+: Alp Arslan, Sun Tzu Prime, Ragnar Prime, Shajar al-Durr, Constantine.
  - Alp Arslan + Shajar al-Durr è *"more for Canyon than for open field"* ([allclash Alp](https://www.allclash.com/best-alp-arslan-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/)). Vedi §4.2.

---

## 2. Meccaniche nuove e cosa cambiano

### 2.1 Combo
- **Cos'è.** Skill che lanciano più colpi in sequenza (*"uses combo attacks to unleash a barrage of damage"*, [rokstats, dati del client](https://app.rokstats.online/talents/combo)).
- **Chi le usa.**
  - Ramo Combo: Achilles, Arthur Pendragon, Bertrand du Guesclin, Gang Gamchan, William Marshal.
  - Con specialità Combo: anche Ivan IV, David IV e Subutai ([allclash tier](https://www.allclash.com/best-commanders-tier-list-in-rise-of-kingdoms-with-talents/)).
- **Esempi dalle skill** (KB, [riseofkingdomsguides](https://riseofkingdomsguides.com/king-arthur-talent-tree-build-and-guide-rise-of-kingdoms/)):
  - Arthur da primario: 2 combo su 3 bersagli con DF 1400, più +10% combo damage (×3 contro truppe sul campo).
  - Subutai: 3 combo single target con DF 1000.
- **Bonus:** Delta Formation +10% combo; Ivan IV +15%; William Marshal +15%.
- **Contromisure:** Achilles riduce del 10-15% skill, combo e counterattack subiti; Ivar da rally leader fa subire −10% combo damage all'armata radunata.
- **Cosa cambia:** una marcia combo usa **Delta** e bonus che nominano esplicitamente il "combo damage".

### 2.2 Smite
- **Cos'è.** Il ramo Smite comprende Bai Qi, Cheok Jun-gyeong, Scipio Aemilianus, Sun Tzu (Prime), Tokugawa Ieyasu e William Wallace ([rokstats](https://app.rokstats.online/talents/smite)). Anche Liu Che e Ivar infliggono smite.
- **Regola chiave:** *"Smite damage uses normal damage bonuses rather than skill damage bonuses"* (skill di Bai Qi, KB da [riseofkingdomsguides](https://riseofkingdomsguides.com/talent-tree/bai-qi/)). Il [handbook su Liu Che (09/09/2026)](https://riseofkingdomshandbook.com/guides/riseofkingdoms-liu-che-guide) lo conferma: *"More damage" e "more skill damage" non sono acquisti intercambiabili.*
- **Formazione.** **Pincer** dà +10% smite, portato a **+12%** con il "Pincer II Update" di agosto 2026 ([changelog Davor's Toolkit](https://codexhelper.com/tools/davor_toolkit/)). Nuove iscrizioni:
  - Legendary: Dominate, Cleaver, Bulwark, Tidebreaker.
  - Rare: Bludgeon, Charge, Bolstered, Vigor.

  Ldshop: *"Pincer is essential for Smite-focused infantry setups"*.
- **Conflitto:** le pagine build allclash indicano **Wedge** per Sun Tzu Prime, Bai Qi e Liu Che (i dettagli sono nella parte PRO). Il JSON usa Pincer come predefinita e Wedge come alternativa.

### 2.3 Pierce
- **Cos'è.** Debuff a stack di **Alp Arslan**:
  - Heroic Lion attiva Lionsoul per 10 s e applica 1 stack ogni 3 s, fino a 3.
  - Ogni stack infligge danno extra al secondo (DF 100).
  - Nei primi 10 s di scontro gli attacchi base hanno il 50% di probabilità di applicare uno stack.

  Fonte: KB da [riseofkingdomsguides, 01/07/2026](https://riseofkingdomsguides.com/talent-tree/alp-arslan/).
- **Sinergia.** Parthian Shot ha un DF pari a *numero di debuff × 100* (massimo 1000). Two-Headed Eagle diffonde i debuff su truppe vicine. Per questo serve un primario che applichi molti debuff, come Hermann Prime ([ldshop](https://www.ldshop.gg/blog/rise-of-kingdoms/best-commander-pairings.html): *"Pierce-based pressure"*).
- **Da non confondere:** "Iron Pierces Bronze" di Qin Shi Huang non è Pierce. Converte 100 rage in danno diretto.

### 2.4 True damage
- **Sun Tzu Prime, Military Sage:** il 20% del danno smite (30% con l'expertise) diventa **true damage fisso** su fino a 2 truppe vicine, 1 volta al secondo, e dà 20 rage per ogni bersaglio colpito. Inoltre la skill costa solo **900 rage** (KB da [riseofkingdomsguides, 27/04/2026](https://riseofkingdomsguides.com/talent-tree/sun-tzu-prime/)).
- Allclash: *"fixed true damage... will directly counter everything the current meta commanders use defensively"*.
- **Lacuna:** nessuna fonte spiega formalmente come il true damage interagisce con difese e riduzioni.
- **In pratica:** l'effetto scatta solo sui colpi smite durante la finestra attiva. La marcia deve restare in contatto e non inseguire ([handbook Sun Tzu Prime](https://riseofkingdomshandbook.com/guides/riseofkingdoms-sun-tzu-prime-guide)).

### 2.5 Prime commanders
- **Cosa sono.** Leggendari **separati**, non potenziamenti: le sculture dell'epico non valgono per il Prime ([handbook – Prime](https://riseofkingdomshandbook.com/guides/riseofkingdoms-prime-commanders-guide)).
- **Rating allclash (09/2026):**

  | Prime | Rating |
  |---|---|
  | Sun Tzu Prime | S+ |
  | Hermann Prime | A |
  | Ragnar Prime | A |
  | Scipio Prime | B+ (niche) |
  | Boudica Prime | B+ |
  | Belisarius Prime | B+ |
  | Joan Prime | B |

- In SoC *"Prime commanders matter a lot"* ([ldshop tier KvK, 24/07/2026](https://www.ldshop.gg/blog/rise-of-kingdoms/kvk-tier-list.html)).
- Prima di prendere un Prime, scegli la marcia completa: partner, equipaggiamento e sculture.

### 2.6 Crystal Tech (Season of Conquest)
- **Come funziona.** La Crystal Mine produce cristalli, il Crystal Research Center esegue le ricerche. È una tecnologia stagionale che non sostituisce l'Accademia ([handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-crystal-technology-guide)).
- **Effetto sul meta:** alza attacco, difesa e salute di tutti, quindi *"skill damage and burst output start to matter far more than raw durability"* ([ldshop](https://www.ldshop.gg/blog/rise-of-kingdoms/kvk-tier-list.html)).
- **Nodi utili per l'attacco** (dal [simulatore community](https://rok-technology-simulator.netlify.app/); verificare in gioco):

  | Nodo | Effetto |
  |---|---|
  | Quenched Blades / Improved Bows / Mounted Combat Techniques | attacco del tipo di truppa +5% (I), +7.5% (II) |
  | Starmetal | difesa +15% |
  | Iron Infantry / Archer's Focus / Rider's Resilience | salute +15% |
  | Swift Marching / Fleet of Foot / Swift Steeds | velocità +5% / +10% / +15% |
  | Call To Arms I/II | capacità +15% / +35% |
  | Leadership I/II | capacità rally +15% / +35% |
  | Special Concoctions I/II | costo cure −15% / −25% |
  | Emergency Support | ospedale +30% |
  | Expanded Formations I/II | +1 marcia ciascuno |
  | Expert per tipo di truppa | danno e riduzione +10% |
  | Surprise Strike | +10% danno contro garrison e armate radunate ([riseofkingdomsguides](https://riseofkingdomsguides.com/season-of-conquest-crystal-tech-changes-in-rise-of-kingdoms/)) |
  | Runecraft | 2 rune al giorno |
  | *Rapid Retreat* | legato a 200 gemme: **il bot non lo usa mai** |

- **Metodo** ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-crystal-technology-guide)):
  - Pianifica a ritroso partendo dal primo scontro importante.
  - Rientro dell'investimento = costo C diviso cristalli al giorno D.
  - Da F2P concentrati su 1-2 marce che riesci a curare.
  - Non copiare l'albero di un whale.

### 2.7 Wedge II e formazioni 2026
- **Wedge II** arriva con l'update **1.1.06 "Battle Resurgent"** (24/03/2026): base 12% skill damage e nuove iscrizioni:
  - Legendary: Advantage Advanced, Indomitable, Maneuver at Ease, Horseback Action.
  - Rare: Fury, Soar, Ballista, Divine Staff.
- **Da giugno 2026** Wedge e Wedge II sono **una sola formazione Wedge al 12%** con iscrizioni combinabili ([Davor's Toolkit](https://codexhelper.com/tools/davor_toolkit/); KB da post Facebook ufficiale).
- **Pincer** passa al 12% smite (agosto 2026). **Delta** dà +10% combo, **Arch** +5% danno normale, **Hollow Square** −2% danno subito, **Staggered** +15% di velocità verso rally e garrison.
- L'update 1.1.11 (27/08/2026) ha corretto solo la descrizione di un'iscrizione Pincer ([ldshop](https://www.ldshop.gg/blog/rise-of-kingdoms/anniversary-special.html)).
- **Regola pratica:** skill → Wedge, smite → Pincer, combo → Delta.

---

## 3. Tattiche: massimo danno, perdite minime

### 3.1 Counter e composizione ([handbook – Counters, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-troop-types-and-counters))
- Fanteria batte cavalleria, cavalleria batte arcieri, arcieri battono fanteria. L'assedio non entra nel triangolo: serve per strutture e raccolta.
- Una fanteria davanti agli arcieri ne allunga molto la vita.
- *"Do not fight uphill"*: se sei contrato e lo scontro è opzionale, non accettarlo.
- **Nessuna fonte quantifica il bonus di counter.**

### 3.2 Swarm e focus fire
- Lo swarm (più marce sullo stesso bersaglio) serve a **finire un bersaglio indebolito** o a **supportare un rally**. I rischi sono danno ad area e contrattacco. Un errore tipico è fare *"Swarming an area-damage garrison"* ([heaven-guardian – City attack, 05/08/2026](https://heaven-guardian.com/rok-conquer-cities-flags-attack-guide-tips/)).
- Commander anti-swarm da evitare: YSG (AoE circolare), Ivar, Tariq, Pakal II, Belisarius Prime ([allclash tier](https://www.allclash.com/best-commanders-tier-list-in-rise-of-kingdoms-with-talents/)). Garrison anti-swarm: Hayam + Heraclius, Cyrus + Ragnar, Gorgo + Ragnar ([ldshop difesa](https://www.ldshop.gg/blog/rise-of-kingdoms/kvk-defense-guide.html)).
- Colpisci **un bersaglio alla volta** ([handbook Osiris](https://riseofkingdomshandbook.com/guides/riseofkingdoms-ark-of-osiris-guide)). Il focus fire riduce anche il danno da contrattacco ([bluestacks, 2024](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-combat-guide-en.html)).

### 3.3 Velocità, kiting e inseguimenti
- La velocità di marcia dipende dalla truppa più lenta, dai talenti e dal terreno ([handbook – Mechanics](https://riseofkingdomshandbook.com/guides/riseofkingdoms-game-mechanics-hub)).
- Allclash: il campo aperto *"is about being quick"*. A YSG serve march speed per *"catch other armies"* ([YSG](https://www.allclash.com/best-yi-seong-gye-ysg-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/), [Zhuge](https://www.allclash.com/best-zhuge-liang-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/)).
- Fonti di velocità: talenti Mobility, set Windswept, tecnologia, VIP, rune, reliquie, armamenti ([heaven-guardian – March speed, 04/08/2026](https://heaven-guardian.com/rise-of-kingdoms-max-cavalry-march-speed-guide/)).
- Con gli arcieri resta un passo dietro la prima linea e ritirati prima che la cavalleria ti tagli la strada ([handbook Hermann Prime](https://riseofkingdomshandbook.com/guides/riseofkingdoms-hermann-prime-guide)).
- **Non inseguire**, né dentro la "palla" nemica né oltre il supporto alleato ([handbook Liu Che](https://riseofkingdomshandbook.com/guides/riseofkingdoms-liu-che-guide), [Sun Tzu Prime](https://riseofkingdomshandbook.com/guides/riseofkingdoms-sun-tzu-prime-guide)).
- Non uscire e rientrare di continuo per riattivare effetti "all'ingresso": QSH ha un cooldown di 60 s ([handbook QSH](https://riseofkingdomshandbook.com/guides/riseofkingdoms-qin-shi-huang-guide)).
- **Lacuna:** nessuna fonte 2026 descrive il kiting come tecnica con numeri e tempi precisi.

### 3.4 Quando ingaggiare e quando ritirarsi
- **Ingaggia se:**
  - hai marce alleate accanto;
  - il bersaglio è raggiungibile e approvato;
  - hai uno scout recente;
  - l'ospedale ha spazio e hai risorse per curare;
  - hai una via di ritirata

  ([handbook Zhuge](https://riseofkingdomshandbook.com/guides/riseofkingdoms-zhuge-liang-guide), [heaven-guardian](https://heaven-guardian.com/rok-conquer-cities-flags-attack-guide-tips/)).
- **Ritirati se:**
  - più nemici si girano su di te;
  - la via di casa si sta chiudendo;
  - ospedale, risorse o vie sicure stanno finendo;
  - lo scambio diventa negativo o arrivano rinforzi schiaccianti;
  - il difensore cambia garrison in un counter

  ([handbook – Hospital](https://riseofkingdomshandbook.com/guides/riseofkingdoms-healing-hospital-guide), heaven-guardian). Non restare con un'armata quasi vuota solo per attivare effetti "a poche truppe" (handbook, Bai Qi).
- **Disciplina:** resta con il gruppo. Nella prima settimana di KvK niente scontri da solo ([handbook KvK1](https://riseofkingdomshandbook.com/guides/riseofkingdoms-kvk-1-guide), [KvK2](https://riseofkingdomshandbook.com/guides/riseofkingdoms-kvk-2-guide)).
- **Soglie numeriche:** nessuna fonte le fornisce. Nel JSON sono parametri che l'utente deve configurare.

### 3.5 Territorio alleato
- Attaccare qualcuno dentro il suo territorio significa combattere contro tutta la sua alleanza. Per attaccare passi, luoghi sacri e flag serve che il tuo territorio sia adiacente ([handbook – Territory](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-territory-flags), [riseofkingdomsguides – Attacking](https://riseofkingdomsguides.com/rise-of-kingdoms-attacking-cities-and-flags-guide/)).
- Non teletrasportarti da solo in una zona contesa ([handbook – Teleport](https://riseofkingdomshandbook.com/guides/riseofkingdoms-teleport-guide)).
- Subutai ha combo extra quando combatte **fuori** dal territorio d'alleanza (KB).
- **Lacuna:** nessuna fonte parla di un bonus di combattimento dentro il territorio.

### 3.6 Feriti e morti
- **Tre stati:**
  - i feriti leggeri si recuperano quando la marcia rientra;
  - i feriti gravi vanno in ospedale;
  - i morti sono persi.

  Se l'ospedale è pieno, l'eccedenza muore ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-healing-hospital-guide), [riseofkingdomsguides](https://riseofkingdomsguides.com/hospital/)).
- **Per tipo di bersaglio:**

  | Bersaglio | Cosa succede alle truppe |
  |---|---|
  | Città, flag e forti d'alleanza | *"some of your troops will die and some will go to the hospital"* |
  | Fortezze d'alleanza | *"all your troops will die"* |
  | Flag | *"only a portion"* muore |
  | Shrine | metà dei feriti gravi muore |
  | Lost Temple | tutti i feriti gravi muoiono |
  | Altar | nessun morto |
  | Ark of Osiris | solo feriti, curati con speedup |
  | Canyon | truppe simulate, nessuna perdita |

  Fonti: [riseofkingdomsguides – Attacking](https://riseofkingdomsguides.com/rise-of-kingdoms-attacking-cities-and-flags-guide/); KB da theriagames per i luoghi sacri; handbook per Ark e Canyon.
- **Durante un rally nemico** non puoi curare finché il rally non finisce ([riseofkingdomsguides](https://riseofkingdomsguides.com/hospital/)).
- **T4 o T5 (KB, [packsify](https://www.packsify.com/blogs/rise-of-kingdoms-t5-troops-guide)):** curare 100.000 T5 costa circa 144M di oro, contro circa 7,2M per 100.000 T4. Usa i T4 in campo aperto e i T5 in rally e garrison.

### 3.7 Ospedale
- Fino a 4 ospedali, da 3.000 (Lv1) a 75.000 (Lv25) posti ciascuno. Se l'alleanza è attiva cura a lotti piccoli, per esempio 1.000 truppe ([riseofkingdomsguides](https://riseofkingdomsguides.com/hospital/)).
- Prima di uno scontro importante: libera spazio, tieni da parte le risorse (gli speedup non pagano le risorse) e scegli dove ritirarti.
- Stima le perdite su un report tipico e moltiplicala per gli scontri che puoi permetterti ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-healing-hospital-guide)).

### 3.8 Rune
- Le rune compaiono vicino ai luoghi sacri e si prendono uccidendo i guardiani. Esistono in 5 tier; le più forti sono vicino al Lost Temple. Vanno a chi arriva per primo, quindi serve una marcia veloce ([handbook – Runes](https://riseofkingdomshandbook.com/guides/riseofkingdoms-map-zones-runes-guide)).
- Le rune da combattimento danno Attack, Defense, Health o March Speed e durano circa 1 ora. **Una sola runa può essere attiva.** Per tier: bianco ~3%, verde ~7%, blu ~10%, viola ~15%, arancio ~20% ([heaven-guardian – Runes, 03/08/2026](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/)).
- Prendile subito prima dello scontro. Si sommano ai titoli e ai buff d'alleanza.
- I guardiani compaiono alle 00:00 e alle 12:00 UTC e restano per 11 ore (KB).

### 3.9 Scouting prima di attaccare
- Scouta **prima di ogni attacco**: la potenza non dice né il tier né le skill né i rinforzi ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-game-mechanics-hub)).
- Nel report controlla ([heaven-guardian](https://heaven-guardian.com/rok-conquer-cities-flags-attack-guide-tips/)):
  - comandanti in garrison;
  - numero e tier delle truppe;
  - Watchtower e Wall;
  - risorse grezze (gli oggetti in inventario non si saccheggiano);
  - alleanza e vicini;
  - completezza del report.
- Non fidarti di un report vecchio.

---

## 4. Rally, Sunset Canyon, Ark of Osiris

### 4.1 Rally
- **Cos'è.** Un attacco organizzato da un giocatore. I **comandanti e i talenti del leader** valgono per tutto il rally. Attaccare da soli bersagli difesi regala kill point al nemico ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-game-mechanics-hub)).
- **Per guidare servono** comandanti forti, tecnologia delle truppe alta, equipaggiamento e armamenti ottimizzati, buff, supporto dell'alleanza e truppe per combattere più volte. Investi in comandanti da rally solo se guidi davvero rally ([heaven-guardian pairings](https://heaven-guardian.com/rise-of-kingdoms-best-commander-pairings/)). Riseofkingdomsguides: *"Do not start a rally if you do not have great rally commanders"* ([Attacking](https://riseofkingdomsguides.com/rise-of-kingdoms-attacking-cities-and-flags-guide/)).
- **Checklist del capitano** ([heaven-guardian](https://heaven-guardian.com/rok-conquer-cities-flags-attack-guide-tips/)):
  1. scout recente;
  2. coppia adatta al bersaglio;
  3. skill e livelli;
  4. set da combattimento;
  5. formazione e armamenti;
  6. tipo di truppa;
  7. capacità;
  8. timer;
  9. condizione di ritirata.

  Prima del lancio ripulisci le marce nemiche nelle vicinanze.
- **Per chi si unisce:**
  - manda solo il tipo e il tier richiesti;
  - niente assedio se non viene chiesto;
  - entra prima del timer;
  - tieni una marcia libera per il supporto;
  - usa la **Staggered Formation** (+15% di velocità verso il rally);
  - la capacità massima non è la quantità da mandare ([handbook – Capacity](https://riseofkingdomshandbook.com/guides/riseofkingdoms-troop-capacity-march-queues-guide)).
- **Quando fermarsi:**
  - arrivano rinforzi schiaccianti;
  - il difensore passa a una garrison counter;
  - gli scambi diventano negativi;
  - gli ospedali sono al limite;
  - il bersaglio si scuda o si sposta;
  - parte un contro-rally sul capitano;
  - la leadership annulla.
- **Bersagli:**
  - Una città con la Wall a 0 viene riposizionata a caso.
  - Si saccheggiano solo le risorse grezze.
  - Riseofkingdomsguides consiglia l'assedio contro le città; heaven-guardian e il handbook lo sconsigliano se non viene chiesto (conflitto).
- **Crystal Tech per i rally:** Leadership I/II, Larger Camps (+100% rinforzi), Surprise Strike.

### 4.2 Sunset Canyon (lineup 2026)
- **Regole:**
  - le truppe sono simulate, quindi non perdi nulla;
  - hai 5 tentativi gratuiti al giorno e la stagione dura 7 giorni;
  - schieri fino a 5 armate di T3;
  - contano gear, skill e talenti (solo del primario);
  - ogni armata attacca prima l'avversario di fronte;
  - la prima fila viene colpita per prima;
  - vince chi elimina tutti i nemici, e in caso di parità chi ha più truppe

  ([handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-sunset-canyon-guide), [riseofkingdomsguides](https://riseofkingdomsguides.com/rise-of-kingdoms-sunset-canyon-guide/), [allclash Canyon, agg. 23/08/2026](https://www.allclash.com/sunset-canyon-guide-for-rise-of-kingdoms-tactics-commanders-to-use/)).
- **Conflitto:** per riseofkingdomsguides tutti hanno lo stesso numero di T3. Per il handbook il tier è uguale ma la capacità cambia con lo sviluppo dei comandanti.
- **Schieramento** (allclash):
  - Tank in prima linea: 1-2 con 3 armate, 2 con 4, 2-3 con 5.
  - AoE e supporto dietro, con YSG al centro.
  - Il nuker va dietro il tank che affronta il tank più forte nemico.
  - Cambia una cosa alla volta e guarda il replay (handbook).
- **Lineup F2P del handbook:**

  | Posizione | Coppia |
  |---|---|
  | Fronte | Scipio (epico) → Sun Tzu |
  | Fronte adiacente | Pelagius → Baibars |
  | Dietro | Aethelflaed → Joan of Arc |
  | Dietro | Kusunoki → Imhotep |
  | Fianco | Eulji → Osman |

  Riseofkingdomsguides indica Sun Tzu + Joan of Arc come "top tier pairing".
- **Fascia alta 2026** (solo rating, nessuna lineup testata):
  - Canyon S+: Alp Arslan, Sun Tzu Prime, Ragnar Prime, Shajar al-Durr (*"if you want to get anything done in canyon... you will need her"*), Constantine.
  - Coppia consigliata: Alp Arslan + Shajar al-Durr.

  Fonte: [allclash tier](https://www.allclash.com/best-commanders-tier-list-in-rise-of-kingdoms-with-talents/).
- **Ticket:** usa prima i tentativi gratuiti. I ticket extra conviene tenerli per gli ultimi giorni, dopo aver verificato la scadenza. Non spendere sculture universali per una lineup Canyon.

### 4.3 Ark of Osiris (basi)
- **Formato:**
  - 30 contro 30;
  - Municipio 16+;
  - alleanza con più di 10 flag e nella top 20 del regno;
  - partite divise in campi Golden e Silver

  ([handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-ark-of-osiris-guide)).
- **Punti:**
  - prima occupazione e mantenimento degli edifici;
  - consegna dell'Ark a un edificio controllato dalla tua alleanza (vale di più a ogni respawn);
  - uccisioni, rifornimenti, catture.

  La prima occupazione di un Obelisk dà 8 teleport d'alleanza ([heaven-guardian, 04/08/2026](https://heaven-guardian.com/ark-of-osiris-guide-dominate-rise-of-kingdoms/)).
- **Truppe:** vengono ferite, non uccise. Il costo sono gli speedup di cura (conflitto con un dato KB che parla di "cura gratuita").
- **Ruoli:**
  - prima marcia sull'Obelisk (per riseofkingdomsguides cavalleria T1, la più veloce);
  - carrier veloce e resistente;
  - scorta;
  - rally leader;
  - garrison captain;
  - support;
  - gatherer.

  I giocatori più deboli riempiono rally e garrison, raccolgono e scoutano.
- **Strategia:**
  - tieni le strutture fin dall'inizio;
  - focus fire e niente inseguimenti;
  - non prendere l'Ark senza scorta o senza un edificio sicuro dove consegnarla;
  - in vantaggio proteggi il punteggio continuo, in svantaggio concentrati su una struttura di valore.

  Preparazione: ospedale vuoto, almeno +25% di espansione dell'armata, massimo 3 marce ([riseofkingdomsguides](https://riseofkingdomsguides.com/ark-of-osiris-guide-and-strategy/)).

---

## 5. Regole per il bot (sintesi; testo completo in `bot_rules` del JSON)

| id | Quando | Allora | Conferma |
|---|---|---|---|
| att-01 | Qualsiasi attacco a un giocatore (città, marcia, raccoglitore, struttura) | Fermati e chiedi conferma. Mostra bersaglio, scout, marcia, spazio in ospedale, rischio di morti | **SÌ** |
| att-02 | Avviare un rally o unirsi a uno | Chiedi conferma. Poi manda solo truppe e tier richiesti, niente assedio, una marcia libera | **SÌ** |
| att-03 | L'azione costa gemme | **Vietato**, nessuna conferma lo sblocca | — (allowed = false) |
| att-04 | Serve informazione su un giocatore | Proponi uno scout (è visibile al bersaglio). Senza scout recente non proporre l'attacco | **SÌ** |
| att-05 | Il bersaglio ha un tipo di truppa prevalente | Proponi il counter. Se sei contrato e lo scontro è opzionale, sconsiglialo | no |
| att-06/07/08 | Scelta di coppia, formazione e armamenti | Prima coppia posseduta in `meta_pairs`. Skill → Wedge, smite → Pincer, combo → Delta. Equipaggiamento sul primario | no |
| att-09 | KvK con T4 e T5 | T4 in campo aperto, T5 nei rally | no |
| att-10 | Prima di combattere | Se l'ospedale non ha spazio per i feriti gravi previsti, non attaccare | no |
| att-11 | Cure | Lotti con aiuto d'alleanza. Speedup solo se già in inventario, con conferma. Mai gemme | SÌ se si usano speedup |
| att-12 | Luogo sacro, fortezza o flag con morti | Avvisa del rischio di morti permanenti | **SÌ** |
| att-13 | Rally nemico in arrivo | Nessun attacco con le truppe di casa; passa alla difesa | no |
| att-14 | Ingaggio in campo aperto | Ingaggia accanto agli alleati; con gli arcieri resta un passo indietro | **SÌ** (basta la conferma di att-01, una per scontro) |
| att-15/16/17 | Durante lo scontro | Ritirati se ti focalizzano o la via si chiude. Non inseguire. Fermati se lo scambio è negativo | no (ritirarsi non richiede conferma) |
| att-18 | Swarm | Solo per finire bersagli o supportare un rally, mai su AoE o anti-swarm | **SÌ** |
| att-19 | Bersaglio nel territorio di un'alleanza forte | Avvisa | **SÌ** |
| att-20 | Settimana 1 di KvK | Niente scontri in solitaria | no |
| att-21 | Runa di combattimento e scontro entro un'ora | Prendi la runa subito prima | no |
| att-22/23/24 | Guidare o unirsi a un rally; condizioni di stop | Checklist capitano, Staggered, stop | **SÌ** / no per lo stop |
| att-25/26 | Sunset Canyon | Conferma (anche una volta sola per i 5 tentativi del giorno); tank davanti, AoE dietro | **SÌ** / no |
| att-27 | Ark of Osiris | Conferma all'inizio per il ruolo, poi segui le chiamate | **SÌ** |
| att-28 | Crystal Tech | Ramo del tuo tipo di truppa, capacità, cure. Mai Rapid Retreat | no |
| att-29 | Teleport per attaccare | Solo oggetti in inventario, con conferma, mai gemme | **SÌ** |
| att-30 | DKP | Segui la formula del regno, niente farming automatico di kill | no |

---

## Lacune principali
1. Nessuna fonte dà il bonus numerico dei counter.
2. Non c'è una definizione formale del true damage.
3. Nessuna fonte descrive il kiting con numeri.
4. Non ci sono soglie numeriche per la ritirata.
5. Manca una lineup Canyon "end-game" completa per il 2026.
6. Armamenti, alberi dei talenti e guanti/stivali/accessori di allclash sono nella parte PRO o solo in immagini.
7. L'albero Crystal Tech viene da un simulatore community senza data.
8. Non si sa se "Pincer II" sia una formazione separata.
9. Mancano la capacità dei rally per livello del Castello e le percentuali di morte per l'attaccante.

## Fonti non raggiunte
- topuplist (403).
- Via curl: ldshop (403), riseofkingdomsguides (verifica anti-bot) e heaven-guardian (reset di connessione). Tutte e tre sono state lette tramite WebFetch.
- Slug non esistenti: heaven-guardian `rise-of-kingdoms-sunset-canyon-guide` e `crystal-tech-guide`, ldshop `sunset-canyon-guide.html` e `crystal-tech-guide.html`.
- Sitemap e categoria allclash (403).
- rok.guide e fandom: non ritentati, come indicato.
