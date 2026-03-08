from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SiteConfig:
    name: str
    source: Path
    target: Path
    title: str


PROJECT_ROOT = Path(__file__).resolve().parent.parent

SITES: dict[str, SiteConfig] = {
    "kreise": SiteConfig(
        name="kreise",
        source=PROJECT_ROOT / "themen" / "kreise" / "LERNSEITE.kreise.md",
        target=PROJECT_ROOT / "dist" / "kreise-lernseite.html",
        title="OOP mit py5 – Lernseite",
    ),
    "aquarium": SiteConfig(
        name="aquarium",
        source=PROJECT_ROOT / "themen" / "aquarium" / "LERNSEITE.aquarium.md",
        target=PROJECT_ROOT / "dist" / "aquarium-lernseite.html",
        title="Aquarium mit OOP in py5",
    ),
}


def get_site(name: str) -> SiteConfig:
    return SITES[name]


def get_all_sites() -> list[SiteConfig]:
    return list(SITES.values())
