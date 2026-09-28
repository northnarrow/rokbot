# Routine giornaliera, economia e crescita — Rise of Kingdoms (bot senza gemme)

Aggiornato al **2026-09-28**. Fonte dati: `data/fragments/strategia_routine.json` (stesso contenuto, con `sources` per ogni voce, `gaps` e `conflicts`). Nomi tecnici in inglese come nel gioco.

> **Vincoli del bot.** Mai spendere gemme (niente acquisti, velocizzazioni, refresh, spin di Wheel of Fortune/Esmeralda, chiavi, VIP points, tentativi extra). Chiedere conferma prima di attaccare giocatori o consumare materiali rari (sculture, Books of Covenant, Arrows of Resistance, Master's Blueprint, Sage's Testimony, Transmutation/Conversion Stones, Armament Tickets, Golden Keys fuori evento, Civilization Change, Passport, teletrasporti, scudi, oggetti AP fuori evento). Le date degli eventi NON sono fisse: il bot legge sempre il pannello Events in gioco e il countdown UTC.

## 0. Orari di riferimento (UTC)

| Cosa | Quando |
|---|---|
| Reset giornaliero | **00:00 UTC** — confidenza media (vedi nota sotto) |
| Reset settimanale | VIP Shop: lunedi' 00:00 UTC (limiti settimanali ripristinati) |
| Guardiani Holy Sites | spawn alle 00:00 e 12:00 UTC, restano 11 ore (theriagames); heaven-guardian parla di ciclo di 12 ore e di orari che dipendono dal regno |
| Action Points | continuo: cap 1.500 AP secondo Lilith (patch 1.0.41, dic 2020; alcune guide riportano ancora 1.000) (+100 a VIP15, +200 a VIP16), rigenerazione ~1 AP ogni ~45 s (stima community), si ferma al cap. Calcolo derivato: ~1.900-2.000 AP naturali al giorno senza bonus (86.400 s / ~45 s; 0->1.000 in ~12-12,5 h), cioe' il cap si riempie due volte al giorno: il bot deve spendere AP almeno ogni ~10-12 ore. |
| Golden Chest gratuita (Tavern) | circa ogni 48 ore (migliora con il livello della Tavern) |

Nota sul reset: media: nessuna fonte letta dice testualmente 'gli obiettivi giornalieri si azzerano alle 00:00 UTC'; lo confermano indirettamente il Mysterious Merchant che arriva alle 00:00 UTC, le chance giornaliere di Silk Road Speculators azzerate alle 00:00 UTC e l'avviso 'le date locali differiscono intorno al daily reset: usare il timer UTC'. Il bot deve leggere il countdown in gioco. Fonti: [heaven-guardian 2026-08-06](https://heaven-guardian.com/rise-of-kingdoms-courier-station-guide/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-shop-guide-dominate-maximize-benefits/); [theriagames 2025-02-12](https://theriagames.com/guide/rise-of-kingdoms-holy-sites-guide/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-maximize-action-points-dominate/).

## 1. Checklist giornaliera (ordine di esecuzione)

Priorita': **P0** = ogni sessione del bot; **P1** = una volta al giorno dopo il reset; **P2** = quando disponibile. Ogni voce: valore, regola if/then per il bot, conferma richiesta, fonti.

### 1. Mail e ricompense: posta di sistema/eventi/alleanza, login rewards, alliance gifts  `P0`

- **Reset/frequenza:** continuo; login rewards giornalieri — ogni sessione
- **Valore:** Le ricompense di molti eventi (es. Silk Road Speculators, ranking) arrivano via mail; gli alliance gifts (da forti, acquisti dei membri, attivita') contengono speedup, crediti, a volte VIP points e gemme (heaven-guardian, riseofkingdomsguides). 'Collect every free source' e' una priorita' F2P (riseofkingdomshandbook). Prima di lasciare un'alleanza riscuotere i suoi tesori (riseofkingdomsguides).
- **Regola bot:** IF ci sono mail con allegati THEN riscuoti tutti gli allegati (non cancellare mail non lette di leader/ufficiali: vanno mostrate all'utente). IF ci sono alliance gifts THEN aprili tutti. IF compare un login reward/calendario THEN riscuoti. IF una mail chiede azioni (registrazione Ark, regole MGE, KvK) THEN segnala all'utente.
- **Conferma:** azione base no; dettaglio: no (solo lettura/riscossione); segnalare all'utente le mail con istruzioni
- **Fonti:** [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-f2p-guide); [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/how-do-you-get-vip-points-in-rise-of-kingdoms/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-gems/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-life-hacks-tips-and-tricks/)

### 2. Riscuotere lavori finiti e tenere SEMPRE occupate le code: costruzione (1-2 builder), ricerca (Academy), addestramento, cura  `P0`

- **Reset/frequenza:** continuo (ogni sessione) — ogni sessione
- **Valore:** Le code inattive sono la perdita piu' grave: 'Research, always running. Never let the Academy idle' e 'City Hall, always upgrading' sono le prime due priorita' F2P (riseofkingdomshandbook). Tenere due builder attivi e l'Academy sempre al lavoro e' la routine base (heaven-guardian). Prima di partire con un timer lungo: runa giusta + titolo (Architect/Scientist/Duke) + buff di regno, perche' i bonus si applicano solo all'avvio della coda (heaven-guardian). Alliance Help riduce costruzione, ricerca e cure ma NON l'addestramento (heaven-guardian).
- **Regola bot:** IF una coda (builder/Academy/caserma/ospedale) e' libera THEN avvia il prossimo elemento del piano 'growth' (prerequisito del prossimo City Hall > Academy > Alliance Center > Hospital > edifici truppe > economia). IF il timer previsto > 8h THEN prima raccogli la runa corrispondente se disponibile (vedi voce Holy Sites e rune) e, se l'utente ha abilitato le richieste in chat, chiedi il titolo; POI avvia. IF la coda e' di costruzione/ricerca/cura THEN chiedi subito Alliance Help. NEVER usare gemme per completare o per affittare il secondo builder. IF l'upgrade consuma Master's Blueprint, Books of Covenant o Arrows of Resistance THEN chiedi conferma.
- **Conferma:** azione base no; dettaglio: solo se consuma materiali rari (Master's Blueprint, Books of Covenant, Arrows of Resistance) o speedup oltre la soglia fissata dall'utente
- **Fonti:** [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-f2p-guide); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-titles-guide-to-maximize-your-buffs/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/)

### 3. Alliance Help: dare aiuto a tutti e chiedere aiuto sulle proprie code  `P0`

- **Reset/frequenza:** continuo; cap crediti giornaliero (reset giornaliero) — ogni sessione
- **Valore:** Ogni tap riduce i timer degli alleati e da' Individual Credits: fino a 10.000 Individual Credits al giorno dall'Alliance Help (heaven-guardian). In un'alleanza attiva l'aiuto vale 'diverse ore al giorno di speedup gratuiti' (riseofkingdomshandbook). Il numero di aiuti ricevibili cresce con l'Alliance Center (30 aiuti a livello 25 secondo heaven-guardian).
- **Regola bot:** IF compare l'icona Alliance Help THEN premi 'Help All'. IF hai appena avviato costruzione/ricerca/cura THEN premi 'Request Help'. IF una coda aiutabile e' in corso THEN non usare speedup finche' il contatore di aiuti non e' esaurito.
- **Conferma:** azione base no
- **Fonti:** [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/)

### 4. Ospedale: curare i feriti e mantenere capacita' sufficiente  `P0`

- **Reset/frequenza:** continuo — ogni sessione
- **Valore:** I feriti che non entrano in ospedale muoiono (riseofkingdomshandbook). Tenere l'ospedale abbastanza grande per una marcia piena di feriti. La cura costa risorse e tempo; Alliance Help riduce le cure; France +20% velocita' di cura, Korea/Byzantium +15% capacita'. Healing speedup: riserva permanente per la guerra (riseofkingdomshandbook).
- **Regola bot:** IF ci sono feriti in ospedale AND le risorse bastano THEN avvia la cura (a lotti se in guerra, per sfruttare piu' Alliance Help) e chiedi aiuto. IF la capacita' libera < dimensione di una marcia THEN non avviare combattimenti (barbari alti, forti, eventi) finche' non curi. IF la capacita' totale < una marcia piena THEN aggiungi upgrade Hospital al piano. NEVER curare con gemme. Healing speedup solo in guerra/KvK o su istruzione dell'utente.
- **Conferma:** azione base no; dettaglio: no per curare con risorse; si' per usare healing speedup fuori dalla guerra
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-speedups-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/); [heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/)

### 5. Marce di raccolta sempre fuori (nodi mappa, preferibilmente dentro il territorio dell'alleanza)  `P0`

- **Reset/frequenza:** continuo — ogni sessione
- **Valore:** La raccolta sulla mappa produce 'un ordine di grandezza' piu' delle fattorie in citta' (riseofkingdomshandbook). Dentro il territorio dell'alleanza +25% velocita' di raccolta (heaven-guardian, riseofkingdomsguides). Truppa ideale: T1 Siege (carico 20 contro 5-7 delle altre T1). Online: nodi vicini; offline: nodi di livello alto (allclash). Contano solo i talenti del comandante primario.
- **Regola bot:** IF una marcia e' libera AND nessun evento/uso pianificato la richiede THEN invia un raccoglitore (comandante specializzato scelto a mano: Cleopatra/Matilda pietra, Constance legno, Gaius Marius cibo...) con T1 Siege sul nodo della risorsa piu' carente per il prossimo upgrade; IF l'utente sara' offline a lungo THEN scegli nodi di livello alto. IF il nodo e' fuori territorio in zona ostile o in guerra THEN preferisci il territorio alleanza. IF su un nodo c'e' gia' la marcia di un altro giocatore THEN NON attaccarla.
- **Conferma:** azione base no; dettaglio: no (attaccare una marcia di raccolta altrui = attacco a giocatore -> conferma)
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/farming-gathering-guide/); [allclash 2020-02-21](https://www.allclash.com/the-only-rise-of-kingdoms-gathering-guide-you-really-need/); [heaven-guardian 2026-08-12](https://heaven-guardian.com/rise-of-kingdoms-gathering-guide-dominate-resources/)

### 6. Barbari con AP naturali (mai lasciare la barra AP al massimo)  `P0`

- **Reset/frequenza:** continuo (AP rigenerano ~1 ogni 45 s fino al cap ufficiale di 1.500) — ogni sessione
- **Valore:** Gli AP si fermano al cap: spenderli regolarmente e' gratis (heaven-guardian, riseofkingdomshandbook). Costo base 50 AP per barbaro, -2 AP per ogni attacco consecutivo senza rientrare fino a -10; talento Insight fino a -9/-10 AP (conflitto). Con 1.000 AP ~25 barbari in catena senza Insight; ~1.900-2.000 AP naturali al giorno (calcolo derivato) = al massimo ~45-50 barbari/giorno in catena continua. Ricompense: XP comandante, risorse, speedup, gemme (barbari alti), Arrows of Resistance. Gli oggetti AP (bottled AP) vanno conservati per eventi ad alto valore (Lohar's Trial, Marauders/Eve of the Crusade, Karuak, fase barbari MGE).
- **Regola bot:** IF AP >= 50 + (AP che si rigenereranno prima della prossima sessione) OR AP >= 80% del cap THEN attacca barbari in catena con il comandante Peacekeeping (primario con Insight) senza rientrare in citta' tra un attacco e l'altro; scegli il livello piu' alto che batti senza perdite rilevanti; IF l'ospedale ha feriti THEN curali prima. IF e' attivo un evento che premia gli AP (Lohar's Trial, fase barbari MGE, Marauders, Karuak) THEN concentra gli AP li'. NEVER comprare AP con gemme. Oggetti AP: usarli solo durante questi eventi e solo se previsto dal piano utente.
- **Conferma:** azione base no; dettaglio: no per AP naturali; si' per consumare oggetti AP fuori dagli eventi pianificati
- **Fonti:** [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-dominate-barbarians-forts-guide/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-maximize-action-points-dominate/); [rokdbot 2026-06-13](https://rokdbot.com/en/blog/action-points-management-guide-rok-2026); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-barbarians-and-barbarian-forts/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-karuak-ceremony-guide)

### 7. Speedup: accumulare e usarli solo con una regola  `P0`

- **Reset/frequenza:** continuo — ad ogni decisione di completamento
- **Valore:** Gli speedup non scadono e non si possono rubare (riseofkingdomshandbook). Usarli durante eventi a punti (MGE, Power stage) vale due volte. Ordine: titolo/runa -> Alliance Help -> speedup specifici -> Universal solo se necessario (heaven-guardian). Eccezioni: cure in guerra, sblocco di un requisito (tier truppe, coda di marcia), Academy che resterebbe ferma, prontezza pre-KvK (riseofkingdomshandbook, heaven-guardian).
- **Regola bot:** IF un evento a punti premia quella coda (MGE training/power, Zenith) THEN usa gli speedup del tipo giusto fino al target fissato dall'utente. ELSE IF lo speedup sblocca subito un traguardo (coda di marcia, tier truppe, prerequisito City Hall) THEN usalo. ELSE tienili. Usa sempre prima gli speedup specifici, poi Universal; abbina la durata al timer residuo.
- **Conferma:** azione base no; dettaglio: si' oltre una soglia configurabile (es. >24 h di speedup in una volta o qualsiasi uso di Universal fuori evento)
- **Fonti:** [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-speedups-guide); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/)

### 8. VIP: riscuotere i VIP points giornalieri e il forziere VIP gratuito  `P1`

