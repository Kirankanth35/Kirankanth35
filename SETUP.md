# Publishing this profile README

Everything is built and verified. You just need to push it.

## 1. Create the profile repo

Your profile README lives in a repo named **exactly** your username.

On github.com → **New repository** → name it `Kirankanth35` → **Public** →
do **not** initialise with a README (this folder has one) → Create.

> You already have a repo called `Kirankanth35`. If it's the profile repo,
> skip creation and just push into it (step 2). If it has content you want to
> keep, back it up first — the push below replaces `README.md`.

## 2. Push

```bash
cd Kirankanth35-profile     # this folder
git init
git add .
git commit -m "feat: monochrome animated profile README"
git branch -M main
git remote add origin https://github.com/Kirankanth35/Kirankanth35.git
git push -u origin main
```

If the remote already exists and has commits:

```bash
git pull --rebase origin main   # then resolve, then push
git push -u origin main
```

## 3. Check it

Open <https://github.com/Kirankanth35>. The README renders at the top of your
profile. Toggle your GitHub theme (Settings → Appearance) to see the light and
dark variants switch.

---

## What's here

| File | Purpose |
|---|---|
| `README.md` | Layout — one `<picture>` per visual, light/dark srcset |
| `assets/*.svg` | 17 visuals (light) |
| `assets/dark/*.svg` | Same 17 (dark srcset targets) |
| `build_assets.py` | Regenerates every SVG — edit content here, not in the SVGs |

## Editing later

Change the text in `build_assets.py`, then:

```bash
python3 build_assets.py
git add assets && git commit -m "chore: update profile content" && git push
```

Content lives in these functions: `header()`, `whoami()`, `PROJECTS` (list),
`experience()`, `stack()`, `timeline()`, `github_stats()`, `telemetry()`,
`now()`, `footer()`.

## Design notes

- **Monochrome by design.** Colour comes only from CSS variables that flip on
  `prefers-color-scheme`. No hardcoded hex in the artwork.
- **Animation is pure CSS keyframes inside each SVG.** GitHub strips `<script>`
  and external CSS from READMEs but does run SVG animations via `<img>`.
- **Reduced-motion safe.** Every file has a
  `@media (prefers-reduced-motion: reduce)` block that freezes the final state.
- **The contribution graph** is the one external dependency
  (github-readme-activity-graph). If it ever breaks, delete that one
  `<picture>` block — everything else is self-hosted in your repo.

## Accuracy note

Stats were pulled live from the GitHub API when this was built: 18 public
repos, 2 stars, Python/HTML/Java language split, account created Oct 2021.
The counters in `telemetry.svg` and `github-stats.svg` are **static text** —
they won't self-update. Re-run `build_assets.py` after editing the numbers when
they drift.
