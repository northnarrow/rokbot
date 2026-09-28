# Armamenti: guida pratica

Questa è la versione da leggere. Le fonti, i conflitti fra guide e le cose ancora
da verificare stanno in `OFFICINA_ARMAMENTI.md`; i dati grezzi in `data/armamenti.json`.

Aggiornata il 28/09/2026. I nomi italiani sono quelli letti sul tuo client.

---

## In due parole

Ogni comandante **primario** ha una **formazione**. La formazione dà un bonus fisso e ha
**4 slot**. In ogni slot va un **armamento**, e ogni armamento porta **3 attributi** più,
eventualmente, delle **iscrizioni**.

Tre cose da tenere a mente fin da subito:

1. Il bonus della formazione vale **solo per il comandante primario**. Sul secondario non conta.
2. **Ogni slot è riservato a un armamento preciso.** Non scegli quale pezzo mettere dove: scegli
   *quale copia* di quel pezzo mettere. Nel Cuneo, per esempio, lo slot in alto vuole
   *Epopee di Olimpia* e nessun altro.
3. Gli attributi sono **casuali**. Due copie dello stesso armamento possono valere molto
   diversamente. È qui che si gioca la partita.

### I 4 slot sono sempre gli stessi quattro tipi

Verificato nel Codice del gioco il 28/09/2026: ogni formazione ha esattamente **una
Pergamena, uno Strumento, una Bandiera e un Emblema**. Cambiano i nomi, non la struttura.

| Formazione | Pergamena | Strumento | Bandiera | Emblema |
|---|---|---|---|---|
| **Arco** | Pergamena del nord | Corno del nord | Stendardo di battaglia del Nord | Emblema del Nord |
| **Cuneo** | Epopee di Olimpia | Direttore del coro di Olimpia | Stendardo del Pantheon | Onori del Pantheon |
| **Cuneo II** | Messaggio dell'araldo | Strumento dell'araldo | Insegna dell'araldo | Marchio dell'araldo |
| **V** | Cronache del drago | Tamburo di guerra imperiale | Stendardo del drago | Decreto imperiale |
| **Sfalsata** | Un record di vendetta | Ode al guerriero | Gloria di battaglia | Sigillo di guerra |
| **Quadrata** | Tomo di Fleur de Lys | Luto di Fleur de Lys | Stendardo Fleur de Lys | Scudo Fleur de Lys |
| **In linea** | Libro di Horus | Arpa di Horus | Taglia di Horus | Occhio di Horus |

*(tabella in costruzione: mancano le altre formazioni e le rarità Epico ed Élite)*

**Come è stata ricavata, e cosa resta da confermare.** I nomi vengono dal Codice del gioco,
letti uno per uno. L'abbinamento nome → formazione viene invece dall'**ordine dei gruppi nel
pannello**, quindi è un'inferenza: se un gruppo venisse saltato, le righe slitterebbero tutte
di una posizione. La verifica definitiva è nell'inventario (Articoli → Armamenti), dove il
pannello di destra scrive la formazione sotto il nome, per esempio *"Per Formazione ad arco"*.

Quindi sapere **quali 4 pezzi ti servono** è immediato, una volta scelta la formazione.
Tutto il resto del lavoro è procurarsi la copia migliore di ognuno.

---

## Le formazioni

