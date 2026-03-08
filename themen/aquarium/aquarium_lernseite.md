# Aquarium mit OOP in py5

<!-- COPILOT: Diese Datei ist die inhaltliche Hauptquelle für die Aquarium-Lernseite. -->
<!-- COPILOT: Platzhalter {{IFRAME: datei.py}} und {{EDIT: datei.py}} werden beim HTML-Bau automatisch aufgelöst. -->
<!-- COPILOT: Zeilen mit > werden als Randnotizen dargestellt. -->

Auf dieser Seite baust du Schritt für Schritt ein kleines Aquarium in py5. Du startest mit genau einem Fisch und landest am Ende bei einer kleinen Unterwasserwelt mit vielen Fischen, Futter und Blasen.

{{IFRAME: aquarium_endloesung.py}}

> **Vorschau:** So könnte das fertige Aquarium am Ende aussehen. Du musst das nicht sofort verstehen. Wir arbeiten uns Schritt für Schritt dorthin.

Der Hintergrund ist diesmal von Anfang an schon da. So kannst du dich auf das konzentrieren, was hier fachlich wichtig ist: **Klassen, Objekte, Listen, Attribute und Verhalten**.

Die Seite ist so aufgebaut, dass du in der nächsten Woche möglichst selbstständig arbeiten kannst. Du musst nicht alles sofort können. Wichtig ist, dass du die Stationen nacheinander bearbeitest und jeweils verstehst, was sich im Code verändert.

## Worum es in dieser Woche geht

Die **Pflichtphase** sind Station 1 bis 5.

Am Ende dieser Pflichtphase kannst du:

- eine Klasse `Fish` mit Attributen und Methoden schreiben
- mehrere `Fish`-Objekte in einer Liste verwalten
- Objekte pro Frame bewegen
- eine zweite Klasse `Food` einbauen
- Objekte verschiedener Klassen zusammenarbeiten lassen

Wenn du schneller fertig bist, kannst du in Station 6 dein Aquarium mit Blasen und weiteren Details erweitern.

---

## So arbeitest du

Arbeite die Stationen der Reihe nach durch.

1. Lies den Arbeitsauftrag.
2. Schaue dir die Demo an.
3. Baue den Schritt selbst nach.
4. Gehe erst weiter, wenn dein Programm in diesem Schritt funktioniert.

> **Pflicht und Bonus:** Station 1 bis 5 gehören zum eigentlichen Lernweg. Station 6 ist eine Erweiterung für alle, die schneller vorankommen oder noch weiterbauen möchten.

---

## Station 1 – Ein einzelner Fisch als Objekt

### Arbeitsauftrag

1. Lege eine Klasse `Fish` an.
2. Schreibe einen Konstruktor mit `x` und `y`.
3. Schreibe eine Methode `draw()`.
4. Zeichne den Fisch aus einer Ellipse und einem Dreieck.
5. Erzeuge in `setup()` genau einen Fisch und zeichne ihn in `draw()`.

### Warum dieser Schritt?

Du trennst zum ersten Mal zwischen dem Hintergrund des Programms und einem eigenen Objekt. Der Fisch ist nicht mehr nur lose Zeichencodes, sondern bekommt eine eigene Klasse.

### Dabei lernst du

- **Klasse** als Bauplan
- **Objekt** als konkrete Instanz
- erste Arbeit mit `self`

> **Fischform:** Für den Anfang reicht eine einfache Form aus Ellipse und Dreieck völlig. Wenn der Code später läuft, kannst du den Fisch immer noch schöner gestalten.

### Demo

{{IFRAME: aquarium1_ein_fisch.py}}

{{EDIT: aquarium1_ein_fisch.py}}

{{SOLUTION: Lösungscode zu Station 1 anzeigen}}

