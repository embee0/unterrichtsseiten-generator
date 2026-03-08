from build import build_lernseite as builder
from build.site_config import get_site


def main() -> None:
    aquarium = get_site("aquarium")
    builder.build_site(
        source=aquarium.source,
        target=aquarium.target,
        title=aquarium.title,
    )


if __name__ == "__main__":
    main()
