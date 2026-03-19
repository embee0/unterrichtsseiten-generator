# Drohnenangriff mit OOP in py5

<!-- COPILOT: Diese Datei ist die inhaltliche Hauptquelle für die Drohnenangriff-Lernseite. -->
<!-- COPILOT: Platzhalter {{IFRAME: datei.py}} und {{EDIT: datei.py}} werden beim HTML-Bau automatisch aufgelöst. -->
<!-- COPILOT: Zeilen mit > werden als Randbemerkungen dargestellt. -->

In dieser Seite baust du Schritt für Schritt ein kleines Verfolgungsspiel in py5. Du startest mit einem Agenten und einer Drohne. Später jagt die Drohne den Agenten. Am Ende kannst du das Spiel noch zu einem ganzen Drohnenschwarm ausbauen.

{{IFRAME: drohnenangriff_endloesung.py}}

> **Vorschau:** So kann dein Spiel am Ende aussehen. Die Vorschau läuft am Anfang auch ohne Tastendruck schon als Demo. Du musst das noch nicht sofort verstehen.

Diesmal geht es nicht zuerst um viele Extras, sondern um eine klare Kernidee: **zwei Klassen mit verschiedenen Rollen**. Ein Agent flieht. Eine Drohne verfolgt.

Die ersten Pflichtstationen bleiben absichtlich klein. Du sollst nicht gleichzeitig neue Syntax, neue Steuerung, neue Bewegungen und mehrere Listen auf einmal lernen.

## Worum es in dieser Woche geht

Die **Pflichtphase** sind Station 1 bis 5.

Am Ende dieser Pflichtphase kannst du:

- eine Klasse `Agent` und eine Klasse `Drohne` anlegen
- Attribute und Methoden in beiden Klassen nutzen
- eine einfache Verfolgungslogik programmieren
- mit einem Rückgabewert eine Kollision prüfen
- mehrere Drohnen in einer Liste verwalten

Danach kannst du das Spiel in einer Kreativstation mit weiteren Ideen ausbauen.

> **Kernidee:** Das eigentlich Wichtige ist hier nicht die Tastatursteuerung, sondern die Predator-Prey-Mechanik. Deshalb ist die Steuerung in dieser Lernseite früh schon weitgehend vorbereitet.

---

## So arbeitest du

Arbeite die Stationen der Reihe nach durch.

1. Lies den Arbeitsauftrag.
2. Schaue dir die Demo an.
3. Baue den Schritt selbst nach.
4. Gehe erst weiter, wenn dein Programm in diesem Schritt funktioniert.

> **Pflicht und Bonus:** Station 1 bis 5 sind der verbindliche Kern. Danach kommt eine offene Kreativstation mit eigenen Erweiterungen.

---

## Station 1 - Agent und Drohne darstellen

### Arbeitsauftrag

1. Lege eine Klasse `Agent` an.
2. Lege eine Klasse `Drohne` an.
3. Beide Klassen bekommen einen Konstruktor mit `x` und `y`.
4. Schreibe für beide Klassen eine Methode `draw()`.
5. Erzeuge in `setup()` genau einen Agenten und genau eine Drohne.

### Warum dieser Schritt?

Du startest nicht mit Bewegung, sondern mit der Struktur. So wird zuerst klar, dass Agent und Drohne zwei verschiedene Objekte mit verschiedenen Rollen sind.

### Dabei lernst du

- zwei Klassen im selben Projekt
- Objekt und Instanz
- Attribute für Position
- Methoden zum Zeichnen

> **Noch ohne Bewegung:** In dieser ersten Station reicht es völlig, wenn Agent und Drohne nur sichtbar sind. Die Jagd kommt erst später.

### Demo

{{IFRAME: drohnenangriff1_agent_und_drohne.py}}

{{EDIT: drohnenangriff1_aufgabe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 1 anzeigen}}

{{EDIT: drohnenangriff1_agent_und_drohne.py | Musterlösung im Editor öffnen}}

```python
class Agent:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

    def draw(self):
        no_stroke()
        fill(110, 220, 255)
        circle(self.x, self.y, 32)


class Drohne:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

    def draw(self):
        no_stroke()
        fill(255, 112, 112)
        rect(self.x - 13, self.y - 13, 26, 26, 6)
```

{{ENDSOLUTION}}

---

## Station 2 - Der Agent kann gesteuert werden

### Arbeitsauftrag

1. Ergänze den Agenten um eine Geschwindigkeit.
2. Nutze die vorbereitete Tastaturabfrage, damit der Agent mit `WASD` bewegt werden kann.
3. Schreibe eine Methode `steuern()`.
4. Achte darauf, dass der Agent im Spielfeld bleibt.

