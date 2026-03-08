# Technische ToDos

Dieses Dokument sammelt die offenen technischen Punkte, die nicht in den inhaltlichen Themenquellen stehen sollten.

## Akute Punkte

### 1. py5-Embed ohne lange `sketch=`-URL

Problem:
Die eingebetteten py5-Vorschauen basieren aktuell auf einer externen URL mit `?sketch=`-Parameter. Der Python-Code wird dafür URL-kodiert und anschließend base64-codiert in die URL gepackt.

Konsequenz:
Längere Sketches stoßen an URL-Grenzen. Das betrifft beim Aquarium schon die Endlösung, wenn sie früh auf der Seite als Demo eingebettet werden soll.

Aktueller Stand:

- Der Generator erzeugt für iframes jetzt lokale Preview-Seiten unter `dist/_previews/`.
- Damit sind die eingebetteten Vorschauen nicht mehr von einer langen externen `?sketch=`-URL abhängig.
- Die Editor-Links nutzen weiterhin den externen py5-Link mit `?sketch=` und fallen bei zu langen URLs auf eine lokale Ersatzbox zurück.

Ziel:
Für iframes ist die Entkopplung erreicht. Offen ist noch, ob später auch die Editor-Nutzung von der externen `sketch=`-URL gelöst werden soll.

Mögliche Richtungen:

- lokale HTML/JS-Hülle pro Sketch erzeugen und diese im iframe laden
- Sketch-Code als separate Datei ausgeben und eine lokale Präsentationsseite darauf zeigen lassen
- bei Bedarf später auch den Editor-Weg ersetzen oder ergänzen

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
