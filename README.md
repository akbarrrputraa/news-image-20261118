[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/akbarrrputraa/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/akbarrrputraa/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# news-image-20261118 — The World in One Image: Wednesday, 18 November 2026

Entry for the [make.fun competition **"Sum up 18 November's world news in one
image"**](https://make.fun/bounty/news-image-20261118) ($250, free entry).

## The image

`entry.png` (1024×1024, PNG) is a newspaper front page summing up Wednesday
18 November 2026:

- **Lead:** Xi Jinping and Vladimir Putin meet in Shenzhen ahead of Donald
  Trump's arrival — a first-ever trilateral summit is set for Thursday
  19 November, with Ukraine, Iran and trade on the agenda.
- **The Gulf war:** US jets strike an Iranian missile site on Qeshm Island;
  Iran answers with drones on a US radar post in Bahrain and on the Ali Al
  Salem air base in Kuwait, and shoots down a US MQ-9 drone near Hormuz.
- **Ukraine:** the Kerch Bridge partly collapses under Ukrainian drone and
  missile strikes, the second day running; Putin is not ready for serious
  peace talks, sources tell the New York Times.
- **Washington:** Democrat Mary Peltola wins Alaska's Senate seat, giving
  Democrats a projected 56–44 majority in the incoming Senate.
- **Israel:** the Knesset elects Matan Kahana speaker, a blow to Netanyahu;
  Trump's Board of Peace accuses Israel and Hamas of failing their
  ceasefire commitments.
- **Health:** the US loses its measles elimination status after 26 years
  (5,400 cases, 10 deaths); the Ebola outbreak in DR Congo more than
  doubles, past 11,000 cases and 5,400 deaths.
- **Disaster & markets:** a Russian military plane crashes in Siberia,
  killing all 19 aboard; Category 5 Cyclone Xavier hits the Northern Cook
  Islands; Nvidia's quarterly revenue doubles year on year.
- **Also:** COP31 in Antalya enters its decisive phase; the World Court is
  to rule on the Myanmar genocide case; Cambridge picks "Human" as Word of
  the Year.

## How it works

`poster.html` is the front page's source (HTML + CSS, rendered at exactly
1024×1024). `main.py` (Python 3.13, standard library only, no network)
copies the rendered `entry.png` to `/output/entry.png`, byte for byte, so
both grading runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
