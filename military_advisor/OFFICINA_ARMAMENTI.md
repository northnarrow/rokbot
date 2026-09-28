# Officina armamenti: come funziona (Formazioni, Armamenti, Iscrizioni, State Forum)

> **Cerchi la guida da leggere? È `GUIDA_ARMAMENTI.md`.**
> Questo file è il dossier: fonti, date, conflitti fra guide e cose non confermate.

> **Stato: ricostruito da 32 fonti online e ricontrollato il 28/09/2026 su note ufficiali Lilith.**
> **Il giro sul telefono è stato fatto il 28/09/2026 (test T08): il percorso dei menu e i nomi italiani dei pulsanti sono ora confermati sul client reale.** Vedi la sezione "Percorso confermato sul telefono".
> Dati completi, ognuno con fonte e data: `data/armamenti.json`.
> Coordinate dei pulsanti: `riferimenti_ui/layout_1560x720.json`.

## In breve

- Ogni comandante **primario** ha una **formazione**: un bonus fisso, per esempio Wedge dà +5% danno da abilità.
- La formazione ha **4 slot** e in ogni slot va un **armamento**.
- Ogni armamento ha **3 attributi casuali** e può avere **0-2 iscrizioni**, cioè attributi extra più forti.
- Gli armamenti si trovano nello **State Forum**, l'edificio in città, con **Travel** e **Dispatch**, che costano solo punti azione (AP).
- Si possono **trasmutare**, cioè ritirare gli attributi, **convertire** su un'altra formazione e **riciclare** per monete.
- Queste tre operazioni consumano materiali rari, quindi il bot chiede sempre conferma.

## 1. Formazioni

Il bonus vale solo per il comandante **primario**. La formazione si cambia quando il comandante è in città.

| Formazione | Effetto | Per chi |
|---|---|---|
| Arch | +5% danno da attacco normale | primari da danno normale |
| Wedge | +5% danno da abilità | nuker, la più usata |
| Wedge II | +12% danno da abilità | nuker di fine gioco |
| V | modalità a distanza, 1 attacco al secondo | situazionale |
| Echelon | buff percentuali ad altre truppe ×1.2 | supporto in rally e guarnigione |
| Hollow Square | −2% danno subito | tank, difesa |
| Line | +10% velocità di raccolta | **raccolta** |
| Double Line | +10% velocità di marcia verso i barbari | **catene di barbari** |
| Triple Line | +5% velocità di marcia | mobilità |
| Testudo | −5% danno con scudo attivo, +2.5% cure | comandanti con scudi |
| Circle | +5% cure ricevute | healer |
| Staggered | +15% velocità verso rally e guarnigioni | chi si unisce ai rally |
| Delta | +10% danno Combo | comandanti Combo, come Arthur |
| Tercio | in guarnigione i bonus degli armamenti valgono per **tutti** i tipi di truppa | **difesa della città** con truppe miste |
| Pincer | +10% danno Smite | comandanti Smite, come Bai Qi e Wallace |

Verifica su seconda fonte (28/09):
- Wedge 5% e Wedge II 12% sono confermati dalle note ufficiali (patch 1.1.06).
- Pincer 10% è l'ultimo valore documentato.
- La fusione di Wedge al 12% e il Pincer al 12% vengono da un solo sito non ufficiale: nessuna nota Lilith li conferma.

Il valore reale lo leggiamo sul telefono.

## 2. Da dove arrivano gli armamenti

| Fonte | Costo | Note |
|---|---|---|
| **Travel** | 20 AP, o 200 AP per ×10 | State Forum liv. 1. Da 5 a 20 viaggi al giorno secondo il livello. Il gioco offre fino a 120 viaggi extra in gemme: **vietati al bot** |
| **Dispatch** | 30–150 AP secondo la rarità | State Forum liv. 10. Da 3 a 8 al giorno. Si forma una squadra di comandanti che soddisfa i requisiti; se li soddisfa, il recupero è quasi certo |
| Formation Choice Chest | monete del riciclo o eventi | scegli la formazione e ricevi un armamento casuale. Leggendaria: 12.47% armamento leggendario con iscrizione |
| Armament Shop | monete e valute evento | vende Transmutation Stone e iscrizioni speciali |
| Evento "Armament, Reveal Thyself" | Armament Tickets | 24.5% leggendario, 3.38% leggendario con iscrizione |

Le probabilità vengono dalla pagina ufficiale Lilith: rok.lilith.com/probability.

