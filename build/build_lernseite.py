import base64
import html
import json
import re
from os.path import relpath
from pathlib import Path
from urllib.parse import quote

from build.site_config import get_site

BUILD_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = BUILD_ROOT.parent
ROOT = PROJECT_ROOT
DEFAULT_SITE = get_site("kreise")
SOURCE = DEFAULT_SITE.source
TARGET = DEFAULT_SITE.target
PAGE_TITLE = DEFAULT_SITE.title
EDIT_BASE = "https://abav.lugaralgum.com/pyp5js/py5mode/?sketch="
PRESENT_BASE = "https://abav.lugaralgum.com/pyp5js/py5mode/presentation.html?sketch="
MAX_SKETCH_URL_LENGTH = 8000

IFRAME_RE = re.compile(r"\{\{IFRAME:\s*([^}]+?)\s*\}\}")
EDIT_RE = re.compile(r"\{\{EDIT:\s*([^}|]+?)(?:\|\s*([^}]+?))?\s*\}\}")
SOLUTION_START_RE = re.compile(r"\{\{SOLUTION:\s*([^}]+?)\s*\}\}")
SOLUTION_END_RE = re.compile(r"\{\{ENDSOLUTION\s*\}\}")
SIZE_RE = re.compile(r"\bsize\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)")
IFRAME_CHROME = 0
PREVIEW_DIR_NAME = "_previews"
SHARED_STYLESHEET_RELATIVE_PATH = Path("assets/lernseite.css")

PYTHON_KEYWORDS = {
    "class",
    "def",
    "global",
    "for",
    "in",
    "if",
    "else",
    "elif",
    "return",
    "while",
}

PY5_NAMES = {
    "size",
    "background",
    "fill",
    "circle",
    "ellipse",
    "triangle",
    "rect",
    "line",
    "stroke",
    "stroke_weight",
    "no_stroke",
    "no_fill",
    "text",
    "text_size",
    "color",
    "sin",
    "random",
    "random_int",
    "range",
    "dist",
    "constrain",
    "width",
    "height",
    "frame_count",
    "mouse_x",
    "mouse_y",
    "TWO_PI",
}

TOKEN_RE = re.compile(
    r"(?P<comment>#.*$)|"
    r"(?P<string>'[^'\\\n]*(?:\\.[^'\\\n]*)*'|\"[^\"\\\n]*(?:\\.[^\"\\\n]*)*\")|"
    r"(?P<number>\b\d+(?:\.\d+)?\b)|"
    r"(?P<name>\b[A-Za-z_][A-Za-z0-9_]*\b)",
    re.MULTILINE,
)


def make_sketch_link(filename: str, *, presentation: bool) -> str:
    code = get_asset_path(filename).read_text(encoding="utf-8")
    normalized = code.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\r\n")
    escaped = quote(normalized, safe="")
    payload = base64.urlsafe_b64encode(escaped.encode("utf-8")).decode("ascii")
    base = PRESENT_BASE if presentation else EDIT_BASE
    return base + payload


def get_asset_path(filename: str) -> Path:
    path = Path(filename)
    if path.is_absolute():
        return path
    return SOURCE.parent / path


def get_target_relative_path(filename: str) -> str:
    asset_path = get_asset_path(filename)
    relative_path = relpath(asset_path, TARGET.parent)
    return Path(relative_path).as_posix()


def get_preview_output_path(filename: str) -> Path:
    asset_path = get_asset_path(filename)
    relative_asset_path = asset_path.relative_to(SOURCE.parent)
    return (
        TARGET.parent
        / PREVIEW_DIR_NAME
        / SOURCE.parent.name
        / relative_asset_path.with_suffix(".html")
    )


def get_preview_relative_path(filename: str) -> str:
    relative_path = relpath(get_preview_output_path(filename), TARGET.parent)
    return Path(relative_path).as_posix()


