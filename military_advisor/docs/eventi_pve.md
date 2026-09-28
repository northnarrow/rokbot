# Consigliere militare — EVENTI E MODALITÀ PvE / ASINCRONE (settembre 2026)

Ricerca del **28/09/2026**. Dati strutturati per il bot: `data/fragments/eventi_pve.json` (25 modalità, 54 lineup, 98 regole per il bot, 67 fonti, 12 conflitti, 44 lacune).
Nomi tecnici in inglese. Accanto alle affermazioni c'è la fonte con la data della pagina; quando un sito compare con una sola pagina nella sezione, il suo nome nel testo è già un link. Dove le fonti non concordano lo trovi scritto nel testo e nella sezione [Conflitti tra fonti](#conflitti-tra-fonti). Dove una fonte non dà il dato, nel JSON c'è `null` e la voce è in [Lacune](#lacune).

> **Vincoli del bot, sempre validi:** MAI spendere gemme (niente army expansion a gemme, tentativi extra, refresh, spin, acquisti). Conferma dell'utente prima di consumare materiali rari (oggetti AP in bottiglia, sculture, blueprint, libri, Armament/Iconic materials) e prima di qualsiasi azione contro giocatori. Le modalita' cooperative in tempo reale (Ceroli, Ian's Ballads, Ark of Osiris, Champions of Olympia, Shadow Legion) sono solo 'assistite': il bot prepara, avvisa e riscuote.
> Le regole marcate **conferma: sì** si eseguono solo dopo l'ok dell'utente.

> **Nota sulle date:** le pagine di riseofkingdomsguides.com hanno tutte data 02/01/2026 (aggiornamento massivo del sito): il contenuto può essere più vecchio. Per i numeri fa sempre fede il pannello in gioco.

---

## Quadro rapido

| # | Modalità | Tipo | Automazione del bot | Sblocco | Cadenza |
|---|---|---|---|---|---|
| 1 | [Expedition](#1-expedition) | PvE asincrono (campagna single-player permanente) | autonomo (nessuna perdita reale) | Menu Campaign > Expedition (bluestacks). Livello di City Hall di sblocco non indicato dalle fonti lette (vedi gaps). | Permanente. Forziere giornaliero basato sulla miglior valutazione in stelle degli stage completati, da riscuotere ogni giorno (bluestacks: reset alle 00:00 UTC). Negozio: epico in evidenza che ruota ogni settimana e alcuni articoli con limite giornaliero. |
| 2 | [Ceroli Crisis (e Ceroli Assault)](#2-ceroli-crisis-e-ceroli-assault) | PvE cooperativo in tempo reale (4 governatori); Ceroli Assault: 12 giocatori | assistito: il bot prepara e avvisa, la partita la gioca l'utente | n.d. | Ruota nel calendario degli eventi insieme a Ian's Ballads, Lohar's Trial e Karuak Ceremony (riseofkingdomshandbook); date dal pannello Events. |
| 3 | [Ian's Ballads](#3-ians-ballads) | PvE cooperativo in tempo reale (4 governatori) | assistito: il bot prepara e avvisa, l'utente gioca | City Hall 16+ (riseofkingdomshandbook). | Ruota nel calendario eventi con Ceroli Crisis, Lohar's Trial e Karuak Ceremony (riseofkingdomshandbook); date dal pannello Events. |
| 4 | [Karuak Ceremony](#4-karuak-ceremony) | PvE individuale a punti AP con rally d'alleanza | semi-autonomo (livelli facili) + conferma per difficolta' e oggetti AP | n.d. | Ruota con Ceroli Crisis, Ian's Ballads e Lohar's Trial (riseofkingdomshandbook); scadenza = countdown dell'evento. |
| 5 | [Trial of Kau Karuak (Season of Conquest)](#5-trial-of-kau-karuak-season-of-conquest) | PvE individuale a tempo (KvK Season of Conquest) | assistito (timer di battaglia, scelta comandanti) | Regni in Season of Conquest; difficolta' sbloccate nelle Lost Kingdom Chronicles (riseofkingdomsguides). | Legato al calendario KvK/Chronicle della Season of Conquest. |
| 6 | [Barbarians e Barbarian Forts (farm Peacekeeping e rally ai forti)](#6-barbarians-e-barbarian-forts-farm-peacekeeping-e-rally-ai-forti) | PvE asincrono sulla mappa (barbari: solo; forti: rally d'alleanza) | autonomo per barbari e per unirsi ai rally dei forti; conferma per guidare rally o usare oggetti AP | Barbari: da inizio gioco. Forti: servono un'alleanza e un capo rally (riseofkingdomshandbook). | Giornaliera/continua (spendere l'AP che si rigenera). Riferimento: 'unisciti a ogni rally di forte' come abitudine quotidiana. |
| 7 | [Holy Sites (Sanctum, Altar, Shrine, Lost Temple) e guardiani](#7-holy-sites-sanctum-altar-shrine-lost-temple-e-guardiani) | PvE (guardiani, rune) + PvP d'alleanza (conquista delle strutture) | autonomo sui guardiani PvE; SOLO su conferma per attaccare/rinforzare strutture contese | Contesa legata all'apertura delle zone/passi del regno; per attaccare una struttura serve territorio d'alleanza collegato (theriagames). | Guardiani: 2 spawn al giorno (00:00 e 12:00 UTC, durata 11 h). Strutture: contesa ogni 3 giorni (Lost Temple ogni 7). |
| 8 | [Lohar's Trial](#8-lohars-trial) | Evento PvE su barbari (Peacekeeping) + rally d'alleanza sul boss evocato | autonomo sul farm; conferma per oggetti AP e per annunci in chat | n.d. | Circa una volta al mese, 2 giorni (riseofkingdomshandbook). heaven-guardian e riseofkingdomsguides non danno durata. |
| 9 | [Arms Training (Armsmaster Lohar)](#9-arms-training-armsmaster-lohar) | PvE individuale a punteggio (classifica) | assistito (scelta dei modificatori) - i tentativi base possono essere automatizzati come test | n.d. | Evento a rotazione; incluso negli eventi dell'Anniversary 1.1.11 (27-08-2026, ldshop); 3 giorni con 5 tentativi al giorno (riseofkingdomsguides). |
| 10 | [Protect the Supplies (scorta carovana individuale)](#10-protect-the-supplies-scorta-carovana-individuale) | PvE individuale a stelle (evento stagionale) | semi-autonomo (AP) con conferma sulla difficolta' | n.d. | Stagionale (Summer of Passion); durata non indicata. |
| 11 | [Sunset Canyon](#11-sunset-canyon) | PvP asincrono contro difese salvate (truppe simulate, rischio zero) | autonomo (nessuna perdita reale, nessuna gemma) | n.d. | Giornaliera (5 tentativi gratis prima del reset) dentro stagioni di 7 giorni; punti azzerati a fine stagione. |
| 12 | [Ark of Osiris](#12-ark-of-osiris) | PvP d'alleanza 30v30 programmato (truppe ferite, non morte) | solo avviso/preparazione: il bot non si registra ne' combatte | City Hall 16+ per il singolo; alleanza con >10 flag e top 20 del regno per potenza (riseofkingdomshandbook). | riseofkingdomsguides: 'almost every two weeks'; riseofkingdomshandbook: usare il calendario di registrazione mostrato per l'alleanza, non un'etichetta settimanale generica. |
| 13 | [Champions of Olympia](#13-champions-of-olympia) | PvP 5v5 in tempo reale in stile MOBA (truppe dell'evento) | solo avviso: il bot non gioca | n.d. | Finestre attive dal pannello Events (riseofkingdomshandbook: registrarle insieme agli impegni d'alleanza). |
| 14 | [Osiris League (scommesse)](#14-osiris-league-scommesse) | Evento asincrono di previsione sulle partite di Ark of Osiris delle alleanze di vertice | autonomo per le missioni; conferma per le scommesse | n.d. | Durante le stagioni della Osiris League (date non indicate). |
| 15 | [Golden Kingdom](#15-golden-kingdom) | PvE dungeon a piani (asincrono, individuale) | semi-autonomo: esplorazione/battaglie con regole conservative; conferma per reset e oggetti rari | City Hall 17+ (riseofkingdomsguides). | Evento ricorrente; data e durata dal pannello Events (le fonti non danno la cadenza). |
| 16 | [Shadow Legion (Dark Fortresses)](#16-shadow-legion-dark-fortresses) | PvE d'alleanza a ondate contro le citta' dei membri | assistito: il bot prepara la citta' e rinforza solo su istruzione | Citta' livello 4+ e alleanza con 30 membri (riseofkingdomsguides). | Una volta per evento, all'orario scelto dagli ufficiali. |
| 17 | [Esmeralda's Prayer / Esmeralda's Collection](#17-esmeraldas-prayer--esmeraldas-collection) | Evento a ruota con valuta (Wishing Coins) + missioni giornaliere | autonomo con sole monete gratuite | n.d. | Stagionale: Spring Symphony 10 giorni (riseofkingdomsguides); Halloween 2026 con la 1.1.12 del 22-09-2026 (ldshop). |
| 18 | [Silk Road Speculators (carovana d'alleanza) e Desert Tracks](#18-silk-road-speculators-carovana-dalleanza-e-desert-tracks) | PvE d'alleanza di scorta (barbari contro la carovana) | autonomo sui barbari della scorta quando la carovana e' in viaggio; il bot non avvia carovane | Avvio riservato a leader/R4 (rok.guide via Wayback). | Evento d'alleanza periodico (fonte 2019); Desert Tracks negli anniversari 2025 e 2026. |
| 19 | [Race Against Time](#19-race-against-time) | PvE a tempo sui barbari (classifica) | autonomo con buff gratuiti; conferma per oggetti rari | n.d. | Stagionale (anniversario, Halloween, Spring Symphony). |
| 20 | [Marauders / Eve of the Crusade (pre-KvK e Lost Kingdom)](#20-marauders--eve-of-the-crusade-pre-kvk-e-lost-kingdom) | PvE a base di AP legato al KvK | autonomo con AP naturale; conferma per oggetti AP | Regni in fase KvK applicabile. | Legata al calendario KvK; dal 1.1.12 contestuale all'apertura del Lost Kingdom. |
| 21 | [Tempest Clash (battaglie navali)](#21-tempest-clash-battaglie-navali) | PvP 5v5 in tempo reale con navi (bonus del governatore disattivati) | solo avviso | City Hall 7+ (riseofkingdomsguides). | Stagionale (non indicata). |
| 22 | [Eventi Anniversario 2026 (versione 1.1.11 'Anniversary Special')](#22-eventi-anniversario-2026-versione-1111-anniversary-special) | Pacchetto stagionale di eventi asincroni (missioni, negozi a valuta, mini-giochi) | autonomo per login/missioni/riscossioni; conferma per interazioni con altri giocatori e acquisti non gratuiti | n.d. | Annuale (fine agosto - settembre). |
| 23 | [Halloween 2026 (versione 1.1.12 'Dreams of Phantasma')](#23-halloween-2026-versione-1112-dreams-of-phantasma) | Pacchetto stagionale + modifiche Lost Kingdom | autonomo per missioni gratuite; conferma per armamenti e speedup | n.d. | Stagionale (dal 22-09-2026). |
| 24 | [Radiant Rivalry (NUOVA modalita' 2026, 1v1 tra regni)](#24-radiant-rivalry-nuova-modalita-2026-1v1-tra-regni) | Competizione tra due regni: fase di preparazione asincrona + fase di battaglia PvP | autonomo nella preparazione (missioni); solo avviso/conferma nella battaglia | n.d. | Nuova nel 2026; calendario non indicato. |
| 25 | [Clash of Divine Isles](#25-clash-of-divine-isles) | Evento a punti con invasioni tra territori (PvP) | solo avviso | n.d. | Non indicata. |

## Pianificazione generale

- Controllo settimanale di 10 minuti: lista eventi attivi/annunciati, annunci d'alleanza (registrazioni, orari fissi), scelta degli eventi utili all'obiettivo, riserva solo del necessario, buffer per progressione e cure; annotare reset/scadenze reali. ([handbook · event calendar hub 09/09/2026][s1])
- Cosa conservare: oggetti AP per eventi PvE ad alto valore (Marauders, Karuak, Lohar's Trial, KvK Honor), speedup per MGE/eventi di potenza, speedup di cura per KvK, token risorse e materiali di equipaggiamento. Il F2P non deve classificarsi in ogni evento: milestone garantite e premi d'alleanza valgono di piu'. ([heaven-guardian · events dominate 03/08/2026][s2] · [heaven-guardian · maximize action points 03/08/2026][s3])
- Le quattro rotazioni 'silenziose' che finanziano equipaggiamento e comandanti: Ceroli Crisis, Ian's Ballads, Lohar's Trial, Karuak Ceremony: giocarle tutte con costanza. ([handbook · ceroli crisis 09/09/2026][s4])
- Prima del reset giornaliero: separare i premi gia' sbloccati ma non riscossi (da riscuotere subito) dagli obiettivi non finiti; non iscriversi a un raid lungo pochi minuti prima di un evento d'alleanza fisso. ([handbook · event calendar hub 09/09/2026][s1])

---

## 1. Expedition

**Tipo:** PvE asincrono (campagna single-player permanente) · **Automazione:** autonomo (nessuna perdita reale)

**Sblocco:** Menu Campaign > Expedition ([bluestacks][s5]). Livello di City Hall di sblocco non indicato dalle fonti lette (vedi gaps).

**Cadenza:** Permanente. Forziere giornaliero basato sulla miglior valutazione in stelle degli stage completati, da riscuotere ogni giorno ([bluestacks][s5]: reset alle 00:00 UTC). Negozio: epico in evidenza che ruota ogni settimana e alcuni articoli con limite giornaliero.

### Meccaniche
- Campagna permanente single-player (menu Campaign > Expedition) contro marce nemiche preimpostate, stage lineari ([riseofkingdomshandbook][s6], [bluestacks][s5]).
- Truppe simulate: nulla muore e nulla va in ospedale; tentativi illimitati. Per ogni unita' addestrata entra 1 unita' nel pool Expedition e le unita' perse in Expedition non riducono quel totale ([riseofkingdomshandbook][s6]; pool truppe: heaven-guardian).
- Fino a 3 stelle per stage: 1 = condizione minima, 2 = due condizioni, 3 = tutte le condizioni; vincere non garantisce 3 stelle. Condizioni tipiche: sconfiggere tutti entro un tempo, perdite sotto una percentuale, proteggere unita' alleate (heaven-guardian, [bluestacks][s5]).
- Marce disponibili: 1 all'inizio, 2 dallo stage 6, 3 dallo stage 16, 4 dallo stage 26, 5 dallo stage 41 ([riseofkingdomshandbook][s6]).
- I comandanti nemici salgono di stelle (e quindi di abilita') a scatti: 2 stelle dallo stage 11, 3 dal 21, 4 dal 31, 5 dal 41, 6 dal 51: sono i 'muri' di difficolta' ([riseofkingdomshandbook][s6]).
- Nella marcia valgono solo talenti e capacita' truppe del comandante PRIMARIO; il secondario porta solo le abilita' sbloccate (heaven-guardian).
- Le truppe T5 non sono obbligatorie: un account T4 con abilita' alte, coppie corrette, tecnologia militare, equipaggiamento e armamenti arriva lontano (heaven-guardian).

### Premi principali
- Medals of the Conqueror (piu' stelle = piu' medaglie) per l'Expedition Store: sculture Aethelflaed (limite giornaliero), Constance, scultura dell'epico in evidenza (settimanale), Dazzling Starlight Sculptures, Silver/Golden Keys, speedup ([bluestacks][s5], [riseofkingdomshandbook][s6], heaven-guardian).
- Premi una-tantum di primo completamento: risorse, Tomes of Knowledge, sculture, forzieri di progressione; [riseofkingdomshandbook][s6] la definisce anche una grossa fonte una-tantum di gemme.
- Forziere giornaliero ricorrente che cresce in modo permanente con le stelle ottenute ([riseofkingdomshandbook][s6]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| F2P | Tank: Bjorn Ironside (o Charles Martel se disponibile) · AoE: Sun Tzu (opzione 'budget friendly') · AoE: Baibars · Supporto/AoE: Aethelflaed (acquistabile con Medals of the Conqueror) | Ruoli consigliati da [heaven-guardian][s7] (tank: Richard I, Charles Martel, Sun Tzu, Bjorn Ironside; AoE: Sun Tzu, Aethelflaed, Baibars, Yi Seong-Gye) e [bluestacks][s5] (Sun Tzu AoE economico; Aethelflaed debuff e versatilita'). [riseofkingdomshandbook][s6]: portare la coppia piu' SVILUPPATA (livelli abilita'), non quella con piu' potenza. | [heaven-guardian · expedition tips rewards 03/08/2026][s7] · [bluestacks · expeditions 11/12/2024][s5] · [handbook · expedition 18/08/2026][s6] |
| F2P - coppia 2026 | Aethelflaed + Sun Tzu | heaven-guardian (2026-08-12): coppia 'especially attractive to newer F2P accounts' perche' Aethelflaed si sviluppa con l'Expedition e Sun Tzu e' un epico accessibile; sviluppare Aethelflaed con l'Expedition invece che con sculture universali (heaven-guardian, pagina Aethelflaed). | [heaven-guardian · best commander pairings 12/08/2026][s8] · [heaven-guardian · aethelflaed talents pairings 06/08/2026][s9] |
| evoluto | Richard I (primario) + Sun Tzu (secondario): tank + AoE · Yi Seong-Gye (primario) + Aethelflaed (secondario): AoE + debuff · Supporto: Joan of Arc, Mulan o Aethelflaed · Burst su bersaglio singolo: Cao Cao, Minamoto no Yoshitsune | Coppie esplicite di [bluestacks][s5] (Richard I+Sun Tzu, YSG+Aethelflaed); ruoli supporto di [heaven-guardian][s7] (Joan of Arc, Aethelflaed, Mulan); cura per ridurre le perdite negli stage a condizione di sopravvivenza (Richard I, Joan of Arc). | [bluestacks · expeditions 11/12/2024][s5] · [heaven-guardian · expedition tips rewards 03/08/2026][s7] |
| formazione (5 marce) | Marcia 1 tank: centro avanti · Marcia 2 AoE: dietro a sinistra · Marcia 3 danno: dietro a destra · Marcia 4 supporto: centro retro · Marcia 5 finisher: retro o fianco | Schema di [heaven-guardian][s7]: il tank entra per primo, si aspetta che i nemici lo prendano di mira, poi damage e supporto entrano nel raggio delle abilita'. | [heaven-guardian · expedition tips rewards 03/08/2026][s7] |

### Trucchi (massimo punteggio, zero perdite)
- Leggere le condizioni delle stelle PRIMA di iniziare (heaven-guardian).
- Mandare il tank per primo verso il nemico piu' vicino; muovere damage e supporto solo quando i nemici lo hanno agganciato (heaven-guardian).
- Raggruppare i nemici e concentrare il fuoco su UN bersaglio alla volta: cinque marce su cinque nemici diversi lasciano tutti i nemici a fare danno (heaven-guardian, [bluestacks][s5]).
- Proteggere la marcia di supporto; riavviare lo stage se il pathing iniziale e' sbagliato (heaven-guardian).
- Non sprecare abilita' attive su nemici quasi morti; tenerle per le minacce grosse ([bluestacks][s5]).
- Assedio solo quando serve limitare le perdite (resta fuori dal combattimento diretto), fanteria per sopravvivenza, arcieri per danno a distanza, cavalleria per mobilita' ([bluestacks][s5]).
- Se uno stage diventa improvvisamente duro controllare se si e' appena superato un breakpoint (11, 21, 31, 41, 51); cambiare coppia invece di insistere ([riseofkingdomshandbook][s6]).
- Tornare sugli stage vecchi a 1-2 stelle dopo ogni potenziamento: le stelle alzano per sempre il forziere giornaliero ([riseofkingdomshandbook][s6], heaven-guardian).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| EXP-01 | Ogni giorno dopo il reset (00:00 UTC secondo bluestacks) e forziere giornaliero Expedition disponibile | Riscuotere il forziere giornaliero. — *Premio gratuito che cresce con le stelle; un tocco al giorno.* | no | [handbook · expedition 18/08/2026][s6] · [bluestacks · expeditions 11/12/2024][s5] |
| EXP-02 | Stage non completato o completato con meno di 3 stelle | Riprovare cambiando coppia/formazione/ordine dei bersagli (tank prima, focus su un nemico). Limite interno consigliato: 5 tentativi per stage per sessione, poi marcare lo stage come 'bloccato' e passare oltre. — *Le truppe sono simulate: il retry non costa risorse (il limite di tentativi e' una scelta di efficienza del bot, non una regola del gioco).* | no | [handbook · expedition 18/08/2026][s6] · [heaven-guardian · expedition tips rewards 03/08/2026][s7] |
| EXP-03 | Lo stage corrente e' 11, 21, 31, 41 o 51 (salto di stelle dei nemici) e fallisce ripetutamente | Fermare il push; registrare lo stage; riprovare dopo un potenziamento di abilita'/equipaggiamento/tecnologia della coppia usata; nel frattempo rifare a 3 stelle gli stage vecchi. — *I nemici guadagnano abilita' a scatti ai breakpoint; le 3 stelle sugli stage vecchi alzano il forziere giornaliero.* | no | [handbook · expedition 18/08/2026][s6] |
| EXP-04 | Medals of the Conqueror disponibili e articoli a limite giornaliero non ancora comprati | Comprare ogni giorno le sculture Aethelflaed (limite giornaliero) se Aethelflaed e' nel piano dell'account; poi la scultura dell'epico in evidenza SOLO se quel comandante e' nella lista obiettivi dell'utente; poi Constance se l'account raccoglie molto. — *Il limite giornaliero premia l'acquisto costante; le fonti divergono sulla priorita' tra Aethelflaed ed epico settimanale (vedi conflicts).* | no | [handbook · expedition 18/08/2026][s6] · [heaven-guardian · expedition tips rewards 03/08/2026][s7] · [bluestacks · expeditions 11/12/2024][s5] |
| EXP-05 | Acquisto nel negozio Expedition di un articolo NON in lista obiettivi (es. epico in evidenza di un comandante non pianificato, keys) | Chiedere conferma all'utente prima di spendere le medaglie. — *Evita di disperdere la valuta su comandanti inutili per l'account.* | **sì** | [handbook · expedition 18/08/2026][s6] |
| EXP-06 | Stage con condizione 'perdite sotto X%' o 'proteggi alleati' | Usare in formazione un tank con cura (Richard I) e un supporto con cura (Joan of Arc/Mulan/Aethelflaed); focus fire; ritirare in retro le marce sotto il 30% di truppe se il gioco lo consente (soglia del bot, non delle fonti). — *Le fonti indicano cura e focus fire come chiave delle 3 stelle.* | no | [bluestacks · expeditions 11/12/2024][s5] · [heaven-guardian · expedition tips rewards 03/08/2026][s7] |

**Lacune:** Livello di City Hall di sblocco dell'Expedition non indicato dalle fonti lette. Numero totale di stage/capitoli nel 2026 non indicato.

**Fonti della sezione:** [handbook · expedition 18/08/2026][s6] · [heaven-guardian · expedition tips rewards 03/08/2026][s7] · [bluestacks · expeditions 11/12/2024][s5]

---

## 2. Ceroli Crisis (e Ceroli Assault)

**Tipo:** PvE cooperativo in tempo reale (4 governatori); Ceroli Assault: 12 giocatori · **Automazione:** assistito: il bot prepara e avvisa, la partita la gioca l'utente

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Ruota nel calendario degli eventi insieme a Ian's Ballads, Lohar's Trial e Karuak Ceremony ([riseofkingdomshandbook][s4]); date dal pannello Events.

### Meccaniche
- Scenario a 4 governatori: ognuno porta UNA marcia e sceglie un ruolo (Tank, Damage/DPS, Support); si sceglie boss e difficolta' ([heaven-guardian][s10], riseofkingdomsguides).
- 5 difficolta': Easy, Normal, Hard, Nightmare, Hell. Non esiste un requisito di potenza fisso: contano abilita', equipaggiamento, armamenti, tecnologia, tier truppe, ruoli ed esecuzione (riseofkingdomsguides, [heaven-guardian][s10]).
- Dekar: capo del veleno; marchi Fire/Lightning che possono scambiarsi (raggrupparsi con lo stesso marchio, separarsi dall'opposto), zone che si espandono, sentinelle/totem da distruggere subito ([heaven-guardian][s10], [riseofkingdomshandbook][s4]).
- Keira: rallentamenti seguiti dalla raffica di frecce: uscire dalle zone rosse ed entrare in tempo nella cupola protettiva; Curse mirata; guardiani d'elite da eliminare. La fanteria (lenta) deve muoversi prima ([heaven-guardian][s10], [riseofkingdomshandbook][s4]).
- Frida: Frozen Form (protetta/invulnerabile: uccidere le evocazioni, NON sprecare abilita'), poi Thawing Point = finestra di vulnerabilita' in cui scaricare tutto il burst e le riduzioni di difesa ([heaven-guardian][s10]).
- Astrid: cambi di postura, debuff cumulativi (Puncture Wound), Spear Volley, Earth Shatter da evitare: ruotare fuori le marce con troppi stack ([heaven-guardian][s10]).
- Ak and Hok: coppia con poteri Sun/Moon: un tank per boss, tenerli separati; setup validi 2 Tank + 2 Damage (aggressivo) o 2 Tank + 1 Damage + 1 Support (sicuro) ([heaven-guardian][s10]).
- Torgny: Thunder Form poi Tempest Form; la guardia evocata, una volta uccisa, crea un velo protettivo: restarci dentro nella fase pericolosa ([heaven-guardian][s10]).
- Ceroli Assault (evento separato): tu + 11 giocatori; servono 50 Horns of Ceroli per sfidare il boss; i corni si rigenerano e vengono restituiti se il tentativo fallisce; boost di attacco/difesa e army expansion NON hanno effetto; dopo il boss si ottengono ticket per forzieri (riseofkingdomsguides).

### Premi principali
- Premi diretti dei boss + medaglie da spendere nel Ceroli Shop prima della chiusura dell'evento (le valute evento non vanno date per trasferibili) ([riseofkingdomshandbook][s4]).
- Priorita' negozio ([riseofkingdomshandbook][s4]): materiali e blueprint di equipaggiamento > sculture > speedup > risorse. [heaven-guardian][s10]: prima gli articoli limitati che servono alla build principale; sculture solo se il comandante e' ancora utile e incompleto; blueprint solo se servono al piano equipaggiamento.
- Keira (comandante) nel Ceroli Shop: riseofkingdomsguides dice di comprarla; [heaven-guardian][s10] la considera utile solo se ancora usata negli scenari (vedi conflicts).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| evoluto - Tank | Richard I + Alexander the Great · Richard I + Yi Seong-Gye · Guan Yu + Alexander the Great | Coppie tank indicate da [riseofkingdomsguides][s11]; [heaven-guardian][s10]: il tank va scelto per Health/Defense/sostegno e controllo del boss, non per potenza. | [riseofkingdomsguides · ceroli crisis 02/01/2026][s11] · [heaven-guardian · ceroli crisis boss 05/08/2026][s10] |
| evoluto - DPS | Genghis Khan + Yi Seong-Gye (preferita) · Minamoto no Yoshitsune + Cao Cao | [riseofkingdomsguides][s11]: 'Khan and YSG are better'; nuke e AoE sui boss. | [riseofkingdomsguides · ceroli crisis 02/01/2026][s11] |
| F2P / account giovane | La coppia piu' sviluppata adatta al ruolo · Aethelflaed o Boudica per i bonus contro unita' neutrali | [heaven-guardian][s10]: le vecchie coppie funzionano se sviluppate, ma i regni nuovi devono usare la migliore coppia di ruolo disponibile; [riseofkingdomshandbook][s4]: Peacekeeping e bonus anti-neutrali aiutano contro i boss (Aethelflaed, Boudica). | [heaven-guardian · ceroli crisis boss 05/08/2026][s10] · [handbook · ceroli crisis 09/09/2026][s4] |
| composizione squadra | 1 Tank + 2 Damage + 1 Support (standard) · 3 Damage solo con difficolta' comoda e tank autosufficiente · Ak and Hok: 2 Tank + 2 Damage oppure 2 Tank + 1 Damage + 1 Support | Il vecchio setup 2 tank + 2 damage + 1 healer e' impossibile: i governatori sono 4. | [heaven-guardian · ceroli crisis boss 05/08/2026][s10] |

### Trucchi (massimo punteggio, zero perdite)
- Squadra privata d'alleanza con ruoli assegnati prima di entrare; il matchmaking casuale va bene solo alle difficolta' basse ([heaven-guardian][s10]); riseofkingdomsguides consiglia di evitarlo.
- Scegliere la difficolta' piu' alta che TUTTA la squadra completa in modo affidabile: un fallimento in alto rende meno di un clear piu' basso ([heaven-guardian][s10]).
- Una persona chiama le meccaniche; tenere corto il percorso verso le zone sicure ([riseofkingdomshandbook][s4]).
- Tenere il burst per le finestre di vulnerabilita' (Thawing Point di Frida); non usare tutte le difese prima della fase finale di Torgny ([heaven-guardian][s10]).
- Ceroli Assault: non copiare i ruoli della Crisis; usare comandanti da nuke (Genghis Khan, Minamoto, Cao Cao) e non accumulare i ticket (riseofkingdomsguides).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| CER-01 | Ceroli Crisis o Ceroli Assault attivo nel pannello Events | Notificare l'utente con difficolta' suggerita (in base all'ultima completata) e ruolo suggerito (Tank se l'account ha una coppia difensiva sviluppata tipo Richard I/Guan Yu + Alexander, altrimenti Damage). Non entrare in matchmaking ne' accettare inviti da solo. — *Contenuto cooperativo in tempo reale con meccaniche da eseguire: serve l'utente.* | **sì** | [heaven-guardian · ceroli crisis boss 05/08/2026][s10] · [riseofkingdomsguides · ceroli crisis 02/01/2026][s11] |
| CER-02 | L'utente conferma la partecipazione | Preparare: formazione/equipaggiamento della coppia di ruolo, truppa corretta per il comandante, check della meccanica del boss scelto (scheda sopra). — *Checklist di preparazione di heaven-guardian.* | no | [heaven-guardian · ceroli crisis boss 05/08/2026][s10] |
| CER-03 | Mancano meno di 24 ore alla chiusura dell'evento e ci sono medaglie Ceroli non spese | Proporre la lista acquisti: materiali/blueprint di equipaggiamento del piano attivo > sculture di comandanti in sviluppo (Keira solo se usata) > speedup > risorse. Acquistare dopo conferma. — *Le medaglie non spese vanno perse; il negozio conta piu' dei drop.* | **sì** | [handbook · ceroli crisis 09/09/2026][s4] · [heaven-guardian · ceroli crisis boss 05/08/2026][s10] |
| CER-04 | Ceroli Assault: Horns of Ceroli >= 50 | Avvisare l'utente che puo' sfidare il boss (il tentativo fallito restituisce i corni); riscuotere e usare i ticket forziere senza accumularli. — *Corni rigenerabili e restituiti in caso di sconfitta; i ticket non vanno tenuti.* | **sì** | [riseofkingdomsguides · ceroli assault event 02/01/2026][s12] |
| CER-05 | Qualsiasi proposta di comprare army expansion o boost per Ceroli Assault | Rifiutare: in Ceroli Assault boost di attacco/difesa e army expansion non hanno effetto; in ogni caso MAI gemme. — *Regola dell'evento + vincolo del bot.* | no | [riseofkingdomsguides · ceroli assault event 02/01/2026][s12] |

**Lacune:** Livello di City Hall richiesto per Ceroli Crisis/Assault non indicato dalle fonti lette. Perdite di truppe in Ceroli Crisis: nessuna fonte letta lo dice esplicitamente. Cadenza precisa (giorni) e prezzi del Ceroli Shop non indicati.

**Fonti della sezione:** [heaven-guardian · ceroli crisis boss 05/08/2026][s10] · [handbook · ceroli crisis 09/09/2026][s4] · [riseofkingdomsguides · ceroli crisis 02/01/2026][s11] · [riseofkingdomsguides · ceroli assault event 02/01/2026][s12]

---

## 3. Ian's Ballads

**Tipo:** PvE cooperativo in tempo reale (4 governatori) · **Automazione:** assistito: il bot prepara e avvisa, l'utente gioca

**Sblocco:** City Hall 16+ ([riseofkingdomshandbook][s13]).

**Cadenza:** Ruota nel calendario eventi con Ceroli Crisis, Lohar's Trial e Karuak Ceremony ([riseofkingdomshandbook][s13]); date dal pannello Events.

### Meccaniche
- Raid per 4 governatori (tu + 3 invitati), ogni governatore invia UNA sola armata; limite di 2 ore per ondate di barbari + 3 boss; 5 difficolta' ([riseofkingdomshandbook][s13]; una sola armata per governatore: [riseofkingdomsguides][s14]).
- Stack di danno bonus: ogni barbaro/boss accumula danno bonus sulle tue truppe; iniziare a fuggire a 15-20 stack; si azzerano dopo 2 s senza subire danni ([riseofkingdomsguides][s14]).
- Resting Campsite: rifornimenti e rinforzi; non utilizzabile durante lo scontro con un capo. Un'armata sconfitta torna al campo piu' vicino e viene curata ([riseofkingdomsguides][s14]).
- Huntmaster Kikkara: Slash a ventaglio (Damage Factor 6000); Hunting Instinct +10% danni da abilita' a ogni abilita' usata; Desperate Will: quando le sue truppe scendono al 25% scatena lo 'spirito combattivo' (fase finale piu' pericolosa); Impulse: 20% di probabilita' per attacco di curare l'1% delle truppe. Disporsi sui quattro lati ([riseofkingdomsguides][s14]).
- Beastlord Mokka: evoca 2 truppe di orsi; Instinct +100% difesa alle sue unita'; Roar +20% attacco per ogni orso in vita; Beastlord Awakens: dopo 300 secondi di battaglia +200% a tutti i danni: uccidere gli orsi e chiudere entro 300 s ([riseofkingdomsguides][s14]).
- Flamebender Papakura: Flaming Vengeance (DF 500 al secondo per 3 secondi su 3 bersagli casuali), Flame Totem che cura l'1% delle sue truppe al secondo (distruggerlo subito), Ring of Flames (DF 100 al secondo ad area), Fiery Sacrifice: quando sconfigge una truppa si cura del 20% e ottiene +200% a tutti i danni: evitare morti ([riseofkingdomsguides][s14]).

### Premi principali
- Dopo ogni boss un forziere di blueprint di equipaggiamento e materiali; clear completo alle difficolta' alte = blueprint e materiali super rari ([riseofkingdomshandbook][s13]).
- Chieftain's reward: una sola volta per governatore, indipendentemente dal numero di run ([riseofkingdomshandbook][s13], [riseofkingdomsguides][s14]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| evoluto | Minamoto no Yoshitsune · Cao Cao · Genghis Khan | [riseofkingdomsguides][s14]: usare comandanti da nuke; tanto danno burst per chiudere Mokka entro 300 s e i totem di Papakura. | [riseofkingdomsguides · ians ballads 02/01/2026][s14] |
| F2P | La coppia da danno piu' sviluppata (non quella da raccolta) · Secondario con albero Peacekeeping per le ondate di barbari | [riseofkingdomshandbook][s13]: sono i boss a decidere i premi, ma i bonus contro barbari aiutano nella fase a ondate. | [handbook · ians ballads 09/09/2026][s13] |

### Trucchi (massimo punteggio, zero perdite)
- Correre con 3 compagni d'alleanza coordinati, non con sconosciuti; focus fire sullo stesso bersaglio ([riseofkingdomshandbook][s13]).
- Muoversi in gruppo tra gli scontri; attivare i campi di riposo lungo il percorso e usarli PRIMA del boss ([riseofkingdomshandbook][s13]).
- Mokka: una persona chiama gli orsi, tutti switchano insieme e tornano sul boss ([riseofkingdomshandbook][s13]).
- Papakura: il totem e' un obiettivo; chi sta per morire deve ritirarsi prima (il boss si potenzia con le morti) ([riseofkingdomshandbook][s13]).
- Se si fallisce, capire la causa (add vivi, totem mancati, frontale preso in gruppo) prima di cambiare difficolta' o comandanti ([riseofkingdomshandbook][s13]).
- Conservare i blueprint e spenderli con un piano (prima l'arma, poi l'elmo, secondo [riseofkingdomshandbook][s13]).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| IAN-01 | City Hall < 16 | Ignorare l'evento (non idoneo). — *Requisito CH16+.* | no | [handbook · ians ballads 09/09/2026][s13] |
| IAN-02 | Ian's Ballads attivo e CH >= 16 | Notificare l'utente e proporre: difficolta' = la piu' alta completata in precedenza (o Easy al primo run); coppia da danno migliore; lista di 3 compagni d'alleanza attivi. Non inviare/accettare inviti in autonomia. — *Gruppo da 4 in tempo reale entro 2 ore.* | **sì** | [handbook · ians ballads 09/09/2026][s13] |
| IAN-03 | Durante il run (modalita' assistita) una marcia ha 15-20 stack di danno | Allontanarla finche' gli stack si azzerano (2 s senza danni), poi rientrare. — *Gli stack aumentano i danni subiti.* | no | [riseofkingdomsguides · ians ballads 02/01/2026][s14] |
| IAN-04 | Suggerimento di usare army expansion / boost di attacco | MAI acquistarli con gemme; usare solo oggetti gia' posseduti e solo dopo conferma dell'utente. — *riseofkingdomsguides li consiglia, ma il bot non spende gemme e gli oggetti sono rari.* | **sì** | [riseofkingdomsguides · ians ballads 02/01/2026][s14] |
| IAN-05 | Fine run | Riscuotere i forzieri dei boss e il chieftain's reward se non ancora ottenuto; registrare difficolta' e boss completati. — *Il chieftain's reward e' una tantum per governatore.* | no | [handbook · ians ballads 09/09/2026][s13] |

**Lacune:** Durata dell'evento in giorni e numero di run possibili non indicati.

**Fonti della sezione:** [handbook · ians ballads 09/09/2026][s13] · [riseofkingdomsguides · ians ballads 02/01/2026][s14]

---

## 4. Karuak Ceremony

**Tipo:** PvE individuale a punti AP con rally d'alleanza · **Automazione:** semi-autonomo (livelli facili) + conferma per difficolta' e oggetti AP

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Ruota con Ceroli Crisis, Ian's Ballads e Lohar's Trial (riseofkingdomshandbook); scadenza = countdown dell'evento.

### Meccaniche
- Formato individuale documentato: 50 livelli e 5 difficolta' (Easy, Normal, Hard, Nightmare, Hell). Non dare per scontato di poter cambiare difficolta' dopo la conferma (riseofkingdomshandbook).
- Si evoca il bersaglio (costo AP) e lo si attacca (costo AP aggiuntivo che cresce con gli attacchi ripetuti). Esempio: 100 AP x 50 evocazioni = 5.000 AP SOLO di evocazioni (riseofkingdomshandbook).
- I bersagli duri richiedono rally/aiuto dell'alleanza; esiste un pannello separato di sfida d'alleanza (boss d'alleanza) distinto dalla traccia individuale (riseofkingdomshandbook).
- Da non confondere con Trial of Kau Karuak (Season of Conquest, cristalli) (riseofkingdomshandbook, heaven-guardian).
- heaven-guardian (2026): evento PvE progressivo con sfidanti sempre piu' difficili, con possibilita' di chiedere aiuto ai membri dell'alleanza; preparare Action Points, comandanti PvE forti e supporto degli alleati.

### Premi principali
- Premi per singolo livello, per completamento della traccia e per le sfide d'alleanza (separati; nessun valore fisso garantito per la modalita' Hell) (riseofkingdomshandbook).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| F2P / livelli facili | Marcia Peacekeeping sostenibile (es. Lohar o altro comandante anti-barbari sviluppato) · Secondario da livellare | [riseofkingdomshandbook][s15]: nei livelli facili una marcia Peacekeeping sostenibile e un secondario da far crescere. (Lohar come esempio di comandante Peacekeeping: vedi Lohar's Trial.) | [handbook · karuak ceremony 09/09/2026][s15] |
| evoluto / livelli difficili | Coppia da combattimento sviluppata · Rally d'alleanza per i bersagli che richiedono piu' marce | [riseofkingdomshandbook][s15]: al primo livello che costringe a ricariche frequenti passare a un partner sviluppato; organizzare aiuto invece di pagare tentativi ripetuti. | [handbook · karuak ceremony 09/09/2026][s15] |

### Trucchi (massimo punteggio, zero perdite)
- Budget AP = evocazioni + attacchi + tentativi extra, calcolato coi costi mostrati sul proprio account, PRIMA di scegliere la difficolta' (riseofkingdomshandbook).
- Nei giorni precedenti non lasciare la barra AP al massimo (la rigenerazione si ferma): spendere l'AP naturale e conservare gli oggetti di ricarica (riseofkingdomshandbook).
- Scegliere la difficolta' piu' alta che si puo' FINIRE col tempo, gli AP e l'aiuto d'alleanza realmente disponibili; concordare finestra di rally e leader prima (riseofkingdomshandbook).
- Annotare per il run successivo: difficolta' completata, livello in cui la marcia solista smette di essere efficiente, AP in bottiglia usati (riseofkingdomshandbook).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| KAR-01 | Karuak Ceremony annunciato o attivo e difficolta' non ancora scelta | Calcolare AP disponibili (barra + oggetti) e costo stimato (evocazione x livelli rimanenti + attacchi + 20% di riserva) e proporre all'utente la difficolta' completabile. — *La difficolta' potrebbe non essere modificabile; il costo di evocazione non e' l'intero budget.* | **sì** | [handbook · karuak ceremony 09/09/2026][s15] |
| KAR-02 | Nei giorni prima dell'evento l'AP naturale e' al massimo | Spendere l'AP in barbari (catena Peacekeeping) e NON usare gli oggetti AP. — *La rigenerazione si ferma al cap; gli oggetti servono all'evento.* | no | [handbook · karuak ceremony 09/09/2026][s15] |
| KAR-03 | Livello evocato battibile dalla marcia Peacekeeping in un attacco | Evocare e attaccare usando SOLO AP naturale. — *PvE su bersagli dell'evento, nessun giocatore coinvolto.* | no | [handbook · karuak ceremony 09/09/2026][s15] |
| KAR-04 | Serve usare oggetti AP o il livello richiede rally | Chiedere conferma per gli oggetti AP; per i rally inviare posizione e tipo truppa richiesto all'alleanza solo con l'ok dell'utente. — *Oggetti AP = risorsa limitata; la chat d'alleanza e' comunicazione per conto dell'utente.* | **sì** | [handbook · karuak ceremony 09/09/2026][s15] |
| KAR-06 | Prossimo livello Karuak difficile (serve piu' di un attacco o un rally) | Verificare prima lo spazio libero in ospedale; se insufficiente, curare o rinviare il livello. — *heaven-guardian elenca lo spazio in ospedale tra le preparazioni per i livelli difficili (i feriti sono reali).* | no | [heaven-guardian · events dominate 03/08/2026][s2] |
| KAR-05 | Ogni livello completato o sfida d'alleanza sbloccata | Riscuotere subito i premi; lasciare margine di tempo prima del countdown finale. — *Premi separati per livello/traccia/alleanza.* | no | [handbook · karuak ceremony 09/09/2026][s15] |

**Lacune:** Requisiti di sblocco, durata in giorni e valori dei premi del Karuak Ceremony non indicati dalle fonti 2026 lette (riseofkingdomshandbook cita un walkthrough AppGamer non raggiungibile).

**Fonti della sezione:** [handbook · karuak ceremony 09/09/2026][s15] · [handbook · ceroli crisis 09/09/2026][s4] · [heaven-guardian · events dominate 03/08/2026][s2] · [heaven-guardian · maximize action points 03/08/2026][s3]

---

## 5. Trial of Kau Karuak (Season of Conquest)

**Tipo:** PvE individuale a tempo (KvK Season of Conquest) · **Automazione:** assistito (timer di battaglia, scelta comandanti)

**Sblocco:** Regni in Season of Conquest; difficolta' sbloccate nelle Lost Kingdom Chronicles ([riseofkingdomsguides][s16]).

**Cadenza:** Legato al calendario KvK/Chronicle della Season of Conquest.

### Meccaniche
- Evento solitario contro un boss: nessun altro governatore puo' aiutare ([riseofkingdomsguides][s16]).
- 5 difficolta' sbloccate con le Lost Kingdom Chronicles, 30 livelli per difficolta'; si completa una difficolta' prima di passare alla successiva ([riseofkingdomsguides][s16]).
- Il bersaglio resta sulla mappa per un tempo limitato; quando il boss entra in battaglia parte un timer: bisogna finire prima della scadenza; tenere sempre almeno una marcia in attacco per evitare il reset del boss ([riseofkingdomsguides][s16]).

### Premi principali
- Milioni di cristalli (tecnologia KvK) inviati per mail al completamento delle prove ([riseofkingdomsguides][s16]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| evoluto | Tank: Charles Martel o Richard I · Danno: i comandanti con piu' burst dell'account | [riseofkingdomsguides][s16]: evitare i comandanti Peacekeeping, usare i piu' forti con burst; i tank servono a mitigare i danni. | [riseofkingdomsguides · trial kau karuak 02/01/2026][s16] |
| F2P | La migliore coppia da burst sviluppata + un tank dedicato | Stessa logica, con le coppie disponibili. | [riseofkingdomsguides · trial kau karuak 02/01/2026][s16] |

### Trucchi (massimo punteggio, zero perdite)
- Preimpostare le truppe per schierare in fretta ([riseofkingdomsguides][s16]).
- Sommare bonus di danno da equipaggiamento, abilita', titoli e rune ([riseofkingdomsguides][s16]).
- [riseofkingdomsguides][s16] cita l'army expansion da 2.000 gemme (+50% danni): VIETATA al bot.

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| KAU-01 | Trial of Kau Karuak disponibile | Avvisare l'utente con la difficolta'/livello corrente e le marce preimpostate (tank + burst). — *Timer di battaglia e reset del boss richiedono gestione attiva.* | **sì** | [riseofkingdomsguides · trial kau karuak 02/01/2026][s16] |
| KAU-02 | Proposta di army expansion a 2.000 gemme | Rifiutare sempre. — *Vincolo MAI gemme.* | no | [riseofkingdomsguides · trial kau karuak 02/01/2026][s16] |

**Fonti della sezione:** [riseofkingdomsguides · trial kau karuak 02/01/2026][s16] · [handbook · karuak ceremony 09/09/2026][s15]

---

## 6. Barbarians e Barbarian Forts (farm Peacekeeping e rally ai forti)

**Tipo:** PvE asincrono sulla mappa (barbari: solo; forti: rally d'alleanza) · **Automazione:** autonomo per barbari e per unirsi ai rally dei forti; conferma per guidare rally o usare oggetti AP

**Sblocco:** Barbari: da inizio gioco. Forti: servono un'alleanza e un capo rally (riseofkingdomshandbook).

**Cadenza:** Giornaliera/continua (spendere l'AP che si rigenera). Riferimento: 'unisciti a ogni rally di forte' come abitudine quotidiana.

### Meccaniche
- Barbari: livelli 1-12 vicino alla citta' (livelli piu' alti su tutto il regno e sulle mappe KvK). Costo base 50 AP prima delle riduzioni (heaven-guardian).
- Catena: ogni attacco consecutivo SENZA far rientrare il comandante in citta' riduce l'AP speso di 2, fino a un massimo di 10 ([riseofkingdomsguides][s17]); le abilita' ad area possono trascinare altri barbari nello stesso scontro senza pagare un attacco separato (heaven-guardian, riseofkingdomshandbook).
- Barbarian Forts: SOLO rally (nessun attacco in solitaria). I comandanti del capo rally valgono per tutto il rally. Livelli 1-5 standard ([riseofkingdomsguides][s17] cita 1-6): 1-3 per alleanze in crescita, 4+ servono ricerca e comandanti costruiti.
- Ogni partecipante riceve sempre casse risorse, libri esperienza e speedup, in quantita' crescenti con il livello del forte e con il danno inflitto; Books of Covenant con circa il 50% di probabilita' per fascia di premio: un forte di livello 5 ne da' tipicamente 5-15 per rally (riseofkingdomshandbook).
- Nella marcia valgono solo i talenti del comandante primario (heaven-guardian).
- Books of Covenant: 20.095 in totale per il Castle 1-25, 5.000 solo per il 24->25; i forti sono la principale fonte ripetibile gratuita (heaven-guardian, 2026-09-19). Il bot non compra libri a gemme (10 gemme a libro).
- AP (heaven-guardian, valori 'comunemente documentati', da verificare sulla barra in gioco): cap base 1.500 AP secondo Lilith dalla patch 1.0.41 (la guida riporta ancora 1.000); rigenerazione ~1 AP ogni 45 s (100 AP ~1 h 15 min, 1.000 AP ~12 h 30 min); al cap la rigenerazione si ferma; oggetti di recupero da 50/100/500/1.000 AP; ricarica a gemme da 100 gemme +50 a ogni acquisto (VIETATA al bot); Shrine of Radiance +20% recupero AP; rune di recupero AP fino al ~15%.
- Solo il primario applica i talenti Peacekeeping: un comandante Peacekeeping da secondario non riduce l'AP (heaven-guardian). Lohar (epico) ha un'abilita' che aumenta fino al 70% l'EXP di tutti i comandanti dell'armata; Aethelflaed ha Quick Study (+15% EXP dai neutrali) (heaven-guardian).
- Rally falliti = AP, viaggio e cure sprecati: unirsi solo a rally con buone probabilita' di successo (heaven-guardian).

### Premi principali
- Barbari: speedup, gemme, risorse, esperienza comandanti, Arrows of Resistance (migliori sulle mappe KvK) ([riseofkingdomsguides][s17]).
- Forti: Books of Covenant (collo di bottiglia del Castle 25 -> City Hall 25 -> T5), libri esperienza, speedup, casse risorse (riseofkingdomshandbook, [riseofkingdomsguides][s17]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| F2P - forti | Boudica (primario) + Aethelflaed (secondario) | [heaven-guardian][s18]: coppia F2P con talenti Peacekeeping, danno da abilita' e debuff. | [heaven-guardian · dominate barbarians forts 03/08/2026][s18] |
| early spender / evoluto - forti | Minamoto no Yoshitsune (primario) + Cao Cao (secondario) · Belisarius come capo rally alternativo | [heaven-guardian][s18] (Minamoto + Cao Cao per early spender); [riseofkingdomshandbook][s19] e [riseofkingdomsguides][s17]: Boudica, Aethelflaed, Cao Cao, Minamoto e Belisarius sono i comandanti da forte (nuke + Peacekeeping + bonus contro barbari). | [heaven-guardian · dominate barbarians forts 03/08/2026][s18] · [handbook · barbarian forts 18/08/2026][s19] · [riseofkingdomsguides · barbarians barbarian forts 02/01/2026][s17] |
| farm barbari (tutti) | Lohar (primario, Peacekeeping) + Cao Cao / Boudica / Aethelflaed · Comandante da livellare come secondario | Lohar e' un curatore PvE che rende il farm quasi senza perdite; Rejuvenate restituisce 150 rage quando scatta la sua abilita' e 150 quando scatta quella del partner (~300 rage per ciclo). Secondario da livellare per guadagnare EXP ([heaven-guardian][s20]). | [handbook · lohar 18/08/2026][s21] · [heaven-guardian · lohars trial 08/08/2026][s20] |
| chain farm AoE | Yi Seong-Gye (danno circolare) · Aethelflaed o Boudica con Lohar | [riseofkingdomsguides][s17] consiglia YSG per il danno AoE circolare in catena; [riseofkingdomshandbook][s21]: Aethelflaed e Boudica sono i migliori partner da chain-farm di Lohar. | [riseofkingdomsguides · barbarians barbarian forts 02/01/2026][s17] · [handbook · lohar 18/08/2026][s21] |

### Talenti e formazione
- **Talenti:** Albero Peacekeeping sul primario: Insight per primo (riduce l'AP per attacco), poi Quick Study, Trophy Hunter, Domination, Thoroughbreds, Curing Chant; poi Support (Burning Blood, Rejuvenate) (riseofkingdomshandbook, build di Lohar).

### Trucchi (massimo punteggio, zero perdite)
- Non lasciare mai l'AP naturale al massimo (la rigenerazione si ferma); gli AP in bottiglia sono un budget separato da usare per un obiettivo preciso (riseofkingdomshandbook).
- Attaccare il livello di barbaro piu' alto che si batte PULITO: piu' efficiente per AP se non genera perdite da curare (riseofkingdomshandbook, Lohar's Trial).
- Catena: non avviare per sbaglio un nuovo attacco a pagamento quando si voleva solo riposizionare; controllare la detrazione AP; tornare prima che perdite o tragitto rendano lo scambio sconveniente (riseofkingdomshandbook).
- Forti: mandare sempre la marcia PIENA con la miglior coppia da forte: la quota di premi dipende dal danno (riseofkingdomshandbook).
- Guidare i rally solo quando la propria coppia da forte e' la migliore dell'alleanza (il capo applica i suoi comandanti a tutti) (riseofkingdomshandbook).
- Formazione Double Line: +10% velocita' di marcia verso i barbari ([bluestacks][s22], anniversario 2025).
- Lohar: tenerlo a una stella finche' l'abilita' attiva non e' al 5, niente equipaggiamento raro endgame su di lui; il comandante da livellare va come secondario (heaven-guardian).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| BAR-01 | AP naturale >= costo di un attacco e marcia Peacekeeping libera, nessun evento AP imminente entro 24 h | Attaccare il barbaro di livello piu' alto battibile senza perdite rilevanti (ultimo report: truppe perse < 5% - soglia del bot); restare fuori citta' e concatenare i barbari vicini. — *-2 AP per attacco consecutivo fino a -10; AP al cap = rigenerazione sprecata.* | no | [riseofkingdomsguides · barbarians barbarian forts 02/01/2026][s17] · [handbook · action points barbarian 09/09/2026][s23] · [heaven-guardian · dominate barbarians forts 03/08/2026][s18] |
| BAR-02 | Marcia in catena sotto il 60% di truppe sane o ospedale oltre l'80% | Rientrare in citta', curare, poi ripartire. — *Il ritorno costa la catena ma evita perdite/feriti oltre la capacita' d'ospedale (soglie del bot).* | no | [handbook · action points barbarian 09/09/2026][s23] |
| BAR-03 | Un evento a punti su barbari (Lohar's Trial, MGE fase barbari, Karuak, Marauders) inizia entro 24-48 h | Smettere di usare oggetti AP; spendere solo l'AP naturale in modo che la barra sia piena all'inizio dell'evento. — *Arrivare con barra piena e ricariche moltiplica i kill nella finestra dell'evento.* | no | [handbook · lohars trial 18/08/2026][s24] · [handbook · action points barbarian 09/09/2026][s23] |
| BAR-04 | L'utente sta per chiudere la sessione e (cap AP - AP attuale) x 45 s < ore fino alla prossima sessione | Spendere AP naturale in barbari finche' il tempo stimato al cap supera la durata dell'assenza (misurare il vero tempo di recupero dal timer in gioco). — *Al cap la rigenerazione si ferma; stima 1 AP/45 s da heaven-guardian (valore comunitario).* | no | [heaven-guardian · maximize action points 03/08/2026][s3] |
| BAR-05 | AP esauriti e il gioco propone la ricarica a gemme (100, 150, 200... gemme) | Rifiutare sempre. — *Vincolo MAI gemme.* | no | [heaven-guardian · maximize action points 03/08/2026][s3] |
| BAR-06 | Serve livellare un comandante e Lohar e' disponibile | Lohar primario (Peacekeeping) + comandante da livellare secondario; prima delle sessioni lunghe raccogliere una runa EXP o recupero AP se disponibile. — *Fino a +70% EXP dall'abilita' di Lohar; i talenti valgono solo da primario.* | no | [heaven-guardian · level up commanders 03/08/2026][s25] · [heaven-guardian · lohar barbarian hunter 05/08/2026][s26] |
| FORT-01 | Rally d'alleanza su un Barbarian Fort aperto e capacita' d'ospedale libera sufficiente | Se il livello del forte e' gia' stato battuto dall'alleanza con rally riusciti, unirsi con la marcia PIENA della miglior coppia da forte (primario con Peacekeeping); altrimenti non unirsi. — *Premi garantiti a ogni partecipante e proporzionali al danno; Books of Covenant.* | no | [handbook · barbarian forts 18/08/2026][s19] · [heaven-guardian · maximize action points 03/08/2026][s3] |
| FORT-02 | L'utente ha la coppia da forte migliore dell'alleanza e il forte e' di livello gia' battuto in passato | Proporre di avviare rally ai forti a orari fissi concordati con l'alleanza. — *Il capo rally applica i suoi comandanti a tutti; orari fissi aumentano la partecipazione.* | **sì** | [handbook · barbarian forts 18/08/2026][s19] |
| FORT-03 | Castle < 25 | Dare priorita' ai rally dei forti (Books of Covenant) rispetto ai barbari singoli quando l'AP e' limitato. — *I Books of Covenant limitano Castle 25, quindi City Hall 25 e T5.* | no | [handbook · barbarian forts 18/08/2026][s19] |

**Lacune:** Costo AP di un rally ai forti e limite giornaliero di premi dai forti non indicati dalle fonti lette. Tabella AP per livello di barbaro non disponibile (solo 50 AP base).

**Fonti della sezione:** [handbook · barbarian forts 18/08/2026][s19] · [riseofkingdomsguides · barbarians barbarian forts 02/01/2026][s17] · [heaven-guardian · dominate barbarians forts 03/08/2026][s18] · [handbook · action points barbarian 09/09/2026][s23] · [handbook · lohar 18/08/2026][s21] · [heaven-guardian · get books covenant 19/09/2026][s27] · [heaven-guardian · maximize action points 03/08/2026][s3] · [heaven-guardian · level up commanders 03/08/2026][s25] · [bluestacks · 7th anniversary update 16/09/2025][s22]

---

## 7. Holy Sites (Sanctum, Altar, Shrine, Lost Temple) e guardiani

**Tipo:** PvE (guardiani, rune) + PvP d'alleanza (conquista delle strutture) · **Automazione:** autonomo sui guardiani PvE; SOLO su conferma per attaccare/rinforzare strutture contese

**Sblocco:** Contesa legata all'apertura delle zone/passi del regno; per attaccare una struttura serve territorio d'alleanza collegato (theriagames).

**Cadenza:** Guardiani: 2 spawn al giorno (00:00 e 12:00 UTC, durata 11 h). Strutture: contesa ogni 3 giorni (Lost Temple ogni 7).

### Meccaniche
- Mappa del regno: 6 Zone 1, 3 Zone 2, 1 Zone 3 con il Lost Temple; la difficolta' cresce verso il centro (riseofkingdomshandbook).
- I Holy Sites danno buff permanenti a tutti i membri dell'alleanza che li controlla; buff identici dello stesso tipo NON si sommano (theriagames).
- Sanctum (Zone 1, 70 in totale, guardiani ~10.000 truppe T1): Sanctum of Courage +10% esperienza comandanti, Sanctum of Wind +5% velocita' di marcia, Sanctum of Blood +2% salute truppe, Sanctum of Hope +5% velocita' di raccolta (riseofkingdomshandbook; conteggi e guardiani da theriagames).
- Altar (37 in totale; theriagames li colloca in Zone 1; guardiani 15.000 T2): Harvest +10% produzione risorse, Earth +5% velocita' costruzione, Wisdom +5% ricerca, Storm +5% addestramento, Surge +3% difesa truppe, Flame +3% attacco truppe. Nelle battaglie agli Altar i feriti gravi vanno in ospedale (nessuna morte).
- Shrine (Zone 2, 3 per regione, 9 in totale; guardiani 30.000 T3, comandante Calvin): Radiance +20% recupero AP e +20% velocita' di cura; Order +3% difesa e +3% salute; War +3% attacco e +10% addestramento; Honor +5% attacco dei rally e +5% raccolta. Rally limitati a 1,5 milioni di unita'; META' dei feriti gravi muore subito (theriagames).
- Contesa: Sanctum/Altar/Shrine aprono alla contesa ogni 3 giorni; serve territorio d'alleanza collegato e occupazione per 4 ore consecutive. Lost Temple (Zone 3): contesa ogni 7 giorni, 8 ore di occupazione, 2 milioni di Royal Crossbowmen T5 + Temple Commanders; TUTTI i feriti gravi muoiono; il leader dell'alleanza diventa Re (theriagames).
- Guardiani: compaiono due volte al giorno alle 00:00 e 12:00 UTC e restano 11 ore (theriagames); heaven-guardian (2026) riporta un ciclo di respawn di 12 ore 'comunemente documentato' e run organizzate due volte al giorno secondo il calendario del regno. Droppano rune e raramente blueprint. EXP: Sanctum ~2.500, Altar 4.000, Shrine 7.000, Temple 10.000 (Temple guardian ~35.000 T4) (theriagames).
- Le uccisioni standard dei guardiani NON costano Action Points: sono la fonte gratuita di EXP comandanti da fare prima dei barbari (heaven-guardian).
- Rune: una sola attiva per volta (raccoglierne un'altra sostituisce subito la precedente); durata comunemente ~1 ora; colori/tier con tetti indicativi Bianca ~3%, Verde ~7%, Blu ~10%, Viola ~15%, Arancione ~20%; rune 'a inizio coda' (ricerca, costruzione, addestramento, cura: valgono se la coda parte con la runa attiva) e rune 'continue' (raccolta, recupero AP, EXP comandanti, attacco, difesa, salute, velocita' di marcia) (heaven-guardian). Le rune si sommano a titoli e buff d'alleanza (riseofkingdomshandbook).

### Premi principali
- Buff permanenti d'alleanza (tabelle sopra) (theriagames, riseofkingdomshandbook).
- Guardiani: EXP comandanti, rune temporanee, blueprint rari (theriagames, heaven-guardian).
- Quest 'The Blessed Place' per scoprire/catturare Holy Sites: boost risorse, scudi, teletrasporti, army expansion, buff attacco/difesa (theriagames).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| F2P - guardiani Sanctum/Altar | Coppia PvE Peacekeeping (Boudica/Aethelflaed o Lohar + Cao Cao) · Cao Cao con build mobilita' per prendere le rune per primi | Guardiani = unita' neutrali (EXP comandanti); le rune vanno a chi arriva prima: Cao Cao e' il comandante piu' veloce (riseofkingdomshandbook). | [handbook · map zones runes 18/08/2026][s28] · [handbook · barbarian forts 18/08/2026][s19] |
| guardian run per EXP (tutti) | Lohar primario (Peacekeeping) + comandante da livellare secondario · Alternativa: Aethelflaed, Boudica, Belisarius primari | [heaven-guardian][s25]: guardian run con runa EXP raccolta prima del primo guardiano, Lohar primario e comandante da sviluppare secondario. | [heaven-guardian · level up commanders 03/08/2026][s25] |
| raccolta rune | Marcia piccola e veloce: comandante cavalleria/mobilita' con talenti velocita' + poche truppe T1 di cavalleria | [heaven-guardian][s29]: non mandare un esercito intero a prendere una runa. | [heaven-guardian · runes find use 03/08/2026][s29] |
| evoluto - Shrine/Temple guardian | Coppia da danno AoE con sostegno (capo rally con AoE e sustain) | [theriagames][s30]: per gli Shrine scegliere un capo rally con forte AoE e sostenibilita'; i guardiani Shrine hanno 30.000 T3. | [theriagames · shrines 13/02/2025][s30] |

### Trucchi (massimo punteggio, zero perdite)
- Restare in Zone 1 finche' i comandanti non reggono Zone 2 (riseofkingdomshandbook).
- Prendere le rune poco prima di un rally o di una sessione di raccolta: sono temporanee e si sommano a titoli e buff d'alleanza (riseofkingdomshandbook, heaven-guardian).
- Scegliere Holy Sites diversi (buff uguali non si sommano) (theriagames).
- Sanctum of Courage (+10% EXP comandanti) e' il migliore per un'alleanza che livella comandanti (riseofkingdomshandbook).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| HS-01 | Finestra guardiani attiva (00:00-11:00 o 12:00-23:00 UTC), guardiano Sanctum/Altar raggiungibile senza uscire dalla zona sicura e marcia PvE con truppe >= requisito (10k T1 / 15k T2) | Attaccare il guardiano con la marcia PvE; se cade una runa, raccoglierla con la marcia piu' veloce solo se servira' entro la sua durata. — *PvE su unita' neutrali: EXP, rune, blueprint rari.* | no | [theriagames · holy sites 13/02/2025][s31] · [handbook · map zones runes 18/08/2026][s28] |
| HS-02 | Guardiano di Shrine o Temple (30k T3 / 35k T4) oppure truppe sotto il requisito | Non attaccare da solo; proporre all'utente un rally d'alleanza o saltare. — *Rischio di perdite elevate.* | **sì** | [theriagames · holy sites 13/02/2025][s31] |
| HS-03 | Richiesta d'alleanza di attaccare, occupare o rinforzare una struttura (Sanctum/Altar/Shrine/Pass/Lost Temple) contesa o occupata da un'altra alleanza | Chiedere SEMPRE conferma mostrando il rischio: Altar = feriti in ospedale; Shrine = meta' dei feriti gravi muore; Lost Temple = tutti i feriti gravi muoiono. — *Azione PvP contro giocatori + perdite permanenti.* | **sì** | [theriagames · shrines 13/02/2025][s30] · [theriagames · altar 13/02/2025][s32] · [theriagames · holy sites 13/02/2025][s31] |
| HS-04 | Holy Site dell'alleanza entra in finestra di contesa (ogni 3 giorni; 7 per il Lost Temple) | Avvisare l'utente: tenere la marcia in citta' e l'ospedale libero per 4 ore (8 per il Lost Temple) nel caso l'alleanza chieda rinforzi. — *Il controllo richiede 4 ore consecutive di occupazione.* | no | [theriagames · holy sites 13/02/2025][s31] |
| HS-05 | Guardian run annunciata dall'alleanza/regno | Prima del primo guardiano raccogliere una runa EXP se presente; marciare con Lohar primario + comandante da livellare; attendere il gruppo prima di attaccare; rispettare i limiti di marce indicati. — *EXP gratuita senza costo AP; etichetta delle guardian run.* | no | [heaven-guardian · level up commanders 03/08/2026][s25] |
| HS-06 | Rune disponibili vicino a un Holy Site | Raccogliere SOLO se l'attivita' collegata parte entro l'ora (rune di coda: aprire la coda, verificare che il timer sia sceso, poi confermare); non sostituire una runa attiva ancora utile; usare la marcia piccola e veloce. — *Una runa per volta, durata ~1 h; le rune di coda valgono solo all'avvio.* | no | [heaven-guardian · runes find use 03/08/2026][s29] |

**Lacune:** Nessuna fonte 2026 letta con la lista completa dei buff di Altar/Shrine: i dati vengono da theriagames (febbraio 2025). Perdite nelle battaglie contro i guardiani (feriti vs morti) non indicate. La pagina riseofkingdomsguides.com/holy-sites/ risponde 404.

**Fonti della sezione:** [handbook · map zones runes 18/08/2026][s28] · [theriagames · holy sites 13/02/2025][s31] · [theriagames · shrines 13/02/2025][s30] · [theriagames · altar 13/02/2025][s32] · [heaven-guardian · runes find use 03/08/2026][s29] · [heaven-guardian · level up commanders 03/08/2026][s25] · [heaven-guardian · zones 08/08/2026][s33]

---

## 8. Lohar's Trial

**Tipo:** Evento PvE su barbari (Peacekeeping) + rally d'alleanza sul boss evocato · **Automazione:** autonomo sul farm; conferma per oggetti AP e per annunci in chat

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Circa una volta al mese, 2 giorni (riseofkingdomshandbook). heaven-guardian e [riseofkingdomsguides][s34] non danno durata.

### Meccaniche
- Durante l'evento i barbari normali della mappa droppano Bone Necklaces (riseofkingdomshandbook, heaven-guardian).
- Bone Necklaces: cibo, legno, speedup da 5 minuti, gemme, Arrows of Resistance e relic Lohar's Longbow / Lohar's Buckler. Non scadono (heaven-guardian).
- Lohar's Longbow evoca Junior Lohar vicino alla citta'; Lohar's Buckler (piu' raro) evoca Dauntless Lohar. L'armata di Lohar si batte SOLO con rally d'alleanza; chi partecipa riceve premi, tra cui sculture di Lohar (heaven-guardian; solo rally: [riseofkingdomsguides][s34]).

### Premi principali
- Sculture di Lohar (dai regali del boss evocato), gemme, speedup, Arrows of Resistance, risorse (riseofkingdomshandbook, heaven-guardian, [riseofkingdomsguides][s34]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| F2P | Lohar + Cao Cao · Boudica / Aethelflaed con talenti Peacekeeping | Coppia Peacekeeping economica: la riduzione AP dell'albero Peacekeeping aumenta direttamente i kill per evento (riseofkingdomshandbook). | [handbook · lohars trial 18/08/2026][s24] · [handbook · lohar 18/08/2026][s21] |
| evoluto | Minamoto no Yoshitsune o Belisarius (primario Peacekeeping) · Secondario = comandante da livellare | [heaven-guardian][s20] elenca Lohar, Boudica, Aethelflaed, Belisarius, Cao Cao, Minamoto come priorita' Peacekeeping; il secondario guadagna EXP mentre si farma. | [heaven-guardian · lohars trial 08/08/2026][s20] |

### Talenti e formazione
- **Talenti:** Peacekeeping: Insight (meno AP per attacco), Quick Study (piu' EXP dai neutrali), Trophy Hunter (piu' risorse), Curing Chant (cure per catene piu' lunghe) (heaven-guardian).

### Trucchi (massimo punteggio, zero perdite)
- Arrivare alla finestra di 2 giorni con AP pieno e oggetti AP pronti; la leva piu' grande sul numero di collane (riseofkingdomshandbook).
- heaven-guardian: non svuotare TUTTA la riserva AP solo perche' l'evento e' attivo (conflitto di enfasi con riseofkingdomshandbook: vedi conflicts).
- Tenere le marce fuori citta' in catena; non rientrare dopo ogni kill (heaven-guardian).
- Aprire le relic durante l'evento (nessun bonus a conservarle), annunciarle in chat e aiutare nei rally degli altri (riseofkingdomshandbook).
- [riseofkingdomsguides][s34]: una volta maxato Lohar, preferire i forti (Books of Covenant) alle ulteriori armate di Lohar.
- Lohar e' epico: le sue sculture arrivano gratis da questo evento circa ogni mese (riseofkingdomshandbook); la sua abilita' aumenta fino al 70% l'EXP dei comandanti dell'armata (heaven-guardian), quindi completarlo accelera tutto il farm.

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| LOH-01 | Lohar's Trial annunciato entro 48 h | Applicare BAR-03 (barra AP piena all'avvio, niente oggetti AP). — *Piu' AP nella finestra = piu' collane.* | no | [handbook · lohars trial 18/08/2026][s24] |
| LOH-02 | Lohar's Trial attivo e AP naturale disponibile | Farm continuo di barbari in catena con la coppia Peacekeeping; aprire le Bone Necklaces durante l'evento, quando l'alleanza e' attiva per i rally sulle relic. — *Le collane droppano solo dai barbari normali durante l'evento; non scadono (heaven-guardian), ma le relic vanno usate nella finestra dell'evento (riseofkingdomshandbook).* | no | [heaven-guardian · lohars trial 08/08/2026][s20] · [handbook · lohars trial 18/08/2026][s24] |
| LOH-03 | AP naturale esaurito durante l'evento | Proporre all'utente quanti oggetti AP usare (default: fino al 50% della scorta). — *heaven-guardian: non svuotare tutta la riserva; gli oggetti AP sono consumabili rari.* | **sì** | [heaven-guardian · lohars trial 08/08/2026][s20] |
| LOH-04 | Si ottiene Lohar's Longbow o Lohar's Buckler | Chiedere all'utente l'orario d'uso (ore di punta dell'alleanza); poi usare la relic, annunciare in chat e aprire il rally (o chiedere a un capo rally). — *Il boss si batte solo in rally; la chat e' comunicazione a nome dell'utente.* | **sì** | [heaven-guardian · lohars trial 08/08/2026][s20] · [riseofkingdomsguides · lohars trial event 02/01/2026][s34] |
| LOH-05 | Rally d'alleanza aperto su un'armata di Lohar | Unirsi con una marcia piena (e' PvE). — *Tutti i partecipanti ricevono premi, incluse sculture di Lohar.* | no | [handbook · lohars trial 18/08/2026][s24] |
| LOH-06 | Mancano meno di 2 ore alla fine e restano relic in inventario | Avvisare l'utente per usarle subito. — *Nessun bonus a conservarle; l'evento finisce.* | **sì** | [handbook · lohars trial 18/08/2026][s24] |

**Lacune:** Requisito di sblocco e livelli/forza dell'armata di Lohar evocata non indicati. Probabilita' di drop delle relic non indicate.

**Fonti della sezione:** [handbook · lohars trial 18/08/2026][s24] · [heaven-guardian · lohars trial 08/08/2026][s20] · [riseofkingdomsguides · lohars trial event 02/01/2026][s34] · [heaven-guardian · level up commanders 03/08/2026][s25] · [handbook · best epic commanders 18/08/2026][s35]

---

## 9. Arms Training (Armsmaster Lohar)

**Tipo:** PvE individuale a punteggio (classifica) · **Automazione:** assistito (scelta dei modificatori) - i tentativi base possono essere automatizzati come test

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Evento a rotazione; incluso negli eventi dell'Anniversary 1.1.11 (27-08-2026, [ldshop][s36]); 3 giorni con 5 tentativi al giorno ([riseofkingdomsguides][s37]).

### Meccaniche
- Si sconfigge ripetutamente Lohar, che diventa piu' forte a ogni vittoria; dopo ogni sconfitta il giocatore sceglie quale nuova abilita'/modificatore Lohar sblocca ([riseofkingdomsguides][s37], heaven-guardian).
- 3 giorni, 5 tentativi al giorno; 10.000 punti per ogni sconfitta di Lohar; gli stage normali valgono al massimo 300.000 punti, poi la Legend Mode assegna punti in base alle truppe rimaste ([riseofkingdomsguides][s37]).
- Modificatori citati: Thrill of Battle, Armor of Thorns, Strike of Vengeance; alcune descrizioni nel riferimento sono duplicate o incoerenti: leggere la carta in gioco ([riseofkingdomshandbook][s38]).
- Lohar ha un'abilita' che riduce del 20% i danni subiti dagli arcieri; i bonus di danno contro barbari di abilita' ed equipaggiamento non valgono contro di lui ([riseofkingdomsguides][s37]); [riseofkingdomshandbook][s38]: verificare in gioco quali bonus Peacekeeping/barbari/equipaggiamento si applicano.

### Premi principali
- Top 10: blueprint leggendari dell'elmo; posizioni inferiori: materiali generici ([riseofkingdomsguides][s37]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| evoluto | Genghis Khan + Yi Seong-Gye ('the best pair') | [riseofkingdomsguides][s37]. | [riseofkingdomsguides · arms training event 02/01/2026][s37] |
| F2P / medio | Coppia di cavalleria con alto burst (la piu' sviluppata) · Alexander e Joan of Arc su barbari vicini per i buff alle truppe (riseofkingdomsguides) | Lohar riduce i danni degli arcieri; [riseofkingdomshandbook][s38]: partire dalla coppia completa gia' posseduta e trovarne il punto di rottura, non comprare un leggendario per copiare un vecchio report. | [riseofkingdomsguides · arms training event 02/01/2026][s37] · [handbook · arms training 09/09/2026][s38] |

### Trucchi (massimo punteggio, zero perdite)
- Primi tentativi (giorni 1-2) = test: registrare coppia, truppe, buff, carte scelte e truppe rimaste a ogni checkpoint; cambiare UNA variabile alla volta ([riseofkingdomshandbook][s38], [riseofkingdomsguides][s37]).
- Scegliere per primi i modificatori meno dannosi per la propria marcia (scaling nel tempo, ritorsione ai danni da abilita', contrattacchi, scudi/cure) ([riseofkingdomshandbook][s38]).
- Decidere prima se si punta alle milestone o alla classifica: budget diversi ([riseofkingdomshandbook][s38]).
- [riseofkingdomsguides][s37] suggerisce army expansion al 50% il giorno 3: per il bot solo se l'oggetto e' gia' posseduto e con conferma, MAI a gemme.

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| ARM-01 | Arms Training attivo, giorni 1-2 | Usare i tentativi giornalieri come test con la coppia migliore e buff gratuiti; salvare un log (coppia, carte, truppe rimaste). — *Il primo run e' informazione.* | no | [handbook · arms training 09/09/2026][s38] · [riseofkingdomsguides · arms training event 02/01/2026][s37] |
| ARM-02 | Dopo ogni vittoria il gioco chiede di scegliere il modificatore di Lohar | Scegliere secondo la tabella: evitare 'ritorsione su danni da abilita'' se la coppia e' a base di abilita', evitare 'contrattacchi piu' forti' se la coppia vive di attacchi normali; in dubbio chiedere all'utente. — *L'ordine dei modificatori va adattato ai punti deboli della marcia.* | no | [handbook · arms training 09/09/2026][s38] |
| ARM-03 | Proposta di usare army expansion/consumabili di danno per la classifica | Chiedere conferma mostrando milestone gia' raggiungibili vs guadagno atteso; mai acquistare con gemme. — *Consumabili rari; la classifica richiede budget dedicato.* | **sì** | [handbook · arms training 09/09/2026][s38] · [riseofkingdomsguides · arms training event 02/01/2026][s37] |

**Lacune:** Requisito di sblocco e tabella completa dei premi a milestone non indicati. Formula esatta del punteggio Legend Mode nel 2026 (riseofkingdomshandbook invita a verificarla in gioco).

**Fonti della sezione:** [riseofkingdomsguides · arms training event 02/01/2026][s37] · [handbook · arms training 09/09/2026][s38] · [ldshop · anniversary special 27/08/2026][s36]

---

## 10. Protect the Supplies (scorta carovana individuale)

**Tipo:** PvE individuale a stelle (evento stagionale) · **Automazione:** semi-autonomo (AP) con conferma sulla difficolta'

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Stagionale (Summer of Passion); durata non indicata.

### Meccaniche
- Evento individuale: si difende una carovana dai barbari; solo tu puoi difenderla ([riseofkingdomsguides][s39]).
- Si spendono 50 AP per evocare una missione di carovana; difficolta' da 3 a 5 stelle; si puo' riprovare ma conta solo il risultato migliore (punteggio = totale stelle) ([riseofkingdomsguides][s39]).
- Parte del pacchetto Summer of Passion ([riseofkingdomsguides][s39]).

### Premi principali
- Premi a soglie di stelle (1, 4, 8, 12+ stelle: risorse, AP, chiavi, speedup, nettari); top 10 in classifica: sculture di comandanti 'golden' ([riseofkingdomsguides][s39]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| tutti | Nessuna coppia indicata dalla fonte: usare la marcia PvE piu' forte (danno ad area contro barbari) | La fonte non da' comandanti; indicazione generica del bot coerente con il farm barbari. | [riseofkingdomsguides · protect supplies event 02/01/2026][s39] |

### Trucchi (massimo punteggio, zero perdite)
- Costo fisso 50 AP per tentativo: fare prima il livello di difficolta' sicuro, poi salire ([riseofkingdomsguides][s39]; ordine di difficolta': scelta del bot).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| SUP-01 | Protect the Supplies attivo e AP >= 50 | Proporre all'utente la difficolta' (default la piu' alta gia' completata); ogni tentativo costa 50 AP; fermarsi quando il miglior risultato non migliora in 2 tentativi. — *Conta solo il miglior risultato; l'AP e' limitato.* | **sì** | [riseofkingdomsguides · protect supplies event 02/01/2026][s39] |

**Lacune:** Evento documentato solo da una pagina riseofkingdomsguides (contenuto datato, lastmod 2026-01-02); presenza nel calendario 2026 non verificata. Requisito di sblocco e durata non indicati.

**Fonti della sezione:** [riseofkingdomsguides · protect supplies event 02/01/2026][s39]

---

## 11. Sunset Canyon

**Tipo:** PvP asincrono contro difese salvate (truppe simulate, rischio zero) · **Automazione:** autonomo (nessuna perdita reale, nessuna gemma)

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Giornaliera (5 tentativi gratis prima del reset) dentro stagioni di 7 giorni; punti azzerati a fine stagione.

### Meccaniche
- Formazione di battaglia separata e truppe simulate: si testano piazzamenti senza perdere l'esercito reale (riseofkingdomshandbook).
- Truppe: riseofkingdomsguides dice che tutti hanno la stessa quantita' di truppe T3 e contano solo equipaggiamento, abilita' e talenti dei comandanti; riseofkingdomshandbook precisa che il tier standard NON implica la stessa capacita' per marcia (dipende dallo sviluppo dei comandanti): vedi conflicts.
- Solo i talenti del comandante PRIMARIO si applicano (riseofkingdomshandbook).
- 5 tentativi gratuiti al giorno; tentativi extra con Challenge Tickets; stagione di 7 giorni. Chi vince guadagna punti, chi perde ne perde; in caso di pareggio vince chi ha piu' truppe rimaste (riseofkingdomsguides).
- Si puo' ispezionare la formazione del difensore prima di attaccare; gli avversari vedono la tua difesa allo stesso modo (riseofkingdomshandbook).
- Le armate attaccano prima il nemico di fronte, poi il piu' vicino; nessun intervento durante lo scontro ([allclash][s40]).

### Premi principali
- Premi giornalieri in base ai punti accumulati; premi di fine stagione in base alla posizione (riseofkingdomsguides).
- Guida F2P di riseofkingdomshandbook: truppe equalizzate, conta l'investimento nei comandanti; 'a real source of equipment materials'. La guida Ian's Ballads dello stesso sito mette il Canyon, con Ian's Ballads e Ceroli Crisis, tra le fonti di equipaggiamento dei F2P.

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| F2P - attacco/difesa iniziale (5 marce) | Fronte, scontro principale: Scipio Africanus (epico) -> Sun Tzu · Fronte, corsia adiacente: Pelagius -> Baibars · Retro dietro lo scontro principale: Aethelflaed -> Joan of Arc (epica) · Retro dietro la corsia adiacente: Kusunoki Masashige -> Imhotep · Lato esposto: Eulji Mundeok -> Osman I | Lineup di partenza di [riseofkingdomshandbook][s41] per un account con epici sviluppati e Aethelflaed dall'Expedition; Charles Martel sviluppato puo' sostituire un tank frontale. E' un esercizio di posizionamento, non una garanzia. | [handbook · sunset canyon 09/09/2026][s41] |
| F2P - coppie consigliate | Sun Tzu e Joan of Arc come comandanti 'first-skill' · Charles Martel + Scipio Africanus (tank da Canyon) · Saladin + Baibars (statistiche e AoE) · Cao Cao primario (cavalleria) · Aethelflaed: unico leggendario consigliato ai F2P | Citazioni di riseofkingdomsguides (guida Canyon e pagina pairings): puntare soprattutto sugli epici. | [riseofkingdomsguides · sunset canyon 02/01/2026][s42] · [riseofkingdomsguides · commander pairings 02/01/2026][s43] |
| 2026 - coppie Canyon (heaven-guardian) | Charles Martel (primario, tank frontale) + Sun Tzu · Charles Martel + Richard I (massima durabilita') · Aethelflaed (primaria) + Baibars · Aethelflaed (primaria) + Yi Seong-Gye (debuff prima dell'AoE circolare) · Saladin + Baibars (budget, AoE e rallentamento) | heaven-guardian 2026: Aethelflaed 'useful' nel Canyon (debuff su 5 bersagli); Charles Martel 'usually primary' come tank del Canyon; YSG ancora utile nel Canyon; Saladin + Baibars 'budget field or Canyon'. Coppie legacy: valide se gia' sviluppate, non motivo per nuovi investimenti. | [heaven-guardian · aethelflaed talents pairings 06/08/2026][s9] · [heaven-guardian · charles martel talents 03/08/2026][s44] · [heaven-guardian · yi seong gye 06/08/2026][s45] · [heaven-guardian · saladin builds pairings 06/08/2026][s46] · [heaven-guardian · best commander pairings 12/08/2026][s8] |
| evoluto | Boudica Prime · Tank: Richard I, Charles Martel · AoE: Yi Seong-Gye, Mehmed II · Nuke: Minamoto no Yoshitsune, Genghis Khan · Supporto: Joan of Arc | Boudica Prime 'molto potente' nel Canyon ([riseofkingdomsguides][s42]); ruoli e nomi da [allclash][s40] (guida del 2020: meta datato, usare come base). | [riseofkingdomsguides · sunset canyon 02/01/2026][s42] · [allclash · sunset canyon tactics 21/02/2020][s40] |
| difesa (schema) | 3 armate: 1-2 tank · 4 armate: 2 tank · 5 armate: 2-3 tank · Dietro: AoE e supporto per colpire i nemici ammassati | Schema difensivo di [allclash][s40]; l'obiettivo e' una difesa generale difficile da isolare, non prevedere ogni attacco. | [allclash · sunset canyon tactics 21/02/2020][s40] |

### Talenti e formazione
- **Talenti:** Aethelflaed nel Canyon: Support + Leadership (fino a Rejuvenate e Cage of Thorns); Charles Martel 'Sunset Canyon Tank Build': spostare punti dalla velocita' a durabilita', Rage e contrattacco (priorita': restare vivo in prima linea, cicli di scudo, danno da contrattacco, meno danni da abilita' subiti, proteggere la retroguardia) (heaven-guardian).
- **Formazione:** Wedge come formazione di partenza pratica per una marcia a base di abilita' guidata da Aethelflaed; nel Canyon privilegiare sopravvivenza e tempo di attivita' dei debuff (heaven-guardian).

### Trucchi (massimo punteggio, zero perdite)
- Registrare la capacita' di truppe mostrata per ogni marcia e cambiare UN comandante o livello alla volta (riseofkingdomshandbook).
- Leggere la difesa avversaria: fronte piu' forte, marce di danno esposte, primi scontri; guardare il replay e individuare la prima marcia che cade (riseofkingdomshandbook).
- Proteggere la corsia del supporto (es. Aethelflaed); se un fianco crolla subito, spostare il miglior danno li' lo fa solo diventare la prossima vittima (riseofkingdomshandbook).
- Non spendere sculture universali leggendarie per una lineup da Canyon (riseofkingdomshandbook).
- Livellare i comandanti da Canyon con l'EXP gratuita dei guardiani (riseofkingdomsguides).
- Tenere i Challenge Tickets per l'ultimo giorno di stagione (riseofkingdomsguides), verificando pero' la validita' scritta sull'oggetto (riseofkingdomshandbook).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| SC-01 | Ogni giorno, prima del reset, tentativi gratuiti Canyon > 0 | Usare tutti i 5 tentativi gratuiti: ispezionare i difensori proposti (il bot ne confronta fino a 3) e attaccare quello con il fronte piu' debole rispetto alla propria linea; mai comprare tentativi con gemme. — *Rischio zero (truppe simulate) e premi giornalieri a punti.* | no | [riseofkingdomsguides · sunset canyon 02/01/2026][s42] · [handbook · sunset canyon 09/09/2026][s41] |
| SC-02 | Attacco perso | Guardare il replay, identificare la prima marcia caduta, cambiare UNA sola variabile (posizione o coppia) e riprovare su un avversario simile; salvare nel log il risultato. — *Metodo di confronto di riseofkingdomshandbook.* | no | [handbook · sunset canyon 09/09/2026][s41] |
| SC-03 | Challenge Tickets in inventario | Leggere la descrizione/validita': se non scadono prima, usarli l'ultimo giorno della stagione per la spinta in classifica; se scadono prima, usarli prima della scadenza. — *riseofkingdomsguides consiglia l'ultimo giorno; riseofkingdomshandbook avverte di non presumere una scadenza.* | no | [riseofkingdomsguides · sunset canyon 02/01/2026][s42] · [handbook · sunset canyon 09/09/2026][s41] |
| SC-04 | Dopo un level-up/cambio abilita' dei comandanti usati in difesa, o almeno una volta a stagione | Aggiornare la formazione difensiva: 2-3 tank davanti (con 5 marce), AoE e supporto dietro, nessuna marcia di danno isolata sul fianco. — *Gli avversari ispezionano la tua difesa.* | no | [allclash · sunset canyon tactics 21/02/2020][s40] · [handbook · sunset canyon 09/09/2026][s41] |
| SC-05 | Un miglioramento Canyon richiederebbe sculture (anche universali) o libri | Non procedere: proporre all'utente, con la priorita' dell'account. — *Materiali rari; il Canyon non giustifica da solo l'investimento.* | **sì** | [handbook · sunset canyon 09/09/2026][s41] |
| SC-06 | Premio giornaliero o di fine stagione disponibile | Riscuotere. — *Premi gratuiti.* | no | [riseofkingdomsguides · sunset canyon 02/01/2026][s42] |

**Lacune:** Livello di City Hall di sblocco e numero di marce Canyon per livello non verificati (riseofkingdomsguides cita City Hall 22 solo come aiuto per il top 50-100). Contenuto del negozio/valuta del Canyon non indicato dalle fonti lette. Nessuna lineup 'meta 2026' per account evoluti (legendary SoC) da fonte 2026: le guide Canyon dedicate di heaven-guardian e ldshop rispondono 404/non trovate; le coppie 2026 disponibili sono epiche/legacy.

**Fonti della sezione:** [handbook · sunset canyon 09/09/2026][s41] · [handbook · f2p 18/08/2026][s47] · [handbook · ians ballads 09/09/2026][s13] · [riseofkingdomsguides · sunset canyon 02/01/2026][s42] · [allclash · sunset canyon tactics 21/02/2020][s40] · [riseofkingdomsguides · commander pairings 02/01/2026][s43] · [heaven-guardian · aethelflaed talents pairings 06/08/2026][s9] · [heaven-guardian · charles martel talents 03/08/2026][s44]

---

## 12. Ark of Osiris

**Tipo:** PvP d'alleanza 30v30 programmato (truppe ferite, non morte) · **Automazione:** solo avviso/preparazione: il bot non si registra ne' combatte

**Sblocco:** City Hall 16+ per il singolo; alleanza con >10 flag e top 20 del regno per potenza ([riseofkingdomshandbook][s48]).

**Cadenza:** [riseofkingdomsguides][s49]: 'almost every two weeks'; [riseofkingdomshandbook][s48]: usare il calendario di registrazione mostrato per l'alleanza, non un'etichetta settimanale generica.

### Meccaniche
- Battaglia 30 contro 30 su mappa separata; ingresso individuale City Hall 16+; l'alleanza deve avere piu' di 10 flag ed essere tra le prime 20 del regno per potenza per iscriversi ([riseofkingdomshandbook][s48]).
- Le strutture producono punti d'alleanza finche' sono tenute; l'Ark compare al centro: scortarla a una struttura controllata da' un grosso bonus, crescente a ogni ricomparsa (le Ark tardive valgono di piu'). Le uccisioni danno punti individuali ([riseofkingdomshandbook][s48]).
- Truppe ferite e non uccise: si paga in speedup di cura ([riseofkingdomshandbook][s48]); [heaven-guardian][s50]: combattimento 'protetto', verificare le regole correnti.
- Campi Golden e Silver per forza delle alleanze; slot da coordinatore per la leadership ([riseofkingdomshandbook][s48]).
- La prima occupazione di un Obelisk da' 8 teletrasporti d'alleanza; formati: standard, practice, league e Raging Sands (tempeste di sabbia e visibilita' ridotta) ([heaven-guardian][s50]).
- Gioco a 3 corsie (centro = Ark, edificio alto e basso) o a 5 corsie per giocatori meno potenti con piu' compiti ([riseofkingdomsguides][s49]).

### Premi principali
- Premi in base a partecipazione e risultato (materiali e risorse di progressione); la presenza vale piu' del saltarla ([riseofkingdomshandbook][s48]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| Ark carrier / cattura Obelisk | Belisarius per prendere l'Ark · Marcia Dragon Lancer per catturare un Obelisk · Cavalleria T1 = unita' piu' veloci | [riseofkingdomsguides][s49]: Belisarius per raccogliere l'Ark, Dragon Lancer per gli Obelisk, 'T1 cavalry units are the fastest'; [heaven-guardian][s50]: il carrier deve unire velocita' e resistenza e consegnare, non combattere. | [riseofkingdomsguides · ark osiris strategy 02/01/2026][s49] · [heaven-guardian · ark osiris dominate 04/08/2026][s50] |
| Field fighter | Charles Martel · Yi Seong-Gye | Marce da combattimento citate da [riseofkingdomsguides][s49]. | [riseofkingdomsguides · ark osiris strategy 02/01/2026][s49] |
| Gatherer (risorse sulla mappa Osiris) | Sarka · Joan of Arc · Constance · Centurion | [riseofkingdomsguides][s49]; [heaven-guardian][s50] cita Sarka, Constance, Joan of Arc. | [riseofkingdomsguides · ark osiris strategy 02/01/2026][s49] · [heaven-guardian · ark osiris dominate 04/08/2026][s50] |
| Structure holder / rally leader | Coppia da guarnigione per tenere le strutture · Le 1-2 migliori coppie da rally dell'alleanza per rompere le guarnigioni | [riseofkingdomshandbook][s48]: la guarnigione vuole una coppia difensiva, non il capo rally. | [handbook · ark osiris 09/09/2026][s48] |
| evoluto - tenuta strutture 2026 | Heraclius + Yi Sun-sin (Leadership) | [ldshop][s51] (settembre 2026): coppia per 'Extreme Structural Survival' negli obiettivi di Ark of Osiris, tiene in vita gli edifici piu' a lungo di quasi ogni altra coppia. | [ldshop · kvk defense 22/09/2026][s51] |

### Trucchi (massimo punteggio, zero perdite)
- Tenere le strutture dall'inizio: i punti si accumulano nel tempo ([riseofkingdomshandbook][s48]).
- Scortare sempre il carrier; valorizzare le Ark tardive; non inseguire marce in fuga; focus fire ([riseofkingdomshandbook][s48]).
- Svuotare l'ospedale prima dell'evento e massimo 3 marce attive; [riseofkingdomsguides][s49] chiede un'army expansion di almeno il 25% (per il bot: solo oggetti gia' posseduti e con conferma, mai gemme).
- Assegnare ruoli prima dell'ingresso (gruppo cattura rapida, guarnigione, rally, campo, riserva) e seguire l'ordine di teletrasporto del caller ([riseofkingdomshandbook][s48]).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| AOO-01 | Registrazione Ark of Osiris aperta nell'alleanza | Notificare l'utente con orario (UTC e locale) e ruolo suggerito in base al roster (carrier se ha Belisarius/cavalleria veloce, gatherer se ha Sarka/Constance, guarnigione se ha una coppia difensiva). — *Il roster lo sceglie la leadership; la partecipazione conta per restare in alleanza.* | **sì** | [handbook · ark osiris 09/09/2026][s48] · [riseofkingdomsguides · ark osiris strategy 02/01/2026][s49] |
| AOO-02 | Utente confermato nel roster e mancano meno di 2 ore alla partita | Preparare: ospedale vuoto, marce preimpostate per il ruolo, lista speedup di cura disponibili; nessun acquisto di boost/army expansion a gemme. — *Le truppe vengono curate a costo di speedup.* | no | [riseofkingdomsguides · ark osiris strategy 02/01/2026][s49] · [handbook · ark osiris 09/09/2026][s48] |
| AOO-03 | Durante la partita | Nessuna azione autonoma (PvP in tempo reale): solo promemoria delle regole (strutture, scorta, focus, niente inseguimenti). — *Azione contro giocatori.* | **sì** | [handbook · ark osiris 09/09/2026][s48] |
| AOO-04 | Partita finita | Riscuotere i premi e riportare all'utente gli speedup di cura spesi. — *Controllo del budget.* | no | [handbook · ark osiris 09/09/2026][s48] |

**Lacune:** Valori dei punti per struttura/Ark e premi esatti: le fonti rimandano al pannello evento.

**Fonti della sezione:** [handbook · ark osiris 09/09/2026][s48] · [heaven-guardian · ark osiris dominate 04/08/2026][s50] · [riseofkingdomsguides · ark osiris strategy 02/01/2026][s49]

---

## 13. Champions of Olympia

**Tipo:** PvP 5v5 in tempo reale in stile MOBA (truppe dell'evento) · **Automazione:** solo avviso: il bot non gioca

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Finestre attive dal pannello Events ([riseofkingdomshandbook][s52]: registrarle insieme agli impegni d'alleanza).

### Meccaniche
- 5 contro 5, tre marce per giocatore, 10 minuti; vince chi ha piu' punti dal controllo delle bandiere ([riseofkingdomshandbook][s52], [riseofkingdomsguides][s53]).
- 5 bandiere: una vicino a ciascuna base, sinistra, destra, centro; si cattura tenendola 5 secondi; punti continui finche' la si tiene; cerchi di recupero vicino alle bandiere catturate (20 s) ([riseofkingdomsguides][s53]).
- Il comandante scelto decide il tipo di truppa (Richard fanteria, El Cid arcieri, Boudica assedio); il numero di truppe dipende da talenti, livello VIP e City Hall; il morale e' una risorsa ([riseofkingdomshandbook][s52]).
- Sistema di abilita' separato: [riseofkingdomshandbook][s52] lo descrive per tipo di unita' (Infantry/Cavalry/Archer/Mixed) con Power/Tactical/Support Skills; [riseofkingdomsguides][s53] (versione precedente) con Cornerstone (All Out, Master of Battlefield, Bloodlust), Secondary e Common Skills (Field Surgery, Swift March).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| 2026 per ruolo (heaven-guardian) | Difensori di bandiera: Richard I, Charles Martel, Alexander the Great, Scipio Africanus Prime, Liu Che · Roamer: Cao Cao, Minamoto no Yoshitsune, Saladin, Alexander Nevsky, Joan of Arc Prime · Danno/centro: Sun Tzu, Yi Seong-Gye, Aethelflaed, Zhuge Liang, Hermann Prime, Boudica Prime · Supporto: Joan of Arc, Aethelflaed, Constantine, Trajan | Scelte di [heaven-guardian][s54] (2026-08-05); ricontrollare la composizione mostrata dopo ogni modifica della marcia. | [heaven-guardian · champions olympia tips 05/08/2026][s54] |
| F2P | Tre lavori: tenere il punto conteso (durabilita'), danno principale (AoE o focus), rotazione/rinforzo (mobilita') | Modalita' pensata per essere F2P-friendly: contano strategia e squadra ([riseofkingdomshandbook][s52]). | [handbook · champions olympia 09/09/2026][s52] |

### Trucchi (massimo punteggio, zero perdite)
- Draft di squadra per coprire i tipi di truppa ([riseofkingdomshandbook][s52]).
- Gestire il morale; usare tutte e tre le marce ([riseofkingdomshandbook][s52]).
- In vantaggio: far venire l'avversario; in svantaggio: ruotare insieme verso uno scontro vincibile ([riseofkingdomshandbook][s52]).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| COO-01 | Finestra Champions of Olympia attiva | Avvisare l'utente e suggerire 3 marce (tenuta/danno/rotazione) tra i comandanti posseduti in base alla lista di ruolo. — *PvP in tempo reale: il bot non gioca.* | **sì** | [handbook · champions olympia 09/09/2026][s52] · [heaven-guardian · champions olympia tips 05/08/2026][s54] |

**Lacune:** Premi e requisiti di sblocco non indicati dalle fonti lette. Esistenza e regole della modalita' ranked nel 2026 non chiarite (riseofkingdomsguides: nessun ranking; riseofkingdomshandbook parla di setup ranked).

**Fonti della sezione:** [handbook · champions olympia 09/09/2026][s52] · [heaven-guardian · champions olympia tips 05/08/2026][s54] · [riseofkingdomsguides · champions olympia 02/01/2026][s53]

---

## 14. Osiris League (scommesse)

**Tipo:** Evento asincrono di previsione sulle partite di Ark of Osiris delle alleanze di vertice · **Automazione:** autonomo per le missioni; conferma per le scommesse

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Durante le stagioni della Osiris League (date non indicate).

### Meccaniche
- Si scommette con monete sulle alleanze che si sfidano; monete da missioni e scommesse, spendibili nel negozio; missioni giornaliere con reset alle 00:00 UTC, settimanali con reset il lunedi'; una scommessa persa restituisce il 50% delle monete ([riseofkingdomsguides][s55]).
- Scommettere sull'alleanza con meno puntate puo' far guadagnare molte monete (ma e' piu' rischioso) ([riseofkingdomsguides][s55]).
- Eye for Talent: si usano i Marks of the Champion sull'alleanza che si pensa vincera'; i Marks si ottengono anche con il pacchetto 'Mark of the Champion' ([riseofkingdomsguides][s55]).

### Premi principali
- Negozio monete: prima sculture di comandanti leggendari e action points, poi blueprint; negozio Eye for Talent: prima sculture leggendarie, poi materiali di equipaggiamento ([riseofkingdomsguides][s55]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| n/a | Nessuna marcia coinvolta | Evento di scommesse, non di combattimento. | [riseofkingdomsguides · osiris league betting 02/01/2026][s55] |

### Trucchi (massimo punteggio, zero perdite)
- Completare ogni giorno le missioni prima del reset delle 00:00 UTC ([riseofkingdomsguides][s55]).
- Underdog = piu' monete ma piu' rischio; la perdita restituisce meta' puntata ([riseofkingdomsguides][s55]).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| OSL-01 | Osiris League attiva | Completare le missioni giornaliere/settimanali e riscuotere le monete. — *Monete gratuite.* | no | [riseofkingdomsguides · osiris league betting 02/01/2026][s55] |
| OSL-02 | Monete disponibili e scommesse aperte | Proporre la puntata secondo il profilo di rischio dell'utente (default prudente: favorita; aggressivo: underdog come suggerito dalla fonte). — *Scommessa = rischio di perdere il 50% della puntata.* | **sì** | [riseofkingdomsguides · osiris league betting 02/01/2026][s55] |
| OSL-04 | Monete o Marks disponibili a fine stagione | Proporre gli acquisti nell'ordine della fonte (sculture leggendarie del piano, action points, blueprint/materiali). — *Valuta evento da non lasciare inutilizzata.* | **sì** | [riseofkingdomsguides · osiris league betting 02/01/2026][s55] |
| OSL-03 | Offerta di pacchetti per Marks of the Champion | Ignorare. — *Il bot non spende denaro ne' gemme.* | no | [riseofkingdomsguides · osiris league betting 02/01/2026][s55] |

**Lacune:** Formato, calendario e stagioni della Osiris League 2026 non indicati; la pagina letta ha contenuto datato (lastmod 2026-01-02). Requisiti per partecipare alle scommesse non indicati.

**Fonti della sezione:** [riseofkingdomsguides · osiris league betting 02/01/2026][s55]

---

## 15. Golden Kingdom

**Tipo:** PvE dungeon a piani (asincrono, individuale) · **Automazione:** semi-autonomo: esplorazione/battaglie con regole conservative; conferma per reset e oggetti rari

**Sblocco:** City Hall 17+ ([riseofkingdomsguides][s56]).

**Cadenza:** Evento ricorrente; data e durata dal pannello Events (le fonti non danno la cadenza).

### Meccaniche
- 20 piani con capo (chief) per piano; checkpoint ogni 4 piani (4, 8, 12, 16, 20) con premi e negozio in Karaku Gold ([riseofkingdomsguides][s56], [riseofkingdomshandbook][s57]).
- Nebbia su tutto il piano: rivelandola si trovano oggetti, nemici e il capo; l'Arrow Tower danneggia le truppe per ogni casella rivelata (si distrugge o si rimuove con una relic apposita) ([riseofkingdomsguides][s56], [riseofkingdomshandbook][s57]).
- Cinque armate per run; la salute delle truppe PERSISTE tra le battaglie; una volta impostate le truppe non si possono cambiare ([riseofkingdomsguides][s56]).
- Relic monouso (massimo 9 tenute), Blessing permanenti per la durata dell'evento scelti tra 3 dopo ogni piano; healing hut: +50% salute a una truppa per incontro ([riseofkingdomsguides][s56]).
- Valgono equipaggiamento, tecnologia, VIP, civilta' e skin; NON vale l'army expansion ([riseofkingdomsguides][s56]).

### Premi principali
- Forzieri d'oro ai checkpoint; negozio Karaku Gold ai checkpoint (contenuti non dettagliati) ([riseofkingdomsguides][s56]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| F2P | Tank: Richard I o Charles Martel (se sviluppati) · AoE: Sun Tzu, Yi Seong-Gye · Supporto: Aethelflaed, Joan of Arc | [riseofkingdomsguides][s56] indica tank (Richard, Alexander, Caesar), supporto (Joan of Arc, Aethelflaed) e danno AoE (Sun Tzu, YSG); [riseofkingdomshandbook][s57]: fronte durevole + danno dietro, usare i comandanti gia' sviluppati; cinque DPS non sono automaticamente migliori. | [riseofkingdomsguides · golden kingdom event 02/01/2026][s56] · [handbook · golden kingdom 09/09/2026][s57] |
| evoluto | Tank: Richard I, Alexander the Great, Julius Caesar · AoE: Yi Seong-Gye, Sun Tzu · Supporto/cura: Joan of Arc, Aethelflaed | Scelte di [riseofkingdomsguides][s56] con enfasi sull'AoE; [heaven-guardian][s2]: preparare piu' coppie con cure, danno ad area e fronti durevoli. | [riseofkingdomsguides · golden kingdom event 02/01/2026][s56] · [heaven-guardian · events dominate 03/08/2026][s2] |

### Trucchi (massimo punteggio, zero perdite)
- Esplorare prima le caselle sicure; combattere solo gli incontri che sbloccano progresso o premi utili ([riseofkingdomshandbook][s57]).
- Curare la marcia la cui perdita romperebbe le battaglie successive, non automaticamente quella piu' bassa; non tenere la cura finche' la marcia e' gia' persa ([riseofkingdomshandbook][s57]).
- Blessing: scegliere cio' che risolve il problema reale del run (difesa/cura se il fronte cade, danno se le battaglie si trascinano) ([riseofkingdomshandbook][s57]).
- Spendere il Karaku Gold ai checkpoint in vista dei piani difficili; tenere la Siege Relic per gli ultimi boss (si somma) ([riseofkingdomsguides][s56]).
- Controllare il comandante di rinforzo offerto: un ritratto leggendario non implica abilita' al massimo ([riseofkingdomshandbook][s57]).
- Se l'inizio e' andato male e le regole lo permettono, ricominciare puo' costare meno che forzare una lineup rotta ([riseofkingdomshandbook][s57]).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| GK-01 | City Hall < 17 | Ignorare l'evento. — *Requisito CH17.* | no | [riseofkingdomsguides · golden kingdom event 02/01/2026][s56] |
| GK-02 | Inizio run | Schierare 2 tank davanti e 3 marce di danno/supporto dietro (ripartizione scelta dal bot), usando SOLO comandanti gia' sviluppati; non comprare comandanti per questa modalita'. — *Salute persistente e truppe non modificabili: serve un fronte durevole.* | no | [handbook · golden kingdom 09/09/2026][s57] · [riseofkingdomsguides · golden kingdom event 02/01/2026][s56] |
| GK-03 | Su un piano | Rivelare prima le caselle adiacenti sicure; se compare una Arrow Tower, smettere di rivelare alla cieca e aprire un percorso per distruggerla; ingaggiare solo nemici che bloccano il percorso verso il capo o premi utili. — *Ogni battaglia costa salute che non si rigenera.* | no | [handbook · golden kingdom 09/09/2026][s57] · [riseofkingdomsguides · golden kingdom event 02/01/2026][s56] |
| GK-04 | Healing hut o oggetto di cura disponibile | Curare la marcia chiave (di solito il tank frontale) se sotto il 50% (soglia del bot); non 'rabboccare' marce che reggono il prossimo incontro facile. — *Cura limitata (50% a una truppa per incontro).* | no | [handbook · golden kingdom 09/09/2026][s57] · [riseofkingdomsguides · golden kingdom event 02/01/2026][s56] |
| GK-05 | Checkpoint con negozio | Spendere il Karaku Gold per il prossimo tratto difficile (cure/relic utili), senza lasciarlo inutilizzato. — *Valuta inutile se il run finisce.* | no | [handbook · golden kingdom 09/09/2026][s57] |
| GK-06 | Run compromesso nei primi piani e reset consentito | Proporre all'utente il reset (verificando regole di reset e premi). — *Il reset puo' costare meno che forzare il run.* | **sì** | [handbook · golden kingdom 09/09/2026][s57] |

**Lacune:** Cadenza/durata dell'evento e contenuto dei premi ai checkpoint non indicati. Perdite reali di truppe: nessuna fonte lo dice esplicitamente (la salute e' dell'evento).

**Fonti della sezione:** [riseofkingdomsguides · golden kingdom event 02/01/2026][s56] · [handbook · golden kingdom 09/09/2026][s57] · [heaven-guardian · events dominate 03/08/2026][s2]

---

## 16. Shadow Legion (Dark Fortresses)

**Tipo:** PvE d'alleanza a ondate contro le citta' dei membri · **Automazione:** assistito: il bot prepara la citta' e rinforza solo su istruzione

**Sblocco:** Citta' livello 4+ e alleanza con 30 membri ([riseofkingdomsguides][s58]).

**Cadenza:** Una volta per evento, all'orario scelto dagli ufficiali.

### Meccaniche
- Le Dark Fortresses compaiono sulla mappa; le piu' vicine mandano ondate contro le citta' dei membri; gli ufficiali scelgono orario e difficolta' ([riseofkingdomshandbook][s59], [riseofkingdomsguides][s58]).
- Requisiti ([riseofkingdomsguides][s58], contenuto datato): citta' di livello 4 o superiore e alleanza con 30 membri; l'alleanza ha una sola possibilita' per evento.
- 'Your troops will not die' ([riseofkingdomsguides][s58]). Gli scudi di pace NON bloccano gli attacchi; i giocatori eliminati non sono piu' bersagli; l'evento finisce se tutti i membri sono sconfitti.
- Punti: rinforzare le citta' d'alleanza, attaccare i barbari Shadow Legion sul campo, spostarsi tra le citta' attaccate (alleanza compatta) ([riseofkingdomsguides][s58]).

### Premi principali
- Premi personali e d'alleanza (non quantificati): verificare se dipendono da partecipazione personale, progresso d'alleanza o stadio ([riseofkingdomshandbook][s59]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| F2P / medio | Richard I · Charles Martel · Yi Seong-Gye · Alternative: Pelagius, Hermann, Sun Tzu | Difensori consigliati da [riseofkingdomsguides][s58]: 'Every commander who has garrison talent is good'. | [riseofkingdomsguides · shadow legion dark 02/01/2026][s58] |
| evoluto | La coppia da guarnigione assegnata dall'alleanza (non necessariamente la migliore coppia da campo) | [riseofkingdomshandbook][s59]: la miglior coppia da campo non e' sempre la miglior difesa; seguire il piano d'alleanza. | [handbook · shadow legion 09/09/2026][s59] |

### Trucchi (massimo punteggio, zero perdite)
- Prima dell'inizio: richiamare le marce, liberare l'ospedale, controllare i comandanti difensori della citta' ([riseofkingdomshandbook][s59]).
- Rinforzare PRIMA della crisi: il tempo di viaggio fa parte della difesa; confrontare orario d'attacco, distanza e difensori gia' dentro ([riseofkingdomshandbook][s59]).
- Un solo canale per le chiamate; i nuovi membri segnalano presto la pressione ([riseofkingdomshandbook][s59]).
- Non inseguire il punteggio personale con rinforzi inutili se un'altra citta' ne ha bisogno ([riseofkingdomshandbook][s59]).
- Usare rune/oggetti di attacco o difesa se disponibili ([riseofkingdomsguides][s58]) - per il bot solo oggetti gia' posseduti.

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| SL-01 | Shadow Legion annunciato (orario noto) e mancano 30 minuti | Richiamare in citta' le marce in raccolta lontane, liberare spazio in ospedale, impostare la coppia di guarnigione indicata dall'alleanza. — *Una marcia che rientra da un nodo lontano non aiuta nessuno.* | no | [handbook · shadow legion 09/09/2026][s59] |
| SL-02 | Richiesta di rinforzo da un ufficiale/membro durante le ondate | Proporre all'utente l'invio del tipo di truppa richiesto alla citta' indicata (tempo di viaggio stimato); inviare dopo conferma. — *L'invio di truppe e' una decisione di coordinamento dell'utente.* | **sì** | [handbook · shadow legion 09/09/2026][s59] |
| SL-03 | Barbari Shadow Legion vicini alla citta' e marcia libera | Attaccarli con la marcia PvE (sono unita' dell'evento, non giocatori). — *Fanno punti e alleggeriscono le ondate.* | no | [riseofkingdomsguides · shadow legion dark 02/01/2026][s58] |
| SL-04 | Fine evento | Riscuotere i premi e controllare l'ospedale prima di tornare alla routine. — *Checklist post-evento.* | no | [handbook · shadow legion 09/09/2026][s59] |

**Lacune:** Numero di ondate, premi e regole di difficolta' 2026: le fonti rimandano al pannello evento.

**Fonti della sezione:** [handbook · shadow legion 09/09/2026][s59] · [riseofkingdomsguides · shadow legion dark 02/01/2026][s58]

---

## 17. Esmeralda's Prayer / Esmeralda's Collection

**Tipo:** Evento a ruota con valuta (Wishing Coins) + missioni giornaliere · **Automazione:** autonomo con sole monete gratuite

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Stagionale: Spring Symphony 10 giorni ([riseofkingdomsguides][s60]); Halloween 2026 con la 1.1.12 del 22-09-2026 ([ldshop][s61]).

### Meccaniche
- Esmeralda's Prayer: da 1 a 3 Wishing Coins per spin; ogni moneta in piu' aggiunge un puntatore indipendente; 8 premi normali e 4 speciali, quantita' limitate non rifornite; completamento automatico quando si prendono i 4 premi speciali; monete avanzate convertite in Golden Keys, Crystal Keys o speedup da 8 ore ([riseofkingdomsguides][s60]).
- Spin in gemme: 1.200 gemme per spin (inefficiente per F2P) ([riseofkingdomsguides][s60]).
- Esmeralda's Collection: via F2P con missioni giornaliere: 4 monete al giorno ([riseofkingdomsguides][s60]); presente anche nel pacchetto Halloween 2026 ([ldshop][s61]).
- Monete anche da Dreams of Spring, Race Against Time, Tempest Clash, pacchetti e gemme ([riseofkingdomsguides][s60]).

### Premi principali
- Premi della ruota (8 normali + 4 speciali); conversione finale delle monete in chiavi/speedup ([riseofkingdomsguides][s60]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| n/a | Nessuna marcia (solo per le missioni collegate, es. Race Against Time: vedi quella modalita') | Evento a valuta. | [riseofkingdomsguides · spring symphony esmeraldas 02/01/2026][s60] |

### Trucchi (massimo punteggio, zero perdite)
- Mai gemme: raccogliere le monete dagli eventi gratuiti collegati ([riseofkingdomsguides][s60]).
- Fare le missioni giornaliere prima del reset ([riseofkingdomsguides][s60]).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| ESM-01 | Esmeralda's Collection attiva | Completare le missioni giornaliere e riscuotere le monete prima del reset. — *Unica via F2P alle monete.* | no | [riseofkingdomsguides · spring symphony esmeraldas 02/01/2026][s60] · [ldshop · halloween 22/09/2026][s61] |
| ESM-02 | Wishing Coins gratuite in inventario | Spendere tutte le Wishing Coins gratuite (1-3 per spin: ogni moneta aggiunge un puntatore indipendente) finche' restano premi speciali; se la ruota si completa, convertire le monete residue in Golden Keys, Crystal Keys o speedup da 8 ore secondo il piano dell'utente. — *Nessun costo reale; le quantita' dei premi sono limitate.* | no | [riseofkingdomsguides · spring symphony esmeraldas 02/01/2026][s60] |
| ESM-03 | Monete esaurite | Fermarsi. Mai spin a 1.200 gemme ne' pacchetti. — *Vincolo MAI gemme.* | no | [riseofkingdomsguides · spring symphony esmeraldas 02/01/2026][s60] |

**Lacune:** Probabilita' dei premi della ruota non indicate dalla fonte (descrive solo i puntatori). Requisiti di sblocco e contenuto preciso dei premi 2026 non indicati.

**Fonti della sezione:** [riseofkingdomsguides · spring symphony esmeraldas 02/01/2026][s60] · [ldshop · halloween 22/09/2026][s61]

---

## 18. Silk Road Speculators (carovana d'alleanza) e Desert Tracks

**Tipo:** PvE d'alleanza di scorta (barbari contro la carovana) · **Automazione:** autonomo sui barbari della scorta quando la carovana e' in viaggio; il bot non avvia carovane

**Sblocco:** Avvio riservato a leader/R4 ([rok.guide][s62] via Wayback).

**Cadenza:** Evento d'alleanza periodico (fonte 2019); Desert Tracks negli anniversari 2025 e 2026.

### Meccaniche
- Leader e R4 scelgono la difficolta' (Easy, Normal, Hard, Nightmare, Hell) e la fortezza d'alleanza di partenza; ogni avvio costa 100.000 Alliance Credits; la difficolta' successiva si sblocca superando la precedente ([rok.guide][s62] via Wayback, 2019).
- La carovana parte subito (Easy ~15 minuti; piu' lunga alle difficolta' alte); i barbari compaiono e la attaccano, sempre piu' numerosi verso la destinazione: i membri devono distruggerli ([rok.guide][s62] via Wayback, 2019).
- Premi via mail a tutti i membri in base alla percentuale di merci consegnate; limite giornaliero di scorte per alleanza (reset 00:00 UTC), oltre si possono fare carovane di allenamento senza premi ma valide per il punteggio; classifica per difficolta' massima e punteggio ([rok.guide][s62] via Wayback, 2019).
- 2025-2026: 'Desert Tracks' (scorta di una carovana del tesoro al festival contro ondate di nemici, premi incrementali) nell'Anniversary 2025 ([bluestacks][s22]) e nell'Anniversary 1.1.11 del 27-08-2026 ([ldshop][s36]).

### Premi principali
- Premi via mail proporzionali alle merci consegnate; premi di classifica a fine evento ([rok.guide][s62] via Wayback, 2019).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| tutti | Coppia PvE veloce con AoE (es. Cao Cao o comandanti Peacekeeping come Boudica/Aethelflaed) | I nemici sono barbari lungo un percorso: servono velocita' e danno contro barbari. Indicazione del bot basata sulle coppie Peacekeeping delle fonti barbari, non su una fonte Silk Road. | [handbook · barbarian forts 18/08/2026][s19] · [handbook · map zones runes 18/08/2026][s28] |

### Trucchi (massimo punteggio, zero perdite)
- Scegliere una partenza vicina alla maggior parte dei membri ([rok.guide][s62] via Wayback, 2019).
- Controllare ogni casella del percorso; eliminare i barbari il prima possibile ([rok.guide][s62] via Wayback, 2019).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| SILK-01 | Carovana d'alleanza in viaggio (annuncio o evento attivo) e marce libere | Mandare la marcia PvE veloce sui barbari che minacciano la carovana lungo il percorso, restando entro distanza di rientro sicura. — *Sono barbari dell'evento, non giocatori; premi per tutti in base alle merci consegnate.* | no | [rok.guide (Wayback) · silk road speculators 27/05/2019][s62] |
| SILK-02 | Proposta di avviare una carovana | Non avviare (serve ruolo leader/R4 e costa 100.000 Alliance Credits): segnalarlo all'utente. — *Spesa di risorse d'alleanza.* | **sì** | [rok.guide (Wayback) · silk road speculators 27/05/2019][s62] |
| SILK-03 | Mail premi carovana ricevuta | Riscuotere. — *Premi gratuiti.* | no | [rok.guide (Wayback) · silk road speculators 27/05/2019][s62] |

**Lacune:** Nessuna fonte 2026 descrive le regole attuali di Silk Road Speculators: dati da rok.guide 2019 (copia Wayback). Regole di dettaglio di Desert Tracks 2026 non documentate (solo descrizione di una riga).

**Fonti della sezione:** [rok.guide (Wayback) · silk road speculators 27/05/2019][s62] · [ldshop · anniversary special 27/08/2026][s36] · [bluestacks · 7th anniversary update 16/09/2025][s22]

---

## 19. Race Against Time

**Tipo:** PvE a tempo sui barbari (classifica) · **Automazione:** autonomo con buff gratuiti; conferma per oggetti rari

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Stagionale (anniversario, Halloween, Spring Symphony).

### Meccaniche
- Ogni tentativo dura 5 minuti: sconfiggere piu' barbari possibile; i barbari di livello alto danno tempo bonus (massimo 4 minuti) (riseofkingdomsguides).
- 3 tentativi al giorno, reset a mezzanotte UTC; top 100 premi extra, top 10 sculture leggendarie (riseofkingdomsguides).
- Fa parte degli eventi dell'Anniversary 2025 ([bluestacks][s22]) e del pacchetto Halloween 2026 ([ldshop][s61]); fornisce Wishing Coins per Esmeralda (riseofkingdomsguides, Spring Symphony).

### Premi principali
- Premi a punteggio; top 100 extra; top 10 sculture leggendarie; Wishing Coins nel pacchetto Esmeralda (riseofkingdomsguides).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| F2P | Primario Peacekeeping: Boudica, Lohar, Minamoto no Yoshitsune, Belisarius o Aethelflaed · Secondario cavalleria ad alto danno: Genghis Khan, Attila o Cao Cao | [riseofkingdomsguides][s63]: cavalleria per la mobilita' (evitare fanteria/assedio lenti), primario Peacekeeping. | [riseofkingdomsguides · race against time 03/09/2026][s63] |
| evoluto | Stessa struttura con comandanti al massimo e tutti i buff (equipaggiamento, rune, titoli, skill d'alleanza, skin) | [riseofkingdomsguides][s63] elenca 10+ fonti di buff; l'army expansion al 50% costa 2.000 gemme ed e' VIETATA al bot. | [riseofkingdomsguides · race against time 03/09/2026][s63] |

### Trucchi (massimo punteggio, zero perdite)
- Posizionarsi vicino a gruppi densi di barbari PRIMA di iniziare (riseofkingdomsguides).
- Puntare ai barbari di livello alto per il tempo bonus (riseofkingdomsguides).
- Double Line Formation: +10% velocita' di marcia verso i barbari ([bluestacks][s22], 2025).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| RAT-01 | Race Against Time attivo e tentativi giornalieri > 0 | Spostare la marcia (senza teletrasporti a pagamento) vicino a un gruppo denso di barbari, impostare Double Line Formation se posseduta, poi avviare il tentativo concatenando i barbari di livello piu' alto battibili. — *5 minuti + bonus fino a 4; 3 tentativi al giorno.* | no | [riseofkingdomsguides · race against time 03/09/2026][s63] · [bluestacks · 7th anniversary update 16/09/2025][s22] |
| RAT-02 | Suggerimento di usare army expansion (2.000 gemme) o altri acquisti per la classifica | Rifiutare. — *Vincolo MAI gemme.* | no | [riseofkingdomsguides · race against time 03/09/2026][s63] |

**Lacune:** Premi per soglia e requisiti non dettagliati.

**Fonti della sezione:** [riseofkingdomsguides · race against time 03/09/2026][s63] · [bluestacks · 7th anniversary update 16/09/2025][s22] · [ldshop · halloween 22/09/2026][s61] · [riseofkingdomsguides · spring symphony esmeraldas 02/01/2026][s60]

---

## 20. Marauders / Eve of the Crusade (pre-KvK e Lost Kingdom)

**Tipo:** PvE a base di AP legato al KvK · **Automazione:** autonomo con AP naturale; conferma per oggetti AP

**Sblocco:** Regni in fase KvK applicabile.

**Cadenza:** Legata al calendario KvK; dal 1.1.12 contestuale all'apertura del Lost Kingdom.

### Meccaniche
- Eve of the Crusade include sconfiggere i Marauders e aprire Marauder Encampments o oggetti di rifornimento dell'evento (heaven-guardian KvK).
- Marauders: una delle fonti evento piu' preziose di speedup, gemme, risorse e oggetti prima delle stagioni KvK (heaven-guardian speedups).
- Dal 1.1.12 (22-09-2026) Eve of the Crusade apre insieme al Lost Kingdom invece che come fase precedente ([ldshop][s61]).

### Premi principali
- Speedup, gemme, risorse, oggetti di rifornimento; Honor nel Lost Kingdom dai barbari (heaven-guardian KvK).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| tutti | Marcia Peacekeeping (vedi Barbarians) | [heaven-guardian][s64]: comandanti Peacekeeping per i barbari e marce Peacekeeping per i contributi di Past Glory stage 2. | [heaven-guardian · kvk season 1 24/08/2026][s64] |

### Trucchi (massimo punteggio, zero perdite)
- Usare l'AP naturale prima di quello in bottiglia; tenere le bottiglie per le attivita' di regno a valore piu' alto (heaven-guardian).
- Non svuotare la riserva AP sui barbari normali poco prima dei Marauders (heaven-guardian).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| MAR-01 | KvK/Eve of the Crusade previsto entro 3 giorni | Non usare oggetti AP su barbari normali; tenere l'AP naturale speso ma non al cap. — *I Marauders rendono piu' dei barbari normali.* | no | [heaven-guardian · speedups ultimate domination 04/08/2026][s65] · [heaven-guardian · kvk season 1 24/08/2026][s64] |
| MAR-02 | Marauders attivi | Farm con AP naturale e marcia Peacekeeping secondo le istruzioni del regno; proporre all'utente l'uso degli oggetti AP. — *Oggetti AP = consumabili rari.* | **sì** | [heaven-guardian · speedups ultimate domination 04/08/2026][s65] · [heaven-guardian · kvk season 1 24/08/2026][s64] |

**Lacune:** Meccanica dettagliata dei Marauders (livelli, costo AP, limiti) non descritta dalle fonti 2026 lette.

**Fonti della sezione:** [heaven-guardian · kvk season 1 24/08/2026][s64] · [heaven-guardian · speedups ultimate domination 04/08/2026][s65] · [ldshop · halloween 22/09/2026][s61]

---

## 21. Tempest Clash (battaglie navali)

**Tipo:** PvP 5v5 in tempo reale con navi (bonus del governatore disattivati) · **Automazione:** solo avviso

**Sblocco:** City Hall 7+ (riseofkingdomsguides).

**Cadenza:** Stagionale (non indicata).

### Meccaniche
- 10 giocatori in due squadre da 5: distruggere le navi di rifornimento nemiche proteggendo le proprie; City Hall 7+; tutti i bonus del governatore sono inattivi sul campo (riseofkingdomsguides).
- Navi: Trireme (tipo cavalleria; Wave Breaker +15% velocita' di marcia, Swift Strike speronamento DF 500, Smash +85% danni da abilita' contro Galley, Entangle -30% velocita' di marcia al nemico), Armored Ship (tipo fanteria; Iron Wall DF 310, fino a 3.800 contro bersagli ad alta velocita'; Head-On Attack +85% contro Trireme; Heavy Hitter +90% attacco normale contro navi rifornimento), Galley (tipo arciere; Barrage DF 500 a distanza sul nemico piu' vicino; Penetrating Strike +15% contro Armored Ship; Burn +30% attacco normale contro navi rifornimento). Le abilita' delle navi non richiedono Rage (riseofkingdomsguides).
- Fonte di Wishing Coins nel pacchetto Esmeralda (riseofkingdomsguides, Spring Symphony).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| tutti | Nessun comandante: si sceglie il tipo di nave (Trireme / Armored Ship / Galley) in base al ruolo della squadra | I bonus del governatore non contano; conta la composizione navale. | [riseofkingdomsguides · tempest clash event 02/01/2026][s66] |

### Trucchi (massimo punteggio, zero perdite)
- Armored Ship contro Trireme e navi rifornimento; Trireme contro Galley; Galley per danno a distanza e contro Armored (riseofkingdomsguides, dedotto dai bonus delle abilita').

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| TEM-01 | Tempest Clash attivo | Avvisare l'utente (PvP in tempo reale); nessuna azione autonoma. — *Azione contro giocatori.* | **sì** | [riseofkingdomsguides · tempest clash event 02/01/2026][s66] |

**Lacune:** Premi, durata e presenza nel calendario 2026 non indicati (pagina con contenuto datato).

**Fonti della sezione:** [riseofkingdomsguides · tempest clash event 02/01/2026][s66] · [riseofkingdomsguides · spring symphony esmeraldas 02/01/2026][s60]

---

## 22. Eventi Anniversario 2026 (versione 1.1.11 'Anniversary Special')

**Tipo:** Pacchetto stagionale di eventi asincroni (missioni, negozi a valuta, mini-giochi) · **Automazione:** autonomo per login/missioni/riscossioni; conferma per interazioni con altri giocatori e acquisti non gratuiti

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Annuale (fine agosto - settembre).

### Meccaniche
- Versione 1.1.11 del 27-08-2026 (manutenzione dalle 06:00 UTC), 9 eventi: Art Festival (raccogliere Brushes e riparare maschere per premi a progressione), Melon Market (vendere Egrimelons per Melon Money da spendere nel negozio; novita': possibilita' di rubare egrimelon tra regni), Alliance Quiz (quiz d'alleanza), Arms Training (combattere Armsmaster Lohar), Riddles of the Sphinx (sfide a tema deserto), Desert Tracks (scortare una carovana del tesoro), Circus of Wonders (giochi con Goldayne e Fogsworth), Lucky Red Packet (premi 'sociali'), RoK Yearbook (riepilogo 2025-2026) ([ldshop][s36]).
- Altre novita' 1.1.11: Armament Scratch con progresso del negozio conservato tra eventi e un refresh gratuito in piu' al prossimo evento; mail Osiris God Chest fissata durante la registrazione; modifiche ai passi di Warriors Unbound e Siege of Orleans ([ldshop][s36]).
- Riferimento 2025 (7th Anniversary, [bluestacks][s22]): 11 eventi tra cui Sign-In Spoils (7 giorni di login per un comandante leggendario), Grand Reunion, Elysian Treasures, Fisherman's Fortune, Melon Market, Desert Tracks, Circus of Wonders, Alliance Quiz, Race Against Time; Zenith of Power con Zenith Badges che scadono a fine evento; nuova formazione Double Line (+10% velocita' di marcia verso i barbari).

### Premi principali
- Premi a progressione e negozi evento; 2025: comandante leggendario dal login di 7 giorni ([bluestacks][s22]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| tutti | Arms Training e Race Against Time: vedi le modalita' dedicate · Desert Tracks: coppia PvE veloce con AoE contro le ondate | Le fonti descrivono gli eventi senza lineup specifiche; si rimanda alle modalita' con dati propri. | [ldshop · anniversary special 27/08/2026][s36] · [bluestacks · 7th anniversary update 16/09/2025][s22] |

### Trucchi (massimo punteggio, zero perdite)
- Fare login ogni giorno durante l'anniversario (nel 2025 il login di 7 giorni dava un leggendario) ([bluestacks][s22]).
- Spendere le valute evento (Melon Money, badge, ecc.) prima della fine: nel 2025 i Zenith Badges non usati scadevano ([bluestacks][s22]).
- Priorita' in quasi ogni negozio evento: sculture del comandante che si sta sviluppando > speedup (soprattutto ricerca) > materiali di equipaggiamento > risorse; spendere i punti evento prima della chiusura del negozio ([riseofkingdomshandbook][s67], Best events to spend on).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| ANN-01 | Evento anniversario attivo | Login giornaliero, missioni gratuite di tutti gli eventi, riscossione premi a progressione. — *Premi gratuiti a tempo.* | no | [ldshop · anniversary special 27/08/2026][s36] · [bluestacks · 7th anniversary update 16/09/2025][s22] |
| ANN-02 | Melon Market: opzione di rubare egrimelon a giocatori di altri regni | Chiedere conferma prima di ogni furto. — *Azione contro altri giocatori.* | **sì** | [ldshop · anniversary special 27/08/2026][s36] |
| ANN-03 | Mancano meno di 24 ore alla fine di un evento con valuta/badge | Proporre la lista acquisti nel negozio evento (sculture del comandante in sviluppo > speedup ricerca > materiali > risorse) e spendere dopo conferma; mai gemme. — *Valute evento non spese vanno perse.* | **sì** | [bluestacks · 7th anniversary update 16/09/2025][s22] · [handbook · best events spend 18/08/2026][s67] |
| ANN-04 | Desert Tracks attivo (carovana in viaggio) | Applicare SILK-01 (marcia PvE sui nemici che attaccano la carovana). — *Evento di scorta contro ondate di nemici.* | no | [ldshop · anniversary special 27/08/2026][s36] · [bluestacks · 7th anniversary update 16/09/2025][s22] |
| ANN-05 | Armament Scratch attivo | Usare solo i refresh gratuiti; acquisti/estrazioni con materiali o gemme solo con conferma (gemme mai). — *Il progresso del negozio ora si conserva tra eventi: nessuna fretta di spendere.* | **sì** | [ldshop · anniversary special 27/08/2026][s36] |

**Lacune:** Regole dettagliate, durate e premi di Art Festival, Riddles of the Sphinx, Circus of Wonders, Lucky Red Packet e Desert Tracks 2026 non documentati (solo descrizioni di una riga).

**Fonti della sezione:** [ldshop · anniversary special 27/08/2026][s36] · [bluestacks · 7th anniversary update 16/09/2025][s22] · [handbook · best events spend 18/08/2026][s67]

---

## 23. Halloween 2026 (versione 1.1.12 'Dreams of Phantasma')

**Tipo:** Pacchetto stagionale + modifiche Lost Kingdom · **Automazione:** autonomo per missioni gratuite; conferma per armamenti e speedup

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Stagionale (dal 22-09-2026).

### Meccaniche
- Versione 1.1.12 del 22-09-2026: Esmeralda's Prayer/Collection, Race Against Time, In Search of Wonders (armamenti di alta qualita'), Eve of the Crusade insieme all'apertura del Lost Kingdom ([ldshop][s61]).
- Lost Kingdom: capitoli chiave delle Chronicle sbloccati a orari fissi (venerdi'-sabato alle 12:00); pass di livello 4 della Season 2 semi-protetto; nuova funzione Acclaim (Season 1 e 2) che premia le battaglie contro governatori di altri regni; lo Stage 2 di Past Glory richiede il consumo di speedup; classifiche individuali di stagione con premi ([ldshop][s61]).
- Conquest Tavern con 5 nuovi comandanti; la Wheel of Fortune della Season 1 consuma spin ticket (da gemme o pacchetti) ([ldshop][s61]).

### Premi principali
- Vedi Esmeralda, Race Against Time; armamenti da In Search of Wonders ([ldshop][s61]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| tutti | Race Against Time: primario Peacekeeping + secondario cavalleria (vedi modalita') | Unico evento del pacchetto con combattimento PvE documentato. | [riseofkingdomsguides · race against time 03/09/2026][s63] · [ldshop · halloween 22/09/2026][s61] |

### Trucchi (massimo punteggio, zero perdite)
- Esmeralda's Collection e' la via F2P alle monete ([ldshop][s61]).
- Past Glory stage 2 ora consuma speedup: decidere il budget prima ([ldshop][s61]).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| HAL-01 | Pacchetto Halloween attivo | Missioni gratuite di Esmeralda's Collection e tentativi giornalieri di Race Against Time; riscossioni. — *Premi gratuiti.* | no | [ldshop · halloween 22/09/2026][s61] |
| HAL-02 | In Search of Wonders o Past Glory stage 2 richiedono di consumare materiali/speedup | Chiedere conferma con il costo esatto mostrato. — *Materiali rari e speedup.* | **sì** | [ldshop · halloween 22/09/2026][s61] |
| HAL-03 | Wheel of Fortune Season 1 con spin ticket | Usare solo ticket gratuiti gia' posseduti; mai comprarli. — *Ticket da gemme o pacchetti.* | no | [ldshop · halloween 22/09/2026][s61] |

**Lacune:** Durata del pacchetto Halloween 2026 non indicata.

**Fonti della sezione:** [ldshop · halloween 22/09/2026][s61]

---

## 24. Radiant Rivalry (NUOVA modalita' 2026, 1v1 tra regni)

**Tipo:** Competizione tra due regni: fase di preparazione asincrona + fase di battaglia PvP · **Automazione:** autonomo nella preparazione (missioni); solo avviso/conferma nella battaglia

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Nuova nel 2026; calendario non indicato.

### Meccaniche
- Introdotta con la 1.1.12 (22-09-2026): due regni abbinati, due fasi ([ldshop][s61]).
- Preparation Phase: per piu' giorni i membri del regno fanno punti completando missioni di preparazione, conteggiati ogni giorno; gli account farm possono contribuire con totali sproporzionati ([ldshop][s61]).
- Battle Phase: il regno vincitore puo' teletrasportarsi nel territorio del perdente e contendere la Radiant Spire ([ldshop][s61]).
- Radiant Emblems da missioni di preparazione e di battaglia, spesi nel Radiance Shop ([ldshop][s61]).

### Premi principali
- Radiant Emblems -> Radiance Shop ([ldshop][s61]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| preparazione | Nessuna lineup: dipende dalle missioni (raccolta, barbari, addestramento...) | La fonte descrive missioni di preparazione senza comandanti. | [ldshop · halloween 22/09/2026][s61] |

### Trucchi (massimo punteggio, zero perdite)
- Completare ogni giorno le missioni di preparazione: non aspettare l'ultimo giorno ([ldshop][s61]).
- Coordinare gli account farm dell'utente/alleanza sulle missioni ([ldshop][s61]).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| RR-01 | Radiant Rivalry in Preparation Phase | Ogni giorno completare le missioni di preparazione compatibili con la routine (raccolta, barbari, costruzione/ricerca gia' pianificate) e riscuotere gli emblemi. — *Punti conteggiati ogni giorno; non rimandare.* | no | [ldshop · halloween 22/09/2026][s61] |
| RR-02 | Missione di preparazione che richiede spesa di speedup/risorse fuori piano | Chiedere conferma. — *Budget dell'utente.* | **sì** | [ldshop · halloween 22/09/2026][s61] |
| RR-03 | Battle Phase (teletrasporto nel regno avversario, Radiant Spire) | Nessuna azione autonoma: avvisare l'utente, tenere la citta' pronta alla difesa. — *PvP contro giocatori di un altro regno.* | **sì** | [ldshop · halloween 22/09/2026][s61] |
| RR-04 | Radiant Emblems disponibili | Proporre acquisti nel Radiance Shop secondo le priorita' dell'account. — *Valuta evento.* | **sì** | [ldshop · halloween 22/09/2026][s61] |

**Lacune:** Durata delle fasi, tipi di missioni, abbinamento e premi del Radiance Shop non documentati: unica fonte l'articolo ldshop del 22-09-2026.

**Fonti della sezione:** [ldshop · halloween 22/09/2026][s61]

---

## 25. Clash of Divine Isles

**Tipo:** Evento a punti con invasioni tra territori (PvP) · **Automazione:** solo avviso

**Sblocco:** non indicato dalle fonti lette (vedi lacune).

**Cadenza:** Non indicata.

### Meccaniche
- Evento a punti; dalla 1.1.12 si ottengono anche 'defense points' affrontando le truppe dei governatori invasori mentre si difende il proprio territorio (prima i punti venivano soprattutto dalle invasioni) ([ldshop][s61]).

### Lineup

| Budget / ruolo | Comandanti (primario + secondario) | Perché | Fonti |
|---|---|---|---|
| tutti | Difesa: coppia da guarnigione/campo dell'account | I punti difensivi vengono dal combattere gli invasori. | [ldshop · halloween 22/09/2026][s61] |

### Trucchi (massimo punteggio, zero perdite)
- Dalla 1.1.12 anche la difesa del territorio fa punti ([ldshop][s61]).

### Regole per il bot

| ID | Quando | Allora | Conferma | Fonti |
|---|---|---|---|---|
| CDI-01 | Clash of Divine Isles attivo | Avvisare l'utente; nessun attacco o ingaggio autonomo contro giocatori. — *PvP.* | **sì** | [ldshop · halloween 22/09/2026][s61] |

**Lacune:** Regole, requisiti e premi di Clash of Divine Isles non documentati dalle fonti lette (solo la modifica della 1.1.12).

**Fonti della sezione:** [ldshop · halloween 22/09/2026][s61]

---

## Conflitti tra fonti

| Tema | Posizioni | Come si comporta il bot |
|---|---|---|
| Expedition: priorita' del negozio Medals of the Conqueror | **heaven-guardian 2026-08-03:** 1) Aethelflaed, 2) Constance (situazionale), 3) sculture epiche, 4) articoli a rotazione<br>**riseofkingdomshandbook 2026-08-18:** L'epico in evidenza (rotazione settimanale) e' 'il vero premio'; poi Constance; Aethelflaed con limite giornaliero<br>**bluestacks 2024-12-11:** Prima Aethelflaed, poi cio' che serve (es. Dazzling Starlight Sculptures) | Regola EXP-04: Aethelflaed ogni giorno se e' nel piano dell'account (2 fonti su 3), epico settimanale solo se in lista obiettivi. ([heaven-guardian · expedition tips rewards 03/08/2026][s7] · [handbook · expedition 18/08/2026][s6] · [bluestacks · expeditions 11/12/2024][s5]) |
| Expedition: marce disponibili nei primi stage | **riseofkingdomshandbook 2026-08-18:** 1 marcia all'inizio, 2 dallo stage 6, 3 dal 16, 4 dal 26, 5 dal 41<br>**bluestacks 2024-12-11:** Early stages allow 1-2 armies; later up to 5<br>**heaven-guardian 2026-08-03:** Later stages allow up to five concurrent marches (nessun breakpoint) | Compatibili; il bot usa i breakpoint di riseofkingdomshandbook e verifica in gioco il numero di slot. ([handbook · expedition 18/08/2026][s6] · [bluestacks · expeditions 11/12/2024][s5] · [heaven-guardian · expedition tips rewards 03/08/2026][s7]) |
| Ceroli Crisis: matchmaking casuale | **riseofkingdomsguides 2026-01-02:** Evitare il matchmaking: molti non sanno cosa fare<br>**heaven-guardian 2026-08-05:** Il matchmaking puo' funzionare alle difficolta' facili; le squadre private rendono meglio | Il bot propone sempre squadra privata; matchmaking solo su Easy/Normal e solo su scelta dell'utente. ([riseofkingdomsguides · ceroli crisis 02/01/2026][s11] · [heaven-guardian · ceroli crisis boss 05/08/2026][s10]) |
| Ceroli Shop: Keira | **riseofkingdomsguides 2026-01-02:** Comprare il nuovo comandante Keira perche' servira' negli eventi futuri<br>**heaven-guardian 2026-08-05:** Sculture Keira utili solo se ancora usata negli scenari; priorita' bassa se completata o sostituita | Keira solo se l'utente la usa/pianifica; altrimenti materiali di equipaggiamento. ([riseofkingdomsguides · ceroli crisis 02/01/2026][s11] · [heaven-guardian · ceroli crisis boss 05/08/2026][s10]) |
| Ian's Ballads: quale difficolta' | **riseofkingdomsguides 2026-01-02:** I premi si prendono una sola volta: puntare alla difficolta' piu' alta<br>**riseofkingdomshandbook 2026-09-09:** La piu' alta che il gruppo FINISCE entro 2 ore: un run incompleto rende meno di uno piu' facile completato | Il bot propone la piu' alta completabile (storico del gruppo), salendo di un livello solo dopo un clear comodo. ([riseofkingdomsguides · ians ballads 02/01/2026][s14] · [handbook · ians ballads 09/09/2026][s13]) |
| Lohar's Trial: quanta riserva AP usare | **riseofkingdomshandbook 2026-08-18:** Arrivare con AP pieno e oggetti di ricarica: e' la leva piu' grande sul numero di collane<br>**heaven-guardian 2026-08-08:** Non svuotare l'intera riserva solo perche' l'evento e' attivo | LOH-02/LOH-03: AP naturale sempre; oggetti AP fino al 50% della scorta e solo con conferma. ([handbook · lohars trial 18/08/2026][s24] · [heaven-guardian · lohars trial 08/08/2026][s20]) |
| Barbarian Forts: livelli | **riseofkingdomshandbook 2026-08-18:** Livelli 1-5 standard (piu' alti in alcuni contenuti)<br>**riseofkingdomsguides 2026-01-02:** Forti 1-6 (1-3 per i nuovi, 4-6 servono tecnologia e comandanti forti) | Il bot legge il livello dal gioco e sale di livello solo dopo rally riusciti senza fallimenti. ([handbook · barbarian forts 18/08/2026][s19] · [riseofkingdomsguides · barbarians barbarian forts 02/01/2026][s17]) |
| Sunset Canyon: numero di truppe per marcia | **riseofkingdomsguides 2026-01-02:** Tutti hanno la stessa quantita' di truppe T3; contano solo equipaggiamento, abilita' e talenti<br>**riseofkingdomshandbook 2026-09-09:** Il tier standardizzato non significa stessa capacita': lo sviluppo dei comandanti cambia il numero di truppe; controllare l'editor di formazione | Il bot legge la capacita' mostrata per ogni marcia nell'editor e non assume parita'. ([riseofkingdomsguides · sunset canyon 02/01/2026][s42] · [handbook · sunset canyon 09/09/2026][s41]) |
| Sunset Canyon: Challenge Tickets a fine stagione | **riseofkingdomsguides 2026-01-02:** Tenerli per l'ultimo giorno; 'can be recovered by the end of the season'<br>**riseofkingdomshandbook 2026-09-09:** Non presumere che scadano ogni settimana: leggere descrizione e regole di stagione | Regola SC-03 (legge la validita' dell'oggetto). ([riseofkingdomsguides · sunset canyon 02/01/2026][s42] · [handbook · sunset canyon 09/09/2026][s41]) |
| Ark of Osiris: perdite di truppe | **riseofkingdomshandbook 2026-09-09:** Le truppe sono ferite, non uccise: si paga in speedup di cura<br>**heaven-guardian 2026-08-04:** Combattimento generalmente 'protetto'; morte permanente non chiara, verificare le regole correnti | Il bot tratta l'Ark come senza morti ma con costo in speedup e verifica il testo dell'evento. ([handbook · ark osiris 09/09/2026][s48] · [heaven-guardian · ark osiris dominate 04/08/2026][s50]) |
| Champions of Olympia: abilita' di battaglia e ranking | **riseofkingdomshandbook 2026-09-09:** Skills per tipo di unita' (Infantry/Cavalry/Archer/Mixed) divise in Power, Tactical, Support; cita setup 'ranked'<br>**riseofkingdomsguides 2026-01-02 (contenuto datato):** 4 abilita' tra Cornerstone/Secondary/Common; 'no ranking system currently exists' | Versioni diverse della modalita': fa fede il pannello in gioco. ([handbook · champions olympia 09/09/2026][s52] · [riseofkingdomsguides · champions olympia 02/01/2026][s53]) |
| Barbarian Forts: i premi dipendono dal danno inflitto? | **riseofkingdomshandbook 2026-08-18:** La quota di premi scala col danno: mandare sempre la marcia piena<br>**heaven-guardian 2026-09-19:** Non dare per scontato che piu' danno garantisca piu' Books: le affermazioni sulla quota di danno non sono meccaniche confermate senza test | FORT-01 manda comunque la marcia piena (nessun costo aggiuntivo in un PvE) e registra i Books ricevuti per rally per verificare. ([handbook · barbarian forts 18/08/2026][s19] · [heaven-guardian · get books covenant 19/09/2026][s27]) |

## Lacune

- Expedition: Livello di City Hall di sblocco dell'Expedition non indicato dalle fonti lette.
- Expedition: Numero totale di stage/capitoli nel 2026 non indicato.
- Ceroli Crisis (e Ceroli Assault): Livello di City Hall richiesto per Ceroli Crisis/Assault non indicato dalle fonti lette.
- Ceroli Crisis (e Ceroli Assault): Perdite di truppe in Ceroli Crisis: nessuna fonte letta lo dice esplicitamente.
- Ceroli Crisis (e Ceroli Assault): Cadenza precisa (giorni) e prezzi del Ceroli Shop non indicati.
- Ian's Ballads: Durata dell'evento in giorni e numero di run possibili non indicati.
- Karuak Ceremony: Requisiti di sblocco, durata in giorni e valori dei premi del Karuak Ceremony non indicati dalle fonti 2026 lette (riseofkingdomshandbook cita un walkthrough AppGamer non raggiungibile).
- Barbarians e Barbarian Forts (farm Peacekeeping e rally ai forti): Costo AP di un rally ai forti e limite giornaliero di premi dai forti non indicati dalle fonti lette.
- Barbarians e Barbarian Forts (farm Peacekeeping e rally ai forti): Tabella AP per livello di barbaro non disponibile (solo 50 AP base).
- Holy Sites (Sanctum, Altar, Shrine, Lost Temple) e guardiani: Nessuna fonte 2026 letta con la lista completa dei buff di Altar/Shrine: i dati vengono da theriagames (febbraio 2025).
- Holy Sites (Sanctum, Altar, Shrine, Lost Temple) e guardiani: Perdite nelle battaglie contro i guardiani (feriti vs morti) non indicate.
- Holy Sites (Sanctum, Altar, Shrine, Lost Temple) e guardiani: La pagina riseofkingdomsguides.com/holy-sites/ risponde 404.
- Lohar's Trial: Requisito di sblocco e livelli/forza dell'armata di Lohar evocata non indicati.
- Lohar's Trial: Probabilita' di drop delle relic non indicate.
- Arms Training (Armsmaster Lohar): Requisito di sblocco e tabella completa dei premi a milestone non indicati.
- Arms Training (Armsmaster Lohar): Formula esatta del punteggio Legend Mode nel 2026 (riseofkingdomshandbook invita a verificarla in gioco).
- Protect the Supplies (scorta carovana individuale): Evento documentato solo da una pagina riseofkingdomsguides (contenuto datato, lastmod 2026-01-02); presenza nel calendario 2026 non verificata.
- Protect the Supplies (scorta carovana individuale): Requisito di sblocco e durata non indicati.
- Sunset Canyon: Livello di City Hall di sblocco e numero di marce Canyon per livello non verificati (riseofkingdomsguides cita City Hall 22 solo come aiuto per il top 50-100).
- Sunset Canyon: Contenuto del negozio/valuta del Canyon non indicato dalle fonti lette.
- Sunset Canyon: Nessuna lineup 'meta 2026' per account evoluti (legendary SoC) da fonte 2026: le guide Canyon dedicate di heaven-guardian e ldshop rispondono 404/non trovate; le coppie 2026 disponibili sono epiche/legacy.
- Ark of Osiris: Valori dei punti per struttura/Ark e premi esatti: le fonti rimandano al pannello evento.
- Champions of Olympia: Premi e requisiti di sblocco non indicati dalle fonti lette.
- Champions of Olympia: Esistenza e regole della modalita' ranked nel 2026 non chiarite (riseofkingdomsguides: nessun ranking; riseofkingdomshandbook parla di setup ranked).
- Osiris League (scommesse): Formato, calendario e stagioni della Osiris League 2026 non indicati; la pagina letta ha contenuto datato (lastmod 2026-01-02).
- Osiris League (scommesse): Requisiti per partecipare alle scommesse non indicati.
- Golden Kingdom: Cadenza/durata dell'evento e contenuto dei premi ai checkpoint non indicati.
- Golden Kingdom: Perdite reali di truppe: nessuna fonte lo dice esplicitamente (la salute e' dell'evento).
- Shadow Legion (Dark Fortresses): Numero di ondate, premi e regole di difficolta' 2026: le fonti rimandano al pannello evento.
- Esmeralda's Prayer / Esmeralda's Collection: Probabilita' dei premi della ruota non indicate dalla fonte (descrive solo i puntatori).
- Esmeralda's Prayer / Esmeralda's Collection: Requisiti di sblocco e contenuto preciso dei premi 2026 non indicati.
- Silk Road Speculators (carovana d'alleanza) e Desert Tracks: Nessuna fonte 2026 descrive le regole attuali di Silk Road Speculators: dati da rok.guide 2019 (copia Wayback).
- Silk Road Speculators (carovana d'alleanza) e Desert Tracks: Regole di dettaglio di Desert Tracks 2026 non documentate (solo descrizione di una riga).
- Race Against Time: Premi per soglia e requisiti non dettagliati.
- Marauders / Eve of the Crusade (pre-KvK e Lost Kingdom): Meccanica dettagliata dei Marauders (livelli, costo AP, limiti) non descritta dalle fonti 2026 lette.
- Tempest Clash (battaglie navali): Premi, durata e presenza nel calendario 2026 non indicati (pagina con contenuto datato).
- Eventi Anniversario 2026 (versione 1.1.11 'Anniversary Special'): Regole dettagliate, durate e premi di Art Festival, Riddles of the Sphinx, Circus of Wonders, Lucky Red Packet e Desert Tracks 2026 non documentati (solo descrizioni di una riga).
- Halloween 2026 (versione 1.1.12 'Dreams of Phantasma'): Durata del pacchetto Halloween 2026 non indicata.
- Radiant Rivalry (NUOVA modalita' 2026, 1v1 tra regni): Durata delle fasi, tipi di missioni, abbinamento e premi del Radiance Shop non documentati: unica fonte l'articolo ldshop del 22-09-2026.
- Clash of Divine Isles: Regole, requisiti e premi di Clash of Divine Isles non documentati dalle fonti lette (solo la modifica della 1.1.12).
- Nessuna fonte letta pubblica un calendario 2026 con date fisse degli eventi: le date vanno lette dal pannello Events/Calendar del regno (riseofkingdomshandbook, Event Calendar).
- Le pagine di riseofkingdomsguides.com hanno tutte lastmod 2026-01-02 (aggiornamento massivo): il loro contenuto puo' riflettere versioni precedenti del gioco.
- WebSearch non disponibile in questa sessione: la copertura e' limitata alle pagine raggiungibili navigando indici e sitemap dei siti indicati (piu' theriagames e copia Wayback di rok.guide).
- Nessuna fonte 2026 con lineup 'meta' per account Season of Conquest evoluti in Expedition/Canyon/Golden Kingdom: le coppie documentate sono soprattutto epiche/legacy.

## Pagine non raggiungibili

- `https://riseofkingdomsguides.com/holy-sites/`: HTTP 404 (WebFetch) - usati theriagames, riseofkingdomshandbook e heaven-guardian
- `https://riseofkingdomsguides.com/best-commander-pairs-for-barbarian-forts/`: HTTP 404 (WebFetch)
- `https://heaven-guardian.com/rise-of-kingdoms-sunset-canyon-guide-best-lineup/`: HTTP 404 (WebFetch)
- `https://heaven-guardian.com/rise-of-kingdoms-sunset-canyon-guide/`: HTTP 404 (WebFetch)
- `https://www.ldshop.gg/blog/rise-of-kingdoms/sunset-canyon-guide.html`: articolo non trovato (WebFetch restituisce la home del blog)
- `https://www.allclash.com/category/rise-of-kingdoms/ (e sitemap.xml, post-sitemap.xml)`: HTTP 403 (WebFetch e curl, challenge Cloudflare); le singole guide allclash restano leggibili via WebFetch
- `https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/`: HTTP 500 (WebFetch e curl); indice ricostruito da https://www.bluestacks.com/sitemap_index.xml (blog_post-sitemap1..57)
- `https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-barbarian-forts-guide-en.html e rok-barbarians-guide-en.html`: HTTP 500 (curl)
- `https://theriagames.com/guide/rise-of-kingdoms-barbarian-forts-guide/`: HTTP 404
- `https://www.appgamer.com/rise-of-kingdoms/strategy-guide/sanctum-guardians`: HTTP 403 (challenge Cloudflare)
- `https://heaven-guardian.com/post-sitemap3.xml, post-sitemap5.xml`: connection reset (curl); post-sitemap4.xml 404; usati post-sitemap.xml e post-sitemap2.xml
- `https://heaven-guardian.com/ (singole pagine via curl)`: connection reset intermittente: pagine lette via WebFetch o curl con retry
- `https://riseofkingdomsguides.com/ (via curl)`: pagina 'Bot Verification': tutte le pagine lette via WebFetch
- `https://rok.guide/, https://riseofkingdoms.fandom.com/, https://www.riseofkingdoms.org/`: irraggiungibili (indicato nelle istruzioni); per Silk Road usata la copia Wayback Machine di rok.guide

## Tutte le fonti lette (28/09/2026)

- [allclash · sunset canyon tactics 21/02/2020][s40] — <https://www.allclash.com/sunset-canyon-guide-for-rise-of-kingdoms-tactics-commanders-to-use/> — tank/AoE/nuke/support, tank count, backline, defense setup, tattiche, difesa
- [bluestacks · expeditions 11/12/2024][s5] — <https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/guide-expeditions-en.html> — Sun Tzu budget friendly, Aethelflaed, coppie avanzate, burst, healing, reset 00:00 UTC, Aethelflaed prima, healing and sustain …
- [bluestacks · 7th anniversary update 16/09/2025][s22] — <https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-7th-anniversary-update-en.html> — Double Line Formation, Desert Tracks 2025, anniversario 2025, Desert Tracks, Race Against Time, Sign-In Spoils …
- [heaven-guardian · aethelflaed talents pairings 06/08/2026][s9] — <https://heaven-guardian.com/aethelflaed-rise-of-kingdoms-guide-talents-pairings/> — develop through Expedition, Canyon, pairings, talenti/formazione Canyon
- [heaven-guardian · ark osiris dominate 04/08/2026][s50] — <https://heaven-guardian.com/ark-of-osiris-guide-dominate-rise-of-kingdoms/> — ruolo carrier, gathering commanders, obelisk teleport, formati, ruoli, protected event fighting
- [heaven-guardian · charles martel talents 03/08/2026][s44] — <https://heaven-guardian.com/charles-martel-rise-of-kingdoms-guide-talents-pairings/> — Canyon tank build, pairings, tank build Canyon
- [heaven-guardian · lohar barbarian hunter 05/08/2026][s26] — <https://heaven-guardian.com/lohar-rise-of-kingdoms-barbarian-hunter-guide-build/> — secondary for XP
- [heaven-guardian · best commander pairings 12/08/2026][s8] — <https://heaven-guardian.com/rise-of-kingdoms-best-commander-pairings/> — Aethelflaed + Sun Tzu F2P, Aethelflaed+YSG Canyon-style
- [heaven-guardian · ceroli crisis boss 05/08/2026][s10] — <https://heaven-guardian.com/rise-of-kingdoms-ceroli-crisis-guide-boss-tips/> — qualita' del tank, commander selection, ruoli e setup, ruoli, difficolta', preparation checklist …
- [heaven-guardian · champions olympia tips 05/08/2026][s54] — <https://heaven-guardian.com/rise-of-kingdoms-champions-of-olympia-guide-tips/> — best commanders 2026, roles, mappa, ruoli, comandanti
- [heaven-guardian · dominate barbarians forts 03/08/2026][s18] — <https://heaven-guardian.com/rise-of-kingdoms-dominate-barbarians-forts-guide/> — F2P pairing, early spender pairing, 50 AP base, catena, AP base, coppie F2P/spender
- [heaven-guardian · events dominate 03/08/2026][s2] — <https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/> — hospital space for difficult levels, Karuak Ceremony progressivo, aiuto d'alleanza, preparazione, Golden Kingdom prep, preparazione, what to save, F2P milestones
- [heaven-guardian · expedition tips rewards 03/08/2026][s7] — <https://heaven-guardian.com/rise-of-kingdoms-expedition-guide-tips-rewards/> — tank/AoE/support consigliati, support, formazione consigliata, tattiche 3 stelle, priorita' negozio …
- [heaven-guardian · get books covenant 19/09/2026][s27] — <https://heaven-guardian.com/rise-of-kingdoms-get-books-of-covenant-level-up-fast/> — 20.095 Books of Covenant, 5.000 per il 24->25, forti fonte ripetibile gratuita, Boudica/Lohar/Aethelflaed, damage-share non confermato
- [heaven-guardian · level up commanders 03/08/2026][s25] — <https://heaven-guardian.com/rise-of-kingdoms-level-up-commanders-fast-guide/> — Lohar carry method, 70%, Lohar +70% EXP, guardian run workflow, guardian workflow, etiquette, no AP, guardiani senza AP
- [heaven-guardian · lohars trial 08/08/2026][s20] — <https://heaven-guardian.com/rise-of-kingdoms-lohars-trial-guide/> — secondario da livellare, commanders, secondary leveling, bone necklaces, AP management, summoning process …
- [heaven-guardian · maximize action points 03/08/2026][s3] — <https://heaven-guardian.com/rise-of-kingdoms-maximize-action-points-dominate/> — Karuak: verificare consumo AP, limiti giornalieri e aiuto d'alleanza prima di usare oggetti AP, cap 1.000, 45 s per AP, stima del cap, gem refill 100 +50, join only rallies likely to succeed, cap, rigenerazione, oggetti AP, Peacekeeping …
- [heaven-guardian · runes find use 03/08/2026][s29] — <https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/> — best march for collecting runes, one rune, queue-start, collection march, rune, respawn 12 h
- [heaven-guardian · speedups ultimate domination 04/08/2026][s65] — <https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/> — avoid spending AP before Marauders, Marauders value, Marauders
- [heaven-guardian · zones 08/08/2026][s33] — <https://heaven-guardian.com/rise-of-kingdoms-zones-guide/> — Sanctum/Altar obiettivi iniziali, Shrine, Lost Temple, passi livello 1-3
- [heaven-guardian · kvk season 1 24/08/2026][s64] — <https://heaven-guardian.com/rok-kvk-season-1-2-guide-dominate-the-lost-kingdom/> — Peacekeeping commanders for Barbarians, natural AP first, bottled AP, Eve of the Crusade, Honor, AP
- [heaven-guardian · saladin builds pairings 06/08/2026][s46] — <https://heaven-guardian.com/saladin-rise-of-kingdoms-guide-builds-pairings/> — Saladin+Baibars
- [heaven-guardian · yi seong gye 06/08/2026][s45] — <https://heaven-guardian.com/yi-seong-gye-rise-of-kingdoms-ultimate-guide/> — Canyon
- [ldshop · anniversary special 27/08/2026][s36] — <https://www.ldshop.gg/blog/rise-of-kingdoms/anniversary-special.html> — Arms Training nell'Anniversary 1.1.11, Desert Tracks 2026, lista eventi, eventi, cross-kingdom egrimelon stealing …
- [ldshop · halloween 22/09/2026][s61] — <https://www.ldshop.gg/blog/rise-of-kingdoms/halloween-guide.html> — F2P coin method, presenza nel 2026, Halloween 2026, Eve of the Crusade con il Lost Kingdom, Race Against Time nel 1.1.12 …
- [ldshop · kvk defense 22/09/2026][s51] — <https://www.ldshop.gg/blog/rise-of-kingdoms/kvk-defense-guide.html> — Heraclius + Yi Sun-sin Ark of Osiris
- [riseofkingdomsguides · ark osiris strategy 02/01/2026][s49] — <https://riseofkingdomsguides.com/ark-of-osiris-guide-and-strategy/> — carrier, field fighters, gatherers, commanders per ruolo, clear hospital …
- [riseofkingdomsguides · champions olympia 02/01/2026][s53] — <https://riseofkingdomsguides.com/champions-of-olympia-guide-in-rok/> — bandiere, morale, abilita', skills, ranking
- [riseofkingdomsguides · golden kingdom event 02/01/2026][s56] — <https://riseofkingdomsguides.com/golden-kingdom-event-guide-rok/> — tank/support/AoE, commanders, CH17, troops fixed, arrow tower …
- [riseofkingdomsguides · commander pairings 02/01/2026][s43] — <https://riseofkingdomsguides.com/guides/commander-pairings/> — Charles Martel+Scipio, Saladin+Baibars, Cao Cao, coppie Canyon
- [riseofkingdomsguides · lohars trial event 02/01/2026][s34] — <https://riseofkingdomsguides.com/lohars-trial-event/> — only rally, rally, premi
- [riseofkingdomsguides · protect supplies event 02/01/2026][s39] — <https://riseofkingdomsguides.com/protect-the-supplies-event-guide-rok/> — nessuna raccomandazione comandanti, 50 AP, best result, meccanica, premi
- [riseofkingdomsguides · arms training event 02/01/2026][s37] — <https://riseofkingdomsguides.com/rise-of-kingdoms-arms-training-event/> — Khan+YSG, cavalleria burst, supporto, days 1-2 test, army expansion day 3, formato, punti, premi, comandanti
- [riseofkingdomsguides · barbarians barbarian forts 02/01/2026][s17] — <https://riseofkingdomsguides.com/rise-of-kingdoms-barbarians-and-barbarian-forts/> — fort commanders, YSG chain, -2 AP, max 10, livelli, AP catena, comandanti, livelli
- [riseofkingdomsguides · ceroli assault event 02/01/2026][s12] — <https://riseofkingdomsguides.com/rise-of-kingdoms-ceroli-assault-event/> — 50 horns, ticket, boost non attivi, Ceroli Assault
- [riseofkingdomsguides · ceroli crisis 02/01/2026][s11] — <https://riseofkingdomsguides.com/rise-of-kingdoms-ceroli-crisis-guide/> — tank Richard+Alexander, Richard+YSG, Guan+Alexander, DPS Khan+YSG, Minamoto+Cao Cao, coppie, coppie tank/DPS, Keira, matchmaking …
- [riseofkingdomsguides · osiris league betting 02/01/2026][s55] — <https://riseofkingdomsguides.com/rise-of-kingdoms-osiris-league-betting-guide/> — betting, daily/weekly quests, underdog, 50% refund, shop priorities, bundles …
- [riseofkingdomsguides · race against time 03/09/2026][s63] — <https://riseofkingdomsguides.com/rise-of-kingdoms-race-against-time-event/> — commanders, damage boosting methods, 5 min, 3 tentativi, positioning, army expansion 2k gems, formato, tentativi, comandanti
- [riseofkingdomsguides · sunset canyon 02/01/2026][s42] — <https://riseofkingdomsguides.com/rise-of-kingdoms-sunset-canyon-guide/> — Sun Tzu, Joan, Aethelflaed, epici, Boudica Prime, 5 tentativi, punti, tickets final day, rewards …
- [riseofkingdomsguides · shadow legion dark 02/01/2026][s58] — <https://riseofkingdomsguides.com/shadow-legion-and-dark-fortress-guide/> — defensive commanders, attacking Shadow Legion barbarians, requisiti, truppe non muoiono, punti, comandanti
- [riseofkingdomsguides · spring symphony esmeraldas 02/01/2026][s60] — <https://riseofkingdomsguides.com/spring-symphony-and-esmeraldas-prayer-event-guide/> — meccanica, 4 monete/giorno, pointers, conversion, 1.200 gemme, Prayer, Collection, costi, fonti monete …
- [riseofkingdomsguides · ians ballads 02/01/2026][s14] — <https://riseofkingdomsguides.com/step-by-step-ians-ballads-guide-rok/> — nuking commanders, 15-20 stack, reset 2 s, army expansion, attack boost, abilita' dei boss, stack, campsite, comandanti, hardest difficulty
- [riseofkingdomsguides · tempest clash event 02/01/2026][s66] — <https://riseofkingdomsguides.com/tempest-clash-event-ship-battels/> — ship types, format, formato, navi, abilita'
- [riseofkingdomsguides · trial kau karuak 02/01/2026][s16] — <https://riseofkingdomsguides.com/the-trial-of-kau-karuak-event-guide/> — commanders, strongest commanders, timer, reset, 2k gem army expansion, formato, premi, comandanti
- [handbook · action points barbarian 09/09/2026][s23] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-action-points-barbarian-chaining-guide> — AP cap, return before losses, two AP budgets, budget AP, catena
- [handbook · ark osiris 09/09/2026][s48] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-ark-of-osiris-guide> — roles, bringing the wrong pair, roster, roles, budget healing speedups, how alliances win, rewards …
- [handbook · arms training 09/09/2026][s38] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-arms-training-guide> — which pair is best, first run is information, modifier types, milestones vs ranking, ordine modificatori, metodo di test
- [handbook · barbarian forts 18/08/2026][s19] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-barbarian-forts-guide> — best fort commanders, participation, damage share, books, lead rallies, fixed times, Books of Covenant, rally-only, premi, comandanti …
- [handbook · best epic commanders 18/08/2026][s35] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-epic-commanders-f2p> — Lohar epico, sculture da Lohar's Trial
- [handbook · best events spend 18/08/2026][s67] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-events-to-spend-on> — event store priority, priorita' negozi evento
- [handbook · ceroli crisis 09/09/2026][s4] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-ceroli-crisis-guide> — Aethelflaed, Boudica, priorita' negozio, spendere prima della fine, rotazione, shop, meccaniche, rotazione calendario, fitting it into the calendar
- [handbook · champions olympia 09/09/2026][s52] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-champions-of-olympia-guide> — three jobs, F2P friendly, rules, regole, truppe, abilita', skills system
- [handbook · event calendar hub 09/09/2026][s1] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub> — ten-minute weekly check, daily reset, busy week
- [handbook · expedition 18/08/2026][s6] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-expedition-guide> — best-built pair, daily chest, retry freely, breakpoint 11/21/31/41/51, negozio, limiti giornalieri, epico settimanale …
- [handbook · f2p 18/08/2026][s47] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-f2p-guide> — Canyon: truppe equalizzate, fonte di materiali equipaggiamento
- [handbook · golden kingdom 09/09/2026][s57] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-golden-kingdom-guide> — durable front, developed commanders, lineup, floor loop, hazards, when to heal, shop/checkpoint …
- [handbook · ians ballads 09/09/2026][s13] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-ians-ballads-guide> — best damage pair, peacekeeping secondary, CH16+, formato, difficolta', chieftain reward, CH16, 4 giocatori, 2 ore, boss, premi …
- [handbook · karuak ceremony 09/09/2026][s15] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-karuak-ceremony-guide> — peacekeeping march, trainee secondary, switch to developed partner, budget AP, difficolta', AP cap, solo attacks …
- [handbook · lohar 18/08/2026][s21] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-lohar-guide> — Lohar, Rejuvenate, pairings, chain-farming partners, build Lohar, pairings
- [handbook · lohars trial 18/08/2026][s24] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-lohars-trial-guide> — bank action points, peacekeeping pair, how it works, everyone involved collects rewards, do not save relics …
- [handbook · map zones runes 18/08/2026][s28] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-map-zones-runes-guide> — Cao Cao rune, guardian XP, rune, zone, buff Sanctum, rune, Cao Cao velocita'
- [handbook · shadow legion 09/09/2026][s59] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-shadow-legion-guide> — field pair vs defence pair, before leadership starts, reinforce before the crisis, after the event, preparazione, ruoli, rinforzi
- [handbook · sunset canyon 09/09/2026][s41] — <https://riseofkingdomshandbook.com/guides/riseofkingdoms-sunset-canyon-guide> — early five-march lineup, inspect defender, simple comparison, ticket rules, save a deliberate defensive formation …
- [rok.guide (Wayback) · silk road speculators 27/05/2019][s62] — <https://web.archive.org/web/20240725150508/https://www.rok.guide/silk-road-speculators-event/> — regole scorta, costo, ruoli, premi via mail, regole Silk Road
- [theriagames · altar 13/02/2025][s32] — <https://theriagames.com/guide/rise-of-kingdoms-altar-guide/> — nessuna morte agli Altar, buff Altar, perdite
- [theriagames · holy sites 13/02/2025][s31] — <https://theriagames.com/guide/rise-of-kingdoms-holy-sites-guide/> — spawn 00:00/12:00 UTC, 11 h, requisiti, guardiani Shrine/Temple, Lost Temple, contesa 3 giorni, 4 ore, tipi, conteggi, guardiani, contesa
- [theriagames · shrines 13/02/2025][s30] — <https://theriagames.com/guide/rise-of-kingdoms-shrines-guide/> — rally leader AoE, meta' dei feriti gravi muore, buff Shrine, perdite

[s1]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub
[s2]: https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/
[s3]: https://heaven-guardian.com/rise-of-kingdoms-maximize-action-points-dominate/
[s4]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-ceroli-crisis-guide
[s5]: https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/guide-expeditions-en.html
[s6]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-expedition-guide
[s7]: https://heaven-guardian.com/rise-of-kingdoms-expedition-guide-tips-rewards/
[s8]: https://heaven-guardian.com/rise-of-kingdoms-best-commander-pairings/
[s9]: https://heaven-guardian.com/aethelflaed-rise-of-kingdoms-guide-talents-pairings/
[s10]: https://heaven-guardian.com/rise-of-kingdoms-ceroli-crisis-guide-boss-tips/
[s11]: https://riseofkingdomsguides.com/rise-of-kingdoms-ceroli-crisis-guide/
[s12]: https://riseofkingdomsguides.com/rise-of-kingdoms-ceroli-assault-event/
[s13]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-ians-ballads-guide
[s14]: https://riseofkingdomsguides.com/step-by-step-ians-ballads-guide-rok/
[s15]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-karuak-ceremony-guide
[s16]: https://riseofkingdomsguides.com/the-trial-of-kau-karuak-event-guide/
[s17]: https://riseofkingdomsguides.com/rise-of-kingdoms-barbarians-and-barbarian-forts/
[s18]: https://heaven-guardian.com/rise-of-kingdoms-dominate-barbarians-forts-guide/
[s19]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-barbarian-forts-guide
[s20]: https://heaven-guardian.com/rise-of-kingdoms-lohars-trial-guide/
[s21]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-lohar-guide
[s22]: https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-7th-anniversary-update-en.html
[s23]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-action-points-barbarian-chaining-guide
[s24]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-lohars-trial-guide
[s25]: https://heaven-guardian.com/rise-of-kingdoms-level-up-commanders-fast-guide/
[s26]: https://heaven-guardian.com/lohar-rise-of-kingdoms-barbarian-hunter-guide-build/
[s27]: https://heaven-guardian.com/rise-of-kingdoms-get-books-of-covenant-level-up-fast/
[s28]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-map-zones-runes-guide
[s29]: https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/
[s30]: https://theriagames.com/guide/rise-of-kingdoms-shrines-guide/
[s31]: https://theriagames.com/guide/rise-of-kingdoms-holy-sites-guide/
[s32]: https://theriagames.com/guide/rise-of-kingdoms-altar-guide/
[s33]: https://heaven-guardian.com/rise-of-kingdoms-zones-guide/
[s34]: https://riseofkingdomsguides.com/lohars-trial-event/
[s35]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-epic-commanders-f2p
[s36]: https://www.ldshop.gg/blog/rise-of-kingdoms/anniversary-special.html
[s37]: https://riseofkingdomsguides.com/rise-of-kingdoms-arms-training-event/
[s38]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-arms-training-guide
[s39]: https://riseofkingdomsguides.com/protect-the-supplies-event-guide-rok/
[s40]: https://www.allclash.com/sunset-canyon-guide-for-rise-of-kingdoms-tactics-commanders-to-use/
[s41]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-sunset-canyon-guide
[s42]: https://riseofkingdomsguides.com/rise-of-kingdoms-sunset-canyon-guide/
[s43]: https://riseofkingdomsguides.com/guides/commander-pairings/
[s44]: https://heaven-guardian.com/charles-martel-rise-of-kingdoms-guide-talents-pairings/
[s45]: https://heaven-guardian.com/yi-seong-gye-rise-of-kingdoms-ultimate-guide/
[s46]: https://heaven-guardian.com/saladin-rise-of-kingdoms-guide-builds-pairings/
[s47]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-f2p-guide
[s48]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-ark-of-osiris-guide
[s49]: https://riseofkingdomsguides.com/ark-of-osiris-guide-and-strategy/
[s50]: https://heaven-guardian.com/ark-of-osiris-guide-dominate-rise-of-kingdoms/
[s51]: https://www.ldshop.gg/blog/rise-of-kingdoms/kvk-defense-guide.html
[s52]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-champions-of-olympia-guide
[s53]: https://riseofkingdomsguides.com/champions-of-olympia-guide-in-rok/
[s54]: https://heaven-guardian.com/rise-of-kingdoms-champions-of-olympia-guide-tips/
[s55]: https://riseofkingdomsguides.com/rise-of-kingdoms-osiris-league-betting-guide/
[s56]: https://riseofkingdomsguides.com/golden-kingdom-event-guide-rok/
[s57]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-golden-kingdom-guide
[s58]: https://riseofkingdomsguides.com/shadow-legion-and-dark-fortress-guide/
[s59]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-shadow-legion-guide
[s60]: https://riseofkingdomsguides.com/spring-symphony-and-esmeraldas-prayer-event-guide/
[s61]: https://www.ldshop.gg/blog/rise-of-kingdoms/halloween-guide.html
[s62]: https://web.archive.org/web/20240725150508/https://www.rok.guide/silk-road-speculators-event/
[s63]: https://riseofkingdomsguides.com/rise-of-kingdoms-race-against-time-event/
[s64]: https://heaven-guardian.com/rok-kvk-season-1-2-guide-dominate-the-lost-kingdom/
[s65]: https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/
[s66]: https://riseofkingdomsguides.com/tempest-clash-event-ship-battels/
[s67]: https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-events-to-spend-on
