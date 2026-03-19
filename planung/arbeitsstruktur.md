# Arbeitsstruktur für die Weiterentwicklung des Projekts

## Zweck

Dieses Dokument hält fest, **wie wir in Zukunft inhaltlich und organisatorisch zusammenarbeiten können**, ohne das Projekt unnötig zu verkomplizieren.

Es beschreibt die Arbeits- und Dateistruktur, nicht die allgemeinen didaktischen Leitlinien. Diese stehen zentral in `planung/didaktische-prinzipien.md`.

Die Leitfrage ist:

**Welche wenigen Dateien und Bezugspunkte brauchen wir, damit klar ist, was inhaltlich gemeint ist, wie der Lernweg aussieht und welche Materialien dazu gehören?**

---

## Grundidee

Wir halten die Struktur absichtlich klein.

Für ein Thema brauchen wir im Kern nur drei Dinge:

1. **Worum geht es?**
2. **Was sollen die Lernenden lernen und in welcher Reihenfolge?**
3. **Welche Materialien und Dateien gehören dazu?**

Alles Weitere ist nachgeordnet.

---

## Die drei zentralen Bezugspunkte pro Thema

### 1. Themenbeschreibung

Hier halten wir fest:

- fachlicher Kern
- Zielgruppe
- Lernziele
- Abgrenzung des Themas

Das ist der Ort für die Frage:

**Was soll hier eigentlich vermittelt werden?**

### 2. Lernweg

Hier halten wir fest:

- welche Schritte oder Phasen der Lernweg hat
- in welcher Reihenfolge sie kommen
- welche davon Pflicht und welche Erweiterung sind
- welche Seite oder welches Material zu welchem Schritt gehört

Das ist der Ort für die Frage:

**Wie soll das Thema aufgebaut werden?**

### 3. Materialübersicht

Hier halten wir fest:

- welche Markdown-Dateien es gibt
- welche Python-Dateien dazugehören
- welche HTML-Seiten daraus erzeugt werden
- welche Dateien Quelle und welche nur Ausgabe sind

Das ist der Ort für die Frage:

**Welche Artefakte gehören zu diesem Thema und wo liegen sie?**

---

## Praktische Arbeitsform mit Copilot

Wenn du später mit mir an einem Thema weiterarbeiten willst, reicht es im Idealfall, wenn du auf diese drei Punkte Bezug nimmst:

1. **Inhalt / Lernziele**
   - Was ist das Ziel des Themas?
   - Was sollen Schüler:innen verstehen oder können?

2. **Lernweg**
   - Welche Reihenfolge der Vermittlung willst du?
   - Was soll eher früh, was eher spät kommen?

3. **Materialien**
   - Welche Dateien gibt es schon?
   - Welche fehlen noch?
   - Welche Seiten sollen gebaut oder verändert werden?

Dann kann ich daraus ableiten:

- welche Markdown-Datei wir bearbeiten sollten
- welche Codebeispiele ergänzt oder verändert werden müssen
- welche HTML-Seiten neu gebaut werden müssen

---

## Was wir nicht brauchen

Um handlungsfähig zu bleiben, brauchen wir im Moment **nicht**:

- zu viele zusätzliche Theoriebegriffe
- für alles ein eigenes Modell-Dokument
- eine perfekte Endarchitektur von Anfang an
- vollständige Standardisierung aller Seiten

Wichtiger ist, dass schnell klar ist:

- was das Thema ist
- was die Lernziele sind
- wie der Lernweg aussehen soll
- welche Materialien dazu gehören

Nicht hier gesammelt werden sollen:

- allgemeine didaktische Prinzipien fuer alle Lernseiten
- Session-Start-Hinweise oder Projektstatus
- technische Einzel-ToDos

Dafuer gibt es bereits zentrale Orte:

- `planung/didaktische-prinzipien.md`
- `AGENTS.md`
- `planung/technik-todos.md`

---

## Minimaler Dateityp pro Thema

Wenn wir ein Thema sauber pflegen wollen, sollte es mittelfristig mindestens diese Arten von Dateien geben.

