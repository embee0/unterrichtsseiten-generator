# OOP mit Py5: Kreise, Kreise und noch mehr Kreise

<!-- COPILOT: Diese Datei ist die inhaltliche Hauptquelle. Kommentare mit COPILOT sollen nicht auf die Website. -->
<!-- COPILOT: Platzhalter {{IFRAME: datei.py}} und {{EDIT: datei.py}} werden beim HTML-Bau automatisch aufgelöst. -->
<!-- COPILOT: Zeilen mit > werden als margin notes / Randnotizen dargestellt. -->

Auf dieser Seite gehst du Schritt für Schritt von einem einfachen _nicht_ objektorientierten py5-Programm zu einem objektorientierten Programm mit vielen Kreisen. Dabei lernst du die OOP-Begriffe **Klasse**, **Objekt**, **Attribut**, **Methode** und **Konstruktor** nicht nur als Wörter kennen, sondern direkt im Code.

Am Ende dieses Lernwegs gibt es viele Kreise in unterschiedlichen Farben und Größen. Der Code bleibt trotzdem übersichtlich, weil alle Kreise nach demselben Bauplan entstehen, aber jeder Kreis seine eigenen Werte für Position, Größe und Farbe mitbringt und sich auch um Bewegung und Darstellung selbst kümmert.

Das ist das Grundprinzip der Objektorientierung: **Jedes Objekt kümmert sich um seinen eigenen Zustand und sein eigenes Verhalten.**

## So arbeitest du mit der Seite

Die Seite ist so aufgebaut, dass du den Weg von Station zu Station nachvollziehen kannst. Es geht nicht darum, jede Definition sofort auswendig zu können, sondern zu verstehen, warum der Code an jeder Stelle umgebaut wird.

In jedem Schritt stellen wir drei Fragen:

1. **Was wird geändert?**
2. **Warum wird das geändert?**
3. **Welcher OOP-Begriff steckt dahinter?**

> **OOP:** Objektorientierte Programmierung (OOP) ist eine Art, Software zu strukturieren. Sie basiert auf der Idee, dass man Dinge als "Objekte" modellieren kann, die Daten (Attribute) und Verhalten (Methoden) in sich tragen. Das macht es einfacher, komplexe Programme zu organisieren und zu erweitern.

---

## Station 0 – Ein Kreis ohne OOP

### Was passiert hier?

Wir starten mit einem sehr einfachen py5-Programm. Es zeichnet einen Kreis in die Mitte des Fensters. Dieser Kreis wird größer und kleiner. Das Programm ist also schon **animiert**.

### Warum starten wir so?

Bevor wir Klassen, Objekte und Attribute einführen, brauchen wir eine funktionierende Ausgangslage. Erst wenn klar ist, wie `setup()` und `draw()` zusammenarbeiten, lohnt sich der nächste Schritt.

### Begriff

**Animation** bedeutet hier: Das Bild wird immer wieder neu gezeichnet, und dabei verändern sich Werte.

> **frame_count:** Im `frame_count` wird gezählt, wie oft die `draw()`-Funktion schon aufgerufen wurde. Das ist praktisch für Animationen, weil man Darstellung oder Verhalten abhängig von der Zeit machen kann. In diesem Fall sorgt `sin(frame_count / 30)` dafür, dass der Kreis immer größer und kleiner wird, weil der Sinus-Wert zwischen -1 und 1 schwankt.

### Vorschau

{{IFRAME: kreise0noch_ohne_OO.py}}

{{EDIT: kreise0noch_ohne_OO.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 0 anzeigen}}

{{EDIT: kreise0noch_ohne_OO.py | Musterlösung im Editor öffnen}}

```python
def setup():
    size(200, 200)


def draw():
    background(200)
    durchmesser = width / 2
    max_aenderung = 20
    aktueller_durchmesser = durchmesser + sin(frame_count / 30) * max_aenderung
    fill(0, 0, 255)
    circle(width / 2, height / 2, aktueller_durchmesser)
```

