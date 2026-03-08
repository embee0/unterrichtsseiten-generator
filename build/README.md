# Build

Hier liegen die eigentlichen Generatoren des Projekts.

- `build_lernseite.py` ist der zentrale Generator
- `build_aquarium_lernseite.py` setzt Quelle und Ziel für das Aquarium-Thema
- `site_config.py` hält die kleine zentrale Themenliste für Quelle, Ziel und Seitentitel
- `build_all_lernseiten.py` baut alle aktuell eingetragenen Themen nacheinander

Die Root-Dateien `build_lernseite.py` und `build_aquarium_lernseite.py` im Projektwurzelverzeichnis sind nur Wrapper für die gewohnten Befehle.
Zusätzlich gibt es mit `build_all_lernseiten.py` im Projektwurzelverzeichnis einen Sammel-Build für alle eingetragenen Themen.