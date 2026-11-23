"""Copy the front-page image to the output directory.

The entry image (entry.png) sits beside this program in the repository.
This program copies it, unchanged, to the file the grader reads:
$MAKEFUN_OUTPUT_DIR/entry.png, or /output/entry.png when that
variable is not set. It writes the same bytes on every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"entry image not found: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)


if __name__ == "__main__":
    main()
