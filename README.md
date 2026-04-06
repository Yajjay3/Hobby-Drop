# Hobby Drop

A free Chrome extension that delivers a fascinating daily fact about your favorite hobby or interest — including what happened **on this day** in history.

## Project Structure

```
DailyObsessionDrop/
├── extension/           # Chrome extension (Manifest V3)
│   ├── manifest.json
│   ├── popup.html       # Extension popup UI
│   ├── popup.css        # Popup styles
│   ├── popup.js         # Popup controller
│   ├── facts-engine.js  # Fact fetching (Wikipedia APIs)
│   ├── background.js    # Service worker (daily alarm + notifications)
│   └── icons/           # Extension icons (16, 48, 128)
├── website/             # One-page landing site
│   └── index.html
└── tools/               # Dev utilities
    └── generate_icons.py
```

## How It Works

1. User enters their hobby/interest (e.g. "Golf", "Painting", "Space")
2. The extension fetches facts using two strategies:
   - **On This Day** — Queries the Wikimedia "on this day" API for today's date, filters events that match the hobby
   - **Did You Know** — Falls back to a Wikipedia article search and pulls an extract
3. Facts are cached once per day
4. A daily alarm sends a Chrome notification reminding the user to check their fact

## Install for Development

1. Open `chrome://extensions/` in Chrome
2. Enable **Developer mode** (top right)
3. Click **Load unpacked** → select the `extension/` folder
4. Click the extension icon in the toolbar and enter your hobby

## APIs Used

- [Wikimedia REST API](https://api.wikimedia.org/) — "On This Day" events
- [Wikipedia Action API](https://www.mediawiki.org/wiki/API:Main_page) — Article search & extracts

No API keys required. All requests are unauthenticated and free.

## Free Edition

This is the free version. Users get one daily fact with the option to refresh for a new one.
