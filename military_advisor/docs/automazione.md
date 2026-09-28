# Automazione del bot — mappa delle schermate, ADB, riconoscimento e rischi

Ricerca del **28/09/2026** per i test di domani sul telefono Android collegato al PC. Dati strutturati: `data/fragments/automazione.json` (schermate, comandi adb, OCR/template matching, rischi, piano di test, fonti, lacune). Nomi tecnici in inglese; accanto a ogni affermazione c'è la fonte con la data della pagina. Dove una fonte non dice nulla il JSON ha `null` e la voce è nelle *gaps*. Le **coordinate dei pulsanti non sono documentate da nessuna fonte**: si misurano domani con i test.

> **Da sapere prima di tutto.** I Termini di servizio di Lilith vietano esplicitamente i bot (17.1.15 e 17.1.18). Lilith ha bannato account per botting (report ufficiali del 2020; 167.000 personaggi bannati in tre mesi secondo il Dev Feedback del gennaio 2021). Dal 30/04/2026 (patch 1.1.07) c'è anche un **Conduct Score** che toglie punti a chi usa "third-party tools such as scripts or cheats". Le precauzioni di questa guida riducono i danni collaterali, cioè spese accidentali e azioni sbagliate, ma **non rendono il bot conforme ai ToS**. Il rischio di sospensione resta del proprietario dell'account. Dettagli e citazioni sono nella sezione 4 ([Lilith ToS, 15/04/2025 (campo show_at della pagina)](https://www.lilith.com/termofservice/?locale=en_US) · [forum ufficiale Lilith, 27/01/2021](https://forum-global.lilithgame.com/post/1044203) · [forum ufficiale Lilith, 30/04/2026](https://forum-global.lilithgame.com/post/2232581)).

**Vincoli del bot, sempre validi:** mai gemme; nessun tocco su pulsanti con icona gemma o prezzo; conferma dell'utente per attacchi, rally e scout contro giocatori e per i materiali rari (gate già in `advisor.py`). Se compare la **finestra di verifica anti-bot**, il bot si ferma e avvisa il proprietario. Non deve provare a risolverla.

---

## Indice
1. [Mappa delle schermate](#1-mappa-delle-schermate)
2. [ADB: comandi e setup](#2-adb-comandi-e-setup)
3. [Riconoscimento: OCR e template matching](#3-riconoscimento-ocr-e-template-matching)
4. [Rischi: Termini di servizio e conseguenze](#4-rischi-termini-di-servizio-e-conseguenze)
5. [Piano di test per domani](#5-piano-di-test-per-domani)
6. [Lacune e fonti non raggiungibili](#6-lacune-e-fonti-non-raggiungibili)

---

## 1. Mappa delle schermate

Client in inglese. Le fonti testuali descrivono **cosa c'è** nelle schermate e quasi mai **dove si trova** un pulsante. Per questo il percorso manca (`null`) quando nessuna fonte lo indica. I nomi italiani vengono solo dalla scheda italiana di Google Play, scritta dallo sviluppatore: vanno controllati sul client italiano, perché il gioco supporta l'italiano ([App Store, 22/09/2026 (versione 1.1.12.20)](https://apps.apple.com/us/app/rise-of-kingdoms/id1354260888)).

| Schermata | Nome IT | Come ci si arriva (fonte) |
|---|---|---|
| City view / HUD principale (home) | — | Schermata di partenza dopo il caricamento; dalla mappa si torna in città con il pulsante mappa/città. |
| Governor Profile | — | HUD -> tocco sull'avatar in alto a sinistra. |
| Settings | — | HUD -> avatar (Governor Profile) -> Settings. |
| Redeem (codici regalo) | — | Avatar in alto a sinistra -> Settings -> opzione 'Redeem' a forma di scatola regalo. |
| Commanders (lista comandanti) | Comandanti | **non documentato** (da misurare) |
| Dettaglio comandante (Skills, Talents, Equipment, Formation/Armaments) | — | Commanders -> tocco sul comandante (percorso da confermare). |
| Troops overview (truppe totali, in città, sulla mappa) | — | Avatar -> Governor Profile -> sezione Troops. |
| Addestramento: Barracks / Stable / Archery Range / Siege Workshop | — | Città -> tocco sull'edificio (Barracks = fanteria, Stable = cavalleria, Archery Range = arcieri, Siege Workshop = assedio). |
| Hospital | — | Città -> tocco sull'Hospital (gli ospedali sono più edifici: 1°, 2° CH4, 3° CH9, 4° CH15). |
| Items (inventario) | — | **non documentato** (da misurare) |
| Alliance (Help, Technology/Donate, Gifts, Territory, Shop) | Alleanza | Menu Alliance (pulsante non localizzato dalle fonti) -> sezioni Help, Technology, Gifts, Territory, Shop. |
| Events | — | HUD -> icona Events 'paper-style'. |
| Campaign -> Expedition | Spedizione | HUD -> menu Campaign -> Expedition. |
| Tavern | — | Città -> Tavern. |
| Courier Station (Mysterious Merchant) | — | Città -> Courier Station (sblocco City Hall 6). |
| Scout Camp | — | Città -> Scout Camp (sblocco City Hall 2). |
| Ricerca sulla mappa (barbari, forti, punti risorsa) | — | Mappa -> pulsante Search (posizione non documentata) -> tipo di bersaglio e livello -> ricerca. |
| March / preset di marcia | — | Dal bersaglio (es. barbaro o nodo) -> schermata di creazione marcia; preset salvati. |
| Rally | — | Bersaglio (es. Barbarian Fort) -> Rally; gli altri si uniscono dall'interfaccia d'alleanza. |
| State Forum: formazioni e armamenti (Travel, Dispatch, Recycle, Transmute) | — | Città -> State Forum -> Travel / Dispatch; gestione armamenti nella sezione Armament/Formation del comandante (percorso esatto da verificare, vedi OFFICINA_ARMAMENTI.md). |
| Mail (posta) | — | **non documentato** (da misurare) |
| Popup e stati bloccanti (da riconoscere prima di ogni azione) | — | **non documentato** (da misurare) |

**Regola generale sulle gemme.** Qualsiasi pulsante con l'icona gemma, un prezzo in valuta reale o testi tipo 'Buy', 'Purchase', 'Refresh' con costo, 'Instant', 'Use Gems' = VIETATO. Il riconoscimento dell'icona gemma va fatto con template matching a colori su tutta la finestra prima di ogni tocco (un solo positivo = annullare).

**Reti di sicurezza già presenti nel gioco:**
- **Settings > General Settings > 'gem use confirmation'**: Chiede conferma prima di spendere gemme: tenerla attiva. ([wiki fandom, 02/12/2025](https://riseofkingdoms.fandom.com/wiki/Governor_Profile))
- **Password secondaria (Settings, dalla 1.0.42)**: Se impostata, è richiesta per: permessi d'alleanza (1.0.50), riciclo armamenti (1.0.66), trasmutazione (1.0.77), immigrazione e forgiatura/raffinazione/risveglio/smantellamento di equipaggiamento leggendario (1.0.83), collegamento di un nuovo metodo di login (1.0.84), donazioni Flux Coins (1.1.04), inscribing/converting armamenti (1.1.08). Il bot non deve conoscerla: queste azioni restano all'utente. ([forum ufficiale Lilith, 20/01/2021](https://forum-global.lilithgame.com/post/1041743) · [forum ufficiale Lilith, 06/09/2021](https://forum-global.lilithgame.com/post/1125881) · [forum ufficiale Lilith, 10/02/2023](https://forum-global.lilithgame.com/post/1433064) · [forum ufficiale Lilith, 06/12/2023](https://forum-global.lilithgame.com/post/1599092) · [forum ufficiale Lilith, 20/06/2024](https://forum-global.lilithgame.com/post/1670239) · [forum ufficiale Lilith, 23/07/2024](https://forum-global.lilithgame.com/post/1726094) · [forum ufficiale Lilith, 26/02/2026](https://forum-global.lilithgame.com/post/2213663) · [forum ufficiale Lilith, 27/05/2026](https://forum-global.lilithgame.com/post/2246725))

**Lingua.** Il gioco supporta l'italiano (App Store: lingue incluse 'Italian'); il cambio lingua è in Settings > Language. Per OCR e template usare UNA lingua fissa: il client inglese è quello descritto dalle fonti; i nomi italiani delle schermate non sono documentati (tranne pochi termini della scheda Google Play). ([App Store, 22/09/2026 (versione 1.1.12.20)](https://apps.apple.com/us/app/rise-of-kingdoms/id1354260888) · [wiki fandom, 02/12/2025](https://riseofkingdoms.fandom.com/wiki/Governor_Profile) · [Google Play, 17/09/2026](https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=it&gl=IT))

### City view / HUD principale (home)

**Percorso:** Schermata di partenza dopo il caricamento; dalla mappa si torna in città con il pulsante mappa/città.

**Elementi stabili / cosa si vede:**
- Ritratto/avatar del governatore in alto a sinistra: apre il profilo (Governor Profile).
- Pulsante 'globe map/city' (alterna mappa e città): due tocchi di fila riportano la telecamera nella posizione standard, utile prima di toccare edifici a coordinate fisse (BlueStacks, guida macro).
- Icona Events 'paper-style' (a forma di foglio) nell'interfaccia principale (heaven-guardian).
- Pulsante a freccia accanto al ritratto: menu a tendina con, tra l'altro, l'opzione teleport (BlueStacks FAQ, 2021: da verificare).
- Queue management (dal City Hall 8, patch 1.1.01): pannello con costruzione, addestramento, ricerca, cure, esplorazione e donazioni d'alleanza, con azioni rapide; disattivabile dalle Settings.
- Nella maggior parte delle finestre c'e' un'icona 'i' con le informazioni (wiki FAQ).

**Insidie:**
- La posizione della telecamera cambia le coordinate degli edifici: prima di toccare un edificio riportare la vista allo standard (doppio tocco sul pulsante mappa/città) e riconoscere l'edificio per immagine, non per coordinate assolute.
- Banner/offerte e schede 'returnee' possono comparire sulla schermata principale (handbook, returning player).
- Dopo manutenzioni arriva posta di compensazione; dopo un aggiornamento obbligatorio il client può bloccarsi al caricamento (handbook, server status).
- Coordinate e aspetto degli elementi del HUD (barra risorse, pulsanti in basso) NON documentati: da misurare domani (test T04-T06).

*Fonti:* [wiki fandom, 02/12/2025](https://riseofkingdoms.fandom.com/wiki/Governor_Profile) · [BlueStacks, 23/12/2024](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-bluestacks-macros-en.html) · [heaven-guardian, 03/08/2026](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/) · [BlueStacks, 10/02/2021](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-faqs-en.html) · [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2161435) · [wiki fandom, 25/06/2026](https://riseofkingdoms.fandom.com/wiki/Frequently_Asked_Questions) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-returning-player-guide) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-server-status-and-fixes)

### Governor Profile

**Percorso:** HUD -> tocco sull'avatar in alto a sinistra.

**Elementi stabili / cosa si vede:**
- Mostra: Governor ID, nome, avatar, civiltà, alleanza, Power, Kills (con '(?)' per il dettaglio per tier), Action Points (massimo 1000 senza oggetti).
- Sezioni: More Info (statistiche di potenza, battaglia, risorse), Rankings (dal City Hall 8), Alliance, Troops, Achievements (dal City Hall 6), Settings.
- Sezione Troops: totale unità, 'In the City', 'On the Map', più march queue (dispatch queue), capacità dell'ospedale e potenza truppe -> fonte principale per la lettura OCR delle truppe.

**Insidie:**
- Il Governor ID serve per il supporto e non va condiviso fuori (handbook).
- In Alliance, senza alleanza compaiono 'Join' e 'Create': Create costa 500 gemme -> non premere.

*Fonti:* [wiki fandom, 02/12/2025](https://riseofkingdoms.fandom.com/wiki/Governor_Profile) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-governor-id-account-guide)

### Settings

**Percorso:** HUD -> avatar (Governor Profile) -> Settings.

**Elementi stabili / cosa si vede:**
- Mostra la versione del gioco e data/ora UTC (utile per log e controllo aggiornamenti).
- Sottosezioni (wiki): Notifications, General Settings (grafica, frame rate, volume, 'gem use confirmation', 'march queue shortcut', visualizzazione UI), Emojis, Character Management, Account ('Link or Switch'), Customer Service, Language, Community, Search Governor, Redemption (codici), Blocked Mail.
- Password secondaria impostabile dalle Settings (patch 1.0.42): richiesta per operazioni sensibili (vedi risks.safety_nets).
- Settings - DLC: download manager dei contenuti aggiuntivi (patch 1.0.77).
- Opzione 'Search/Return Switch' (1.0.94, solo mobile): se attiva il pulsante Search diventa 'Return to City' quando è selezionata una truppa.

**Insidie:**
- MAI toccare: Account -> Switch/Link, Character Management -> Create New Character, 'Other' -> 'Delete Account' (cancellazione definitiva), Language (cambia tutti i testi e rompe OCR/template).
- 'gem use confirmation' deve restare ATTIVA: è la rete di sicurezza contro spese di gemme accidentali (verificarla nei test T00 e T08, solo lettura).
- Le Settings sono cambiate negli anni (wiki aggiornata al 2025-12-02): i nomi esatti vanno letti sul telefono.

*Fonti:* [wiki fandom, 02/12/2025](https://riseofkingdoms.fandom.com/wiki/Governor_Profile) · [forum ufficiale Lilith, 20/01/2021](https://forum-global.lilithgame.com/post/1041743) · [forum ufficiale Lilith, 06/12/2023](https://forum-global.lilithgame.com/post/1599092) · [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2030530) · [riseofkingdomsguides, 02/01/2026](https://riseofkingdomsguides.com/how-to-delete-unlink-account-in-rise-of-kingdoms/) · [heaven-guardian, 03/08/2026](https://heaven-guardian.com/rise-of-kingdoms-farm-account-guide-for-max-resources/) · [BlueStacks, 24/01/2025](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-multiple-devices-update-en.html) · [heaven-guardian, 18/09/2026](https://heaven-guardian.com/rise-of-kingdoms-codes/)

### Redeem (codici regalo)

**Percorso:** Avatar in alto a sinistra -> Settings -> opzione 'Redeem' a forma di scatola regalo.

**Elementi stabili / cosa si vede:**
- Campo di testo per il codice; dopo l'invio compare un messaggio di conferma; le ricompense arrivano nell'inventario (Items) o nella posta.

**Insidie:**
- Il codice si applica al governatore connesso in quel momento (con più personaggi, controllare quale).
- Inserire testo richiede 'input text': testare prima su un codice scaduto per vedere i messaggi d'errore ('already redeemed' / 'expired').

*Fonti:* [heaven-guardian, 18/09/2026](https://heaven-guardian.com/rise-of-kingdoms-codes/) · [handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-gift-codes)

### Commanders (lista comandanti) — *Comandanti*

**Percorso:** non documentato dalle fonti lette → da misurare domani.

**Elementi stabili / cosa si vede:**
- Il nome 'Comandanti' compare nella scheda italiana di Google Play.
- Ogni comandante ha tre specialità (alberi dei talenti), quattro abilità sbloccate con le stelle e, per Epic/Legendary, una quinta abilità 'expertise' (wiki).

**Insidie:**
- Percorso e posizione del pulsante Commanders NON documentati da nessuna fonte letta: da individuare domani (test T07).
- Filtri/ordinamenti della lista non documentati.

*Fonti:* [Google Play, 17/09/2026](https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=it&gl=IT) · [wiki fandom, 16/07/2023](https://riseofkingdoms.fandom.com/wiki/Commander_Guide)

### Dettaglio comandante (Skills, Talents, Equipment, Formation/Armaments)

**Percorso:** Commanders -> tocco sul comandante (percorso da confermare).

**Elementi stabili / cosa si vede:**
- Skills: potenziare un'abilità ne sceglie una a CASO tra quelle disponibili fino al livello 5 (wiki) -> consuma sculture.
- Talents: un punto talento per livello, altri alle stelle 5 e 6; il reset dei talenti è costoso (oggetto Talent Reset).
- Descrizioni abilità: dalla 1.0.91 esiste un interruttore tra versione semplificata e completa del testo (cambia cio' che legge l'OCR).
- Formation: una formazione si assegna al comandante mentre è in città; 4 slot armamento (touchscreengaming).
- Le note 1.1.01 citano 'customizable equipment and armament loadout presets' nelle 'Commander Settings', ma nella sezione dedicata a Champions of Olympia: non riguardano la schermata normale del comandante.

**Insidie:**
- MAI premere senza conferma dell'utente: potenziamento abilità (sculture), stelle (sculture/Starlight), reset talenti, cambio equipaggiamento (dalla 1.0.92 chiede conferma quando si cambia il setup).
- Posizione delle schede (Skills/Talents/Equipment/Formation) non documentata: da mappare domani (test T07).
- Numero di slot equipaggiamento: vedi data/fragments/equipaggiamento.json (non riverificato qui).

*Fonti:* [wiki fandom, 16/07/2023](https://riseofkingdoms.fandom.com/wiki/Commander_Guide) · [forum ufficiale Lilith, 24/02/2025](https://forum-global.lilithgame.com/post/1935973) · [touchscreengaming, 10/10/2025](https://touchscreengaming.com/formations-guide/) · [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2161435) · [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/1963188)

### Troops overview (truppe totali, in città, sulla mappa)

**Percorso:** Avatar -> Governor Profile -> sezione Troops.

**Elementi stabili / cosa si vede:**
- Tre viste: Total Number of Units, In the City, On the Map; mostra anche dispatch queue, capacità ospedale e potenza truppe (wiki).
- City Hall -> icona 'grafico' con le statistiche/bonus (es. velocità di raccolta per risorsa) (riseofkingdomsguides).

**Insidie:**
- La richiesta chiedeva 'Troops (City Hall)': nessuna fonte letta descrive un pulsante Troops sul City Hall; la fonte documentata è la sezione Troops del profilo. Da verificare domani (test T06).
- Numeri grandi con separatori delle migliaia: usare il parser di recognition.ocr.number_parsing.

*Fonti:* [wiki fandom, 02/12/2025](https://riseofkingdoms.fandom.com/wiki/Governor_Profile) · [riseofkingdomsguides, s.d.](https://riseofkingdomsguides.com/farming-gathering-guide/)

### Addestramento: Barracks / Stable / Archery Range / Siege Workshop

**Percorso:** Città -> tocco sull'edificio (Barracks = fanteria, Stable = cavalleria, Archery Range = arcieri, Siege Workshop = assedio).

**Elementi stabili / cosa si vede:**
- Cinque tier per tipo, sbloccati con la ricerca; le unità esistenti si possono promuovere di un tier alla volta (costo complessivo maggiore che addestrare direttamente il tier alto).
- Ogni edificio ha una coda di addestramento separata.
- L'aiuto d'alleanza NON riduce i tempi di addestramento (solo costruzione, ricerca, cure).

**Insidie:**
- Quantità (slider/campo numerico), pulsante Train, pulsante Upgrade e loro posizione: NON documentati nelle fonti lette -> mappare domani (test T12) senza premere Train.
- I pulsanti che completano o velocizzano con gemme (le gemme si possono spendere 'directly to speed up training, researching, or building') vanno riconosciuti dall'icona gemma e MAI premuti.
- Durante gli eventi (es. MGE) il punteggio dell'upgrade è la differenza tra i tier: il piano di addestramento resta dell'advisor, il bot esegue solo ordini già confermati.

*Fonti:* [wiki fandom, 29/04/2020](https://riseofkingdoms.fandom.com/wiki/Buildings/Barracks) · [heaven-guardian, 02/09/2026](https://heaven-guardian.com/rise-of-kingdoms-best-troops-training-guide/) · [wiki fandom, 26/09/2026](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) · [wiki fandom, 31/05/2025](https://riseofkingdoms.fandom.com/wiki/Resources)

### Hospital

**Percorso:** Città -> tocco sull'Hospital (gli ospedali sono più edifici: 1°, 2° CH4, 3° CH9, 4° CH15).

**Elementi stabili / cosa si vede:**
- Cura dei feriti gravi; i feriti leggeri guariscono al rientro in città.
- Se l'ospedale è pieno i feriti in eccesso muoiono.
- Gli sviluppatori riportano che 'most governors prefer to heal all troops at once' (cura di tutti di default).
- Le cure beneficiano dell'Alliance Help.

**Insidie:**
- Pulsanti Heal / cura istantanea in gemme: posizione non documentata; mai la variante con gemme.
- Se la città è sotto rally non si può curare fino alla fine del rally (riseofkingdomsguides).
- La guida handbook sconsiglia di 'automate taps' per le cure (consiglio community).

*Fonti:* [wiki fandom, 30/04/2020](https://riseofkingdoms.fandom.com/wiki/Buildings/Hospital) · [forum ufficiale Lilith, 28/04/2023](https://forum-global.lilithgame.com/post/1466061) · [wiki fandom, 26/09/2026](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) · [riseofkingdomsguides, 02/01/2026](https://riseofkingdomsguides.com/hospital/) · [handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-healing-hospital-guide)

### Items (inventario)

**Percorso:** non documentato dalle fonti lette → da misurare domani.

**Elementi stabili / cosa si vede:**
- Gruppi di oggetti nella wiki (2019): Resources, Speedups, Boosts, Equipment, Other (+ oggetti evento); probabile corrispondenza con le schede dell'inventario, da verificare.
- Le ricompense dei codici arrivano negli Items o nella posta.
- Le risorse in forma di oggetto non possono essere saccheggiate.

**Insidie:**
- Pulsante Items e schede: posizione non documentata (test T11).
- Usare un oggetto lo consuma: in lettura il bot apre solo le schede e fa OCR delle quantità; 'Use' solo con ordine confermato (materiali rari -> gate dell'advisor).

*Fonti:* [wiki fandom, 01/12/2019](https://riseofkingdoms.fandom.com/wiki/Items) · [heaven-guardian, 18/09/2026](https://heaven-guardian.com/rise-of-kingdoms-codes/) · [wiki fandom, 31/05/2025](https://riseofkingdoms.fandom.com/wiki/Resources)

### Alliance (Help, Technology/Donate, Gifts, Territory, Shop) — *Alleanza*

**Percorso:** Menu Alliance (pulsante non localizzato dalle fonti) -> sezioni Help, Technology, Gifts, Territory, Shop.

**Elementi stabili / cosa si vede:**
- Help: pulsante 'Alliance Help' dopo aver avviato costruzione/ricerca/cura; gli altri vedono una 'mano' sopra l'Alliance Center; ogni aiuto toglie 1% del tempo o 1 minuto (fino a 3 min con Together We Rise). Aiutare gli altri: menu 'Help' nella sezione Alliance (crediti).
- Technology: donazioni di risorse nella sezione 'Technology' (Technology panel/tab) per crediti.
- Gifts: esiste 'Claim All' per i regali normali, NON per quelli rari (sviluppatori, 2022).
- Territory: i membri ritirano il 50% della produzione delle risorse d'alleanza nella pagina Alliance Territory.
- Shop d'alleanza: crediti individuali per sculture, teleport, passaporti (handbook).
- Sezione Alliance anche nel Governor Profile (Join/Create senza alleanza).

**Insidie:**
- Senza alleanza, 'Create' costa 500 gemme.
- Donazioni: seguire l'interfaccia (non sempre oro); verificare che non compaia un'opzione in gemme.
- Donare Flux Coins all'armeria d'alleanza richiede riconferma e password secondaria (1.1.04).
- Limite crediti da Help: fino a 10.000 crediti individuali al giorno (heaven-guardian).

*Fonti:* [wiki fandom, 26/09/2026](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) · [wiki fandom, 12/06/2024](https://riseofkingdoms.fandom.com/wiki/Territory) · [forum ufficiale Lilith, 26/10/2022](https://forum-global.lilithgame.com/post/1395812) · [Theria Games, 06/02/2025](https://theriagames.com/guide/rise-of-kingdoms-alliance-center-guide/) · [heaven-guardian, 19/09/2026](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-shop-guide) · [handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-guide-hub) · [BlueStacks, 06/12/2024](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-ultimate-alliance-guide-en.html) · [forum ufficiale Lilith, 26/02/2026](https://forum-global.lilithgame.com/post/2213663) · [Google Play, 17/09/2026](https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=it&gl=IT)

### Events

**Percorso:** HUD -> icona Events 'paper-style'.

**Elementi stabili / cosa si vede:**
- Elenco eventi attivi e in arrivo con countdown; orari in UTC; Monument per gli obiettivi di regno.

**Insidie:**
- Molti eventi hanno negozi e acquisti in gemme (es. Wheel of Fortune di Season 2: gli Spin Ticket si ottengono da pacchetti o si comprano con gemme, 1.0.94; More Than Gems conta la spesa in gemme): il bot legge soltanto, non compra.
- I contatori giornalieri e le registrazioni d'alleanza possono chiudere prima del countdown principale (handbook).

*Fonti:* [heaven-guardian, 03/08/2026](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/) · [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2030530) · [handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub)

### Campaign -> Expedition — *Spedizione*

**Percorso:** HUD -> menu Campaign -> Expedition.

**Elementi stabili / cosa si vede:**
- La schermata Campaign raggruppa le modalità (Expedition, Sunset Canyon, Lost Canyon...); pallini rossi di promemoria per le sfide disponibili (1.0.90).
- Expedition: stelle 1-3 per missione; con 3 stelle le ricompense si ritirano ogni giorno senza rigiocare; 'Click the button on the top left corner to claim all 3-Star mission rewards'; reset giornaliero alle 00:00 UTC.
- Le truppe in Expedition sono simulate: niente morti né ospedale.
- Medal Store con Medals of the Conqueror.

**Insidie:**
- Posizione del menu Campaign non documentata (test T11).
- Il bot può limitarsi al ritiro giornaliero del forziere (azione senza costo) solo dopo il test di sola lettura.

*Fonti:* [BlueStacks, 11/12/2024](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/guide-expeditions-en.html) · [forum ufficiale Lilith, 31/12/2024](https://forum-global.lilithgame.com/post/1896244) · [wiki fandom, 11/03/2024](https://riseofkingdoms.fandom.com/wiki/Expedition) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-expedition-guide) · [Google Play, 17/09/2026](https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=it&gl=IT)

### Tavern

**Percorso:** Città -> Tavern.

**Elementi stabili / cosa si vede:**
- Silver Chests (Silver Keys), Golden Chests (Golden Keys), Equipment Chests.
- Aperture gratuite: handbook 'five free openings every day' per gli Silver e circa una Golden gratuita ogni due giorni; riseofkingdomsguides: 3-10 Silver gratuiti al giorno e Golden gratuita ogni 3-2 giorni secondo il livello della Tavern (vedi conflicts nel campo pitfalls).
- Opzione per aprire tutte le chiavi se se ne hanno 10 o più.

**Insidie:**
- Conflitto sul numero di aperture gratuite (dipende dal livello): leggerlo dal contatore in gioco.
- Se non ci sono chiavi, un pulsante di apertura potrebbe costare gemme: non documentato -> riconoscere l'icona gemma e fermarsi.
- Le probabilità mostrate sono contestate dalla community (handbook): irrilevante per il bot.

*Fonti:* [wiki fandom, 01/09/2020](https://riseofkingdoms.fandom.com/wiki/Buildings/Tavern) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-tavern-keys-guide) · [riseofkingdomsguides, 02/01/2026](https://riseofkingdomsguides.com/tavern/) · [Theria Games, 08/02/2025](https://theriagames.com/guide/rise-of-kingdoms-tavern-guide/)

### Courier Station (Mysterious Merchant)

**Percorso:** Città -> Courier Station (sblocco City Hall 6).

**Elementi stabili / cosa si vede:**
- Icona del Mysterious Merchant (la figura della mercante) sopra l'edificio quando arriva; arrivo garantito alle 0:00 UTC, più visite dopo upgrade, addestramenti e barbari.
- 16 oggetti (4 risorse, 4 speedup, 4 boost, 4 altri); pulsante 'Refresh' in alto a destra della finestra.
- Prezzi in gemme (sconto 30-90%) oppure in cibo/legno (sconto 10-40%).

**Insidie:**
- Refresh: 1° gratis, poi 100, 200, 300, 400 gemme -> il bot può al massimo usare il refresh gratuito e solo se l'utente lo abilita.
- Comprare SOLO voci con prezzo in cibo/legno e solo con ordine confermato; qualunque prezzo con icona gemma = non toccare.
- riseofkingdomsguides riporta riacquisti fino a 5 volte con costi Free -> 100 -> 200 -> 300 -> 400 gemme (coerente con la wiki).

*Fonti:* [wiki fandom, 11/01/2020](https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station) · [Theria Games, 07/02/2025](https://theriagames.com/guide/rise-of-kingdoms-courier-station-guide/) · [riseofkingdomsguides, 02/01/2026](https://riseofkingdomsguides.com/courier-station/)

### Scout Camp

**Percorso:** Città -> Scout Camp (sblocco City Hall 2).

**Elementi stabili / cosa si vede:**
- Pulsante 'Explore' accanto a ogni scout: seleziona automaticamente il blocco di nebbia inesplorato più vicino alla città; premendo di nuovo 'Explore' lo scout parte.
- Pulsante 'Visit' accanto alle scoperte non ancora esplorate (Theria).
- Posta 'Scouting Report' aggiornata a ogni scoperta, con etichetta verde 'NEW!'.
- Villaggi tribali: icona regalo sopra; toccando l'icona si riceve la ricompensa. Caverne misteriose: selezionarle e inviare uno scout.

**Insidie:**
- Esplorare è gratuito (nessun costo documentato), ma gli scout inviati su città o edifici di altri giocatori sono ricognizioni ostili: il bot NON deve usare 'Scout' su giocatori senza conferma.
- Numero di scout (riseofkingdomsguides: tre) da leggere in gioco.

*Fonti:* [wiki fandom, 03/06/2025](https://riseofkingdoms.fandom.com/wiki/Scouting) · [wiki fandom, 22/11/2023](https://riseofkingdoms.fandom.com/wiki/Buildings/Scout_Camp) · [Theria Games, 07/02/2025](https://theriagames.com/guide/rise-of-kingdoms-scout-camp-guide/) · [riseofkingdomsguides, 02/01/2026](https://riseofkingdomsguides.com/scouting-tribal-village-and-mysterious-cave-guide/) · [heaven-guardian, 02/09/2026](https://heaven-guardian.com/rise-of-kingdoms-scout-camp-guide/)

### Ricerca sulla mappa (barbari, forti, punti risorsa)

**Percorso:** Mappa -> pulsante Search (posizione non documentata) -> tipo di bersaglio e livello -> ricerca.

**Elementi stabili / cosa si vede:**
- Esiste un pulsante 'Search' (citato nelle note 1.0.94 a proposito dell'opzione 'Search/Return Switch', solo versione mobile).
- Dalla 1.1.02 la ricerca trova anche i Barbarian Forts attaccabili (e Marauders durante 'Eve of the Crusade').
- Dalla 1.0.91 i punti risorsa già raggiunti da altri o con poche riserve hanno priorità di ricerca più bassa.
- Il raggio della ricerca è limitato: se non trova livelli alti bisogna zoomare e cercare a mano (riseofkingdomsguides).
- I livelli dei barbari si sbloccano battendo il livello precedente; il livello cercabile dipende dal regno.

**Insidie:**
- Con 'Search/Return Switch' attivo il pulsante Search diventa 'Return to City' quando è selezionata una truppa: il template deve riconoscere entrambe le icone.
- Attaccare barbari consuma Action Points (da leggere prima di ogni invio).
- Esiste la funzione ufficiale Auto-Peacekeeping (caccia automatica ai barbari, ottimizzata in 1.1.01, 1.1.04, 1.1.07 con livelli salvati e display AP): è uno strumento del gioco da preferire all'automazione esterna.

*Fonti:* [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2030530) · [forum ufficiale Lilith, 12/12/2025](https://forum-global.lilithgame.com/post/2179486) · [forum ufficiale Lilith, 24/02/2025](https://forum-global.lilithgame.com/post/1935973) · [riseofkingdomsguides, 02/01/2026](https://riseofkingdomsguides.com/rise-of-kingdoms-barbarians-and-barbarian-forts/) · [wiki fandom, 07/11/2024](https://riseofkingdoms.fandom.com/wiki/Barbarians) · [heaven-guardian, 03/08/2026](https://heaven-guardian.com/rise-of-kingdoms-dominate-barbarians-forts-guide/) · [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2161435) · [forum ufficiale Lilith, 30/04/2026](https://forum-global.lilithgame.com/post/2232581)

### March / preset di marcia

**Percorso:** Dal bersaglio (es. barbaro o nodo) -> schermata di creazione marcia; preset salvati.

**Elementi stabili / cosa si vede:**
- I preset di marcia esistono: la schermata di creazione marcia mostra la capacità finale; un preset salvato può contenere numeri vecchi ('Edit and resave the march') (heaven-guardian).
- Nel 2023 i giocatori chiedevano più 'preset panels' con 7 marce; gli sviluppatori hanno risposto che valuteranno l'ottimizzazione.
- Impostazione 'march queue shortcut (quick march using commander avatar)' nelle General Settings.
- Numero di marce (dispatch queue): 1 (CH1), 2 (CH5), 3 (CH11), 4 (CH17), 5 (CH22).

**Insidie:**
- Numero di pannelli preset e posizione dei pulsanti non documentati: da mappare domani senza inviare marce (test T13).
- Un preset già in marcia non è riutilizzabile finche' non rientra.

*Fonti:* [heaven-guardian, 06/08/2026](https://heaven-guardian.com/rise-of-kingdoms-troop-capacity-march-queue-guide/) · [forum ufficiale Lilith, 28/04/2023](https://forum-global.lilithgame.com/post/1466061) · [BlueStacks, 23/05/2023](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-developer-feedback-march-april-2023-en.html) · [wiki fandom, 02/12/2025](https://riseofkingdoms.fandom.com/wiki/Governor_Profile) · [wiki fandom, 15/09/2024](https://riseofkingdoms.fandom.com/wiki/Troop_Dispatch_Queue)

### Rally

**Percorso:** Bersaglio (es. Barbarian Fort) -> Rally; gli altri si uniscono dall'interfaccia d'alleanza.

**Elementi stabili / cosa si vede:**
- Il capo rally lo avvia, gli altri si uniscono entro una finestra di preparazione; valgono comandanti e talenti del capo (handbook).
- I forti sono solo in rally (handbook).
- Si può richiamare un'armata prima che arrivi alla città del capo rally toccando l'armata in marcia (wiki FAQ).

**Insidie:**
- Rally e attacchi contro giocatori richiedono SEMPRE conferma dell'utente (gate dell'advisor).
- Posizione dei pulsanti Rally/Join e opzioni del tempo di preparazione non documentate.

*Fonti:* [handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-game-mechanics-hub) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-barbarian-forts-guide) · [wiki fandom, 25/06/2026](https://riseofkingdoms.fandom.com/wiki/Frequently_Asked_Questions)

### State Forum: formazioni e armamenti (Travel, Dispatch, Recycle, Transmute)

**Percorso:** Città -> State Forum -> Travel / Dispatch; gestione armamenti nella sezione Armament/Formation del comandante (percorso esatto da verificare, vedi OFFICINA_ARMAMENTI.md).

**Elementi stabili / cosa si vede:**
- Travel: 20 AP a viaggio, 'Travel x10' = 200 AP (pulsante aggiunto in 1.0.91); animazioni saltabili (1.0.67).
- Dispatch dal livello 10 dello State Forum, 30-150 AP secondo la rarità; pulsante 'Quick Dispatch' (1.0.91); scelta di 3 formazioni preferite.
- Inventario armamenti: icone con le formazioni applicabili, blocco dall'inventario (1.0.66), ordinamento per data (1.0.67).

**Insidie:**
- TRAVEL CON GEMME: dalla 1.0.66, esauriti gli AP, i viaggi si possono pagare in gemme (fino a 200 viaggi extra al giorno) -> il bot deve fermarsi quando il pulsante Travel mostra l'icona gemma.
- Recycle richiede la password secondaria (1.0.66); Transmute richiede verifica secondaria (1.0.77); inscribing e converting richiedono la password secondaria (1.1.08): il bot non deve conoscere la password -> queste operazioni restano manuali.
- Transmutation/Conversion consumano materiali rari -> gate dell'advisor.

*Fonti:* [touchscreengaming, 10/10/2025](https://touchscreengaming.com/formations-guide/) · [forum ufficiale Lilith, 24/02/2025](https://forum-global.lilithgame.com/post/1935973) · [BlueStacks, 20/02/2023](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-gunning-for-the-top-en.html) · [forum ufficiale Lilith, 10/02/2023](https://forum-global.lilithgame.com/post/1433064) · [BlueStacks, 29/03/2023](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-spring-once-more-en.html) · [forum ufficiale Lilith, 06/12/2023](https://forum-global.lilithgame.com/post/1599092) · [forum ufficiale Lilith, 27/05/2026](https://forum-global.lilithgame.com/post/2246725) · [handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-formations-armaments-inscriptions-guide)

### Mail (posta)

**Percorso:** non documentato dalle fonti lette → da misurare domani.

**Elementi stabili / cosa si vede:**
- Scouting Report aggiornato con 'NEW!'; ricompense dei codici e compensazioni dopo manutenzione arrivano per posta.

**Insidie:**
- Pulsante e schede della posta non documentati; la posta può contenere link a eventi/negozi.

*Fonti:* [wiki fandom, 03/06/2025](https://riseofkingdoms.fandom.com/wiki/Scouting) · [heaven-guardian, 18/09/2026](https://heaven-guardian.com/rise-of-kingdoms-codes/) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-server-status-and-fixes)

### Popup e stati bloccanti (da riconoscere prima di ogni azione)

**Percorso:** non documentato dalle fonti lette → da misurare domani.

**Elementi stabili / cosa si vede:**
- Finestra di verifica: gli sviluppatori parlano di una '1-minute verification window' che compare durante le grandi battaglie, dovuta a 'prevalent usage of plug-ins'; il sistema di 'verification code' riduce le richieste per chi ha un buon 'conduct score' (1.0.60).
- Richiesta di password secondaria (se impostata) su operazioni sensibili.
- Dialoghi di conferma: attacco/scouting di governatori del proprio campo (1.0.76, disattivabile), ritiro dal presidio da capitano ('Don't ask again today', 1.0.78), cambio equipaggiamento (1.0.92), riconferma donazioni Flux (1.1.04).
- Disconnessione: un solo login attivo per account; entrare da PC scollega il telefono (handbook).
- Manutenzione/aggiornamento obbligatorio: il client si ferma al caricamento (handbook).

**Insidie:**
- FINESTRA DI VERIFICA -> il bot si FERMA, salva lo screenshot e avvisa il proprietario: non deve tentare di risolverla (ToS 17.1.6 vieta di aggirare misure tecniche).
- Offerte a pagamento e negozi: riconoscere i prezzi in valuta reale e l'icona gemma e chiudere solo con la X/indietro verificati.
- Tutorial guidati di nuove funzioni: esistono (es. tutorial interattivo di Ark of Osiris, 1.0.98); se un tutorial blocca l'interfaccia il bot si ferma e chiede aiuto.
- 'Rapid Retreat' in modalità automatica (Lost Kingdom, 1.0.99): il ritorno istantaneo delle truppe costa 80 gemme -> verificare che la modalità automatica sia spenta se presente.

*Fonti:* [forum ufficiale Lilith, 24/03/2023](https://forum-global.lilithgame.com/post/1450660) · [forum ufficiale Lilith, 29/07/2022](https://forum-global.lilithgame.com/post/1359527) · [forum ufficiale Lilith, 10/01/2022](https://forum-global.lilithgame.com/post/1197916) · [forum ufficiale Lilith, 20/01/2021](https://forum-global.lilithgame.com/post/1041743) · [forum ufficiale Lilith, 07/11/2023](https://forum-global.lilithgame.com/post/1589003) · [forum ufficiale Lilith, 09/01/2024](https://forum-global.lilithgame.com/post/1612606) · [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/1963188) · [forum ufficiale Lilith, 26/02/2026](https://forum-global.lilithgame.com/post/2213663) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-how-to-play-on-pc) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-server-status-and-fixes) · [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2124406) · [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2102690) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-shop-and-bundles-guide) · [Lilith ToS, 15/04/2025 (campo show_at della pagina)](https://www.lilith.com/termofservice/?locale=en_US)

---

## 2. ADB: comandi e setup

Pagina ufficiale adb aggiornata il 2026-09-25: documenta screencap/exec-out, am start/force-stop, am display-size/display-density, pm list packages, adb devices, Wi-Fi (adb pair, adb tcpip/connect, adb Wi-Fi 2.0 su Android 17). NON documenta 'input', 'wm size/density', 'svc power stayon', 'dumpsys window/activity' con i campi mCurrentFocus/mResumedActivity: per questi la stessa pagina dice che 'Help is available for most of the commands via the --help argument' -> la sintassi va verificata sul telefono (test T02) prima dell'uso. ([Android Developers, 25/09/2026](https://developer.android.com/tools/adb))

### 2.1 Autorizzazione USB e Wi-Fi
- Attivare le Developer options: Settings > About phone > Build number, toccare Build number sette volte fino al messaggio 'You are now a developer!' (il percorso varia per produttore).
- Attivare USB debugging: Android 9+ Settings > System > Advanced > Developer Options > USB debugging (percorso ufficiale Pixel; su altri telefoni può variare).
- Collegare il cavo: Android 4.2.2+ mostra un dialogo che chiede di accettare la chiave RSA del computer; senza sbloccare il telefono e confermare, i comandi adb non funzionano.
- Verificare con 'adb devices -l': lo stato deve essere 'device'. Altri stati documentati: 'offline' (non connesso o non risponde) e 'no device'.
- Lo stato 'unauthorized' non è descritto nella pagina letta; è il caso in cui il dialogo RSA non è stato accettato (da verificare: se compare, sbloccare il telefono e accettare).
- Dalla pagina adb: 'Revoke adb debugging authorizations' nelle impostazioni del telefono dissocia questa e tutte le altre workstation associate.
- Con più dispositivi usare 'adb -s <serial> ...' oppure la variabile ANDROID_SERIAL; senza, adb dà errore 'more than one device/emulator'.

*Fonti:* [Android Developers, 25/09/2026](https://developer.android.com/tools/adb) · [Android Developers, 16/09/2026](https://developer.android.com/studio/debug/dev-options)

> "When you connect a device running Android 4.2.2 (API level 17) or higher, the system shows a dialog asking whether to accept an RSA key that allows debugging through this computer. This security mechanism protects user devices because it ensures that USB debugging and other adb commands cannot be executed unless you're able to unlock the device and acknowledge the dialog."

**Wi-Fi.** Developer options > Wireless debugging > 'Pair using pairing code' (annotare IP, porta e codice) -> sul PC: 'adb pair ipaddr:port' e inserire il codice; poi 'adb devices' per verificare. L'associazione si fa una volta sola; si revoca con 'Forget' o 'Revoke adb debugging authorizations'. Con Android 17 e adb 37.0.0 (ADB Wi-Fi 2.0) il telefono si ricollega automaticamente al PC sulle reti Wi-Fi marcate come fidate ('always allow on this network'). Diagnostica: 'adb server-status' (version >= 37.0.0, mdns_enabled: true) e 'adb mdns track-services --proto-text'.
Metodo classico (Android 10 e precedenti, o con cavo iniziale): `adb tcpip 5555   (con cavo collegato)` → `scollegare il cavo` → `adb connect <ip_telefono>:5555` → `adb devices   -> '<ip>:5555 device'` → `se cade: rifare 'adb connect'; se non basta 'adb kill-server' e ripartire`. Per il bot il cavo USB resta preferibile: alimenta il telefono (serve per 'Stay awake') ed evita cadute di rete. Il Wi-Fi è utile solo se il cavo dà problemi. ([Android Developers, 25/09/2026](https://developer.android.com/tools/adb))

### 2.2 Comandi

| Scopo | Comando | Documentato? | Note | Fonte |
|---|---|---|---|---|
| Screenshot direttamente sul PC (PNG, senza file sul telefono) | `adb exec-out screencap -p > screen.png` | sì | La doc: "use 'exec-out' instead of 'shell' to get raw data". In Python: subprocess.run(['adb','exec-out','screencap','-p'], capture_output=True).stdout -> bytes PNG -> cv2.imdecode. | [Android Developers, 25/09/2026](https://developer.android.com/tools/adb) |
| Screenshot su file nel telefono + pull | `adb shell screencap /sdcard/screen.png && adb pull /sdcard/screen.png` | sì |  | [Android Developers, 25/09/2026](https://developer.android.com/tools/adb) |
| Registrazione video dello schermo (utile per il debug dei test) | `adb shell screenrecord /sdcard/demo.mp4` | sì |  | [Android Developers, 25/09/2026](https://developer.android.com/tools/adb) |
| Tap / swipe / tasti / testo | `adb shell input tap X Y \| adb shell input swipe X1 Y1 X2 Y2 [durata_ms] \| adb shell input keyevent <KEYCODE> \| adb shell input text <testo>` | no → verificare con `adb shell input   (senza argomenti stampa l'help con la sintassi supportata da quella versione di Android)` | La pagina ufficiale adb non documenta 'input'. La sintassi indicata è quella d'uso comune e va confermata con l'help del telefono (test T02). Le coordinate sono in pixel dello schermo fisico nell'orientamento corrente (da verificare confrontando con lo screenshot e con l'opzione sviluppatore 'Pointer location'). | [Android Developers, 25/09/2026](https://developer.android.com/tools/adb) |
| Codici tasto utili (per 'input keyevent') | — | sì | KEYCODE_BACK=4, KEYCODE_HOME=3, KEYCODE_POWER=26, KEYCODE_MENU=82, KEYCODE_APP_SWITCH=187, KEYCODE_SLEEP=223, KEYCODE_WAKEUP=224. Usare KEYCODE_WAKEUP (224) e non POWER (26): POWER spegne lo schermo se è già acceso. KEYCODE_HOME 'is handled by the framework and is never delivered to applications'. L'effetto di BACK dentro il gioco non è documentato: va osservato nel test T10 (chiude la finestra? apre un dialogo di uscita?). | [Android Developers, 03/08/2026](https://developer.android.com/reference/android/view/KeyEvent) |
| Risoluzione e densità dello schermo (lettura) | `adb shell wm size ; adb shell wm density` | no → verificare con `adb shell wm   (help)` |  Alternativa documentata: Le dimensioni reali da usare per le coordinate sono quelle dello screenshot (larghezza x altezza del PNG di screencap): metodo documentato e indipendente da 'wm'. **Attenzione:** NON usare 'am display-size' / 'am display-density' (documentati) né 'wm size WxH': SOVRASCRIVONO risoluzione/densità del telefono. Per annullare: 'am display-size reset'. | [Android Developers, 25/09/2026](https://developer.android.com/tools/adb) |
| Schermo sempre acceso mentre è in carica | `adb shell svc power stayon usb` | no → verificare con `adb shell svc power   (help)` | Per i test di domani basta attivare 'Stay awake' a mano nelle Developer options (reversibile). Annotare il valore precedente per ripristinarlo. Alternativa documentata: Opzione sviluppatore 'Stay awake' ('Sets your screen to stay on while the device is plugged in'); impostazione di sistema Settings.Global.STAY_ON_WHILE_PLUGGED_IN ('stay_on_while_plugged_in'): 0 = mai, BATTERY_PLUGGED_AC = 1, BATTERY_PLUGGED_USB = 2, BATTERY_PLUGGED_WIRELESS = 4, BATTERY_PLUGGED_DOCK = 8, combinabili in OR (es. 3 = AC+USB). | [Android Developers, 16/09/2026](https://developer.android.com/studio/debug/dev-options) · [Android Developers, 03/08/2026](https://developer.android.com/reference/android/provider/Settings.Global) · [Android Developers, 03/08/2026](https://developer.android.com/reference/android/os/BatteryManager) |
| Risvegliare lo schermo | `adb shell input keyevent KEYCODE_WAKEUP   (oppure 224)` | parziale (codice documentato; comando input da verificare) | Se il telefono ha un blocco schermo con PIN/impronta, adb non può e non deve aggirarlo: per il bot tenere il telefono sbloccato e in carica con 'Stay awake', oppure sbloccarlo a mano. Il bot deve controllare che lo schermo sia acceso prima di ogni screenshot (screenshot nero = schermo spento o app protetta). | [Android Developers, 03/08/2026](https://developer.android.com/reference/android/view/KeyEvent) |
| App in primo piano | `adb shell dumpsys window \| grep mCurrentFocus ; adb shell dumpsys activity activities \| grep -E 'mResumedActivity\|topResumedActivity'` | no → verificare con `adb shell dumpsys window -h ; adb shell dumpsys activity -h` | La pagina ufficiale dumpsys documenta la sintassi generale ('adb shell dumpsys [-t timeout] [--help \| -l \| --skip services \| service [arguments] \| -c \| -h]', 'dumpsys -l' per l'elenco servizi) ma non i campi mCurrentFocus / mResumedActivity: il parser deve cercare il nome del package (com.lilithgame.roc.gp) nella riga, non una posizione fissa, e tollerare formati diversi. Se nessuno dei due campi è presente, usare come ripiego il riconoscimento dello screenshot. | [Android Developers, 23/07/2026](https://developer.android.com/tools/dumpsys) |
| Trovare il package installato | `adb shell pm list packages lilith` | sì | Da eseguire al primo test: conferma il package reale sul telefono (Google Play: com.lilithgame.roc.gp). | [Android Developers, 25/09/2026](https://developer.android.com/tools/adb) |
| Avviare il gioco | `adb shell monkey -p com.lilithgame.roc.gp -c android.intent.category.LAUNCHER 1` | sì | La doc ufficiale di Monkey: '-p <allowed-package-name>' limita il Monkey a quel package; '-c <main-category>' limita alle activity di quella categoria (default LAUNCHER o MONKEY); l'ultimo numero è <event-count>. Uso comune (non scritto nella doc): con event-count 1 il Monkey apre l'activity di avvio del package; verificare nel test T14 che non generi altri tocchi, altrimenti usare 'am start'. Alternativa: `adb shell am start -W -n <package>/<activity>   (da preferire quando l'activity è nota: è deterministico; -W attende la fine del lancio; il nome dell'activity va letto da dumpsys dopo un avvio manuale; NON usare -S che fa force-stop)` | [Android Developers, 12/04/2023](https://developer.android.com/studio/test/other-testing-tools/monkey) · [Android Developers, 25/09/2026](https://developer.android.com/tools/adb) |
| Chiudere il gioco (solo in caso di blocco) | `adb shell am force-stop com.lilithgame.roc.gp` | sì | Da usare solo come recupero dopo timeout ripetuti; tra un force-stop e il successivo lasciare un intervallo lungo. | [Android Developers, 25/09/2026](https://developer.android.com/tools/adb) |
| Debug delle coordinate | `Developer options > 'Show taps' e 'Pointer location'` | sì | Utile domani per misurare a mano le coordinate dei pulsanti; disattivarlo prima degli screenshot per il template matching (la barra in alto copre la UI). | [Android Developers, 16/09/2026](https://developer.android.com/studio/debug/dev-options) |

### 2.3 Package del gioco e aggiornamenti
- **Google Play:** `com.lilithgame.roc.gp`, titolo in store "Rise of Kingdoms: Lost Crusade", sviluppatore LilithGames, aggiornato il 17/09/2026, 50M+ download, uscito il 24/05/2018, classificazione: Everyone 10+ (classificazione mostrata sulla scheda USA: Fantasy Violence; Users Interact, In-Game Purchases (Includes Random Items)), acquisti in-app $0.29 - $499.99 per item, supporto rok-service@lilith.com ([Google Play, 17/09/2026](https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=en&gl=US) · [sito ufficiale RoK, 2025 (footer '© 2025')](https://rok.lilith.com/)).
- **App Store (iOS/Mac):** id1354260888, venditore LilithGame Co., Ltd, ultima versione 1.1.12.20 (2026-09-22); lingue: English, Arabic, French, German, Indonesian, Italian, Japanese, Kanuri, Korean, Malay, Polish, Portuguese, Russian, Simplified Chinese, Spanish, Thai, Traditional Chinese, Turkish, Vietnamese ([App Store, 22/09/2026 (versione 1.1.12.20)](https://apps.apple.com/us/app/rise-of-kingdoms/id1354260888)).
- **Huawei AppGallery:** id C100816261, package non verificato ([sito ufficiale RoK, 2025 (footer '© 2025')](https://rok.lilith.com/)).
- **Client PC ufficiale:** com.lilithgames.rok.pc.int (identificativo nel link di download Windows, non è un package Android) ([sito ufficiale RoK, 2025 (footer '© 2025')](https://rok.lilith.com/)).
- Altri store o la versione cinese: nessuna fonte trovata. Il bot non deve fidarsi di un nome fisso: al primo avvio esegue 'pm list packages lilith' e salva il package trovato.

**Frequenza degli aggiornamenti.** Versioni iOS 2026: 1.1.3.18 (20 gen), 1.1.3.22 (9 feb), 1.1.4.21 (27 feb), 1.1.5.22 (9 mar), 1.1.6.18 (24 mar), 1.1.6.33 (10 apr), 1.1.7.26 (13 mag), 1.1.8.22 (3 giu), 1.1.8.26 (11 giu), 1.1.9.19 (30 giu), 1.1.10.21 (30 lug), 1.1.11.25 (27 ago), 1.1.11.28 (2 set), 1.1.12.20 (22 set). Google Play: 'Updated on Sep 17, 2026'. Quindi un aggiornamento ogni 1-5 settimane: i template grafici vanno ri-validati dopo ogni aggiornamento. Note di rilascio 1.1.12: 'Devices that have medium graphics recommendations will show remastered troop models by default after the version update. You may change these settings under Unit Visuals.' -> gli aggiornamenti possono cambiare la grafica anche senza intervento dell'utente. ([App Store, 22/09/2026 (versione 1.1.12.20)](https://apps.apple.com/us/app/rise-of-kingdoms/id1354260888) · [Google Play, 17/09/2026](https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=en&gl=US))

**Wrapper robusto (proposta):**
- Ogni comando adb con timeout (es. 10-20 s) e controllo del codice di uscita; se 'adb devices' non mostra 'device', fermarsi e avvisare.
- Prima di ogni ciclo: schermo acceso? package in primo piano? se no -> recupero (wake, avvio app, attesa caricamento).
- Un solo client adb alla volta sul telefono; con più dispositivi sempre '-s <serial>'.

---

## 3. Riconoscimento: OCR e template matching

### 3.1 OCR con Tesseract
- **Motore:** Tesseract (ultima release nelle note ufficiali: V5.5.3, 24 luglio 2026) via pytesseract 0.3.13 (2024-08-16). ([doc Tesseract, 24/07/2026 (ultima release elencata: V5.5.3)](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ReleaseNotes.md) · [PyPI, 16/08/2024 (versione 0.3.13)](https://pypi.org/project/pytesseract/))
- **Lingue:** '-l LANG' con codice di tre lettere; più lingue insieme con '-l LANG[+LANG]' (es. -l ita+eng); se non indicata si usa l'inglese. L'ordine delle lingue cambia tempi e risultato. 'ita' (Italian) è tra le lingue con dati addestrati. Con il client in inglese usare 'eng' per i testi e la whitelist di cifre per i numeri; 'ita+eng' solo se il client è in italiano. ([doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/Command-Line-Usage.md) · [doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/Data-Files.md))
- **Modelli:** tessdata_fast: modelli interi più veloci (quelli nelle distribuzioni Linux); tessdata_best: più lenti e un po' più accurati; con questi due set solo motore LSTM (--oem 1). ([doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/Data-Files.md))
- Testo scuro su fondo chiaro: dalla 4.x Tesseract vuole 'dark text on light background' -> invertire i testi chiari del gioco (cv2.bitwise_not) dopo la conversione in grigio. ([doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ImproveQuality.md))
- Ingrandire: Tesseract lavora meglio con testo a >= 300 DPI -> per il testo piccolo dello schermo ingrandire il ritaglio 2-4x (cv2.INTER_CUBIC o INTER_LINEAR per ingrandire, INTER_AREA per rimpicciolire). ([doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ImproveQuality.md) · [doc OpenCV, s.d.](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.markdown))
- Binarizzazione: Tesseract usa Otsu internamente ma può sbagliare con sfondi non uniformi -> provare cv2.threshold con Otsu o cv2.adaptiveThreshold sul ritaglio. ([doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ImproveQuality.md) · [doc OpenCV, s.d.](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.markdown))
- Bordi: ritagliare solo l'area del numero lasciando ~10 px di bordo; troppo bordo o nessun bordo peggiorano il risultato. ([doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ImproveQuality.md))
- Canale alpha: Tesseract lo elimina fondendolo con il bianco -> passare immagini RGB/grigio. pytesseract assume RGB, OpenCV usa BGR: convertire con cv2.cvtColor(img, cv2.COLOR_BGR2RGB). ([doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ImproveQuality.md) · [PyPI, 16/08/2024 (versione 0.3.13)](https://pypi.org/project/pytesseract/))
- **Segmentazione:** --psm 7 = una riga di testo; --psm 8 = una parola; --psm 6 = blocco uniforme; --psm 13 = riga grezza; default 3 (pagina intera, sbagliato per piccoli ritagli). Per un numero singolo (risorse, truppe, potenza) usare --psm 7 (o 8); per righe tipo 'Lv. 25' --psm 7. ([doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ImproveQuality.md))
- **Whitelist e dizionari:** tessedit_char_whitelist limita i caratteri (supportato nel motore LSTM dalla 4.1.0, luglio 2019); si possono disattivare i dizionari con load_system_dawg=false e load_freq_dawg=false; user-words/user-patterns funzionano con LSTM dalla 4.1.0. Esempio: `--oem 1 --psm 7 -c tessedit_char_whitelist=0123456789.,KMB` ([doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ImproveQuality.md) · [doc Tesseract, 24/07/2026 (ultima release elencata: V5.5.3)](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ReleaseNotes.md) · [doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/tess3/FAQ-Old.md))
- **pytesseract:** image_to_string(image, lang=..., config=..., timeout=...) per il testo; image_to_data(..., output_type=Output.DICT) per box e confidenze; timeout in secondi con RuntimeError alla scadenza; get_languages() per le lingue installate; tesseract_cmd per il percorso dell'eseguibile (es. su Windows). ([PyPI, 16/08/2024 (versione 0.3.13)](https://pypi.org/project/pytesseract/))

**Numeri con separatori delle migliaia e abbreviazioni K/M:**
- Il formato dei numeri nel client (separatore delle migliaia ',' o '.', abbreviazioni K/M/B, decimali) NON è documentato dalle fonti: va osservato sugli screenshot di domani (test T04) e fissato nel parser.
- Parser proposto: togliere spazi; se il testo termina con K/M/B -> numero decimale (accettare sia '.' sia ',' come separatore decimale) x 1e3/1e6/1e9; altrimenti togliere tutti i separatori e convertire a intero.
- Regex di validazione: ^\d{1,3}([.,]\d{3})*$ (numero intero con migliaia) oppure ^\d+([.,]\d+)?[KMB]$ (abbreviato).
- Correzioni tipiche da whitelist: 'O'->'0', 'l'/'I'->'1', 'S'->'5' SOLO se la whitelist non basta; loggare sempre il testo grezzo.
- Un valore abbreviato (es. 1.2M) è approssimato: per decisioni che richiedono il numero esatto aprire la finestra di dettaglio (se esiste) o trattarlo come intervallo.
- Rileggere 2 volte (due screenshot a distanza di ~1 s) e accettare solo se uguali; controllare la plausibilità rispetto all'ultima lettura (le risorse non cambiano di ordini di grandezza in pochi secondi); usare le confidenze di image_to_data e scartare letture sotto soglia (soglia da calibrare).

### 3.2 Template matching con OpenCV
- cv.matchTemplate fa scorrere il template sull'immagine e restituisce una mappa di somiglianza di dimensione (W-w+1, H-h+1); cv.minMaxLoc dà il punto migliore (per TM_SQDIFF/TM_SQDIFF_NORMED il migliore è il MINIMO). Metodi: TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED; nel tutorial TM_CCORR dà risultati scarsi.
- Per più occorrenze: res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED); threshold = 0.8; loc = np.where(res >= threshold) (esempio ufficiale).
- Solo TM_SQDIFF e TM_CCORR_NORMED accettano una maschera; la maschera deve avere le stesse dimensioni del template (utile per icone con sfondo variabile). ([doc OpenCV, s.d.](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_template_matching/py_template_matching.markdown) · [doc OpenCV, s.d.](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/tutorials/imgproc/histograms/template_matching/template_matching.markdown))

**Soglie:**
- Partire da 0.8 con TM_CCOEFF_NORMED (valore dell'esempio ufficiale) e calibrare per OGNI template con screenshot positivi e negativi presi domani: soglia = metà strada tra il punteggio minimo dei positivi e il massimo dei negativi; se la distanza è piccola il template è ambiguo (ritagliarlo meglio o usare il colore).
- Per le icone 'pericolose' (gemma, prezzo in valuta) usare una soglia PIÙ BASSA (meglio un falso allarme che una spesa) e controllare tutta la finestra, non solo il pulsante.

**Risoluzione diversa:**
- matchTemplate confronta il template alla scala originale (lo fa scorrere, non lo ridimensiona): i template vanno catturati dallo STESSO telefono alla risoluzione di lavoro.
- Se cambia risoluzione (altro telefono, 'wm size' diverso, client PC): ridimensionare i template del fattore larghezza_nuova/larghezza_riferimento (cv.resize con INTER_AREA se si rimpicciolisce, INTER_LINEAR/INTER_CUBIC se si ingrandisce) oppure provare poche scale vicine (0.9-1.1) e tenere la migliore.
- Salvare accanto a ogni template la risoluzione dello screenshot da cui è stato preso e rifiutare il confronto se il rapporto d'aspetto è diverso.

**Buone pratiche:**
- Cercare in una ROI (regione attesa) e non su tutto lo schermo: più veloce e meno falsi positivi.
- Scala di grigi per la forma, colore (BGR) quando il colore distingue (gemme, pulsanti verdi/gialli).
- Dopo un aggiornamento del gioco (ogni 1-5 settimane nel 2026) ricontrollare tutti i template con uno screenshot di riferimento; la 1.1.12 ha cambiato di default i modelli delle truppe sui dispositivi con grafica media.
- opencv-python: installare UN solo pacchetto (opencv-python, opencv-contrib-python o le varianti -headless), non più di uno nello stesso ambiente.

*Fonti:* [doc OpenCV, s.d.](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_template_matching/py_template_matching.markdown) · [doc OpenCV, s.d.](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.markdown) · [PyPI, 02/07/2026 (versione 5.0.0.93)](https://pypi.org/project/opencv-python/) · [App Store, 22/09/2026 (versione 1.1.12.20)](https://apps.apple.com/us/app/rise-of-kingdoms/id1354260888)

### 3.3 Rendere robusto il bot
*Questa sezione contiene raccomandazioni di progettazione (non da fonte) salvo dove è citata una fonte.*

**Macchina a stati:**
- Ogni azione = (stato atteso prima) -> tocco -> attesa -> screenshot -> verifica dello stato atteso dopo. Se la verifica fallisce: nessun secondo tocco alla cieca, ma recupero.
- Stati minimi: SCHERMO_SPENTO, APP_NON_IN_PRIMO_PIANO, CARICAMENTO, CITTÀ, MAPPA, FINESTRA_NOTA(x), POPUP_SCONOSCIUTO, VERIFICA_ANTIBOT, DISCONNESSO, MANUTENZIONE.
- VERIFICA_ANTIBOT e POPUP_SCONOSCIUTO -> STOP immediato, screenshot salvato, notifica al proprietario (nessun tentativo di risolvere o chiudere a caso).

**Timeout:**
- Timeout per ogni attesa di stato (es. 5-10 s per una finestra, 60-120 s per il caricamento del gioco); massimo 2-3 tentativi per passo, poi recupero.
- Timeout sui comandi adb e su Tesseract (pytesseract accetta timeout=...).

**Ritorno alla città:**
- Procedura 'torna alla città': premere il pulsante X/indietro riconosciuto per immagine; in alternativa KEYCODE_BACK una volta per volta con verifica dopo ogni pressione (l'effetto di BACK nel gioco va osservato domani: se apre un dialogo di uscita, rispondere 'annulla' riconoscendolo per immagine).
- Quando si è in città, doppio tocco sul pulsante mappa/città per riportare la telecamera alla vista standard (BlueStacks, guida macro).
- Se dopo N tentativi non si riconosce la città: force-stop + riavvio del gioco, con un limite di riavvii all'ora; oltre il limite fermarsi.

**Sicurezza:**
- Lista nera di template (icona gemma, prezzi, 'Buy', 'Purchase', 'Refresh' con costo, 'Delete Account', 'Switch', 'Create New Character', 'Language'): se uno compare nell'area del tocco, il tocco è annullato.
- Tenere attiva 'gem use confirmation' e impostare la password secondaria che il bot NON conosce (vedi screens_common.safety_nets_in_game).
- Solo azioni del piano confermato dall'utente (gate dell'advisor); log di ogni azione con screenshot prima/dopo e testo OCR grezzo.
- Il bot non deve interagire con giocatori (chat, attacchi, scouting) senza conferma esplicita.

*Fonti:* [BlueStacks, 23/12/2024](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-bluestacks-macros-en.html) · [PyPI, 16/08/2024 (versione 0.3.13)](https://pypi.org/project/pytesseract/) · [forum ufficiale Lilith, 24/03/2023](https://forum-global.lilithgame.com/post/1450660)

---

## 4. Rischi: Termini di servizio e conseguenze

Fatti UFFICIALI: (1) ToS 17.1.15/17.1.18 vietano bot e software di terze parti; (2) Lilith ha pubblicato nel 2020 report anti-botting con account bannati (anche permanentemente) e nel gennaio 2021 dichiarava 167.000 personaggi bannati in 3 mesi per programmi di terze parti; (3) esiste un sistema di verifica in gioco (codici di verifica, finestra di verifica di 1 minuto) legato all'uso di plug-in; (4) dalla 1.1.07 (30 aprile 2026) un 'Conduct Score System' toglie punti a chi usa 'third-party tools such as scripts or cheats', con penalità sotto certe soglie (prima nei regni in Season of Conquest).

I Termini di servizio Lilith (versione inglese, data 2025-04-15 nel campo 'show_at' della pagina, collegata dal sito ufficiale rok.lilith.com) vietano esplicitamente l'uso di 'bots' e di 'third-party software' per ottenere un vantaggio o per interferire con il servizio (17.1.18) e l'accesso ai servizi 'by automated means including but not limited to, bots' (17.1.15). La sanzione prevista è la sospensione o chiusura dell'account a discrezione di Lilith (20.1), con perdita di oggetti e valuta virtuali e nessun rimborso (21.2, 21.3). Il testo non distingue tra uso privato e uso commerciale e non prevede eccezioni per l'automazione via ADB. Fonti community del 2026 riportano che gli account che usano bot vengono bannati (a livello di account) e che il rilevamento si basa su schemi di comportamento; queste affermazioni NON sono verificate da fonte ufficiale.

### 4.1 Termini di servizio Lilith (testo inglese)
Documento: *Lilith Terms of Service (versione inglese)*, pubblicato/mostrato 2025-04-15 11:00:00 (campo 'show_at' del contenuto della pagina; nessuna 'effective date' esplicita nel testo); soggetto: Lilith Technology Hong Kong Limited e affiliate (per le versioni diverse da Cina continentale, Giappone e Corea; clausola 1.1). Sì: la pagina è linkata dal sito ufficiale del gioco; le Terms coprono tutte le 'Lilith Applications' (1.2.1) e le 'Affiliate Publishers' (30.3). Il testo non nomina Rise of Kingdoms esplicitamente. Lingue disponibili: zh_CN, en, ja, ko (nessuna versione italiana). ([Lilith ToS, 15/04/2025 (campo show_at della pagina)](https://www.lilith.com/termofservice/?locale=en_US) · [sito ufficiale RoK, 2025 (footer '© 2025')](https://rok.lilith.com/) · [Google Play, 17/09/2026](https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=en&gl=US))

| Clausola | Testo (EN) | Perché conta |
|---|---|---|
| 17.1.15 | Post User content or take any action that infringes or violates the rights of another Member: Bully, harass or intimidate any Member of the Services; Solicit Member login credentials from another Member or collect User content or otherwise access the Services by automated means including but not limited to, bots, robots, spiders; | Vieta l'accesso ai servizi 'con mezzi automatici', bot inclusi. |
| 17.1.18 | Use cheats, exploits, hacks, bots, mods or third-party software designed to gain an advantage, perceived or actual, over other Members, or modify or interfere with the Service; | Divieto esplicito di bot e software di terze parti che danno un vantaggio 'percepito o reale'. Un bot ADB che gioca al posto dell'utente rientra nella lettura letterale di 'bots'. |
| 17.1.7 | Attempt to access or search our Services or Lilith Content, or download Lilith Content from our Services, through the use of any engine, software, tool, agent, device or mechanism (including spiders, robots, crawlers, data mining tools or the like) other than the software and/or search agents provided by Lilith or other generally available third-party web browsers (such as Google Chrome, Microsoft Internet Explorer, Mozilla Firefox, Apple Safari or Opera); | Accesso tramite strumenti diversi dal software fornito da Lilith. |
| 17.1.6 | Avoid, bypass, remove, deactivate, impair, descramble or otherwise circumvent any technological measure implemented by Lilith or any of Lilith's providers or any other third party (including another Lilith User) to protect our Services or Lilith Content; | Vieta l'elusione delle misure tecniche di protezione: il bot NON deve tentare di aggirare controlli anti-bot. |
| 17.1.12 | Attempt to decipher, decompile, disassemble or reverse engineer any of the software used to provide our Services or Lilith Content; Interfere with, or attempt to interfere with, the access of any user, host or network, including, without limitation, sending a virus, overloading, flooding, spamming, or mail-bombing our Services; | Il bot deve lavorare solo su screenshot e input, senza decompilare o modificare il client. |
| 17.1.19 | Abuse or exploit a bug, glitch or mechanism in the Service; or Engage in any fraudulent behavior, including but not limited to credit card scams or credit card misappropriation. | Sfruttare bug è vietato. |
| 17.1.21 | Unsportsmanlike behavior. Account sharing, including but not limited to the sharing of username and password for others to login for you. | Condivisione dell'account vietata. |
| 17.3 | You acknowledge that Lilith has no obligation to monitor or record your access to or use of our Services or Lilith Content, or to monitor, record, or edit any User Content, but agree that we have the right to do so for the purpose of operating our Services, to ensure your compliance with these Terms, or to comply with applicable law or the order or requirement of a court, administrative agency or other governmental body. | Lilith si riserva il diritto di monitorare l'uso per verificare il rispetto dei Terms. |
| 20.1 | Without limiting other remedies, Lilith may at any time suspend or terminate your Lilith Account and refuse to provide access to our Services if Lilith suspects or determines, in its own discretion, that you may have or there is a significant risk that you have: (i) failed to comply with any provision of these Terms or any policies or Rules established by Lilith; (ii) engaged in actions relating to or in the course of using our Services that may be illegal or cause liability, harm, embarrassment, harassment, abuse or disruption for you, Lilith Users, Lilith or any other third parties or our Services; or (iii) infringed the proprietary rights, rights of privacy, or Intellectual Property Rights of any person, including as a repeat infringer. | Sanzione: sospensione o chiusura dell'account anche solo su sospetto ('suspects or determines, in its own discretion'). |
| 21.1 | Upon termination of your Lilith Account for any reason by you or us, you will lose all access to such account. Terminated Lilith Accounts cannot be reinstated; any Lilith Account that may be registered by you after termination of a Lilith Account is a unique account. | Un account chiuso non viene ripristinato. |
| 21.2 | If your Lilith Account is terminated for any reason by you or us, you understand and agree that any Virtual Items to which you had access via your Lilith Account at the time of termination will be lost and no longer be available to you, and you will have no right to them. [...] | Perdita di oggetti e valuta virtuali. |
| 21.3 | YOU AGREE THAT LILITH IS NOT REQUIRED TO PROVIDE A REFUND FOR ANY REASON, AND THAT YOU WILL NOT RECEIVE MONEY OR OTHER COMPENSATION FOR UNUSED VIRTUAL ITEMS OR VIRTUAL CURRENCY IN AN INACTIVE ACCOUNT OR THAT WAS IN A TERMINATED LILITH ACCOUNT, NO MATTER HOW EITHER CAME ABOUT. [...] | Nessun rimborso. |
| 2 | Lilith reserves the right, at its sole discretion, to modify, discontinue or terminate our Services, including any portion thereof, on a global or individual basis, or to modify these Terms, at any time and without prior notice. [...] | I Terms possono cambiare senza preavviso: ricontrollare la pagina prima di ogni fase di sviluppo. |
| 26 | These Terms and any action related thereto will be governed by the laws of People's Republic of China without regard to its conflict of law's provisions. Any dispute arising from or in connection with These Terms shall be submitted to Shanghai International Economic and Trade Arbitration Commission/Shanghai International Arbitration Center ("SHIAC") for arbitration [...] | Legge applicabile: Repubblica Popolare Cinese; arbitrato SHIAC a Shanghai. |

Contatti: service@lilith.com (ToS, sez. 5 e 31); supporto del gioco indicato su Google Play: rok-service@lilith.com.

### 4.2 Dichiarazioni ufficiali su bot, plug-in e sanzioni
- **2020-09-01** — Post ufficiale 'Anti-Botting Report - 2020-08-10 ~ 2020-08-24': Lilith pubblica un elenco parziale di account 'found to be in violations of our policies on botting or third-party payments. As a result, these accounts have been banned.' ([forum ufficiale Lilith, 01/09/2020](https://forum-global.lilithgame.com/post/1000060))
- **2020-10-16** — Secondo report ufficiale (2020-08-31 ~ 2020-09-14): stessi motivi, account 'banned permanently'. ([forum ufficiale Lilith, 16/10/2020](https://forum-global.lilithgame.com/post/1003107))
- **2021-01-27** — Dev Feedback ufficiale: 'If we discover any use of third-party programs, we will ban those involved. In the past 3 months, we have banned a total of 167,000 characters. We will always continue to enhance our anti-cheating system'. ([forum ufficiale Lilith, 27/01/2021](https://forum-global.lilithgame.com/post/1044203))
- **2022-01-10 / 2022-07-29** — Esiste un sistema di verifica in gioco ('verification system' per 'eliminating idling and providing a genuine gaming environment'); con la 1.0.60 'Governors with good conduct scores can minimize the number of verification codes needed'. ([forum ufficiale Lilith, 10/01/2022](https://forum-global.lilithgame.com/post/1197916) · [forum ufficiale Lilith, 29/07/2022](https://forum-global.lilithgame.com/post/1359527))
- **2023-03-24** — Face-to-Face ufficiale: la '1-minute verification window' compare spesso nelle grandi battaglie; 'Due to the prevalent usage of plug-ins and behavior that disrupts the game's ecology, we are unable to fix this issue for large-scale battles at the moment.' ([forum ufficiale Lilith, 24/03/2023](https://forum-global.lilithgame.com/post/1450660) · [BlueStacks, 21/04/2023](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-face-to-face-developer-notes-en.html))
- **2026-04-30** — Note di rilascio ufficiali 1.1.07: 'Conduct Score System: Players who use third-party tools such as scripts or cheats will have their Conduct score deducted. When a player's Conduct score falls below certain thresholds, penalties will be applied accordingly.' '* This feature will first be available in kingdoms that have entered the Season of Conquest.' ([forum ufficiale Lilith, 30/04/2026](https://forum-global.lilithgame.com/post/2232581))

### 4.3 Cosa dice la community (non ufficiale)
- Secondo riseofkingdomshandbook.com (sito community, 2026-08-18) i bot di auto-farming 'do work' ma sono 'explicitly against the terms of service'; 'Bans are account-level, not device-level. You lose the account, the spending on it, and your standing in your alliance.'; 'Purchases are not refunded.' ([handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-mod-apk-bots-and-bans))
- Stessa fonte: il rilevamento cercherebbe schemi di comportamento ('perfectly regular action timing, 24-hour activity, identical march sequences') e le alleanze segnalano gli account sospetti. Affermazione della community, NON documentata da Lilith. ([handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-mod-apk-bots-and-bans))
- Stessa fonte: giocare su PC con il client ufficiale o con un emulatore 'mainstream' è considerato accettabile; 'The line is automation and client modification, not the device you play on.' Il client PC ufficiale si scarica da rok.lilith.com. ([handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-mod-apk-bots-and-bans) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-how-to-play-on-pc))
- Le 'mod APK' (gemme infinite) non possono funzionare perché il gioco è 'server-authoritative'; sono spesso malware che ruba le credenziali. Il bot deve usare solo il client ufficiale installato dallo store. ([handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-mod-apk-bots-and-bans))
- Una sola sessione attiva per account: 'logging in on PC signs your phone out'. Se il proprietario apre il gioco su un altro dispositivo, il telefono del bot viene disconnesso (da gestire come stato 'disconnesso', senza ri-login automatici a raffica). ([handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-how-to-play-on-pc))
- Vendita/cessione di account contraria ai ToS (clausole 12.2 sugli oggetti virtuali e 17.1.21 sulla condivisione); la community riporta ban per gli account scambiati. ([Lilith ToS, 15/04/2025 (campo show_at della pagina)](https://www.lilith.com/termofservice/?locale=en_US) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-account-buying-selling-risks))
- **BlueStacks (produttore dell'emulatore, parte interessata):** Le guide BlueStacks promuovono il Macro Recorder per automatizzare raccolta, addestramento, upgrade e barbari in Rise of Kingdoms e la sincronizzazione multi-istanza; le pagine non citano i ToS di Lilith. Non costituisce un'autorizzazione di Lilith. ([BlueStacks, 23/12/2024](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-bluestacks-macros-en.html) · [BlueStacks, 02/03/2021](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-instance-manager-en.html))
- **riseofkingdomshandbook.com (community):** 'Bots and auto-farming scripts do work, and they are against the terms of service, and accounts using them get banned.'; nella guida alle cure: 'Do not build a plan around “infinite healing” or automate taps.' ([handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-mod-apk-bots-and-bans) · [handbook, 09/09/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-healing-hospital-guide))

### 4.4 Funzioni di automazione ufficiali del gioco
Alternative ufficiali (dentro il gioco, quindi non 'third-party') a parte del lavoro del bot. Usarle riduce la quantità di input automatizzati necessari.

- **Auto-Peacekeeping:** Caccia automatica ai barbari: attacco coordinato di più truppe e assegnazione in blocco (1.1.01), evita barbari già ingaggiati da altri (1.1.04), display AP con uso rapido e livelli salvati (1.1.07); durante 'Eve of the Crusade' anche Marauders (1.1.02). ([forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2161435) · [forum ufficiale Lilith, 26/02/2026](https://forum-global.lilithgame.com/post/2213663) · [forum ufficiale Lilith, 30/04/2026](https://forum-global.lilithgame.com/post/2232581) · [forum ufficiale Lilith, 12/12/2025](https://forum-global.lilithgame.com/post/2179486))
- **Queue management:** Dal City Hall 8 (1.1.01): panoramica di costruzione, addestramento, ricerca, cure, esplorazione e donazioni d'alleanza con azioni rapide; disattivabile dalle Settings. ([forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2161435))
- **Quick Dispatch / Travel x10:** Pulsanti dello State Forum (1.0.91) per usare in un colpo le chance di Dispatch e 10 viaggi. ([forum ufficiale Lilith, 24/02/2025](https://forum-global.lilithgame.com/post/1935973))
- **Claim All (regali d'alleanza normali):** Ritiro di tutti i regali normali; non per i regali rari (2022). ([forum ufficiale Lilith, 26/10/2022](https://forum-global.lilithgame.com/post/1395812))
- **Expedition: claim di tutte le missioni a 3 stelle:** Pulsante in alto a sinistra per ritirare tutte le ricompense 3 stelle (wiki). ([wiki fandom, 11/03/2024](https://riseofkingdoms.fandom.com/wiki/Expedition))

### 4.5 Riduzione del danno (non elusione)
- Il bot NON deve: modificare l'APK o la memoria del gioco, intercettare il traffico di rete, decompilare il client (17.1.12), aggirare misure di protezione (17.1.6), spendere gemme, sfruttare bug (17.1.19).
- Rispettare sempre le conferme dell'utente per azioni che spendono risorse rare o attaccano giocatori (gate già presente in advisor.py).
- Tenere un log locale di ogni azione (screenshot prima/dopo) per poter ricostruire cosa ha fatto il bot.
- Queste misure riducono i danni collaterali ma NON rendono l'automazione conforme ai ToS: il testo 17.1.15/17.1.18 vieta i bot in quanto tali. La decisione di usare il bot resta del proprietario, che se ne assume il rischio (sospensione/chiusura account, 20.1).

---

## 5. Piano di test per domani

L'ordine va dalla sola lettura (screenshot e OCR, con la navigazione fatta a mano) alle azioni reversibili: aprire e chiudere schermate, cercare sulla mappa senza attaccare. Le righe con **safe = no** non sono per domani. È una proposta: le fonti sono quelle dei comandi e delle schermate usati.

**Da lanciare per primo:** Nel progetto esiste già military_advisor/adb_tools.py (sola lettura: adb devices, wm size/density, app in primo piano, schermo acceso, screenshot) con il comando 'python -m military_advisor phone-check --out test_telefono': copre gran parte di T01-T04 e va lanciato per primo. Proposta di test (non da fonte); le fonti indicate sono quelle dei comandi e delle schermate usate.

| # | Cosa fare | Risultato atteso | Safe |
|---|---|---|---|
| T00 Preparazione (a mano, bot spento) | Telefono in carica col cavo USB. Developer options -> USB debugging ON; 'Stay awake' ON (annotare lo stato precedente per ripristinarlo); disattivare 'Pointer location' se attivo. Nel gioco: aprire Settings e CONTROLLARE (senza cambiare altro) che 'gem use confirmation' sia attiva; decidere se impostare la password secondaria (la conosce solo il proprietario). Annotare la lingua del client (ideale: inglese per coerenza con le fonti). | Telefono sveglio e collegato; conferma gemme attiva; lingua annotata. | sì |
| T01 Connessione adb | adb devices -l | Una riga con stato 'device'. Se non compare o lo stato non è 'device': sbloccare il telefono e accettare il dialogo RSA 'Allow USB debugging?'; se ci sono più dispositivi usare sempre -s <serial>. | sì |
| T02 Help dei comandi non documentati (sola lettura) | adb shell input ; adb shell wm ; adb shell svc power ; adb shell dumpsys -l > servizi.txt ; salvare tutto l'output in un file di log *Nota:* Se un comando senza argomenti non stampa l'help, riprovare con --help o -h; NON lanciare 'wm size WxH' né 'am display-size' (cambiano la risoluzione). | Sintassi reale di input (tap/swipe/keyevent/text), wm (size/density) e svc power (stayon) su QUESTO telefono; elenco servizi dumpsys con 'window' e 'activity'. Nessun evento inviato allo schermo. | sì |
| T03 Package e app in primo piano (gioco aperto a mano) | adb shell pm list packages lilith ; adb shell dumpsys window \| grep mCurrentFocus ; adb shell dumpsys activity activities \| grep -E 'mResumedActivity\|topResumedActivity' | Compare 'package:com.lilithgame.roc.gp' (o il package reale da salvare); le righe di dumpsys contengono il package e il nome dell'activity (salvarlo per 'am start -n'). | sì |
| T04 Screenshot e risoluzione | Con la città a schermo: adb exec-out screencap -p > t04_city.png (ripetere 5 volte misurando il tempo); confrontare larghezza x altezza del PNG con 'adb shell wm size'. | PNG validi (non neri) con la risoluzione del telefono; tempo medio per screenshot annotato (serve per i timeout). | sì |
| T05 OCR della barra risorse (nessun tocco) | Sul PC: ritagliare le aree di cibo, legno, pietra, oro, gemme da t04_city.png; pytesseract --oem 1 --psm 7 con whitelist 0123456789.,KMB; confrontare con i valori letti a occhio. | Formato numerico del client annotato (separatori, K/M/B); 5/5 valori letti correttamente dopo il pre-processing (grigio, inversione, ingrandimento 3x, soglia). | sì |
| T06 Profilo e truppe (navigazione A MANO, bot solo screenshot) | Aprire a mano avatar -> Governor Profile; screenshot; poi sezione Troops (Total / In the City / On the Map); screenshot; OCR di potenza, AP, truppe. | Valori OCR uguali a quelli a schermo; posizione di avatar e sezioni annotata (coordinate lette con 'Pointer location' prima di disattivarlo). | sì |
| T07 Comandanti (a mano, sola lettura) | Aprire a mano la lista Commanders (annotare dove si trova il pulsante), poi un comandante e le sue schede (Skills, Talents, Equipment, Formation); screenshot di ogni schermata; OCR nome/livello/stelle. | Percorso e posizione dei pulsanti documentati con screenshot; nessun potenziamento premuto. | sì |
| T08 Settings (a mano, sola lettura) | Aprire Settings: screenshot della versione e dell'ora UTC; screenshot delle sottosezioni SENZA entrare in Account, Character Management, Language o 'Other'. | Versione del client annotata (serve a capire quando rifare i template). | sì |
| T09 Cattura e calibrazione dei template (solo PC) | Dagli screenshot ritagliare: avatar, pulsante mappa/città, icona Events, X di chiusura, icona gemma, pulsante Search (e variante 'Return to City'), mano dell'Alliance Help, icona del Mysterious Merchant. Salvare con la risoluzione. Calcolare i punteggi TM_CCOEFF_NORMED su screenshot positivi e negativi. | Per ogni template: punteggio minimo dei positivi > massimo dei negativi; soglia scelta e salvata; icona gemma rilevata in tutti gli screenshot dove c'e'. | sì |
| T10 Primi tocchi automatici: apri/chiudi profilo | Bot: verifica stato CITTÀ -> tap sull'avatar (coordinate dal template) -> attende -> verifica PROFILO -> chiude con X (template) -> verifica CITTÀ. Poi ripetere chiudendo con 'input keyevent KEYCODE_BACK' per osservare l'effetto di BACK. | Ogni passaggio verificato da screenshot; effetto di BACK annotato (chiude la finestra? apre un dialogo di uscita?). | sì |
| T11 Apri/chiudi schermate di menu | Bot, una alla volta con verifica: Commanders (lista, un dettaglio, cambio scheda), Items (cambio scheda), Alliance (senza premere Help/Donate/Claim), Events, Campaign -> Expedition (senza avviare missioni), Mail. Dopo ognuna: procedura return_home. | Tutte le schermate aperte e chiuse con verifica; tempi di attesa annotati; nessun pulsante con gemma/prezzo toccato (lista nera attiva). | sì |
| T12 Apri/chiudi edifici | Bot: doppio tocco mappa/città per la telecamera standard; poi Barracks, Stable, Archery Range, Siege Workshop (aprire la schermata di addestramento SENZA premere Train/Upgrade), Hospital (senza Heal), Tavern (leggere i contatori, senza Open), Courier Station (senza Buy/Refresh), Scout Camp (senza Explore), State Forum (leggere Travel/Dispatch rimasti, senza Travel). | Screenshot di ogni schermata; posizione di quantità/Train/Upgrade/Heal annotata per il futuro; zero risorse spese (confrontare la barra risorse prima/dopo con OCR). | sì |
| T13 Mappa e ricerca (nessun attacco) | Bot: passa alla mappa -> apre Search -> sceglie barbari di un livello -> preme la ricerca (la camera si sposta sul bersaglio) -> NON attacca -> torna in città. Ripetere per un punto risorsa e per i Barbarian Forts. Poi, A MANO (non il bot): toccare il barbaro -> Attack per vedere la schermata di creazione marcia e i pannelli preset, screenshot, chiudere con X SENZA premere il pulsante di invio. | La camera si centra sul bersaglio; schermata marcia e preset documentati con screenshot; nessuna marcia partita (controllare con la sezione Troops o il contatore marce); ritorno in città riuscito. | sì |
| T14 Recupero | Da una finestra aperta: return_home con X/BACK; dalla mappa: ritorno in città. Solo se nessuna marcia/azione è in corso: 'adb shell am force-stop com.lilithgame.roc.gp' seguito da avvio con 'adb shell am start -W -n <package>/<activity>' (activity ricavata in T03; deterministico) e, come prova separata, con 'adb shell monkey -p com.lilithgame.roc.gp -c android.intent.category.LAUNCHER 1'; attendere il caricamento. | Il bot riconosce CARICAMENTO -> CITTÀ; tempo di caricamento annotato; nessun tocco casuale del Monkey (se succede, usare solo 'am start -W -n'). | sì |
| T15 Schermo spento e risveglio | Spegnere lo schermo a mano; adb shell input keyevent KEYCODE_WAKEUP (224); screenshot. | Schermo acceso. Se compare la schermata di blocco con PIN/impronta il bot si ferma e avvisa (non deve aggirarla). | sì |
| T16 Rilevamento popup | Durante tutti i test salvare gli screenshot 'sconosciuti' (nessun template riconosciuto) in una cartella; alla fine classificarli a mano (offerte, eventi, tutorial, conferme, verifica). | Primo catalogo di popup reali con i relativi template 'chiudi' e 'pericolo'. | sì |
| T17 (NON domani) Azioni gratuite ma non reversibili | Alliance Help agli altri, ritiro regali/ricompense gratuite (Claim All), Explore degli scout, ritiro del forziere giornaliero di Expedition, aperture gratuite della Tavern. | Da fare solo dopo che T00-T16 sono stabili e con l'OK esplicito del proprietario, una funzione alla volta. | **no** |
| T18 (NON domani) Azioni che spendono | Addestramento/upgrade truppe (risorse), cure (risorse), Travel/Dispatch (AP; oltre gli AP il Travel costa gemme), acquisti con cibo/legno al Courier, uso di oggetti, invio di marce e attacchi. *Nota:* Promemoria: l'automazione resta contraria ai ToS (17.1.15/17.1.18) indipendentemente da queste precauzioni. | Solo con piano confermato dall'advisor (gate) e con la lista nera gemme attiva; MAI gemme; attacchi a giocatori sempre con conferma. | **no** |

Fonti usate dal piano: [Android Developers, 16/09/2026](https://developer.android.com/studio/debug/dev-options) · [wiki fandom, 02/12/2025](https://riseofkingdoms.fandom.com/wiki/Governor_Profile) · [forum ufficiale Lilith, 20/01/2021](https://forum-global.lilithgame.com/post/1041743) · [Android Developers, 25/09/2026](https://developer.android.com/tools/adb) · [Android Developers, 23/07/2026](https://developer.android.com/tools/dumpsys) · [Google Play, 17/09/2026](https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=en&gl=US) · [doc Tesseract, s.d.](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ImproveQuality.md) · [PyPI, 16/08/2024 (versione 0.3.13)](https://pypi.org/project/pytesseract/) · [wiki fandom, 16/07/2023](https://riseofkingdoms.fandom.com/wiki/Commander_Guide) · [touchscreengaming, 10/10/2025](https://touchscreengaming.com/formations-guide/) · [riseofkingdomsguides, 02/01/2026](https://riseofkingdomsguides.com/how-to-delete-unlink-account-in-rise-of-kingdoms/) · [doc OpenCV, s.d.](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_template_matching/py_template_matching.markdown) · [doc OpenCV, s.d.](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/tutorials/imgproc/histograms/template_matching/template_matching.markdown) · [forum ufficiale Lilith, 14/11/2025](https://forum-global.lilithgame.com/post/2030530) · [Android Developers, 03/08/2026](https://developer.android.com/reference/android/view/KeyEvent) · [BlueStacks, 11/12/2024](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/guide-expeditions-en.html) · [heaven-guardian, 03/08/2026](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/) · [wiki fandom, 12/06/2024](https://riseofkingdoms.fandom.com/wiki/Territory) · [BlueStacks, 23/12/2024](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-bluestacks-macros-en.html) · [wiki fandom, 29/04/2020](https://riseofkingdoms.fandom.com/wiki/Buildings/Barracks) · [wiki fandom, 11/01/2020](https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station) · [BlueStacks, 20/02/2023](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-gunning-for-the-top-en.html) · [forum ufficiale Lilith, 12/12/2025](https://forum-global.lilithgame.com/post/2179486) · [forum ufficiale Lilith, 24/02/2025](https://forum-global.lilithgame.com/post/1935973) · [riseofkingdomsguides, 02/01/2026](https://riseofkingdomsguides.com/rise-of-kingdoms-barbarians-and-barbarian-forts/) · [heaven-guardian, 06/08/2026](https://heaven-guardian.com/rise-of-kingdoms-troop-capacity-march-queue-guide/) · [Android Developers, 12/04/2023](https://developer.android.com/studio/test/other-testing-tools/monkey) · [forum ufficiale Lilith, 24/03/2023](https://forum-global.lilithgame.com/post/1450660) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-shop-and-bundles-guide) · [wiki fandom, 26/09/2026](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) · [forum ufficiale Lilith, 26/10/2022](https://forum-global.lilithgame.com/post/1395812) · [wiki fandom, 03/06/2025](https://riseofkingdoms.fandom.com/wiki/Scouting) · [wiki fandom, 11/03/2024](https://riseofkingdoms.fandom.com/wiki/Expedition) · [handbook, 18/08/2026](https://riseofkingdomshandbook.com/guides/riseofkingdoms-tavern-keys-guide) · [Lilith ToS, 15/04/2025 (campo show_at della pagina)](https://www.lilith.com/termofservice/?locale=en_US)

---

## 6. Lacune e fonti non raggiungibili

**Lacune (dati non trovati: nel JSON sono `null`):**
- Coordinate e posizione dei pulsanti del HUD (Commanders, Items, Alliance, Campaign, Search, Mail, barra risorse): nessuna fonte testuale le descrive; vanno misurate sul telefono (test T04-T13).
- Percorso esatto verso Commanders e Items: non documentato nelle fonti lette (solo 'Commanders'/'Comandanti' come nome).
- UI dell'addestramento (slider quantità, pulsante Train, pulsante Upgrade, pulsante gemme): non documentata.
- Numero di pannelli preset di marcia e loro posizione: non documentati (solo richiesta community del 2023 e risposta degli sviluppatori).
- Nomi italiani delle schermate nel client: non documentati; disponibili solo alcuni termini della scheda italiana di Google Play (Comandanti, Spedizione, Alleanza).
- Troops dal City Hall: nessuna fonte descrive un pulsante 'Troops' sul City Hall; documentata solo la sezione Troops del Governor Profile.
- Tavern: numero di aperture gratuite in conflitto tra fonti (handbook: 5 al giorno; riseofkingdomsguides: 3-10 secondo il livello).
- Tutorial/popup di nuove funzioni: nessun elenco; solo esempi dalle note di rilascio.
- Sintassi di 'input' (tap/swipe/keyevent/text), 'wm size/density', 'svc power stayon' e campi 'mCurrentFocus'/'mResumedActivity' di dumpsys: non documentati nelle pagine ufficiali lette (adb 2026-09-25, dumpsys 2026-07-23). Da verificare con l'help del telefono (test T02).
- Package name per Huawei AppGallery, Samsung, Amazon o versione cinese: non trovato (AppGallery API 403, pagina JS). Il bot deve rilevarlo con 'pm list packages lilith'.
- Stato 'unauthorized' di 'adb devices' non descritto nella pagina adb letta.
- Formato dei numeri nel client (separatore migliaia, K/M/B, decimali) e font: non documentati; da osservare negli screenshot (test T04).
- Date di ultima modifica dei file di documentazione Tesseract/OpenCV su GitHub non disponibili (API GitHub 403); docs.opencv.org risponde 403 sia a curl sia a WebFetch: usato il sorgente markdown ufficiale su raw.githubusercontent.com.
- Report anti-botting ufficiali con elenchi di account bannati trovati solo per il 2020 (post 1000060 e 1003107); tra gli 832 post dell'account ufficiale sul forum globale (ultimo post: 2026-06-23) non ci sono report più recenti. Il Conduct Score (1.1.07) non ha soglie né penalità pubbliche.
- Nessuna versione italiana dei ToS: la pagina offre solo zh_CN, en, ja, ko.
- Nessuna fonte ufficiale descrive i metodi di rilevamento dei bot; le affermazioni sul rilevamento sono della community (riseofkingdomshandbook.com).

**Fonti non raggiungibili o lette con un metodo alternativo:**
- `https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html (e group__imgproc__object, tutorial_py_thresholding, group__imgproc__transform)`: HTTP 403 sia con curl sia con WebFetch; usato il sorgente markdown ufficiale su raw.githubusercontent.com/opencv/opencv
- `https://api.github.com/repos/... (date dei commit della documentazione)`: HTTP 403 (come atteso dietro il proxy)
- `https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/ e /blog/games/rise-of-kingdoms/page/7.html, page/8.html`: HTTP 500 (l'indice esiste solo come /blog/games/rise-of-kingdoms.html e pagine 1-6)
- `https://www.allclash.com/rise-of-kingdoms/ e https://www.allclash.com/sitemap_index.xml`: HTTP 403 (WebFetch) / challenge Cloudflare (curl)
- `https://appgallery.huawei.com/app/C100816261`: pagina JavaScript vuota via WebFetch; API web-dre.hispace.dbankcloud.com HTTP 403 -> package Huawei non verificato
- `https://www.lilith.com/termofservice/?locale=en_US (via WebFetch)`: WebFetch vede solo il logo (pagina JS); testo letto con curl dal JSON incorporato nella pagina (campo multilang_content, lingua 'en')
- `https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp (via WebFetch)`: contenuto troncato; letto con curl (hl=en e hl=it)
- `https://riseofkingdomsguides.com/* (via curl)`: pagina 'Bot Verification'; lette via WebFetch (testo riassunto, non verbatim)
- `https://developer.android.com/tools/adb (via curl senza cookie)`: loop di redirect oauth2; risolto con cookie jar (curl -c/-b)
- `https://heaven-guardian.com/* (richieste ravvicinate)`: 'Connection reset by peer' intermittente; risolto con richieste distanziate e tentativi
- `https://forum-global.lilithgame.com/post/<id> (pagina HTML)`: pagina JS; testo letto dall'API pubblica /api/v2/posts/<id>
- `https://android.googlesource.com/... (sorgenti AOSP di input/svc/screencap)`: non usati come fonte: l'istruzione vieta di scaricare codice di terzi; PowerCommand.java HTTP 503, screencap.cpp 404/503
- `WebSearch / Bing / ricerca GitHub`: non disponibili in questa sessione (budget esaurito / 403): le pagine sono state trovate tramite sitemap, indici dei siti e API del forum ufficiale

**Metodo.** Fonti lette il 2026-09-28 con curl (pagine statiche, API MediaWiki della wiki, API del forum ufficiale Lilith, raw.githubusercontent.com, pypi.org) o WebFetch (riseofkingdomsguides.com, allclash.com, ldshop.gg: testo riassunto dal fetcher, quindi citato come parafrasi). Nessun codice di terzi eseguito. Le date 'page_date' sono quelle della pagina (dateModified/og:modified, revisione wiki, data del post) o null se non disponibili.

---

## Fonti (126)

- [https://www.allclash.com/the-only-rise-of-kingdoms-gathering-guide-you-really-need/](https://www.allclash.com/the-only-rise-of-kingdoms-gathering-guide-you-really-need/) — allclash.com (WebFetch), pagina del 21/02/2020, letta il 28/09/2026. Usata per: consultata: nessuna descrizione della UI di ricerca/raccolta
- [https://apps.apple.com/us/app/rise-of-kingdoms/id1354260888](https://apps.apple.com/us/app/rise-of-kingdoms/id1354260888) — apps.apple.com, pagina del 22/09/2026 (versione 1.1.12.20), letta il 28/09/2026. Usata per: id; seller; versione e data; lingue (Italian incluso)
- [https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/guide-expeditions-en.html](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/guide-expeditions-en.html) — bluestacks.com, pagina del 11/12/2024, letta il 28/09/2026. Usata per: Campaign menu -> Expedition; Campaign -> Expedition
- [https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-bluestacks-macros-en.html](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-bluestacks-macros-en.html) — bluestacks.com, pagina del 23/12/2024, letta il 28/09/2026. Usata per: globe map/city button, doppio clic per reset camera; evitare di muovere la camera; doppio clic sul pulsante mappa/città per reset camera; Macro Recorder per RoK
- [https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-faqs-en.html](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-faqs-en.html) — bluestacks.com, pagina del 10/02/2021, letta il 28/09/2026. Usata per: arrow button next to your profile picture
- [https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-instance-manager-en.html](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-instance-manager-en.html) — bluestacks.com, pagina del 02/03/2021, letta il 28/09/2026. Usata per: Multi-Instance Sync
- [https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-ultimate-alliance-guide-en.html](https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/rok-ultimate-alliance-guide-en.html) — bluestacks.com, pagina del 06/12/2024, letta il 28/09/2026. Usata per: Alliance menu -> Create
- [https://www.bluestacks.com/blog/games/rise-of-kingdoms.html](https://www.bluestacks.com/blog/games/rise-of-kingdoms.html) — bluestacks.com, pagina del s.d., letta il 28/09/2026. Usata per: indice articoli RoK (pagine 1-6, 65 articoli)
- [https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-developer-feedback-march-april-2023-en.html](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-developer-feedback-march-april-2023-en.html) — bluestacks.com, pagina del 23/05/2023, letta il 28/09/2026. Usata per: stessa domanda/risposta
- [https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-face-to-face-developer-notes-en.html](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-face-to-face-developer-notes-en.html) — bluestacks.com, pagina del 21/04/2023, letta il 28/09/2026. Usata per: stessa risposta riportata da BlueStacks (Developer Notes #13)
- [https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-gunning-for-the-top-en.html](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-gunning-for-the-top-en.html) — bluestacks.com, pagina del 20/02/2023, letta il 28/09/2026. Usata per: travel con gemme fino a 200/giorno; recycle con password secondaria; lock; icone formazioni
- [https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-multiple-devices-update-en.html](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-multiple-devices-update-en.html) — bluestacks.com, pagina del 24/01/2025, letta il 28/09/2026. Usata per: Account -> switch
- [https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-spring-once-more-en.html](https://www.bluestacks.com/blog/updates/rise-of-kingdoms/rok-spring-once-more-en.html) — bluestacks.com, pagina del 29/03/2023, letta il 28/09/2026. Usata per: skip animazioni; ordinamento per data
- [https://developer.android.com/reference/android/os/BatteryManager](https://developer.android.com/reference/android/os/BatteryManager) — developer.android.com, pagina del 03/08/2026, letta il 28/09/2026. Usata per: BATTERY_PLUGGED_AC/USB/WIRELESS/DOCK = 1/2/4/8
- [https://developer.android.com/reference/android/provider/Settings.Global](https://developer.android.com/reference/android/provider/Settings.Global) — developer.android.com, pagina del 03/08/2026, letta il 28/09/2026. Usata per: STAY_ON_WHILE_PLUGGED_IN
- [https://developer.android.com/reference/android/view/KeyEvent](https://developer.android.com/reference/android/view/KeyEvent) — developer.android.com, pagina del 03/08/2026, letta il 28/09/2026. Usata per: valori KEYCODE_BACK/HOME/POWER/MENU/APP_SWITCH/SLEEP/WAKEUP; descrizione WAKEUP e HOME; KEYCODE_WAKEUP; KEYCODE_BACK = 4
- [https://developer.android.com/studio/debug/dev-options](https://developer.android.com/studio/debug/dev-options) — developer.android.com, pagina del 16/09/2026, letta il 28/09/2026. Usata per: Build number sette volte; percorsi USB debugging per versione Android; Stay awake; Show taps
- [https://developer.android.com/studio/test/other-testing-tools/monkey](https://developer.android.com/studio/test/other-testing-tools/monkey) — developer.android.com, pagina del 12/04/2023, letta il 28/09/2026. Usata per: sintassi monkey [options] <event-count>; -p; -c; --throttle
- [https://developer.android.com/tools/adb](https://developer.android.com/tools/adb) — developer.android.com, pagina del 25/09/2026, letta il 28/09/2026. Usata per: Enable adb debugging; RSA key dialog; adb devices -l stati; -s serial / ANDROID_SERIAL
- [https://developer.android.com/tools/dumpsys](https://developer.android.com/tools/dumpsys) — developer.android.com, pagina del 23/07/2026, letta il 28/09/2026. Usata per: sintassi dumpsys; -l; -t timeout (default 10 s); l'output varia con la versione di Android
- [https://forum-global.lilithgame.com/api/v2/posts?account_id=10000000](https://forum-global.lilithgame.com/api/v2/posts?account_id=10000000) — forum-global.lilithgame.com (API del forum ufficiale), pagina del 23/06/2026 (ultimo post dell'account ufficiale), letta il 28/09/2026. Usata per: elenco post ufficiali: 832 in totale
- [https://forum-global.lilithgame.com/post/1041743](https://forum-global.lilithgame.com/post/1041743) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 20/01/2021, letta il 28/09/2026. Usata per: secondary password in Settings; password secondaria; secondary password
- [https://forum-global.lilithgame.com/post/1125881](https://forum-global.lilithgame.com/post/1125881) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 06/09/2021, letta il 28/09/2026. Usata per: permessi alleanza
- [https://forum-global.lilithgame.com/post/1197916](https://forum-global.lilithgame.com/post/1197916) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 10/01/2022, letta il 28/09/2026. Usata per: scopo del sistema di verifica; scopo della verifica
- [https://forum-global.lilithgame.com/post/1359527](https://forum-global.lilithgame.com/post/1359527) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 29/07/2022, letta il 28/09/2026. Usata per: verification code system, conduct scores; verification codes e conduct score
- [https://forum-global.lilithgame.com/post/1395812](https://forum-global.lilithgame.com/post/1395812) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 26/10/2022, letta il 28/09/2026. Usata per: Claim All regali normali, non rari; Claim All
- [https://forum-global.lilithgame.com/post/1433064](https://forum-global.lilithgame.com/post/1433064) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 10/02/2023, letta il 28/09/2026. Usata per: recycle con password secondaria; riciclo
- [https://forum-global.lilithgame.com/post/1450660](https://forum-global.lilithgame.com/post/1450660) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 24/03/2023, letta il 28/09/2026. Usata per: 1-minute verification window; plug-ins; finestra di verifica; verification window
- [https://forum-global.lilithgame.com/post/1466061](https://forum-global.lilithgame.com/post/1466061) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 28/04/2023, letta il 28/09/2026. Usata per: heal all troops at once; preset panels con 7 marce (risposta sviluppatori)
- [https://forum-global.lilithgame.com/post/1589003](https://forum-global.lilithgame.com/post/1589003) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 07/11/2023, letta il 28/09/2026. Usata per: conferma attacco/scout nel proprio campo
- [https://forum-global.lilithgame.com/post/1599092](https://forum-global.lilithgame.com/post/1599092) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 06/12/2023, letta il 28/09/2026. Usata per: Settings - DLC; transmutation con verifica secondaria; trasmutazione
- [https://forum-global.lilithgame.com/post/1612606](https://forum-global.lilithgame.com/post/1612606) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 09/01/2024, letta il 28/09/2026. Usata per: Don't ask again today
- [https://forum-global.lilithgame.com/post/1670239](https://forum-global.lilithgame.com/post/1670239) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 20/06/2024, letta il 28/09/2026. Usata per: immigrazione, equipaggiamento leggendario
- [https://forum-global.lilithgame.com/post/1726094](https://forum-global.lilithgame.com/post/1726094) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 23/07/2024, letta il 28/09/2026. Usata per: nuovo login
- [https://forum-global.lilithgame.com/post/1896244](https://forum-global.lilithgame.com/post/1896244) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 31/12/2024, letta il 28/09/2026. Usata per: Campaign interface, red dot
- [https://forum-global.lilithgame.com/post/1935973](https://forum-global.lilithgame.com/post/1935973) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 24/02/2025, letta il 28/09/2026. Usata per: skill semplificate/complete; priorità ricerca punti risorsa; Quick Dispatch e Travel x10; Quick Dispatch
- [https://forum-global.lilithgame.com/post/1963188](https://forum-global.lilithgame.com/post/1963188) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 14/11/2025, letta il 28/09/2026. Usata per: conferma al cambio equipaggiamento; conferma cambio equipaggiamento
- [https://forum-global.lilithgame.com/post/2030530](https://forum-global.lilithgame.com/post/2030530) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 14/11/2025, letta il 28/09/2026. Usata per: Search/Return Switch; Spin Ticket acquistabili con gemme; pulsante Search (mobile)
- [https://forum-global.lilithgame.com/post/2102690](https://forum-global.lilithgame.com/post/2102690) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 14/11/2025, letta il 28/09/2026. Usata per: tutorial interattivo Ark of Osiris (1.0.98)
- [https://forum-global.lilithgame.com/post/2124406](https://forum-global.lilithgame.com/post/2124406) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 14/11/2025, letta il 28/09/2026. Usata per: Rapid Retreat automatico, 80 gemme
- [https://forum-global.lilithgame.com/post/2161435](https://forum-global.lilithgame.com/post/2161435) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 14/11/2025, letta il 28/09/2026. Usata per: queue management (CH8, disattivabile in Settings); loadout presets (sezione Champions of Olympia); auto peacekeeping batch; queue management
- [https://forum-global.lilithgame.com/post/2179486](https://forum-global.lilithgame.com/post/2179486) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 12/12/2025, letta il 28/09/2026. Usata per: ricerca Barbarian Forts; Marauders; ricerca forti
- [https://forum-global.lilithgame.com/post/2213663](https://forum-global.lilithgame.com/post/2213663) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 26/02/2026, letta il 28/09/2026. Usata per: Flux Coins: riconferma + password secondaria; riconferma Flux; evita barbari ingaggiati; Flux
- [https://forum-global.lilithgame.com/post/2232581](https://forum-global.lilithgame.com/post/2232581) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 30/04/2026, letta il 28/09/2026. Usata per: Auto-Peacekeeping: AP display, livelli salvati; Conduct Score System; scripts/cheats; penalità a soglie
- [https://forum-global.lilithgame.com/post/2246725](https://forum-global.lilithgame.com/post/2246725) — forum-global.lilithgame.com (forum ufficiale, account GM 'Rise of Kingdoms'; testo letto via API /api/v2/posts/<id>), pagina del 27/05/2026, letta il 28/09/2026. Usata per: password secondaria per inscribing e converting; inscribing/converting
- [https://forum-global.lilithgame.com/post/1000060](https://forum-global.lilithgame.com/post/1000060) — forum-global.lilithgame.com (forum ufficiale, account GM; API /api/v2/posts/<id>), pagina del 01/09/2020, letta il 28/09/2026. Usata per: Anti-Botting Report; banned
- [https://forum-global.lilithgame.com/post/1003107](https://forum-global.lilithgame.com/post/1003107) — forum-global.lilithgame.com (forum ufficiale, account GM; API /api/v2/posts/<id>), pagina del 16/10/2020, letta il 28/09/2026. Usata per: banned permanently
- [https://forum-global.lilithgame.com/post/1044203](https://forum-global.lilithgame.com/post/1044203) — forum-global.lilithgame.com (forum ufficiale, account GM; API /api/v2/posts/<id>), pagina del 27/01/2021, letta il 28/09/2026. Usata per: third-party programs -> ban; 167.000 personaggi bannati in 3 mesi
- [https://heaven-guardian.com/rise-of-kingdoms-alliance-guide-territory-flags-forts/](https://heaven-guardian.com/rise-of-kingdoms-alliance-guide-territory-flags-forts/) — heaven-guardian.com, pagina del 03/08/2026, letta il 28/09/2026. Usata per: territorio: 'usare i costi mostrati nell'interfaccia'
- [https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/) — heaven-guardian.com, pagina del 02/09/2026, letta il 28/09/2026. Usata per: consultata: strategia, nessun dettaglio UI
- [https://heaven-guardian.com/rise-of-kingdoms-best-troops-training-guide/](https://heaven-guardian.com/rise-of-kingdoms-best-troops-training-guide/) — heaven-guardian.com, pagina del 02/09/2026, letta il 28/09/2026. Usata per: code separate per edificio; MGE punti upgrade
- [https://heaven-guardian.com/rise-of-kingdoms-codes/](https://heaven-guardian.com/rise-of-kingdoms-codes/) — heaven-guardian.com, pagina del 18/09/2026, letta il 28/09/2026. Usata per: Profile > Settings > Redeem; percorso Profile > Settings > Redeem; icona a scatola regalo; conferma
- [https://heaven-guardian.com/rise-of-kingdoms-dominate-barbarians-forts-guide/](https://heaven-guardian.com/rise-of-kingdoms-dominate-barbarians-forts-guide/) — heaven-guardian.com, pagina del 03/08/2026, letta il 28/09/2026. Usata per: map search interface/function
- [https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/) — heaven-guardian.com, pagina del 19/09/2026, letta il 28/09/2026. Usata per: tap help icon; donazioni secondo interfaccia; 10.000 crediti/giorno
- [https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/) — heaven-guardian.com, pagina del 03/08/2026, letta il 28/09/2026. Usata per: paper-style Events icon; icona Events 'paper-style'; UTC; Monument
- [https://heaven-guardian.com/rise-of-kingdoms-farm-account-guide-for-max-resources/](https://heaven-guardian.com/rise-of-kingdoms-farm-account-guide-for-max-resources/) — heaven-guardian.com, pagina del 03/08/2026, letta il 28/09/2026. Usata per: Character Management -> Create New Character
- [https://heaven-guardian.com/rise-of-kingdoms-scout-camp-guide/](https://heaven-guardian.com/rise-of-kingdoms-scout-camp-guide/) — heaven-guardian.com, pagina del 02/09/2026, letta il 28/09/2026. Usata per: navigazione verso il villaggio successivo
- [https://heaven-guardian.com/rise-of-kingdoms-troop-capacity-march-queue-guide/](https://heaven-guardian.com/rise-of-kingdoms-troop-capacity-march-queue-guide/) — heaven-guardian.com, pagina del 06/08/2026, letta il 28/09/2026. Usata per: saved preset; march-creation screen; schermata creazione marcia e preset
- [https://www.ldshop.gg/blog/rise-of-kingdoms/](https://www.ldshop.gg/blog/rise-of-kingdoms/) — ldshop.gg (WebFetch), pagina del s.d., letta il 28/09/2026. Usata per: indice: solo 4 articoli (anniversario 1.1.11, Halloween 2026, difesa KvK, codici), nessuno sulla UI
- [https://www.lilith.com/termofservice/?locale=en_US](https://www.lilith.com/termofservice/?locale=en_US) — lilith.com, pagina del 15/04/2025 (campo show_at della pagina), letta il 28/09/2026. Usata per: 17.1.6; testo clausole 1.1, 2, 17.1.6, 17.1.7, 17.1.12, 17.1.15, 17.1.18, 17.1.19, 17.1.21, 17.3, 20.1, 21.1-21.3, 26, 30.3; data show_at 2025-04-15; lingue disponibili
- [https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=en&gl=US](https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=en&gl=US) — play.google.com, pagina del 17/09/2026, letta il 28/09/2026. Usata per: package; titolo; sviluppatore; Updated on
- [https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=it&gl=IT](https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp&hl=it&gl=IT) — play.google.com (scheda italiana, testo dello sviluppatore), pagina del 17/09/2026, letta il 28/09/2026. Usata per: 'Comandanti'; 'albero del talento', 'abilità'; 'Sistema dell'Alleanza'; 'Modalità Spedizione'
- [https://pypi.org/project/opencv-python/](https://pypi.org/project/opencv-python/) — pypi.org, pagina del 02/07/2026 (versione 5.0.0.93), letta il 28/09/2026. Usata per: un solo pacchetto; headless
- [https://pypi.org/project/pytesseract/](https://pypi.org/project/pytesseract/) — pypi.org, pagina del 16/08/2024 (versione 0.3.13), letta il 28/09/2026. Usata per: BGR -> RGB; image_to_string; image_to_data; timeout
- [https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.markdown](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.markdown) — raw.githubusercontent.com/opencv/opencv (sorgente della doc ufficiale), pagina del s.d., letta il 28/09/2026. Usata per: INTER_AREA per shrink, INTER_CUBIC/INTER_LINEAR per zoom; cv.resize e interpolazioni
- [https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.markdown](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.markdown) — raw.githubusercontent.com/opencv/opencv (sorgente della doc ufficiale), pagina del s.d., letta il 28/09/2026. Usata per: threshold, adaptiveThreshold, Otsu
- [https://raw.githubusercontent.com/opencv/opencv/4.x/doc/tutorials/imgproc/histograms/template_matching/template_matching.markdown](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/tutorials/imgproc/histograms/template_matching/template_matching.markdown) — raw.githubusercontent.com/opencv/opencv (sorgente della doc ufficiale), pagina del s.d., letta il 28/09/2026. Usata per: mask solo TM_SQDIFF e TM_CCORR_NORMED; mask stesse dimensioni; mask
- [https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_template_matching/py_template_matching.markdown](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_template_matching/py_template_matching.markdown) — raw.githubusercontent.com/opencv/opencv (sorgente della doc ufficiale; identico sul branch 5.x), pagina del s.d., letta il 28/09/2026. Usata per: matchTemplate; dimensione risultato; minimo per SQDIFF; threshold 0.8 con np.where
- [https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/Command-Line-Usage.md](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/Command-Line-Usage.md) — raw.githubusercontent.com/tesseract-ocr/tessdoc (documentazione ufficiale Tesseract, branch main), pagina del s.d., letta il 28/09/2026. Usata per: -l LANG; -l LANG[+LANG]; ordine delle lingue
- [https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/Data-Files.md](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/Data-Files.md) — raw.githubusercontent.com/tesseract-ocr/tessdoc (documentazione ufficiale Tesseract, branch main), pagina del s.d., letta il 28/09/2026. Usata per: ita | Italian; tessdata_fast vs tessdata_best; tessdata_fast/best; LSTM only
- [https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ImproveQuality.md](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ImproveQuality.md) — raw.githubusercontent.com/tesseract-ocr/tessdoc (documentazione ufficiale Tesseract, branch main), pagina del s.d., letta il 28/09/2026. Usata per: Inverting images; Rescaling 300 dpi; Binarisation; Missing borders
- [https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ReleaseNotes.md](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/ReleaseNotes.md) — raw.githubusercontent.com/tesseract-ocr/tessdoc (documentazione ufficiale Tesseract, branch main), pagina del 24/07/2026 (ultima release elencata: V5.5.3), letta il 28/09/2026. Usata per: V4.1.0: whitelist/blacklist in LSTM; user-words/user-patterns con LSTM
- [https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/tess3/FAQ-Old.md](https://raw.githubusercontent.com/tesseract-ocr/tessdoc/main/tess3/FAQ-Old.md) — raw.githubusercontent.com/tesseract-ocr/tessdoc (documentazione ufficiale Tesseract, branch main), pagina del s.d., letta il 28/09/2026. Usata per: How do I recognize only digits
- [https://riseofkingdoms.fandom.com/wiki/Barbarians](https://riseofkingdoms.fandom.com/wiki/Barbarians) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 07/11/2024, letta il 28/09/2026. Usata per: sblocco livelli barbari
- [https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center](https://riseofkingdoms.fandom.com/wiki/Buildings/Alliance_Center) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 26/09/2026, letta il 28/09/2026. Usata per: training non beneficia dell'Alliance Help; Help su healing; Alliance Help, mano sopra l'Alliance Center, 1%/1 min, max aiuti; Help
- [https://riseofkingdoms.fandom.com/wiki/Buildings/Barracks](https://riseofkingdoms.fandom.com/wiki/Buildings/Barracks) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 29/04/2020, letta il 28/09/2026. Usata per: 5 tier; upgrade di un tier alla volta; tier e upgrade
- [https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station](https://riseofkingdoms.fandom.com/wiki/Buildings/Courier_Station) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 11/01/2020, letta il 28/09/2026. Usata per: icona sopra l'edificio; 0:00 UTC; 16 oggetti; Refresh in alto a destra
- [https://riseofkingdoms.fandom.com/wiki/Buildings/Hospital](https://riseofkingdoms.fandom.com/wiki/Buildings/Hospital) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 30/04/2020, letta il 28/09/2026. Usata per: feriti gravi/leggeri; ospedale pieno -> morti; sblocco ospedali 1/4/9/15
- [https://riseofkingdoms.fandom.com/wiki/Buildings/Scout_Camp](https://riseofkingdoms.fandom.com/wiki/Buildings/Scout_Camp) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 22/11/2023, letta il 28/09/2026. Usata per: sblocco CH2; funzioni
- [https://riseofkingdoms.fandom.com/wiki/Buildings/Tavern](https://riseofkingdoms.fandom.com/wiki/Buildings/Tavern) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 01/09/2020, letta il 28/09/2026. Usata per: tipi di forzieri
- [https://riseofkingdoms.fandom.com/wiki/Commander_Guide](https://riseofkingdoms.fandom.com/wiki/Commander_Guide) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 16/07/2023, letta il 28/09/2026. Usata per: specialità, abilità, expertise; abilità a caso fino al 5; punti talento; Talent Reset costoso
- [https://riseofkingdoms.fandom.com/wiki/Expedition](https://riseofkingdoms.fandom.com/wiki/Expedition) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 11/03/2024, letta il 28/09/2026. Usata per: regole; pulsante in alto a sinistra per claim 3 stelle; reset 00:00 UTC; claim all 3-Star
- [https://riseofkingdoms.fandom.com/wiki/Frequently_Asked_Questions](https://riseofkingdoms.fandom.com/wiki/Frequently_Asked_Questions) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 25/06/2026, letta il 28/09/2026. Usata per: icona 'i'; richiamo prima dell'arrivo
- [https://riseofkingdoms.fandom.com/wiki/Governor_Profile](https://riseofkingdoms.fandom.com/wiki/Governor_Profile) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 02/12/2025, letta il 28/09/2026. Usata per: avatar/profilo; campi del profilo; Rankings CH8; Achievements CH6
- [https://riseofkingdoms.fandom.com/wiki/Items](https://riseofkingdoms.fandom.com/wiki/Items) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 01/12/2019, letta il 28/09/2026. Usata per: categorie
- [https://riseofkingdoms.fandom.com/wiki/Resources](https://riseofkingdoms.fandom.com/wiki/Resources) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 31/05/2025, letta il 28/09/2026. Usata per: gemme per velocizzare training/research/building; risorse come oggetti non saccheggiabili
- [https://riseofkingdoms.fandom.com/wiki/Scouting](https://riseofkingdoms.fandom.com/wiki/Scouting) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 03/06/2025, letta il 28/09/2026. Usata per: Explore; Scouting Report NEW!; villaggi con icona regalo; caverne
- [https://riseofkingdoms.fandom.com/wiki/Territory](https://riseofkingdoms.fandom.com/wiki/Territory) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 12/06/2024, letta il 28/09/2026. Usata per: menu Help e sezione Technology per crediti; 50% nella pagina Alliance Territory; sezioni Alliance
- [https://riseofkingdoms.fandom.com/wiki/Troop_Dispatch_Queue](https://riseofkingdoms.fandom.com/wiki/Troop_Dispatch_Queue) — riseofkingdoms.fandom.com (wiki community; testo letto via API MediaWiki, data = ultima revisione), pagina del 15/09/2024, letta il 28/09/2026. Usata per: code per livello CH
- [https://riseofkingdomsguides.com/barracks/](https://riseofkingdomsguides.com/barracks/) — riseofkingdomsguides.com (WebFetch), pagina del 02/01/2026, letta il 28/09/2026. Usata per: consultata: solo tabella livelli, nessuna descrizione della UI di addestramento
- [https://riseofkingdomsguides.com/how-to-get-alliance-and-individual-credits-in-rise-of-kingdoms/](https://riseofkingdomsguides.com/how-to-get-alliance-and-individual-credits-in-rise-of-kingdoms/) — riseofkingdomsguides.com (WebFetch), pagina del s.d., letta il 28/09/2026. Usata per: consultata: Alliance Shop/Reclaim, nessuna posizione di pulsanti
- [https://riseofkingdomsguides.com/post-sitemap.xml](https://riseofkingdomsguides.com/post-sitemap.xml) — riseofkingdomsguides.com (WebFetch), pagina del s.d., letta il 28/09/2026. Usata per: elenco URL (184) per trovare le guide senza motore di ricerca
- [https://riseofkingdomsguides.com/post-sitemap2.xml](https://riseofkingdomsguides.com/post-sitemap2.xml) — riseofkingdomsguides.com (WebFetch), pagina del s.d., letta il 28/09/2026. Usata per: elenco URL (21 pertinenti)
- [https://riseofkingdomsguides.com/rise-of-kingdoms-commander-guide/](https://riseofkingdomsguides.com/rise-of-kingdoms-commander-guide/) — riseofkingdomsguides.com (WebFetch), pagina del 02/01/2026, letta il 28/09/2026. Usata per: consultata: nessuna descrizione della UI dei comandanti
- [https://riseofkingdomsguides.com/rise-of-kingdoms-troop-capacity-and-march-queue-guide/](https://riseofkingdomsguides.com/rise-of-kingdoms-troop-capacity-and-march-queue-guide/) — riseofkingdomsguides.com (WebFetch), pagina del 02/01/2026, letta il 28/09/2026. Usata per: consultata: nessuna descrizione della schermata marcia/preset
- [https://riseofkingdomsguides.com/courier-station/](https://riseofkingdomsguides.com/courier-station/) — riseofkingdomsguides.com (letto via WebFetch: testo riassunto dal fetcher), pagina del 02/01/2026, letta il 28/09/2026. Usata per: costi Free/100/200/300/400
- [https://riseofkingdomsguides.com/farming-gathering-guide/](https://riseofkingdomsguides.com/farming-gathering-guide/) — riseofkingdomsguides.com (letto via WebFetch: testo riassunto dal fetcher), pagina del s.d., letta il 28/09/2026. Usata per: city hall -> graph icon
- [https://riseofkingdomsguides.com/hospital/](https://riseofkingdomsguides.com/hospital/) — riseofkingdomsguides.com (letto via WebFetch: testo riassunto dal fetcher), pagina del 02/01/2026, letta il 28/09/2026. Usata per: niente cure durante un rally subito
- [https://riseofkingdomsguides.com/how-to-delete-unlink-account-in-rise-of-kingdoms/](https://riseofkingdomsguides.com/how-to-delete-unlink-account-in-rise-of-kingdoms/) — riseofkingdomsguides.com (letto via WebFetch: testo riassunto dal fetcher), pagina del 02/01/2026, letta il 28/09/2026. Usata per: Other -> Delete Account; definitivo; Other -> Delete Account da evitare
- [https://riseofkingdomsguides.com/rise-of-kingdoms-barbarians-and-barbarian-forts/](https://riseofkingdomsguides.com/rise-of-kingdoms-barbarians-and-barbarian-forts/) — riseofkingdomsguides.com (letto via WebFetch: testo riassunto dal fetcher), pagina del 02/01/2026, letta il 28/09/2026. Usata per: limite raggio ricerca; sconto AP in catena; limite del raggio di ricerca
- [https://riseofkingdomsguides.com/scouting-tribal-village-and-mysterious-cave-guide/](https://riseofkingdomsguides.com/scouting-tribal-village-and-mysterious-cave-guide/) — riseofkingdomsguides.com (letto via WebFetch: testo riassunto dal fetcher), pagina del 02/01/2026, letta il 28/09/2026. Usata per: tre scout
- [https://riseofkingdomsguides.com/tavern/](https://riseofkingdomsguides.com/tavern/) — riseofkingdomsguides.com (letto via WebFetch: testo riassunto dal fetcher), pagina del 02/01/2026, letta il 28/09/2026. Usata per: open all keys (>=10); tabella free chest per livello
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-account-buying-selling-risks](https://riseofkingdomshandbook.com/guides/riseofkingdoms-account-buying-selling-risks) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: The Terms of Service Position
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-guide-hub](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-guide-hub) — riseofkingdomshandbook.com, pagina del 09/09/2026, letta il 28/09/2026. Usata per: alliance screen
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-shop-guide](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-shop-guide) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: help button, shop d'alleanza
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-barbarian-forts-guide](https://riseofkingdomshandbook.com/guides/riseofkingdoms-barbarian-forts-guide) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: forti solo in rally
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub](https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub) — riseofkingdomshandbook.com, pagina del 09/09/2026, letta il 28/09/2026. Usata per: contatori More Than Gems, registrazioni
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-expedition-guide](https://riseofkingdomshandbook.com/guides/riseofkingdoms-expedition-guide) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: truppe simulate; daily chest
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-formations-armaments-inscriptions-guide](https://riseofkingdomshandbook.com/guides/riseofkingdoms-formations-armaments-inscriptions-guide) — riseofkingdomshandbook.com, pagina del 09/09/2026, letta il 28/09/2026. Usata per: preset e pezzi equipaggiati da controllare
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-game-mechanics-hub](https://riseofkingdomshandbook.com/guides/riseofkingdoms-game-mechanics-hub) — riseofkingdomshandbook.com, pagina del 09/09/2026, letta il 28/09/2026. Usata per: rally: leader, finestra di preparazione
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-gift-codes](https://riseofkingdomshandbook.com/guides/riseofkingdoms-gift-codes) — riseofkingdomshandbook.com, pagina del 09/09/2026, letta il 28/09/2026. Usata per: Tap the avatar, open Settings and find Redeem; messaggi already redeemed/expired
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-governor-id-account-guide](https://riseofkingdomshandbook.com/guides/riseofkingdoms-governor-id-account-guide) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: avatar in alto a sinistra; Governor ID
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-healing-hospital-guide](https://riseofkingdomshandbook.com/guides/riseofkingdoms-healing-hospital-guide) — riseofkingdomshandbook.com, pagina del 09/09/2026, letta il 28/09/2026. Usata per: non automatizzare i tocchi; automate taps
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-how-to-play-on-pc](https://riseofkingdomshandbook.com/guides/riseofkingdoms-how-to-play-on-pc) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: una sola sessione attiva; client PC ufficiale; emulatori; Auto-farming bots ... against the terms of service
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-mod-apk-bots-and-bans](https://riseofkingdomshandbook.com/guides/riseofkingdoms-mod-apk-bots-and-bans) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: What Bots Actually Do; ban a livello di account; acquisti non rimborsati; Detection has improved considerably
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-returning-player-guide](https://riseofkingdomshandbook.com/guides/riseofkingdoms-returning-player-guide) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: banner e tab returnee
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-server-status-and-fixes](https://riseofkingdomshandbook.com/guides/riseofkingdoms-server-status-and-fixes) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: compensation mail; aggiornamento obbligatorio; manutenzione, update obbligatorio
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-shop-and-bundles-guide](https://riseofkingdomshandbook.com/guides/riseofkingdoms-shop-and-bundles-guide) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: negozi e pacchetti; offerte e negozi
- [https://riseofkingdomshandbook.com/guides/riseofkingdoms-tavern-keys-guide](https://riseofkingdomshandbook.com/guides/riseofkingdoms-tavern-keys-guide) — riseofkingdomshandbook.com, pagina del 18/08/2026, letta il 28/09/2026. Usata per: 5 aperture gratuite, gold ogni ~2 giorni; aperture gratuite
- [https://rok.lilith.com/](https://rok.lilith.com/) — rok.lilith.com, pagina del 2025 (footer '© 2025'), letta il 28/09/2026. Usata per: link Google Play con id=com.lilithgame.roc.gp; link AppGallery C100816261; link download PC; link ufficiale ai Terms of Service e alla Privacy Policy
- [https://theriagames.com/guide/rise-of-kingdoms-alliance-center-guide/](https://theriagames.com/guide/rise-of-kingdoms-alliance-center-guide/) — theriagames.com, pagina del 06/02/2025, letta il 28/09/2026. Usata per: Technology panel; creazione alleanza 500 gemme
- [https://theriagames.com/guide/rise-of-kingdoms-barracks-guide/](https://theriagames.com/guide/rise-of-kingdoms-barracks-guide/) — theriagames.com, pagina del 08/02/2025, letta il 28/09/2026. Usata per: consultata: testo generico, nessun dettaglio UI
- [https://theriagames.com/guide/rise-of-kingdoms-courier-station-guide/](https://theriagames.com/guide/rise-of-kingdoms-courier-station-guide/) — theriagames.com, pagina del 07/02/2025, letta il 28/09/2026. Usata per: 0:00 UTC; primo refresh gratis
- [https://theriagames.com/guide/rise-of-kingdoms-scout-camp-guide/](https://theriagames.com/guide/rise-of-kingdoms-scout-camp-guide/) — theriagames.com, pagina del 07/02/2025, letta il 28/09/2026. Usata per: Explore; Visit
- [https://theriagames.com/guide/rise-of-kingdoms-tavern-guide/](https://theriagames.com/guide/rise-of-kingdoms-tavern-guide/) — theriagames.com, pagina del 08/02/2025, letta il 28/09/2026. Usata per: free silver keys, upgrade aumenta aperture
- [https://touchscreengaming.com/formations-guide/](https://touchscreengaming.com/formations-guide/) — touchscreengaming.com, pagina del 10/10/2025, letta il 28/09/2026. Usata per: formazione assegnata in città; 4 armamenti; 20 AP / 200 AP x10; Dispatch L10 30-150 AP