**State Forum per livello:**

| Livello | Travel al giorno | Dispatch al giorno | Probabilità Major Dispatch |
|---|---|---|---|
| 1 | 5 | – | – |
| 10 | 13 | 3 | 1.5% |
| 15 | 16 | 5 | 1.5% |
| 20 | 18 | 7 | 2% |
| 25 | 20 | 8 | 3% |

Per salire di livello servono **Sage's Testimony**: è la risorsa più limitante. Dal livello 25 non se ne ricevono più.

## 3. Attributi

Ogni armamento è di uno di 4 tipi: Scroll, Instrument, Flag, Emblem. Ha 3 attributi pescati da una lista ufficiale di 21.

| Attributo | Leggendario | Epico | Elite |
|---|---|---|---|
| Attacco, Difesa, Salute di un tipo di truppa; velocità di marcia | 1.5–3.5% | 1–2.5% | 0.5–2% |
| Danno totale (All Damage) | 0.5–2% | 0.5–1.5% | 0.5–1% |
| Velocità di raccolta dell'oro | 5–7.5% | 4–6% | 3–5% |
| Carico truppe | 4–7% | 3–5% | 2–4% |
| Danno ai barbari, riduzione del danno dai barbari | 4–7% | 3–5% | 2–3% |

**Slot e famiglie:** ogni slot accetta una sola famiglia di armamenti. Per esempio, nella Wedge lo slot in alto accetta "Epics of Olympia" e quello sotto "Honors of the Pantheon". La mappa completa famiglia–slot la leggiamo sul telefono.

**Priorità consigliate dalle fonti:**

| Uso | Slot 1 | Slot 2 | Slot 3 | Formazione |
|---|---|---|---|---|
| Fanteria | Attacco fanteria | Difesa fanteria | Salute fanteria o All Damage | Wedge, Hollow Square, Pincer |
| Cavalleria | Attacco cavalleria | Difesa cavalleria | Salute cavalleria o All Damage | Wedge, Delta |
| Arcieri | Attacco arcieri | Difesa arcieri | Salute arcieri o All Damage | Wedge |
| Raccolta | Velocità raccolta oro | Carico truppe | qualsiasi | Line |
| Barbari | Attacco | Difesa | Danno ai barbari o riduzione dai barbari | Double Line per le catene, Wedge per i forti |
| Guarnigione | Attacco | Difesa | Salute o All Damage | Tercio, Hollow Square |

## 4. Iscrizioni

- Sono un 4° attributo, a volte anche un 5°, con bonus più grandi: danno da abilità, All Damage, contrattacco. Dipendono dalla formazione.
- Rarità: Common, Rare, Special.
- Su un armamento leggendario la probabilità è 85.7% Common, 6.6% Rare, 0.66% Special, e 7.1% di averne due.
- Dopo 150 armamenti leggendari della stessa formazione, uno è **garantito** con iscrizione Rare o superiore.
- La **wishlist** permette di scegliere quale armamento Special ricevere.
- Regola d'oro: **tieni** sempre i pezzi con iscrizioni Rare o Special e trasmuta gli attributi attorno a loro.

## 5. Modificare gli armamenti: consuma materiali rari, quindi **conferma obbligatoria**

| Operazione | Cosa fa | Materiale | Limiti |
|---|---|---|---|
| **Transmute** | ritira i 3 attributi e conserva le iscrizioni. Solo leggendari con iscrizione | Transmutation Stone | 10 tentativi per pezzo. Con un attributo di combattimento bloccato: ogni 10 tentativi è garantito un attributo dello stesso tipo di truppa, ogni 30 uno da almeno 2.5%. Puoi bloccare 1-2 attributi, a un costo maggiore. Dopo ogni tentativo scegli se tenere il nuovo risultato. La Transmutation Crystal azzera il contatore |
| **Convert** | sposta un leggendario su un'altra formazione | Conversion Stone, molto rara | solo verso lo **stesso slot**. Iscrizioni Rare e Special si adattano, attributi invariati |
| **Recycle** | distrugge il pezzo in cambio di monete | nessuno | Elite 1 argento, Epico 2, Epico con iscrizione 4, Leggendario 1 oro, Leggendario con iscrizione 2. **Chiede la password secondaria** |
| Honing | alza un attributo di +0.2% a volta, fino a +3.5%. All Damage: +0.1%, fino a +2% | Honing Stones, dalla sezione Autarch del negozio iscrizioni | confermato dalle note ufficiali della patch 1.1.03 |