- **Reset/frequenza:** giornaliero (ogni 24 h; streak consecutiva) — giornaliero
- **Valore:** Unica vera fonte gratuita continua di VIP: i claim consecutivi salgono fino a 200 VIP points/giorno (heaven-guardian; riseofkingdomsguides: '200 VIP points ogni 24 ore'). ~6.000 punti al mese. Il forziere giornaliero migliora con il livello VIP (VIP 10/12/14 = 1/2/3 Universal Legendary Sculptures al giorno). Altre fonti gratuite: Alliance Shop 100 VIP points per 50.000 Individual Credits, alliance gifts, Mysterious Caves (VIP points tra i premi possibili).
- **Regola bot:** IF il claim VIP giornaliero o il forziere VIP gratuito e' disponibile THEN riscuoti (non saltare giorni: la streak aumenta il premio). NEVER convertire gemme in VIP points (1 gemma = 1 VIP point) ne' comprare pacchetti.
- **Conferma:** azione base no
- **Fonti:** [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-guide-level-up-fast-get-rewards/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/how-do-you-get-vip-points-in-rise-of-kingdoms/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-vip-levels-guide); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-scout-villages-caves-for-fast-growth/)

### 9. Obiettivi giornalieri (daily objectives) e forzieri attivita'  `P1`

- **Reset/frequenza:** giornaliero 00:00 UTC (vedi reset_reference) — giornaliero + controllo prima del reset
- **Valore:** Fonte costante di speedup e risorse; completare TUTTA la traccia, non solo i primi forzieri (heaven-guardian). Le quest giornaliere danno 100 gemme (riseofkingdomsguides). Attivita' tipiche: addestrare truppe, raccogliere, sconfiggere barbari, usare AP, aiutare l'alleanza, compiti di citta' (heaven-guardian). Sono anche la base di chiavi della Tavern e VIP point items (riseofkingdomshandbook).
- **Regola bot:** IF un forziere attivita' e' sbloccabile THEN riscuotilo subito. Pianifica la sessione in modo che le azioni gia' previste (raccolta, barbari, addestramento, aiuti) completino gli obiettivi. IF un obiettivo richiede di spendere gemme o comprare qualcosa THEN saltalo. Prima del reset (23:00-23:59 UTC) controlla forzieri non riscossi.
- **Conferma:** azione base no
- **Fonti:** [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-gems/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-tavern-keys-guide); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub)

### 10. Courier Station / Mysterious Merchant: comprare solo offerte pagate in Food/Wood + refresh gratuito  `P1`

- **Reset/frequenza:** arrivo 00:00 UTC + visite extra dopo addestramenti/costruzioni/barbari — dopo il reset + quando compare l'icona
- **Valore:** Il mercante arriva normalmente alle 00:00 UTC (sbloccato a City Hall 6): 16 offerte (4 risorse, 4 speedup, 4 boost, 4 altro). Le offerte in Food/Wood (sconto ~10-40%) sono il miglior valore: speedup Universal/Research prima, poi Training/Healing, pacchetti risorse (restano protetti in inventario). 1 refresh gratuito per visita; i refresh successivi costano 100/200/300/400 gemme (heaven-guardian). Anche i token Enhanced Gathering (+50% per 8 h o 24 h) si comprano con risorse (riseofkingdomsguides).
- **Regola bot:** IF il mercante e' presente THEN compra tutte le offerte pagate in Food o Wood che sono speedup (Universal > Research > Training > Healing > Building) purche' le risorse restanti coprano il prossimo upgrade pianificato; poi usa il refresh GRATUITO e ripeti. Pacchetti risorse/boost raccolta: compra solo se colmano una carenza o se verranno usati a breve. NEVER offerte in gemme, NEVER refresh a pagamento.
- **Conferma:** azione base no
- **Fonti:** [heaven-guardian 2026-08-06](https://heaven-guardian.com/rise-of-kingdoms-courier-station-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/farming-gathering-guide/)

### 11. Tavern: aprire le casse gratuite (Silver e Golden) e le Silver Keys  `P1`

- **Reset/frequenza:** Silver: giornaliero; Golden gratuita: circa ogni 48 h — giornaliero
- **Valore:** Secondo riseofkingdomshandbook: 5 aperture Silver gratuite al giorno (comandanti elite/advanced, sculture, Starlight Sculptures, speedup, Tomes of Knowledge) e circa 1 Golden gratuita ogni 2 giorni, piu' frequente salendo di livello la Tavern. 'Not opening them is the only genuine mistake'. Golden Keys: aprirle quando un evento premia l'apertura di forzieri (valgono due volte); nessuna ragione meccanica per accumularle altrimenti.
- **Regola bot:** IF una cassa Silver o Golden gratuita e' disponibile THEN aprila. IF hai Silver Keys THEN aprile ogni giorno. IF hai Golden Keys AND c'e' un evento attivo che premia le aperture THEN aprile; ELSE conservale (chiedi conferma all'utente per aprirle fuori evento). NEVER comprare chiavi con gemme.
- **Conferma:** azione base no; dettaglio: no per le gratuite e le Silver; si' per spendere Golden Keys fuori da eventi che le premiano
- **Fonti:** [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-tavern-keys-guide); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-shop-guide-dominate-maximize-benefits/)

### 12. Expedition: forziere giornaliero, stage non completati, acquisti nel Medal Store  `P1`

- **Reset/frequenza:** forziere giornaliero; negozio con limiti giornalieri/rotazioni — giornaliero
- **Valore:** Modalita' PvE permanente: le truppe sono simulate, nulla muore e nulla va in ospedale, si puo' ritentare all'infinito (riseofkingdomshandbook, heaven-guardian). Le stelle/progressi aumentano il premio giornaliero ricorrente. Medals of the Conqueror -> sculture (Aethelflaed con limite giornaliero, Constance, epico in rotazione). Marce disponibili: 1, 2 dallo stage 6, 3 dal 16, 4 dal 26, 5 dal 41; salti di difficolta' agli stage 11/21/31/41/51.
- **Regola bot:** IF il premio giornaliero Expedition e' disponibile THEN riscuoti. IF c'e' uno stage non completato o con <3 stelle THEN tenta con la coppia piu' sviluppata (tank avanti per primo, focus fire su un bersaglio), massimo N tentativi per sessione (N configurabile, es. 5). IF nel Medal Store ci sono sculture Aethelflaed non ancora comprate oggi AND Aethelflaed non e' expertised THEN comprale con le medaglie (priorita' secondo heaven-guardian; handbook indica l'epico in rotazione: vedi conflicts). Applicare sculture alle skill -> conferma.
- **Conferma:** azione base no; dettaglio: no per tentativi e acquisti con medaglie; si' per spendere sculture sulle skill
- **Fonti:** [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-expedition-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-expedition-guide-tips-rewards/)

### 13. Sculture gratuite: riscuoterle tutte, non spenderle senza piano  `P1`

- **Reset/frequenza:** giornaliero (forziere VIP, Tavern, negozi con limiti giornalieri) — giornaliero
- **Valore:** Fonti gratuite: forziere VIP giornaliero (VIP 10/12/14 = 1/2/3 Universal Legendary Sculptures al giorno), casse Tavern (Silver/Golden, Starlight Sculptures), Expedition Medal Store (Aethelflaed con limite giornaliero, Constance, epico in rotazione), Alliance Shop (sculture pagate in Individual Credits: prima priorita' del negozio per riseofkingdomshandbook), negozi degli eventi, Ark of Osiris, MGE. Un leggendario richiede fino a 690 sculture per 5/5/5/5 dopo l'evocazione; alcuni (Minamoto, Aethelflaed, Hannibal) non accettano le Universal.
- **Regola bot:** IF una fonte gratuita di sculture e' disponibile oggi (forziere VIP, casse gratuite, negozio con limite giornaliero pagabile in medaglie/crediti/valuta evento) THEN riscuoti/compra per il comandante indicato dall'utente. NEVER applicare Universal Legendary Sculptures o sculture specifiche alle skill senza conferma; NEVER comprarle con gemme (VIP 13 Shop: 2.000 gemme l'una).
- **Conferma:** azione base no; dettaglio: si' per spenderle; no per riscuoterle
- **Fonti:** [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-commander-sculptures-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-guide-level-up-fast-get-rewards/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-tavern-keys-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-expedition-guide-tips-rewards/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-shop-guide); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-shop-guide-dominate-maximize-benefits/)

### 14. Donazioni alla tecnologia dell'alleanza  `P1`

- **Reset/frequenza:** tentativi che si ricaricano nel tempo (continuo) — 2-3 volte al giorno
- **Valore:** Danno Individual Credits (e Alliance Credits all'alleanza); i tentativi si ricaricano nel tempo: tornare durante il giorno e non lasciarli al massimo (heaven-guardian). La tecnologia d'alleanza da' bonus a costruzione, ricerca, addestramento, cure e raccolta (heaven-guardian).
- **Regola bot:** IF ci sono tentativi di donazione disponibili THEN dona alla tecnologia segnata/raccomandata dai leader (la risorsa richiesta, NON sempre oro) purche' non intacchi le risorse del prossimo upgrade. NEVER donare con gemme.
- **Conferma:** azione base no
- **Fonti:** [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/); [heaven-guardian 2026-08-12](https://heaven-guardian.com/rise-of-kingdoms-gathering-guide-dominate-resources/)

### 15. Holy Sites: guardiani (XP comandante senza AP) e rune  `P1`

- **Reset/frequenza:** guardiani alle 00:00 e 12:00 UTC per 11 h (theriagames) / ciclo di 12 h (heaven-guardian); runa: durata ~1 h — 2 volte al giorno (dopo 00:00 e 12:00 UTC)
- **Valore:** I guardiani intorno a Sanctum/Altar/Shrine danno XP comandante senza costo AP e droppano rune; le alleanze organizzano 'guardian run' (heaven-guardian). Rune: solo una attiva alla volta (una nuova sostituisce la vecchia), durata ~1 h; bianca ~3%, verde ~7%, blu ~10%, viola ~15%, arancio ~20%. Le rune di sviluppo (costruzione/ricerca/addestramento/cura) contano all'AVVIO della coda; raccolta/AP/XP/combattimento contano mentre sono attive. Le rune raccolta valgono sui nodi mappa, non sulla produzione in citta'.
- **Regola bot:** IF l'alleanza/regno annuncia un guardian run THEN partecipa con il comandante da livellare rispettando le regole (dimensione marcia). IF stai per avviare una coda lunga AND c'e' una runa del tipo giusto raggiungibile senza attraversare territorio ostile THEN mandala a prendere con una marcia veloce (T1 cavalleria), verifica che il timer sia ridotto, avvia la coda. IF hai gia' una runa attiva ancora utile THEN non raccoglierne un'altra. IF nessuna coda lunga e' pianificata AND tutte le marce raccolgono THEN runa raccolta generica; IF farm barbari AND AP sotto il cap THEN runa AP recovery.
- **Conferma:** azione base no; dettaglio: no (PvE); evitare zone ostili
- **Fonti:** [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/); [theriagames 2025-02-12](https://theriagames.com/guide/rise-of-kingdoms-holy-sites-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-runes/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/)

### 16. Scout: villaggi tribali (Tribal Villages) e caverne (Mysterious Caves)  `P1`

- **Reset/frequenza:** continuo finche' c'e' nebbia (una tantum per luogo) — ogni sessione finche' c'e' nebbia
- **Valore:** Villaggi: si riscuotono appena scoperti (cibo/legno, truppe T1, speedup brevi, Kingdom Maps, tecnologia economica di basso livello). Caverne: vanno investigate da uno scout (Low/Medium/High) -> risorse, gemme, speedup, VIP points, chiavi, oggetti AP, oggetti comandante; lo scout non rischia nulla. Scout: 1 all'inizio, 2 a Scout Camp 5, 3 a Scout Camp 11. Kingdom Map = libera un'area 10x10 casuale (heaven-guardian).
- **Regola bot:** IF uno scout e' fermo AND c'e' nebbia THEN mandalo a esplorare in una direzione diversa dagli altri (percorsi lunghi prima di andare offline). IF lo Scouting Report mostra villaggi non riscossi THEN riscuotili. IF ci sono caverne scoperte non investigate THEN investigale in ordine High > Medium > Low. IF hai Kingdom Maps AND resta molta nebbia THEN usale.
- **Conferma:** azione base no
- **Fonti:** [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-scout-villages-caves-for-fast-growth/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-life-hacks-tips-and-tricks/)

### 17. Armamenti: State Forum -> Travel e Dispatch giornalieri  `P1`

- **Reset/frequenza:** giornaliero (Luck e chance si azzerano al reset del server) — giornaliero
- **Valore:** Travel sbloccato a State Forum 1 (5 viaggi/giorno, fino a 20 al livello 24-25), 20 AP a viaggio ('Travel x10' = 200 AP). Dispatch sbloccato a State Forum 10 (3/giorno, fino a 8), 30-150 AP a seconda della rarita'; dopo 15 dispatch riusciti la Dispatch Commendation chest garantisce un armamento Epic/Legendary o 100 Sage's Testimony. Premi: armamenti e Sage's Testimony (serve per salire di State Forum). Dal 1.0.79 si scelgono 3 formazioni preferite. Oltre i viaggi gratuiti con AP esistono viaggi extra in gemme: vietati.
- **Regola bot:** IF lo State Forum ha viaggi con AP rimasti oggi AND (AP disponibili - 20*viaggi) >= riserva AP per i barbari/eventi THEN usa 'Travel' (x10 se ne restano >=10) con i comandanti raccomandati del giorno. IF ci sono Dispatch disponibili THEN usa 'Quick Dispatch' soddisfacendo i requisiti. Imposta prima le 3 formazioni preferite scelte dall'utente. NEVER viaggi extra in gemme. Riciclo/Transmutation/Conversion degli armamenti e spesa di Sage's Testimony per l'upgrade -> conferma.
- **Conferma:** azione base no; dettaglio: no per Travel/Dispatch con AP; si' per riciclare armamenti o consumare Sage's Testimony, Transmutation Stones, Conversion Stones
- **Fonti:** [touchscreengaming 2025-10-10](https://touchscreengaming.com/formations-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-1-0-91-moon-and-star-update/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/formations-armaments-and-inscriptions-guide-rok/)

### 18. Sunset Canyon: usare i tentativi gratuiti giornalieri  `P1`

- **Reset/frequenza:** giornaliero (stagione di 7 giorni) — giornaliero
- **Valore:** Truppe simulate, nessuna perdita reale; formato documentato: 5 tentativi gratuiti al giorno e stagione di 7 giorni (riseofkingdomshandbook). Fonte di materiali equipaggiamento e premi F2P (riseofkingdomshandbook). I Challenge Tickets extra sono una risorsa separata.
- **Regola bot:** IF ci sono tentativi gratuiti rimasti oggi THEN sfida l'avversario con la formazione salvata (ispeziona la difesa avversaria e scegli quello con potenza/formazione piu' debole); usa tutti i tentativi prima del reset. NEVER comprare tentativi/ticket con gemme; usa i Challenge Tickets gia' posseduti solo se l'utente lo consente.
- **Conferma:** azione base no
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-sunset-canyon-guide); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-f2p-guide)

### 19. Blacksmith: tenere attiva la produzione di materiali equipaggiamento  `P1`

- **Reset/frequenza:** continuo — ogni sessione (dopo CH16)
- **Valore:** Il Blacksmith (City Hall 16) e' anche un generatore passivo di materiali da non lasciare mai fermo (riseofkingdomshandbook); la forgiatura costa molto oro.
- **Regola bot:** IF la produzione di materiali del Blacksmith e' ferma THEN avviala sul materiale che serve al prossimo pezzo pianificato dall'utente. Forgiare o smontare equipaggiamento -> conferma.
- **Conferma:** azione base no; dettaglio: no per produrre materiali; si' per forgiare/smontare
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide-hub); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-resources-guide-hub)