### Warum dieser Schritt?

Jetzt wird aus der statischen Figur ein spielbares Objekt. Die Steuerung ist hier bewusst vorbereitet, damit du dich nicht in technischen Details verlierst.

### Dabei lernst du

- Methode als Verhalten
- Änderung von Attributen während des Programms
- Begrenzung am Rand

> **Entlastung:** Die Tastatursteuerung ist diesmal nicht der eigentliche Knackpunkt. Wir arbeiten deshalb mit vier einfachen Variablen statt mit einem `dict`. Wichtig ist, dass du verstehst, wie der Agent seine Position verändert.

> **Technik im Hintergrund:** In der vorbereiteten Tastaturabfrage tauchen auch Dinge wie `key` oder `key_code` auf. Das musst du hier nicht selbst herleiten. Für diese Station ist wichtig, was mit `links`, `rechts`, `oben` und `unten` passiert.

### Demo

{{IFRAME: drohnenangriff2_agent_steuern.py}}

{{EDIT: drohnenangriff2_aufgabe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 2 anzeigen}}

{{EDIT: drohnenangriff2_agent_steuern.py | Musterlösung im Editor öffnen}}

```python
class Agent:
    def __init__(self, x_position, y_position, speed):
        self.x = x_position
        self.y = y_position
        self.speed = speed
        self.radius = 16

    def steuern(self):
        if links:
            self.x -= self.speed
        if rechts:
            self.x += self.speed
        if oben:
            self.y -= self.speed
        if unten:
            self.y += self.speed

        self.x = constrain(self.x, self.radius, width - self.radius)
        self.y = constrain(self.y, self.radius, height - self.radius)
```

{{ENDSOLUTION}}

---

## Station 3 - Die Drohne verfolgt den Agenten

### Arbeitsauftrag

1. Schreibe in der Klasse `Drohne` eine Methode `verfolgen(ziel_x, ziel_y)`.
2. Vergleiche in dieser Methode die aktuelle Position der Drohne mit dem Ziel.
3. Bewege die Drohne in kleinen Schritten nach links, rechts, oben oder unten.
4. Lasse in `draw()` zuerst den Agenten steuern und danach die Drohne verfolgen.

### Warum dieser Schritt?

Hier steckt die eigentliche Spielidee drin. Die Drohne reagiert nicht einfach nur auf Tastendruck, sondern orientiert sich an einem anderen Objekt.

### Dabei lernst du

- Parameter als Zielwerte
- Verhalten zwischen zwei Objekten
- einfache Verfolgungslogik

> **Einfach reicht:** Die Drohne muss noch nicht "intelligent" sein. Es reicht, wenn sie in x- und y-Richtung Schritt für Schritt näher kommt.

### Demo

{{IFRAME: drohnenangriff3_verfolgung.py}}

{{EDIT: drohnenangriff3_aufgabe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 3 anzeigen}}

{{EDIT: drohnenangriff3_verfolgung.py | Musterlösung im Editor öffnen}}

```python
class Drohne:
    def __init__(self, x_position, y_position, speed):
        self.x = x_position
        self.y = y_position
        self.speed = speed

    def verfolgen(self, ziel_x, ziel_y):
        if ziel_x > self.x:
            self.x += self.speed
        elif ziel_x < self.x:
            self.x -= self.speed

        if ziel_y > self.y:
            self.y += self.speed
        elif ziel_y < self.y:
            self.y -= self.speed
```

{{ENDSOLUTION}}

---

## Station 4 - Abstand und Kollision prüfen

### Arbeitsauftrag

1. Ergänze in der Klasse `Agent` eine Methode `position()`.
2. Diese Methode soll `self.x` und `self.y` zurückgeben.
3. Ergänze in der Klasse `Drohne` eine Methode `abstand(ax, ay)`.
4. Diese Methode soll den Abstand zwischen Drohne und Agent als Zahl zurückgeben.
5. Wenn der Abstand klein genug ist, endet das Spiel mit einer Meldung.

### Warum dieser Schritt?

Jetzt kommt der Rückgabewert an einer klaren Stelle ins Spiel. Die Methoden geben nicht nur etwas aus, sondern liefern einen Wert, mit dem dein Hauptprogramm weiterarbeiten kann.

### Dabei lernst du

- `return` für Rückgabewerte
- einen Rückgabewert direkt in zwei Variablen aufteilen
- Rückgabewerte in Bedingungen nutzen
- Kollision als Spielregel

> **Rückgabewerte:** `position()` liefert die aktuelle Position des Agenten zurück. Diese zwei Werte kannst du direkt in zwei Variablen auffangen: `agent_x, agent_y = agent.position()`. `abstand(...)` liefert eine Zahl. Diese Zahl kannst du direkt in einer `if`-Bedingung benutzen.

