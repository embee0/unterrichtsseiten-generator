# AGENTS.md

## Zweck

Diese Datei hält den aktuellen Arbeitsstand fest, damit nach einem VS-Code-Neustart oder Update ohne Kontextverlust weitergearbeitet werden kann.

## Projektüberblick

Das Projekt entwickelt sich von einer einzelnen OOP-mit-py5-Lernseite zu einem **allgemeineren Tool zur Generierung von Unterrichtsmaterial und Unterrichtswebseiten**.

Die bisherigen Themen `kreise` und `aquarium` sind dafür vor allem Referenz- und Beispielthemen.
An ihnen wurde die Struktur für Quellen, Planung, Build-Skripte und Ausgabedateien herausgearbeitet.

Die Projektstruktur wurde aufgeräumt:

- `themen/` enthält die inhaltlichen Quellen und Beispielprogramme
- `planung/` enthält Arbeits-, Struktur- und Ideendokumente
- `build/` enthält die eigentlichen Generatoren
- `dist/` enthält die generierten HTML-Seiten

## Wichtige Dateien

- `themen/kreise/LERNSEITE.kreise.md` → Beispiel für eine inhaltliche Hauptquelle
- `themen/aquarium/LERNSEITE.aquarium.md` → weiteres Beispiel für eine inhaltliche Hauptquelle
- `build/build_lernseite.py` → zentraler Generator, aktuell noch teilweise thematisch auf py5/OOP zugeschnitten
- `build/build_aquarium_lernseite.py` → themenspezifischer Wrapper für Quelle und Ziel
- `build_lernseite.py` → Root-Wrapper für das Kreis-Beispiel
- `build_aquarium_lernseite.py` → Root-Wrapper für das Aquarium-Beispiel
- `dist/livecoding-doku.html` → generierte Beispiel-Ausgabe für `kreise`
- `dist/aquarium-lernseite.html` → generierte Beispiel-Ausgabe für `aquarium`
- `planung/arbeitsstruktur.md` → zentrale Arbeitsdatei für die weitere Zusammenarbeit
- `planung/projektideen.md` → Fortsetzungs-/Alternativprojekte

### py5-Beispieldateien

Die Kreis-Beispiele liegen in `themen/kreise/`, die Aquarium-Beispiele in `themen/aquarium/`.

- `kreise0noch_ohne_OO.py`
- `kreise1OO.py`
- `kreise1aOO_ein_objekt.py`
- `kreise1bOO_mit_durchmesser.py`
- `kreise2OOzweikreise.py`
- `kreise2aOO_zwei_objekte.py`
- `kreise2bOO_liste_von_objekten.py`
- `kreise3aOO_verhalten_und_farbe.py`
- `kreise3OOvielekreise.py`

## Aktueller Inhalt / didaktischer Stand

Die Lernseite erklärt den Weg von einem nicht-objektorientierten py5-Programm hin zu vielen OOP-Kreisen in Stationen:

1. Kreis ohne OOP
2. erste Klasse
3. Attribut `durchmesser`
4. zwei Objekte
5. Liste von Objekten
6. Verhalten als Methode
7. viele Kreise mit eigenem Zustand

Zu jeder Station gibt es:

- Erklärung, was geändert wird
- Erklärung, warum das sinnvoll ist
- passenden OOP-Begriff
- py5-Vorschau
- Link zum Bearbeiten
- Codeblock auf der Seite

## Autoring-Workflow

### Quelle

Inhalt direkt nur in den Markdown-Quellen unter `themen/` bearbeiten.

- Die bestehenden Themen unter `themen/` dienen aktuell als Muster für weitere Themen.
- Neue Themen sollten dieselbe Trennung aus Inhaltsquelle, Code-/Materialdateien und generierter Ausgabe übernehmen.

### Interne Kommentare

Interne Notizen in den Lernseiten nur mit diesem Format:

```html
<!-- COPILOT: ... -->
```

Diese Kommentare sollen nicht auf der Website erscheinen.

### Platzhalter in den `LERNSEITE.*.md`-Dateien

Gelten in den Lernseiten unter `themen/`:

- `{{IFRAME: datei.py}}` → eingebettete py5-Vorschau
- `{{EDIT: datei.py}}` → Link zum Bearbeiten im py5-Editor
- Zeilen mit `>` → Randbemerkungen / margin notes

## Build

HTML neu erzeugen mit:

```bash
python3 build_lernseite.py
python3 build_aquarium_lernseite.py
```

Danach werden die Dateien in `dist/` überschrieben.

Der aktuelle Aufbau ist schon so gedacht, dass weitere Themen über zusätzliche Wrapper oder eine spätere allgemeinere Build-Schnittstelle angebunden werden können.

## Technische Hinweise zum Generator

Der zentrale Generator kann aktuell:

- Markdown-artige Abschnitte rendern
- py5-Links direkt aus den aktuellen `.py`-Dateien erzeugen
- Python-Codeblöcke syntax-highlighten
- Randbemerkungen aus `>`-Zeilen rendern
- `_kursiv_`, `` `code` ``, `**fett**` und Links verarbeiten
- bei zu langen py5-URLs eine lokale Fallback-Box statt eines kaputten iframes anzeigen

Er ist damit bereits als zentraler Renderer nutzbar, ist aber noch nicht vollständig themenagnostisch.
Derzeit sind insbesondere Standardpfade, HTML-Title und py5-spezifische Platzhalterlogik noch fest eingebaut.

## Wichtige inhaltliche Entscheidungen

- sichtbare Codebeispiele wurden auf `size(200, 200)` umgestellt
- eingebettete Vorschauen sind einheitlich `300x300`
- Tonfall: leicht humorvoll, aber nicht albern
- Seite ist **für Schüler:innen**, nicht als Lehrkraft-Dokumentation gedacht
- Ziel ist Nachvollziehbarkeit des OOP-Aufbaus, nicht vollständige Theorie

## Jüngste Änderungen

- Anfang von `LERNSEITE.kreise.md` wurde stark überarbeitet und ist maßgeblich
- Generator wurde angepasst, damit `_nicht_` korrekt als Kursivtext erscheint
- Margin-Note-Layout wurde zuletzt nachgeschärft
- py5-Fallback für zu lange URLs wurde ergänzt
- Projekt wurde in `themen/`, `planung/`, `build/` und `dist/` neu strukturiert
- beide HTML-Seiten wurden aus der neuen Struktur erfolgreich neu gebaut
- Zielrichtung der Umstrukturierung: weg von zwei Einzelbeispielen hin zu einem allgemeinen Generator für Unterrichtsmaterial

## Bekannte Punkte / nächster Check nach Neustart

1. Prüfen, ob `dist/livecoding-doku.html` und `dist/aquarium-lernseite.html` optisch die aktuelle Version zeigen
2. Falls die alte Ansicht sichtbar ist: Browser/Preview hart neu laden
3. Falls Randbemerkungen optisch noch nicht gut sitzen: CSS in `build/build_lernseite.py` weiter anpassen

## Letzter verifizierter Stand

- Root-Wrapper `build_lernseite.py` und `build_aquarium_lernseite.py` funktionieren
- `build/build_lernseite.py` war nach der Pfadumstellung fehlerfrei
- `dist/livecoding-doku.html` wurde neu erzeugt
- `dist/aquarium-lernseite.html` wurde neu erzeugt
- Margin-Notes wurden im HTML als `<aside class="margin-note">...` erzeugt

## Falls weitergearbeitet wird

Zuerst diese drei Dateien prüfen:

- `planung/arbeitsstruktur.md`
- eine passende Quelldatei unter `themen/`, zum Beispiel `themen/kreise/LERNSEITE.kreise.md` oder `themen/aquarium/LERNSEITE.aquarium.md`
- `build/build_lernseite.py`

Dann bei Bedarf neu bauen mit:

```bash
python3 build_lernseite.py
python3 build_aquarium_lernseite.py
```

Wenn die Generalisierung weitergeführt werden soll, danach besonders prüfen:

- welche Teile im Generator noch auf `kreise` oder `py5` fest verdrahtet sind
- wie neue Themen konfiguriert statt per Dateikonstanten eingebunden werden sollen
- ob aus den bisherigen Wrappern eine allgemeinere CLI oder Konfigurationsdatei werden soll