def sketch_url_is_safe(filename: str, *, presentation: bool) -> bool:
    return (
        len(make_sketch_link(filename, presentation=presentation))
        <= MAX_SKETCH_URL_LENGTH
    )


def render_sketch_fallback(
    filename: str, *, presentation: bool, button_label: str | None = None
) -> str:
    if presentation:
        title = "Vorschau nicht direkt eingebettet"
        text = (
            "Dieser py5-Sketch ist zu lang für die URL-basierte Vorschau. "
            "Die Seite zeigt deshalb hier absichtlich keinen kaputten iframe an."
        )
        resolved_button_label = button_label or "Python-Datei öffnen"
    else:
        title = "Editor-Link ersetzt"
        text = (
            "Dieser Sketch ist zu lang für einen py5-Editorlink mit ?sketch=. "
            "Arbeite stattdessen direkt mit der Python-Datei aus diesem Ordner."
        )
        resolved_button_label = button_label or "Python-Datei öffnen"

    href = quote(get_target_relative_path(filename))
    return (
        '<div class="sketch-fallback">'
        f'<p class="sketch-fallback-title">{html.escape(title)}</p>'
        f"<p>{html.escape(text)}</p>"
        f'<p class="sketch-fallback-link"><a class="button-link" href="{html.escape(href, quote=True)}" target="_blank" rel="noopener noreferrer">{html.escape(resolved_button_label)}</a></p>'
        "</div>"
    )


def get_sketch_dimensions(filename: str) -> tuple[int, int]:
    code = get_asset_path(filename).read_text(encoding="utf-8")
    match = SIZE_RE.search(code)
    if not match:
        return 300, 300
    return int(match.group(1)), int(match.group(2))


def render_preview_page(filename: str) -> str:
    code = get_asset_path(filename).read_text(encoding="utf-8")
    return f"""<!doctype html>
<html lang=\"de\">
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>{html.escape(Path(filename).name)} – Vorschau</title>
    <style>
      html, body {{
        margin: 0;
        padding: 0;
        background: transparent;
        overflow: hidden;
      }}

      #sketch-holder {{
        display: block;
        line-height: 0;
      }}

      canvas {{
        display: block;
      }}
    </style>
    <script src=\"https://cdn.jsdelivr.net/npm/p5@1.0.0/lib/p5.js\"></script>
    <script src=\"https://cdn.jsdelivr.net/pyodide/v0.18.1/full/pyodide.js\"></script>
    <script>
      function checkForSketch() {{
        return {json.dumps(code)};
      }}
    </script>
  </head>
  <body>
    <div id=\"sketch-holder\"></div>
    <script src=\"https://abav.lugaralgum.com/pyp5js/py5mode/target/target_sketch.js\"></script>
  </body>
</html>
"""


def ensure_preview_page(filename: str) -> str:
    preview_output_path = get_preview_output_path(filename)
    preview_output_path.parent.mkdir(parents=True, exist_ok=True)
    preview_output_path.write_text(render_preview_page(filename), encoding="utf-8")
    return get_preview_relative_path(filename)


def inline_format(text: str) -> str:
    placeholders: list[str] = []

    def stash(value: str) -> str:
        placeholders.append(value)
        return f"@@PLACEHOLDER{len(placeholders) - 1}@@"

    text = re.sub(
        r"`([^`]+)`",
        lambda m: stash(f"<code>{html.escape(m.group(1))}</code>"),
        text,
    )
    text = re.sub(
        r"\*\*([^*]+)\*\*",
        lambda m: stash(f"<strong>{html.escape(m.group(1))}</strong>"),
        text,
    )
    text = re.sub(
        r"_([^_]+)_",
        lambda m: stash(f"<em>{html.escape(m.group(1))}</em>"),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: stash(
            f'<a href="{html.escape(m.group(2), quote=True)}">{html.escape(m.group(1))}</a>'
        ),
        text,
    )

    escaped = html.escape(text)
    for index, value in enumerate(placeholders):
        escaped = escaped.replace(f"@@PLACEHOLDER{index}@@", value)
    return escaped