```python
def draw_background():
    for row in range(height):
        blend = row / height
        stroke(18, 110 + 60 * blend, 170 + 40 * blend)
        line(0, row, width, row)

    no_stroke()
    fill(19, 100, 70, 170)
    rect(0, height - 38, width, 38)

    fill(204, 182, 112)
    rect(0, height - 14, width, 14)


class Fish:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

    def draw(self):
        no_stroke()
        fill(255, 141, 76)
        ellipse(self.x, self.y, 84, 42)
        triangle(self.x - 40, self.y, self.x - 68, self.y - 18, self.x - 68, self.y + 18)
        fill(255)
        circle(self.x + 22, self.y - 6, 11)
        fill(15)
        circle(self.x + 24, self.y - 6, 5)


def setup():
    global fish
    size(420, 260)
    fish = Fish(width / 2, height / 2)


def draw():
    draw_background()
    fish.draw()
```

{{ENDSOLUTION}}

---

## Station 2 – Der Fisch bekommt mehr Eigenschaften

### Arbeitsauftrag

1. Ergänze den Konstruktor um weitere Attribute.
2. Speichere mindestens `scale`, `body_color` und `fin_color` im Objekt.
3. Passe die Methode `draw()` so an, dass diese Werte benutzt werden.
4. Erzeuge wieder genau einen Fisch, aber diesmal mit eigenen Eigenschaften.

### Warum dieser Schritt?

Ein Objekt besteht nicht nur aus seiner Position. Erst mit mehreren Attributen wird deutlich, dass jedes Objekt seinen eigenen Zustand besitzt.

### Dabei lernst du

- **Attribut** als gespeicherte Eigenschaft
- Objekte mit unterschiedlichen Startwerten erzeugen
- Zeichnen auf Basis von Objektzustand

> **Attribute:** Position, Größe und Farbe lassen sich gut in der Klasse speichern. So steckt das Aussehen des Fisches direkt im Objekt.

### Demo

{{IFRAME: aquarium2_fisch_mit_attributen.py}}

{{EDIT: aquarium2_fisch_mit_attributen.py}}

{{SOLUTION: Lösungscode zu Station 2 anzeigen}}

```python
class Fish:
    def __init__(self, x_position, y_position, scale, body_color, fin_color):
        self.x = x_position
        self.y = y_position
        self.scale = scale
        self.body_color = body_color
        self.fin_color = fin_color

    def draw(self):
        body_length = 84 * self.scale
        body_height = 42 * self.scale
        tail_length = 28 * self.scale
        no_stroke()
        fill(self.body_color)
        ellipse(self.x, self.y, body_length, body_height)
        fill(self.fin_color)
        triangle(
            self.x - body_length * 0.48,
            self.y,
            self.x - body_length * 0.48 - tail_length,
            self.y - body_height * 0.45,
            self.x - body_length * 0.48 - tail_length,
            self.y + body_height * 0.45,
        )
```

{{ENDSOLUTION}}

---

## Station 3 – Viele Fische in einer Liste

### Arbeitsauftrag

1. Erzeuge nicht mehr nur ein Objekt, sondern mehrere.
2. Speichere alle Fische in einer Liste `fishes`.
3. Gehe in `draw()` mit einer Schleife durch die Liste.
4. Zeichne alle Fische nacheinander.

### Warum dieser Schritt?

Hier wird OOP praktisch nützlich. Eine Klasse lohnt sich erst richtig, wenn du viele ähnliche Objekte mit wenig Code verwalten willst.

### Dabei lernst du

- **Liste von Objekten**
- Schleife über Instanzen
- zufällige Startwerte für viele Objekte

> **Liste:** Ab hier ist eine Liste sinnvoller als einzelne Variablen wie `fish1`, `fish2` und `fish3`. So kannst du viele Objekte mit derselben Schleife verwalten.

### Demo

{{IFRAME: aquarium3_liste_von_fischen.py}}

{{EDIT: aquarium3_liste_von_fischen.py}}

{{SOLUTION: Lösungscode zu Station 3 anzeigen}}

```python
def setup():
    global fishes
    size(420, 260)
    fishes = []

    for _ in range(6):
        fishes.append(create_random_fish())


def draw():
    draw_background()

    for fish in fishes:
        fish.draw()
```

{{ENDSOLUTION}}

---

## Station 4 – Die Fische bewegen sich selbst

### Arbeitsauftrag

