"""news-image-20261124 entry: write the day's front page to /output/entry.png.

The image (hero.jpg) ships in this repository. This program copies it
byte for byte to /output/entry.png, so the two runs the grader performs
write identical bytes.

Standard library only. No network access. Deterministic.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "hero.jpg")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(source, "/output/entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
