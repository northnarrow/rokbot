# Talenti dei comandanti — Rise of Kingdoms

Guida del consigliere militare, dati raccolti il **2026-09-28**. Nomi tecnici in inglese (come nel gioco in inglese), testo in italiano. I numeri tra parentesi quadre rimandano all'elenco delle fonti in fondo. Dati macchina: `data/fragments/talenti.json`.

## 1. In breve

- Un comandante a livello 60 ha **74 punti talento** [1] [2] [3].
- Si ottiene **1 punto per livello** più punti bonus alla promozione a 5 e 6 stelle [4]; la promozione a 6 stelle vale +10 [5] (fonte non ufficiale), quindi a 5 stelle restano +5 (valore derivato).
- **Solo il comandante primario usa i talenti**: i punti del secondario non hanno effetto [1] [2] [4] [6].
- Un talento si sblocca solo con **tutti** i talenti collegati sotto di lui al massimo [3] [7] [8].
- Ogni albero vale 48-50 punti: con 74 punti si completa un albero e circa metà di un altro.
- Alberi: 15 originali completi [3] + **Engineering** (2023), **Smite** (2024) e **Combo** (2025) [9]. Di Combo sono noti 4 talenti ufficiali [10]; di Engineering un solo nome (Forbearance) [11]; di Smite **nessun** nome o effetto nelle fonti raggiungibili.
- Consiglio operativo per il bot: i raccoglitori e i cacciatori di barbari vanno messi come **primari** (i loro talenti Gathering/Peacekeeping non contano da secondari); per leggere la build di un comandante dal telefono basta confrontare i punti per albero con le tabelle della sezione 3.

## 2. Regole dei punti talento

**Punti massimi.** 74 a livello 60 [1] [2] [3]. Livello massimo 60 per tutte le rarità (6 stelle) [1] [2] [12].

**Da dove arrivano i punti.** 1 punto talento per ogni livello guadagnato (dal livello 2 in poi) + punti bonus alla promozione a 5 e 6 stelle. [4]. 6 stelle = +10 (commento Reddit 2024, non ufficiale). 5 stelle = +5 è DERIVATO per differenza: 74 - 59 (livelli 2-60) - 10 = 5. La fonte fandom conferma solo che 5 e 6 stelle danno punti extra. [4] [5]

Tabella livello → punti (DERIVATA, vedi nota):

| Livello | Punti |
|---|---|
| 10 | 9 |
| 20 | 19 |
| 27 | 26 |
| 30 | 29 |
| 37 | 36 |
| 40 (4 stelle) | 39 |
| 40 (dopo 5 stelle) | 44 |
| 50 (5 stelle) | 54 |
| 50 (dopo 6 stelle) | 64 |
| 60 | 74 |

Tabella DERIVATA (livello-1 punti + bonus stelle). Coerente con le tappe della build di Cleopatra di allclash (lv10 = Gold+Stone Mastery = 9 punti; lv27 = The More The Better = 26; lv37 = Superior Tools = 36; lv40 = Modified Axle = 39) e con 'livello 37 per maxare Superior Tools' (riseofkingdomsguides). [8] [13] [4] [5]

**Stelle e livelli.** gamesguideinfo: '2 Stars require XP level 10, 3 Stars XP 20, 4 Stars XP 30, 5 Stars XP 40'. 6 stelle a lv 50: dal commento Reddit ('6th star, meaning level 50'). Le stelle si possono anche anticipare (rok.guide: 4 stelle già a livello 10). [14] [5]

**Prerequisiti.** Un talento si sblocca solo quando TUTTI i talenti a cui è collegato 'da sotto' sono al massimo (es. Superior Tools richiede The More The Better 3/3 e Armed Convoy 3/3). Il campo cost_to_unlock_with_prereqs di ogni talento = punti minimi totali nell'albero per poterlo prendere al massimo. [3] [7] [8]

**Primario e secondario.** Solo i talenti del comandante PRIMARIO hanno effetto; il secondario contribuisce solo con le abilità. Conseguenza pratica: un raccoglitore/peacekeeper deve essere primario; il secondario può avere punti talento spesi in qualunque modo. [1] [2] [4] [6]

**Reset dei talenti.** Oggetto 'Talent Reset' (azzera tutti i punti del comandante): da Mysterious Merchant e Shop (fandom 2022); acquistabile anche nel negozio dell'alleanza (post Reddit 2022: '300k alliance credits'). Reset con gemme: 1000 gemme secondo un post Reddit del 2022 (non verificato su fonte ufficiale). Esistono preset dell'albero talenti; secondo un PSA Reddit del 2019 rifare un preset richiede lo scroll di reset e resettare con un preset selezionato azzera il preset e non l'albero attivo. Resettare è costoso: non spendere punti se non si è sicuri del ruolo del comandante (fandom). Nessuna fonte ufficiale sul costo esatto. [15] [4] [16] [17] [18]

**Novità dalle patch che riguardano i talenti:**

- 1.0.78 (2024-01-09): Condizioni di attivazione di alcuni talenti (e accessori/iscrizioni) modificate: si attivano sia con attacchi normali sia con attacchi a distanza. [19]
- 1.0.81 (2024-04-16): Last Stand (albero Attack): descrizione aggiornata con ricarica di 2 secondi, effetto invariato. [20]
- 1.0.83 (2024-06-21): Commander Revamp: per i comandanti 'revamped' alla guida di una truppa, i bonus di talenti/equipaggiamento/formazioni ecc. vengono convertiti in bonus per le unità 'shifter' in base ai tag dei talenti originali (es. tag Infantry -> bonus fanteria convertiti). Solo comandanti revamped o con il talento Engineering usano l'abilità attiva con truppe skirmisher/artillery. [21]
- 1.0.88 (2024-11-25): Nell'interfaccia talenti si vede la percentuale di governatori che ha scelto ogni talento (le percentuali verdi negli screenshot). [22]
- 1.0.90 (2025-01-05): Arrivo di King Arthur (Cavalry/Versatility/Combo) e dell'albero Combo. [23] [10]

**Punti per completare ogni albero:** Infantry 50, Cavalry 50, Archer 48, Leadership 50, Integration 50, Attack 48, Defense 48, Skill 48, Support 48, Mobility 48, Garrison 48, Peacekeeping 48, Gathering 48, Conquering 48, Versatility 48.

## 3. Build standard per ruolo

I talenti principali e l'ordine vengono dalle guide citate; i punti dei nodi statistica attraversati (percorso) sono calcolati dal grafo dell'albero con la regola dei prerequisiti. "Cumul." = punti totali spesi dopo quel passo: indica anche a che livello si arriva al talento (livello ≈ punti + 1 fino al 40).

### Raccolta

Esempio: Cleopatra VII (Integration/Gathering/Support); schema Gathering valido per ogni raccoglitore. Alberi: Gathering, Integration, Support. Punti per albero: Gathering 39, Integration 10, Support 15; totale **64**/74. Fonti: [24] [8] [13] [3]

| # | Albero | Talento | Punti | + percorso | Cumul. | Nota |
|---|---|---|---|---|---|---|
| 1 | Gathering | Gathering Mastery (Gold) | 3/3 | 3 | 6 | lv10 (Cleopatra); in generale prima la Mastery della risorsa principale del comandante |
| 2 | Gathering | Gathering Mastery (Stone) | 3/3 | 0 | 9 | lv10: risorsa migliore di Cleopatra |
| 3 | Gathering | Gathering Mastery (Food) | 3/3 | 2 | 14 | lv20 |
| 4 | Gathering | Gathering Mastery (Wood) | 3/3 | 0 | 17 | lv20 |
| 5 | Gathering | March Speed (All Troops) | 2/2 | 0 | 19 | lv20: 'March Speed (All Troops) in the middle' |
| 6 | Gathering | The More The Better | 3/3 | 4 | 26 | lv27: +6% risorse a fine raccolta |
| 7 | Gathering | Armed Convoy | 3/3 | 2 | 31 | lv37: necessario per Superior Tools |
| 8 | Gathering | Superior Tools | 5/5 | 0 | 36 | lv37: +25% velocità di raccolta |
| 9 | Gathering | Modified Axle | 3/3 | 0 | 39 | lv40: +30% velocità delle unità d'assedio (raccogliere solo con assedio) |
| 10 | Integration | Charge | 3/3 | 4 | 46 | oltre lv40 (Cleopatra): per scappare |
| 11 | Integration | March Speed (All Troops) | 3/3 | 0 | 49 | 'there's a march speed talent behind that' |
| 12 | Support | Hasty Departure | 3/3 | 4 | 56 | +60% velocità per 10 s partendo da una struttura (anche nodi risorsa) |
| 13 | Support | March Speed (All Troops) | 2/2 | 6 | 64 | 'the talent node in front of [Rejuvenate] has also march speed' |

Effetto complessivo: Raccolta: +30% per risorsa (Mastery), +25% generale (Superior Tools), +6% risorse a fine raccolta, +30% velocità assedio, +9% velocità di marcia (albero Gathering) +9% (Integration), Hasty Departure +60% per 10 s; difesa in raccolta +15% (Armed Convoy).

Nota: Ordine e talenti principali dalla fonte; i punti dei nodi di percorso (prereq_path) sono calcolati dal grafo roktalents con la regola 'tutti i prerequisiti al massimo' (DERIVATO). Le tappe di livello (10/20/27/37/40) e i punti corrispondono esattamente a livello-1 punti. I 10 punti residui vanno 'in difesa o salute' (nessuna indicazione precisa: gap).

### Barbari / Peacekeeping

Esempio: Lohar (Integration/Peacekeeping/Support); varianti: Boudica, Aethelflaed, Minamoto, Belisarius. Alberi: Peacekeeping, Support. Punti per albero: Peacekeeping 43, Support 31; totale **74**/74. Fonti: [25] [3]

| # | Albero | Talento | Punti | + percorso | Cumul. | Nota |
|---|---|---|---|---|---|---|
| 1 | Peacekeeping | Insight | 3/3 | 4 | 7 | prima priorità: meno AP per attacco |
| 2 | Support | Rejuvenate | 3/3 | 15 | 25 | 150 ira a ogni abilità (anche del secondario) |
| 3 | Peacekeeping | Thoroughbreds | 3/3 | 8 | 36 | +9% velocità di marcia |
| 4 | Peacekeeping | Trophy Hunter | 3/3 | 0 | 39 | pacchi risorse extra dai barbari |
| 5 | Peacekeeping | Domination | 3/3 | 3 | 45 |  |
| 6 | Peacekeeping | Killer Instinct | 3/3 | 0 | 48 |  |
| 7 | Peacekeeping | Curing Chant | 5/5 | 8 | 61 | cura dopo ogni barbaro: si resta fuori senza tornare in città |
| 8 | Support | Elixir | 3/3 | 3 | 67 | +9% cure ricevute |
| 9 | Support | Loose Formation | 3/3 | 0 | 70 | -9% danno da abilità subito |
| 10 | Support | Counterattack | 3/3 | 1 | 74 |  |

Effetto complessivo: Barbari: -9 (o -9%) costo AP, +9% danno normale e +15% danno abilità contro barbari, +9% velocità, cura dopo ogni combattimento (Curing Chant 500), Rejuvenate 150 ira, +9% cure (Elixir).

Nota: Ordine e talenti principali dalla fonte; i punti dei nodi di percorso (prereq_path) sono calcolati dal grafo roktalents con la regola 'tutti i prerequisiti al massimo' (DERIVATO). Totale esatto 74 punti: conferma la regola dei prerequisiti. Nota: il riassunto WebFetch della pagina dal vivo attribuisce Curing Chant al Support Tree, ma nei dati roktalents/gamesguideinfo Curing Chant è nell'albero Peacekeeping.

- Variante **Boudica (Peacekeeping + Skill)**: Insight → Rejuvenate (Skill) → Trophy Hunter → Thoroughbreds → Domination → Killer Instinct → Feral Nature (Skill) → Naked Rage (ultimi 2 punti) [26]
- Variante **Minamoto forti barbari (Peacekeeping + Skill + Cavalry)**: Insight → Rejuvenate (con Burning Blood e All For One) → Feral Nature → resto Peacekeeping → velocità in Cavalry [27]

### Guarnigione (difesa città)

Esempio: Sun Tzu (Infantry/Garrison/Skill). Alberi: Garrison, Skill, Infantry. Punti per albero: Garrison 17, Skill 42, Infantry 14; totale **73**/74. Fonti: [28] [3]

| # | Albero | Talento | Punti | + percorso | Cumul. | Nota |
|---|---|---|---|---|---|---|
| 1 | Garrison | Nowhere To Turn | 3/3 | 7 | 10 | ira extra quando la città è attaccata |
| 2 | Garrison | Impregnable | 3/3 | 4 | 17 | -15% danno da abilità alla guarnigione; 'that's actually all the points you should spend in this tree' |
| 3 | Skill | Rejuvenate | 3/3 | 15 | 35 | con Burning Blood e All For One lungo il percorso |
| 4 | Skill | Feral Nature | 5/5 | 19 | 59 |  |
| 5 | Infantry | Undying Fury | 3/3 | 3 | 65 |  |
| 6 | Infantry | Call of the Pack | 3/3 | 2 | 70 |  |
| 7 | Infantry | Double-Headed Axe | 3/3 | 0 | 73 | ultimi punti |

