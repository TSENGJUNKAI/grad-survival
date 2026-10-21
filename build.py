"""Wrap grad-survival.html (artifact format) into a standalone index.html."""
from pathlib import Path

root = Path(__file__).parent
body = (root / "grad-survival.html").read_text(encoding="utf-8")
body = body.replace('<meta charset="utf-8">\n', "", 1)

page = (
    "<!doctype html>\n"
    '<html lang="zh-Hant">\n'
    "<head>\n"
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    "<style>body{margin:0}</style>\n"
    "</head>\n"
    "<body>\n" + body + "\n</body>\n</html>\n"
)
(root / "index.html").write_text(page, encoding="utf-8")
print("wrote index.html")