{{ENDSOLUTION}}

---

## Station 1 – Eine Klasse für einen Kreis

### Was wird geändert?

Jetzt bekommt der Kreis eine eigene **Klasse**. Seine Position wird nicht mehr irgendwo lose gespeichert, sondern direkt im Objekt.

### Warum ist das sinnvoll?

Ein Kreis weiß jetzt selbst, wo er gezeichnet werden soll. Das Hauptprogramm muss sich nicht mehr um jedes einzelne Detail kümmern.

### Begriffe

- **Klasse**: ein Bauplan
- **Konstruktor**: `__init__()` setzt die Anfangswerte

> **Klasse und Objekt:** Eine _Klasse_ ist ein Bauplan für viele ähnliche Objekte. Ein Objekt ist ein einzelnes konkretes Beispiel, das nach diesem Bauplan erzeugt wurde und eigene Werte hat. Ein konkretes Objekt nennt man auch _Instanz_ der Klasse.

### Vorschau

{{IFRAME: kreise1aOO_ein_objekt.py}}

{{EDIT: kreise1_aufgabe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 1 anzeigen}}

{{EDIT: kreise1aOO_ein_objekt.py | Musterlösung im Editor öffnen}}

```python
class Kreis:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        diameter = sin(frame_count / 60) * 20 + 80
        fill(0, 0, 255)
        circle(self.x, self.y, diameter)


def setup():
    global k1
    size(200, 200)
    k1 = Kreis(100, 100)


def draw():
    global k1
    background(200)
    k1.draw()
```

{{ENDSOLUTION}}

---

## Station 2 – Der Kreis bekommt ein Attribut mehr

### Was wird geändert?

Der Kreis speichert jetzt nicht nur `x` und `y`, sondern auch `durchmesser`.

### Warum ist das sinnvoll?

Ein Objekt hat meistens mehrere Eigenschaften. Ein Kreis hat eben nicht nur einen Ort, sondern auch eine Größe.

### Begriff

**Attribut** = eine gespeicherte Eigenschaft eines Objekts.

> **Attribut:** Ein Attribut ist eine Eigenschaft, die zu einem Objekt gehört. In diesem Fall ist `durchmesser` ein Attribut des Kreis-Objekts, das seine Größe beschreibt. Jedes Kreis-Objekt kann einen eigenen Wert für `durchmesser` haben.

> **self.durchmesser:** Mit `self` bezeichnet man innerhalb einer Methode das aktuelle Objekt, mit dem gerade gearbeitet wird. Mit `self` kann eine Methode auf die Attribute dieses konkreten Objekts zugreifen. `self.durchmesser` ist also genau der Durchmesser, der zu dem Objekt gehört, dessen Methode gerade ausgeführt wird.

### Vorschau

{{IFRAME: kreise1bOO_mit_durchmesser.py}}

{{EDIT: kreise1aOO_ein_objekt.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 2 anzeigen}}

{{EDIT: kreise1bOO_mit_durchmesser.py | Musterlösung im Editor öffnen}}

```python
class Kreis:
    def __init__(self, x, y, durchmesser):
        self.x = x
        self.y = y
        self.durchmesser = durchmesser

    def draw(self):
        max_aenderung = 0.2 * self.durchmesser
        aktueller_durchmesser = self.durchmesser + sin(frame_count / 30) * max_aenderung
        fill(0, 0, 255)
        circle(self.x, self.y, aktueller_durchmesser)


def setup():
    global k1
    size(200, 200)
    k1 = Kreis(100, 100, 90)


def draw():
    global k1
    background(200)
    k1.draw()
```

{{ENDSOLUTION}}

---

## Station 3 – Zwei Objekte derselben Klasse

### Was wird geändert?

Jetzt erzeugen wir zwei Kreise aus derselben Klasse.

### Warum ist das sinnvoll?