def highlight_python(code: str) -> str:
    parts: list[str] = []
    last_index = 0

    for match in TOKEN_RE.finditer(code):
        start, end = match.span()
        parts.append(html.escape(code[last_index:start]))
        token = match.group(0)

        if match.lastgroup == "comment":
            css_class = "tok-comment"
        elif match.lastgroup == "string":
            css_class = "tok-string"
        elif match.lastgroup == "number":
            css_class = "tok-number"
        else:
            if token in PYTHON_KEYWORDS:
                css_class = "tok-keyword"
            elif token in PY5_NAMES:
                css_class = "tok-builtin"
            elif token == "self":
                css_class = "tok-self"
            else:
                css_class = "tok-name"

        parts.append(f'<span class="{css_class}">{html.escape(token)}</span>')
        last_index = end

    parts.append(html.escape(code[last_index:]))
    highlighted = "".join(parts)
    highlighted = re.sub(
        r'(<span class="tok-keyword">class</span>)(\s+)(<span class="tok-name">[A-Za-z_][A-Za-z0-9_]*</span>)',
        r'\1\2<span class="tok-class">\3</span>',
        highlighted,
    )
    highlighted = re.sub(
        r'(<span class="tok-keyword">def</span>)(\s+)(<span class="tok-name">[A-Za-z_][A-Za-z0-9_]*</span>)',
        r'\1\2<span class="tok-function">\3</span>',
        highlighted,
    )
    return highlighted


def render_code_block(code: str, language: str) -> str:
    language = language.strip().lower()
    rendered = (
        highlight_python(code) if language in {"python", "py"} else html.escape(code)
    )
    css_language = language or "text"
    return (
        f'<div class="code-block"><pre><code class="language-{css_language}">'
        f"{rendered}</code></pre></div>"
    )


def close_lists(parts: list[str], in_ul: bool, in_ol: bool) -> tuple[bool, bool]:
    if in_ul:
        parts.append("</ul>")
        in_ul = False
    if in_ol:
        parts.append("</ol>")
        in_ol = False
    return in_ul, in_ol


def close_section(
    parts: list[str], section_open: bool, in_ul: bool, in_ol: bool
) -> tuple[bool, bool, bool]:
    if section_open:
        in_ul, in_ol = close_lists(parts, in_ul, in_ol)
        parts.append("</section>")
        section_open = False
    return section_open, in_ul, in_ol


def render_iframe(filename: str) -> str:
    url = ensure_preview_page(filename)
    sketch_width, sketch_height = get_sketch_dimensions(filename)
    iframe_width = sketch_width + IFRAME_CHROME
    iframe_height = sketch_height + IFRAME_CHROME
    return (
        '<div class="preview-frame">'
        f'<iframe src="{html.escape(url, quote=True)}" width="{iframe_width}" height="{iframe_height}" loading="lazy"></iframe>'
        "</div>"
    )


def render_edit_link(filename: str, label: str = "Im Editor öffnen") -> str:
    if not sketch_url_is_safe(filename, presentation=False):
        return render_sketch_fallback(filename, presentation=False, button_label=label)

    url = make_sketch_link(filename, presentation=False)
    return (
        '<p class="editor-link">'
        f'<a class="button-link" href="{html.escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{html.escape(label)}</a>'
        "</p>"
    )


def render_margin_note(note_text: str) -> str:
    return f'<aside class="margin-note">{inline_format(note_text)}</aside>'


def render_solution_block(summary_text: str, content_html: str) -> str:
    return (
        '<details class="solution-block">'
        f"<summary>{inline_format(summary_text)}</summary>"
        f'<div class="solution-content">{content_html}</div>'
        "</details>"
    )


def wrap_with_margin_note(content_html: str, note_html: str) -> str:
    return (
        '<div class="note-layout">'
        f'<div class="note-content">{content_html}</div>'
        f"{note_html}"
        "</div>"
    )