### 20. Peerless Scholar (Lyceum of Wisdom): Preliminary nei giorni feriali  `P1`

- **Reset/frequenza:** lun-ven, entro le 23:00 UTC; Midterm sabato 02:30 o 12:30 UTC; Final ultimo sabato del mese 14:30 UTC — lun-ven
- **Valore:** Quiz gratuito (City Hall 10): 10 domande senza timer, 6 corrette per qualificarsi al Midterm, 3 aiuti d'alleanza; premi gemme, speedup, forzieri d'alleanza (riseofkingdomshandbook, heaven-guardian).
- **Regola bot:** IF e' un giorno feriale AND Preliminary non completato AND ora < 23:00 UTC THEN rispondi alle 10 domande usando il database di risposte verificato; IF una domanda non e' nel database THEN usa un aiuto d'alleanza o salta. Midterm/Final a tempo: solo se il bot risponde entro 10-15 s in modo affidabile, altrimenti avvisa l'utente.
- **Conferma:** azione base no
- **Fonti:** [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-peerless-scholar-answers/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-lyceum-of-wisdom-guide)

### 21. Eventi attivi: leggere il pannello Events e fare le azioni gratuite che danno punti  `P1`

- **Reset/frequenza:** secondo il countdown UTC di ogni evento — ogni sessione
- **Valore:** Le date non sono uguali per tutti i regni: l'autorita' e' il pannello Events in gioco con il suo countdown UTC (heaven-guardian, riseofkingdomshandbook). Per F2P contano milestone garantite, eventi d'alleanza e attivita' che coincidono con la crescita normale.
- **Regola bot:** IF un evento e' attivo THEN applica le 'bot_actions' della voce corrispondente in 'events'; IF un premio e' gia' sbloccato THEN riscuotilo subito; IF un evento chiede gemme THEN ignoralo (tranne componenti gratuite: spin gratuito, missioni gratuite). IF l'evento richiede PvP (Eliminating Enemies, Ark of Osiris, Olympia) THEN chiedi conferma.
- **Conferma:** azione base no; dettaglio: si' per qualsiasi azione PvP o consumo di materiali rari
- **Fonti:** [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub)

### 22. Alliance Resource Center: raccogliere nei centri risorse dell'alleanza  `P2`

- **Reset/frequenza:** quando l'alleanza ne piazza uno — quando disponibile
- **Valore:** I resource point dell'alleanza sono nodi sicuri ad alta resa non accessibili da soli (riseofkingdomshandbook); il territorio d'alleanza da' +25% e parte della raccolta (+5% secondo allclash) va al deposito dell'alleanza. Sono piazzati dai leader con Alliance Credits (heaven-guardian).
- **Regola bot:** IF esiste un Alliance Resource Center della risorsa che ti serve AND hai una marcia libera THEN invia il raccoglitore migliore per quella risorsa (vedi task 3). IF i leader indicano regole (turni, limiti) THEN rispettale.
- **Conferma:** azione base no
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/); [allclash 2020-02-21](https://www.allclash.com/the-only-rise-of-kingdoms-gathering-guide-you-really-need/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/farming-gathering-guide/)

### 23. Costruzioni dell'alleanza (flag/fortress/resource center in costruzione)  `P2`

- **Reset/frequenza:** cap crediti giornaliero (reset giornaliero) — quando c'e' un cantiere
- **Valore:** Contribuire con truppe alle costruzioni dell'alleanza da' fino a 20.000 Individual Credits al giorno (heaven-guardian). Gli Individual Credits comprano nell'Alliance Shop: Civilization Change (2.000.000), VIP points (100 per 50.000), speedup, teletrasporti, Passport Pages (600.000).
- **Regola bot:** IF un edificio dell'alleanza e' in costruzione AND hai una marcia libera AND non hai raggiunto il cap giornaliero THEN invia una marcia di truppe economiche; IF i leader chiedono di completarlo in fretta THEN manda tutto quello che serve; IF il cap e' raggiunto THEN richiama la marcia e rimettila in raccolta.
- **Conferma:** azione base no
- **Fonti:** [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/); [heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-guide-level-up-fast-get-rewards/)

### 24. Gem deposits: raccolta di gemme sulla mappa con marce libere (opzionale)  `P2`

- **Reset/frequenza:** continuo — quando ci sono marce libere
- **Valore:** Serve la ricerca economica Jewelry (dopo Multilayer Structure); Cutting & Polishing fino a +35% velocita' di raccolta gemme a livello 10. Depositi livello 1 = 10 gemme, livello 2 = 20 gemme. Le gemme raccolte valgono 150 punti l'una nella fase raccolta MGE. Priorita': prima il forziere da 100 attivita' (100 gemme/giorno), gli eventi e gli AP; poi marce libere sulle gemme, senza lasciare scoperta l'economia normale.
- **Regola bot:** IF Jewelry e' ricercata AND ci sono marce libere dopo aver coperto le risorse del prossimo upgrade THEN manda un raccoglitore (talenti Gathering sul primario) sul deposito di gemme piu' vicino di livello >= 2 e, finito, spostalo direttamente al successivo. NEVER spendere le gemme raccolte (le decide l'utente).
- **Conferma:** azione base no
- **Fonti:** [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-gem-farming-guide-best-commanders-tips/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-win-mightiest-governor-event/)

### 25. Titoli di regno (Architect/Scientist/Duke) prima delle code lunghe  `P2`

- **Reset/frequenza:** a richiesta — per code lunghe
- **Valore:** Architect +10% costruzione, Scientist +5% ricerca (+10% raccolta oro), Duke +10% addestramento (+5% difesa), Kingdom Queen +15% raccolta, Prime Minister +15% produzione +10% costruzione, Justice +5% attacco +10% marcia. Il titolo deve essere attivo PRIMA di avviare la coda; va rilasciato dopo (heaven-guardian, riseofkingdomshandbook). Si chiede in chat condividendo le coordinate.
- **Regola bot:** IF l'utente ha abilitato le richieste di titolo AND stai per avviare una coda > 24 h THEN posta coordinate + titolo nel canale del regno, attendi l'icona del titolo, verifica il timer ridotto, avvia, poi scrivi che hai finito. ELSE avvia senza titolo (non bloccare la coda piu' di ~15 minuti in attesa).
- **Conferma:** azione base si'; dettaglio: si' (scrive in chat a nome dell'utente)
- **Fonti:** [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-titles-guide-to-maximize-your-buffs/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-kingdom-titles-guide)

### 26. Negozi settimanali: VIP Shop (solo articoli in risorse) e Alliance Shop (Individual Credits)  `P2`

- **Reset/frequenza:** VIP Shop: lunedi' 00:00 UTC; Alliance Shop: stock deciso dai leader — settimanale (lunedi')
- **Valore:** VIP Shop con risorse: Basic AP Recovery (100 AP) 12.000 Food x30/settimana (VIP 2), Universal Speedup 5m 7.000 Food x50 (VIP 3), Brand-new Starlight Sculpture 60.000 Food x20 (VIP 4), Dazzling Starlight Sculpture 400.000 Wood x5 (VIP 5); il resto e' in gemme (heaven-guardian). Alliance Shop con Individual Credits: VIP points, speedup, teletrasporti, Civilization Change, Passport Pages (heaven-guardian).
- **Regola bot:** IF e' passato il reset del lunedi' AND il VIP level lo consente THEN compra gli articoli pagati in Food/Wood (AP Recovery, Universal 5m, Starlight se servono ancora stelle) senza scendere sotto la riserva risorse del prossimo upgrade. IF Individual Credits sufficienti THEN proponi all'utente (conferma) l'acquisto secondo il piano: Civilization Change se pianificato, VIP points se vicino a VIP 6/10, speedup. NEVER articoli in gemme.
- **Conferma:** azione base no; dettaglio: no per articoli in risorse; si' per spendere Individual Credits (Passport, Civilization Change, teletrasporti)
- **Fonti:** [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-shop-guide-dominate-maximize-benefits/); [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/)

### 27. Gift codes (codici regalo)  `P2`

- **Reset/frequenza:** occasionale (quando esce un codice ufficiale) — occasionale
- **Valore:** Si riscattano da avatar -> Settings -> Redeem (icona regalo) -> Exchange; il premio arriva in mail; ogni codice vale una volta per governatore. Le liste 'attive' dei siti sono in disaccordo (vedi conflicts): trattarli come bonus.
- **Regola bot:** IF l'utente fornisce un codice (o compare in un annuncio ufficiale in gioco) THEN riscattalo una volta e leggi il messaggio di esito; poi riscuoti la mail. NEVER inserire credenziali in siti terzi.
- **Conferma:** azione base no
- **Fonti:** [heaven-guardian 2026-09-18](https://heaven-guardian.com/rise-of-kingdoms-codes/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-gift-codes)

### 28. Fine sessione / prima di andare offline: sicurezza e code lunghe  `P0`

- **Reset/frequenza:** ogni volta che il bot si ferma — fine sessione
- **Valore:** Non tenere risorse aperte oltre il limite protetto (Storehouse): il surplus si puo' saccheggiare; tenere i pacchetti risorse chiusi finche' servono; scudo o riparo prima di uscire nei periodi di conflitto (riseofkingdomshandbook, heaven-guardian, riseofkingdomsguides). Avviare timer lunghi e mandare le marce in raccolta prima di uscire (riseofkingdomshandbook, heaven-guardian).
- **Regola bot:** IF le risorse aperte > capacita' protetta dello Storehouse THEN spendile in code utili (costruzione/ricerca/addestramento) o convertile in pacchetti al mercante; NON aprire pacchetti risorse se non servono subito. IF ci sono code libere THEN avvia i timer piu' lunghi. IF marce libere THEN raccolta su nodi alti. IF scout liberi THEN percorsi lunghi. IF e' in corso guerra/KvK o sei stato scoutato/attaccato di recente THEN chiedi all'utente se attivare uno scudo (Peace Shield).
- **Conferma:** azione base no; dettaglio: si' per attivare scudi o teletrasporti
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/); [heaven-guardian 2026-08-06](https://heaven-guardian.com/rise-of-kingdoms-courier-station-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/)

### Settimanale

- **settimanale:** Controllare la lista eventi attivi e annunciati, gli annunci d'alleanza (registrazioni, orari fissi), scegliere gli eventi che servono all'obiettivo dell'account e riservare solo le risorse necessarie ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub))
- **lunedi' 00:00 UTC:** Dopo il reset del lunedi' 00:00 UTC: VIP Shop (solo articoli in risorse); rivedere le riserve di speedup per tipo; identificare il prossimo upgrade importante; risparmiare AP se si avvicina un evento migliore (Marauders) ([heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-shop-guide-dominate-maximize-benefits/))
- **sabato:** Sabato: Midterm del Peerless Scholar (02:30 o 12:30 UTC, una sola sessione) se qualificati; ultimo sabato del mese: Final alle 14:30 UTC ([heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-peerless-scholar-answers/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-lyceum-of-wisdom-guide))
- **rotazione decisa dai leader:** Alliance Shop: controllare lo stock (le sculture ruotano) e mantenere una riserva di Individual Credits (Passport Pages, Civilization Change) ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-shop-guide); [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/))

## 2. Priorita' di crescita

### 2.1 Edifici

- City Hall e' la radice: ogni edificio e' limitato al suo livello. Prima i prerequisiti diretti del prossimo City Hall, poi Academy, poi Hospital, poi edifici truppe; edifici risorse per ultimi (la raccolta sulla mappa produce molto di piu'). ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/))
- Controllare i prerequisiti del livello successivo PRIMA che finisca l'upgrade corrente; un builder sul blocco immediato, l'altro sul ramo successivo (pianificare due livelli avanti). Il Wall e' prerequisito di quasi ogni livello. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-city-hall-requirements); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/))
- Non livellare tutto in modo uniforme ne' tutti e quattro gli edifici truppe: sviluppare quello del tipo di truppa principale; i doppioni (fattorie, ospedali) non servono tutti a 25 nemmeno per il T5. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide-hub))
- Alliance Center vicino al City Hall: aumenta gli aiuti ricevibili (30 a livello 25) e i rinforzi; non aumenta la capacita' dei rally (Castle). ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/))
- Hospital: capacita' almeno pari a una marcia piena di feriti prima di combattere; Storehouse quando si accumulano risorse (sopra il limite protetto si viene saccheggiati). ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide-hub); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub))
- Castle e Watchtower: accumulare presto Books of Covenant (forti barbari, 20.095 per Castle 1->25) e Arrows of Resistance (barbari/Lohar): diventano il collo di bottiglia per Academy 25/T5. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-barbarians-and-barbarian-forts/))
- Master's Blueprint: richiesto per ogni edificio 24->25 (City Hall, Academy...); heaven-guardian indica lo Shop in gemme come fonte: per il bot e' un blocco (vedi gaps) e ogni uso richiede conferma. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/))

