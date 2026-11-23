# Front-Page Summary of 24 Nov 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/pakun1/news-image-20261124-entry/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/pakun1/news-image-20261124-entry/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A newspaper front page that sums up the world's news of Tuesday,
24 November 2026, in one image. Built for the make.fun bounty
[news-image-20261124](https://make.fun/bounty/news-image-20261124).

## The day in six stories

- **Sport — Geneva:** the World Chess Championship opens. Defending
  champion Gukesh of India, 20, faces challenger Javokhir Sindarov
  of Uzbekistan, 20, in Game 1 — the youngest title match ever.
  Fourteen games, a $2.5 million prize fund; Sindarov has White.
- **United States — Iowa:** President Trump orders the Army to halt
  the planned detonation of unstable lead azide at the Iowa Army
  Ammunition Plant. The blast was due on 24 November.
- **Tech — Washington:** the U.S. adds Megaspeed, a chip firm linked
  to Nvidia, to its Entity List, the latest twist in the scandal
  around the chipmaker. Trump urges Nvidia to bring back Jensen Huang.
- **Conflict — Kyiv:** a Russian drone strike in Ukraine's Kyiv
  region leaves several people missing, President Zelenskyy says.
- **Asia — Nepal:** the first Saryu-Kamala Express, flagged off by
  Modi and Nepal's PM Shah, rolls into Janakpur Dham, opening a
  direct Ayodhya–Janakpur rail link.
- **Justice — The Hague:** Tajikistan begins withdrawing from the
  International Criminal Court, the fourth country to quit since
  the U.S. push to dismantle the tribunal.

## How it was made

The front page was drawn with PIL from the day's reporting: a
masthead, a date line, one lead panel and five more panels, each
with a short headline and two to three lines of text. Every story
was checked against real reporting for its date before it went in.

## Files

- `entry.png` — the front page, 1024×1024 PNG.
- `main.py` — copies `entry.png` to `/output/entry.png`
  (or `$MAKEFUN_OUTPUT_DIR/entry.png`). Deterministic: two runs
  write the same bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT. See `LICENSE`.