def attach_note_to_previous_block(parts: list[str], note_html: str) -> bool:
    if not parts:
        return False

    if parts[-1].startswith("<p>"):
        start_index = len(parts) - 1
        if start_index > 0 and parts[start_index - 1].startswith(("<h2>", "<h3>")):
            start_index -= 1

        content_html = "\n".join(parts[start_index:])
        del parts[start_index:]
        parts.append(wrap_with_margin_note(content_html, note_html))
        return True

    if parts[-1] in {"</ul>", "</ol>"}:
        closing_tag = parts[-1]
        opening_tag = "<ul>" if closing_tag == "</ul>" else "<ol>"

        start_index = len(parts) - 1
        while start_index >= 0 and parts[start_index] != opening_tag:
            start_index -= 1

        if start_index >= 0:
            if start_index > 0 and parts[start_index - 1].startswith("<p>"):
                start_index -= 1
            if start_index > 0 and parts[start_index - 1].startswith(("<h2>", "<h3>")):
                start_index -= 1

            list_html = "\n".join(parts[start_index:])
            del parts[start_index:]
            parts.append(wrap_with_margin_note(list_html, note_html))
            return True

    return False


def render_markdown(lines: list[str]) -> str:
    parts: list[str] = []
    active_parts = parts
    solution_parts: list[str] = []
    solution_summary = ""
    in_code = False
    code_language = ""
    code_lines: list[str] = []
    in_ul = False
    in_ol = False
    section_open = False
    hero_open = False

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        if stripped.startswith("<!-- COPILOT:"):
            continue

        solution_start_match = SOLUTION_START_RE.fullmatch(stripped)
        if solution_start_match:
            in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
            solution_summary = solution_start_match.group(1).strip()
            solution_parts = []
            active_parts = solution_parts
            continue

        if SOLUTION_END_RE.fullmatch(stripped):
            in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
            parts.append(
                render_solution_block(solution_summary, "\n".join(solution_parts))
            )
            solution_parts = []
            solution_summary = ""
            active_parts = parts
            continue

        if in_code:
            if stripped.startswith("```"):
                code = "\n".join(code_lines)
                active_parts.append(render_code_block(code, code_language))
                in_code = False
                code_language = ""
                code_lines = []
            else:
                code_lines.append(line)
            continue

        if stripped.startswith("```"):
            in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
            in_code = True
            code_language = stripped[3:].strip()
            code_lines = []
            continue

        if not stripped:
            in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
            continue

        if stripped == "---":
            in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
            active_parts.append("<hr />")
            continue

        iframe_match = IFRAME_RE.fullmatch(stripped)
        if iframe_match:
            in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
            active_parts.append(render_iframe(iframe_match.group(1).strip()))
            continue

        edit_match = EDIT_RE.fullmatch(stripped)
        if edit_match:
            in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
            filename = edit_match.group(1).strip()
            label = (
                edit_match.group(2).strip()
                if edit_match.group(2)
                else "Im Editor öffnen"
            )
            active_parts.append(render_edit_link(filename, label))
            continue

        if stripped.startswith("# "):
            section_open, in_ul, in_ol = close_section(
                parts, section_open, in_ul, in_ol
            )
            parts.append('<header class="hero">')
            parts.append(f"<h1>{inline_format(stripped[2:].strip())}</h1>")
            hero_open = True
            continue

        if stripped.startswith("## "):
            if hero_open:
                parts.append("</header>")
                hero_open = False
            section_open, in_ul, in_ol = close_section(
                parts, section_open, in_ul, in_ol
            )
            parts.append('<section class="content-section">')
            parts.append(f"<h2>{inline_format(stripped[3:].strip())}</h2>")
            section_open = True
            continue

        if stripped.startswith("### "):
            in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
            active_parts.append(f"<h3>{inline_format(stripped[4:].strip())}</h3>")
            continue

        if stripped.startswith(">"):
            in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
            note_text = stripped[1:].strip()
            note_html = render_margin_note(note_text)
            if not attach_note_to_previous_block(active_parts, note_html):
                active_parts.append(note_html)
            continue

        match_ol = re.match(r"(\d+)\.\s+(.*)", stripped)
        if match_ol:
            if in_ul:
                active_parts.append("</ul>")
                in_ul = False
            if not in_ol:
                active_parts.append("<ol>")
                in_ol = True
            active_parts.append(f"<li>{inline_format(match_ol.group(2))}</li>")
            continue

        if stripped.startswith("- "):
            if in_ol:
                active_parts.append("</ol>")
                in_ol = False
            if not in_ul:
                active_parts.append("<ul>")
                in_ul = True
            active_parts.append(f"<li>{inline_format(stripped[2:])}</li>")
            continue

        in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
        active_parts.append(f"<p>{inline_format(stripped)}</p>")

    if in_code:
        code = "\n".join(code_lines)
        active_parts.append(render_code_block(code, code_language))

    if active_parts is not parts:
        in_ul, in_ol = close_lists(active_parts, in_ul, in_ol)
        parts.append(render_solution_block(solution_summary, "\n".join(solution_parts)))

    if hero_open:
        parts.append("</header>")

    section_open, in_ul, in_ol = close_section(parts, section_open, in_ul, in_ol)
    in_ul, in_ol = close_lists(parts, in_ul, in_ol)
    return "\n".join(parts)


