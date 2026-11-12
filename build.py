#!/usr/bin/env python3
"""Generate the Monokai Pro Glass themes for Zed and Rex.

    python3 build.py

Outputs:
    zed/monokai-pro-glass.json           Zed theme family (Octagon + Light)
    rex/Monokai Pro Octagon Glass        Ghostty-format theme files, which
    rex/Monokai Pro Light Glass          Rex imports as custom themes
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent

# Monokai Pro filter palettes. dark1/dark2 step away from the background
# (darker for Octagon, greyer for Light); dim1..dim5 fade from text to background.
VARIANTS = {
    "Octagon": dict(
        appearance="dark",
        bg="#282a3a", dark1="#1e1f2b", dark2="#161821",
        fg="#eaf2f1",
        dim1="#b2b9bd", dim2="#888d94", dim3="#696d77", dim4="#535763", dim5="#3a3d4b",
        red="#ff657a", orange="#ff9b5e", yellow="#ffd76d",
        green="#bad761", cyan="#9cd1bb", purple="#c39ac9",
        # Glass tint: the window colour that sits over the blurred desktop.
        glass="#161821", glass_alpha="cc",
        comment="dim3",
    ),
    "Light": dict(
        appearance="light",
        bg="#faf4f2", dark1="#ede7e5", dark2="#d3cdcc",
        fg="#29242a",
        dim1="#706b6e", dim2="#918c8e", dim3="#a59fa0", dim4="#bfb9ba", dim5="#d3cdcc",
        red="#e14775", orange="#e16032", yellow="#cc7a0a",
        green="#269d69", cyan="#1c8ca8", purple="#7058be",
        glass="#faf4f2", glass_alpha="d9",
        # dim3 washes out over a blurred backdrop, so comments go one step darker.
        comment="dim2",
    ),
}


def zed_theme(name, p):
    def a(key, alpha):
        return p[key] + alpha

    clear = p["glass"] + "00"
    glass = p["glass"] + p["glass_alpha"]
    # Popovers and menus are not blurred by Zed, so they stay opaque.
    solid = p["dark1"] if p["appearance"] == "dark" else p["bg"]
    border = a("dim4", "55")
    comment = p[p["comment"]]

    style = {
        "background.appearance": "blurred",
        "background": glass,
        "surface.background": clear,
        "elevated_surface.background": solid,
        "border": border,
        "border.variant": a("dim4", "33"),
        "border.focused": a("yellow", "aa"),
        "border.selected": a("yellow", "aa"),
        "border.transparent": clear,
        "border.disabled": a("dim4", "33"),
        "element.background": a("dim3", "33"),
        "element.hover": a("dim3", "4d"),
        "element.active": a("dim3", "66"),
        "element.selected": a("dim3", "59"),
        "element.disabled": a("dim3", "1a"),
        "drop_target.background": a("yellow", "33"),
        "ghost_element.background": clear,
        "ghost_element.hover": a("dim3", "33"),
        "ghost_element.active": a("dim3", "59"),
        "ghost_element.selected": a("dim3", "40"),
        "ghost_element.disabled": clear,
        "text": p["fg"],
        "text.muted": p["dim1"],
        "text.placeholder": p["dim3"],
        "text.disabled": p["dim3"],
        "text.accent": p["yellow"],
        "icon": p["fg"],
        "icon.muted": p["dim2"],
        "icon.disabled": p["dim3"],
        "icon.placeholder": p["dim3"],
        "icon.accent": p["yellow"],
        # Zed paints `background` only behind the workspace body, so the title
        # and status bars need the tint themselves to match it.
        "status_bar.background": glass,
        "title_bar.background": glass,
        "title_bar.inactive_background": glass,
        "toolbar.background": clear,
        "tab_bar.background": clear,
        "tab.inactive_background": clear,
        "tab.active_background": a("dim3", "33"),
        "search.match_background": a("yellow", "44"),
        "search.active_match_background": a("orange", "66"),
        "panel.background": clear,
        "panel.focused_border": a("yellow", "aa"),
        "pane.focused_border": a("dim4", "55"),
        "pane_group.border": border,
        "scrollbar.thumb.background": a("dim3", "55"),
        "scrollbar.thumb.hover_background": a("dim3", "99"),
        "scrollbar.thumb.border": clear,
        "scrollbar.track.background": clear,
        "scrollbar.track.border": clear,
        "editor.foreground": p["fg"],
        "editor.background": clear,
        "editor.gutter.background": clear,
        "editor.subheader.background": a("dim3", "1f"),
        "editor.active_line.background": a("dim3", "1f"),
        "editor.highlighted_line.background": a("dim3", "33"),
        "editor.line_number": p["dim4"],
        "editor.active_line_number": p["dim1"],
        "editor.invisible": p["dim4"],
        "editor.wrap_guide": a("dim4", "33"),
        "editor.active_wrap_guide": a("dim4", "66"),
        "editor.indent_guide": a("dim4", "40"),
        "editor.indent_guide_active": a("dim3", "99"),
        "editor.document_highlight.read_background": a("dim3", "40"),
        "editor.document_highlight.write_background": a("dim3", "59"),
        "editor.document_highlight.bracket_background": a("dim2", "4d"),
        "terminal.background": clear,
        "terminal.foreground": p["fg"],
        "terminal.bright_foreground": p["fg"],
        "terminal.dim_foreground": p["dim2"],
        "link_text.hover": p["cyan"],
        "conflict": p["orange"],
        "conflict.background": a("orange", "26"),
        "conflict.border": a("orange", "80"),
        "created": p["green"],
        "created.background": a("green", "26"),
        "created.border": a("green", "80"),
        "deleted": p["red"],
        "deleted.background": a("red", "26"),
        "deleted.border": a("red", "80"),
        "error": p["red"],
        "error.background": solid,
        "error.border": a("red", "80"),
        "hidden": p["dim3"],
        "hidden.background": clear,
        "hidden.border": border,
        "hint": p["dim2"],
        "hint.background": solid,
        "hint.border": border,
        "ignored": p["dim3"],
        "ignored.background": clear,
        "ignored.border": border,
        "info": p["cyan"],
        "info.background": solid,
        "info.border": a("cyan", "80"),
        "modified": p["orange"],
        "modified.background": a("orange", "26"),
        "modified.border": a("orange", "80"),
        "predictive": p["dim3"],
        "predictive.background": clear,
        "predictive.border": border,
        "renamed": p["cyan"],
        "renamed.background": a("cyan", "26"),
        "renamed.border": a("cyan", "80"),
        "success": p["green"],
        "success.background": solid,
        "success.border": a("green", "80"),
        "unreachable": p["dim2"],
        "unreachable.background": clear,
        "unreachable.border": border,
        "warning": p["yellow"],
        "warning.background": solid,
        "warning.border": a("yellow", "80"),
        "version_control.added": p["green"],
        "version_control.modified": p["orange"],
        "version_control.deleted": p["red"],
        "players": [
            {"cursor": p[c], "background": p[c], "selection": a(c, "40")}
            for c in ("yellow", "cyan", "purple", "green", "orange", "red")
        ],
    }
    # The local cursor keeps the foreground colour, and selections stay neutral.
    style["players"][0] = {
        "cursor": p["fg"],
        "background": p["yellow"],
        "selection": a("dim2", "4d"),
    }
    style.update(
        {f"terminal.ansi.{k}": v for k, v in zip(ANSI_NAMES, ansi(p))}
    )

    def s(color, italic=False, bold=False):
        return {
            "color": color,
            "font_style": "italic" if italic else None,
            "font_weight": 700 if bold else None,
        }

    style["syntax"] = {
        "attribute": s(p["cyan"], italic=True),
        "boolean": s(p["purple"]),
        "comment": s(comment, italic=True),
        "comment.doc": s(comment, italic=True),
        "constant": s(p["purple"]),
        "constructor": s(p["cyan"]),
        "embedded": s(p["fg"]),
        "emphasis": s(p["fg"], italic=True),
        "emphasis.strong": s(p["fg"], bold=True),
        "enum": s(p["cyan"]),
        "function": s(p["green"]),
        "function.builtin": s(p["green"]),
        "hint": s(p["dim2"]),
        "keyword": s(p["red"]),
        "label": s(p["orange"]),
        "link_text": s(p["red"]),
        "link_uri": s(p["green"]),
        "namespace": s(p["cyan"]),
        "number": s(p["purple"]),
        "operator": s(p["red"]),
        "predictive": s(p["dim3"], italic=True),
        "preproc": s(p["red"]),
        "primary": s(p["fg"]),
        "property": s(p["fg"]),
        "punctuation": s(p["dim2"]),
        "punctuation.bracket": s(p["dim2"]),
        "punctuation.delimiter": s(p["dim2"]),
        "punctuation.list_marker": s(p["orange"]),
        "punctuation.special": s(p["red"]),
        "selector": s(p["green"]),
        "selector.pseudo": s(p["cyan"]),
        "string": s(p["yellow"]),
        "string.escape": s(p["purple"]),
        "string.regex": s(p["orange"]),
        "string.special": s(p["orange"]),
        "string.special.symbol": s(p["purple"]),
        "tag": s(p["red"]),
        "text.literal": s(p["yellow"]),
        "title": s(p["yellow"], bold=True),
        "type": s(p["cyan"]),
        "type.builtin": s(p["cyan"], italic=True),
        "variable": s(p["fg"]),
        "variable.parameter": s(p["orange"], italic=True),
        "variable.special": s(p["dim1"], italic=True),
        "variant": s(p["cyan"]),
    }
    return {
        "name": f"Monokai Pro {name} Glass",
        "appearance": p["appearance"],
        "style": style,
    }


ANSI_NAMES = [
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "bright_black", "bright_red", "bright_green", "bright_yellow",
    "bright_blue", "bright_magenta", "bright_cyan", "bright_white",
]


def ansi(p):
    """Monokai Pro's terminal mapping: the blue slot carries orange."""
    normal = [p["dim5"], p["red"], p["green"], p["yellow"],
              p["orange"], p["purple"], p["cyan"], p["fg"]]
    return normal + [p["dim3"]] + normal[1:]


def ghostty_theme(p):
    lines = [f"palette = {i}={c}" for i, c in enumerate(ansi(p))]
    lines += [
        f"background = {p['bg']}",
        f"foreground = {p['fg']}",
        f"cursor-color = {p['fg']}",
        f"cursor-text = {p['bg']}",
        f"selection-background = {p['dim4']}",
        f"selection-foreground = {p['fg']}",
    ]
    return "\n".join(lines) + "\n"


def main():
    (ROOT / "zed").mkdir(exist_ok=True)
    (ROOT / "rex").mkdir(exist_ok=True)

    family = {
        "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
        "name": "Monokai Pro Glass",
        "author": "hiroto",
        "themes": [zed_theme(n, p) for n, p in VARIANTS.items()],
    }
    (ROOT / "zed/monokai-pro-glass.json").write_text(json.dumps(family, indent=2) + "\n")

    for name, p in VARIANTS.items():
        (ROOT / f"rex/Monokai Pro {name} Glass").write_text(ghostty_theme(p))


if __name__ == "__main__":
    main()
