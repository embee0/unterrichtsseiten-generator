# AGENTS.md

## Zweck

Diese Datei hält den aktuellen Arbeitsstand fest, damit nach einem VS-Code-Neustart oder Update ohne Kontextverlust weitergearbeitet werden kann.

Sie ist vor allem eine Start- und Orientierungshilfe fuer neue Sessions.
Allgemeine didaktische Leitlinien und laengerfristige Strukturregeln sollen nicht hier doppelt gepflegt werden, sondern in den zentralen Planungsdateien.

## Projektüberblick

Das Projekt entwickelt sich von einer einzelnen OOP-mit-py5-Lernseite zu einem **allgemeineren Tool zur Generierung von Unterrichtsmaterial und Unterrichtswebseiten**.

Die bisherigen Themen `kreise` und `aquarium` sind dafür vor allem Referenz- und Beispielthemen.
An ihnen wurde die Struktur für Quellen, Planung, Build-Skripte und Ausgabedateien herausgearbeitet.

Die Projektstruktur wurde aufgeräumt:

- `themen/` enthält die inhaltlichen Quellen und Beispielprogramme
- `planung/` enthält Arbeits-, Struktur- und Ideendokumente
- `build/` enthält die eigentlichen Generatoren
- `dist/` enthält die generierten HTML-Seiten

## Rollen der Meta-Dateien

- `AGENTS.md` -> Session-Start, Projektkontext, Einstiegspfade, zuletzt verifizierter Stand
- `planung/didaktische-prinzipien.md` -> allgemeine didaktische Leitlinien fuer alle Lernseiten
- `planung/arbeitsstruktur.md` -> schlanke Arbeits- und Dateistruktur fuer Themen und Materialien
- themennahe Dateien wie `themen/*/*_thema.md` -> Lernziele, Lernweg und Materiallage fuer ein einzelnes Thema
- `planung/projektideen.md` -> moegliche neue Themen oder Fortsetzungen

## Wichtige Dateien

- `themen/kreise/LERNSEITE.kreise.md` → Beispiel für eine inhaltliche Hauptquelle
- `themen/aquarium/LERNSEITE.aquarium.md` → weiteres Beispiel für eine inhaltliche Hauptquelle
- `planung/didaktische-prinzipien.md` → zentrale Sammlung der didaktischen Leitlinien für neue und bestehende Lernseiten
- `build/render_lernseite.py` → zentraler Generator, aktuell noch teilweise thematisch auf py5/OOP zugeschnitten
- `build/build_lernseite.py` → generischer Build-Einstieg für ein einzelnes Thema oder alle Themen
- `build/build_kreise_lernseite.py` → themenspezifischer Wrapper für Quelle und Ziel von `kreise`
- `build/build_aquarium_lernseite.py` → themenspezifischer Wrapper für Quelle und Ziel
- `build_lernseite.py` → Root-Wrapper für den generischen Build-Aufruf
- `build_kreise_lernseite.py` → Root-Wrapper für das Kreis-Beispiel
- `build_aquarium_lernseite.py` → Root-Wrapper für das Aquarium-Beispiel
- `dist/kreise-lernseite.html` → generierte Beispiel-Ausgabe für `kreise`
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

## Referenzthemen

Die bisherigen Themen `kreise` und `aquarium` sind Referenzthemen fuer Aufbau, Lernweg und Materialstruktur.
Die konkreten didaktischen Leitlinien stehen in `planung/didaktische-prinzipien.md`.
Die themenspezifischen Lernwege stehen in den jeweiligen Quellen unter `themen/`.

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
python3 build_lernseite.py aquarium
python3 build_lernseite.py kreise
python3 build_lernseite.py --all
python3 build_kreise_lernseite.py
python3 build_aquarium_lernseite.py
```

Danach werden die Dateien in `dist/` überschrieben.

Die themenspezifischen Root-Befehle bleiben als kurze Gewohnheitsbefehle erhalten.

Der aktuelle Aufbau ist schon so gedacht, dass weitere Themen über zusätzliche Wrapper oder eine spätere allgemeinere Build-Schnittstelle angebunden werden können.

## Technischer Fokus

Der zentrale Renderer ist `build/render_lernseite.py`.
Er ist bereits fuer mehrere Themen nutzbar, aber noch nicht vollstaendig themenagnostisch.
Details zu offener Technik oder Infrastruktur gehoeren nach `planung/technik-todos.md`.

## Wichtige Projektkonstanten

- sichtbare Codebeispiele wurden auf `size(200, 200)` umgestellt
- eingebettete Vorschauen sind einheitlich `300x300`
- die Seiten richten sich an Schueler:innen

## Jüngste Änderungen

- Anfang von `LERNSEITE.kreise.md` wurde stark überarbeitet und ist maßgeblich
- Generator wurde angepasst, damit `_nicht_` korrekt als Kursivtext erscheint
- Margin-Note-Layout wurde zuletzt nachgeschärft
- py5-Fallback für zu lange URLs wurde ergänzt
- Projekt wurde in `themen/`, `planung/`, `build/` und `dist/` neu strukturiert
- beide HTML-Seiten wurden aus der neuen Struktur erfolgreich neu gebaut
- Zielrichtung der Umstrukturierung: weg von zwei Einzelbeispielen hin zu einem allgemeinen Generator für Unterrichtsmaterial

## Bekannte Punkte / nächster Check nach Neustart

1. Prüfen, ob `dist/kreise-lernseite.html` und `dist/aquarium-lernseite.html` optisch die aktuelle Version zeigen
2. Falls die alte Ansicht sichtbar ist: Browser/Preview hart neu laden
3. Falls Randbemerkungen optisch noch nicht gut sitzen: CSS in `build/render_lernseite.py` weiter anpassen

## Letzter verifizierter Stand

- Root-Wrapper `build_kreise_lernseite.py` und `build_aquarium_lernseite.py` funktionieren
- `build/render_lernseite.py` war nach der Pfadumstellung fehlerfrei
- `dist/kreise-lernseite.html` wurde neu erzeugt
- `dist/aquarium-lernseite.html` wurde neu erzeugt
- Margin-Notes wurden im HTML als `<aside class="margin-note">...` erzeugt

## Falls weitergearbeitet wird

Zuerst diese drei Dateien prüfen:

- `planung/didaktische-prinzipien.md`
- `planung/arbeitsstruktur.md`
- eine passende Quelldatei unter `themen/`, zum Beispiel `themen/kreise/LERNSEITE.kreise.md` oder `themen/aquarium/LERNSEITE.aquarium.md`

Danach bei Bedarf diese Datei prüfen:

- `build/render_lernseite.py`

Dann bei Bedarf neu bauen mit:

```bash
python3 build_kreise_lernseite.py
python3 build_aquarium_lernseite.py
```

Wenn die Generalisierung weitergeführt werden soll, danach besonders prüfen:

- welche Teile im Generator noch auf `kreise` oder `py5` fest verdrahtet sind
- wie neue Themen konfiguriert statt per Dateikonstanten eingebunden werden sollen
- ob aus den bisherigen Wrappern eine allgemeinere CLI oder Konfigurationsdatei werden soll

Bei neuen Lernseiten oder groesseren Ueberarbeitungen gilt zusaetzlich:

- zuerst die didaktischen Leitlinien in `planung/didaktische-prinzipien.md` gegen den geplanten Lernweg pruefen
- dann Thema, Pflichtweg, Bonusideen und passende Hilfestufen festlegen
- themenspezifische Details danach in einer passenden Datei unter `themen/` festhalten statt hier in `AGENTS.md`
