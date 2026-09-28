# Consigliere militare — MECCANICHE DI COMBATTIMENTO E FORMULE (settembre 2026)

Ricerca del **28/09/2026**. Dati strutturati per il bot: `data/fragments/meccaniche.json` (danno, rage, nuove meccaniche, feriti/morti, counter, buff esterni, movimento, regole per il bot, fonti, conflitti, lacune).
I nomi tecnici sono in inglese. Accanto a ogni affermazione trovi la fonte e la data della pagina.

**Come leggere le etichette**
- **Ufficiale**: patch notes e Q&A degli sviluppatori sul forum Lilith, letti dall'API pubblica del forum. Sono 832 post dell'account "Rise of Kingdoms", da luglio 2020 a giugno 2026.
- **Guida 2026**: riseofkingdomshandbook, riseofkingdomsguides, heaven-guardian, ldshop, theriagames, BlueStacks.
- **Community**: test empirici pubblicati su bilibili (in cinese) tra il 2020 e il 2023. Metodo dichiarato, ma nessuna conferma ufficiale.
- **Derivazione nostra**: calcoli fatti da me sulle fonti. Vanno presi come stime.

> **Vincoli del bot, sempre validi:** attacchi, rally, scout, teleport e messaggi in chat del regno richiedono la **conferma dell'utente**. Le **gemme non si spendono mai**. L'automazione di terze parti è contro i termini di servizio (vedi §8, regola mech-16).

---

## 1. Come si calcola il danno