**Regola bot:** IF un builder e' libero THEN (1) prerequisito diretto mancante del prossimo City Hall; (2) City Hall se tutti i prerequisiti sono pronti e le risorse bastano; (3) Academy fino al livello del City Hall; (4) prerequisito del livello ancora successivo; (5) Alliance Center; (6) Hospital se capacita' < una marcia; (7) edificio del tipo di truppa principale; (8) Storehouse se le risorse tenute superano la protezione; (9) edifici risorse solo se nient'altro e' utile. NEVER gemme. Upgrade che consumano Master's Blueprint/Books of Covenant/Arrows of Resistance -> conferma.

**Traguardi del City Hall** ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-city-hall-requirements); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide-hub); [heaven-guardian 2026-08-06](https://heaven-guardian.com/rise-of-kingdoms-courier-station-guide/)):

- CH5: seconda coda di marcia
- CH6: Courier Station (Mysterious Merchant)
- CH8: progressione Academy per ricerca T2
- CH10: Lyceum of Wisdom (Peerless Scholar); oggetto Civilization Change gratuito (heaven-guardian)
- CH11: terza coda di marcia
- CH16: progressione per ricerca T3; Blacksmith; accesso a Ian's Ballads
- CH17: quarta coda di marcia; accesso a Golden Kingdom
- CH21: progressione per ricerca T4
- CH22: quinta coda di marcia
- CH25: livello massimo; percorso finale verso T5 (serve comunque Academy 25 + ricerca)

**Ordine edifici per livello di City Hall** — prerequisiti diretti, costo base e tempo base ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-city-hall-requirements)). Tempi base prima di bonus (VIP, tech, rune, titoli, civilta', Alliance Help). Il handbook avverte che i tempi base pubblicati per i livelli alti sono incoerenti tra fonti: usare il timer mostrato in gioco.

| CH | Prima costruisci | Food | Wood | Stone | Extra | Tempo base | Capacita' truppe CH | Traguardo |
|---|---|---|---|---|---|---|---|---|
| 2 | — | 3.5K | 3.5K | — | — | 2 s | 3.000 |  |
| 3 | — | 6.5K | 6.5K | — | — | 5 min | 4.000 |  |
| 4 | Wall 3 | 11.8K | 11.8K | — | — | 20 min | 5.000 |  |
| 5 | Wall 4, Hospital 4 | 21.3K | 21.3K | — | — | 1 h | 7.000 | seconda coda di marcia |
| 6 | Wall 5, Scout Camp 5 | 36.3K | 36.3K | 12K | — | 2 h | 9.000 | Courier Station (Mysterious Merchant) |
| 7 | Wall 6, Storehouse 6 | 54.4K | 54.4K | 19.2K | — | 5 h | 12.000 |  |
| 8 | Wall 7, Barracks 7 | 81.8K | 81.8K | 30.8K | — | 10 h | 15.000 | progressione Academy per ricerca T2 |
| 9 | Wall 8, Alliance Center 8 | 122.8K | 122.8K | 49.2K | — | 15 h | 19.000 |  |
| 10 | Wall 9, Academy 9 | 184.3K | 184.3K | 78.7K | — | 1 d | 23.000 | Lyceum of Wisdom (Peerless Scholar); oggetto Civilization Change gratuito (heaven-guardian) |
| 11 | Wall 10, Hospital 10 | 277.5K | 277.5K | 120K | — | 1 d 6 h | 28.000 | terza coda di marcia |
| 12 | Wall 11, Storehouse 11 | 417.5K | 417.5K | 180K | — | 1 d 16 h | 33.000 |  |
| 13 | Wall 12, Archery Range 12 | 627.5K | 627.5K | 270K | — | 2 d 2 h | 38.000 |  |
| 14 | Wall 13, Alliance Center 13, Trading Post 13 | 942.5K | 942.5K | 405K | — | 2 d 12 h | 44.000 |  |
| 15 | Wall 14, Scout Camp 14 | 1.415M | 1.415M | 607.5K | — | 2 d 22 h | 50.000 |  |
| 16 | Wall 15, Academy 15 | 2.1225M | 2.1225M | 912.5K | — | 4 d | 57.000 | progressione per ricerca T3; Blacksmith; accesso a Ian's Ballads |
| 17 | Wall 16, Hospital 16 | 3.185M | 3.185M | 1.37M | — | 4 d 20 h | 64.000 | quarta coda di marcia; accesso a Golden Kingdom |
| 18 | Wall 17, Storehouse 17 | 4.8M | 4.8M | 2.075M | — | 5 d 20 h | 72.000 |  |
| 19 | Wall 18, Stable 18 | 7.2M | 7.2M | 3.125M | — | 7 d | 80.000 |  |
| 20 | Wall 19, Alliance Center 19 | 10.8M | 10.8M | 4.7M | — | 8 d 6 h | 90.000 |  |
| 21 | Wall 20, Academy 20 | 16.2M | 16.2M | 7.05M | — | 11 d | 100.000 | progressione per ricerca T4 |
| 22 | Wall 21, Hospital 21 | 24.3M | 24.3M | 10.575M | — | 17 d 3 h | 110.000 | quinta coda di marcia |
| 23 | Wall 22, Storehouse 22 | 36.45M | 36.45M | 15.875M | — | 23 d 23 h | 120.000 |  |
| 24 | Wall 23, Siege Workshop 23 | 54.75M | 54.75M | 24M | — | 35 d 23 h | 130.000 |  |
| 25 | Wall 24, Trading Post 24 | 82.25M | 82.25M | 36M | 1 Master's Blueprint | 126 d 3 h | 150.000 | livello massimo; percorso finale verso T5 (serve comunque Academy 25 + ricerca) |

Schema per ogni livello: 1) prerequisiti diretti; 2) City Hall; 3) sul secondo builder Academy fino al livello del CH, poi Alliance Center / Hospital / edificio della truppa principale; 4) preparare i prerequisiti del livello successivo (es. a CH20 si preparano gia' Wall 21 e Hospital 21).

- Scout: 1 scout iniziale; 2 a Scout Camp 5; 3 a Scout Camp 11 ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-scout-villages-caves-for-fast-growth/))
- Trading Post: sblocco a City Hall 10 (hb city hall FAQ) oppure 12 (hb buildings hub): vedi conflicts; serve livello 13 per CH14 e 24 per CH25; il livello riduce la tassa di trasferimento ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-city-hall-requirements); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/))
- Farm account: CH17 (4 marce, economico) oppure CH22 (5 marce, farm di lungo periodo) ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/))

### 2.2 Ricerca (Academy)

- L'Academy non deve mai stare ferma: la ricerca e' potenza permanente e sblocca i tier di truppe. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-f2p-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/))
- Early game: prima tecnologie economiche poco costose e rapide che accelerano lo sviluppo (velocita' di ricerca come Writing, velocita' di costruzione, raccolta della risorsa carente), poi le tecnologie militari del prossimo tier; mid game: Engineering (costruzione) e Mathematics (ricerca), T3/T4, Combat Tactics, Defensive Formation, Herbal Medicine, rami del tipo di truppa principale; late game: completare i prerequisiti economici e militari e UN solo tipo di truppa fino al T5. ([heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/))
- Prima di una ricerca lunga: runa Research, titolo Scientist, buff di regno, poi Alliance Help, poi research speedup e solo dopo Universal. I bonus si applicano all'avvio del timer. ([heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/))
- Non dividere mesi di ricerca tra fanteria, cavalleria e arcieri: scegliere il tipo supportato dai comandanti migliori. ([heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/))
- **Economia vs militare:** Economia prima nell'early game (crescita piu' rapida), militare man mano che ci si avvicina al PvP serio e ai tier superiori; mantenere competitiva la ricerca militare del tipo di truppa principale. Le fonti non danno percentuali. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/))
- **Tecnologie chiave:** Writing (velocita' ricerca), Mathematics (velocita' ricerca), Engineering (velocita' costruzione), tecnologie di raccolta della risorsa carente, tecnologie dei tier T2/T3/T4/T5 del tipo principale, Combat Tactics, Defensive Formation, Herbal Medicine ([heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/); [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-unlock-t5-troops-dominate/))
- **Rami tardivi:** Rami tardivi per tipo (per orientarsi, non bastano da soli): fanteria Wootz Steel e Scutum; cavalleria Stirrups e Plate Armor; arcieri Bodkin Arrows e Pavise. Sconsigliato fare per primo il T5 d'assedio. Castle 24->25 = 5.000 Books of Covenant (solo l'ultimo livello). ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-t5-troops-unlock-guide); [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-unlock-t5-troops-dominate/))
- **T5:** City Hall 25 non da' il T5: serve Academy 25 (con la catena Castle/Watchtower/Trading Post a 25), poi ricerche economiche e militari prerequisite e il nodo T5 di UN tipo di truppa alla volta. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-city-hall-requirements))

| Academy | Bonus ricerca | Sblocco |
|---|---|---|
| 8 | 4% | accesso ricerca T2 |
| 16 | 8% | accesso ricerca T3 |
| 21 | 12% | accesso ricerca T4 |
| 25 | 25% | nodi finali Level V (T5); richiede City Hall 25, Watchtower 25, Trading Post 25, 1 Master's Blueprint, ~26,8M Food, 36M Wood, 10,2M Stone |

Academy 1-24 richiede il City Hall dello stesso livello (1-4 richiedono CH4); il bonus di ricerca cresce di 0,5% per livello fino a 10% (lv20), poi 12/14/16/18/25%. ([heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/))

**Regola bot:** IF l'Academy e' libera THEN scegli: (a) tecnologia che sblocca il prossimo tier di truppe se l'Academy lo consente; (b) Writing/Mathematics/Engineering disponibili; (c) raccolta della risorsa carente; (d) combattimento del tipo principale; ELSE la piu' breve utile (per non lasciare l'Academy ferma prima di andare offline scegli la piu' lunga utile). Prima di timer > 24 h: runa + titolo (se abilitato). NEVER gemme.

### 2.3 Civilta' (2026) e quale scegliere

| Civilta' | Comandante iniziale | Unita' speciale | Bonus |
|---|---|---|---|
| China | Sun Tzu | Chu-Ko-Nu | 3% difesa truppe, 5% recupero AP, 5% velocita' costruzione |
| Germany | Hermann | Teutonic Knight | 5% attacco cavalleria, 5% velocita' addestramento, 10% recupero AP |
| France | Joan of Arc | Throwing Axeman | 3% salute truppe, 10% raccolta legno, 20% velocita' cura ospedale |
| Arabia | Baibars | Mamluk | 5% attacco cavalleria, 10% danno a barbari e neutrali, 5% danno dei rally |
| Ottoman Empire | Osman I | Janissary | 5% salute arcieri, 5% velocita' marcia, 5% danno abilita' attive |
| Greece | Pericles | Argyraspide | 5% salute fanteria, 5% danno dei rally, 10% raccolta pietra |
| Egypt | Imhotep | Maryannu | 5% attacco arcieri, 5% danno dei rally, 1,5% velocita' costruzione e ricerca |
| Maya | Wak Chanil Ajaw | Spear-Thrower | 5% difesa arcieri, 10% raccolta oro, 3% danno normale tutte le truppe |
| Vikings | Bjorn Ironside | Berserker | 5% attacco fanteria, 3% danno contrattacco, 10% carico truppe |
| Korea | Eulji Mundeok | Hwarang | 5% difesa arcieri, 15% capacita' ospedale, 3% velocita' ricerca |
| Britain | Boudica | Longbowman | 5% attacco arcieri, 5% velocita' addestramento, 20% capacita' guarnigione alleata |
| Japan | Kusunoki Masashige | Samurai | 3% attacco truppe, 30% velocita' marcia scout, 5% velocita' raccolta |
| Byzantium | Belisarius | Cataphract | 5% salute cavalleria, 10% raccolta pietra, 15% capacita' ospedale |
| Rome | Scipio Africanus | Legionary | 5% difesa fanteria, 5% velocita' marcia, 10% raccolta cibo |
| Spain | Pelagius | Conquistador | 5% difesa cavalleria, 10% XP da barbari e neutrali, 20% produzione risorse |

Fonte tabella: [heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/).

**Tier list (le fonti non concordano):**

- heaven guardian 2026 09 01: S: Germany, France, China; A: Ottoman Empire, Arabia, Greece, Egypt, Maya, Korea, Vikings; B: Britain, Japan, Byzantium, Rome; C: Spain
- riseofkingdomsguides 2026 01 02: S: Arabia, Ottoman Empire, Vikings, France; A: Rome, Germany, Britain; B: China, Korea; C: Byzantium, Japan, Spain
- Le due classifiche divergono (vedi conflicts): la prima pesa progressione/versatilita' per un account tipico, la seconda il ruolo KvK. ([heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-best-civilization-tier-list/))

**Quale scegliere:**

