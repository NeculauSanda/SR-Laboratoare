[← Înapoi la indexul general](../../README.md) | 🇬🇧 English Version TBA

**Acces Rapid:** [📄 Vezi `my_hash.py`](../my_hash.py)

---

# Laborator 4: Dezvoltarea unei ontologii în WebProtégé

În cadrul acestui laborator veți crea o ontologie pentru a reprezenta cunoștințele unui domeniu.

- **Editor web ontologie:** [WebProtégé Stanford](https://webprotege.stanford.edu/)
- **Tutorial ontologie în WebProtégé:** [Introduction to RDF and OWL](https://csiro-enviro-informatics.github.io/info-engineering/tutorials/tutorial-intro-to-rdf-and-owl.html)

## Obiective

1. Înțelegerea conceptelor fundamentale ale web-ului Semantic (*clase*, *subclase*, *proprietăți*, *indivizi*).
2. Utilizarea platformei **WebProtégé** pentru crearea vizuală a unei ontologii.
3. Validarea ontologiei prin export și vizualizare grafică.

## Cerințe de implementare

### 1. Studierea materialului introductiv

- Parcurgeți tutorialul introductiv despre **RDF** și **OWL** disponibil la adresa: [Introduction to RDF and OWL](https://csiro-enviro-informatics.github.io/info-engineering/tutorials/tutorial-intro-to-rdf-and-owl.html).

### 2.Crearea proiectului în WebProtégé

1. Deschideți platforma web în browser: [WebProtégé Stanford](https://webprotege.stanford.edu/).
2. Creați un proiect nou folosind ca punct de plecare exemplul clasic de pizza din tutorialul menționat anterior.
3. Modelați elementele ontologiei direct în interfața vizuală:
- *Clase* și *subclase* (ex.: `Pizza` => `MargheritaPizza`, `Topping` => `CheeseTopping`).
- *Indivizi* / *Instanțe* (ex.: `margheritaPizza1`, `mozzarella1`).
- *Proprietăți de obiect* / *Object Properties* (ex.: `hasTopping`).
- *Proprietăți de date* / *Datatype Properties* (ex.: `hasPrice`, `hasCalories`).

### 3. Adăugarea identificatorului propriu securizat

Pentru a atesta realizarea laboratorului fără a expune date cu caracter personal, fiecare student va include în ontologie un *individ* care îl reprezintă, identificat printr-un **hash SHA-256 generat din emailul instituțional**.

Puteți genera rapid hash-ul propriu rulând codul de Python din fișierul [`my_hash.py`](../my_hash.py).

#### Ce veți adăuga în WebProtégé:

1. Creați o *clasă* suplimentară (ex.: `Student` sau `User`).
2. Creați un *individ* dedicat vouă (ex.: `euStudent`).
3. Adăugați o *proprietate de date* (ex.: `hasUserHash`) căreia îi asociați ca valoare șirul hexazecimal rezultat în urma rulării script-ului de Python.

### 4. Partajarea proiectului

1. Din interfața *WebProtégé*, folosiți opțiunea *Share Project* pentru a genera un link de acces public (viewer sau editor).
2. Creați un fișier text local (ex: `ontologie.txt`) și inserați în el link-ul generat.

### 5. Livrabile obligatorii

- **Repository:** (opțional) Dacă doriți, actualizați repository-ul de *GitHub*/*GitLab* adăugând ontologia voastră exportată în format *XML*.
- **Predare:** Încărcați pe platforma Moodle un fișier cu extensie `.txt` care conține exclusiv link-ul către ontologia voastră share-uită conform pasului 4.

## Barem de notare

| Nr. | Criteriu    | Punctaj |
| - | -------- | ------- |
| 1 | Structura ierarhică: Ontologia conține cel puțin 2 clase principale și minimum 2 subclase pentru fiecare. | 20p |
| 2 | Populare cu indivizi: Există cel puțin 5 indivizi (instanțe) creați în clasele definite (inclusiv individul care reprezintă studentul). | 20p |
| 3 | Proprietăți definite: Sunt definite cel puțin 3 proprietăți de obiect (*Object Properties*, ex.: `hasTopping`) și cel puțin 3 proprietăți de date (*Datatype Properties*, ex.: `hasPrice`, `userHash`). | 20p |
| 4 | Valori asignate și securitate: Proprietățile definite au completate valori reale pentru cel puțin 2 dintre indivizi, incluzând obligatoriu valoarea de tip hash a ID-ului de *Microsoft Teams* pentru identificarea corectă a autorului. | 20p |
| 5 | Funcționalitate și livrare: Ontologia este complet funcțională, iar fișierul text cu link-ul de *Share* din *WebProtégé* este încărcat corect în assignment. | 20p |