Effetto complessivo: Guarnigione: ira extra (Nowhere To Turn 6), -15% danno abilità subito da comandante di guarnigione, motore d'ira Skill (Rejuvenate 60, Feral Nature 100, Burning Blood 9), +6% difesa sotto il 50% (Call of the Pack).

Nota: Ordine e talenti principali dalla fonte; i punti dei nodi di percorso (prereq_path) sono calcolati dal grafo roktalents con la regola 'tutti i prerequisiti al massimo' (DERIVATO). Totale 73: resta 1 punto libero. Varianti allclash: Richard I = Garrison 18 punti fino a King's Guard (City Guardian, Impenetrable Fortifications) + Infantry 13 + resto Defense; Charles Martel = Garrison 17 + Defense (Master Armorer, Burning Blood, Loose Formation, Medicinal Supplies, Balance, Testudo Formation) + Infantry (Undying Fury) — nel testo la somma dichiarata 17+47+13 supera 74 (incoerenza della fonte).

- Variante **Richard I garrison**: Garrison fino a King's Guard (18 punti: City Guardian, Impenetrable Fortifications, King's Guard) → Infantry (13 punti) → Defense (resto) [29]
- Variante **Charles Martel garrison**: Garrison (17 punti) → Defense: Master Armorer, Burning Blood, Loose Formation, Medicinal Supplies, Balance, Testudo Formation → Infantry: Undying Fury [30]

### Campo aperto - nuker (danno abilità)

Esempio: Sun Tzu (Infantry/Garrison/Skill) in campo aperto. Alberi: Skill, Infantry. Punti per albero: Skill 24, Infantry 45; totale **69**/74. Fonti: [28] [3]

| # | Albero | Talento | Punti | + percorso | Cumul. | Nota |
|---|---|---|---|---|---|---|
| 1 | Skill | Rejuvenate | 3/3 | 15 | 18 | 'without any hesitation' prima Rejuvenate (Burning Blood lungo il percorso) |
| 2 | Infantry | Snare of Thorns | 4/4 | 15 | 37 | rallenta i nemici; velocità e ira sul lato destro |
| 3 | Infantry | Elite Soldiers | 5/5 | 18 | 60 | minimo necessario per Elite Soldiers |
| 4 | Skill | Tactical Mastery | 3/3 | 0 | 63 | punti residui |
| 5 | Skill | Heraldic Shield | 3/3 | 0 | 66 | punti residui |
| 6 | Infantry | Strong of Body | 3/3 | 0 | 69 | punti residui |

Effetto complessivo: Nuker: motore d'ira (Rejuvenate +60 per abilità), Tactical Mastery +3% danno attivo, riduzioni danno abilità subito (Heraldic Shield 6%), fanteria: Elite Soldiers +2,5% att/dif/salute se solo fanteria, Snare of Thorns rallentamento 20%.

Nota: Ordine e talenti principali dalla fonte; i punti dei nodi di percorso (prereq_path) sono calcolati dal grafo roktalents con la regola 'tutti i prerequisiti al massimo' (DERIVATO). Totale 69: 5 punti non specificati dalla fonte. Variante Guan Yu 2023 (allclash): Skill Rejuvenate -> Feral Nature, Infantry fino a Strong of Body, Conquering Entrenched (con Moment of Triumph) = 71 punti derivati.

- Variante **Guan Yu 2023**: Rejuvenate → Feral Nature → Strong of Body (Infantry) → Moment of Triumph + Entrenched (Conquering) [31]

### Campo aperto - tank (fanteria)

Esempio: Richard I / Charles Martel (Infantry/Garrison/Defense). Alberi: Infantry, Defense. Punti per albero: Infantry 50, Defense 22; totale **72**/74. Fonti: [29] [30] [3]

| # | Albero | Talento | Punti | + percorso | Cumul. | Nota |
|---|---|---|---|---|---|---|
| 1 | Infantry | Fleet Of Foot | 3/3 | 8 | 11 | prima la velocità: obbligatoria in campo aperto |
| 2 | Defense | March Speed (All Troops) | 2/2 | 10 | 23 |  |
| 3 | Defense | Loose Formation | 3/3 | 7 | 33 | -9% danno da abilità subito |
| 4 | Infantry | Strong of Body | 3/3 | 7 | 43 | +6% salute fanteria |
| 5 | Infantry | Elite Soldiers | 5/5 | 22 | 70 | 'work your way through the Infantry tree to the top' |
| 6 | Infantry | Undying Fury | 3/3 | 0 | 70 | completamento albero Infantry |
| 7 | Infantry | Health (Infantry) | 1/1 | 0 | 71 | completamento albero Infantry |
| 8 | Infantry | Defense (Infantry) | 1/1 | 0 | 72 | completamento albero Infantry |

Effetto complessivo: Tank: Infantry completo (Elite Soldiers +2,5%, Hold The Line -20% danno, Strong of Body +6% salute, Iron Spear +9% vs cavalleria), Loose Formation -9% danno abilità, Master Armorer (difesa × stelle), velocità fanteria +6% (Fleet Of Foot) + nodi velocità.

Nota: Ordine e talenti principali dalla fonte; i punti dei nodi di percorso (prereq_path) sono calcolati dal grafo roktalents con la regola 'tutti i prerequisiti al massimo' (DERIVATO). Infantry completo (50) + Defense 22 = 72: 2 punti non specificati.

### Rally (capo rally)

Esempio: Julius Caesar (Leadership/Conquering/Attack). Alberi: Attack, Leadership. Punti per albero: Attack 24, Leadership 50; totale **74**/74. Fonti: [32] [3]

| # | Albero | Talento | Punti | + percorso | Cumul. | Nota |
|---|---|---|---|---|---|---|
| 1 | Attack | Lord of War | 3/3 | 4 | 7 |  |
| 2 | Attack | Burning Blood | 3/3 | 0 | 10 |  |
| 3 | Attack | Effortless | 3/3 | 5 | 18 |  |
| 4 | Leadership | Strategic Prowess | 4/4 | 16 | 38 |  |
| 5 | Leadership | Fresh Recruits | 3/3 | 2 | 43 | +3% capacità truppe |
| 6 | Leadership | Armored To The Teeth | 3/3 | 3 | 49 |  |
| 7 | Leadership | Armed To The Teeth | 3/3 | 0 | 52 |  |
| 8 | Leadership | Close Formation | 4/4 | 7 | 63 |  |
| 9 | Leadership | Name Of The King | 5/5 | 0 | 68 | +5% attacco del rally |
| 10 | Attack | Armored Joints | 3/3 | 3 | 74 | ultimi punti a Julius Caesar massimo |

Effetto complessivo: Rally: Name Of The King +5% attacco radunato, Fresh Recruits +3% truppe, +3%/-3% danno con 3 tipi di unità, Close Formation +12% attacco sotto il 50%, Strategic Prowess +20% difesa per 2 s dopo abilità, Effortless fino a +10% danno, Lord of War attacco × stelle.

Nota: Ordine e talenti principali dalla fonte; i punti dei nodi di percorso (prereq_path) sono calcolati dal grafo roktalents con la regola 'tutti i prerequisiti al massimo' (DERIVATO). Totale esatto 74. Varianti: rally città con Conquering (Entrenched -> Tear of Blessing -> Meteor Shower; Frederick I) o Skill+Leadership (Mehmed II: Rejuvenate -> Hidden Wrath -> Strategic Prowess -> Close Formation -> Name of the King).

- Variante **Mehmed II rally città**: Rejuvenate (Skill, con Burning Blood e All For One) → Hidden Wrath → Strategic Prowess → Close Formation → Name of the King → Armed/Armored to the Teeth → Tactical Mastery, Heraldic Shield (se restano punti) [33]
- Variante **Frederick I rally città**: Entrenched → Tear of Blessing → Meteor Shower (Conquering) → Rejuvenate (Skill) → Hidden Wrath, Healing Herbs, March Speed (Leadership) [34]

### Mobilità (velocità / caccia)

Esempio: Cao Cao (Cavalry/Peacekeeping/Mobility) - "the fastest build". Alberi: Mobility, Peacekeeping, Cavalry. Punti per albero: Mobility 48, Peacekeeping 18, Cavalry 7; totale **73**/74. Fonti: [35] [3]

| # | Albero | Talento | Punti | + percorso | Cumul. | Nota |
|---|---|---|---|---|---|---|
| 1 | Mobility | Hasty Departure | 3/3 | 7 | 10 | la fonte scrive 'Peacekeeping tree', ma Hasty Departure è nell'albero Mobility |
| 2 | Mobility | Lightning Charge | 3/3 | 1 | 14 |  |
| 3 | Peacekeeping | Thoroughbreds | 3/3 | 15 | 32 | +9% velocità |
| 4 | Cavalry | Charge | 3/3 | 4 | 39 | +30% velocità sotto il 50% |
| 5 | Mobility | Time Management | 5/5 | 25 | 69 | 'as fast as possible'; poi completare Mobility |
| 6 | Mobility | Swiftness | 3/3 | 0 | 72 | completamento Mobility |
| 7 | Mobility | Vortex | 3/3 | 0 | 72 | completamento Mobility |
| 8 | Mobility | Health (All Troops) | 1/1 | 0 | 73 | completamento Mobility |

Effetto complessivo: Velocità: Time Management +10% fuori combattimento (-10% in combattimento), Hasty Departure +60% per 10 s, Lightning Charge +6%, Thoroughbreds +9%, Swiftness +15% quando colpiti da abilità, Alacrity 30% resistenza ai rallentamenti, Triumphant March +15%.

Nota: Ordine e talenti principali dalla fonte; i punti dei nodi di percorso (prereq_path) sono calcolati dal grafo roktalents con la regola 'tutti i prerequisiti al massimo' (DERIVATO). Mobility completo (48) + Thoroughbreds (18) + Charge (7) = 73. Variante Belisarius campo aperto (Cavalry fino a Rallying Cry + Lightning Charge, Spiked Armor, Hasty Departure + Thoroughbreds): la somma derivata è 75, cioè 1 punto oltre 74 (la build reale lascia un nodo non al massimo, non indicato nel testo).

- Variante **Belisarius campo aperto**: Charge → Galea (+velocità) → Emblazoned Shield → Dragon Saber → Halberd → Disarm → Rallying Cry → Lightning Charge → Spiked Armor → Hasty Departure → Thoroughbreds [36]

### Combo (cavalleria a combo attack)

Esempio: Arthur Pendragon (Cavalry/Versatility/Combo). Alberi: Combo, Cavalry. Punti per albero: Combo 43, Cavalry 31, Versatility 0; totale **74**/74. Fonti: [37] [10] [38] [3]

| # | Albero | Talento / blocco | Punti | Nota |
|---|---|---|---|---|
| 1 | Combo | Iron and Steel | 5/5 | nodo da 5 punti, preso al massimo |
| 2 | Combo | Blizzard of Blows | 3/3 |  |
| 3 | Combo | Force of Nature | 3/3 |  |
| 4 | Combo | No Quarter | 3/3 |  |
| 5 | Combo | 4 talenti principali Combo senza nome (icone spada, mezzaluna, scudo crociato, armatura) | 12 | 3/3 ciascuno |
| 6 | Combo | nodi statistica Combo | 17 | somma letta dallo screenshot |
| 7 | Cavalry | Charge | 3/3 |  (+4 punti di percorso) |
| 8 | Cavalry | Galea | 3/3 |  |
| 9 | Cavalry | Dragon Saber | 3/3 |  (+2 punti di percorso) |
| 10 | Cavalry | Undying Fury | 3/3 |  (+1 punti di percorso) |
| 11 | Cavalry | Emblazoned Shield | 4/4 |  (+6 punti di percorso) |
| 12 | Cavalry | Halberd | 2/3 | 2/3 nello screenshot |

Effetto complessivo: Combo quasi completo (non presi: nodo con spade incrociate 0/3 e due nodi da 1 punto): Iron and Steel 10% di combo attack extra (fattore 250), Blizzard of Blows -1,5% salute nemica cumulabile x5, Force of Nature +3% danno, No Quarter +15 ira per combo attack; Cavalry: Charge, Galea, Dragon Saber, Undying Fury, Emblazoned Shield 4/4 (-12% danno abilità), Halberd 2/3.

Dalla fonte: Allclash (2025-02-03): 'The combo tree is new but already crazy strong with the one downside that you have to invest fully there if you want the final talent ... it's strong and the way to go with him'.

Nota: Allocazione letta VISIVAMENTE dallo screenshot 'King-Arthur-Talent-Tree-Build.jpg' (riseofkingdomsguides, 2025/01) e abbinata alle icone della mappa ufficiale Combo e alle icone roktalents della Cavalry (redHilt=Dragon Saber, redHelmetSide=Galea, redHalberd=Halberd, redHorse=Charge, redSkullFire=Undying Fury, redCrossShield=Emblazoned Shield). L'ordine di acquisto NON è indicato da nessuna fonte. Punti Cavalry (con i nodi di percorso) calcolati dal grafo roktalents: coincidono con i 31 punti letti nello screenshot.

### Smite (fanteria)

Esempio: William Wallace (Infantry/Versatility/Smite). Alberi: Smite, Infantry. Punti non documentati. Fonti: [39] [40] [41] [42]

| # | Albero | Talento / blocco | Punti | Nota |
|---|---|---|---|---|
| 1 | Smite | Smite: tutto il percorso fino al nodo finale (5/5) | n.d. | 'Go first into the Smite Tree and unlock the final node' |
| 2 | Infantry | Infantry: punti restanti | n.d. | 'before investing in the Infantry Tree' |