### 1.1 Il ciclo del combattimento
- Il combattimento avanza a **turni di 1 secondo**. In ogni turno ogni armata fa **1 attacco base** sul suo bersaglio e **contrattacca tutte** le armate che la colpiscono, senza limite ([BlueStacks, agg. 11/12/2024](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-combat-guide-en.html)).
- Con due comandanti la skill del **primario parte prima**, subito seguita da quella del secondario, nello stesso turno ([BlueStacks](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-combat-guide-en.html)).
- A rage piena la truppa passa un turno in "preparazione" e lancia la skill nel turno successivo, insieme all'attacco base. **Il danno della skill non provoca contrattacco.** Tutto il danno di un turno è calcolato sulle unità presenti all'inizio del turno ([community, bilibili 07/02/2022](https://www.bilibili.com/read/cv15160006)).
- **Ufficiale:** dal 1.0.76 (nov 2023) il termine "normal damage" comprende **sia l'attacco base sia il contrattacco** ([patch 1.0.76](https://forum-global.lilithgame.com/post/1589003)).

### 1.2 Formula dell'attacco normale (community)
```
Danno = k · A_s / (D_e · H_e) · √N_s · (1 + (N_s + N_e)/950.000) · (1 + E_s) · (1 − E_e) · (1 + Cou)
k ≈ 192,54   s = propria truppa, e = nemico
N = unità a inizio turno   A/D/H = Attack/Defense/Health con i bonus
E_s = bonus al danno normale   E_e = riduzione del danno del nemico   Cou = counter (+5%)
```
Fonte: [omegaaa_, bilibili 07/02/2022](https://www.bilibili.com/read/cv15160006). Un secondo autore arriva a una forma equivalente: Damage = DF · √N · A / D · …, con **perdite = danno / Health**. Il DF dell'attacco base è **200 sia per l'attacco sia per il contrattacco**, e il termine di scala vale **circa +1% ogni 10.000 unità totali in campo** ([bilibili 21/03/2022](https://www.bilibili.com/read/cv15768684), [22/03/2022](https://www.bilibili.com/read/cv15784839)).

Cosa ne segue:
- Il danno cresce con la **radice quadrata** delle unità. Nel test, 1.000 unità infliggono 20 danni e 10.000 ne infliggono 61. **Derivazione nostra:** passare da 100k a 200k unità contro 100k porta il danno a circa **1,54 volte**.
- Il danno cresce **in modo lineare con l'Attack**. Le unità perse sono proporzionali a **1/(Defense × Health)**: conta il prodotto, non la somma.
- La **Health non è una "vita che si azzera"**: funziona come stat di riduzione delle perdite. Defense e Health vengono mediate tra i tipi di unità presenti nella truppa.
- Un bonus "normal damage" vale sia per l'attacco sia per il contrattacco. Un bonus "counterattack damage" vale solo per il contrattacco ([bilibili 21/03/2022](https://www.bilibili.com/read/cv15768684)).
- **Derivazione nostra:** 192,54 / 0,96 ≈ 200. L'attacco base equivale quindi a una skill con DF 200, in linea con il termine ufficiale *"basic attack Damage Factor"* ([patch 1.1.07, 30/04/2026](https://forum-global.lilithgame.com/post/2232581)).

### 1.3 Danno da skill
- La formula è Danno_skill = **0,96 · DF** · (stessa scala dell'attacco normale). Il danno da skill **non riceve il counter**, e i bonus "skill damage" si applicano per intero: nel test, Sun Tzu secondario dà esattamente +20% ([bilibili 07/02/2022](https://www.bilibili.com/read/cv15160006)).
- Nelle skill ad area ogni bersaglio aggiuntivo toglie di solito il **15%** del danno (alcune skill arrivano al massimo al 50%). Alcune skill fanno **metà danno se il comandante è secondario**: Guan Yu, Edward of Woodstock, Honda Tadakatsu (testi skill in KB, da [riseofkingdomsguides](https://riseofkingdomsguides.com/talent-tree/guan-yu/)).

### 1.4 Tipi di danno nel 2026
| Tipo | Cosa lo potenzia | Note |
|---|---|---|
| normal (base + contrattacco) | Attack, "normal damage", counter | L'unico che riceve il counter (+5%) |
| skill | "skill damage", Wedge / Wedge II (+12%) | Un bonus skill **non** migliora smite, combo o danno normale ([handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-civilization)) |
| smite | bonus del danno **normale**, Pincer (+10%, +12% dal Pincer II), talento Enhanced Smite (+6%) | Regola dal testo di Bai Qi |
| combo | Delta (+10%, [1.0.85](https://forum-global.lilithgame.com/post/1752431)), talento Colossus (+6%) | Più colpi in sequenza |
| true | effetti come Military Sage | Categoria a sé: il fix [1.0.93](https://forum-global.lilithgame.com/post/1994801) impedisce all'iscrizione Crazed di attivarsi con il true damage |

**Ufficiale, 1.1.04** (patch notes del 24/02/2026, in vigore dal 27/02/2026, Season 2 e successive): ogni riduzione "skill damage taken" ora vale anche contro **combo e smite**. Sono stati ritoccati anche questi talenti: Martial Mastery (+6% danno normale, −3% skill/combo/smite), Naked Rage (+6% skill, ma +6% di danno subito) e Loose Formation / Saving Cross (−9%) ([patch 1.1.04](https://forum-global.lilithgame.com/post/2213663)).

### 1.5 Come si sommano i bonus
- Le **percentuali dello stesso attributo si sommano** (ricerca, alleanza, VIP, equipaggiamento…). Categorie diverse (bonus al danno, riduzione del nemico, counter, bonus di mappa) **si moltiplicano** tra loro ([bilibili 2022](https://www.bilibili.com/read/cv15768684)).
- **Derivazione nostra:** aggiungere +x% a un attributo che ha già +B% rende x/(1+B). Per esempio, +10% di Attack su un +100% già attivo vale **+5% di danno reale**.
- Per la sopravvivenza conta Defense × Health. Conviene alzare l'attributo con il moltiplicatore totale più basso: +a% Health vale più di +b% Defense se a/(1+H) > b/(1+D). Le fonti fisse danno circa **+92% Attack, +92% Defense e +47% Health**, quindi la Health è più rara ([bilibili 2022](https://www.bilibili.com/read/cv15160006)).
- Due holy site dello stesso tipo **non si sommano** ([theriagames](https://theriagames.com/guide/rise-of-kingdoms-shrines-guide/)). Titoli e rune si sommano agli altri bonus ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-kingdom-titles-guide)).

### 1.6 Tetti e limiti
- **Ufficiale:** nelle battaglie di città c'è **un limite al danno normale e al contrattacco per turno** su entrambi i lati, pensato per evitare che l'attaccante venga annientato in un turno. Questo penalizza i difensori che vivono di danno normale. Il valore non è pubblicato ([Q&A sviluppatori, 11/11/2022](https://forum-global.lilithgame.com/post/1402281)).
- Rage: al massimo **220 per turno** (community, [bilibili 10/05/2022](https://www.bilibili.com/read/cv16537956)).
- Feriti gravi negli scontri sul campo: almeno il **10%** delle perdite (community, [bilibili 2022-23](https://www.bilibili.com/read/cv17010914)).
- Honing degli armamenti: +3,5% agli attributi e +2,0% all damage al massimo ([1.1.03](https://forum-global.lilithgame.com/post/2197960)).
- Non ho trovato nessun tetto generale ai bonus di Attack/Defense/Health.

### 1.7 T4 contro T5 e potenza
| | Attack | Defense | Health | Potenza/unità | Cura per unità (fanteria) |
|---|---|---|---|---|---|
| T4 Long Swordsman | 192 | 192 | 187 | 4 | 120 cibo, 120 legno, 8 oro |
| T5 Royal Guard | 220 | 212 | 216 | 10 | 320 cibo, 320 legno, 160 oro |

Fonti: KB `truppe_pve.json`, da [riseofkingdomsguides](https://riseofkingdomsguides.com/best-special-units-in-rise-of-kingdoms/) e [onechilledgamer](https://onechilledgamer.com/rise-of-kingdoms-troops-guide/).

**Derivazione nostra:** a parità di numero, un T5 fa circa **+14,6% di danno** e perde circa **22% di unità in meno**, per uno scambio di circa **1,46 volte**. Costa però 2,5 volte in potenza e 20 volte in oro per curarlo. Per questo le guide consigliano di tenere riserve di T4 ([heaven-guardian, 02/09/2026](https://heaven-guardian.com/rise-of-kingdoms-best-troops-training-guide/)).
- La cura recupera **meno unità di tier alto**: unità curate = cura / Health base del tipo. Nelle truppe miste, skill e cure agiscono prima sui tier bassi ([bilibili 2022](https://www.bilibili.com/read/cv15768684)).
- La **potenza non misura la forza**. Serve lo scout per vedere tier, skill e rinforzi ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-game-mechanics-hub)).

---

## 2. Rage
- **Soglia standard: 1000.** Eccezioni nei testi skill: Sun Tzu Prime 900, Gorgo 900, Genghis Khan 950 (valore riportato in KB), Edward of Woodstock 1350 (dopo la skill perde 300 rage), Honda Tadakatsu 1350 (KB, da riseofkingdomsguides).
- **Generazione** (community, [bilibili 10/05/2022](https://www.bilibili.com/read/cv16537956)):
  - in un 1v1 senza bonus si accumulano circa **102 rage per turno**: **~86 dall'attacco base** e **~16 dal contrattacco**;
  - +10 rage se il proprio attacco fa meno danno del contrattacco nemico;
  - al massimo 220 rage per turno;
  - contro i barbari il primo turno sembra non dare rage.
  
  Una guida del 2020 parlava di "100 per attacco" ([bilibili](https://www.bilibili.com/read/cv7922133)).
- **Derivazione nostra:** una skill da 1000 parte circa **ogni 10 turni (~10 s)**, dopo circa 9 turni con +9 rage per attacco o con una soglia di 900.
- **Talenti:** Undying Fury e Razor Sharp +9 per attacco. Hidden Wrath e Burning Blood +6 quando si viene attaccati. Desperate Elegy +25 sotto il 30% di unità. Rejuvenate +60 dopo ogni skill. Feral Nature 10% di probabilità di +100. No Quarter +15 per ogni combo (KB `talenti.json`, dati di [roktalents](https://roktalents.com/static/js/main.68410830.chunk.js)).
- **Skill e oggetti:** Qin Shi Huang +500 rage all'inizio dello scontro. Sun Tzu Prime +20 per ogni truppa colpita dal true damage. Iscrizione Embattled: 10% di probabilità di +50 ([1.1.04](https://forum-global.lilithgame.com/post/2213663)).
- **Riduzione della rage nemica:**
  - Hermann: −100 rage e Silence;
  - Amanitore e Belisarius Prime: rage tolta ogni secondo;
  - Deception: +200 rage richiesta;
  - una skill 1.0.94: +200 rage richiesta per 5 s ([1.0.94](https://forum-global.lilithgame.com/post/2030530)).
- **Ufficiale 1.0.96** (luglio 2025): *"Troops can no longer gain Rage while out of combat."* ([patch](https://forum-global.lilithgame.com/post/2081453)).
- **Ordine delle skill:** primario prima, poi secondario. **Solo talenti ed equipaggiamento del primario** valgono per la marcia ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-commanders-guide-hub)). Il Silence blocca le skill attive; Amanitore e Attila (expertise) ne sono immuni.

---

## 3. Nuove meccaniche
- **Smite**: usa i bonus del danno **normale**, non quelli di skill damage. Si potenzia con Pincer, Enhanced Smite e Bai Qi (+5% ogni 10% di unità perse, fino al 30%).
- **Combo**: colpi multipli con bonus propri (Delta, Colossus). Lo contrastano Achilles (−10/15% di skill, combo e contrattacco subiti), Hector (−10% se la truppa ha almeno 2 tipi di unità) e le riduzioni del 1.1.04.
- **Pierce** (Alp Arslan): 1 stack ogni 3 s, al massimo 3 stack. I bersagli colpiti subiscono danno ogni secondo. Non va confuso con *Iron Pierces Bronze* di Qin Shi Huang, che converte la rage in danno diretto.
- **True damage**: danno fisso. Esempi: Military Sage (20%, o 30% con expertise, dello smite su 2 truppe vicine), Choe Yeong (80% della cura), Shajar al-Durr. Non si sa come interagisca con Defense, Health e riduzioni (è una lacuna).
- **Sundered** (Achilles): +5% di danno da Pelian Spear per stack, fino a 3 stack, per 10 s.
- **Poison**: stack di danno nel tempo.
  - Hermann Prime applica 2 stack per colpo; ogni 25 stack rilancia la sua skill; la sua truppa subisce −1% di danno per ogni stack sul nemico.
  - Tomyris consuma gli stack e li trasforma in danno immediato.
  - "Cleanse" rimuove i debuff, "dispel" rimuove i buff (terminologia [1.0.88](https://forum-global.lilithgame.com/post/1835007)).
- **Malice** (Bai Qi, contro truppe sul campo):
  - gli stack arrivano entrando in battaglia, per ogni 10% di unità perse e per ogni skill;
  - quando gli stack superano la % di unità rimaste al nemico, Bai Qi spende 10 stack per uno smite (DF 300) e ottiene +10% di feriti gravi e +20% di rage per 1 s;
  - i barbari sconfitti contano come severely wounded ([1.0.95](https://forum-global.lilithgame.com/post/2056756)).
- **Military Sage** (Sun Tzu Prime, rage 900): true damage a ventaglio (1 volta al secondo), +10% smite, attacchi base con 50% di probabilità di smite DF 400, +20 rage per ogni truppa colpita.
- **Shield / Mighty Shield**: assorbe danno per 2-5 s. Il suo valore dipende solo dalla radice delle unità, e solo la **Defense** (non la Health) aumenta quanto danno regge (community). Shapur blocca gli scudi del nemico per 2 s se questo ha meno di 500 rage.
- **Heal / Mighty Healing**: rimette in campo unità *slightly wounded*. Dipende dalla radice delle unità e non dagli attributi.
- **Controllo**: Silence, Disarm, Slow, Ambushed.

Fonti: testi skill nella KB (`commanders.json`, da [riseofkingdomsguides](https://riseofkingdomsguides.com/talent-tree/sun-tzu-prime/) e altre), [community bilibili](https://www.bilibili.com/read/cv15768684), patch ufficiali citate sopra.

---

## 4. Feriti e morti
Le perdite si dividono in tre esiti:
- ***slightly wounded***: tornano da soli;
- ***severely wounded***: vanno in ospedale se c'è posto;
- ***dead***: persi per sempre.

**Se l'ospedale è pieno, l'eccedenza muore sempre** ([theriagames, 09/02/2025](https://theriagames.com/guide/rise-of-kingdoms-hospital-guide/), [riseofkingdomsguides](https://riseofkingdomsguides.com/hospital/), [handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-healing-hospital-guide)).

| Attività | Cosa succede ai severely wounded | Fonte |
|---|---|---|
| Campo aperto (attacco o difesa) | Ospedale; muoiono solo se l'ospedale è pieno | theriagames; sviluppatori 2020: chi *non* attacca una città o uno stronghold viene solo ferito ([post](https://forum-global.lilithgame.com/post/1014483)) |
| Difesa della **propria** città | Tutti in ospedale | theriagames |
| **Rinforzi** a città o strutture alleate | **50% muore** | theriagames + fix ufficiale [1.1.02](https://forum-global.lilithgame.com/post/2179486) sui morti dei rinforzi in città |
| Attacco a **città nemiche** | Muoiono. theriagames dice tutti, riseofkingdomsguides una parte (**conflitto**) | [rkg](https://riseofkingdomsguides.com/rise-of-kingdoms-attacking-cities-and-flags-guide/); il talento Tear of Blessing riduce proprio questi morti |
| Attacco a **fortezze** / **flag** d'alleanza | Fortezze: tutti morti. Flag: una parte (rkg); theriagames dice tutti | rkg, theriagames |
| Shrine, Pass livello 2 | Sopravvive metà | theriagames |
| Lost Temple, Pass livello 3 | Tutti morti | theriagames |
| Rally | Come l'obiettivo del rally; **nessuna cura finché il rally non finisce** | theriagames, rkg |
| Ark of Osiris | Nessun morto (si curano con speedup); nel campo non si curano i severely wounded | [handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-ark-of-osiris-guide), [1.0.67](https://forum-global.lilithgame.com/post/1443512) |
| Expedition, Sunset Canyon | Truppe simulate, niente morti | [handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-expedition-guide) |
| Supreme Strife (2025) | Una parte dei severely wounded muore; a fine partita la maggior parte dei morti resuscita | [1.0.96](https://forum-global.lilithgame.com/post/2081453) |
| KvK / Lost Kingdom | Stesse regole per attività. Ospedale ×2. La **Hall of Heroes** restituisce a fine stagione una parte dei morti (tasso non pubblicato) e dal 1.0.89 parte delle risorse spese in cure | [theriagames](https://theriagames.com/guide/rise-of-kingdoms-lost-kingdom-guide/), [1.0.94](https://forum-global.lilithgame.com/post/2030530), [1.0.89](https://forum-global.lilithgame.com/post/1868790) |
| Barbari e forti | Nessuna regola esplicita. Il handbook dice solo che i forti non causano perdite permanenti significative | [handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-barbarian-forts-guide) |

**Rapporto tra feriti gravi e perdite** (community, [bilibili 2022-23](https://www.bilibili.com/read/cv17010914)):
- non scende sotto il **10%**;
- è più basso con il danno da skill;
- è più alto per chi infligge danno in vantaggio;
- la Health non lo cambia; la **Defense riduce** il proprio rapporto.

La formula esatta non è stata risolta.

**Cosa riduce le perdite:**
- **Ospedali**: 4 ospedali da 75.000 posti al livello 25, 300.000 in tutto ([Lyceum](https://riseofkingdomsguides.com/lyceum-of-wisdom-rok-answers/)). Bonus di capacità da VIP, Korea e Byzantium (+15%), Crystal Tech (+30%) e KvK (×2).
- **Talenti**:
  - Tear of Blessing: −9/10% di morti quando si attaccano città;
  - Ares' Blessing: −10% di severely wounded;
  - Tourniquet: −6% di severely wounded;
  - Curing Chant: cura dopo i barbari;
  - Know Thy Enemy: guarnigione circondata.
  
  Fonti: [gamesguideinfo](https://www.gamesguideinfo.com/rise-of-kingdoms/boost-type/160001806-Convert-Severely-Wounded-to-Slightly-Wounded-When-in-Battle), KB `talenti.json`.
- **Skill**: Gaius Marius +5% di slightly wounded; cure in battaglia.
- **Strategie di stagione**: Safe Return (−8% di severely wounded, fino a 500.000 unità, non tocca i morti), Frugality e Medical Skills ([1.0.77](https://forum-global.lilithgame.com/post/1599092)). Recovery Potions in Heroic Anthem ([1.1.04](https://forum-global.lilithgame.com/post/2213663)).
- **Come si gioca**: spazio libero e risorse di cura prima di combattere, ritirarsi in tempo, cure a lotti con l'aiuto dell'alleanza.

---

## 5. Counter, truppe miste, bersagli, surrounded e swarm
- **Triangolo**: fanteria > cavalleria > arcieri > fanteria. L'assedio è fuori dal triangolo e contrasta le Watchtower ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-troop-types-and-counters), [rok.guide archiviato](https://web.archive.org/web/20240530185650/https://www.rok.guide/troops/)).
- **Quanto vale il counter:** **+5% fisso**, solo sul danno normale. **Le skill ignorano il counter** (community, [bilibili 2022](https://www.bilibili.com/read/cv15160006)). I talenti Iron Spear, Halberd e Thumb Ring aggiungono **+9%** contro il tipo contrastato. **Derivazione nostra:** il counter pesa poco rispetto a skill e attributi, ma decide gli scontri "in salita" delle marce che vivono di danno normale.
- **Ranged e melee:** dal sistema Formation esistono buff validi solo a distanza ([1.0.75](https://forum-global.lilithgame.com/post/1578327)). La King skill **Inspire** riduce il danno ranged subito dalle truppe melee ([1.0.88](https://forum-global.lilithgame.com/post/1835007), [1.1.01](https://forum-global.lilithgame.com/post/2161435)).
- **Truppe miste:**
  - Defense e Health sono mediate tra i tipi;
  - la velocità è quella dell'unità più lenta;
  - molte skill richiedono "solo unità di un tipo": Qin Shi Huang, Genghis Khan, Byeolmuban;
  - bonus per 3 o più tipi con Armed/Armored To The Teeth (+3/4%);
  - nei rally mandare **solo il tipo richiesto** dal capitano ([ldshop, 22/09/2026](https://www.ldshop.gg/blog/rise-of-kingdoms/kvk-defense-guide.html)).
- **Bersagli:**
  - 1 attacco base per turno e contrattacco verso tutti;
  - in **Attack March** si dà priorità ai nemici vicini e non ci si fa attirare dietro le linee ([1.0.91](https://forum-global.lilithgame.com/post/1935973));
  - il focus fire ha un angolo di apertura più stretto ([1.1.01](https://forum-global.lilithgame.com/post/2161435));
  - nell'Auto-Peacekeeping riceve il danno per prima la truppa con più unità ([1.1.07](https://forum-global.lilithgame.com/post/2232581)).
- **Surrounded:** una truppa ingaggiata da più truppe nemiche. Le skill contano "il numero di truppe che la circondano": William I fino a 5, Pakal II fino a 6, Harald fino a 10.
  - Chi sta attaccando un bersaglio circondato ne approfitta: Norman Conquest di William I, Deception di Belisarius Prime.
  - Chi è circondato ha effetti difensivi con Mulan (−5% di danno e rage tolta all'attaccante), Pakal II (−5% per ogni truppa nemica) ed Harald (+2% di contrattacco per ogni truppa nemica).
  - **Ambushed** (Dido) toglie gli effetti legati all'essere circondati ([testi di gioco su rokstats](https://app.rokstats.online/commanders/william-i)).
  - Non si sa quante truppe servano per essere "surrounded" (è una lacuna).
- **Swarm:** più marce su un solo bersaglio. Il bersaglio contrattacca tutti e guadagna rage (~16 per contrattacco), ma subisce molto più danno.
  - La coppia ufficiale William I + Nevsky: *"Team up with your allies to swarm hapless stragglers"* ([testo di gioco](https://app.rokstats.online/commanders/william-i)).
  - ldshop parla di strutture attaccate da "10+ marce" e di marce circondate da "12+" nemici ([22/09/2026](https://www.ldshop.gg/blog/rise-of-kingdoms/kvk-defense-guide.html)).

---

## 6. Buff esterni: quanto pesano

| Fonte | Valori tipici (massimi) | Note / fonte |
|---|---|---|
| **Ricerca militare** (Accademia) | Per tipo di truppa: Attack +70% (10+15+20+25), Defense +70%, Health +40% (Herbal Medicine 15 + Medical Corps 25), March Speed +30% | [gamesguideinfo](https://www.gamesguideinfo.com/rise-of-kingdoms/research-category/130000105-Military) |
| **Tecnologia d'alleanza** | Archer Attack II +10%, Cavalry Defense I +5%. Altri rami con lo stesso schema, non verificati | Fandom archiviato ([II](https://web.archive.org/web/20200920054932/https://riseofkingdoms.fandom.com/wiki/Alliance_Technology/Archer_Attack_II), [I](https://web.archive.org/web/20200921003236/https://riseofkingdoms.fandom.com/wiki/Alliance_Technology/Cavalry_Defense_I)) |
| **VIP** | +5% Attack (dal VIP 11), Defense (12), Health (13), capacità (14), March Speed (15). VIP 19: +5% Attack e +5% addestramento | Tabella storica di [gamesguideinfo](https://www.gamesguideinfo.com/rise-of-kingdoms/overview/vip-levels); [VIP 19 ufficiale](https://forum-global.lilithgame.com/post/1812473). Buff rivisti nel [1.0.87](https://forum-global.lilithgame.com/post/1817043) |
| **Civiltà** | 3-5% su un attributo (es. France +3% Health e +20% velocità di cura; Ottoman +5% skill attiva; Maya +3% danno normale) | [heaven-guardian, 01/09/2026](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/). Dal [1.1.01](https://forum-global.lilithgame.com/post/2161435) i buff di civiltà si cambiano con City Hall 16 |
| **Titoli** | Justice +5% Attack e +10% velocità; General +5% Attack e +5% Defense; King +5% Attack/Defense/Health | [riseofkingdomsguides](https://riseofkingdomsguides.com/how-to-use-title-buffs-guide/). Vanno chiesti **prima** dell'azione ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-kingdom-titles-guide)) |
| **Rune** | 3 / 7 / 10 / 15 / 20% a seconda della rarità; **una sola attiva**, circa 1 ora | [rkg](https://riseofkingdomsguides.com/rise-of-kingdoms-runes/), [heaven-guardian](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/) |
| **Holy site** | Sanctum of Blood +2% Health; Flame Altar / Shrine of War +3% Attack; Shrine of Order +3% Defense e Health; Great Ziggurat (Lost Kingdom) +3% danno e −3% danno subito | [theriagames](https://theriagames.com/guide/rise-of-kingdoms-holy-sites-guide/). Siti dello stesso tipo non si sommano |
| **Temi città** | Fino a +20% Infantry Attack, +16% Troop Attack, +20% Cavalry Defense | Zenith of Power ([mar 2025](https://forum-global.lilithgame.com/post/1957780), [set 2025](https://forum-global.lilithgame.com/post/2120406), [dic 2025](https://forum-global.lilithgame.com/post/2177079)) |
| **Oggetti** | Enhanced Attack (Advanced) +10% | [Lyceum](https://riseofkingdomsguides.com/lyceum-of-wisdom-rok-answers/) |
| **Equipaggiamento** | Attributi del set; special talent +30% se il comandante ha il talento giusto | [Lyceum](https://riseofkingdomsguides.com/lyceum-of-wisdom-rok-answers/), KB `equipaggiamento.json` |
| **Formazioni e armamenti** | Wedge/Wedge II +12% skill, Pincer +10/12% smite, Delta +10% combo, Arch +5% danno da attacco. Honing fino a +3,5% | [1.1.06](https://forum-global.lilithgame.com/post/2219742), [1.1.03](https://forum-global.lilithgame.com/post/2197960), KB `armamenti.json` |
| **Crystal Tech** (solo SoC) | Attack del tipo +5/7,5%, Defense e Health +15%, Expert +10% di danno e di riduzione del danno | KB, dal [simulatore](https://rok-technology-simulator.netlify.app/); Expert dal [1.0.99](https://forum-global.lilithgame.com/post/2124406) |

**Derivazione nostra:** ricerca (+70%), alleanza (circa +15%) e VIP (+5%) portano vicino al **~92% di Attack da fonti fisse** misurato dalla community nel 2022. Da qui in poi ogni punto % in più rende sempre meno (formula x/(1+B)).

---

## 7. Movimento, AP, teleport, scouting
- **Velocità di marcia:**
  - la decide il tipo di unità **più lento**, insieme a talenti e terreno ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-game-mechanics-hub));
  - dal **1.0.96** le unità ferite o morte non rallentano più la marcia, salvo in ritirata ([patch](https://forum-global.lilithgame.com/post/2081453));
  - Rapid March (tecnologia d'alleanza) vale mentre si è **in territorio d'alleanza**.
- **Bonus alla velocità:**
  - Pathfinding e Cartography: +15% ciascuna;
  - Justice +10%, Sanctum of Wind +5%, Rome e Ottoman +5%;
  - rune fino a circa 20%;
  - Staggered +15% verso rally e guarnigioni, Double Line +10% verso i barbari ([1.0.99](https://forum-global.lilithgame.com/post/2124406));
  - Cao Cao con build mobilità ~51-52% dai soli talenti ([rkg](https://riseofkingdomsguides.com/fastest-cavalry-march-speed/)).
  
  heaven-guardian avverte di **non sommare alla cieca** le percentuali ([04/08/2026](https://heaven-guardian.com/rise-of-kingdoms-max-cavalry-march-speed-guide/)). Le velocità base in numeri non le ho trovate.
- **Action Points:**
  - tetto **1.500** ([1.0.41, dic 2020](https://forum-global.lilithgame.com/post/1030636)), più **500 AP gratuiti al giorno**; dal 1.1.02 si possono riscattare anche oltre il tetto ([patch](https://forum-global.lilithgame.com/post/2179486));
  - al tetto gli AP smettono di rigenerarsi;
  - un barbaro costa 50 AP, −2 per ogni attacco consecutivo (fino a −10); il talento Insight toglie fino a 9 AP ([heaven-guardian](https://heaven-guardian.com/rise-of-kingdoms-dominate-barbarians-forts-guide/));
  - esiste un **Auto-Peacekeeping** ufficiale ([1.1.07](https://forum-global.lilithgame.com/post/2232581)).
- **Teleport:**
  - tipi: Random (~500 gemme), Territorial (~750), Targeted (~1.500) e Beginner's ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-teleport-guide));
  - servono le marce in città, nessun rally o attacco in arrivo e nessuna War Frenzy;
  - dal **1.1.06** gli scout possono restare sulla mappa ([patch](https://forum-global.lilithgame.com/post/2219742));
  - nel Lost Kingdom si usa solo il Territorial.
- **Scouting:**
  - fare sempre uno scout recente prima di attaccare;
  - dal **1.1.09** (giugno 2026) le **Deceptive Troops non esistono più**: sono diventate Anti-Scouting Spyglass ([patch](https://forum-global.lilithgame.com/post/2259768)), quindi le guide che parlano di "truppe doppie" sono superate;
  - il Peace Shield blocca gli scout ([theriagames](https://theriagames.com/guide/rise-of-kingdoms-scout-camp-guide/)).
- **Code di marcia:** 1, poi 2/3/4/5 con il Municipio a 5/11/17/22. Rally al Castello 25: 2 milioni ([handbook](https://riseofkingdomshandbook.com/guides/riseofkingdoms-troop-capacity-march-queues-guide), [Lyceum](https://riseofkingdomsguides.com/lyceum-of-wisdom-rok-answers/)).

---

## 8. Regole per il bot (sintesi di `bot_rules`)
| id | Quando | Cosa fa | Conferma |
|---|---|---|---|
| mech-01 | Città, strutture, Lost Temple, Pass L2-3, Shrine, rinforzi | Mostra la regola di morte e una stima prudente delle perdite permanenti | **sì** |
| mech-02 | Prima di ogni scontro o rally | Controlla lo spazio in ospedale e blocca se non basta. Niente cure a gemme | no |
| mech-03 | Expedition, Canyon, Ark | Nessuna stima dei morti (per l'Ark vale comunque la conferma sugli attacchi ai giocatori) | no |
| mech-04 | Confronti tra scelte | Usa la formula solo in modo relativo e dichiara che è una stima | no |
| mech-05 | Cosa potenziare | Valore marginale x/(1+B); per sopravvivere, Defense × Health | no |
| mech-06 | Preparazione della marcia | Formazione e bonus in base al tipo di danno del primario | no |
| mech-07 | Scontro opzionale in cui si è contrastati | Evitarlo se la marcia vive di danno normale | no |
| mech-08 | Marce miste | Non mescolare quando le skill richiedono unità pure | no |
| mech-09 | Scontri tra più marce contro giocatori | Focus fire, attack march, evitare di farsi circondare | **sì** |
| mech-10 | Tempi delle skill | Niente rage fuori combattimento; prima skill dopo ~10 s | no |
| mech-11 | AP | Restare sotto 1.500, riscattare i 500 giornalieri, mai gemme | no |
| mech-12 | Titoli e rune | Chiederli prima dell'azione. Scrivere in chat richiede conferma | **sì** |
| mech-13 | Teleport | Solo con oggetti, dopo i controlli | **sì** |
| mech-14 | Prima di attaccare | Scout recente; niente "truppe doppie" dal 1.1.09 | **sì** |
| mech-15 | T4 o T5 | T4 per gli scontri di poco valore o con rischio di morti | no |
| mech-16 | Qualsiasi automazione | Avvisare del Conduct Score e dei termini di servizio; preferire le funzioni ufficiali | **sì** |
| mech-17 | KvK | Ospedale ×2, ma i morti restano un costo pieno | no |
| mech-18 | Marce veloci | Solo cavalleria; bonus condizionali | no |

---

## 9. Conflitti principali (dettagli nel JSON)
- **Tetto degli AP**: 1.500 (ufficiale, 2020) contro 1.000 in `truppe_pve.json`. Da correggere nella KB.
- **Attacco a città e strutture**: theriagames dice "tutti morti", riseofkingdomsguides "una parte". Il bot usa l'ipotesi prudente.
- **Tear of Blessing**: 9% (roktalents) contro 10% (gamesguideinfo).
- **Herbal Medicine**: Health +15% (dati di gioco) contro "healing efficiency" (theriagames).
- **Rage per attacco**: 100 (guida 2020) contro ~86 + ~16 (misura 2022).
- **Termine di scala**: due forme della community con la stessa pendenza.
- **Civiltà**: Arabia (+50% nel testo theriagames, probabile refuso), Britain (+10% o +20%), Japan (velocità di marcia o solo degli scout).
- **Scout "doppi"**: superato dalla patch 1.1.09.

## 10. Lacune
- La formula ufficiale del danno.
- Come funziona il true damage.
- Il valore del limite di danno per turno in città.
- Eventuali tetti ai bonus.
- La formula dei feriti gravi.
- Quante truppe servono per essere "surrounded".
- I tassi della Hall of Heroes.
- Le regole di morte contro barbari e forti.
- Le velocità base in numeri.
- Le tecnologie d'alleanza non verificate.
- La tabella VIP dopo il 1.0.87.
- L'effetto dello Spyglass.
- La durata ufficiale delle rune e della War Frenzy.
- Le patch dopo il 1.1.09: l'API ufficiale arriva al 23/06/2026. Per il 1.1.11 c'è solo il riassunto di [ldshop](https://www.ldshop.gg/blog/rise-of-kingdoms/anniversary-special.html), che non riporta modifiche al combattimento.

## 11. Fonti non raggiungibili
- **Reddit**: rimanda al login.
- **CDX di archive.org**: offline; singole pagine archiviate raggiungibili solo a tentativi.
- **heaven-guardian**: con curl la connessione viene chiusa; letto con WebFetch.
- **allclash**: risponde 403.
- **Indice RoK di BlueStacks**: errore 500.
- **API articoli bilibili**: rifiuta per troppe richieste; articoli letti dalle pagine /opus/.
- **riseofkingdoms.wiki**: bloccato dal proxy.
- **altema**: 403. **gamewith e game8**: nessuna sezione RoK.
- **rok.guide, fandom, riseofkingdoms.org**: irraggiungibili come previsto. Ho usato solo poche copie Wayback.
