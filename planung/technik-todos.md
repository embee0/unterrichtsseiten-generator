# Technische ToDos

Dieses Dokument sammelt die offenen technischen Punkte, die nicht in den inhaltlichen Themenquellen stehen sollten.

## Akute Punkte

### 1. py5-Embed ohne lange `sketch=`-URL

Problem:
Die eingebetteten py5-Vorschauen basieren aktuell auf einer externen URL mit `?sketch=`-Parameter. Der Python-Code wird dafür URL-kodiert und anschließend base64-codiert in die URL gepackt.

Konsequenz:
Längere Sketches stoßen an URL-Grenzen. Das betrifft beim Aquarium schon die Endlösung, wenn sie früh auf der Seite als Demo eingebettet werden soll.

Aktueller Stand:
- Der Generator fängt das Problem mit einer Fallback-Box ab, statt einen kaputten iframe zu erzeugen.
- Für Editor- und Vorschau-Links funktioniert das als Notlösung, löst aber das eigentliche Embed-Problem nicht.

Ziel:
Eine Möglichkeit finden, sich mindestens für iframes von der externen py5-URL mit `sketch=`-Parameter zu lösen.

Mögliche Richtungen:
- lokale HTML/JS-Hülle pro Sketch erzeugen und diese im iframe laden
- Sketch-Code als separate Datei ausgeben und eine lokale Präsentationsseite darauf zeigen lassen
- eigenen kleinen Preview-Mechanismus im generierten Material vorsehen

### 2. Git sauber aufsetzen

Problem:
Das Projekt war bisher noch nicht als Git-Repository aufgesetzt.

Ziel:
Das Projekt versionieren, damit Änderungen am Generator, an den Themenquellen und an der Planung nachvollziehbar bleiben.

Minimaler Stand:
- Git-Repository initialisieren
- `.gitignore` für `.venv`, `__pycache__` und ähnliche lokale Artefakte anlegen
- danach regulär mit Commits arbeiten

## Später sinnvoll

### 3. Globale Design- und Build-Änderungen zentral halten

Der Build ist inzwischen so vorbereitet, dass mehrere Themen gemeinsam gebaut werden können. Weitere Änderungen an Layout, HTML-Grundstruktur und gemeinsamen Regeln sollten möglichst zentral im Generator passieren.

### 4. Weitere Themen ohne Strukturumbau ergänzen

Neue Themen sollten möglichst nur über eine neue Quelldatei, passende Materialien und einen neuen Eintrag in der zentralen Themenkonfiguration hinzukommen.