| Formazione | Bonus | A cosa serve |
|---|---|---|
| **Cuneo** (Wedge) | +12% danno da abilità *(letto sul client)* | La più usata. Quasi tutti i nuke sono abilità |
| **Cuneo II** | +12% danno da abilità | Versione potenziata, per chi ha già investito sul Cuneo |
| **Arco** (Arch) | +5% danno da attacco normale | Comandanti che picchiano di attacco base, non di abilità |
| **Linea** (Line) | +10% velocità di raccolta | Raccolta. È la formazione dei raccoglitori |
| **Tenaglia** (Pincer) | +10% danno smite | Comandanti smite |
| **Delta** | +10% danno combo | Comandanti combo |
| **Quadrato** (Hollow Square) | −2% danno subito | Difesa pura |
| **Testuggine** (Testudo) | −5% danno quando hai uno scudo, +2.5% guarigione | Difensivi con scudo |
| **Cerchio** (Circle) | +5% a tutte le guarigioni ricevute | Sostegno |
| **Echelon** | Buff dati agli altri ×1.2 (max +5%) | Comandanti di supporto in rally |
| **Tercio** | In guarnigione, i bonus degli armamenti valgono per **tutti** i tipi di unità | Difesa città con truppe miste |
| **Linea Tripla** | +5% velocità di marcia | Spostamenti |
| **Sfalsata** (Staggered) | +15% velocità di marcia verso rally o guarnigione | Arrivare in tempo sui rally |
| **Doppia Linea** | +10% velocità di marcia verso i barbari | Catene di barbari |
| **V** | Converte la truppa in modalità a distanza | Solo comandanti col talento adatto |

**Nota sulla Tenaglia:** il 10% è l'ultimo valore documentato (ott 2025). Un aggiornamento
di agosto 2026 avrebbe portato il bonus a 12%, ma non è confermato: vedi i conflitti in
`OFFICINA_ARMAMENTI.md`.

**Se devi scegliere dove investire per primo:** Cuneo, perché copre la maggior parte dei
comandanti da combattimento, e Linea, perché la raccolta gira tutto il giorno.

---

## Gli attributi: la regola che conta

**Allinea gli attributi al tipo di truppa del comandante.** Un armamento con bonus alla
fanteria su un comandante di cavalleria è sprecato, per quanto alti siano i numeri.

Ordine di importanza, in pratica:

1. **Attacco / Difesa / Salute del tipo di truppa giusto** — il grosso del valore.
2. **Danno da abilità**, se il comandante vive di abilità (quindi quasi sempre, in Cuneo).
3. **Velocità di marcia** — utile ovunque, decisiva per rally e barbari.
4. **Velocità di raccolta / carico** — solo sui raccoglitori, dove però vale tantissimo.
5. **Riduzione danni contro i barbari** — di nicchia, ottima se fai molto PvE.

Attributi fuori tipo (cavalleria su un fante) contano **zero**. Non farti ingannare da un
7,2% se è sull'unità sbagliata.

---

## Iscrizioni

Sono un attributo **extra** che si aggiunge ai 3 normali, e sono più forti di quelli.
Hanno tre livelli di rarità: comune, raro, speciale.

Arrivano insieme all'armamento oppure dal Negozio delle iscrizioni. Un armamento può avere
da 0 a 2 iscrizioni.

**Le iscrizioni sopravvivono alla trasmutazione.** È la ragione per cui un pezzo con una
buona iscrizione e attributi mediocri vale più di quanto sembri: gli attributi si possono
rifare, l'iscrizione no.

---

## Trasmutazione: rifare gli attributi

Rilancia i dadi sui 3 attributi, **tenendo le iscrizioni**.

- Puoi **bloccare** alcuni attributi perché non vengano rilanciati. Più ne blocchi, più
  pietre di trasmutazione costa.
- Il rilancio è **completamente casuale**. Non c'è modo di indirizzarlo.
- **Massimo 10 trasmutazioni per armamento.** Finite quelle, l'armamento è chiuso.
- I **cristalli di trasmutazione** azzerano il contatore e te ne ridanno 10.

**Come usarla senza sprecare:** trasmuta solo pezzi che hanno già qualcosa che vale la pena
tenere, cioè un'iscrizione buona o un attributo forte da bloccare. Trasmutare un pezzo
mediocre e senza iscrizioni è buttare pietre: tanto vale cercarne uno migliore viaggiando.

---

## Affinamento (Honing): limare i numeri

Alza il valore di un attributo, a piccoli passi.

