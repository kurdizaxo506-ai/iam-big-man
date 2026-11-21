# IAM BIG MAN V24 — Quality fix

Based on V23. Fixed null-safe DOM setters in 20 template scripts, clipboard fallback cleanup, Escape-to-close navigation, keyboard focus styling, reduced-motion support, and small-screen form styling. Synced embedded offline configuration to each config.json. Added repeatable `verify_project.py`.

## Verified
Static link and image checks, JSON/embedded config consistency, HTML duplicate ids, and JS syntax (where Node is available).

## Not verified / not included
No actual device/browser screenshot audit, Lighthouse score, third-party Formspree end-to-end test, payments or real booking backend. The 20 templates remain portfolio demonstrations, not fully custom production websites.

## Acode
Extract all files to a NEW folder; open `index.html` or `templates/restaurant/index.html`. Keep `assets`, `demos`, and `templates` alongside index.html.
