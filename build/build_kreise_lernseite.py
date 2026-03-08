from build import render_lernseite as builder
from build.site_config import get_site


def main() -> None:
    kreise = get_site("kreise")
    builder.build_site(
        source=kreise.source,
        target=kreise.target,
        title=kreise.title,
        aliases=kreise.aliases,
    )


if __name__ == "__main__":
    main()
