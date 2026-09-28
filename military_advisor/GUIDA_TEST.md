# Test di domani

## Variante A: client ufficiale per PC (quella che useremo)

1. Scompatta `military_advisor.zip` nella cartella del bot.
2. Apri Claude Code sul PC in quella cartella.
3. In un terminale, una volta sola: `pip install mss pygetwindow`
4. Avvia Rise of Kingdoms e lascialo sulla città, in finestra, **non ridotto a icona**.
5. Primo controllo, sola lettura:

```
python -m military_advisor pc-check
```

Deve trovare la finestra del gioco e salvare `test_pc/pc_screenshot_test.png`.

Poi seguo gli stessi test della tabella qui sotto, dal 4 al 17, sulla finestra del PC invece che sul telefono:
- screenshot della finestra;
- lettura delle risorse;
- apertura e chiusura delle schermate;
- nessuna spesa.

Durante i test **non usare il mouse** sul PC: i clic del bot e i tuoi si sovrapporrebbero. La finestra del gioco deve restare visibile, quindi non si può guardare un film sullo stesso schermo mentre il bot lavora.

## Variante B: telefono collegato al PC

Obiettivo: verificare che il bot veda e capisca il gioco **senza spendere niente**.

- Si parte dalla sola lettura, poi si aprono e chiudono schermate.
- Nessun addestramento, acquisto, attacco o uso di oggetti.

Piano completo con fonti: `docs/automazione.md`, passi T00–T18.

## Prima di iniziare (5 minuti)

**Sul PC**
1. Scompatta `military_advisor.zip` dentro la cartella del bot.
2. Serve Python 3.10 o più recente. Per controllare, in un terminale: `python --version`.
3. Installa Android Platform Tools e aggiungi `adb` al PATH: https://developer.android.com/tools/releases/platform-tools

**Sul telefono**
1. Attiva Opzioni sviluppatore → Debug USB.
2. Tienilo in carica con il cavo e attiva "Rimani attivo". Annota com'era, così lo rimettiamo com'era.
3. Nel gioco: Avatar → Settings. Attiva la **conferma per l'uso delle gemme** e imposta la **password secondaria**.
4. Queste due protezioni fermano anche un tocco sbagliato del bot.
5. Apri Rise of Kingdoms e lascialo sulla città.

## Primo comando

Dalla cartella che contiene `military_advisor`:

```
python -m military_advisor phone-check
```

Deve mostrare `[OK]` su tutte le righe e `Rise of Kingdoms in primo piano: SI`. Lo screenshot finisce in `test_telefono/screenshot_test.png`.

Se una riga è `[ERR]`, il messaggio dice cosa sistemare:
- "adb non trovato": manca Platform Tools nel PATH.
- "non autorizzato": sblocca il telefono e accetta "Consenti debug USB".

## I test, in ordine

Tutti sicuri. Dal test 5 in poi apriamo le schermate **a mano la prima volta**: io leggo solo gli screenshot.

| # | Test | Chi tocca lo schermo | Cosa verifichiamo |
|---|---|---|---|
| 1 | Collegamento | nessuno | `adb devices` mostra il telefono come "device" |
| 2 | Comandi del telefono | nessuno | sintassi reale di tap, swipe, risoluzione, schermo sempre acceso |
| 3 | Pacchetto del gioco | nessuno | `com.lilithgame.roc.gp` in primo piano |
| 4 | Screenshot | nessuno | 5 screenshot della città, risoluzione e tempi |
| 5 | Lettura risorse | nessuno | cibo, legno, pietra, oro e gemme letti dall'immagine, 5 su 5 corretti |
| 6 | Profilo e truppe | **tu**, a mano | potenza, AP e truppe lette dagli screenshot |
| 7 | Comandanti | **tu**, a mano | dove sono i pulsanti; schermate abilità, talenti, equipaggiamento e formazione |
| 8 | Officina armamenti | **tu**, a mano | percorso dei menu, Travel, Dispatch, Transmute, Recycle **senza premerli** |
| 9 | Impostazioni | **tu**, a mano | versione del gioco. Non si entra in Account |
| 10 | Modelli grafici | nessuno, sul PC | ritaglio delle icone: avatar, X di chiusura, gemma, eventi, ricerca |
| 11 | Primo tocco del bot | bot | apre e chiude il profilo, verificando ogni passo |
| 12 | Menu | bot | apre e chiude Comandanti, Oggetti, Alleanza, Eventi, Spedizione, **senza premere niente dentro** |
| 13 | Edifici | bot | apre le caserme e l'ospedale **senza premere Addestra o Cura**. La barra risorse deve restare identica |
| 14 | Mappa | bot | cerca un barbaro, la telecamera ci va sopra, **nessuna marcia parte** |
| 15 | Ritorno sicuro | bot | torna alla città da qualsiasi schermata |
| 16 | Risveglio | bot | riaccende lo schermo. Se c'è il PIN si ferma e ti avvisa |
| 17 | Popup | nessuno | catalogo delle finestre inattese: offerte, eventi, conferme |

Con questi test costruiamo anche il **profilo reale del tuo account**, `account_profile.json`. È il dato che manca al consigliere per darti le raccomandazioni vere al posto di quelle d'esempio:

```
python -m military_advisor validate --profile account_profile.json
python -m military_advisor report --profile account_profile.json --json raccomandazioni.json
```

## Cosa NON facciamo domani

- Azioni gratuite ma non reversibili: aiuti d'alleanza, riscossioni, esplorazione. Solo dopo che i test sono stabili, con il tuo ok, una alla volta.
- Azioni che spendono: addestramento, cure, Travel e Dispatch, acquisti, uso di oggetti, invio di marce.
- Queste passano sempre dal blocco di sicurezza del consigliere:
  - **mai gemme**;
  - **conferma** prima di attaccare giocatori o usare materiali rari.

## Regole fisse del bot

- Se compare una **finestra di verifica anti-bot**, il bot si ferma, salva lo screenshot e ti avvisa. Non prova mai a risolverla.
- Impostazioni dell'account, cambio personaggio e cancellazione account: mai toccati.
- Qualsiasi pulsante con il simbolo della gemma o un prezzo: mai toccato.

## Rischio da conoscere

I termini di servizio di Lilith, versione del 15/04/2025, vietano bot e programmi di automazione. Le clausole sono la 17.1.15 e la 17.1.18. La sanzione può arrivare alla sospensione o chiusura dell'account, senza rimborso.

- Nel 2021 Lilith ha dichiarato 167.000 personaggi bannati in 3 mesi.
- Dalla versione 1.1.07 del 30/04/2026 il "Conduct Score" toglie punti a chi usa strumenti di terze parti.

Fonti e testo delle clausole: `docs/automazione.md`, sezione Rischi.
