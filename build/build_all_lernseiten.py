from build import render_lernseite as builder
from build.site_config import get_all_sites


def main() -> None:
    for site in get_all_sites():
        builder.build_site(
            source=site.source,
            target=site.target,
            title=site.title,
            aliases=site.aliases,
        )


if __name__ == "__main__":
    main()