Materiali rari che il bot non tocca mai senza il tuo sì:
- Sage's Testimony, Transmutation Stone e Crystal, Conversion Stone, Armament Converter.
- Monete d'oro e d'argento, Autarch Testimony, Conquest Coins, Honing Stones, Armament Tickets.
- Formation Choice Chest.

## 6. Attenzione: "Arms Training" non c'entra

"Arms Training" è un **evento** di 3 giorni con 5 tentativi al giorno. Si combatte ripetutamente Lohar vicino alla città con una sola marcia; tornare in città azzera la catena di punti. Non ha niente a che vedere con gli armamenti.

## 7. Cosa è confermato e cosa no

**Confermato dalle fonti:**
- Travel e Dispatch si fanno dallo State Forum. Esistono i pulsanti "Travel x10" e "Quick Dispatch".
- La formazione ha 4 slot e si assegna in città.
- L'inventario armamenti ha: blocco dei pezzi, ordinamento, icone delle formazioni compatibili, riciclo con password secondaria.
- Esistono Transmute, Convert, Recycle, Wishlist, loadout per comandante (fino a 30) e scelta di 3 formazioni preferite per Travel e Dispatch.

**Ancora da verificare sul telefono:**
- I valori attuali di Wedge e Pincer.
- Dove stanno Transmute e Convert: nella schermata Formazione non compaiono, potrebbero essere dentro il Negozio degli armamenti o legati alla password secondaria.
- Il contenuto del Negozio degli armamenti e i suoi prezzi.

## 7b. Percorso confermato sul telefono (test T08 del 28/09/2026)

Client in **italiano**, schermo 1560x720. Non è servito passare dallo State Forum: l'officina
si apre direttamente dal comandante.

**Menu → Comandante → icona Formazione** (l'icona dorata a quattro nodi sul fianco destro del
comandante, sotto l'albero dei talenti).

Nomi italiani dei pulsanti, prima sconosciuti:

| Inglese | Italiano | Dove |
|---|---|---|
| Travel | **Viaggiare** | pannello Fonte, pulsante "Vai" |
| Dispatch | **Spedisci** | pannello Fonte, pulsante "Vai" |
| Armament Shop | **Negozio degli armamenti** | pannello Fonte, pulsante "Vai" |
| Recycle | **Ricicla** | schermata Formazione, in basso a destra |
| Wishlist | **Lista dei desideri** | schermata Formazione, in basso a destra |
| Codex | **Codice** | schermata Formazione, in basso a destra |

**Schermata Formazione:** mostra il nome della formazione, il suo bonus, i 4 slot attorno al
comandante e la lista "Info armamento" con i bonus sommati. Esempio letto su Scipione
l'Africano: *Formazione a cuneo*, +12% danni da abilità.

**Slot armamento → "Seleziona armamento":** nome, formazione compatibile, iscrizione
("Nessuna inscrizione" se vuoto), i **3 attributi**, il comandante che lo equipaggia e il totale
posseduto. Esempio: *Epopee di Olimpia*, raccolta oro +7,2%, difesa fanteria +3,3%, riduzione
danni dai barbari +6,8%. Pulsanti **Potenzia** e **Rimuovi**: entrambi da non premere senza
conferma.

**Codice:** catalogo di sola lettura di tutti gli armamenti, diviso per rarità
(Leggendario / Epico / Élite) e raggruppato per formazione (ad arco, a cuneo, a V), con
l'elenco completo delle iscrizioni e un pulsante **Fonte** per ogni pezzo. È la fonte interna
al gioco da usare per riempire `data/armamenti.json` al posto delle fonti online.

## 8. Cosa propongo di automatizzare, dopo il tuo ok sul giro manuale

1. **Solo lettura:** per ogni comandante usato leggo formazione, 4 armamenti, attributi e iscrizioni, e li salvo nel profilo account.
2. **Automatico, senza rischio:** ogni giorno usare i Travel e i Dispatch disponibili, che costano solo AP. Imposto prima le 3 formazioni preferite.
3. **Solo con conferma:** Transmute, Convert, riciclo di epici e leggendari, acquisti con monete d'oro, qualsiasi uso di Sage's Testimony.
4. **Mai:** qualsiasi acquisto o viaggio in gemme.

Il blocco è già nel codice. `MilitaryAdvisor.gate()` rifiuta le gemme e chiede conferma per ogni materiale della lista rari.
