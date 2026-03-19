# Aquarium mit OOP in py5

<!-- COPILOT: Diese Datei ist die inhaltliche Hauptquelle für die Aquarium-Lernseite. -->
<!-- COPILOT: Platzhalter {{IFRAME: datei.py}} und {{EDIT: datei.py}} werden beim HTML-Bau automatisch aufgelöst. -->
<!-- COPILOT: Zeilen mit > werden als Randnotizen dargestellt. -->

Auf dieser Seite baust du Schritt für Schritt ein kleines Aquarium in py5. Du startest mit genau einem Fisch und landest am Ende bei einer kleinen Unterwasserwelt mit vielen Fischen, Futter und Blasen.

{{IFRAME: aquarium_endloesung.py}}

> **Vorschau:** So könnte dein Aquarium am Ende aussehen. Du musst das noch nicht komplett verstehen. Die Seite ist so aufgebaut, dass du dir alle Bausteine dafür Schritt für Schritt erarbeitest.

Der Hintergrund ist diesmal von Anfang an schon da. So kannst du dich auf das konzentrieren, was hier fachlich wichtig ist: **Klassen, Objekte, Listen, Attribute und Verhalten**.

Die Seite ist so aufgebaut, dass du in der nächsten Woche möglichst selbstständig arbeiten kannst. Du musst nicht alles sofort können. Wichtig ist, dass du die Stationen nacheinander bearbeitest und jeweils verstehst, was sich im Code verändert.

In den ersten Pflichtstationen findest du noch deutlichere TODO-Hinweise und Lücken im Code. Später werden die Aufgaben offener, damit du mehr Schritte selbst planst.

## Worum es in dieser Woche geht

Die **Pflichtphase** sind Station 1 bis 4.

Am Ende dieser Pflichtphase kannst du:

- eine Klasse `Fish` mit Attributen und Methoden schreiben
- mehrere `Fish`-Objekte in einer Liste verwalten
- Objekte pro Frame bewegen

Wenn du danach weitergehst, kannst du dein Aquarium mit einer zweiten Klasse `Food` und weiteren Interaktionen ausbauen.

Wenn du schneller fertig bist, kannst du ab Station 5 freiwillig weiterbauen und in Station 6 noch Blasen und weitere Details ergänzen.

> **Aufgabe 0:** Schreibe mir am Ende der Woche eine kurze Mail: Was hast du geschafft? Was fiel dir leicht? Wo war es schwierig? Hilfreich sind auch Screenshots und kleine Codeausschnitte. Wenn du magst, schreib auch kurz dazu, was an den Webseiten gut funktioniert und was dir noch fehlt.

---

## So arbeitest du

Arbeite die Stationen der Reihe nach durch.

1. Lies den Arbeitsauftrag.
2. Schaue dir die Demo an.
3. Baue den Schritt selbst nach.
4. Gehe erst weiter, wenn dein Programm in diesem Schritt funktioniert.

> **Pflicht und Bonus:** Station 1 bis 4 sind der verbindliche Kern. Ab Station 5 beginnt der freiwillige Teil. Dort wird das Aquarium Schritt für Schritt erweitert.

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

> **Fischform:** Für den Anfang reicht eine einfache Form völlig. Wichtig ist zuerst die Struktur des Programms: Klasse, Objekt, Konstruktor und Methode. Das Aussehen kannst du später immer noch verbessern.

### Demo

{{IFRAME: aquarium1_ein_fisch.py}}

{{EDIT: aquarium1_aufgabe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 1 anzeigen}}

{{EDIT: aquarium1_ein_fisch.py | Musterlösung im Editor öffnen}}

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

> **Attribute:** Attribute sind Eigenschaften eines Objekts. Bei einem Fisch können das zum Beispiel Position, Größe und Farben sein. Dadurch trägt jedes Objekt seine eigenen Werte direkt bei sich.

### Demo

{{IFRAME: aquarium2_fisch_mit_attributen.py}}

{{EDIT: aquarium2_aufgabe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 2 anzeigen}}

{{EDIT: aquarium2_fisch_mit_attributen.py | Musterlösung im Editor öffnen}}

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

> **Liste:** Die Liste ist der gemeinsame Behälter für viele Fisch-Objekte. So kannst du mit einer Schleife alle Fische gleich behandeln, statt für jeden eine eigene Variable zu brauchen.

### Demo

{{IFRAME: aquarium3_liste_von_fischen.py}}

{{EDIT: aquarium3_aufgabe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 3 anzeigen}}

{{EDIT: aquarium3_liste_von_fischen.py | Musterlösung im Editor öffnen}}

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
2. Schreibe eine Methode `move()` und lasse die Fische zuerst nur geradeaus schwimmen.
3. Wenn ein Fisch den Rand erreicht, soll er umdrehen.
4. Zeichne den Schwanz passend zur Schwimmrichtung.
5. Bonus: Baue erst danach die leichte Wellenbewegung mit `sin(...)` ein.

### Warum dieser Schritt?

Jetzt bekommen die Objekte nicht nur Daten, sondern **Verhalten**. Das ist einer der zentralen Gedanken der Objektorientierung.