### A. eine inhaltliche Quelldatei

Zum Beispiel:

- eine Lernseite in Markdown
- oder ein Projektauftrag in Markdown

### B. die zugehörigen Codebeispiele

Zum Beispiel:

- Zwischenstände
- Endlösung

### C. eine kleine Themennotiz

Diese muss nicht lang sein, aber sie sollte festhalten:

- Lernziele
- Lernweg
- Materialzuordnung

---

## Begriffsklärung

Damit wir nicht durcheinanderkommen, verwenden wir diese Begriffe möglichst eindeutig:

### Projektauftrag

`Projektauftrag` ist ein **Schülerformat**.

Gemeint ist also ein Dokument, das sich an Lernende richtet und beschreibt,

- was sie bauen sollen,
- welche Anforderungen gelten,
- was Pflicht und was Bonus ist.

### Interner Auftrag

Wenn sich ein Dokument oder eine Anweisung an die Materialentwicklung richtet, nennen wir das **nicht** `Projektauftrag`.

Dafür verwenden wir eher Begriffe wie:

- Arbeitsauftrag
- Entwicklungsauftrag
- Briefing

Wichtig ist nur die klare Trennung:

- `Projektauftrag` = für Schüler:innen
- interner Auftrag = für die Entwicklung von Material, Code oder Seiten

---

## Praktischer Arbeitsablauf

Für die Zusammenarbeit reicht meistens diese Reihenfolge:

1. Thema und Lernziele klären
2. Lernweg mit Pflicht und Erweiterung festlegen
3. vorhandene und fehlende Materialien zuordnen
4. erst dann Dateien, Generator und HTML konkret ändern

---

## Konkrete Dateirollen im aktuellen Projekt

Im jetzigen Projekt lassen sich die Rollen schon grob so lesen:

### Inhaltliche Quellen

- `themen/kreise/LERNSEITE.kreise.md`
- `themen/aquarium/LERNSEITE.aquarium.md`
- `themen/aquarium/aquarium_projektauftrag.md`

### Build-Skripte

- `build/render_lernseite.py`
- `build/build_aquarium_lernseite.py`
- `build/build_kreise_lernseite.py`
- Root-Wrapper: `build_kreise_lernseite.py`, `build_aquarium_lernseite.py`

### Code-Artefakte

- `themen/kreise/*.py`
- `themen/aquarium/*.py`

### Generierte Ausgaben

- `dist/kreise-lernseite.html`
- `dist/aquarium-lernseite.html`

### Planungs- und Strukturdateien

- `planung/arbeitsstruktur.md`
- `planung/projektideen.md`

---

## Merksatz für die Arbeit im Projekt

Wenn wir weiterarbeiten, ist diese Faustregel meistens genug:

- Inhalt in `themen/`
- Abstimmung in `planung/`
- Generatorlogik in `build/`
- erzeugte Ergebnisse in `dist/`
- `AGENTS.md`

---

## Der entscheidende Punkt für die Zukunft

Wenn du mir später gut sagen willst, was als Nächstes passieren soll, dann ist die nützlichste Form ungefähr diese:

1. **Thema**
   - Worum geht es?

2. **Lernziele**
   - Was sollen die Lernenden am Ende verstanden oder gebaut haben?

3. **Lernweg**
   - Welche Reihenfolge willst du?

4. **Materiallage**
   - Welche Dateien gibt es schon?
   - Welche fehlen?

5. **Ausgabeziel**
   - Soll eine Lernseite, ein Projektauftrag, neue Beispiele oder eine Überarbeitung entstehen?

Wenn diese fünf Punkte klar sind, kann ich sehr zielgerichtet weiterarbeiten.

---

## Arbeitsstatus

Diese Datei ist absichtlich eine **schlanke Arbeitsvereinbarung** und kein großes Modellpapier.

Sie soll uns helfen, mit wenigen klaren Bezugspunkten weiterzuarbeiten.
Wenn Inhalte hier auftauchen, die eigentlich allgemeine Didaktik, technische ToDos oder Session-Kontext sind, sollten sie in die jeweils passendere Datei verschoben werden.
