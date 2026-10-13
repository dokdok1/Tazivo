# Tazivo

Habit tracker (move, focus, grow). Single-page web app, no backend, 9 languages, installable on iPhone/Android as a home-screen app.

## Run it locally
```
python3 build.py          # builds index.html from src/
python3 -m http.server 8000
```
Open http://localhost:8000

## Put it online with GitHub Pages
1. Push this folder to a GitHub repo (branch `main`).
2. Repo, Settings, Pages, Build and deployment: Source = "Deploy from a branch", Branch = `main`, folder = `/ (root)`, Save.
3. After about a minute the site is live at `https://<your-username>.github.io/<repo-name>/`.
4. On iPhone: open the link in Safari, Share, "Add to Home Screen".

Note: GitHub Pages on the free plan needs a public repo, which makes the source readable by anyone. For a private repo use Cloudflare Pages or Netlify (both can deploy a private GitHub repo for free).

## Edit
- `src/head.html` styles and markup, `src/i18n.js` all translations, `src/app.js` logic and pricing (`PRICES`, `FREE_LIMIT`).
- Run `python3 build.py` after any edit, then commit `index.html` too.
- When you ship a new version, bump `CACHE` in `sw.js` so phones pick it up.

## What is not real yet
The lifetime unlock button is a demo (no payment). Real payments, push reminders, widgets and Apple Watch need a native iOS app (StoreKit, local notifications).

Data is stored in the browser (localStorage) on each device. Use Settings, Your data to back up.