> **Neuer Schritt:** Das ist hier absichtlich neu. Eine Methode kann also nicht nur genau einen Wert zurückgeben, sondern auch mehrere Werte, die du direkt passend auf Variablen verteilen kannst.

> **Abstand messen:** Für `abstand(...)` musst du die Formel nicht selbst erfinden. In py5 gibt es mit `dist(...)` schon eine fertige Funktion für den Abstand zwischen zwei Punkten.

### Demo

{{IFRAME: drohnenangriff4_kollision.py}}

{{EDIT: drohnenangriff4_aufgabe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 4 anzeigen}}

{{EDIT: drohnenangriff4_kollision.py | Musterlösung im Editor öffnen}}

```python
agent_x, agent_y = agent.position()
drohne.verfolgen(agent_x, agent_y)

if drohne.abstand(agent_x, agent_y) < 18:
    game_over = True
```

{{ENDSOLUTION}}

---

## Station 5 - Mehrere Drohnen

### Arbeitsauftrag

1. Erzeuge nicht mehr nur eine Drohne, sondern mehrere.
2. Speichere sie in einer Liste `drohnen`.
3. Gehe in `draw()` mit einer Schleife durch die Liste.
4. Lasse alle Drohnen verfolgen und prüfe für jede die Kollision.
5. Gib den Drohnen zufällige Farben, damit sie sich besser unterscheiden.

### Warum ist das eine gute Erweiterung?

Erst hier lohnt sich die Liste wirklich. Du überträgst die bekannte Logik auf mehrere Objekte derselben Klasse.

### Dabei lernst du

- Liste von Objekten
- gleiche Logik für mehrere Instanzen
- zufällige Attribute für mehr Variation

> **Wichtiger Schritt:** Diese Station gehört noch zum Kern des Projekts. Erst mit mehreren Drohnen wird richtig sichtbar, warum OOP und Listen zusammen nützlich sind.

> **Farben:** Der Ausdruck mit `color(random(...), random(...), random(...))` darf hier ruhig erstmal als fertiges Muster benutzt werden. Wichtig ist vor allem die Idee: Jede Drohne bekommt beim Erzeugen ihren eigenen Farbwert als Attribut.

### Demo

{{IFRAME: drohnenangriff5_mehrere_drohnen.py}}

{{EDIT: drohnenangriff5_aufgabe.py | Aufgabe im Editor öffnen}}

{{SOLUTION: Lösungscode zu Station 5 anzeigen}}

{{EDIT: drohnenangriff5_mehrere_drohnen.py | Musterlösung im Editor öffnen}}

```python
class Drohne:
    def __init__(self, x_position, y_position, speed):
        self.x = x_position
        self.y = y_position
        self.speed = speed
        self.body_color = color(random(120, 255), random(90, 220), random(90, 255))


drohnen = [
    Drohne(110, 90, 0.18),
    Drohne(150, 150, 0.22),
    Drohne(110, 220, 0.26),
]

for drohne in drohnen:
    drohne.verfolgen(agent_x, agent_y)
    if drohne.abstand(agent_x, agent_y) < 18:
        game_over = True
```

{{ENDSOLUTION}}

---

## Station 6 - Kreative Erweiterungen

### Arbeitsauftrag

Wähle eine oder mehrere Ideen aus und erweitere dein Spiel selbstständig.

### Mögliche Ideen

1. **Hübscher machen:** Verändere Farben, Formen, Hintergrund oder HUD.
2. **Punktezähler:** Zähle, wie lange man überlebt, und zeige den Wert sichtbar an.
3. **Teleportation:** Mit einer Taste springt der Agent einmal an eine neue Stelle.
4. **Sprint:** Der Agent kann für kurze Zeit schneller werden.
5. **Schwierigkeit steigern:** Die Drohnen werden mit der Zeit etwas schneller.
6. **Neustarttaste:** Starte das Spiel per Taste neu.
7. **Besondere Zonen:** Baue Bereiche ein, die schützen oder verlangsamen.

### Warum ist das eine gute Station?

Hier planst du selbst, welche Idee du umsetzen willst. Du benutzt die bekannten Klassen und Methoden weiter, entscheidest aber eigenständiger, wie dein Spiel sich entwickeln soll.

### Dabei lernst du

- bekannte Bausteine kreativ weiterverwenden
- Spielideen selbst planen
- eigene Zusatzregeln programmieren

> **Kreativstation:** Nimm dir lieber eine Idee vor, die sauber funktioniert, statt fünf Dinge gleichzeitig halb anzufangen.
