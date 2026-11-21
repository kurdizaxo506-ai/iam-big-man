# IAM BIG MAN V21 — Functional contact QA

## Changes
- All 20 editable templates: contact form now clearly says that opening an e-mail application is **not sending** a message.
- Added “Copier ma demande” fallback button, with status feedback for accessibility.
- Browser titles say “Démonstration IAM BIG MAN”, not “Site officiel”.
- Embedded offline configurations synchronized with each template config.json at build time.
- Main studio Formspree form was **not** changed. The owner has shown a successful test notification in Gmail; this does not verify all future submissions.

## Test on Android / Acode
1. Extract the ZIP in full, keeping assets/, demos/, templates/.
2. Open index.html, then templates/restaurant/index.html in Acode Preview.
3. In Contact, fill name, valid e-mail, message (10+ characters), and tick consent.
4. Tap “Copier ma demande”. Check the confirmation and paste into a note.
5. Tap “Ouvrir mon application e-mail”. Verify an e-mail draft opens with recipient iambigman0122@gmail.com; **you must tap Send yourself**.
6. Repeat for a second template and test menu, images, and navigation.
7. Open the studio home page and test the Formspree contact form with a harmless test message, then check inbox and spam.

## Remaining before client launch
- Real customer details, privacy/legal terms, genuine customer imagery, and feature-specific backend services must be supplied per client.
- Test all 20 templates visually on actual devices.
- Payment and bookings are not implemented.
