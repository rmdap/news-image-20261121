# AGENT.md — The World in One Day, 21 November 2026 (v2 rebuild)

## How this entry was built

1. **Research** (fresh agent session started after the competition opened,
   2026-11-21T00:00:00Z): web search across Reuters, AP, BBC, ATP Tour,
   ESA, IANS, the New Straits Times and others. Every story was date-checked
   against its own source — aggregator "day" pages re-surface earlier items,
   so items first reported on 20 November or earlier (Hormuz $64m insurance,
   879,000 AI chips for China, the Rubin dwarf-planet candidate, the
   Palisades verdict, the PT RAPP licence) were caught and excluded.
   Full notes, including the excluded list, are in `news-2026-11-21-v2.md`
   (kept in the builder's workspace, not in this repository).
2. **Timing honesty**: v1 was researched ~03:00–04:00 UTC on Saturday
   21 Nov, only ~3 hours into the news day (31 verified stories, most of
   the day's events still DUE). This v2 rebuild was researched after the
   21 Nov UTC day ended (Sun 22 Nov ~01:00 UTC), so every DUE item is now
   resolved with its actual outcome: BepiColombo's burn SUCCEEDED, Alcaraz
   and Zverev won their ATP semi-finals, Verstappen inherited pole in Las
   Vegas, all seven Premier League games have results, India reached
   486/4 in Wellington, and COP31 still had no deal — talks ran into
   Sunday. The verified count is **54 stories** (v1's 31, updated, + 23
   new). Events not yet happened at research time (F1 race, ATP final,
   COP31 approval session, Rafah reopening) are listed as due in the
   footer, never claimed as done.
3. **Image**: drawn by a fresh Python/PIL generator written in the same
   session (`gen-21nov-v2.py`, a rebuild of the v1 generator): front-page
   newspaper style, 1024×1024 PNG: masthead dated "21 November 2026",
   3 hero cards + 10 small illustrated cards (4 new scenes: the Sinaloa
   arrest, the Bahrain strike, the IEU-CEPA signing, the Banda Sea quake),
   39 briefs in three columns, and a DATE CHECK footer. Seven small-card
   bodies and one headline that wrapped past their line limits were spotted
   by a line-count check and shortened, and a "1.5°C" label overlapping the
   COP31 sun was moved, before the final render.
4. **Program**: `main.py` (stdlib only) copies the bundled `entry.png` to
   `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Two runs to different
   output directories produce byte-identical files (verified by sha256).

## Reproduce

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out1/entry.png out2/entry.png   # identical
```
