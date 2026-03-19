# Build

Hier liegen die eigentlichen Generatoren des Projekts.

- `render_lernseite.py` ist der zentrale Generator
- `build_lernseite.py` ist der generische Einstieg für einen einzelnen Build oder einen Sammel-Build
- `build_kreise_lernseite.py` und `build_aquarium_lernseite.py` sind nur noch dünne Themen-Wrapper
- `site_config.py` hält die kleine zentrale Themenliste; Quelle und Ziel folgen dort einer festen Konvention
- `build_all_lernseiten.py` baut alle aktuell eingetragenen Themen nacheinander

Der Generator erzeugt für `{{IFRAME: ...}}` lokale Vorschau-Seiten unter `dist/_previews/`, damit eingebettete Sketches nicht mehr an langen `sketch=`-URLs scheitern.

Der Generator exportiert bei Bedarf außerdem Python-Dateien nach `dist/_sources/`, damit zu lange Editor-Links auf eine lokale Datei zurückfallen können.

Die Root-Dateien `build_kreise_lernseite.py` und `build_aquarium_lernseite.py` im Projektwurzelverzeichnis sind nur Wrapper für die gewohnten Befehle.
Zusätzlich gibt es mit `build_lernseite.py` im Projektwurzelverzeichnis einen generischen Aufruf und mit `build_all_lernseiten.py` einen Sammel-Build.

Beispiele:

- `python3 build_lernseite.py kreise`
- `python3 build_lernseite.py aquarium`
- `python3 build_lernseite.py --all`
