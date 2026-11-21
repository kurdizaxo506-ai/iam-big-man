# V25 — Browser QA attempt and verified checks

## Source
Started from IAM_BIG_MAN_QUALITY_FIX_V24.zip, with no changes to production HTML/CSS/JS.

## Verified
- ZIP CRC passed (204 source files).
- `python verify_project.py` PASS: 62 HTML files, 20 templates, 20 demos; relative links, local photos, unique IDs and embedded configuration.
- JavaScript syntax checked using Node for each template script.

## Browser QA limitation
- Chromium 144 and Python Playwright are installed and launch successfully.
- Both localhost HTTP navigation and file:// navigation fail with `net::ERR_BLOCKED_BY_ADMINISTRATOR` in this execution environment.
- Therefore **zero pages were visually or interactively verified**. This is an environment restriction, not evidence that the website is broken.
- No Lighthouse scores or end-to-end Formspree delivery tests were obtained.

## How to test on your own machine
1. Extract ZIP to a directory.
2. Run `python -m http.server 8765` inside the extracted directory.
3. Visit http://localhost:8765/index.html in Chrome.
4. Test Website Shop and each of the 20 demos, plus each template under templates/<slug>/index.html.
5. Inspect widths 320, 390, 768, 1440 px; test menu, filters, inquiry copy, and mailto.
6. Run Lighthouse on a deployed HTTPS site for measured scores.

## External services
The main Formspree form requires a real submission to verify delivery. Demo template forms use mailto, not server submission. Payment and booking backends are not included.
