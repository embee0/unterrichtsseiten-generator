from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SiteConfig:
    name: str
    source: Path
    target: Path
    title: str
    aliases: tuple[Path, ...] = ()


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def make_site(
    name: str, title: str, *, aliases: tuple[Path, ...] = ()
) -> SiteConfig:
    theme_dir = PROJECT_ROOT / "themen" / name
    dist_dir = PROJECT_ROOT / "dist"
    return SiteConfig(
        name=name,
        source=theme_dir / f"LERNSEITE.{name}.md",
        target=dist_dir / f"{name}-lernseite.html",
        title=title,
        aliases=aliases,
    )

SITES: dict[str, SiteConfig] = {
    "kreise": make_site(
        "kreise",
        title="OOP mit py5 – Lernseite",
        aliases=(PROJECT_ROOT / "dist" / "livecoding-doku.html",),
    ),
    "aquarium": make_site(
        "aquarium",
        title="Aquarium mit OOP in py5",
    ),
    "drohnenangriff": make_site(
        "drohnenangriff",
        title="Drohnenangriff mit OOP in py5",
    ),
}


def get_site(name: str) -> SiteConfig:
    return SITES[name]


def get_all_sites() -> list[SiteConfig]:
    return list(SITES.values())


def get_site_names() -> list[str]:
    return list(SITES.keys())