Effetto complessivo: Nomi ed effetti dei talenti Smite non disponibili nelle fonti raggiungibili.

Nota: Solo indicazioni testuali di allclash (William Wallace 2024; Bai Qi e Tokugawa 2025: 'the talent build that makes sense with him and the Smite Tree'; Tokugawa ha anche una build 'mixed garrison'); il dettaglio è solo nelle immagini o a pagamento.

### Assedio a distanza (Engineering) - extra

Esempio: Babur (Engineering/Versatility/Attack); Margaret I (Engineering/Versatility/Support). Alberi: Engineering, Attack. Punti per albero: Engineering 47, Attack 27; totale **74**/74. Fonti: [11] [43] [44] [3]

| # | Albero | Talento / blocco | Punti | Nota |
|---|---|---|---|---|
| 1 | Engineering | Engineering: percorso fino a Forbearance | n.d. | 'don't spend any talent points anywhere else until you have that unlocked' |
| 2 | Engineering | Engineering: resto dell'albero | 47 | totale Engineering letto dallo screenshot (manca solo un talento da 3 punti, icona aquila) |
| 3 | Attack | Effortless | 3/3 | 'take Effortless to gradually increase the damage dealt to up to 10%' (+15 punti di percorso) |
| 4 | Attack | Fight To The Death | 3/3 | 'Fight to Death is also an interesting talent' (+1 punti di percorso) |
| 5 | Attack | Armored Joints | 2/3 | 2/3 nello screenshot (icona guanto) (+3 punti di percorso) |

Effetto complessivo: Danno a distanza delle unità d'assedio: Forbearance (aumento graduale del danno), Effortless fino a +10% danno, Fight To The Death +6% danno inflitto / +3% subito, Lord of War e Burning Blood lungo il percorso, Armored Joints 2/3.

Nota: Ordine dal testo allclash; Engineering 47 punti letti visivamente dallo screenshot 'rok-babur-best-talent-build.jpg'; ramo Attack (Lord of War, Burning Blood, Effortless, Fight To The Death, Armored Joints 2/3 riconosciuti dalle icone roktalents blueSword/blueSkullFire/blueWaves/blueSwordsMoon/blueGloves) calcolato dal grafo roktalents: 27 punti, coerente con 74-47. Variante Margaret: Engineering fino a Forbearance, poi Support: Rejuvenate, Loose Formation, Hasty Departure.

## 4. I 15 alberi originali

Colonne: Tipo P = talento principale (icona), S = nodo statistica; Punti = punti massimi; Effetto = valore al massimo (tra parentesi il valore con 1 punto se diverso); Tier = profondità nell'albero (1 = nodo iniziale); Prereq = nodi (#id) da avere al massimo; Costo = punti minimi nell'albero per averlo al massimo.

### Infantry — Fanteria

Albero di tipo truppa: bonus a fanteria (attacco/difesa/salute/velocità), anti-cavalleria (Iron Spear), bonus 'solo fanteria' (Hold The Line, Elite Soldiers). Nodi 20 (9 principali), **50 punti** per completarlo; talento finale: Elite Soldiers. Fonti: [3] [45] [9]

Comandanti con questo albero (Zoe 2026): Bai QI, Bjorn Ironside, Charles Martel, Cheok Jun-Gyeong, City Keeper, Eulji Mundeok, Flavius Aetius, Gorgo, Guan Yu, Harald Sigurdsson, K'inich Janaab' Pakal, Leonidas, Liu Che, Pericles, Pyrrhus, Ragnar Prime, Richard I, Sargon the Great, Scipio Aemilianus, Scipio Prime, Sun Tzu, Sun Tzu Prime, Tariq ibn Ziyad, Tokugawa Ieyasu, William Wallace, Zenobia.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | Defense (Infantry) | S | 1 | Difesa della fanteria +1% | 1 | — | 1 |
| 3 | Defense (Infantry) | S | 2 | Difesa della fanteria +2% — per livello: 1 / 2 | 2 | #1 | 3 |
| 4 | Attack (Infantry) | S | 2 | Attacco della fanteria +2% — per livello: 1 / 2 | 2 | #1 | 3 |
| 2 | Call of the Pack | P | 3 | Quando l'armata scende al 50% delle forze, difesa di tutte le truppe +6% — per livello: 2 / 4 / 6 | 3 | #3 | 6 |
| 5 | Iron Spear | P | 3 | La fanteria guidata da questo comandante infligge +9% di danno alla cavalleria — per livello: 3 / 6 / 9 | 3 | #4 | 6 |
| 7 | Double-Headed Axe | P | 3 | Danno degli attacchi normali +1,5% — per livello: 0,5 / 1 / 1,5 | 3 | #3 | 6 |
| 8 | Undying Fury | P | 3 | Gli attacchi normali danno +9 ira — per livello: 3 / 6 / 9 | 3 | #4 | 6 |
| 6 | Health (Infantry) | S | 2 | Salute della fanteria +2% — per livello: 1 / 2 | 4 | #2 | 8 |
| 9 | March Speed (Infantry) | S | 2 | Velocità di marcia della fanteria +6% — per livello: 3 / 6 | 4 | #5 | 8 |
| 10 | Strong of Body | P | 3 | Salute della fanteria +6% — per livello: 2 / 4 / 6 | 5 | #6 | 11 |
| 11 | Defense (Infantry) | S | 2 | Difesa della fanteria +2% — per livello: 1 / 2 | 5 | #6, #7 | 13 |
| 12 | March Speed (Infantry) | S | 2 | Velocità di marcia della fanteria +6% — per livello: 3 / 6 | 5 | #8, #9 | 13 |
| 13 | Fleet Of Foot | P | 3 | Velocità di marcia della fanteria +6% — per livello: 2 / 4 / 6 | 5 | #9 | 11 |
| 14 | Defense (Infantry) | S | 1 | Difesa della fanteria +1% | 6 | #11 | 14 |
| 15 | Health (Infantry) | S | 2 | Salute della fanteria +2% — per livello: 1 / 2 | 6 | #11 | 15 |
| 17 | Attack (Infantry) | S | 2 | Attacco della fanteria +2% — per livello: 1 / 2 | 6 | #12 | 15 |
| 18 | Health (Infantry) | S | 1 | Salute della fanteria +1% | 6 | #12 | 14 |
| 19 | Hold The Line | P | 4 | Se l'armata ha solo fanteria, quando viene attaccata ha il 10% di probabilità di ridurre del 20% il danno subito per 2 secondi — per livello: 5 / 10 / 15 / 20 | 7 | #15 | 19 |
| 20 | Snare of Thorns | P | 4 | Gli attacchi normali hanno il 10% di probabilità di ridurre del 20% la velocità di marcia del bersaglio per 2 secondi — per livello: 5 / 10 / 15 / 20 | 7 | #17 | 19 |
| 16 | Elite Soldiers | P | 5 | Se l'armata ha solo fanteria, attacco, difesa e salute +2,5% — per livello: 0,5 / 1 / 1,5 / 2 / 2,5 | 8 | #19, #20 | 42 |

### Cavalry — Cavalleria

Albero di tipo truppa: bonus alla cavalleria, velocità di marcia, anti-arcieri (Halberd), riduzione danno da abilità (Emblazoned Shield), burst iniziale (Rallying Cry). Nodi 20 (9 principali), **50 punti** per completarlo; talento finale: Rallying Cry. Fonti: [3] [46] [9]

Comandanti con questo albero (Zoe 2026): Achilles, Alexander Nevsky, Arthur Pendragon, Attila, Baibars, Belisarius, Belisarius Prime, Bertrand du Guesclin, Cao Cao, Dragon Lancer, Eleanor of Aquitaine, Genghis Khan, Huo Qubing, Jadwiga, Jan Zizka, Joan of Arc Prime, Justinian I, Lancelot, Minamoto no Yoshitsune, Pelagius, Subutai, William I, Xiang Yu.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | March Speed (Cavalry) | S | 1 | Velocità di marcia della cavalleria +3% | 1 | — | 1 |
| 2 | Attack (Cavalry) | S | 2 | Attacco della cavalleria +2% — per livello: 1 / 2 | 2 | #1 | 3 |
| 3 | Defense (Cavalry) | S | 1 | Difesa della cavalleria +1% | 2 | #1 | 2 |
| 4 | Health (Cavalry) | S | 2 | Salute della cavalleria +2% — per livello: 1 / 2 | 2 | #1 | 3 |
| 5 | Dragon Saber | P | 3 | Danno degli attacchi normali di tutte le truppe guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 3 | #2 | 6 |
| 6 | Galea | P | 3 | Salute della cavalleria +3% — per livello: 1 / 2 / 3 | 3 | #4 | 6 |
| 8 | Halberd | P | 3 | La cavalleria guidata da questo comandante infligge +9% di danno agli arcieri — per livello: 3 / 6 / 9 | 3 | #2, #3 | 7 |
| 9 | Charge | P | 3 | Quando l'armata scende sotto il 50% delle forze, velocità di marcia +30% — per livello: 10 / 20 / 30 | 3 | #3, #4 | 7 |
| 7 | Attack (Cavalry) | S | 1 | Attacco della cavalleria +1% | 4 | #5 | 7 |
| 10 | March Speed (Cavalry) | S | 1 | Velocità di marcia della cavalleria +3% | 4 | #6 | 7 |
| 13 | Attack (Cavalry) | S | 3 | Attacco della cavalleria +3% — per livello: 1 / 2 / 3 | 4 | #8 | 10 |
| 15 | Defense (Cavalry) | S | 3 | Difesa della cavalleria +3% — per livello: 1 / 2 / 3 | 4 | #9 | 10 |
| 11 | Undying Fury | P | 3 | Gli attacchi normali danno +9 ira — per livello: 3 / 6 / 9 | 5 | #7 | 10 |
| 12 | March Speed (Cavalry) | S | 2 | Velocità di marcia della cavalleria +6% — per livello: 3 / 6 | 5 | #13 | 12 |
| 14 | Health (Cavalry) | S | 1 | Salute della cavalleria +1% | 5 | #13, #15 | 19 |
| 16 | March Speed (Cavalry) | S | 2 | Velocità di marcia della cavalleria +6% — per livello: 3 / 6 | 5 | #15 | 12 |
| 17 | Equestrian Excellence | P | 3 | Gli attacchi normali hanno il 10% di probabilità di dare velocità di marcia +15% per 2 secondi — per livello: 5 / 10 / 15 | 5 | #10 | 10 |
| 18 | Disarm | P | 4 | Gli attacchi normali hanno il 10% di probabilità di ridurre del 20% l'attacco nemico per 2 secondi — per livello: 5 / 10 / 15 / 20 | 6 | #7, #12 | 20 |
| 19 | Emblazoned Shield | P | 4 | Danno da abilità subito -12% — per livello: 3 / 6 / 9 / 12 | 6 | #16, #10 | 20 |
| 20 | Rallying Cry | P | 5 | Tutto il danno inflitto +15% nei primi 10 secondi di battaglia — per livello: 3 / 6 / 9 / 12 / 15 | 7 | #18, #19 | 43 |

### Archer — Arcieri

Albero di tipo truppa: bonus agli arcieri, anti-fanteria (Thumb Ring), danno abilità (Venomous Sting), bonus 'solo arcieri' (Phoenix-Tail Arrows, Whistling Arrows). Nodi 20 (9 principali), **48 punti** per completarlo; talento finale: Whistling Arrows. Fonti: [3] [47] [9]