HTML_TEMPLATE = """<!doctype html>
<html lang=\"de\">
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>__TITLE__</title>
    <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet" />
    <style>
      :root {
        --bg: #2d2a2e;
        --bg-deep: #221f22;
        --panel: rgba(45, 42, 46, 0.84);
        --panel-strong: rgba(36, 33, 37, 0.94);
        --panel-soft: rgba(54, 49, 56, 0.84);
        --text: #fcfcfa;
        --muted: #c8c2bf;
        --accent: #ffd866;
        --accent-2: #78dce8;
        --accent-3: #fc9867;
        --accent-4: #a9dc76;
        --accent-5: #ab9df2;
        --border: rgba(255, 255, 255, 0.1);
        --shadow: 0 24px 70px rgba(0, 0, 0, 0.34);
        --code-bg: #2d2a2e;
        --code-line: #403e41;
        --code-text: #fcfcfa;
      }

      * { box-sizing: border-box; }
      html { scroll-behavior: smooth; }
      body {
        margin: 0;
        color: var(--text);
        font-family: "Manrope", "Segoe UI", sans-serif;
        font-variant-numeric: lining-nums proportional-nums;
        font-feature-settings: "lnum" 1, "pnum" 1;
        line-height: 1.72;
        background:
          radial-gradient(circle at 12% 10%, rgba(120, 220, 232, 0.16), transparent 24%),
          radial-gradient(circle at 88% 12%, rgba(252, 152, 103, 0.16), transparent 20%),
          radial-gradient(circle at 50% 120%, rgba(255, 214, 102, 0.12), transparent 24%),
          linear-gradient(180deg, #2d2a2e 0%, #262328 42%, #221f22 100%);
      }

      body::before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        background-image:
          linear-gradient(rgba(255, 255, 255, 0.035) 1px, transparent 1px),
          linear-gradient(90deg, rgba(255, 255, 255, 0.035) 1px, transparent 1px);
        background-size: 38px 38px;
        mask-image: radial-gradient(circle at center, black 42%, transparent 95%);
        opacity: 0.4;
      }

      body::after {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        opacity: 0.08;
        background-image: radial-gradient(rgba(120, 220, 232, 0.45) 0.6px, transparent 0.6px);
        background-size: 14px 14px;
      }

      main {
        position: relative;
        width: min(calc(100% - 2rem), 1040px);
        margin: 0 auto;
        padding: 2rem 0 5rem;
        counter-reset: lesson;
      }

      .hero,
      .content-section {
        position: relative;
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 30px;
        box-shadow: var(--shadow);
        backdrop-filter: blur(14px);
        overflow: visible;
        animation: rise-in 680ms cubic-bezier(.2,.8,.2,1) both;
      }

      .hero::after,
      .content-section::after {
        content: "";
        display: block;
        clear: both;
      }

      .hero {
        padding: 2.7rem;
        margin-bottom: 1.35rem;
        background:
          linear-gradient(160deg, rgba(41, 37, 44, 0.98), rgba(34, 31, 34, 0.94)),
          var(--panel);
      }

      .hero::before {
        content: "";
        position: absolute;
        inset: 1rem;
        border: 1px solid rgba(120, 220, 232, 0.16);
        border-radius: 24px;
        pointer-events: none;
        box-shadow: inset 0 0 0 1px rgba(255, 209, 102, 0.08);
      }

      .hero::after {
        content: "";
        position: absolute;
        right: 2rem;
        top: 1.8rem;
        width: 9rem;
        height: 9rem;
        border-radius: 50%;
        background:
          radial-gradient(circle at 30% 30%, rgba(120, 220, 232, 0.3), transparent 48%),
          radial-gradient(circle at 70% 70%, rgba(255, 209, 102, 0.28), transparent 50%);
        filter: blur(14px);
        opacity: 0.85;
        pointer-events: none;
      }

      .content-section {
        padding: 2rem 2rem 2.1rem;
        margin-top: 1.15rem;
        background:
          linear-gradient(180deg, rgba(49, 44, 52, 0.96), rgba(35, 32, 38, 0.96));
      }

      .content-section:nth-of-type(2n) {
        transform: translateX(0.6rem);
      }

      .content-section:nth-of-type(2n + 1) {
        transform: translateX(-0.35rem);
      }

      h1, h2, h3 {
        margin: 0;
        line-height: 1.05;
        letter-spacing: -0.035em;
        font-family: "Syne", "Manrope", sans-serif;
        font-variant-numeric: lining-nums proportional-nums;
        font-feature-settings: "lnum" 1, "pnum" 1;
      }

      h1 {
        margin-top: 0;
        font-size: clamp(2.8rem, 7vw, 5.2rem);
        max-width: 9ch;
        text-wrap: balance;
      }

      h2 {
        font-size: clamp(1.9rem, 4vw, 2.7rem);
        margin-bottom: 1.1rem;
        padding-top: 0.25rem;
      }

      h3 {
        font-size: 1.28rem;
        color: var(--accent-3);
        margin-top: 1.5rem;
        margin-bottom: 0.45rem;
      }

      p, li {
        color: var(--muted);
        margin: 0.62rem 0;
        font-size: 1.02rem;
        font-variant-numeric: lining-nums proportional-nums;
        font-feature-settings: "lnum" 1, "pnum" 1;
      }

      strong {
        color: var(--text);
      }

      a {
        color: var(--accent-2);
        text-decoration: none;
        border-bottom: 1px solid rgba(120, 220, 232, 0.22);
      }

      a:hover {
        color: var(--accent);
      }

      code {
        font-family: "JetBrains Mono", Menlo, Consolas, monospace;
        color: #f0f7f7;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 8px;
        padding: 0.14rem 0.38rem;
      }

      ul, ol {
        padding-left: 1.4rem;
        margin: 0.55rem 0 0.95rem;
      }

      li::marker {
        color: var(--accent);
      }

      hr {
        border: 0;
        height: 16px;
        margin: 1.25rem 0;
        background:
          radial-gradient(circle at center, rgba(255, 209, 102, 0.85) 0 2px, transparent 3px),
          linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.16), transparent);
        background-repeat: no-repeat;
        background-position: center center;
      }

      .note-layout {
        display: grid;
        grid-template-columns: minmax(0, 1fr) minmax(14rem, 16rem);
        align-items: start;
        gap: 1.4rem;
        margin: 0.7rem 0 1rem;
      }

      .note-content > :first-child {
        margin-top: 0;
      }

      .note-content > :last-child {
        margin-bottom: 0;
      }

      .note-content ul,
      .note-content ol {
        margin-top: 0;
        margin-bottom: 0;
      }

      .margin-note {
        width: 100%;
        margin: 0;
        padding: 1rem 1rem 1rem 1.2rem;
        border-radius: 20px;
        background: linear-gradient(180deg, rgba(34, 31, 37, 0.98), rgba(26, 24, 29, 0.96));
        border: 1px solid rgba(255, 209, 102, 0.22);
        color: #f2efed;
        font-size: 0.96rem;
        line-height: 1.58;
        box-shadow: 0 18px 32px rgba(0, 0, 0, 0.28);
        transform: none;
      }

      .margin-note strong,
      .margin-note code {
        color: #ffd866;
        font-weight: 800;
        letter-spacing: 0.01em;
      }

      .margin-note code {
        background: transparent;
        border: 0;
        border-radius: 0;
        padding: 0;
      }

      .preview-frame {
        display: inline-block;
        width: fit-content;
        max-width: 100%;
        margin: 1.1rem 0 0.95rem;
        padding: 1rem;
        border-radius: 22px;
        background:
          linear-gradient(180deg, rgba(40, 36, 44, 0.96), rgba(30, 27, 33, 0.98));
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03);
      }

      .sketch-fallback {
        margin: 1.1rem 0 0.95rem;
        padding: 1rem 1.1rem;
        border-radius: 22px;
        background:
          linear-gradient(180deg, rgba(40, 36, 44, 0.96), rgba(30, 27, 33, 0.98));
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03);
      }

      .sketch-fallback-title {
        margin-top: 0;
        color: var(--text);
        font-weight: 800;
      }

      .sketch-fallback-link {
        margin-bottom: 0;
      }

      iframe {
        display: block;
        max-width: 100%;
        border: 0;
        border-radius: 18px;
        background: transparent;
        box-shadow: 0 18px 30px rgba(0, 0, 0, 0.28);
      }

      .editor-link {
        margin: 0.55rem 0 1rem;
      }

      .button-link {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        padding: 0.76rem 1.05rem;
        border-radius: 999px;
        border: 1px solid rgba(255, 209, 102, 0.18);
        background: linear-gradient(135deg, rgba(252, 152, 103, 0.16), rgba(120, 220, 232, 0.16));
        color: var(--text);
        font-weight: 700;
        transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
      }

      .button-link:hover {
        transform: translateY(-2px) rotate(-0.5deg);
        box-shadow: 0 14px 28px rgba(0, 0, 0, 0.3);
        background: linear-gradient(135deg, rgba(252, 152, 103, 0.24), rgba(120, 220, 232, 0.24));
      }

      .solution-block {
        margin: 1rem 0 1.2rem;
        border-radius: 24px;
        border: 1px solid var(--code-line);
        background: linear-gradient(180deg, rgba(45, 42, 46, 0.98), rgba(34, 31, 34, 0.98));
        box-shadow: 0 18px 34px rgba(0, 0, 0, 0.22);
        overflow: hidden;
      }

      .solution-block summary {
        cursor: pointer;
        list-style: none;
        padding: 1rem 1.15rem;
        color: var(--text);
        font-weight: 800;
        background: linear-gradient(90deg, rgba(64, 62, 65, 0.98), rgba(52, 49, 53, 0.98));
        border-bottom: 1px solid var(--code-line);
      }

      .solution-block summary::-webkit-details-marker {
        display: none;
      }

      .solution-block summary::before {
        content: "+";
        display: inline-block;
        width: 1.1rem;
        margin-right: 0.5rem;
        color: var(--accent);
        font-size: 1.1rem;
        font-weight: 900;
      }

      .solution-block[open] summary::before {
        content: "-";
      }

      .solution-content {
        padding: 0.2rem 1.15rem 1rem;
        background: rgba(45, 42, 46, 0.82);
      }

      .solution-content > :first-child {
        margin-top: 0.9rem;
      }

      .solution-content > :last-child {
        margin-bottom: 0;
      }

      .code-block {
        clear: both;
        margin: 1rem 0 0.5rem;
        border-radius: 22px;
        overflow: hidden;
        border: 1px solid var(--code-line);
        background: var(--code-bg);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03);
      }

      .code-block pre {
        margin: 0;
        padding: 1rem 1.1rem 1.15rem;
        overflow-x: auto;
      }

      .code-block code {
        display: block;
        background: transparent;
        border: 0;
        padding: 0;
        color: var(--code-text);
      }

      .tok-comment { color: #727072; }
      .tok-string { color: #ffd866; }
      .tok-number { color: #ab9df2; }
      .tok-keyword { color: #ff6188; font-weight: 700; }
      .tok-builtin { color: #78dce8; }
      .tok-self { color: #fc9867; }
      .tok-class, .tok-function { color: #a9dc76; font-weight: 700; }
      .tok-name { color: #fcfcfa; }

      .content-section::before {
        content: none;
      }

      .hero > p:last-of-type {
        max-width: 58ch;
        font-size: 1.08rem;
      }

      .content-section p + .preview-frame,
      .content-section p + .editor-link,
      .content-section p + .code-block {
        margin-top: 0.95rem;
      }

      @keyframes rise-in {
        from {
          opacity: 0;
          transform: translateY(18px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }

      @media (max-width: 920px) {
        .content-section:nth-of-type(2n),
        .content-section:nth-of-type(2n + 1) {
          transform: none;
        }

        .note-layout {
          grid-template-columns: 1fr;
          gap: 0.8rem;
        }

        .margin-note {
          width: auto;
        }
      }

      @media (max-width: 700px) {
        body {
          line-height: 1.66;
        }

        .margin-note {
          padding: 0.9rem 0.95rem;
        }

        main {
          width: min(calc(100% - 1rem), 1020px);
          padding-top: 1rem;
        }

        .hero,
        .content-section {
          padding: 1.3rem;
          border-radius: 22px;
        }

        .hero::before {
          inset: 0.8rem;
          border-radius: 18px;
        }

        h1 {
          max-width: none;
          font-size: clamp(2.35rem, 11vw, 3.5rem);
        }

        h2 {
          font-size: clamp(1.7rem, 8vw, 2.2rem);
        }

        iframe {
          max-width: 100%;
        }
      }
    </style>
  </head>
  <body>
    <main>
      __CONTENT__
    </main>
  </body>
</html>
"""