### Dabei lernst du

- **Methode** als Verhalten eines Objekts
- Zustandsänderung pro Frame
- mehrere Objekte mit eigenem Tempo
- im Bonus: eine einfache Wellenbewegung als Erweiterung

> **Bewegung:** Eine Methode beschreibt, was ein Objekt tun kann. Hier bekommt jeder Fisch mit `move()` seine eigene Bewegung. Die Wellenbewegung mit `sin(...)` ist eine coole Erweiterung, aber nicht noetig fuer den Pflichtteil.
>
> **Sinnvolle Reihenfolge:** Baue die Bewegung in drei Schritten auf. Erst `self.x += self.dx` fuer eine gerade Bewegung. Dann das Umdrehen am Rand, indem du `self.dx` auf `self.speed` oder `-self.speed` setzt. Erst wenn das sicher funktioniert, kommt `sin(...)` als Bonus fuer das leichte Auf-und-ab.
>
> **Einfaches Modell:** `speed` bleibt immer positiv und beschreibt nur das Tempo. In `dx` steckt die Richtung: positiv bedeutet nach rechts, negativ bedeutet nach links.
>
> **Bonus statt Pflicht:** Fuer die Wellenbewegung musst du die Mathematik dahinter noch nicht komplett verstehen. Wenn du magst, uebernimm den Ausdruck erstmal als fertigen Zusatz und beobachte nur, was er bewirkt. Eine individuelle Phasenverschiebung lassen wir im Pflichtteil bewusst weg.
>
> **Fortgeschrittener Bonus:** Wenn spaeter nicht alle Fische gleich wackeln sollen, kannst du jedem Fisch noch einen eigenen Startwert geben, zum Beispiel mit `self.phase = random(TWO_PI)`. Dann wird aus `sin(frame_count * 0.08)` spaeter `sin(frame_count * 0.08 + self.phase)`.

### Demo

{{IFRAME: aquarium4_fische_bewegen_sich.py}}

{{EDIT: aquarium4_aufgabe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 4 anzeigen}}

{{EDIT: aquarium4_fische_bewegen_sich.py | Musterlösung im Editor öffnen}}

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
        self.dx = speed

    def move(self):
        self.x += self.dx

        if self.x < 48:
            self.x = 48
            self.dx = self.speed
        elif self.x > width - 48:
            self.x = width - 48
            self.dx = -self.speed

        self.y = self.base_y + sin(frame_count * 0.08) * (7 * self.scale)
```

{{ENDSOLUTION}}

---

## Station 5 – Freiwillig: Futter als zweite Klasse

### Arbeitsauftrag

1. Lege eine zweite Klasse `Food` an.
2. Futter soll nach unten fallen.
3. Ein Mausklick soll neues Futter erzeugen.
4. Wenn du weitergehen möchtest, sollen sich Fische zum nächsten Futter bewegen.
5. Wenn ein Fisch nah genug dran ist, kann das Futter verschwinden.

### Warum dieser Schritt?

Das Aquarium besteht jetzt nicht mehr nur aus vielen Objekten derselben Klasse. Schon mit einer zweiten Klasse wird sichtbar, wie OOP hilft, verschiedene Rollen im Programm sauber zu trennen.

### Dabei lernst du

- zweite Klasse im selben Projekt
- Listen für verschiedene Objektarten
- im erweiterten Teil: einfache Zielsuche mit `dist(...)`

> **Freiwillige Erweiterung:** Der erste Teil dieser Station ist noch gut überschaubar: eine neue Klasse und fallendes Futter. Der Teil, in dem Fische gezielt auf Futter reagieren, ist anspruchsvoller, weil dabei Objekte auf andere Objekte Bezug nehmen.

### Demo

{{IFRAME: aquarium5_futter_und_jagd.py}}

{{EDIT: aquarium4_fische_bewegen_sich.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 5 anzeigen}}

{{EDIT: aquarium5_futter_und_jagd.py | Musterlösung im Editor öffnen}}

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

> **Fortgeschrittener Effekt:** In der Endstufe taucht die individuelle Phasenverschiebung bei der Fischbewegung wieder auf. Dadurch wackeln nicht mehr alle Fische synchron, sondern jeder etwas anders.

### Demo der Endstufe

{{IFRAME: aquarium_endloesung.py}}

{{EDIT: aquarium5_futter_und_jagd.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode der Endstufe anzeigen}}

{{EDIT: aquarium_endloesung.py | Musterlösung im Editor öffnen}}

```python
class Bubble:
    def __init__(self):
        self.reset(random(width), random(height), random(8, 22))

    def reset(self, x_position, y_position, diameter):
        self.x = x_position
        self.y = y_position
        self.diameter = diameter
        self.speed = random(0.4, 1.4)
        self.wobble = random(0.3, 1.0)
        self.phase = random(TWO_PI)

    def update(self):
        self.y -= self.speed
        self.x += sin(frame_count * 0.03 + self.phase) * self.wobble

        if self.y < -self.diameter:
            self.reset(random(width), height + random(10, 60), random(8, 22))

    def draw(self):
        no_fill()
        stroke(220, 245, 255, 170)
        stroke_weight(2)
        circle(self.x, self.y, self.diameter)
        no_stroke()