Comandanti con questo albero (Zoe 2026): Amanitore, Artemisia I, Ashurbanipal, Boudica Prime, Choe Yeong, Cyrus the Great, Dido, Edward of Woodstock, El Cid, Gilgamesh, Henry V, Hermann, Hermann Prime, Imhotep, Keira, Markswoman, Nebuchadnezzar II, Qin Shi Huang, Ramesses II, Shajar al-Durr, Shapur I, Siyaj K'ak', Thutmose III, Tomoe Gozen, Tomyris, Zhuge Liang.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | Attack (Archers) | S | 1 | Attacco degli arcieri +1% | 1 | — | 1 |
| 3 | Attack (Archers) | S | 2 | Attacco degli arcieri +2% — per livello: 1 / 2 | 2 | #1 | 3 |
| 4 | March Speed (Archers) | S | 2 | Velocità di marcia degli arcieri +6% — per livello: 3 / 6 | 2 | #1 | 3 |
| 7 | Arrows Nocked | P | 3 | Quando l'armata scende al 50% delle forze, attacco di tutte le truppe +9% — per livello: 3 / 6 / 9 | 3 | #3 | 6 |
| 8 | Thumb Ring | P | 3 | Gli arcieri guidati da questo comandante infliggono +9% di danno alla fanteria — per livello: 3 / 6 / 9 | 3 | #4 | 6 |
| 10 | Rapid Fire | P | 3 | Danno degli attacchi normali di tutte le truppe guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 3 | #3 | 6 |
| 11 | Armed and Armored | P | 3 | Salute degli arcieri +3% — per livello: 1 / 2 / 3 | 3 | #4 | 6 |
| 2 | Attack (Archers) | S | 1 | Attacco degli arcieri +1% | 4 | #7 | 7 |
| 5 | Defense (Archers) | S | 1 | Difesa degli arcieri +1% | 4 | #8 | 7 |
| 12 | Attack (Archers) | S | 3 | Attacco degli arcieri +3% — per livello: 1 / 2 / 3 | 4 | #7, #10 | 12 |
| 13 | March Speed (Archers) | S | 3 | Velocità di marcia degli arcieri +9% — per livello: 3 / 6 / 9 | 4 | #8, #11 | 12 |
| 6 | Full Quiver | P | 3 | Attacco degli arcieri +3% — per livello: 1 / 2 / 3 | 5 | #2 | 10 |
| 9 | Razor Sharp | P | 3 | +9 ira (rage) dopo ogni attacco normale — per livello: 3 / 6 / 9 | 5 | #5 | 10 |
| 14 | Health (Archers) | S | 1 | Salute degli arcieri +1% | 5 | #12 | 13 |
| 15 | Health (Archers) | S | 1 | Salute degli arcieri +1% | 5 | #12 | 13 |
| 16 | Defense (Archers) | S | 1 | Difesa degli arcieri +1% | 5 | #13 | 13 |
| 17 | March Speed (Archers) | S | 1 | Velocità di marcia degli arcieri +3% | 5 | #13 | 13 |
| 18 | Phoenix-Tail Arrrows | P | 4 | Se l'armata ha solo arcieri, gli attacchi normali hanno il 10% di probabilità di lanciare un attacco aggiuntivo (fattore di danno 200) — per livello: 50 / 100 / 150 / 200 | 6 | #14, #15 | 18 |
| 19 | Venomous Sting | P | 4 | Danno delle abilità attive di comandante primario e secondario +8% — per livello: 2 / 4 / 6 / 8 | 6 | #16, #17 | 18 |
| 20 | Whistling Arrows | P | 5 | Se l'armata ha solo arcieri, gli attacchi normali hanno il 10% di probabilità di dare danno inflitto +25% per 2 secondi — per livello: 5 / 10 / 15 / 20 / 25 | 7 | #18, #19 | 40 |

### Leadership — Comando (Leadership)

Albero per truppe miste/rally: capacità truppe (Fresh Recruits), bonus con 3+ tipi di unità, Name Of The King (attacco del rally). Nodi 18 (9 principali), **50 punti** per completarlo; talento finale: Name Of The King. Fonti: [3] [48] [9]

Comandanti con questo albero (Zoe 2026): Aethelflaed, Charlemagne, Frederick I, Gaius Marius, Hannibal Barca, Hector, Heraclius, Honda Tadakatsu, Lapulapu, Lu Bu, Mehmed II, Moctezuma, Osman I, Philip II, Ragnar Lodbrok, Scipio Africanus, Suleiman I, Theodora, Trajan, Wu Zetian, Yi Sun-Sin.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 1 | — | 1 |
| 4 | Attack (All Troops) | S | 2 | Attacco di tutte le unità guidate +1% — per livello: 0,5 / 1 | 2 | #1 | 3 |
| 5 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 2 | #1 | 3 |
| 2 | Fresh Recruits | P | 3 | Capacità massima di truppe (dimensione marcia) +3% — per livello: 1 / 2 / 3 | 3 | #4 | 6 |
| 3 | Healing Herbs | P | 3 | Aumenta del 9% gli effetti di cura ricevuti dalle truppe — per livello: 3 / 6 / 9 | 3 | #5 | 6 |
| 7 | Steely Soul | P | 3 | Danno degli attacchi normali +1,5% — per livello: 0,5 / 1 / 1,5 | 3 | #4 | 6 |
| 8 | Hidden Wrath | P | 3 | +6 ira ogni volta che le truppe di questo comandante vengono attaccate — per livello: 2 / 4 / 6 | 3 | #5 | 6 |
| 6 | Health (All Troops) | S | 3 | Salute di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #2 | 9 |
| 9 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #3 | 9 |
| 11 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #7 | 8 |
| 12 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 4 | #8 | 8 |
| 10 | Armored To The Teeth | P | 3 | Con 3 o più tipi di unità nell'armata, tutto il danno subito -3% — per livello: 1 / 2 / 3 | 5 | #6 | 12 |
| 13 | Armed To The Teeth | P | 3 | Con 3 o più tipi di unità nell'armata, tutto il danno inflitto +3% — per livello: 1 / 2 / 3 | 5 | #9 | 12 |
| 14 | Attack (All Troops) | S | 2 | Attacco di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #6, #11 | 16 |
| 15 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 5 | #9, #12 | 16 |
| 16 | Close Formation | P | 4 | Quando l'armata scende al 50% delle forze, attacco +12% — per livello: 3 / 6 / 9 / 12 | 6 | #14 | 20 |
| 17 | Strategic Prowess | P | 4 | Dopo aver usato un'abilità, difesa delle truppe +20% per 2 secondi — per livello: 5 / 10 / 15 / 20 ✔ allclash Mehmed 2023: 'that additional 20% defense' | 6 | #15 | 20 |
| 18 | Name Of The King | P | 5 | Quando questo comandante guida un rally, attacco dell'armata radunata +5% — per livello: 1 / 2 / 3 / 4 / 5 | 7 | #16, #17 | 44 |

### Integration — Integrazione (truppe miste)

Albero per truppe miste: bonus 'sotto il 50%' per ogni tipo di unità, capacità truppe, bonus con 3+ tipi di unità, Ares' Blessing (meno feriti gravi). Nodi 18 (9 principali), **50 punti** per completarlo; talento finale: Ares' Blessing. Fonti: [3] [49] [9]

Comandanti con questo albero (Zoe 2026): Boudica, Casimir III, Cleopatra VII, Constance, Ishida Mitsunari, Joan of Arc, Lohar, Matilda, Mulan, Pepin III, Queen Tamar of Georgia, Sarka, Seondeok.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 1 | — | 1 |
| 2 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 3 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 4 | Call of the Pack | P | 3 | Quando l'armata scende sotto il 50% delle forze, difesa della fanteria +9% — per livello: 3 / 6 / 9 | 3 | #2 | 7 |
| 5 | Defense Formation | P | 3 | Quando l'armata scende sotto il 50% delle forze, difesa delle unità d'assedio +15% — per livello: 5 / 10 / 15 | 3 | #2 | 7 |
| 6 | Charge | P | 3 | Quando l'armata scende sotto il 50% delle forze, velocità di marcia della cavalleria +9% — per livello: 3 / 6 / 9 | 3 | #3 | 7 |
| 7 | Full Quiver | P | 3 | Quando l'armata scende al 50% delle forze, attacco degli arcieri +9% — per livello: 3 / 6 / 9 | 3 | #3 | 7 |
| 10 | Health (All Troops) | S | 3 | Salute di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #5 | 10 |
| 11 | March Speed (All Troops) | S | 3 | Velocità di marcia di tutte le unità guidate +9% — per livello: 3 / 6 / 9 | 4 | #6 | 10 |
| 9 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #4, #10 | 15 |
| 12 | Attack (All Troops) | S | 2 | Attacco di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #11, #7 | 15 |
| 15 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 5 | #10 | 11 |
| 16 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 5 | #11 | 11 |
| 8 | Fresh Recruits | P | 3 | Capacità massima di truppe (dimensione marcia) +3% — per livello: 1 / 2 / 3 | 6 | #9 | 18 |
| 13 | Steely Soul | P | 3 | Danno degli attacchi normali +1,5% — per livello: 0,5 / 1 / 1,5 | 6 | #12 | 18 |
| 14 | Armored To The Teeth | P | 4 | Con 3 o più tipi di unità nell'armata, tutto il danno subito -4% — per livello: 1 / 2 / 3 / 4 | 6 | #9 | 19 |
| 17 | Armed To The Teeth | P | 4 | Con 3 o più tipi di unità nell'armata, tutto il danno inflitto +4% — per livello: 1 / 2 / 3 / 4 | 6 | #12 | 19 |
| 18 | Ares' Blessing | P | 5 | In battaglia, le unità gravemente ferite si riducono del 10% (diventano leggermente ferite) — per livello: 2 / 4 / 6 / 8 / 10 | 7 | #14, #17 | 42 |

### Attack — Attacco

Albero offensivo generico: attacco, danno normale, Effortless, Last Stand, Lord of War (scala con le stelle). Nodi 18 (9 principali), **48 punti** per completarlo; talento finale: Last Stand. Fonti: [3] [50] [9]

