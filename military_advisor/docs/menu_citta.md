# I due menu della città: Sommario delle code e Comando rapido

Ricerca del 29/09/2026. Sono due cose diverse che è facile confondere, e
nessuna delle due raccoglie le risorse dalle miniere.

## Sommario delle code (icona a righe, in alto a sinistra)

Si sblocca al **Municipio livello 8**. È un cruscotto di sola lettura su tutto
quello che nel villaggio sta lavorando o è fermo.

L'ingranaggio in cima al pannello elenca le sezioni attivabili, e sono
**otto**, tutte qui sotto. Questo è il punto decisivo: **non esiste una
sezione per le risorse pronte**, quindi il pannello non può raccogliere dalle
miniere. Non è nascosta, non c'è.

| Sezione | Cosa mostra |
|---|---|
| Addestramento delle unità | le quattro code di addestramento e i tempi |
| Guarigione delle unità | capacità ospedale e feriti |
| Code per gli edifici | i costruttori, con "Inattivo" quando sono fermi |
| Ricerca tecnologica | ricerca in corso e tempo residuo |
| Donazioni alleanza | oppure "Non in un'alleanza" |
| Produzione materiali | materiali equipaggiamento producibili |
| Acquisizione armamento | Viaggia e Spedisci, con i residui |
| Code di ricognizione | Scout A, B, C, con "In attesa" quando sono fermi |

Cliccare una voce la **evidenzia soltanto**: non esegue l'azione. Fa eccezione
"Donazioni alleanza", che ha una freccia e porta alla schermata.

Lo legge `military_advisor/stato.py`.

## Comando rapido (etichetta in basso a sinistra)

**Non è una lista del villaggio**: è il sistema di *puntamento per le marce*.
Il pannello che apre si chiama "Obiettivi attaccabili" ed è fatto di caselle
che scelgono su cosa il gesto rapido può agire:

- **Truppe:** eserciti nemici radunati, eserciti alleati radunati, truppe da
  campo alleate, barbari
- **Edifici:** città schierata, città nemica, edifici alleanza alleata,
  edifici alleanza nemica, tutti gli edifici
- **Altro:** punti di risorse, rune
- due interruttori: "Tieni premuto per marcia di attacco" e "Sincronizza
  Premi e Trascina"

Serve a mandare marce con un gesto invece che con la sequenza completa. Nulla
a che vedere con la raccolta.

## Conseguenza per il bot

Per svuotare le miniere del villaggio **non c'è una scorciatoia a lista**:
vanno cliccate le nuvolette sopra gli edifici, che è quello che fa
`military_advisor/autonomia.py`.

## Nota sulle fonti

Le guide online su questi due menu sono quasi mute: confermano solo che la
gestione code si sblocca al Municipio 8 e che il Comando rapido è uno schema
di controllo alternativo al Classico su PC. La descrizione completa qui sopra
viene dal gioco, leggendo le opzioni dei pannelli. È lo stesso schema già
visto con gli armamenti: per l'interfaccia, il client batte le guide.

Fonti web consultate:
- https://riseofkingdomsguides.com/faq/
- https://riseofkingdoms.fandom.com/wiki/Frequently_Asked_Questions
- https://theriagames.com/guide/rise-of-kingdoms-builders-hut-guide/