Hier sieht man zum ersten Mal deutlich: Eine Klasse ist ein Bauplan, und aus einem Bauplan kann man mehrere Objekte erzeugen.

### Begriff

**Objekt** oder **Instanz** = ein konkretes Exemplar einer Klasse.

> **Instanzen:** Instanzen sind einzelne Objekte derselben Klasse. Sie teilen sich denselben Bauplan, können aber unterschiedliche _Attributwerte_ haben. So können zwei Kreise aus derselben Klasse trotzdem an unterschiedlichen Orten liegen und unterschiedliche Größen haben. Achtung, unterscheide genau: Alle Instanzen einer Klasse haben dieselben Attribute, aber die Werte dieser Attribute können unterschiedlich sein.

### Vorschau

{{IFRAME: kreise2aOO_zwei_objekte.py}}

{{EDIT: kreise1bOO_mit_durchmesser.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 3 anzeigen}}

{{EDIT: kreise2aOO_zwei_objekte.py | Musterlösung im Editor öffnen}}

```python
class Kreis:
    def __init__(self, x, y, durchmesser):
        self.x = x
        self.y = y
        self.durchmesser = durchmesser

    def draw(self):
        max_aenderung = 0.2 * self.durchmesser
        aktueller_durchmesser = self.durchmesser + sin(frame_count / 30) * max_aenderung
        fill(0, 0, 255)
        circle(self.x, self.y, aktueller_durchmesser)


def setup():
    global k1, k2
    size(200, 200)
    k1 = Kreis(145, 60, 35)
    k2 = Kreis(80, 145, 90)


def draw():
    global k1, k2
    background(200)
    k1.draw()
    k2.draw()
```

{{ENDSOLUTION}}

---

## Station 4 – Viele Objekte in einer Liste

### Was wird geändert?

Statt einzelner Variablen wie `k1` und `k2` benutzen wir jetzt eine Liste.

### Warum ist das sinnvoll?

Mit einer Liste kann man viele Objekte gleich behandeln. Das spart Wiederholungen und macht den Code deutlich flexibler.

### Begriff

**Liste von Objekten** = viele Instanzen gemeinsam speichern und mit einer Schleife bearbeiten.

> **Liste:** Eine Liste ist hier der gemeinsame Behälter für viele Kreis-Objekte. Dadurch kannst du alle Kreise mit derselben Schleife verwalten, zeichnen oder bewegen.

### Vorschau

{{IFRAME: kreise2bOO_liste_von_objekten.py}}

{{EDIT: kreise2aOO_zwei_objekte.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 4 anzeigen}}

{{EDIT: kreise2bOO_liste_von_objekten.py | Musterlösung im Editor öffnen}}

```python
class Kreis:
    def __init__(self, x, y, durchmesser):
        self.x = x
        self.y = y
        self.durchmesser = durchmesser

    def draw(self):
        max_aenderung = 0.2 * self.durchmesser
        aktueller_durchmesser = self.durchmesser + sin(frame_count / 30) * max_aenderung
        fill(0, 0, 255)
        circle(self.x, self.y, aktueller_durchmesser)


def setup():
    global kreise
    size(200, 200)
    kreise = []
    kreise.append(Kreis(145, 60, 35))
    kreise.append(Kreis(80, 145, 90))
    kreise.append(Kreis(45, 85, 42))


def draw():
    global kreise
    background(200)
    for kreis in kreise:
        kreis.draw()
```

{{ENDSOLUTION}}

---

## Station 5 – Verhalten als Methode

### Was wird geändert?

Die Kreise können jetzt selbst etwas tun: Sie fallen nach unten.

### Warum ist das sinnvoll?

In der Objektorientierung speichert ein Objekt nicht nur Daten. Es kann auch Verhalten mitbringen.

### Begriff

**Methode** = eine Funktion innerhalb einer Klasse.

> **Methode:** Eine Methode beschreibt die _Fähigkeit_ eines Objekts, also das, was es tun kann. `falle_runter()` ist so eine Fähigkeit: Der Kreis verändert dabei seine Position selbst.