Comandanti con questo albero (Zoe 2026): Attila, Babur, City Keeper, Eulji Mundeok, Gonzalo de Cordoba, Hannibal Barca, Liu Che, Ragnar Lodbrok, Ramesses II, Scipio Africanus, Seondeok, Suleiman I, Tomoe Gozen, Tomyris, William I.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 1 | — | 1 |
| 2 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 3 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 4 | Lord of War | P | 3 | Entrando in battaglia, attacco +(1,5 × livello stelle del comandante)% — per livello: 0,5 / 1 / 1,5 | 3 | #2 | 7 |
| 5 | Burning Blood | P | 3 | +6 ira ogni volta che le truppe di questo comandante vengono attaccate — per livello: 2 / 4 / 6 | 3 | #2 | 7 |
| 6 | Unyielding | P | 3 | Danno da contrattacco inflitto +1,5% — per livello: 0,5 / 1 / 1,5 | 3 | #3 | 7 |
| 7 | Armored Joints | P | 3 | Tutto il danno subito -1,5% — per livello: 0,5 / 1 / 1,5 | 3 | #3 | 7 |
| 8 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 4 | #4 | 8 |
| 9 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #4, #5 | 13 |
| 10 | Health (All Troops) | S | 3 | Salute di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #6, #7 | 13 |
| 11 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 4 | #7 | 8 |
| 12 | Fight To The Death | P | 3 | Tutto il danno inflitto +6%, ma anche tutto il danno subito +3% — per livello: 2 / 4 / 6 | 5 | #8 | 11 |
| 13 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 5 | #9 | 15 |
| 14 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #10 | 15 |
| 15 | Martial Mastery | P | 3 | Danno degli attacchi normali +6%, ma danno dell'abilità attiva -3% — per livello: 2 / 4 / 6 | 5 | #11 | 11 |
| 16 | Effortless | P | 3 | In battaglia, tutto il danno inflitto aumenta del 2,5% ogni 10 secondi (massimo 10%) — per livello: 0,5 / 1 / 2,5 | 6 | #13 | 18 |
| 17 | Victory Charge | P | 3 | Quando l'armata sconfigge un'armata (non guarnigione) di un altro governatore, attacco +6% per 10 secondi (l'effetto svanisce uscendo dalla battaglia) — per livello: 2 / 4 / 6 | 6 | #14 | 18 |
| 18 | Last Stand | P | 5 | Gli attacchi normali hanno il 10% di probabilità di scatenare le truppe (danno +10% per 3 secondi, ma durante l'effetto non si possono usare abilità) — per livello: 2 / 4 / 6 / 8 / 10 | 7 | #16, #17 | 40 |

### Defense — Difesa

Albero difensivo generico: riduzione danni, Loose Formation, Master Armorer (scala con le stelle), cure, Desperate Elegy. Nodi 18 (9 principali), **48 punti** per completarlo; talento finale: Desperate Elegy. Fonti: [3] [51] [9]

Comandanti con questo albero (Zoe 2026): Archimedes, Artemisia I, Bertrand du Guesclin, Casimir III, Charles Martel, Choe Yeong, Eleanor of Aquitaine, Gajah Mada, Gorgo, Heraclius, K'inich Janaab' Pakal, Leonidas, Matilda, Narses, Pyrrhus, Richard I, Tariq ibn Ziyad, Theodora, Yi Sun-Sin.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 1 | — | 1 |
| 2 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 3 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 4 | Master Armorer | P | 3 | Entrando in battaglia, difesa +(1,5 × livello stelle del comandante)% — per livello: 0,5 / 1 / 1,5 | 3 | #2 | 7 |
| 5 | Burning Blood | P | 3 | +6 ira ogni volta che le truppe di questo comandante vengono attaccate — per livello: 2 / 4 / 6 | 3 | #2 | 7 |
| 6 | No Weaknesses | P | 3 | Danno subito -1,5% — per livello: 0,5 / 1 / 1,5 | 3 | #3 | 7 |
| 7 | Spiked Armor | P | 3 | Danno da contrattacco inflitto +1,5% — per livello: 0,5 / 1 / 1,5 | 3 | #3 | 7 |
| 9 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 4 | #4 | 8 |
| 10 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 4 | #4, #5 | 12 |
| 11 | Attack (All Troops) | S | 2 | Attacco di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #6, #7 | 12 |
| 12 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 4 | #7 | 8 |
| 8 | Balance | P | 3 | Danno subito -3%, ma anche danno inflitto -1,5% — per livello: 1 / 2 / 3 | 5 | #9 | 11 |
| 13 | Loose Formation | P | 3 | Danno da abilità subito -9% — per livello: 3 / 6 / 9 ✔ allclash Charles Martel 2023: 'decrease the skill damage taken by 9%' | 5 | #12 | 11 |
| 14 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 5 | #10 | 15 |
| 15 | Health (All Troops) | S | 3 | Salute di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 5 | #11 | 15 |
| 16 | Testudo Formation | P | 3 | Gli attacchi normali hanno il 10% di probabilità di ridurre del 15% tutto il danno subito per 1 secondo — per livello: 5 / 10 / 15 | 6 | #14 | 18 |
| 17 | Medicinal Supplies | P | 3 | Dopo aver usato un'abilità, cura una parte delle unità leggermente ferite (fattore di cura 300) — per livello: 100 / 200 / 300 | 6 | #15 | 18 |
| 18 | Desperate Elegy | P | 5 | Quando le truppe scendono al 30% delle unità, ogni attacco normale dà +25 ira — per livello: 5 / 10 / 15 / 20 / 25 | 7 | #16, #17 | 40 |

### Skill — Abilità

Albero 'nuker': generazione di ira (Rejuvenate, Feral Nature, Burning Blood), danno abilità (Tactical Mastery, Clarity, All For One). Nodi 19 (9 principali), **48 punti** per completarlo; talento finale: Feral Nature. Fonti: [3] [52] [9]

Comandanti con questo albero (Zoe 2026): Alexander Nevsky, Ashurbanipal, Baibars, Bjorn Ironside, Boudica, Boudica Prime, Charlemagne, Constance, Cyrus the Great, Edward of Woodstock, El Cid, Flavius Aetius, Frederick I, Gaius Marius, Genghis Khan, Gilgamesh, Guan Yu, Harald Sigurdsson, Hermann, Honda Tadakatsu, Huo Qubing, Jan Zizka, Joan of Arc Prime, Keira, Lapulapu, Lu Bu, Markswoman, Mary I, Mehmed II, Minamoto no Yoshitsune, Moctezuma, Nebuchadnezzar II, Osman I, Pelagius, Qin Shi Huang, Ragnar Prime, Sargon the Great, Sarka, Shajar al-Durr, Shapur I, Siyaj K'ak', Sun Tzu, Xiang Yu, Zhuge Liang.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 1 | — | 1 |
| 3 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 2 | Burning Blood | P | 3 | Gli attacchi normali danno +9 ira — per livello: 3 / 6 / 9 | 3 | #3 | 7 |
| 4 | Heraldic Shield | P | 3 | Danno da abilità subito -6% — per livello: 2 / 4 / 6 | 3 | #3 | 7 |
| 7 | All For One | P | 3 | Dopo che il comandante primario usa un'abilità, il danno dell'abilità attiva del secondario aumenta del 6% — per livello: 2 / 4 / 6 | 3 | #3 | 7 |
| 8 | Tactical Mastery | P | 3 | Danno dell'abilità attiva +3% — per livello: 1 / 2 / 3 | 3 | #3 | 7 |
| 6 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 4 | #2 | 8 |
| 9 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 4 | #4 | 8 |
| 11 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #7 | 9 |
| 13 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #8 | 9 |
| 5 | Latent Power | P | 3 | Aumenta del 6% il danno aggiuntivo delle abilità (additional skill damage) — per livello: 2 / 4 / 6 | 5 | #6 | 11 |
| 10 | Naked Rage | P | 3 | Danno da abilità inflitto +6%, ma anche danno da abilità subito +6% — per livello: 2 / 4 / 6 | 5 | #9 | 11 |
| 12 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #11, #13 | 16 |
| 14 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #6, #11 | 15 |
| 16 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 5 | #9, #13 | 15 |
| 15 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 6 | #12 | 19 |
| 17 | Rejuvenate | P | 3 | Ripristina subito 60 ira ogni volta che viene usata un'abilità — per livello: 20 / 40 / 60 ✔ allclash Sun Tzu 2023: 'you will get 60 rage each time a skill is used' | 6 | #14 | 18 |
| 19 | Clarity | P | 3 | Dopo aver usato l'abilità attiva, danno da abilità +6% per 6 secondi — per livello: 2 / 4 / 6 | 6 | #16 | 18 |
| 18 | Feral Nature | P | 5 | Gli attacchi normali hanno il 10% di probabilità di dare +100 ira — per livello: 20 / 40 / 60 / 80 / 100 ✔ allclash Guan Yu 2023: 'basically give you 10 rage with every attack statistically' (10% x 100) | 7 | #15, #17, #19 | 42 |

### Support — Supporto

Albero di supporto: cure ricevute (Elixir), riduzione danno abilità, Hasty Departure, Rejuvenate (150 ira), Cage of Thorns (rallentamento). Nodi 20 (9 principali), **48 punti** per completarlo; talento finale: Cage of Thorns. Fonti: [3] [53] [9]

Comandanti con questo albero (Zoe 2026): Aethelflaed, Afonso de Albuquerque, Amanitore, Cleopatra VII, Dido, Hector, Henry V, Hermann Prime, Imhotep, Ishida Mitsunari, Joan of Arc, Justinian I, Lohar, Margaret, Mulan, Pepin III, Pericles, Philip II, Queen Tamar of Georgia, Scipio Prime, Thutmose III, Trajan, Wu Zetian, Zenobia.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | March Speed (All Troops) | S | 1 | Velocità di marcia di tutte le unità guidate +3% | 1 | — | 1 |
| 2 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 3 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 4 | Loose Formation | P | 3 | Danno da abilità subito -9% — per livello: 3 / 6 / 9 | 3 | #2 | 7 |
| 5 | Elixir | P | 3 | Aumenta del 9% gli effetti di cura ricevuti dalle truppe — per livello: 3 / 6 / 9 ✔ allclash Lohar 2023: 'Elixir, which will give you 9% more healing effect' | 3 | #2 | 7 |
| 6 | Hasty Departure | P | 3 | Partendo da una struttura, velocità di marcia +60% per 10 secondi — per livello: 20 / 40 / 60 | 3 | #3 | 7 |
| 7 | Burning Blood | P | 3 | Gli attacchi normali danno +9 ira — per livello: 3 / 6 / 9 | 3 | #3 | 7 |
| 8 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #4, #5 | 12 |
| 9 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 4 | #5 | 8 |
| 10 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 4 | #6 | 8 |
| 11 | Attack (All Troops) | S | 2 | Attacco di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #6, #7 | 12 |
| 12 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 5 | #8 | 13 |
| 13 | Counterattack | P | 3 | Quando vengono curate, le truppe ottengono attacco +9% per 3 secondi — per livello: 3 / 6 / 9 | 5 | #9 | 11 |
| 14 | Expert Design | P | 3 | Attacco, difesa e salute delle unità d'assedio +6% — per livello: 2 / 4 / 6 | 5 | #10 | 11 |
| 15 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 5 | #11 | 13 |
| 16 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 6 | #12 | 15 |
| 17 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 6 | #15 | 15 |
| 18 | Emergency Protection | P | 3 | Quando le truppe subiscono danno da abilità, 50% di probabilità di ottenere un'ulteriore riduzione del danno da abilità del 15% per 3 secondi — per livello: 5 / 10 / 15 | 7 | #16 | 18 |
| 19 | Rejuvenate | P | 3 | Ripristina subito 150 ira ogni volta che viene usata un'abilità — per livello: 50 / 100 / 150 ✔ allclash Lohar/Saladin 2023: '150 rage when you use ... skill' | 7 | #17 | 18 |
| 20 | Cage of Thorns | P | 5 | Dopo aver usato l'abilità attiva, riduce del 25% la velocità di marcia delle truppe nemiche vicine (3 secondi, max 5 bersagli) — per livello: 5 / 10 / 15 / 20 / 25 | 8 | #18, #19 | 40 |

### Mobility — Mobilità

Albero della velocità: velocità di marcia (Lightning Charge, Hasty Departure, Time Management), resistenza ai rallentamenti. Nodi 20 (9 principali), **48 punti** per completarlo; talento finale: Time Management. Fonti: [3] [54] [9]

Comandanti con questo albero (Zoe 2026): Belisarius, Belisarius Prime, Cao Cao, Dragon Lancer, Jadwiga, Lancelot.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | March Speed (All Troops) | S | 1 | Velocità di marcia di tutte le unità guidate +3% | 1 | — | 1 |
| 2 | Attack (All Troops) | S | 2 | Attacco di tutte le unità guidate +1% — per livello: 0,5 / 1 | 2 | #1 | 3 |
| 3 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 2 | #1 | 2 |
| 4 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 2 | #1 | 3 |
| 5 | Saving Cross | P | 3 | Danno da abilità subito -9% — per livello: 3 / 6 / 9 | 3 | #2 | 6 |
| 6 | Vortex | P | 3 | Quando si usa l'abilità attiva, 10% di probabilità di ridurre del 15% la velocità di marcia del bersaglio per 3 secondi — per livello: 5 / 10 / 15 | 3 | #2, #3 | 7 |
| 7 | Lightning Charge | P | 3 | Velocità di marcia di tutte le truppe +6% — per livello: 2 / 4 / 6 | 3 | #3, #4 | 7 |
| 8 | Spiked Armor | P | 3 | Danno da contrattacco inflitto +1,5% — per livello: 0,5 / 1 / 1,5 | 3 | #4 | 6 |
| 10 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 4 | #5 | 7 |
| 11 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #6 | 10 |
| 12 | Health (All Troops) | S | 3 | Salute di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #7 | 10 |
| 13 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 4 | #8 | 7 |
| 9 | Swiftness | P | 3 | Quando le truppe sono colpite da un'abilità attiva, velocità di marcia +15% per 5 secondi — per livello: 5 / 10 / 15 | 5 | #10 | 10 |
| 14 | Hasty Departure | P | 3 | Partendo da una struttura, velocità di marcia +60% per 10 secondi — per livello: 20 / 40 / 60 ✔ allclash Cao Cao 2023: 'boost the movement speed by 60% in the first 10 seconds after leaving a structure' | 5 | #13 | 10 |
| 15 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 5 | #10, #11 | 16 |
| 16 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 5 | #11, #12 | 19 |
| 17 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #12, #13 | 16 |
| 18 | Alacrity | P | 3 | Le truppe hanno il 30% di probabilità di resistere ai rallentamenti nemici — per livello: 10 / 20 / 30 | 6 | #15 | 19 |
| 20 | Triumphant March | P | 3 | Quando l'armata sconfigge un'armata di un altro governatore, velocità di marcia +15% per 10 secondi — per livello: 5 / 10 / 15 | 6 | #17 | 19 |
| 19 | Time Management | P | 5 | Velocità di marcia +10% fuori dal combattimento, ma -10% durante il combattimento — per livello: 2 / 4 / 6 / 8 / 10 | 7 | #18, #20 | 41 |

### Garrison — Guarnigione

Albero di difesa città/strutture: bonus quando il comandante è comandante di guarnigione, torre di guardia, King's Guard, Divine Favor. Nodi 20 (9 principali), **48 punti** per completarlo; talento finale: Divine Favor. Fonti: [3] [55] [9]

Comandanti con questo albero (Zoe 2026): Amanitore, Artemisia I, Charles Martel, Choe Yeong, Dido, Eleanor of Aquitaine, Eulji Mundeok, Flavius Aetius, Gorgo, Heraclius, Hermann, Imhotep, Jadwiga, Jan Zizka, Lapulapu, Pelagius, Pericles, Richard I, Sun Tzu, Theodora, Tokugawa Ieyasu, Wu Zetian, Yi Sun-Sin, Zenobia.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 1 | — | 1 |
| 4 | Attack (All Troops) | S | 2 | Attacco di tutte le unità guidate +1% — per livello: 0,5 / 1 | 2 | #1 | 3 |
| 3 | Empty Fortress Strategem | P | 3 | Da comandante di guarnigione: danno inflitto alle armate attaccanti +6% — per livello: 2 / 4 / 6 | 3 | #4 | 6 |
| 5 | Impenetrable Fortifications | P | 3 | Da comandante di guarnigione: danno subito dalla guarnigione dall'armata attaccante -6% — per livello: 2 / 4 / 6 | 3 | #4 | 6 |
| 8 | Adamantine Walls | P | 3 | Da comandante di guarnigione: difesa della torre di guardia +15% — per livello: 5 / 10 / 15 | 3 | #4 | 6 |
| 9 | City Guardian | P | 3 | Da comandante di guarnigione: attacco della torre di guardia +15% — per livello: 5 / 10 / 15 | 3 | #4 | 6 |
| 2 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 4 | #3 | 7 |
| 6 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 4 | #5 | 7 |
| 12 | Attack (All Troops) | S | 2 | Attacco di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #3 | 8 |
| 13 | Attack (All Troops) | S | 2 | Attacco di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #8 | 8 |
| 14 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #9 | 8 |
| 15 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #5 | 8 |
| 7 | Impregnable | P | 3 | Da comandante di guarnigione: danno da abilità subito dalla guarnigione -15% — per livello: 5 / 10 / 15 | 5 | #2 | 10 |
| 10 | Nowhere To Turn | P | 3 | Da comandante di guarnigione: +6 ira ogni volta che la città viene attaccata — per livello: 2 / 4 / 6 | 5 | #6 | 10 |
| 11 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #12 | 10 |
| 16 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #15 | 10 |
| 18 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 5 | #13, #14 | 15 |
| 17 | Know Thy Enemy | P | 3 | Da comandante di guarnigione: se la guarnigione viene circondata, l'effetto di riduzione del danno aumenta del 9% — per livello: 3 / 6 / 9 | 6 | #11, #13 | 18 |
| 19 | Kings Guard | P | 3 | Da comandante di guarnigione: attacco, difesa e salute della guarnigione +3% (nessun effetto nella guarnigione delle città) — per livello: 1 / 2 / 3 | 6 | #14, #16 | 18 |
| 20 | Divine Favor | P | 5 | Da comandante di guarnigione: quando attaccata, la guarnigione ha il 10% di probabilità di ottenere uno scudo che assorbe danni (fattore 500) — per livello: 100 / 200 / 300 / 400 / 500 | 7 | #17, #19 | 38 |

### Peacekeeping — Mantenimento della pace (barbari)

Albero PvE: danno a barbari/neutrali, esperienza, costo AP ridotto (Insight), Trophy Hunter, Curing Chant. Nodi 20 (9 principali), **48 punti** per completarlo; talento finale: Curing Chant. Fonti: [3] [56] [9] [57]

Comandanti con questo albero (Zoe 2026): Aethelflaed, Belisarius, Boudica, Boudica Prime, Cao Cao, Keira, Lohar, Markswoman, Minamoto no Yoshitsune, Moctezuma, Mulan.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | March Speed (All Troops) | S | 1 | Velocità di marcia di tutte le unità guidate +3% | 1 | — | 1 |
| 2 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 3 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 4 | Killer Instinct | P | 3 | Danno degli attacchi normali contro barbari e unità neutrali +9% — per livello: 3 / 6 / 9 | 3 | #2 | 7 |
| 5 | Domination | P | 3 | Danno da abilità contro barbari e unità neutrali +15% — per livello: 5 / 10 / 15 ✔ allclash Boudica 2023: 'increase the skill damage ... against Barbarians for another 15%' | 3 | #2 | 7 |
| 6 | Quick Study | P | 3 | Esperienza ottenuta da barbari e unità neutrali +15% — per livello: 5 / 10 / 15 | 3 | #3 | 7 |
| 7 | Insight | P | 3 | Costo in punti azione (AP) per attaccare barbari e unità neutrali -9% — per livello: 3 / 6 / 9 | 3 | #3 | 7 |
| 8 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #4 | 9 |
| 9 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 4 | #5 | 8 |
| 12 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 4 | #6 | 8 |
| 13 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 4 | #7 | 9 |
| 10 | Mighty Force | P | 3 | Quando questo comandante guida un rally, tutto il danno inflitto a barbari e unità neutrali +9% — per livello: 3 / 6 / 9 | 5 | #9 | 11 |
| 11 | Trophy Hunter | P | 3 | Dopo aver sconfitto barbari o altre unità neutrali, l'armata riceve 15 Resource Pack C di lv.1 (a caso 1.000 cibo, 1.000 legno, 750 pietra o 500 oro) — per livello: 5 / 10 / 15 | 5 | #12 | 11 |
| 14 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #8, #9 | 15 |
| 17 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #12, #13 | 15 |
| 15 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 6 | #14 | 16 |
| 16 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 6 | #17 | 16 |
| 18 | Double-Edged Sword | P | 3 | Danno inflitto a barbari/unità neutrali +15%, ma anche danno subito da essi +15%; effetti di cura ricevuti +15% — per livello: 5 / 10 / 15 | 6 | #14 | 18 |
| 19 | Thoroughbreds | P | 3 | Velocità di marcia di tutte le truppe +9% — per livello: 3 / 6 / 9 ✔ allclash Boudica 2023: 'the 9% added march speed' | 6 | #17 | 18 |
| 20 | Curing Chant | P | 5 | Dopo aver sconfitto barbari o altre unità neutrali, cura una parte delle unità leggermente ferite (fattore di cura 500) — per livello: 100 / 200 / 300 / 400 / 500 | 7 | #18, #19 | 40 |

### Gathering — Raccolta

Albero di raccolta: velocità di raccolta per risorsa e generale (Superior Tools), risorse extra (The More The Better), velocità unità d'assedio. Nodi 20 (9 principali), **48 punti** per completarlo; talento finale: Superior Tools. Fonti: [3] [58] [9] [57]

Comandanti con questo albero (Zoe 2026): Casimir III, Cleopatra VII, Constance, Gaius Marius, Ishida Mitsunari, Joan of Arc, Matilda, Pepin III, Queen Tamar of Georgia, Sarka, Seondeok.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | March Speed (All Troops) | S | 1 | Velocità di marcia di tutte le unità guidate +3% | 1 | — | 1 |
| 2 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 2 | #1 | 3 |
| 3 | Attack (All Troops) | S | 2 | Attacco di tutte le unità guidate +1% — per livello: 0,5 / 1 | 2 | #1 | 3 |
| 4 | Gathering Mastery (Gold) | P | 3 | Velocità di raccolta dell'oro +30% — per livello: 10 / 20 / 30 | 3 | #2 | 6 |
| 5 | Gathering Mastery (Stone) | P | 3 | Velocità di raccolta della pietra +30% — per livello: 10 / 20 / 30 | 3 | #2 | 6 |
| 6 | Gathering Mastery (Food) | P | 3 | Velocità di raccolta del cibo +30% — per livello: 10 / 20 / 30 | 3 | #3 | 6 |
| 7 | Gathering Mastery (Wood) | P | 3 | Velocità di raccolta del legno +30% — per livello: 10 / 20 / 30 | 3 | #3 | 6 |
| 8 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 4 | #4 | 7 |
| 9 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 4 | #5, #6 | 13 |
| 10 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 4 | #7 | 7 |
| 11 | Tourniquet | P | 3 | In battaglia, le unità gravemente ferite si riducono del 6% (diventano leggermente ferite) — per livello: 2 / 4 / 6 | 5 | #8 | 10 |
| 12 | Modified Axle | P | 3 | Velocità di marcia delle unità d'assedio +30% — per livello: 10 / 20 / 30 | 5 | #10 | 10 |
| 14 | Health (All Troops) | S | 2 | Salute di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #9 | 15 |
| 13 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 6 | #8, #14 | 20 |
| 15 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 6 | #10, #14 | 20 |
| 16 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 6 | #14 | 18 |
| 17 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 6 | #14 | 18 |
| 18 | The More The Better | P | 3 | Al termine della raccolta le truppe ricevono il 6% di risorse in più — per livello: 2 / 4 / 6 ✔ allclash Cleopatra 2023/2026: 'the 6% flat increase of gathered resources' | 7 | #13 | 23 |
| 20 | Armed Convoy | P | 3 | Difesa delle truppe +15% mentre raccolgono risorse sulla mappa — per livello: 5 / 10 / 15 | 7 | #15 | 23 |
| 19 | Superior Tools | P | 5 | Velocità di raccolta di tutte le risorse +25% — per livello: 5 / 10 / 15 / 20 / 25 ✔ allclash Cleopatra 2023/2026: 'gather 25% faster' | 8 | #18, #20 | 36 |

### Conquering — Conquista

Albero d'assalto alle città: torri di guardia, guarnigioni (Meteor Shower), meno morti attaccando città (Tear of Blessing), velocità del rally. Nodi 18 (9 principali), **48 punti** per completarlo; talento finale: Meteor Shower. Fonti: [3] [59] [9]

Comandanti con questo albero (Zoe 2026): Ashurbanipal, Attila, Baibars, Bertrand du Guesclin, Bjorn Ironside, Charlemagne, Frederick I, Gilgamesh, Guan Yu, Hannibal Barca, Harald Sigurdsson, Henry V, Justinian I, K'inich Janaab' Pakal, Lu Bu, Mehmed II, Nebuchadnezzar II, Osman I, Ragnar Lodbrok, Scipio Aemilianus, Scipio Africanus, Shapur I, Siyaj K'ak', Subutai, Suleiman I, Tariq ibn Ziyad, Tomyris, Xiang Yu.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 1 | — | 1 |
| 2 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 3 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 5 | Signal Flare | P | 3 | Danno inflitto alle torri di guardia (watchtower) +15% — per livello: 5 / 10 / 15 | 3 | #2 | 7 |
| 6 | Marionette | P | 3 | Danno subito dalle torri di guardia -15% — per livello: 5 / 10 / 15 | 3 | #2 | 7 |
| 7 | Moment of Triumph | P | 3 | Finché l'armata è sopra il 90% delle forze, tutto il danno inflitto +9% — per livello: 3 / 6 / 9 | 3 | #3 | 7 |
| 8 | Buckler Shield | P | 3 | Danno da contrattacco subito -9% — per livello: 3 / 6 / 9 | 3 | #3 | 7 |
| 4 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 4 | #5 | 8 |
| 9 | Health (All Troops) | S | 1 | Salute di tutte le unità guidate +0,5% | 4 | #8 | 8 |
| 11 | Health (All Troops) | S | 3 | Salute di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #5, #6 | 13 |
| 12 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #7, #8 | 13 |
| 10 | Well Provisioned | P | 3 | Capacità di carico delle truppe +9% — per livello: 3 / 6 / 9 | 5 | #4 | 11 |
| 13 | Thoroughbreds | P | 3 | Quando questo comandante guida un rally, velocità di marcia dell'armata radunata +9% — per livello: 3 / 6 / 9 | 5 | #9 | 11 |
| 14 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 5 | #11 | 15 |
| 16 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 5 | #12 | 15 |
| 17 | Tear of Blessing | P | 3 | Attaccando la città di un altro governatore, le truppe che muoiono si riducono del 9%: diventano gravemente ferite (curabili in ospedale) — per livello: 3 / 6 / 9 | 6 | #14 | 18 |
| 18 | Entrenched | P | 3 | Danno inflitto alle roccaforti (strongholds) +3% e danno subito dalle loro guarnigioni -3% — per livello: 1 / 2 / 3 | 6 | #16 | 18 |
| 15 | Meteor Shower | P | 5 | Attaccando guarnigioni, gli attacchi normali hanno il 10% di probabilità di aumentare del 50% tutto il danno del turno successivo — per livello: 10 / 20 / 30 / 40 / 50 | 7 | #17, #18 | 40 |

### Versatility — Versatilità

Albero ibrido: un po' di raccolta, barbari, guarnigione e attacco città; finale Turn Of Fate. Nodi 18 (9 principali), **48 punti** per completarlo; talento finale: Turn Of Fate. Fonti: [3] [60] [9]

Comandanti con questo albero (Zoe 2026): Achilles, Afonso de Albuquerque, Alexander Nevsky, Archimedes, Arthur Pendragon, Babur, Bai QI, Belisarius Prime, Cheok Jun-Gyeong, City Keeper, Cyrus the Great, Dragon Lancer, Edward of Woodstock, El Cid, Gajah Mada, Genghis Khan, Gonzalo de Cordoba, Hector, Hermann Prime, Honda Tadakatsu, Huo Qubing, Joan of Arc Prime, Lancelot, Leonidas, Liu Che, Margaret, Mary I, Narses, Philip II, Pyrrhus, Qin Shi Huang, Ragnar Prime, Ramesses II, Sargon the Great, Scipio Prime, Shajar al-Durr, Sun Tzu Prime, Thutmose III, Tomoe Gozen, Trajan, William I, William Wallace, Zhuge Liang.

| # | Talento | Tipo | Punti | Effetto (IT) | Tier | Prereq | Costo |
|---|---|---|---|---|---|---|---|
| 1 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 1 | — | 1 |
| 3 | Health (All Troops) | S | 3 | Salute di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 2 | #1 | 4 |
| 2 | Superior Tools | P | 3 | Velocità di raccolta +15% — per livello: 5 / 10 / 15 | 3 | #3 | 7 |
| 4 | Marionette | P | 3 | Attaccando altre città, danno subito dalle torri di guardia -9% — per livello: 3 / 6 / 9 | 3 | #3 | 7 |
| 7 | City Guardian | P | 3 | Da comandante di guarnigione: attacco della torre di guardia +9% — per livello: 3 / 6 / 9 | 3 | #3 | 7 |
| 8 | Insight | P | 3 | Costo in punti azione (AP) per attaccare barbari e unità neutrali -9 — per livello: 3 / 6 / 9 | 3 | #3 | 7 |
| 6 | Attack (All Troops) | S | 1 | Attacco di tutte le unità guidate +0,5% | 4 | #2 | 8 |
| 9 | Defense (All Troops) | S | 1 | Difesa di tutte le unità guidate +0,5% | 4 | #4 | 8 |
| 11 | March Speed (All Troops) | S | 2 | Velocità di marcia di tutte le unità guidate +6% — per livello: 3 / 6 | 4 | #2 | 9 |
| 12 | Attack (All Troops) | S | 3 | Attacco di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #7 | 10 |
| 13 | Defense (All Troops) | S | 3 | Difesa di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 4 | #8 | 10 |
| 14 | Defense (All Troops) | S | 2 | Difesa di tutte le unità guidate +1% — per livello: 0,5 / 1 | 4 | #4 | 9 |
| 5 | Nowhere To Turn | P | 3 | Da comandante di guarnigione: +6 ira ogni volta che la città viene attaccata — per livello: 2 / 4 / 6 | 5 | #6 | 11 |
| 10 | Buckler Shield | P | 3 | Attaccando città di altri governatori, le unità che muoiono si riducono del 3% (diventano gravemente ferite e vanno in ospedale) — per livello: 1 / 2 / 3 | 5 | #9 | 11 |
| 15 | King's Guard | P | 3 | Da comandante di guarnigione: attacco, difesa e salute della guarnigione +3% — per livello: 1 / 2 / 3 | 5 | #11, #12 | 18 |
| 16 | Health (All Troops) | S | 3 | Salute di tutte le unità guidate +1,5% — per livello: 0,5 / 1 / 1,5 | 5 | #12, #13 | 19 |
| 17 | Meteor Shower | P | 3 | Attaccando altre città, danno inflitto alla guarnigione +3% — per livello: 1 / 2 / 3 | 5 | #13, #14 | 18 |
| 18 | Turn Of Fate | P | 5 | Entrando in battaglia concede a caso, per 5 secondi, uno di questi effetti: attacco +5%, difesa -5%, danno inflitto +5% o velocità di marcia -5% (testo come da fonte) — per livello: 1 / 2 / 3 / 4 / 5 | 6 | #15, #17 | 37 |

## 5. Alberi nuovi: Engineering, Smite, Combo

### Engineering — Ingegneria (assedio)

Stato: **esiste; un solo talento noto per nome (Forbearance), struttura letta da screenshot; nomi/effetti degli altri talenti NON documentati**. Albero delle unità d'assedio a distanza ('ranged'), introdotto nel 2023 con Babur e Margaret I (patch 1.0.67-1.0.68). Introdotto: inizio 2023 (patch 1.0.67 "Spring Once More": equipaggiamento leggendario da ingegneria; 1.0.68 "Shifting Sands": filtro "Engineering" nella selezione comandanti). Screenshot Babur (allclash 2023-04) e Narses (riseofkingdomsguides 2024-12): nodo finale da 5 punti in cima (icona a spirale), due talenti principali da 4 punti sotto il finale (icone scudo e catapulta), sei talenti principali da 3 punti (icone ingranaggio, uomo forte, frecce, elmo, bandiera, aquila) e nodi statistica da 1-2 punti. Unico nome noto: Forbearance. Patch 1.0.83 (2024-06-21): solo i comandanti 'revamped' o quelli con il talento Engineering possono usare l'abilità attiva guidando truppe skirmisher o artillery. Fonti: [61] [62] [9] [63] [64] [11] [43] [44] [21]

Comandanti (Zoe 2026 + hokbuild 2026): Afonso de Albuquerque, Archimedes, Babur, Elizabeth I, Gajah Mada, Gonzalo de Cordoba, John Hunyadi, Margaret, Mary I, Narses, Stephen III.

| Talento | Punti | Effetto (IT) |
|---|---|---|
| Forbearance | n.d. | Aumento del danno inflitto che si riattiva e cresce gradualmente durante il combattimento ('re-triggering damage boost'); valori non pubblicati — Allclash consiglia di non spendere punti altrove finché Forbearance non è sbloccato: talento profondo nell'albero (posizione esatta non documentata). |

Punti totali: 50 (20 nodi e 50 punti letti VISIVAMENTE dallo screenshot della build di Babur (allclash, 2023-04): 47 punti assegnati + un talento principale da 3 punti a 0/3. Derivato, da verificare.)

### Smite — Smite

Stato: **esiste; talenti NON documentati (nessuna fonte testuale raggiungibile)**. Albero di fanteria legato al danno 'Smite' (William Wallace, Scipio Aemilianus, Bai Qi, Tokugawa Ieyasu, Sun Tzu Prime). Introdotto: estate 2024 (William Wallace e Scipio Aemilianus; immagine build riseofkingdomsguides caricata 2024/06; Zoe: release 2024-07-30). Allclash (2024-08-02): l'albero è costruito in modo da dover andare 'all-in' per sbloccare il nodo finale. Screenshot allclash (William Wallace 2024-08, Tokugawa 2025-04): nodo finale da 5 punti (icona martello), talenti principali da 3 punti con icone teschio in fiamme, mazza chiodata, incudine, martello con mezzaluna, martello, armatura, ascia e onde; nomi non leggibili.  Fonti: [9] [63] [39] [40] [41] [42]

Comandanti (Zoe 2026 + hokbuild 2026): Bai QI, Cheok Jun-Gyeong, Scipio Aemilianus, Sun Tzu Prime, Tokugawa Ieyasu, William Wallace.

### Combo — Combo

Stato: **parziale: 4 talenti principali documentati da fonte ufficiale**. Albero di cavalleria basato sui 'combo attack' (attacchi extra che contano come attacchi normali). Definizione ufficiale: il danno dei combo attack è influenzato dai bonus al danno normale; i combo attack attivano gli effetti degli attacchi base ma non provocano contrattacchi. Introdotto: gennaio 2025: patch 1.0.90 'Return of the King' (2025-01-05) con King Arthur; rivelazione ufficiale dell'albero 2025-01-03. Mappa ufficiale: 9 talenti principali (icone spada, mezzaluna, scudo crociato, figura [Blizzard of Blows], figura in corsa [Force of Nature], teschio in fiamme [No Quarter], armatura, vortice [Iron and Steel], spade incrociate) più nodi statistica. 5 talenti principali senza nome nelle fonti.  Fonti: [10] [9] [63] [37] [38] [23]

Comandanti (Zoe 2026 + hokbuild 2026): Achilles, Arthur Pendragon, David, Gang Gamchan, Subutai.

| Talento | Punti | Effetto (IT) |
|---|---|---|
| Blizzard of Blows | 3 | Ogni volta che la truppa lancia un attacco base di qualsiasi tipo, 10% di probabilità di ridurre la salute della truppa bersaglio dell'1,5% per 3 secondi (cumulabile fino a 5 volte; più truppe possono cumulare l'effetto sullo stesso bersaglio) |
| No Quarter | 3 | Ogni volta che la truppa lancia un combo attack di qualsiasi tipo, ottiene 15 ira |
| Force of Nature | 3 | Ogni volta che la truppa lancia un attacco base di qualsiasi tipo, 10% di probabilità di ottenere +3% di danno inflitto per 3 secondi (ricarica 5 secondi) |
| Iron and Steel | 5 | Ogni volta che la truppa lancia un combo attack/ranged combo attack, 10% di probabilità di lanciarne uno extra (fattore di danno 250; ricarica 10 secondi). È il nodo da 5 punti dell'albero |

Punti totali: 48 (48 = somma letta visivamente dallo screenshot della build di Arthur (43 punti assegnati + nodi a 0/3, 0/1, 0/1): derivato, da verificare.)

## 6. Conflitti tra fonti

- **Infantry / Call of the Pack (#2) tipo di effetto** — roktalents.com: When the army led by this commander has been reduced to 50% strength, increases defense of all troops by 6%; gamesguideinfo.com: Max Lv. 3 Troop Attack Inc Upon 50 Perc Army Reduction 6.0%. Stesso numero ma effetto di natura diversa: usato roktalents (più recente). [3] [45]
- **Attack / Lord of War (#4) valore/effetto al massimo** — roktalents.com: When troops led by this commander enter battle, increases attack by (1,5 x Commander Star Level)%; gamesguideinfo.com: Max Lv. 3 Commander Star Level Attack Increase Factor +2. Usato il valore roktalents (più recente); possibile revisione del talento dopo il 2019 o errore di etichetta su gamesguideinfo. [3] [50]
- **Attack / Effortless (#16) valore/effetto al massimo** — roktalents.com: During battles, increases all damage dealt by 2,5% every 10 seconds (up to a maximum of 10%); gamesguideinfo.com: Max Lv. 3 Damage Dealt 10s Increment 1.5%. Usato il valore roktalents (più recente); possibile revisione del talento dopo il 2019 o errore di etichetta su gamesguideinfo. [3] [50]
- **Garrison / Health (All Troops) (#2) valore/effetto al massimo** — roktalents.com: Increases the health of all units led by this commander by 0,5%; gamesguideinfo.com: Max Lv. 1 Troop Health 1.0%. Usato il valore roktalents (più recente); possibile revisione del talento dopo il 2019 o errore di etichetta su gamesguideinfo. [3] [55]
- **Conquering / Meteor Shower (#15) punti massimi** — roktalents.com: 5; gamesguideinfo.com: 3. roktalents è più recente (2020); gamesguideinfo riflette dati dell'epoca Rise of Civilizations. [3] [59]
- **Conquering / Tear of Blessing (#17) punti massimi** — roktalents.com: 3; gamesguideinfo.com: 5. roktalents è più recente (2020); gamesguideinfo riflette dati dell'epoca Rise of Civilizations. [3] [59]
- **Conquering / Entrenched (#18) valore/effetto al massimo** — roktalents.com: Increases all damage dealt to strongholds by 3%, and damage taken from stronghold garrisons is reduced by 3%; gamesguideinfo.com: Max Lv. 3 Damage Taken from Garrison Reduction 6.0%. Usato il valore roktalents (più recente); possibile revisione del talento dopo il 2019 o errore di etichetta su gamesguideinfo. [3] [59]
- **Versatility / Buckler Shield (#10) tipo di effetto** — roktalents.com: When attacking other governors' cities, decreases the number of units that die in battle by 3% (these units will instead be severely wounded and sent to the hospital); gamesguideinfo.com: Max Lv. 3 Damage Taken from Garrison Reduction 3.0%. Stesso numero ma effetto di natura diversa: usato roktalents (più recente). [3] [60]
- **Archer / Full Quiver (#6): attacco arcieri o ira** — roktalents.com: Increases attack of archer units by 1/2/3%; gamesguideinfo.com: Max Lv. 3 Rage Increase After Launching Attack +3. Effetti di natura diversa con lo stesso numero; usato roktalents (più recente). [3] [47]
- **Skill / Naked Rage (#10): aumento o riduzione del danno da abilità** — roktalents.com: Increases skill damage dealt by 6%, but also increases skill damage taken by 6%; gamesguideinfo.com: Max Lv. 3 Skill Damage Dealt Decrease 6.0%. Allclash (Boudica, 2023) conferma il compromesso 'extra skill damage ... than the extra skill damage you take': usato roktalents. [3] [52] [26]
- **Mobility / Alacrity (#18): resistenza o aumento dei rallentamenti** — roktalents.com: 30% chance to resist enemy slow effects; gamesguideinfo.com: Chance to Increase Enemy Slow Effects 30.0%. Probabile etichetta errata su gamesguideinfo. [3] [54]
- **Nomi dei talenti diversi tra roktalents e gamesguideinfo (stesso effetto)** — Mobility #14 Hasty Departure: gamesguideinfo: 'Mighty Force'; Mobility #9 Swiftness: gamesguideinfo: 'Trophy Hunter'; Skill #19 Clarity: gamesguideinfo: 'Undying Fury'; Garrison #17 Know Thy Enemy: gamesguideinfo: 'Snare of Thorns'; Garrison/Versatility Nowhere To Turn: gamesguideinfo: 'Nowhere to Run'; Infantry #13 Fleet Of Foot: gamesguideinfo: 'Fleet of the Foot'; Integration #5 Defense Formation: gamesguideinfo: 'Defensive Formation'; Archer #18: roktalents scrive 'Phoenix-Tail Arrrows' (refuso), gamesguideinfo 'Phoenix Tail Arrows'. Etichette errate o varianti; il nome usato nel file è quello roktalents (allclash 2023 usa gli stessi nomi: Hasty Departure, Nowhere To Turn, Fleet of Foot). [3] [54] [52] [55]
- **Skill / Rejuvenate (#17): ira ripristinata per abilità** — roktalents.com: 20/40/60; allclash Sun Tzu (2023-10-20): 'you will get 60 rage each time a skill is used'; allclash Margaret (2023-10-23): 'Rejuvenate in the Support Tree grants 150 extra rage compared to the 50 rage commanders with the skill tree gain'. Usato 60 (roktalents + allclash Sun Tzu); il 50 di allclash Margaret è probabilmente un refuso. [3] [28] [43]
- **Peacekeeping / Insight: riduzione AP in % o in punti** — roktalents.com (Peacekeeping): -9% costo AP; roktalents.com (Versatility): -9 (senza %); gamesguideinfo.com: Action Point Cost Reduction +9; truppe_pve.json (KB): -9 costo AP. Le fonti non concordano sull'unità (percentuale vs punti fissi). Allclash: Insight "reduce the amount of action points required". Da verificare in gioco. [3] [56] [60] [57]
- **Numero di alberi: 15 (roktalents/gamesguideinfo) vs 18 (Zoe/hokbuild/rivelazioni ufficiali)** — roktalents.com (dati 2020): 15; gamesguideinfo.com: 15; zoe-rok.com / rok.hokbuild.com / Lilith (2023-2025): 15 + Engineering + Smite + Combo. Le fonti con alberi dettagliati sono anteriori all'introduzione di Engineering (2023), Smite (2024) e Combo (2025). [3] [9] [63] [10] [62]
- **Cheok Jun-Gyeong: terzo albero Attack o Smite** — roktalents.com (2023): Infantry / Versatility / Attack; rok.hokbuild.com (2026-02-06): Infantry / Versatility / Attack; zoe-rok.com (2026): Infantry / Versatility / Smite. Possibile rework dell'albero; non verificabile senza il gioco. [3] [63] [9]
- **Talenti degli alberi Engineering / Smite / Combo secondo rok.hokbuild.com** — hokbuild Gajah Mada (Engineering): Superior Engineering, Battering Ram, Siege Mastery, Ruthless Assault, ...; hokbuild Margaret (Engineering): Buckshot, Shattering Shot, Impairing Shot, Siege Training, ...; hokbuild Gonzalo (Engineering): Engineering Mastery, Ballistics, Quick Construction, ...; hokbuild Arthur (Combo): Combo Mastery, Quick Strike, Relentless Assault; rivelazione ufficiale Lilith (Combo): Blizzard of Blows, No Quarter, Force of Nature, Iron and Steel; hokbuild Bai Qi (Smite): Clarity, Rejuvenate, Burning Blood, Feral Nature (nomi dell'albero Skill). Elenchi incoerenti tra articoli dello stesso sito e smentiti dalla fonte ufficiale per Combo: scartati come dati. [63] [10]
- **Trophy Hunter: quantità di Resource Pack** — roktalents.com: 15 x Resource Pack C lv.1 al massimo (5/10/15); gamesguideinfo.com: Barbarian Default Resource Pack C Amount +15; allclash.com (Lohar/Belisarius 2023): "an additional resource pack with every defeated barbarian". Il valore numerico concorda (15) ma allclash parla di un pacco per barbaro: il "15" potrebbe essere una probabilità o una quantità; da verificare in gioco. [3] [56] [25]

## 7. Lacune

- Albero Engineering: noto un solo nome di talento (Forbearance, senza valori); nomi, punti, effetti e prerequisiti degli altri talenti non trovati in nessuna fonte testuale raggiungibile (riseofkingdomsguides/allclash mostrano solo immagini o paywall; rok.guide archiviato si ferma al 2023; fandom non ha pagine talenti). Struttura (20 nodi, 50 punti) solo letta da screenshot.
- Albero Smite: nomi, punti, effetti e prerequisiti non trovati (stesse ragioni); noto solo che il nodo finale vale 5 punti e che conviene andare 'all-in'.
- Albero Combo: documentati 4 talenti principali (fonte ufficiale); mancano nomi/effetti degli altri 5 talenti principali, valori per livello, prerequisiti e tier.
- Valori per livello (non solo al massimo) dei talenti Combo non pubblicati.
- Bonus punti a 5 stelle: il valore +5 è derivato per differenza (74-59-10), non letto da una fonte.
- Costo ufficiale del reset talenti (gemme/oggetto) non confermato da fonte ufficiale: solo post Reddit (1000 gemme; 300k crediti alleanza) e fandom (oggetto da Mysterious Merchant/Shop).
- Eventuali ribilanciamenti dei 15 alberi dopo il 2020: roktalents (ultima modifica dati 2020-12-03) è la fonte più recente con i valori completi; allclash (ottobre 2023) conferma i valori citati (Rejuvenate 150/60, Elixir 9%, Thoroughbreds 9%, Domination 15%, Loose Formation 9%, Hasty Departure 60%, Superior Tools 25%, The More The Better 6%), ma non è stato possibile verificare tutti i nodi sul gioco del 2026.
- Build smite e combo: ordine di acquisto non documentato (combo) e punti per talento non documentati (smite).
- Punti esatti di alcune build allclash sono solo nelle immagini: i punti dei nodi di percorso sono derivati dal grafo (vedi derivation_note).
- Build 'guarnigione' Charles Martel: la fonte dichiara Garrison 17 + Defense 47 + Infantry 13 = 77 (>74): incoerenza non risolvibile senza l'immagine.

## 8. Fonti non raggiungibili

- https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/: HTTP 500 (pagina anti-bot) sia con curl sia con WebFetch
- https://www.rok.guide/: HTTP 503 captcha SiteGround (lette solo copie Wayback Machine fino al 2023)
- https://riseofkingdoms.fandom.com/wiki/Talents: HTTP 403 Cloudflare (lette copie Wayback di Commander_Guide e Items/Talent_Reset)
- https://riseofkingdoms.wiki.gg/: HTTP 403 Cloudflare, nessuna copia in Wayback
- https://www.allclash.com/wp-json/wp/v2/posts: HTTP 403 (API e curl); pagine articolo lette con WebFetch o dalla Wayback Machine
- https://riseofkingdomsguides.com/talent-tree/ (curl): verifica anti-bot ALTCHA con curl; letta con WebFetch
- https://www.reddit.com/r/RiseofKingdoms/ (live e API): HTTP 403 / pagina di blocco; lette copie Wayback Machine
- https://i.redd.it/ (immagini originali): HTTP 403; usate le anteprime firmate preview.redd.it
- https://www.gamesguideinfo.com/rise-of-kingdoms/overview/commander-talent-tree: HTTP 404 (pagine per albero raggiungibili via ID 830000023-830000037; Defense 830000037 senza dati)
- https://rok.hokbuild.com/talents/: HTTP 404 (dati letti dalle API WordPress /wp-json/wp/v2/posts)
- https://api.github.com/repos/sho-87/rok-talents: API GitHub non abilitata nella sessione (usato git clone anonimo)

## 9. Fonti

1. riseofkingdomsguides.com — https://riseofkingdomsguides.com/talent-tree/ (data pagina: 2026-08 (titolo: "Rise Of Kingdoms Talent Tree Builds August 2026"); consultata 2026-09-28)
2. rok.guide (copia Wayback Machine) — https://web.archive.org/web/20190922034823/https://rok.guide/talent-guide/ (data pagina: 2019-09-19; consultata 2026-09-28)
3. roktalents.com — https://roktalents.com/static/js/main.68410830.chunk.js (data pagina: 2020-12-03 / 2023-01-04; consultata 2026-09-28)
4. riseofkingdoms.fandom.com (copia Wayback Machine) — https://web.archive.org/web/20200921/https://riseofkingdoms.fandom.com/wiki/Commander_Guide (data pagina: n.d.; consultata 2026-09-28)
5. reddit.com (copia Wayback 2025-02-25) — https://www.reddit.com/r/RiseofKingdoms/comments/1h33chj/maxed_sun_tzu_didnt_get_10_bonus_talent_points/ (data pagina: 2024-11-30; consultata 2026-09-28)
6. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/how-to-level-up-commander-in-rise-of-kingdoms-as-fast-as-possible/ (data pagina: 2021-01 (archiviata); consultata 2026-09-28)
7. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-skill/790001347-Superior-Tools (data pagina: n.d.; consultata 2026-09-28)
8. allclash.com / allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-cleopatra-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2026-03-03 / 2023-10-24; consultata 2026-09-28)
9. zoe-rok.com — https://zoe-rok.com/commanders (data pagina: 2026 (schede comandanti aggiornate fino ad aprile 2026); consultata 2026-09-28)
10. reddit.com (copia Wayback 2025-01-03; immagini ufficiali Lilith su preview.redd.it) — https://www.reddit.com/r/RiseofKingdoms/comments/1hsjnnj/king_arthur_skills_revealed_combo_talent_tree/ (data pagina: 2025-01-03; consultata 2026-09-28)
11. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-babur-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/ (data pagina: 2023-10-23; consultata 2026-09-28)
12. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/overview/commander-grades (data pagina: n.d.; consultata 2026-09-28)
13. riseofkingdomsguides.com — https://riseofkingdomsguides.com/farming-gathering-guide/ (data pagina: 2026-01-02; consultata 2026-09-28)
14. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/guide/commanders (data pagina: n.d.; consultata 2026-09-28)
15. riseofkingdoms.fandom.com (copia Wayback Machine) — https://web.archive.org/web/20220708/https://riseofkingdoms.fandom.com/wiki/Items/Talent_Reset (data pagina: n.d.; consultata 2026-09-28)
16. reddit.com (copia Wayback) — https://www.reddit.com/r/RiseofKingdoms/comments/t5sdd1/how_can_i_reset_talent_tree_without_spending_1000/ (data pagina: 2022-03-03; consultata 2026-09-28)
17. reddit.com (copia Wayback) — https://www.reddit.com/r/RiseofKingdoms/comments/z1lw70/ive_spent_300k_alliance_credits_on_talent_reset/ (data pagina: 2022-11-22; consultata 2026-09-28)
18. reddit.com (copia Wayback) — https://www.reddit.com/r/RiseofKingdoms/comments/b3zmec/psa_talent_tree_preset/ (data pagina: 2019-03-22; consultata 2026-09-28)
19. riseofkingdomsguides.com (patch notes, copia Wayback Machine) — https://riseofkingdomsguides.com/rise-of-kingdoms-1-0-78-live-loong-and-prosper-update/ (data pagina: 2024-01-09; consultata 2026-09-28)
20. riseofkingdomsguides.com (patch notes, copia Wayback Machine) — https://riseofkingdomsguides.com/rise-of-kingdoms-1-0-81-unearthing-history-update/ (data pagina: 2024-04-16; consultata 2026-09-28)
21. riseofkingdomsguides.com (patch notes, copia Wayback Machine) — https://riseofkingdomsguides.com/rise-of-kingdoms-1-0-83-eternal-city-update/ (data pagina: 2024-06-21; consultata 2026-09-28)
22. riseofkingdomsguides.com (patch notes, copia Wayback Machine) — https://riseofkingdomsguides.com/rise-of-kingdoms-1-0-88-giving-thanks-update/ (data pagina: 2024-11-25; consultata 2026-09-28)
23. riseofkingdomsguides.com (patch notes, copia Wayback Machine) — https://riseofkingdomsguides.com/rise-of-kingdoms-1-0-90-return-of-the-king-update/ (data pagina: 2025-01-05; consultata 2026-09-28)
24. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/the-only-rise-of-kingdoms-gathering-guide-you-really-need/ (data pagina: 2021-01-21; consultata 2026-09-28)
25. allclash.com / allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-lohar-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2026-03-03 / 2023-10-25; consultata 2026-09-28)
26. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-boudica-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-25; consultata 2026-09-28)
27. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-minamoto-yoshitsune-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-20; consultata 2026-09-28)
28. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-sun-tzu-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-20; consultata 2026-09-28)
29. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-richard-i-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-20; consultata 2026-09-28)
30. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-charles-martel-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-20; consultata 2026-09-28)
31. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-guan-yu-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-20; consultata 2026-09-28)
32. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-julius-caesar-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-24; consultata 2026-09-28)
33. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-mehmed-ii-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-24; consultata 2026-09-28)
34. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-frederick-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-24; consultata 2026-09-28)
35. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-cao-cao-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-20; consultata 2026-09-28)
36. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-belisarius-builds-talent-tree-skill-order-best-pairing-in-rise-of-kingdoms/ (data pagina: 2023-10-20; consultata 2026-09-28)
37. riseofkingdomsguides.com — https://riseofkingdomsguides.com/king-arthur-talent-tree-build-and-guide-rise-of-kingdoms/ (data pagina: 2026-01-02; consultata 2026-09-28)
38. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-arthur-paragon-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/ (data pagina: 2025-02-03; consultata 2026-09-28)
39. allclash.com (copia Wayback 2024-09-13) — https://www.allclash.com/best-william-wallace-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/ (data pagina: 2024-08-02; consultata 2026-09-28)
40. riseofkingdomsguides.com — https://riseofkingdomsguides.com/william-wallace-talent-tree-build-and-guide/ (data pagina: 2026-01-02; consultata 2026-09-28)
41. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-bai-qi-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/ (data pagina: 2025-04-14; consultata 2026-09-28)
42. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-tokugawa-ieyasu-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/ (data pagina: 2025-04-14; consultata 2026-09-28)
43. allclash.com (copia Wayback Machine, snapshot più recente) — https://www.allclash.com/best-margaret-builds-talents-skill-order-pairing-equipment-in-rise-of-kingdoms/ (data pagina: 2023-10-23; consultata 2026-09-28)
44. allclash.com (immagine) — https://www.allclash.com/wp-content/uploads/2023/04/rok-babur-best-talent-build.jpg (data pagina: 2023-04; consultata 2026-09-28)
45. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000023-Infantry (data pagina: n.d.; consultata 2026-09-28)
46. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000026-Cavalry (data pagina: n.d.; consultata 2026-09-28)
47. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000030-Archer (data pagina: n.d.; consultata 2026-09-28)
48. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000034-Leadership (data pagina: n.d.; consultata 2026-09-28)
49. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000028-Integration (data pagina: n.d.; consultata 2026-09-28)
50. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000025-Attack (data pagina: n.d.; consultata 2026-09-28)
51. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000037-Defense (data pagina: n.d.; consultata 2026-09-28)
52. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000027-Skill (data pagina: n.d.; consultata 2026-09-28)
53. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000036-Support (data pagina: n.d.; consultata 2026-09-28)
54. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000033-Mobility (data pagina: n.d.; consultata 2026-09-28)
55. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000024-Garrison (data pagina: n.d.; consultata 2026-09-28)
56. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000032-Peacekeeping (data pagina: n.d.; consultata 2026-09-28)
57. military_advisor KB (truppe_pve.json) — file:data/truppe_pve.json (data pagina: 2026-09-27; consultata 2026-09-28)
58. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000029-Gathering (data pagina: n.d.; consultata 2026-09-28)
59. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000035-Conquering (data pagina: n.d.; consultata 2026-09-28)
60. gamesguideinfo.com — https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000031-Versatility (data pagina: n.d.; consultata 2026-09-28)
61. rok.guide (copia Wayback Machine) — https://web.archive.org/web/20230313/https://www.rok.guide/update-1-0-67-spring-once-more/ (data pagina: 2023-03-13; consultata 2026-09-28)
62. rok.guide (copia Wayback Machine) — https://web.archive.org/web/20230413/https://www.rok.guide/update-1-0-68-shifting-sands/ (data pagina: 2023-04-13; consultata 2026-09-28)
63. rok.hokbuild.com — https://rok.hokbuild.com/wp-json/wp/v2/posts (data pagina: 2025-10-01..2026-09-02; consultata 2026-09-28)
64. riseofkingdomsguides.com — https://riseofkingdomsguides.com/narses-talent-tree-build-and-guide-rise-of-kingdoms/ (data pagina: 2026-01-02; consultata 2026-09-28)
