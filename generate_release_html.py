"""Generate the latest.html release information in installation"""

from pathlib import Path

from tools.releases import fetch_release_info
from tools.templating import generate_html

# Constants
THIS_DIR = Path(__file__).parent
TEMPLATE_PATH = THIS_DIR / "source" / "_templates"
RELEASE = "latest"


def main():
    # Generate installation/latest.html
    release_info = fetch_release_info(RELEASE)
    header = (
        "<!-- This file is generated from the installation-latest.html template -->"
    )
    target_path = THIS_DIR / "source" / "installation" / "latest.html"
    generate_html(
        template_path=(TEMPLATE_PATH / "installation-latest.html"),
        target_path=target_path,
        context=dict(release_info=release_info, header=header),
    )
    print(
        f"Generated {target_path} with information from release {release_info.version}"
    )


if __name__ == "__main__":
    main()
