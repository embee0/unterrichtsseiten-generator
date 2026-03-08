# Projektideen zur Fortsetzung der OOP-Einführung mit py5

## Zielrichtung

Die bisherige Reihe entwickelt sich klar so:

1. **ein Objekt zeichnen**
2. **Eigenschaften in einer Klasse kapseln**
3. **mehrere Objekte derselben Klasse verwenden**
4. **viele Objekte in einer Liste verwalten**
5. **Objekte bekommen Verhalten**

Daran lässt sich sehr gut anschließen.

---

## Variante A: Fortsetzung des Kreis-Projekts

### Arbeitstitel

**"Lebendige Kreise"** oder **"Teilchen-System"**

### Kernidee

Die vorhandenen `Kreis`-Objekte werden erweitert. Die Kreise fallen nicht nur nach unten, sondern reagieren auf Regeln:

- bewegen sich mit eigener Geschwindigkeit
- prallen am Rand ab
- ändern Größe oder Farbe
- erscheinen neu, wenn sie den Bildschirm verlassen
- reagieren auf die Maus

### Fachliche Lernziele

Die Schülerinnen und Schüler üben dabei:

- Klassen mit Attributen und Methoden
- Objektzustände verändern
- Listen von Objekten verwalten
- Schleifen über Objektlisten
- Zufallswerte sinnvoll einsetzen
- schrittweise Refactoring eines bestehenden Programms

### Mögliche Ausbaustufen

#### Pflichtteil

- `x`, `y`, `dx`, `dy`, `durchmesser`, `farbe`
- Methode `bewege()`
- Methode `zeichne()`
- Randverhalten: abprallen oder neu erscheinen

#### Erweiterung 1

- Maus-Klick erzeugt neuen Kreis
- Taste löscht alle Kreise
- Taste erzeugt 20 neue Kreise

#### Erweiterung 2

- Kreise ändern beim Berühren des Randes die Farbe
- Kreise pulsieren unterschiedlich schnell
- einige Kreise steigen auf, andere fallen

#### Erweiterung 3

- Kollisionen grob erkennen
- Kreise stoßen einander ab
- "Schwarm"- oder "Explosion"-Effekt

### Vorschlag für eine Woche

#### Stunde 1

- Ausgangscode mit vielen Kreisen verstehen
- Klasse um `dx` und `dy` erweitern
- Methode `bewege()` einführen

#### Stunde 2

- Randverhalten programmieren
- Farbwechsel oder Größenänderung ergänzen

#### Stunde 3

- Interaktion mit Tastatur oder Maus
- Neue Objekte dynamisch erzeugen

#### Stunde 4

- Eigenständige Erweiterungen in Partnerarbeit
- Zwischenstände präsentieren

#### Stunde 5

- Aufräumen des Codes
- kurze Reflexion: Was steckt in der Klasse, was im Hauptprogramm?

### Gute Leitfrage

**Wie kann man viele ähnliche Dinge mit wenig Code steuern?**

---

## Variante B: Alternatives Projekt

### Arbeitstitel

**"Aquarium"**

### Kernidee

Statt Kreisen werden einfache Fische, Blasen oder Quallen als Objekte modelliert. Das ist sehr nah an der bisherigen Logik, aber motivierend anders.

### Objektideen

- `Fisch`: schwimmt horizontal, hat Farbe, Größe, Geschwindigkeit
- `Blase`: steigt nach oben, wird größer oder verschwindet
- `Futter`: fällt nach unten

### Warum didaktisch passend?

Das Projekt bleibt in derselben Struktur wie die Kreise:

- Klasse definieren
- mehrere Objekte erzeugen
- Liste verwenden
- Bewegung pro Frame berechnen
- unterschiedliche Attribute pro Objekt

### Minimale Version

- Viele `Blase`-Objekte steigen auf
- Wenn sie oben ankommen, erscheinen sie unten neu

### Mittlere Version

- Mehrere `Fisch`-Objekte mit eigener Geschwindigkeit
- Richtung nach links/rechts
- bei Randkontakt umdrehen

### Erweiterte Version

- Maus fügt Futter hinzu
- Fische bewegen sich zum Futter
- Blasen steigen unabhängig weiter

### Gute Leitfrage

**Wie modelliert man eine kleine Welt aus vielen Objekten?**

---

## Einschätzung

Wenn die Klasse nah am bisherigen Stand bleiben soll, ist **Variante A** am sinnvollsten.

Wenn ein kleiner Neustart mit gleichem OOP-Prinzip gewünscht ist, ist **Variante B** motivierender.

---

## Konkrete Empfehlung

Für die Vertretungs- oder Selbstarbeitsphase eignet sich am ehesten:

### Empfohlenes Wochenprojekt

**"Teilchen-System mit interaktiven Kreisen"**

#### Mindestanforderungen

- Es gibt mindestens 20 Objekte einer Klasse.
- Jedes Objekt hat eigene Attribute.
- Jedes Objekt bewegt sich selbstständig.
- Das Hauptprogramm verwaltet die Objekte in einer Liste.
- Mindestens eine Benutzerinteraktion ist eingebaut.

#### Mögliche Bewertungskriterien

- Klasse sinnvoll aufgebaut
- Attribute und Methoden passend gewählt
- Code funktioniert stabil
- Erweiterungsideen umgesetzt
- Code ist lesbar und kommentiert

#### Differenzierung

- **einfacher:** nur vertikale Bewegung und Reset unten/oben
- **mittel:** freie Bewegung mit `dx`, `dy`
- **schwieriger:** Kollisionen oder Objekt-Erzeugung per Eingabe

---

## Arbeitsauftrag für Schülerinnen und Schüler

**Entwickle auf Basis der bisherigen Kreis-Beispiele eine kleine Animation mit vielen Objekten.**

Dein Programm soll:

1. eine eigene Klasse verwenden,
2. viele Objekte in einer Liste speichern,
3. die Objekte in `draw()` aktualisieren und zeichnen,
4. mindestens eine eigene Erweiterung enthalten.

Mögliche Themen:

- fallende Bälle
- schwebende Blasen
- Aquarium
- Feuerwerk
- Schneeflocken
- Planeten

---

## Mögliche Lehrer-Notiz

Die Reihe eignet sich gut, um den Übergang zu erklären von:

- **Zeichencode** → **Objekt**
- **eine Variable** → **Attribute**
- **eine Figur** → **viele Instanzen**
- **Ablaufsteuerung** → **Verhalten von Objekten**
