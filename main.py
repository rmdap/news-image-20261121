#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-20261121.

Copies the bundled entry.png (the 21 November 2026 news image, built
for this entry) to $MAKEFUN_OUTPUT_DIR/entry.png (default /output).
Standard library only; no network access; deterministic output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("missing bundled image: %s" % SRC)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Fail loudly instead of silently shipping a bad file: the copy must
    # be a complete PNG of exactly the same size as the bundled image.
    with open(dst, "rb") as fh:
        head = fh.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        raise SystemExit("output is not a PNG: %s" % dst)
    if os.path.getsize(dst) != os.path.getsize(SRC):
        raise SystemExit("output size mismatch after copy: %s" % dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
