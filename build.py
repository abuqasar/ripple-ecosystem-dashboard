"""Rebuild the static site after editing map-source.html (Python 3, no packages)."""
from pathlib import Path
from html import escape

root = Path(__file__).resolve().parent
source = (root / 'map-source.html').read_text(encoding='utf-8')
template = (root / 'page-template.html').read_text(encoding='utf-8')
assert template.count('<!-- MAP_SOURCE -->') == 1
(root / 'index.html').write_text(template.replace('<!-- MAP_SOURCE -->', escape(source, quote=True)), encoding='utf-8')
print('Built index.html')
