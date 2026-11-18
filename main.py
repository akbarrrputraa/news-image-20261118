# A working news-image-daily entry (Python 3.13, standard library only).
#
# The image is entry.png beside this file: a newspaper front page summing up
# Wednesday 18 November 2026, rendered from poster.html (the page's own
# source, kept in this repository) and checked by eye. The program copies it
# to /output/entry.png, byte for byte, so the two runs the grader does write
# the same bytes. No network, no dependencies, no randomness.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