def main() -> None:
    build_site(source=SOURCE, target=TARGET, title=PAGE_TITLE)


def build_site(*, source: Path, target: Path, title: str) -> None:
    global SOURCE, TARGET, PAGE_TITLE

    SOURCE = source
    TARGET = target
    PAGE_TITLE = title
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    content = render_markdown(lines)
    html_text = HTML_TEMPLATE.replace("__TITLE__", html.escape(title)).replace(
        "__CONTENT__", content
    )
    style_start = html_text.index("<style>")
    style_end = html_text.index("</style>", style_start) + len("</style>")
    css_text = html_text[
        style_start + len("<style>") : html_text.index("</style>", style_start)
    ].strip("\n")
    stylesheet_path = target.parent / SHARED_STYLESHEET_RELATIVE_PATH
    stylesheet_path.parent.mkdir(parents=True, exist_ok=True)
    stylesheet_path.write_text(css_text + "\n", encoding="utf-8")
    html_text = (
        html_text[:style_start]
        + f'<link rel="stylesheet" href="{SHARED_STYLESHEET_RELATIVE_PATH.as_posix()}" />'
        + html_text[style_end:]
    )
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(html_text, encoding="utf-8")
    print(f"Wrote {TARGET.name}")


if __name__ == "__main__":
    main()