class Food:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position
        self.size = random(6, 10)
        self.speed = random(1.2, 2.0)
        self.drift = random(-0.35, 0.35)
        self.phase = random(TWO_PI)

    def update(self):
        self.y += self.speed
        self.x += self.drift + sin(frame_count * 0.05 + self.phase) * 0.15

    def draw(self):
        fill(255, 188, 73)
        circle(self.x, self.y, self.size)

    def is_outside(self):
        return self.y > height + self.size


class Fish:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.base_y = y_position
        self.y = y_position
        self.scale = random(0.7, 1.35)
        self.body_length = 58 * self.scale
        self.body_height = 30 * self.scale
        self.tail_length = 24 * self.scale
        self.speed = random(0.6, 1.8)
        self.dx = self.speed
        self.phase = random(TWO_PI)
        self.body_color = color(random(70, 255), random(90, 230), random(110, 255))
        self.fin_color = color(random(140, 255), random(120, 220), random(40, 180))
        self.eye_size = 4.5 * self.scale

    def update(self, food_list):
        target_food = self.find_nearest_food(food_list)

        if target_food is not None:
            x_distance = target_food.x - self.x
            y_distance = target_food.y - self.y
            if x_distance > 0:
                self.dx += 0.02
            else:
                self.dx -= 0.02
            self.dx = constrain(self.dx, -2.2, 2.2)
            self.base_y += y_distance * 0.015
            self.base_y = constrain(self.base_y, 45, height - 35)

            if (
                dist(self.x, self.y, target_food.x, target_food.y)
                < self.body_length * 0.35
            ):
                food_list.remove(target_food)
        else:
            self.base_y += sin(frame_count * 0.02 + self.phase) * 0.35

        self.x += self.dx
        self.y = self.base_y + sin(frame_count * 0.08 + self.phase) * (8 * self.scale)

        if self.x < 35:
            self.x = 35
            self.dx = self.speed
        elif self.x > width - 35:
            self.x = width - 35
            self.dx = -self.speed

    def find_nearest_food(self, food_list):
        nearest_food = None
        nearest_distance = 10**9

        for food in food_list:
            current_distance = dist(self.x, self.y, food.x, food.y)
            if current_distance < nearest_distance:
                nearest_distance = current_distance
                nearest_food = food

        return nearest_food

    def draw(self):
        direction = 1
        if self.dx < 0:
            direction = -1

        no_stroke()
        fill(self.body_color)
        ellipse(self.x, self.y, self.body_length, self.body_height)

        fill(self.fin_color)
        triangle(
            self.x - direction * (self.body_length * 0.48),
            self.y,
            self.x - direction * (self.body_length * 0.48 + self.tail_length),
            self.y - self.body_height * 0.45,
            self.x - direction * (self.body_length * 0.48 + self.tail_length),
            self.y + self.body_height * 0.45,
        )

        fill(255, 255, 255, 160)
        ellipse(
            self.x + direction * self.body_length * 0.12,
            self.y - self.body_height * 0.12,
            self.body_length * 0.33,
            self.body_height * 0.2,
        )

        fill(255)
        circle(
            self.x + direction * self.body_length * 0.24,
            self.y - self.body_height * 0.12,
            self.eye_size * 1.6,
        )
        fill(22)
        circle(
            self.x + direction * self.body_length * 0.28,
            self.y - self.body_height * 0.12,
            self.eye_size,
        )


def draw_background():
    for row in range(height):
        blend = row / height
        red = 16 + 10 * blend
        green = 95 + 85 * blend
        blue = 165 + 55 * blend
        stroke(red, green, blue)
        line(0, row, width, row)

    no_stroke()
    fill(18, 84, 58, 180)
    rect(0, height - 42, width, 42)

    fill(200, 177, 108)
    rect(0, height - 18, width, 18)


def draw_seaweed():
    stroke(24, 118, 76)
    stroke_weight(5)

    for x_position in range(25, width, 44):
        line(
            x_position,
            height - 18,
            x_position + sin(frame_count * 0.03 + x_position * 0.1) * 10,
            height - 72 - (x_position % 3) * 12,
        )

    no_stroke()


def setup():
    global fishes, bubbles, food_list

    size(520, 320)
    fishes = []
    bubbles = []
    food_list = []

    for _ in range(7):
        fishes.append(Fish(random(50, width - 50), random(70, height - 70)))

    for _ in range(16):
        bubbles.append(Bubble())


def draw():
    draw_background()
    draw_seaweed()

    for bubble in bubbles:
        bubble.update()
        bubble.draw()

    for food in food_list[:]:
        food.update()
        food.draw()
        if food.is_outside():
            food_list.remove(food)

    for fish in fishes:
        fish.update(food_list)
        fish.draw()

    fill(255, 248, 214)
    text_size(14)
    text("Klick ins Aquarium: Futter fallen lassen", 16, 24)


def mouse_pressed():
    food_list.append(Food(mouse_x, mouse_y))
```

{{ENDSOLUTION}}