- account nuovo / fase costruzione: **China (5% costruzione, 5% AP, Sun Tzu)** ([heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-civilization); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-best-civilization-tier-list/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/))
- F2P generico dopo la fase costruzione (bot che fa PvE e addestra): **Germany (5% addestramento, 10% recupero AP, 5% attacco cavalleria)** ([heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-best-civilization-tier-list/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-civilization))
- combattente in campo aperto in KvK: **France (3% salute, 20% velocita' cura)** ([heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-best-civilization-tier-list/))
- capo rally: **Arabia (cavalleria) / Egypt (arcieri) / Greece (fanteria): solo se si guidano davvero rally** ([heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-civilization))
- farm account: **Japan (5% raccolta tutte le risorse); Maya per oro** ([heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-best-civilization-tier-list/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-civilization))
- spinta di ricerca: **Korea (3% ricerca) - valutare il costo di cambiare e tornare indietro** ([heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-civilization))
- **Come cambiare:** Oggetto Civilization Change: 1 gratuito a City Hall 10 (heaven-guardian; handbook: 'un token gratuito durante la progressione iniziale'); Alliance Shop ~2.000.000 Individual Credits (se l'alleanza lo stocka); oppure 10.000 gemme (VIETATO al bot). Si tengono comandanti, edifici, ricerca e truppe; le unita' speciali si convertono; non si ottiene il comandante iniziale della nuova civilta'. Il handbook sconsiglia di cambiare sotto City Hall 15 finche' si costruisce. ([heaven-guardian 2026-09-01](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-how-to-change-civilization); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-best-civilization-tier-list/))
- **Regola bot:** IF CH >= 15 AND la fase di costruzione intensa e' finita AND l'utente ha scelto il ruolo THEN proponi il cambio (conferma obbligatoria) usando l'oggetto gratuito o i crediti; NEVER gemme.

### 2.4 VIP

| VIP | Punti totali | Cosa conta |
|---|---|---|
| 1 | 200 |  |
| 2 | 400 |  |
| 3 | 1.200 |  |
| 4 | 3.500 |  |
| 5 | 6.000 |  |
| 6 | 11.500 | secondo builder permanente (+10% costruzione, +10% raccolta) |
| 7 | 17.500 |  |
| 8 | 35.000 |  |
| 9 | 75.000 |  |
| 10 | 150.000 | 1 Universal Legendary Sculpture al giorno nel forziere VIP |
| 11 | 250.000 | +5% attacco truppe |
| 12 | 350.000 | 2 Universal Legendary Sculptures/giorno, +5% attacco e difesa |
| 13 | 500.000 |  |
| 14 | 750.000 | 3 Universal Legendary Sculptures/giorno, +5% capacita' truppe |
| 15 | 1.000.000 | 30% raccolta, 30% recupero AP, 50% velocita' cura, +100 cap AP |
| 16 | 1.500.000 | 35% recupero AP, +200 cap AP |
| 17 | 2.500.000 |  |
| 18 | 4.000.000 |  |
| 19 | 6.000.000 |  |
| SVIP | 9.000.000 |  |

Fonti: [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-guide-level-up-fast-get-rewards/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/how-do-you-get-vip-points-in-rise-of-kingdoms/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-vip-levels-guide).

Fonti gratuite di VIP points:

- claim giornaliero VIP: fino a 200 VIP points/giorno con claim consecutivi (~6.000/mese) ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-guide-level-up-fast-get-rewards/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/how-do-you-get-vip-points-in-rise-of-kingdoms/))
- Alliance Shop: 100 VIP points per 50.000 Individual Credits (se stockato) ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-guide-level-up-fast-get-rewards/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/how-do-you-get-vip-points-in-rise-of-kingdoms/))
- alliance gifts: casuale: 10, 50, 100, 200 o 1.000 punti ([rkguides 2026-01-02](https://riseofkingdomsguides.com/how-do-you-get-vip-points-in-rise-of-kingdoms/))
- Mysterious Caves / eventi / codici: occasionali ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-scout-villages-caves-for-fast-growth/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-vip-levels-guide))
- **Tempi solo gratuiti (calcolo derivato):** Solo con il claim giornaliero a 200/giorno: VIP 6 (11.500) ~58 giorni da zero; VIP 10 (150.000) ~750 giorni. I crediti d'alleanza (100 VIP ogni 50.000 crediti, max ~10.000 crediti/giorno da help + 20.000 da costruzioni) accelerano poco: ~60 VIP/giorno al massimo teorico (calcolo derivato).

VIP Shop — articoli pagati in risorse (reset lunedi' 00:00 UTC; [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-shop-guide-dominate-maximize-benefits/)):

- VIP 2: Basic Action Point Recovery (100 AP) — 12.000 Food, max 30/settimana
- VIP 3: Universal Speedup (5m) — 7.000 Food, max 50/settimana
- VIP 4: Brand-new Starlight Sculpture — 60.000 Food, max 20/settimana
- VIP 5: Dazzling Starlight Sculpture — 400.000 Wood, max 5/settimana

**Regola bot:** Riscuoti il VIP giornaliero ogni giorno (streak). Target: VIP 6 poi VIP 10, solo con fonti gratuite. NEVER gemme->VIP. Ogni lunedi' dopo le 00:00 UTC compra nel VIP Shop solo gli articoli pagati in Food/Wood utili. Il VIP non da' code di marcia (vengono dal City Hall 5/11/17/22). ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-vip-levels-guide); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-resources-guide-hub))

### 2.5 Titoli di regno

| Titolo | Buff |
|---|---|
| King | +5% attacco, +5% difesa, +5% salute |
| Kingdom Queen | +15% velocita' raccolta |
| General | +5% attacco, +5% difesa |
| Prime Minister | +15% produzione risorse, +10% velocita' costruzione |
| Justice | +5% attacco, +10% velocita' marcia |
| Duke | +5% difesa, +10% velocita' addestramento |
| Architect | +10% velocita' costruzione |
| Scientist | +5% velocita' ricerca, +10% raccolta oro |

- I titoli di sviluppo (Architect, Scientist, Duke) devono essere attivi PRIMA di avviare la coda; dopo l'avvio si rilasciano.
- Titoli 'continui' (Justice, Kingdom Queen, King/General, Prime Minister) valgono solo mentre sono assegnati.
- Si richiedono condividendo le coordinate nel canale del regno (chat, Discord, bot o alleanza titoli, dipende dal regno); non c'e' limite d'uso e si sommano con rune, buff e tecnologie.
- Titoli negativi: Traitor (-3% att/dif), Beggar (-10% produzione), Exile (-5% difesa), Slave (-5% salute), Sluggard (-5% marcia e addestramento), Fool (-5% costruzione e ricerca)
- **Regola bot:** Richiesta titolo solo se l'utente ha abilitato i messaggi in chat (conferma); mai attendere piu' di ~15 minuti tenendo ferma una coda. ([heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-titles-guide-to-maximize-your-buffs/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-kingdom-titles-guide))

### 2.6 Uso degli speedup

- Accumulare tra un evento e l'altro e usarli nella fase a punti (MGE, Power stage): lo stesso speedup paga due volte. Non scadono e non si rubano. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-speedups-guide); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-events-to-spend-on))
- Eccezioni (usare subito): cure in guerra; sbloccare un requisito rigido (tier truppe, coda di marcia, prerequisito City Hall); ricerca che lascerebbe l'Academy ferma; prontezza pre-KvK. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-speedups-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/))
- Ordine: bonus all'avvio (titolo, runa, buff) -> Alliance Help (non vale per l'addestramento) -> speedup specifici -> Universal solo per il resto. ([heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/))
- Research speedup i piu' preziosi; Healing speedup: tenere sempre una riserva; Building speedup su timer lunghi, non su edifici economici. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-speedups-guide))
- Early game non accumulare all'infinito se le code restano ferme: gli sblocchi precoci danno valore permanente. ([heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/))

### 2.7 Risorse e protezione

