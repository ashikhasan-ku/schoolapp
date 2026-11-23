# School app concept

A clickable concept for a connected school app: a parent app, a staff app and an admin panel. Every screen uses fictional sample data.

## Folders

| Folder | What it holds |
|---|---|
| `site/` | The website people open. Netlify publishes this folder. |
| `design/` | The source screens (one `.dc.html` file per screen) and `canvas.json`, the board layout used in the design canvas. |
| `tools/` | The start page, the phone-frame viewer, the screen list and the build script. |

## Making a change

1. Edit the screen in `design/`, or the start page and screen list in `tools/`.
2. Run `python3 tools/build_site.py` to rebuild `site/`.
3. Commit and push. Netlify publishes the new version within about a minute.

## Screens

- **Parent app (22):** sign in, home, emergency alert, messages, chat, calendar, pay fees, payment status, fees, services, attendance, homework, results, routine, meals, notices, safe pickup, leave, feedback, bus, meetings, settings.
- **Staff app (10):** sign in, today, attendance, messages, homework, marks, leave, class moments, meeting slots, bus trip (drivers and attendants).
- **Admin panel (18):** sign in, dashboard, emergency alert, communication, notices, students and families, attendance, safe pickup, results, routine and calendar, events, meals, fee collection, fee setup, transport, feedback, approvals, roles and access.
- **Overview (3):** system overview, how every feature connects, design rules.
