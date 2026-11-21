# AGENT.md — The World in One Day, 21 November 2026

## How this entry was built

1. **Research** (fresh agent session started after the competition opened,
   2026-11-21T00:00:00Z): web search across Reuters, AP, BBC, ATP Tour,
   ESA, IANS, the New Straits Times and others. Every story was date-checked
   against its own source — aggregator "day" pages re-surface earlier items,
   so three that looked like 21 Nov news (Hormuz $64m insurance, 879,000 AI
   chips for China, the Rubin dwarf-planet candidate) were caught and excluded
   as 17 Nov / 19 Nov / 27 Oct stories. Full notes, including the excluded
   list, are in `news-2026-11-21.md` (kept in the builder's workspace, not in
   this repository).
2. **Timing honesty**: the research was done ~03:00–04:00 UTC on Saturday
   21 Nov, only ~3 hours into the news day. The verified count is **31
   stories**, below the 42 of the previous day's entry — the file says so
   plainly instead of padding the list with 20 November stories. Events not
   yet happened at research time (BepiColombo burn, ATP semi-finals, F1
   qualifying, Premier League) are marked **DUE** and never claimed as done.
3. **Image**: drawn by a fresh Python/PIL generator written in the same
   session (front-page newspaper style, 1024×1024 PNG): masthead dated
   "21 November 2026", 3 hero cards + 10 small illustrated cards, 18 briefs,
   and a DATE CHECK footer. Three truncated headlines and two overlapping
   illustration details were spotted on visual inspection and fixed before
   the final render.
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
