"""Build the shareable website (site/) from the design screens (design/).

Run from the repo root:  python3 tools/build_site.py

What it does to each screen:
- adds a viewport tag (phone screens render at 390px wide, admin pages fit the device)
- makes phone screens fill the screen height so the bottom menu stays put
- adds an "All screens" button to admin and overview pages
"""
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESIGN = ROOT / "design"
TOOLS = ROOT / "tools"
SITE = ROOT / "site"

PILL = (
    '<a href="index.html" id="allscreens" style="position:fixed;right:18px;bottom:18px;z-index:99;'
    "display:flex;align-items:center;min-height:42px;padding:0 16px;background:#172042;color:#fff;"
    "border-radius:21px;font:700 13px 'Plus Jakarta Sans',system-ui,sans-serif;text-decoration:none;"
    'box-shadow:0 8px 20px rgba(23,32,66,.25)">← All screens</a>'
)
WIDE = {"Main", "FlowMap", "XGuide"}


def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    for name in ("index.html", "phone.html", "screens.js"):
        shutil.copy(TOOLS / name, SITE / name)
    shutil.copy(DESIGN / "support.js", SITE / "support.js")

    screens = (TOOLS / "screens.js").read_text()
    phone = set(re.findall(r"\['(\w+)'", screens.split("admin:")[0]))

    count = 0
    for src in sorted(DESIGN.glob("*.dc.html")):
        name = src.name[: -len(".dc.html")]
        text = src.read_text()
        if name in phone:
            viewport = "width=390"
        elif name in WIDE:
            viewport = "width=1440"
        else:
            viewport = "width=device-width, initial-scale=1"
        text = text.replace(
            '<meta charset="utf-8">',
            f'<meta charset="utf-8">\n<meta name="viewport" content="{viewport}">',
            1,
        )
        if name in phone:
            text = re.sub(r"width: 390px; height: \d+px;", "width: 390px; height: 100vh; height: 100dvh;", text, count=1)
        else:
            text = text.replace("</body>", PILL + "\n</body>", 1)
        (SITE / src.name).write_text(text)
        count += 1
    print(f"Built {count} screens into {SITE.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
