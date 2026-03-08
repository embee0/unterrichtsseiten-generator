.PHONY: help build all kreise aquarium status publish

PYTHON ?= python3

KREISE_TARGET := dist/livecoding-doku.html
AQUARIUM_TARGET := dist/aquarium-lernseite.html

KREISE_DEPS := \
	build_lernseite.py \
	build/build_lernseite.py \
	build/site_config.py \
	themen/kreise/LERNSEITE.kreise.md \
	$(wildcard themen/kreise/*.py)

AQUARIUM_DEPS := \
	build_aquarium_lernseite.py \
	build/build_aquarium_lernseite.py \
	build/build_lernseite.py \
	build/site_config.py \
	themen/aquarium/LERNSEITE.aquarium.md \
	$(wildcard themen/aquarium/*.py)

help:
	@printf "Verfuegbare Ziele:\n"
	@printf "  make build     - alle Seiten neu generieren\n"
	@printf "  make all       - Alias fuer build\n"
	@printf "  make kreise    - nur die Kreis-Seite neu generieren\n"
	@printf "  make aquarium  - nur die Aquarium-Seite neu generieren\n"
	@printf "  make status    - Git-Status kurz anzeigen\n"
	@printf "  make publish   - build ausfuehren und aktuellen Branch pushen\n"
	@printf "\n"
	@printf "Die Build-Ziele arbeiten inkrementell: neu gebaut wird nur,\n"
	@printf "wenn Quellen oder Generator-Dateien neuer sind als die HTML-Ausgabe.\n"

build: $(KREISE_TARGET) $(AQUARIUM_TARGET)

all: build

kreise: $(KREISE_TARGET)

$(KREISE_TARGET): $(KREISE_DEPS)
	$(PYTHON) build_lernseite.py

aquarium: $(AQUARIUM_TARGET)

$(AQUARIUM_TARGET): $(AQUARIUM_DEPS)
	$(PYTHON) build_aquarium_lernseite.py

status:
	git status --short --untracked-files=all

publish: build
	git push