- Food e Wood dominano l'early game; la Stone diventa il collo di bottiglia da City Hall 17 a 25 (iniziare a raccoglierla prima); il Gold e' la piu' scarsa (ricerca, truppe T4/T5, forgiatura) e i nodi d'oro sono piu' rari: tenere un raccoglitore d'oro fisso. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-resources-guide-hub))
- Fonti per impatto: raccolta sulla mappa >> farm account > eventi > alleanza > saccheggio > produzione in citta'. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-resources-guide-hub); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub))
- Tutto cio' che supera il limite protetto dello Storehouse puo' essere saccheggiato: spendere prima di uscire o convertire in pacchetti. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-resources-guide-hub); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide-hub))
- Tenere i pacchetti risorse (resource items/tokens) chiusi fino al momento dell'upgrade: in inventario non si rubano. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-beginners-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-life-hacks-tips-and-tricks/))
- Il Mysterious Merchant permette di scambiare risorse aperte in pacchetti (protetti). ([heaven-guardian 2026-08-06](https://heaven-guardian.com/rise-of-kingdoms-courier-station-guide/))
- In periodi di conflitto: riparo o scudo prima di uscire; il territorio dell'alleanza non rende invulnerabili. ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-mightiest-governor-guide))
- Raccolta: T1 Siege per carico; comandanti raccolta separati su marce diverse (contano i talenti del primario); +25% nel territorio alleanza; token Enhanced Gathering +50% (8 h/24 h) comprabili con risorse; Kingdom Queen +15%; rune raccolta sui nodi. ([rkguides 2026-01-02](https://riseofkingdomsguides.com/farming-gathering-guide/); [heaven-guardian 2026-08-12](https://heaven-guardian.com/rise-of-kingdoms-gathering-guide-dominate-resources/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-titles-guide-to-maximize-your-buffs/))
- Farm account: Un farm account raccoglie e trasferisce risorse al principale via Trading Post (il livello riduce la tassa); tenerlo economico, fermarsi a CH17 o CH22. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide-hub))

## 3. Eventi 2026: come fare punti senza gemme

### Mightiest Governor (MGE)

- **Cadenza:** Ricorrente, date non fisse (pannello Events). Formato riseofkingdomsguides: 6 fasi, 5 da 24 h + Final Sprint da 48 h (6 giorni). heaven-guardian: 5 fasi 'classiche' + Final Sprint come sesta finestra.
- **Come funziona:** Fasi: Training Troops, Defeating Barbarians, Gathering Resources, Increasing Power, Eliminating Enemies, Final Sprint (attivita' precedenti a punteggio ridotto). Punti standard: truppe addestrate T1 5, T2 10, T3 20, T4 40, T5 100 (upgrade = differenza tra i tier); raccolta 100 Food 1, 100 Wood 1, 100 Stone 2, 100 Gold 5, 1 gemma 150; potenza +2 punti per punto potenza. Premi: sculture leggendarie a scelta tra i comandanti offerti. Molti regni fanno 'fixed MGE' con posizioni/cap assegnati.
- **Azioni del bot:**
  - Prima dell'evento: chiedere all'utente target di punteggio, budget massimo (speedup/risorse) e cap del regno; leggere la mail del regno.
  - Training: preparare una coda che finisca DOPO l'inizio della fase; attivare Duke/runa/buff prima di avviare; addestrare il tier piu' alto sostenibile; fermarsi al cap.
  - Barbari: spendere AP naturali (e bottled AP solo se previsto dal budget) in catena con Peacekeeping.
  - Raccolta: marce quasi piene tenute fuori e fatte rientrare quando la fase e' iniziata; preferire oro (5 punti/100) salvo nodi di gemme.
  - Power: completare upgrade/ricerche UTILI pianificate durante la fase.
  - Final Sprint: calcolare il gap al prossimo scaglione prima di spendere; non iniziare azioni che finiscono dopo la fine.
  - Riscuotere milestone e premi di fase.
- **Da evitare:** Eliminating Enemies: attaccare giocatori o farm senza conferma dell'utente e senza le regole del regno (vietato al bot senza conferma). Superare il cap assegnato in una fixed MGE. Spendere tutti gli speedup/risorse di KvK per un piccolo miglioramento di classifica; usare gemme. Spendere sculture o tomi solo per punti se il pannello non li premia.
- **Conferma:** si' per la fase Eliminating Enemies e per usare riserve oltre il budget
- **Fonti:** [rkguides 2026-01-02](https://riseofkingdomsguides.com/the-mightiest-governor-event/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-win-mightiest-governor-event/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-mightiest-governor-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/)

### Ceroli Crisis (e Ceroli Assault)

- **Cadenza:** Ricorrente nel calendario eventi d'alleanza (ruota con Ian's Ballads, Lohar's Trial, Karuak Ceremony); date dal pannello Events.
- **Come funziona:** Ceroli Crisis: evento PvE a squadre di 4 giocatori contro boss con meccaniche (Dekar, Keira, Frida, Astrid...), difficolta' multiple; premi diretti + medaglie da spendere nello store dell'evento (materiali/blueprint equipaggiamento prima di tutto). Ceroli Assault: evento separato da 12 giocatori.
- **Azioni del bot:**
  - E' un contenuto in tempo reale e di coordinamento: il bot NON lo gioca in autonomia; avvisa l'utente quando e' attivo.
  - Spendere le medaglie Ceroli prima della chiusura: priorita' materiali/blueprint equipaggiamento > sculture > speedup > risorse.
- **Da evitare:** Lasciare medaglie non spese a fine evento. Scegliere difficolta' che la squadra non completa (un clear piu' basso vale di piu').
- **Conferma:** si' (partecipazione gestita dall'utente)
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-ceroli-crisis-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/); [heaven-guardian 2026-08-05](https://heaven-guardian.com/rise-of-kingdoms-ceroli-crisis-guide-boss-tips/)

### Ian's Ballads

- **Cadenza:** Ricorrente (evento raid gemello di Ceroli); date dal pannello Events.
- **Come funziona:** Raid da 4 giocatori (tu + 3 invitati), City Hall 16+, limite 2 ore, ondate di barbari e 3 boss (Huntmaster Kikkara, Beastlord Mokka, Flamebender Papakura), 5 difficolta'. Ogni boss da' un forziere di blueprint e materiali; il 'chieftain's reward' si ottiene una sola volta per governatore.
- **Azioni del bot:**
  - Avvisare l'utente quando e' attivo; il bot non forma gruppi da solo.
  - Dopo i run: riscuotere i forzieri e il chieftain's reward se non ancora preso.
- **Da evitare:** Difficolta' non completabili entro 2 ore. Andare con la coppia da raccolta invece della coppia da danno.
- **Conferma:** si'
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-ians-ballads-guide)

### Karuak Ceremony (e Trial of Kau Karuak)

- **Cadenza:** Ricorrente; date dal pannello Events. Trial of Kau Karuak e' un evento separato della Season of Conquest (cristalli).
- **Come funziona:** Formato individuale documentato: 50 livelli, 5 difficolta' (Easy, Normal, Hard, Nightmare, Hell). Si evocano bersagli e si attaccano: costo AP per evocare + costo AP per attaccare (crescente con attacchi ripetuti); per i livelli duri si chiede aiuto/rally all'alleanza.
- **Azioni del bot:**
  - Prima di scegliere la difficolta' (non modificabile dopo): calcolare AP richiesti = evocazioni + attacchi + tentativi (es. 50 x 100 AP = 5.000 AP solo per evocare) e proporre all'utente la difficolta' completabile.
  - Livelli facili: marcia Peacekeeping sostenibile; spendere prima gli AP naturali, poi gli oggetti AP previsti dal budget.
  - Riscuotere i premi di ogni livello e della sfida d'alleanza prima della scadenza.
- **Da evitare:** Scegliere la difficolta' per il forziere finale senza budget AP. Lasciare gli AP naturali al cap nei giorni prima. Confondere Karuak Ceremony con Trial of Kau Karuak.
- **Conferma:** si' per la scelta della difficolta' e l'uso di oggetti AP
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-karuak-ceremony-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/)

### Golden Kingdom

- **Cadenza:** Ricorrente; date dal pannello Events (le fonti non danno la cadenza).
- **Come funziona:** Dungeon PvE a 20 piani, City Hall 17+; checkpoint ogni 4 piani con premi e shop (Karaku Gold); relics monouso (max 9), blessings permanenti scelte tra 3 dopo ogni piano; la salute delle truppe persiste tra le battaglie; nebbia da esplorare; healing hut +50%; funzionano equipaggiamento/tecnologia/VIP/civilta', non l'army expansion. Serve una prima linea resistente.
- **Azioni del bot:**
  - Se l'utente abilita la modalita': esplorare prima le caselle sicure, evitare combattimenti opzionali poco utili, curare la marcia che regge le battaglie successive, spendere Karaku Gold nei checkpoint.
  - Altrimenti avvisare l'utente e riscuotere i premi dei checkpoint.
- **Da evitare:** Combattere ogni nemico visibile. Tenere valuta/oggetti inutilizzati fino alla sconfitta. Comprare un leggendario solo per questa modalita'.
- **Conferma:** si' per avviare la modalita' (logica complessa; le fonti lette non chiariscono se le perdite toccano le truppe reali)
- **Fonti:** [rkguides 2026-01-02](https://riseofkingdomsguides.com/golden-kingdom-event-guide-rok/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-golden-kingdom-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/)

### Silk Road Speculators (scorta carovana d'alleanza)

- **Cadenza:** Evento d'alleanza 'tenuto regolarmente in ogni regno' (fonte 2019); chance di scorta giornaliere azzerate alle 00:00 UTC. Nel 2026 l'Anniversary 1.1.11 include 'Desert Tracks' (scorta di una carovana del tesoro): formato simile, dettagli non verificati.
- **Come funziona:** Leader/R4 scelgono difficolta' (Easy, Normal, Hard, Nightmare, Hell) e fortezza di partenza (costo 100.000 Alliance Credits per avvio); la carovana viaggia (Easy ~15 min) e i barbari la attaccano: i membri devono distruggerli. Premi via mail a tutti i membri in base alla percentuale di merci consegnate; classifica tra alleanze; oltre il limite giornaliero solo carovane di allenamento senza premi.
- **Azioni del bot:**
  - Quando la carovana e' in viaggio (annuncio d'alleanza): se l'utente lo abilita, mandare marce PvE sui barbari lungo il percorso (sono barbari, non giocatori).
  - Riscuotere i premi arrivati via mail.
- **Da evitare:** Avviare carovane (solo leader/R4 e costa Alliance Credits). Allontanare tutte le marce dalla citta' in zona ostile.
- **Conferma:** no per attaccare i barbari della scorta; il bot non avvia la carovana
- **Fonti:** [rok.guide 2019-05-27](https://web.archive.org/web/20240725150508/https://www.rok.guide/silk-road-speculators-event/); [rok.guide 2019-05-24](https://web.archive.org/web/20240417223657/https://www.rok.guide/silk-road-speculators/); [ldshop 2026-08-27](https://www.ldshop.gg/blog/rise-of-kingdoms/anniversary-special.html)

### Esmeralda's Prayer / Esmeralda's Collection

- **Cadenza:** Evento stagionale ricorrente (Spring Symphony: 10 giorni; presente anche in Halloween 2026, versione 1.1.12 del 22-09-2026).
- **Come funziona:** Esmeralda's Prayer: ruota con Wishing Coins (1-3 monete per spin); Esmeralda's Collection: via F2P con missioni giornaliere che si azzerano ogni giorno (4 monete/giorno secondo riseofkingdomsguides). Le monete arrivano anche da altri eventi del pacchetto (Race Against Time, Dreams of Spring...). Uno spin in gemme costa 1.200 gemme.
- **Azioni del bot:**
  - Completare ogni giorno le missioni di Esmeralda's Collection e riscuotere le monete.
  - Usare SOLO le Wishing Coins gratuite per gli spin; riscuotere i premi.
- **Da evitare:** Spin in gemme (1.200 gemme/spin) o acquisto di monete.
- **Conferma:** no
- **Fonti:** [rkguides 2026-01-02](https://riseofkingdomsguides.com/spring-symphony-and-esmeraldas-prayer-event-guide/); [ldshop 2026-09-22](https://www.ldshop.gg/blog/rise-of-kingdoms/halloween-guide.html)

### Arms Training (Armsmaster Lohar)

- **Cadenza:** Ricorrente (Holiday Events; presente nell'Anniversary 1.1.11 dell'agosto 2026). Durata 3 giorni.
- **Come funziona:** NON e' un evento di addestramento truppe: si combatte ripetutamente Lohar con UNA marcia senza tornare in citta'; 5 tentativi al giorno; ogni vittoria rende Lohar piu' forte e aggiunge un'abilita'/modificatore scelto; 10.000 punti per sconfitta, stage normali max 300.000 punti, poi Legend Mode (punteggio in base alle truppe rimaste). Top 10: blueprint leggendari.
- **Azioni del bot:**
  - Primi tentativi come prova: registrare coppia, buff, modificatori scelti e truppe rimaste.
  - Usare la coppia a bersaglio singolo piu' forte, runa/ buff gia' disponibili, ospedale libero.
  - Puntare alle milestone raggiungibili; niente classifica senza budget.
- **Da evitare:** Usare speedup di addestramento 'perche' si chiama Training'. Comprare army expansion/leggendari per la classifica. Tornare in citta' durante la catena.
- **Conferma:** si' per consumare expansion/consumabili costosi
- **Fonti:** [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-arms-training-event/); [kibezaka 2021-11](https://www.kibezaka.com/2021/11/tips-arms-training-rise-of-kingdoms.html); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-arms-training-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/); [ldshop 2026-08-27](https://www.ldshop.gg/blog/rise-of-kingdoms/anniversary-special.html)

### Armament, Reveal Thyself

- **Cadenza:** Evento a rotazione dal 1.0.83; solo regni in Season 3 o Season of Conquest all'inizio dell'evento. Cadenza non trovata.
- **Come funziona:** Si sceglie la formazione preferita e il negozio dell'evento si riempie di armamenti per quella formazione con informazioni parzialmente nascoste, rivelate dopo l'acquisto con Armament Tickets. Probabilita' pubblicate da Lilith separatamente dagli armamenti standard.
- **Azioni del bot:**
  - Se il regno e' idoneo: mostrare all'utente formazione consigliata e biglietti posseduti; NON acquistare in autonomia (conferma).
- **Da evitare:** Acquistare biglietti con gemme. Spendere Armament Tickets senza conferma (materiale raro).
- **Conferma:** si'
- **Fonti:** [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-1-0-83-eternal-city-update/); [rok.lilith.com s.d.](https://rok.lilith.com/probability/)

### In Search of Wonders

- **Cadenza:** Evento armamenti (dal 1.0.83; presente in Halloween 2026 v1.1.12). Stessa idoneita' Season 3/SoC indicata per il 1.0.83.
- **Come funziona:** Evento focalizzato sull'ottenere armamenti di alta qualita' (nel 1.0.83 per le nuove formazioni staggered). Meccanica e punti non dettagliati dalle fonti lette.
- **Azioni del bot:**
  - Riscuotere premi gratuiti e segnalare all'utente.
- **Da evitare:** Gemme.
- **Conferma:** si' per spendere materiali
- **Fonti:** [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-1-0-83-eternal-city-update/); [ldshop 2026-09-22](https://www.ldshop.gg/blog/rise-of-kingdoms/halloween-guide.html)

### Lohar's Trial

- **Cadenza:** Circa una volta al mese, 2 giorni (riseofkingdomshandbook).
- **Come funziona:** Durante l'evento i barbari normali droppano Bone Necklaces (risorse, speedup, gemme, Arrows of Resistance, relics); le relics (Lohar's Longbow, Lohar's Buckler) evocano Lohar vicino alla citta'; sconfitto (di solito in rally) da' sculture di Lohar a chi partecipa. Le Bone Necklaces non scadono.
- **Azioni del bot:**
  - Nei giorni prima: non sprecare AP (non superare il cap) e tenere gli oggetti AP per l'evento.
  - Durante: farm di barbari in catena con Peacekeeping; aprire le Bone Necklaces; usare le relics nelle ore di punta dell'alleanza e annunciarle (annuncio in chat = conferma utente); unirsi ai rally Lohar degli alleati.
- **Da evitare:** Rientrare in citta' dopo ogni barbaro (rompe la catena). Tenere le relics oltre la fine dell'evento.
- **Conferma:** no per i barbari; si' per usare oggetti AP e per scrivere in chat
- **Fonti:** [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-lohars-trial-guide); [heaven-guardian 2026-08-08](https://heaven-guardian.com/rise-of-kingdoms-lohars-trial-guide/)

### Wheel of Fortune

- **Cadenza:** Nessun calendario fisso: in media ogni ~3 settimane (fino a 6), dura 3 giorni (riseofkingdomsguides).
- **Come funziona:** Evento di spin in gemme per sculture di comandanti leggendari; 1 spin gratuito all'inizio; spin scontati giornalieri in gemme; milestone a 10, 25... spin.
- **Azioni del bot:**
  - Fare SOLO lo spin gratuito e riscuotere cio' che e' gratuito.
- **Da evitare:** Qualsiasi spin in gemme (primo spin pagato 400 gemme; 10 spin 5.600; 100 spin 70.400).
- **Conferma:** no (solo spin gratuito)
- **Fonti:** [rkguides 2026-01-02](https://riseofkingdomsguides.com/wheel-of-fortune-guide-in-rise-of-kingdoms/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-wheel-of-fortune-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/)

### More Than Gems

- **Cadenza:** Due giorni con contatori giornalieri separati; nessuna data universale.
- **Come funziona:** Premia la SPESA di gemme (7.000 gemme/giorno = 5 Universal Legendary Sculptures; 25.000/giorno = 13).
- **Azioni del bot:**
  - Nessuna azione (il bot non spende gemme). Segnalare all'utente se attivo.
- **Da evitare:** Spendere gemme.
- **Conferma:** n/a
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-more-than-gems-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/)

### Zenith of Power

- **Cadenza:** Circa ogni 3 mesi, su tutto il continente.
- **Come funziona:** Gara di crescita della potenza tra i regni del continente; skin citta' +20% attacco fanteria (permanente top 20, temporanea top 100); milestone con sculture e casse materiali.
- **Azioni del bot:**
  - Far coincidere upgrade/ricerche gia' pianificati con la finestra e riscuotere le milestone.
- **Da evitare:** Inseguire la classifica (territorio da spender).
- **Conferma:** no
- **Fonti:** [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-zenith-of-power-guide); [rkguides 2026-01-02](https://riseofkingdomsguides.com/spring-symphony-and-esmeraldas-prayer-event-guide/)

### Shadow Legion

- **Cadenza:** Evento d'alleanza con orario scelto dagli ufficiali.
- **Come funziona:** Ondate di eserciti (Dark Fortresses) attaccano le citta' dei membri; conta la difesa coordinata e i rinforzi.
- **Azioni del bot:**
  - All'orario annunciato: richiamare le marce in citta', liberare spazio in ospedale, impostare la guarnigione indicata; inviare rinforzi solo su istruzione.
- **Da evitare:** Avere le marce lontane in raccolta all'inizio delle ondate.
- **Conferma:** si' per inviare rinforzi
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-shadow-legion-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/)

### Alliance Mobilization

- **Cadenza:** Competizione d'alleanza ricorrente.
- **Come funziona:** Missioni a tempo prese dalla bacheca d'alleanza; tentativi limitati; un'accettata non completata spreca il tentativo.
- **Azioni del bot:**
  - Accettare solo missioni che coincidono con azioni gia' pianificate (raccolta di una risorsa necessaria, barbari, ricerca) e completabili prima del timer; consegnarle e riscuotere.
- **Da evitare:** Comprare tentativi extra con gemme. Missioni che richiedono spesa o code che non si completano in tempo.
- **Conferma:** no per missioni compatibili
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-mobilization-guide); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/)

### Sunset Canyon

- **Cadenza:** Stagione di 7 giorni, 5 tentativi gratuiti al giorno.
- **Come funziona:** Battaglie con truppe simulate e formazione dedicata; nessuna perdita reale.
- **Azioni del bot:**
  - Usare ogni giorno i tentativi gratuiti (vedi daily_checklist).
- **Da evitare:** Comprare tentativi con gemme.
- **Conferma:** no
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-sunset-canyon-guide)

### Peerless Scholar (Lyceum of Wisdom)

- **Cadenza:** Preliminary lun-ven (10 domande senza timer, finestra ~00:00-23:00 UTC, 6/10 per qualificarsi); Midterm sabato alle 02:30 o 12:30 UTC (15 domande a tempo); Final l'ultimo sabato del mese alle 14:30 UTC (20 domande a tempo). Sblocco a City Hall 10.
- **Come funziona:** Quiz su meccaniche e storia; premi gemme, speedup, forzieri d'alleanza; pool di gemme condiviso per Midterm/Final.
- **Azioni del bot:**
  - Preliminary ogni giorno feriale prima delle 23:00 UTC usando un database di risposte verificato (e i 3 aiuti d'alleanza).
  - Midterm/Final: solo se il bot risponde in tempo reale in modo affidabile, altrimenti avvisare l'utente.
- **Da evitare:** Liste di risposte vecchie non verificate.
- **Conferma:** no
- **Fonti:** [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-peerless-scholar-answers/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-lyceum-of-wisdom-guide)

### Champions of Olympia

- **Cadenza:** Finestre attive dal pannello Events.
- **Come funziona:** 5v5 in tempo reale, 3 marce a testa, 10 minuti, controllo delle bandiere.
- **Azioni del bot:**
  - Non giocare in autonomia (PvP in tempo reale): avvisare l'utente.
- **Da evitare:** Automatizzare PvP.
- **Conferma:** si'
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-champions-of-olympia-guide)

### Ark of Osiris

- **Cadenza:** Evento d'alleanza 30v30 programmato con registrazione.
- **Come funziona:** Battaglia su mappa separata; le truppe non muoiono (cure a costo di speedup).
- **Azioni del bot:**
  - Segnalare registrazione e orario all'utente; non registrarsi ne' combattere in autonomia.
- **Da evitare:** Combattere senza l'utente (PvP).
- **Conferma:** si'
- **Fonti:** [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-ark-of-osiris-guide)

### Marauders / Eve of the Crusade (pre-KvK)

- **Cadenza:** Legato al KvK; dal 1.1.12 (settembre 2026) Eve of the Crusade apre insieme al Lost Kingdom invece che come fase precedente.
- **Come funziona:** Una delle fonti piu' ricche di speedup, gemme e risorse a base di AP (Marauders).
- **Azioni del bot:**
  - Nei giorni prima: tenere gli oggetti AP e non spendere l'intera riserva in barbari normali.
  - Durante: farm efficiente con Peacekeeping seguendo le istruzioni del regno.
- **Da evitare:** Svuotare gli AP poco prima dei Marauders.
- **Conferma:** si' per usare oggetti AP
- **Fonti:** [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [ldshop 2026-09-22](https://www.ldshop.gg/blog/rise-of-kingdoms/halloween-guide.html)

### Eventi stagionali 2026 (Anniversary 1.1.11, Halloween 1.1.12)

- **Cadenza:** Anniversary: versione 1.1.11 del 27-08-2026; Halloween: versione 1.1.12 del 22-09-2026.
- **Come funziona:** Anniversary: Art Festival, Melon Market, Alliance Quiz, Arms Training, Riddles of the Sphinx, Desert Tracks, Circus of Wonders, Lucky Red Packet, RoK Yearbook. Halloween: Esmeralda's Prayer/Collection, Race Against Time, In Search of Wonders, Eve of the Crusade con il Lost Kingdom; Chronicle del Lost Kingdom a orari fissi (venerdi'-sabato 12:00).
- **Azioni del bot:**
  - Completare le missioni giornaliere gratuite degli eventi stagionali e riscuotere; spendere le valute evento nei negozi secondo priorita' (sculture del comandante in sviluppo > speedup ricerca > materiali > risorse).
- **Da evitare:** Componenti in gemme o pacchetti.
- **Conferma:** no per missioni gratuite
- **Fonti:** [ldshop 2026-08-27](https://www.ldshop.gg/blog/rise-of-kingdoms/anniversary-special.html); [ldshop 2026-09-22](https://www.ldshop.gg/blog/rise-of-kingdoms/halloween-guide.html); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-events-to-spend-on)

## 4. Errori comuni

- **Lasciare ferme le code (builder, Academy, caserme) o gli scout.** → Ogni sessione riempire tutte le code; prima di uscire avviare i timer piu' lunghi. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-f2p-guide); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-scout-villages-caves-for-fast-growth/))
- **Lasciare la barra AP al massimo (la rigenerazione si ferma).** → Spendere gli AP naturali in barbari prima del cap; conservare solo gli oggetti AP. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-beginners-guide/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-karuak-ceremony-guide))
- **Usare subito tutte le pozioni AP in barbari normali.** → Tenerle per Lohar's Trial, Marauders, Karuak, fase barbari MGE. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/))
- **Usare speedup prima dell'Alliance Help o prima di aver attivato titolo/runa.** → Titolo/runa all'avvio -> help -> speedup specifici -> Universal. ([heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/))
- **Bruciare gli speedup fuori dagli eventi per far salire la potenza oggi.** → Accumulare e usarli nelle fasi a punti, salvo eccezioni (sblocchi, guerra). ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-speedups-guide); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-events-to-spend-on))
- **Livellare ogni edificio allo stesso livello / riempire la citta' di fattorie.** → Seguire solo i prerequisiti del prossimo City Hall; la raccolta sulla mappa rende molto di piu'. ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/))
- **Ospedale sottodimensionato: i feriti in eccesso muoiono.** → Capacita' almeno per una marcia piena prima di combattere; curare prima di nuovi scontri. ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-healing-hospital-guide); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/))
- **Tenere risorse aperte oltre il limite protetto o aprire subito i pacchetti.** → Spendere o convertire in pacchetti; aprire i pacchetti solo al momento dell'upgrade. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-resources-guide-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-beginners-guide/))
- **Sparpagliare sculture su troppi comandanti / usare Universal Legendary Sculptures su comandanti da Golden Chest o su Aethelflaed.** → Una coppia principale alla volta; conservare le 'gold heads' (conferma utente). ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/rise-of-kingdoms-beginners-guide/))
- **Ignorare i forti barbari fino al late game.** → Unirsi presto ai rally dei forti: i Books of Covenant (20.095 per Castle 25) diventano il collo di bottiglia del T5. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/))
- **Riciclare Books of Covenant/Arrows of Resistance nell'Alliance Reclaim prima di Castle/Watchtower 25.** → Reclaim solo di surplus confermato dall'utente. ([heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/))
- **Restare in un'alleanza morta.** → Alleanza attiva (help che si riempiono, forti, guardian run, ufficiali che comunicano); la soglia di membri attivi e' discussa (vedi conflicts). Cambiare alleanza -> decisione dell'utente. ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-guide-hub); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/))
- **Richiedere un titolo dopo aver avviato la coda.** → Titolo attivo prima dell'avvio, poi rilasciarlo. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-kingdom-titles-guide); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-titles-guide-to-maximize-your-buffs/))
- **Raccogliere una runa nuova sopra una ancora utile (ne vale una sola).** → Controllare la runa attiva prima di prenderne un'altra. ([heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/))
- **Fidarsi di calendari eventi esterni o di orari locali.** → Pannello Events in gioco e countdown UTC. ([heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub))
- **Non spendere le valute evento (medaglie Ceroli, monete) prima della chiusura.** → Spendere prima della fine secondo le priorita' del negozio. ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-ceroli-crisis-guide); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-events-to-spend-on))
- **Combattere solo per i kill point / attaccare farm o raccoglitori altrui (anche in MGE) senza regole.** → Mai attaccare giocatori senza conferma dell'utente e senza le regole di regno/alleanza. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-win-mightiest-governor-event/))
- **Seguire vecchie guide 'jumper account' (Beginner's Immigration sospeso per i nuovi account dal 26-03-2025).** → Crescere nel regno dove si gioca. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/))
- **Cadere nelle 'offerte' in gemme (refresh del mercante, VIP Shop, ruote, chiavi).** → Il bot compra solo con risorse/crediti/medaglie; le gemme restano all'utente. ([heaven-guardian 2026-08-06](https://heaven-guardian.com/rise-of-kingdoms-courier-station-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-shop-guide-dominate-maximize-benefits/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-wheel-of-fortune-guide))

## 5. Regole del bot

- **R1_no_gems** — MAI spendere gemme: niente acquisti, velocizzazioni, refresh, spin (Wheel of Fortune, Esmeralda), chiavi, VIP points, civilization change, tentativi extra (Canyon, Mobilization), viaggi State Forum extra, donazioni in gemme. *Conferma:* non superabile dal bot. ([heaven-guardian 2026-08-06](https://heaven-guardian.com/rise-of-kingdoms-courier-station-guide/); [rkguides 2026-01-02](https://riseofkingdomsguides.com/wheel-of-fortune-guide-in-rise-of-kingdoms/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-guide-level-up-fast-get-rewards/))
- **R2_pvp_confirm** — Qualsiasi attacco a giocatori, citta', marce di raccolta altrui, flag/strutture nemiche, Ark of Osiris, Olympia, fase Eliminating Enemies della MGE -> conferma esplicita dell'utente. *Conferma:* si'. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-win-mightiest-governor-event/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/))
- **R3_rare_materials** — Conferma prima di consumare: Universal Legendary Sculptures e sculture su skill, Books of Covenant, Arrows of Resistance, Master's Blueprint, Sage's Testimony, Transmutation/Conversion Stones, Armament Tickets, Golden Keys fuori evento, Civilization Change, Passport Pages, teletrasporti, Peace Shield, oggetti AP fuori evento, speedup oltre la soglia, Alliance Reclaim. *Conferma:* si'. ([heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-tavern-keys-guide))
- **R4_queues** — Ogni sessione: nessuna coda ferma (builder, Academy, caserme, ospedale), nessuna marcia o scout inattivo, AP sotto il cap. *Conferma:* no. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-f2p-guide))
- **R5_bonus_before_start** — Per code > 8 h: runa del tipo giusto e titolo (se abilitato) PRIMA di avviare; dopo l'avvio chiedere Alliance Help; speedup solo dopo gli aiuti e prima gli specifici. *Conferma:* no. ([heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-titles-guide-to-maximize-your-buffs/); [heaven-guardian 2026-08-04](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/))
- **R6_ap_policy** — AP naturali: spenderli sempre prima del cap (barbari in catena, poi Travel dello State Forum). Oggetti AP: solo durante eventi che li premiano e nel budget dell'utente. *Conferma:* si' per oggetti AP. ([heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/); [heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-maximize-action-points-dominate/))
- **R7_speedup_policy** — Speedup: accumulare; usarli in fasi a punti o per sblocchi (coda di marcia, tier, prerequisito CH) o in guerra per curare; soglia di conferma configurabile. *Conferma:* oltre soglia. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-speedups-guide))
- **R8_resource_safety** — Fine sessione: risorse aperte <= protezione Storehouse; pacchetti chiusi; in guerra proporre scudo all'utente. *Conferma:* si' per scudo. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-resources-guide-hub); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub))
- **R9_events_authority** — Date e regole degli eventi solo dal pannello Events/mail del regno; convertire tutto in UTC; il bot non assume cadenze fisse. *Conferma:* no. ([heaven-guardian 2026-08-03](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/); [handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub))
- **R10_shops** — Negozi: Mysterious Merchant solo offerte in Food/Wood + refresh gratuito; VIP Shop solo articoli in risorse (lunedi' 00:00 UTC); Expedition store con medaglie; Alliance Shop con Individual Credits solo su piano/conferma; mai sotto la riserva risorse del prossimo upgrade. *Conferma:* si' per Alliance Shop. ([heaven-guardian 2026-08-06](https://heaven-guardian.com/rise-of-kingdoms-courier-station-guide/); [heaven-guardian 2026-09-02](https://heaven-guardian.com/rise-of-kingdoms-vip-shop-guide-dominate-maximize-benefits/); [handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-shop-guide))
- **R11_chat** — Nessun messaggio in chat (titoli, annunci Lohar, richieste) senza abilitazione/conferma dell'utente. *Conferma:* si'. ([handbook 2026-08-18](https://riseofkingdomshandbook.com/guides/riseofkingdoms-kingdom-titles-guide))
- **R12_daily_reset** — Tra le 23:00 e le 23:59 UTC: riscuotere tutti i forzieri sbloccati, usare tentativi gratuiti residui (Canyon, State Forum), completare il Preliminary del Peerless Scholar (entro le 23:00 UTC); dopo le 00:00 UTC: mercante, VIP giornaliero, nuove missioni. *Conferma:* no. ([handbook 2026-09-09](https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub); [heaven-guardian 2026-08-06](https://heaven-guardian.com/rise-of-kingdoms-courier-station-guide/); [heaven-guardian 2026-09-19](https://heaven-guardian.com/rise-of-kingdoms-peerless-scholar-answers/))

## 6. Lacune e conflitti tra fonti

**Lacune (dati non trovati):**

- Orario del reset giornaliero degli obiettivi: nessuna fonte 2026 letta lo dice testualmente (dedotto 00:00 UTC da Mysterious Merchant 00:00 UTC, chance Silk Road 00:00 UTC [fonte 2019], avviso 'timer UTC intorno al daily reset').
- Tavern: '5 Silver gratuite al giorno' e 'Golden gratuita ogni ~2 giorni' confermati da una sola fonte (riseofkingdomshandbook); valori per livello Tavern non trovati.
- Numero di tentativi/giorno delle donazioni alla tecnologia d'alleanza e loro tempo di ricarica: non trovato (solo 'si ricaricano nel tempo').
- Master's Blueprint: l'unica fonte indicata (heaven-guardian) e' lo Shop in gemme; fonti gratuite (eventi?) non verificate: blocca CH25/Academy 25 per un bot senza gemme.
- Armament Tickets (Armament, Reveal Thyself): come ottenerli gratis e cadenza dell'evento non trovati.
- Cadenza di Golden Kingdom, Ceroli Crisis, Ian's Ballads, Karuak Ceremony, Alliance Mobilization, Shadow Legion: le fonti dicono solo 'ricorrente, vedere il pannello Events'.
- Silk Road Speculators: unica descrizione dettagliata e' del 2019 (rok.guide via Wayback Machine); non verificato se nel 2026 esista ancora con lo stesso nome (l'Anniversary 2026 cita 'Desert Tracks', scorta di carovana).
- Esmeralda's Collection: '4 monete al giorno' viene da riseofkingdomsguides (pagina Spring Symphony, data 2026-01-02); per Halloween 2026 non verificato.
- Premio giornaliero Expedition: importo esatto non pubblicato (dipende dai progressi).
- Ordine ottimale di ricerca tecnologia per tecnologia (livelli esatti di Academy per ogni nodo): le fonti avvertono che le tabelle community sono in conflitto; il bot deve leggere i prerequisiti in gioco.
- Capacita' protetta dello Storehouse per livello: non trovata nelle fonti lette.
- Dettagli di Race Against Time, Radiant Rivalry e degli altri eventi Halloween 2026 non disponibili nelle fonti lette.
- Quantita' di Individual Credits per singolo aiuto/donazione: non trovata (solo i cap giornalieri 10.000 help / 20.000 costruzioni).

**Conflitti:**

- **Tier list civilta' 2026** — heaven-guardian 2026-09-01: S: Germany, France, China; A: Ottoman, Arabia, Greece, Egypt, Maya, Korea, Vikings; B: Britain, Japan, Byzantium, Rome; C: Spain / riseofkingdomsguides 2026-01-02: S: Arabia, Ottoman, Vikings, France; A: Rome, Germany, Britain; B: China, Korea; C: Byzantium, Japan, Spain. *Scelta del bot:* Il bot usa le raccomandazioni per ruolo (concordanti: China all'inizio, Germany post-costruzione F2P, France campo aperto, Japan farm).
- **Priorita' del Medal Store dell'Expedition** — heaven-guardian 2026-08-03: Aethelflaed sculptures prima finche' non e' expertised / riseofkingdomshandbook 2026-08-18: la scultura epica in rotazione settimanale e' il premio principale. *Scelta del bot:* Default: Aethelflaed finche' non e' expertised (limite giornaliero), poi l'epico in rotazione se fa parte di una marcia; chiedere all'utente.
- **Riduzione AP del talento Insight** — gamesguideinfo (truppe_pve.json): fino a -9 AP / heaven-guardian MGE 2026-09-02: fino a -10 AP. *Scelta del bot:* Usare il costo mostrato in gioco.
- **VIP points giornalieri gratuiti** — heaven-guardian 2026-09-02: crescono con i claim consecutivi fino a 200/giorno / riseofkingdomsguides 2026-01-02: 200 VIP points ogni 24 ore. *Scelta del bot:* Riscuotere ogni giorno senza saltare (streak).
- **Prerequisito City Hall 3** — heaven-guardian 2026-09-02: nessuno / riseofkingdomshandbook 2026-09-09: Wall 2. *Scelta del bot:* Irrilevante per il bot (leggere il pannello).
- **Sblocco Trading Post** — riseofkingdomshandbook city hall FAQ: City Hall 10 / riseofkingdomshandbook buildings hub: City Hall 12. *Scelta del bot:* Serve comunque Trading Post 13 per CH14: costruirlo appena disponibile.
- **Tempi base City Hall di alto livello** — heaven-guardian: es. CH25 126 d 3 h, CH24 35 d 23 h / riseofkingdomshandbook: i tempi base pubblicati per i livelli alti sono incoerenti; usare il pannello. *Scelta del bot:* Il bot legge il timer in gioco.
- **Numero di fasi MGE** — riseofkingdomsguides: 6 fasi (5 x 24 h + Final Sprint 48 h) / heaven-guardian: 5 fasi classiche + Final Sprint trattata come sesta finestra / riseofkingdomshandbook: formato 'stabilito' a 6 attivita'; guide commerciali recenti citano una fase di sviluppo comandanti non verificata. *Scelta del bot:* Leggere le fasi dal pannello dell'evento.
- **Ciclo dei guardiani degli Holy Sites** — theriagames 2025-02-12: spawn 00:00 e 12:00 UTC, restano 11 ore / heaven-guardian 2026-08-03: ciclo di 12 ore; orari dipendenti da reset/regno. *Scelta del bot:* Controllare dopo le 00:00 e le 12:00 UTC e seguire gli annunci del regno.
- **Formato Ceroli Crisis** — heaven-guardian: squadra di 4 giocatori (Ceroli Assault separato da 12) / riseofkingdomshandbook: raid cooperativo con altri governatori (numero non specificato). *Scelta del bot:* Nessun impatto: il bot non lo gioca in autonomia.
- **Gift codes 'attivi' a settembre 2026** — heaven-guardian 2026-09-18: segnalati attivi: 4t2q6axhjk, lilith13th, ROKRMDAN26, vvrw9aq6y6, ROKTHX2025, RISEIN2025, Rokhaunt25 / riseofkingdomshandbook 2026-09-09: ROMERALLYR segnalato (rkg 03-09-2026); 4t2q6axhjk e ROKRMDAN26 contestati; vvrw9aq6y6 scaduto il 28-02-2026 15:59 UTC; lilith13th, ROKTHX2025, RISEIN2025, Rokhaunt25 non confermati. *Scelta del bot:* Il bot prova un codice solo se fornito dall'utente o annunciato in gioco e registra l'esito.
- **Quando lasciare un'alleanza** — riseofkingdomshandbook beginner hub 2026-09-09: se ha meno di 40 membri attivi, lasciarla / riseofkingdomshandbook alliance hub 2026-09-09: guardare a help e rally affidabili piu' che a un numero minimo di membri. *Scelta del bot:* Il bot misura l'attivita' (aiuti ricevuti/ora, rally di forti, guardian run) e la riporta all'utente; non cambia alleanza da solo.
- **Uso degli Universal speedup** — riseofkingdomsguides beginner 2026-01-02: usare gli Universal solo per la tecnologia / heaven-guardian speedups 2026-08-04: Universal per il collo di bottiglia attuale, sempre dopo gli specifici. *Scelta del bot:* Default del bot: Universal alla ricerca salvo sblocchi critici; sempre dopo gli specifici.

## 7. Fonti

Tutte lette il 2026-09-28 salvo dove indicato (dati riusati da `data/truppe_pve.json` e `data/fragments/armamenti.json`, letti il 2026-09-27).

- [allclash.com](https://www.allclash.com/the-only-rise-of-kingdoms-gathering-guide-you-really-need/) — pagina: 2020-02-21; letta: 2026-09-27
- [gamesguideinfo.com](https://www.gamesguideinfo.com/rise-of-kingdoms/commander-talent-tree/830000032-Peacekeeping) — pagina: s.d.; letta: 2026-09-27
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-academy-guide/) — pagina: 2026-08-03; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-beginners-guide/) — pagina: 2026-09-02; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-best-civilization-tier-list-2026-guide/) — pagina: 2026-09-01; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-buildings-guide-city-development/) — pagina: 2026-09-02; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-ceroli-crisis-guide-boss-tips/) — pagina: 2026-08-05; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-city-hall-upgrade-guide-level-up-fast/) — pagina: 2026-09-02; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-codes/) — pagina: 2026-09-18; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-commander-sculptures-guide/) — pagina: 2026-09-19; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-courier-station-guide/) — pagina: 2026-08-06; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-dominate-barbarians-forts-guide/) — pagina: 2026-08-03; letta: 2026-09-27
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-earn-spend-alliance-individual-credits/) — pagina: 2026-09-19; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-events-dominate-with-this-guide/) — pagina: 2026-08-03; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-expedition-guide-tips-rewards/) — pagina: 2026-08-03; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-gathering-guide-dominate-resources/) — pagina: 2026-08-12; letta: 2026-09-27
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-gem-farming-guide-best-commanders-tips/) — pagina: 2026-09-02; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-lohars-trial-guide/) — pagina: 2026-08-08; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-maximize-action-points-dominate/) — pagina: 2026-08-03; letta: 2026-09-27
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-peerless-scholar-answers/) — pagina: 2026-09-19; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-runes-find-use-magical-boosts/) — pagina: 2026-08-03; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-scout-villages-caves-for-fast-growth/) — pagina: 2026-09-02; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-speedups-the-ultimate-guide-to-domination/) — pagina: 2026-08-04; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-titles-guide-to-maximize-your-buffs/) — pagina: 2026-08-04; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-unlock-t5-troops-dominate/) — pagina: 2026-09-19; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-vip-guide-level-up-fast-get-rewards/) — pagina: 2026-09-02; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-vip-shop-guide-dominate-maximize-benefits/) — pagina: 2026-09-02; letta: 2026-09-28
- [heaven-guardian.com](https://heaven-guardian.com/rise-of-kingdoms-win-mightiest-governor-event/) — pagina: 2026-09-02; letta: 2026-09-28
- [kibezaka.com](https://www.kibezaka.com/2021/11/tips-arms-training-rise-of-kingdoms.html) — pagina: 2021-11; letta: 2026-09-27
- [ldshop.gg](https://www.ldshop.gg/blog/rise-of-kingdoms/anniversary-special.html) — pagina: 2026-08-27; letta: 2026-09-28
- [ldshop.gg](https://www.ldshop.gg/blog/rise-of-kingdoms/halloween-guide.html) — pagina: 2026-09-22; letta: 2026-09-28
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/farming-gathering-guide/) — pagina: 2026-01-02; letta: 2026-09-27
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/formations-armaments-and-inscriptions-guide-rok/) — pagina: 2026-01-02; letta: 2026-09-27
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/golden-kingdom-event-guide-rok/) — pagina: 2026-01-02; letta: 2026-09-28
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/how-do-you-get-vip-points-in-rise-of-kingdoms/) — pagina: 2026-01-02; letta: 2026-09-28
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-1-0-83-eternal-city-update/) — pagina: 2026-01-02; letta: 2026-09-28
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-1-0-91-moon-and-star-update/) — pagina: 2026-01-02; letta: 2026-09-27
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-arms-training-event/) — pagina: 2026-01-02; letta: 2026-09-27
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-barbarians-and-barbarian-forts/) — pagina: 2026-01-02; letta: 2026-09-27
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-beginners-guide/) — pagina: 2026-01-02; letta: 2026-09-28
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-best-civilization-tier-list/) — pagina: 2026-01-02; letta: 2026-09-28
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-gems/) — pagina: 2026-01-02; letta: 2026-09-28
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-life-hacks-tips-and-tricks/) — pagina: 2026-01-02; letta: 2026-09-28
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/rise-of-kingdoms-runes/) — pagina: 2026-01-02; letta: 2026-09-27
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/spring-symphony-and-esmeraldas-prayer-event-guide/) — pagina: 2026-01-02; letta: 2026-09-28
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/the-mightiest-governor-event/) — pagina: 2026-01-02; letta: 2026-09-28
- [riseofkingdomsguides.com](https://riseofkingdomsguides.com/wheel-of-fortune-guide-in-rise-of-kingdoms/) — pagina: 2026-01-02; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-guide-hub) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-mobilization-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-alliance-shop-guide) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-ark-of-osiris-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-arms-training-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-beginners-guide-hub) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-civilization) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-best-events-to-spend-on) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-buildings-guide-hub) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-ceroli-crisis-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-champions-of-olympia-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-city-hall-requirements) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-event-calendar-hub) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-expedition-guide) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-f2p-guide) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-gift-codes) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-golden-kingdom-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-healing-hospital-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-how-to-change-civilization) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-ians-ballads-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-karuak-ceremony-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-kingdom-titles-guide) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-lohars-trial-guide) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-lyceum-of-wisdom-guide) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-mightiest-governor-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-more-than-gems-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-resources-guide-hub) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-shadow-legion-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-speedups-guide) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-sunset-canyon-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-t5-troops-unlock-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-tavern-keys-guide) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-vip-levels-guide) — pagina: 2026-08-18; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-wheel-of-fortune-guide) — pagina: 2026-09-09; letta: 2026-09-28
- [riseofkingdomshandbook.com](https://riseofkingdomshandbook.com/guides/riseofkingdoms-zenith-of-power-guide) — pagina: 2026-08-18; letta: 2026-09-28
- [rok.guide (copia Wayback Machine del 2024-04-17)](https://web.archive.org/web/20240417223657/https://www.rok.guide/silk-road-speculators/) — pagina: 2019-05-24; letta: 2026-09-28
- [rok.guide (copia Wayback Machine del 2024-07-25)](https://web.archive.org/web/20240725150508/https://www.rok.guide/silk-road-speculators-event/) — pagina: 2019-05-27; letta: 2026-09-28
- [rok.lilith.com (ufficiale Lilith)](https://rok.lilith.com/probability/) — pagina: s.d.; letta: 2026-09-27
- [rokdbot.com](https://rokdbot.com/en/blog/action-points-management-guide-rok-2026) — pagina: 2026-06-13; letta: 2026-09-27
- [theriagames.com](https://theriagames.com/guide/rise-of-kingdoms-holy-sites-guide/) — pagina: 2025-02-12; letta: 2026-09-27
- [touchscreengaming.com](https://touchscreengaming.com/formations-guide/) — pagina: 2025-10-10; letta: 2026-09-27

Irraggiungibili in questa sessione: https://rok.guide/ (irraggiungibile (indicato nelle istruzioni; usato solo tramite Wayback Machine per Silk Road)); https://riseofkingdoms.fandom.com/ (irraggiungibile (indicato nelle istruzioni)); https://www.ldshop.gg/sitemap.xml e pagine ldshop via curl (HTTP 403 (curl); lette via WebFetch); https://www.bluestacks.com/blog/game-guides/rise-of-kingdoms/ (HTTP 500 (WebFetch)); https://www.allclash.com/?s=silk+road+rise+of+kingdoms (HTTP 403 (WebFetch)); https://heaven-guardian.com/sitemap.xml, /sitemap_index.xml (connection reset (curl); usata post-sitemap.xml); https://riseofkingdomsguides.com/sitemap.xml (pagina Bot Verification (curl); indice letto via WebFetch); https://web.archive.org/cdx (ricerche wildcard rok.guide tavern/beginner) (timeout / 'Temporarily Offline').
