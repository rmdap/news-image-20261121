# The World in One Day — 21 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/rmdap/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/rmdap/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

A front-page newspaper image summing up the world's news of **Saturday,
21 November 2026** — the events that happened, or were first reported, on
that day in any time zone. **Version 2** — a rebuild of the v1 entry with
the full day's verified news (54 stories, researched after the 21 November
UTC day ended; v1 had 31, researched only ~3 hours into the day).

## What is on the page

- **BepiColombo reaches Mercury** — ESA confirms orbit insertion at
  19:24 CET after an 8-year journey, only the second mission ever to do so.
- **COP31: no deal on Saturday** — talks in Antalya run into Sunday; a
  new package text goes to a 06:00 GMT approval session, fossil fuels still
  out of the draft.
- **Gaza** — Saturday strikes kill 30+, the heaviest toll in weeks; a
  strike on a World Central Kitchen van killed 3. Rafah is due to reopen
  Sunday or Monday.
- Plus: Mexico captures "El Chapo Isidro" (11 dead in Sinaloa), the ATP
  Finals semi-finals, Verstappen on pole in Las Vegas, the Premier League
  results, Modi's Nitish Setu bridge, the Wellington Test, the Hong Kong
  Open, Iran's strike on a facility in Bahrain, the Banda Sea M6.8 quake,
  and the Indonesia–EU IEU-CEPA signing — with 39 more stories in the
  briefs and a DATE CHECK footer listing what was excluded (all 20 November
  stories and earlier-dated items that roundups re-surfaced).

## How it was built

Researched from Reuters, AP, BBC, ATP Tour, ESA, IANS and the New Straits
Times after the news day ended (Sun 22 Nov 2026 ~01:00 UTC), so every
event v1 had marked DUE is now reported with its actual outcome. Every
story was date-checked against its own source — aggregator "day" pages
re-surface earlier items, so items first reported on 20 November or
earlier were excluded rather than presented as 21 November news. The
image was drawn with a fresh Python/PIL generator (`gen-21nov-v2.py`,
kept outside this repository) and `main.py` copies the bundled `entry.png`
to the output directory. 54 stories were verified; 52 appear on the page
(3 hero cards + 10 small cards + 39 briefs) and the Iran-pause context is
noted in the Bahrain card's text.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024, under 1 MiB)
```

## License

MIT — see `LICENSE`.
