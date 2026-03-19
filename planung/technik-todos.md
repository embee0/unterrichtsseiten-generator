# Technische ToDos

Dieses Dokument sammelt die noch offenen technischen Punkte, die nicht in den inhaltlichen Themenquellen stehen sollten.

## Erledigt oder weitgehend erledigt

### 1. py5-Embeds von langen `sketch=`-URLs entkoppeln

Stand:

- Der Generator erzeugt lokale Preview-Seiten unter `dist/_previews/`.
- Iframes hängen damit nicht mehr an einer langen externen `?sketch=`-URL.
- Zu lange Editor-Links fallen bereits auf eine lokale Ersatzbox mit Python-Datei zurück.

Fazit:

- Das ursprüngliche iframe-Problem ist gelöst.
- Offen ist nur noch eine mögliche spätere Verbesserung für den Editor-Weg.

### 2. Git sauber aufsetzen

Stand:

- Das Projekt ist als Git-Repository aufgesetzt.
- Eine `.gitignore` für `.venv`, `__pycache__` und ähnliche lokale Artefakte ist vorhanden.
- Versionierung ist damit im normalen Arbeitsfluss angekommen.

Fazit:

- Dieser Punkt ist erledigt.

### 3. Globale Design- und Build-Änderungen zentral halten

Stand:

- `build/render_lernseite.py` ist der zentrale Renderer.
- `build/site_config.py` hält die zentrale Themenkonfiguration.
- `build/build_lernseite.py` ist jetzt der generische Einstiegspunkt für Einzel- und Sammel-Builds.
- `build/build_all_lernseiten.py` baut alle eingetragenen Themen gesammelt.
- Gemeinsame Layout- und Render-Änderungen laufen damit bereits zentral.

Fazit:

- Der Punkt ist weitgehend erreicht.
- Offen bleibt nur die weitere Generalisierung des Renderers.

### 4. Weitere Themen ohne Strukturumbau ergänzen

Stand:

- Neue Themen lassen sich bereits über `themen/...`, einen Eintrag in `build/site_config.py` und bei Bedarf einen kleinen Wrapper anbinden.
- Die aktuelle Struktur mit `themen/`, `build/`, `planung/` und `dist/` trägt bereits mehrere Themen.

Fazit:

- Der strukturelle Umbau ist hier nicht mehr das eigentliche Problem.
- Offen ist eher, wie weit die Anbindung noch vereinfacht oder verallgemeinert werden soll.

## Noch offene Technikfragen

### 1. Editor-Weg unabhängig von externer `sketch=`-URL machen

Aktueller Stand:

- Für Vorschauen ist das URL-Längenproblem gelöst.
- Für Editor-Links wird weiterhin der externe py5-Link mit `?sketch=` genutzt.
- Bei zu langen Links gibt es bereits einen funktionierenden Fallback auf die exportierte Python-Datei unter `dist/_sources/`.

Offene Frage:

- Soll der Editor-Weg später ebenfalls komplett lokal oder robuster gelöst werden?

Mögliche Richtungen:

- lokale HTML/JS-Hülle auch für den Bearbeitungsweg
- separate Sketch-Dateien plus lokale Startseite
- bestehende Fallback-Lösung bewusst als Dauerlösung akzeptieren

### 2. Renderer weiter themenagnostisch machen

Aktueller Stand:

- Der Renderer funktioniert bereits für mehrere Themen.
- Einige Teile sind aber noch klar auf py5-Lernseiten zugeschnitten, zum Beispiel Platzhalterlogik, Preview-Erzeugung und py5-spezifische Annahmen.

Offene Frage:

- Soll der Generator nur mehrere py5-Themen bedienen oder mittelfristig allgemeiner Unterrichtsmaterial-Generator werden?

Naheliegende nächste Schritte:

- py5-spezifische Teile klarer kapseln
- allgemeine Renderlogik und themenspezifische Erweiterungen stärker trennen

### 3. Themenanbindung weiter vereinfachen

Aktueller Stand:

- Die zentrale Themenliste in `build/site_config.py` funktioniert bereits.
- Neue Themen brauchen aber weiterhin etwas manuelle Verdrahtung.

Offene Frage:

- Reicht die aktuelle kleine Konfiguration, oder soll daraus spaeter eine allgemeinere CLI- oder Konfigurationsstruktur werden?

Mögliche Richtungen:

- bei der jetzigen kleinen `site_config.py` bleiben
- Konfiguration pro Thema in eigene Datei auslagern
- allgemeineren Build-Befehl für neue Themen einführen
