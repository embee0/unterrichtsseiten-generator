import argparse

from build import render_lernseite as builder
from build.site_config import get_all_sites, get_site, get_site_names


def build_named_site(name: str) -> None:
    site = get_site(name)
    builder.build_site(
        source=site.source,
        target=site.target,
        title=site.title,
        aliases=site.aliases,
    )


def build_all_sites() -> None:
    for site in get_all_sites():
        builder.build_site(
            source=site.source,
            target=site.target,
            title=site.title,
            aliases=site.aliases,
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Baut eine oder alle Lernseiten aus der zentralen Themenkonfiguration."
    )
    parser.add_argument(
        "site",
        nargs="?",
        choices=get_site_names(),
        help="Name des Themas aus build/site_config.py",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Alle eingetragenen Lernseiten bauen",
    )
    args = parser.parse_args()

    if args.all and args.site is not None:
        parser.error("Bitte entweder einen Themennamen oder --all verwenden.")

    if not args.all and args.site is None:
        parser.error("Bitte einen Themennamen angeben oder --all verwenden.")

    return args


def main() -> None:
    args = parse_args()
    if args.all:
        build_all_sites()
        return

    build_named_site(args.site)


if __name__ == "__main__":
    main()