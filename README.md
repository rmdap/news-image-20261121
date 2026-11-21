# The World in One Day — 21 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/rmdap/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/rmdap/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

A front-page newspaper image summing up the world's news of **Saturday,
21 November 2026** — the events that happened, or were first reported, on
that day in any time zone.

## What is on the page

- **COP31 in overtime** — talks in Antalya pass the Friday deadline with no
  deal; the draft drops all mention of phasing out fossil fuels and the
  $120bn adaptation-finance figure.
- **Gaza** — Saturday strikes kill ~30, the heaviest toll in weeks; Rafah is
  due to reopen on Sunday.
- **BepiColombo** — the ESA/JAXA probe fires for Mercury orbit insertion at
  19:24 CET after an 8-year journey.
- Plus: Modi's Nitish Setu bridge, the ATP Finals semi-finals, F1 Las Vegas
  qualifying, the Premier League, Cyclone Akvan's rains, the Wellington Test,
  the Hong Kong Open, Malaysia–China ties, an Australian cocaine-ring bust,
  and two Indonesian earthquakes — with 18 more stories in the briefs and a
  DATE CHECK footer listing what was excluded (all 20 November stories and
  earlier-dated items that roundups re-surfaced).

## How it was built

Researched from Reuters, AP, BBC, ATP Tour, ESA, IANS and the New Straits
Times on the morning of 21 November 2026 (mid-day UTC — only ~3 hours into
the news day, so the verified count is 31 stories, honestly noted in the
research file rather than padded with 20 November stories). The image was
drawn with a fresh Python/PIL generator (`gen-21nov-v1.py`, kept outside this
repository) and `main.py` copies the bundled `entry.png` to the output
directory.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024, under 1 MiB)
```

## License

MIT — see `LICENSE`.