### Vorschau

{{IFRAME: kreise3aOO_verhalten_und_farbe.py}}

{{EDIT: kreise2bOO_liste_von_objekten.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 5 anzeigen}}

{{EDIT: kreise3aOO_verhalten_und_farbe.py | Musterlösung im Editor öffnen}}

```python
class Kreis:
    def __init__(self, x, y, durchmesser):
        self.x = x
        self.y = y
        self.durchmesser = durchmesser
        self.farbe = color(50, random(100, 230), 0)

    def falle_runter(self):
        self.y += 1

    def draw(self):
        max_aenderung = 0.2 * self.durchmesser
        aktueller_durchmesser = self.durchmesser + sin(frame_count / 30) * max_aenderung
        fill(self.farbe)
        circle(self.x, self.y, aktueller_durchmesser)


def setup():
    global kreise
    size(200, 200)
    kreise = []
    for nr in range(40):
        kreise.append(Kreis(random_int(0, width), random_int(0, height), 16))


def draw():
    global kreise
    background(200)
    for kreis in kreise:
        kreis.falle_runter()
        kreis.draw()
```

{{ENDSOLUTION}}

---

## Station 6 – Viele Kreise mit eigenem Zustand

### Was wird geändert?

Im letzten Schritt gibt es viele Kreise, und jeder bringt seine eigene Farbe mit.

### Warum ist das sinnvoll?

Jetzt wird sichtbar, was Objektorientierung praktisch bedeutet: gleiche Struktur, aber unterschiedliche Werte pro Objekt.

### Begriff

**Zustand eines Objekts** = alle aktuellen Attributwerte zusammen.

> **Zustand:** Der Zustand eines Objekts ist das Gesamtbild seiner aktuellen Eigenschaften, zum Beispiel der Attributwerte für Position, Größe und Farbe. Darum können zwei Kreise aus derselben Klasse trotzdem unterschiedlich aussehen und sich unterschiedlich verhalten.

### Vorschau

{{IFRAME: kreise3OOvielekreise.py}}

{{EDIT: kreise3aOO_verhalten_und_farbe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 6 anzeigen}}

{{EDIT: kreise3OOvielekreise.py | Musterlösung im Editor öffnen}}

```python
class Kreis:
    def __init__(self, x, y, durchmesser):
        self.x = x
        self.y = y
        self.durchmesser = durchmesser
        r = 50
        g = random(100, 230)
        b = 0
        self.color = color(r, g, b)

    def falle_runter(self):
        self.y += 1

    def draw(self):
        max_aenderung = 0.2 * self.durchmesser
        aktueller_durchmesser = self.durchmesser + sin(frame_count / 30) * max_aenderung
        fill(self.color)
        circle(self.x, self.y, aktueller_durchmesser)


def setup():
    global kreise
    size(200, 200)
    kreise = []
    for nr in range(180):
        k = Kreis(random_int(0, width), random_int(0, height), 16)
        kreise.append(k)


def draw():
    global kreise
    background(200)
    for kreis in kreise:
        kreis.falle_runter()
        kreis.draw()
```

{{ENDSOLUTION}}

---

## Mögliche Denkfragen

1. Warum ist eine Liste besser als viele Variablen wie `k1`, `k2`, `k3`?
2. Welche Eigenschaften eines Kreises würden sich noch als Attribute eignen?
3. Welche neue Methode könnte man ergänzen, damit die Kreise nicht nur fallen?
4. Was müsste man ändern, damit jeder Kreis eine andere Geschwindigkeit hat?

## Merksätze

- Eine **Klasse** ist ein Bauplan.
- Ein **Objekt** ist ein konkretes Exemplar einer Klasse.
- Ein **Attribut** speichert Daten.
- Eine **Methode** beschreibt Verhalten.
- Der **Konstruktor** setzt Anfangswerte.
