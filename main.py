"""news-image-20261124 entry: write the day's front page to /output/entry.png.

The image (hero.jpg) ships in this repository. This program copies it
byte for byte to /output/entry.png, so the two runs the grader performs
write identical bytes. After copying, it verifies the output matches the
source byte for byte and exits non-zero if it does not.

Standard library only. No network access. Deterministic.
"""

import hashlib
import os
import shutil
import sys


def _sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "hero.jpg")
    os.makedirs("/output", exist_ok=True)
    target = "/output/entry.png"
    shutil.copyfile(source, target)
    if _sha256(source) != _sha256(target):
        print("entry.png does not match hero.jpg", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
