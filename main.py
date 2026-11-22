#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-20261121 (v2 rebuild).

Copies the bundled entry.png (the 21 November 2026 news image, rebuilt
with the full day's verified news) to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output). Standard library only; no network access. Before
copying it validates the bundled file (PNG magic, IHDR dimensions,
1 MiB cap); two runs write byte-identical files.
"""
import os
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def png_dimensions(path):
    """Return (width, height) read from a PNG file's IHDR chunk."""
    with open(path, "rb") as fh:
        header = fh.read(33)
    if header[:8] != PNG_MAGIC:
        raise SystemExit("not a PNG file: %s" % path)
    if header[12:16] != b"IHDR":
        raise SystemExit("PNG has no IHDR chunk: %s" % path)
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    if not SRC.is_file():
        raise SystemExit("missing bundled image: %s" % SRC)
    if SRC.stat().st_size > MAX_BYTES:
        raise SystemExit("bundled image over 1 MiB: %s" % SRC)
    width, height = png_dimensions(SRC)
    if (width, height) != (1024, 1024):
        raise SystemExit("bundled image is %dx%d, want 1024x1024"
                         % (width, height))
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    data = SRC.read_bytes()
    dst.write_bytes(data)
    if dst.stat().st_size != len(data):
        raise SystemExit("output size mismatch after copy: %s" % dst)
    if dst.read_bytes()[:8] != PNG_MAGIC:
        raise SystemExit("output is not a PNG: %s" % dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