| Tipo di attributo | Ogni affinamento | Tetto massimo |
|---|---|---|
| Normale (attacco, difesa, salute, marcia…) | +0,2% | +3,5% |
| Danno totale (*all damage*) | +0,1% | +2,0% |

Il danno totale sale la metà e si ferma prima, ma è l'attributo che vale di più: sceglilo
con cognizione, non a caso.

**Affina solo i pezzi definitivi.** Su un armamento che poi trasmuti è lavoro buttato.

---

## Conversione e riciclo

- **Conversione:** sposta un armamento su un'altra formazione. Costa pietre di conversione,
  comprabili nel Negozio.
- **Riciclo:** distrugge il pezzo e ti dà monete, con cui compri materiali di potenziamento
  o forzieri di scelta formazione.

**Attenzione:** il riciclo è irreversibile. Il gioco chiede la password secondaria per i
pezzi di valore — non disattivarla.

---

## Come si ottengono

| Via | Nome italiano | Costo | Note |
|---|---|---|---|
| Travel | **Viaggiare** | ~20 AP a viaggio | Il metodo quotidiano. Esiste "Viaggia x10" |
| Dispatch | **Spedisci** | 30–150 AP | Missioni di spedizione. C'è "Spedizione rapida" |
| Shop | **Negozio degli armamenti** | monete | Anche iscrizioni e pietre |

Entrambi costano **solo punti azione**, non risorse e non gemme. Gli AP si rigenerano da
soli: se la barra è piena, stai sprecando. Imposta le **3 formazioni preferite** prima di
viaggiare, così i pezzi che escono sono quelli che ti servono.

C'è anche l'**auto-riciclo** dentro Viaggiare: i pezzi che rispettano le condizioni che
imposti vengono riciclati da soli, senza riempirti l'inventario.

---

## Dove si trova nel gioco

Percorso verificato sul client italiano il 28/09/2026:

```
Menu → Comandante → icona Formazione
```

È l'icona dorata a quattro nodi sul fianco destro del comandante, sotto l'albero dei talenti.
**Non serve passare dallo State Forum**, che resta l'edificio che sblocca il sistema e ne
determina i limiti (Viaggiare dal livello 1, Spedisci dal livello 10).

Da lì:

- **Slot** attorno al comandante → apre "Seleziona armamento", con nome, iscrizione, i 3
  attributi e quanti ne possiedi.
- **Lista dei desideri** → i pezzi che stai cercando.
- **Codice** → il catalogo di **tutti** gli armamenti del gioco, diviso per rarità
  (Leggendario / Epico / Élite) e raggruppato per formazione, con l'elenco completo delle
  iscrizioni e un pulsante **Fonte** per ogni pezzo.
- **Ricicla** → distrugge per monete.

**Il Codice è la fonte migliore che esista su questo argomento**, e sta dentro il gioco.
Nessuna guida online pubblica la tabella formazione → 4 armamenti: quelle che ce l'hanno la
mettono dietro abbonamento, le altre rimandano ai video.

---

## Le regole del bot

- **Mai gemme.** Nessun viaggio, acquisto o velocizzazione in gemme.
- **Conferma obbligatoria** per trasmutazione, conversione, affinamento e riciclo di pezzi
  epici o leggendari: consumano materiali rari.
- **Viaggiare e Spedisci quotidiani** sono automatizzabili senza rischio: costano solo AP.
- **Attenzione:** l'evento *Arms Training* non c'entra con gli armamenti. È un evento di
  addestramento truppe. Non confonderli.

---

## Cosa manca ancora

- La tabella **formazione → 4 armamenti** per tutte le formazioni. Da leggere dal Codice.
- **Trasmutazione e Conversione** non compaiono nella schermata Formazione: vanno cercate
  nel Negozio degli armamenti.
- I valori attuali di Cuneo e Tenaglia dopo gli aggiornamenti del 2026.
