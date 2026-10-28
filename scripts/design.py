"""Design tokens and small SVG helpers shared by every generated asset."""
from xml.sax.saxutils import escape

# "Data Intelligence Lab": charcoal base, midnight-purple panels, one violet accent.
BG = "#0d0b14"
PANEL = "#151226"
PANEL_HI = "#1b1733"
BORDER = "#2a2347"
VIOLET = "#a371f7"
VIOLET_DEEP = "#7c3aed"
TEXT = "#e8e4f3"
MUTED = "#8f89a8"
DIM = "#5d5778"

SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"


def esc(value) -> str:
    """Escape any dynamic text before it goes into SVG."""
    return escape(str(value), {'"': "&quot;"})


def svg_open(w, h, title, desc, extra_css=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" role="img" aria-labelledby="t d">\n'
        f'<title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc>\n'
        f"<style>text{{font-family:{SANS}}}.m{{font-family:{MONO}}}{extra_css}</style>\n"
    )