1. Ergänze die Klasse `Fish` um eine Geschwindigkeit.
2. Schreibe eine Methode `move()`.
3. Lasse die Fische horizontal schwimmen.
4. Wenn ein Fisch den Rand erreicht, soll er umdrehen.
5. Zeichne den Schwanz passend zur Schwimmrichtung.

### Warum dieser Schritt?

Jetzt bekommen die Objekte nicht nur Daten, sondern **Verhalten**. Das ist einer der zentralen Gedanken der Objektorientierung.

### Dabei lernst du

- **Methode** als Verhalten eines Objekts
- Zustandsänderung pro Frame
- mehrere Objekte mit eigenem Tempo

> **Bewegung:** Schon eine kleine Wellenbewegung mit `sin(...)` macht die Bewegung glaubwürdiger. Der Fisch schwimmt dadurch nicht völlig starr durch das Aquarium.

### Demo

{{IFRAME: aquarium4_fische_bewegen_sich.py}}

{{EDIT: aquarium4_fische_bewegen_sich.py}}

{{SOLUTION: Lösungscode zu Station 4 anzeigen}}

```python
class Fish:
    def __init__(self, x_position, y_position, scale, body_color, fin_color, speed):
        self.x = x_position
        self.base_y = y_position
        self.y = y_position
        self.scale = scale
        self.body_color = body_color
        self.fin_color = fin_color
        self.speed = speed
        self.dx = speed if random(1) < 0.5 else -speed
        self.phase = random(TWO_PI)

    def move(self):
        self.x += self.dx
        self.y = self.base_y + sin(frame_count * 0.08 + self.phase) * (7 * self.scale)
```

{{ENDSOLUTION}}

---

## Station 5 – Futter als zweite Klasse

### Arbeitsauftrag

1. Lege eine zweite Klasse `Food` an.
2. Futter soll nach unten fallen.
3. Ein Mausklick soll neues Futter erzeugen.
4. Fische sollen sich zum nächsten Futter bewegen.
5. Wenn ein Fisch nah genug dran ist, verschwindet das Futter.

### Warum dieser Schritt?

Das Aquarium besteht jetzt nicht mehr nur aus vielen Objekten derselben Klasse. Mehrere Klassen greifen ineinander und bilden zusammen eine kleine Welt.

### Dabei lernst du

- Zusammenarbeit mehrerer Klassen
- Listen für verschiedene Objektarten
- einfache Zielsuche mit `dist(...)`

> **Zweite Klasse:** Hier wird deutlich, dass OOP nicht nur beim Zeichnen hilft. Klassen helfen auch dabei, verschiedene Rollen im Programm sauber zu trennen.

### Demo

{{IFRAME: aquarium5_futter_und_jagd.py}}

{{EDIT: aquarium5_futter_und_jagd.py}}

{{SOLUTION: Lösungscode zu Station 5 anzeigen}}

```python
class Food:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position
        self.size = random(6, 10)
        self.speed = random(1.1, 1.9)


def mouse_pressed():
    food_list.append(Food(mouse_x, mouse_y))
```

{{ENDSOLUTION}}

---

## Station 6 – Erweiterung zur Endstufe

### Arbeitsauftrag

Wenn du bis hier gekommen bist, erweitere dein Aquarium weiter:

1. Ergänze eine Klasse `Bubble`.
2. Lasse Blasen nach oben steigen.
3. Wenn eine Blase oben angekommen ist, soll sie unten neu erscheinen.
4. Gestalte die Unterwasserwelt lebendiger.

### Warum ist das eine gute Erweiterung?

Die Pflichtteile sind schon ein vollständiges OOP-Projekt. Die Blasen sind ein sauberer Bonus, weil du dieselben Prinzipien noch einmal auf eine neue Objektart anwendest.

### Demo der Endstufe

{{IFRAME: aquarium_endloesung.py}}

{{EDIT: aquarium_endloesung.py}}

{{SOLUTION: Lösungscode der Endstufe anzeigen}}

```python
class Bubble:
    def __init__(self):
        self.reset(random(width), random(height), random(8, 22))

    def update(self):
        self.y -= self.speed
        self.x += sin(frame_count * 0.03 + self.phase) * self.wobble
```

{{ENDSOLUTION}}
