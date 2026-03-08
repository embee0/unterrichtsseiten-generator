import base64
import html
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
EDIT_RE = re.compile(r"\{\{EDIT:\s*([^}]+?)\s*\}\}")
SIZE_RE = re.compile(r"\bsize\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)")
IFRAME_CHROME = 16

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


def sketch_url_is_safe(filename: str, *, presentation: bool) -> bool:
    return (
        len(make_sketch_link(filename, presentation=presentation))
        <= MAX_SKETCH_URL_LENGTH
    )


def render_sketch_fallback(filename: str, *, presentation: bool) -> str:
    if presentation:
        title = "Vorschau nicht direkt eingebettet"
        text = (
            "Dieser py5-Sketch ist zu lang für die URL-basierte Vorschau. "
            "Die Seite zeigt deshalb hier absichtlich keinen kaputten iframe an."
        )
        button_label = "Python-Datei öffnen"
    else:
        title = "Editor-Link ersetzt"
        text = (
            "Dieser Sketch ist zu lang für einen py5-Editorlink mit ?sketch=. "
            "Arbeite stattdessen direkt mit der Python-Datei aus diesem Ordner."
        )
        button_label = "Python-Datei öffnen"

    href = quote(get_target_relative_path(filename))
    return (
        '<div class="sketch-fallback">'
        f'<p class="sketch-fallback-title">{html.escape(title)}</p>'
        f"<p>{html.escape(text)}</p>"
        f'<p class="sketch-fallback-link"><a class="button-link" href="{html.escape(href, quote=True)}">{html.escape(button_label)}</a></p>'
        "</div>"
    )


def get_sketch_dimensions(filename: str) -> tuple[int, int]:
    code = get_asset_path(filename).read_text(encoding="utf-8")
    match = SIZE_RE.search(code)
    if not match:
        return 300, 300
    return int(match.group(1)), int(match.group(2))


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
    if not sketch_url_is_safe(filename, presentation=True):
        return render_sketch_fallback(filename, presentation=True)

    url = make_sketch_link(filename, presentation=True)
    sketch_width, sketch_height = get_sketch_dimensions(filename)
    iframe_width = sketch_width + IFRAME_CHROME
    iframe_height = sketch_height + IFRAME_CHROME
    return (
        '<div class="preview-frame">'
        f'<iframe src="{html.escape(url, quote=True)}" width="{iframe_width}" height="{iframe_height}" loading="lazy"></iframe>'
        "</div>"
    )


def render_edit_link(filename: str) -> str:
    if not sketch_url_is_safe(filename, presentation=False):
        return render_sketch_fallback(filename, presentation=False)

    url = make_sketch_link(filename, presentation=False)
    return (
        '<p class="editor-link">'
        f'<a class="button-link" href="{html.escape(url, quote=True)}">Im Editor öffnen</a>'
        "</p>"
    )


def render_margin_note(note_text: str) -> str:
    return f'<aside class="margin-note">{inline_format(note_text)}</aside>'


def render_markdown(lines: list[str]) -> str:
    parts: list[str] = []
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

        if in_code:
            if stripped.startswith("```"):
                code = "\n".join(code_lines)
                parts.append(render_code_block(code, code_language))
                in_code = False
                code_language = ""
                code_lines = []
            else:
                code_lines.append(line)
            continue

        if stripped.startswith("```"):
            in_ul, in_ol = close_lists(parts, in_ul, in_ol)
            in_code = True
            code_language = stripped[3:].strip()
            code_lines = []
            continue

        if not stripped:
            in_ul, in_ol = close_lists(parts, in_ul, in_ol)
            continue

        if stripped == "---":
            in_ul, in_ol = close_lists(parts, in_ul, in_ol)
            parts.append("<hr />")
            continue

        iframe_match = IFRAME_RE.fullmatch(stripped)
        if iframe_match:
            in_ul, in_ol = close_lists(parts, in_ul, in_ol)
            parts.append(render_iframe(iframe_match.group(1).strip()))
            continue

        edit_match = EDIT_RE.fullmatch(stripped)
        if edit_match:
            in_ul, in_ol = close_lists(parts, in_ul, in_ol)
            parts.append(render_edit_link(edit_match.group(1).strip()))
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
            in_ul, in_ol = close_lists(parts, in_ul, in_ol)
            parts.append(f"<h3>{inline_format(stripped[4:].strip())}</h3>")
            continue

        if stripped.startswith(">"):
            in_ul, in_ol = close_lists(parts, in_ul, in_ol)
            note_text = stripped[1:].strip()
            note_html = render_margin_note(note_text)
            if parts and parts[-1].startswith("<p>"):
                previous_paragraph = parts.pop()
                parts.append(note_html)
                parts.append(previous_paragraph)
            else:
                parts.append(note_html)
            continue

        match_ol = re.match(r"(\d+)\.\s+(.*)", stripped)
        if match_ol:
            if in_ul:
                parts.append("</ul>")
                in_ul = False
            if not in_ol:
                parts.append("<ol>")
                in_ol = True
            parts.append(f"<li>{inline_format(match_ol.group(2))}</li>")
            continue

        if stripped.startswith("- "):
            if in_ol:
                parts.append("</ol>")
                in_ol = False
            if not in_ul:
                parts.append("<ul>")
                in_ul = True
            parts.append(f"<li>{inline_format(stripped[2:])}</li>")
            continue

        in_ul, in_ol = close_lists(parts, in_ul, in_ol)
        parts.append(f"<p>{inline_format(stripped)}</p>")

    if in_code:
        code = "\n".join(code_lines)
        parts.append(render_code_block(code, code_language))

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
    <link href=\"https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap\" rel=\"stylesheet\" />
    <style>
      :root {
        --bg: #17161b;
        --bg-deep: #111015;
        --panel: rgba(31, 29, 37, 0.88);
        --panel-strong: rgba(39, 36, 46, 0.94);
        --panel-soft: rgba(43, 39, 52, 0.72);
        --text: #f8f8f2;
        --muted: #b7b3c0;
        --accent: #fd971f;
        --accent-2: #66d9ef;
        --accent-3: #f92672;
        --accent-4: #a6e22e;
        --accent-5: #ae81ff;
        --border: rgba(255, 255, 255, 0.08);
        --shadow: 0 24px 80px rgba(0, 0, 0, 0.42);
        --code-bg: #121118;
        --code-text: #f8f8f2;
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
          radial-gradient(circle at 10% 12%, rgba(249, 38, 114, 0.16), transparent 24%),
          radial-gradient(circle at 84% 8%, rgba(102, 217, 239, 0.16), transparent 24%),
          radial-gradient(circle at 48% 120%, rgba(166, 226, 46, 0.12), transparent 28%),
          linear-gradient(180deg, #151419 0%, #17161b 38%, #111015 100%);
      }

      body::before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        background-image:
          linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
          linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
        background-size: 36px 36px;
        mask-image: radial-gradient(circle at center, black 42%, transparent 95%);
        opacity: 0.5;
      }

      body::after {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        opacity: 0.07;
        background-image: radial-gradient(rgba(255, 255, 255, 0.8) 0.5px, transparent 0.5px);
        background-size: 12px 12px;
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
          linear-gradient(155deg, rgba(40, 36, 50, 0.98), rgba(26, 24, 32, 0.92)),
          var(--panel);
      }

      .hero::before {
        content: "";
        position: absolute;
        inset: 1rem;
        border: 1px solid rgba(102, 217, 239, 0.14);
        border-radius: 24px;
        pointer-events: none;
        box-shadow: inset 0 0 0 1px rgba(249, 38, 114, 0.06);
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
          radial-gradient(circle at 30% 30%, rgba(102, 217, 239, 0.34), transparent 50%),
          radial-gradient(circle at 70% 70%, rgba(249, 38, 114, 0.28), transparent 48%);
        filter: blur(12px);
        opacity: 0.75;
        pointer-events: none;
      }

      .content-section {
        padding: 2rem 2rem 2.1rem;
        margin-top: 1.15rem;
        background:
          linear-gradient(180deg, rgba(35, 32, 43, 0.96), rgba(24, 23, 30, 0.96));
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
        font-family: "Sora", "Manrope", sans-serif;
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
        border-bottom: 1px solid rgba(102, 217, 239, 0.24);
      }

      a:hover {
        color: var(--accent);
      }

      code {
        font-family: "JetBrains Mono", Menlo, Consolas, monospace;
        color: #f8f8f2;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.07);
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
          radial-gradient(circle at center, rgba(166, 226, 46, 0.9) 0 2px, transparent 3px),
          linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.14), transparent);
        background-repeat: no-repeat;
        background-position: center center;
      }

      .margin-note {
        float: right;
        width: min(16rem, 42%);
        margin: 0.15rem 0 0.9rem 1.4rem;
        padding: 1rem 1rem 1rem 1.2rem;
        border-radius: 20px;
        background: linear-gradient(180deg, rgba(44, 40, 54, 0.98), rgba(31, 29, 39, 0.94));
        border: 1px solid rgba(249, 38, 114, 0.2);
        color: #d6d1de;
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
          linear-gradient(180deg, rgba(26, 24, 32, 0.96), rgba(20, 19, 26, 0.98));
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03);
      }

      .sketch-fallback {
        margin: 1.1rem 0 0.95rem;
        padding: 1rem 1.1rem;
        border-radius: 22px;
        background:
          linear-gradient(180deg, rgba(26, 24, 32, 0.96), rgba(20, 19, 26, 0.98));
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
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        background: white;
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
        border: 1px solid rgba(255, 255, 255, 0.1);
        background: linear-gradient(135deg, rgba(249, 38, 114, 0.18), rgba(102, 217, 239, 0.16));
        color: var(--text);
        font-weight: 700;
        transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
      }

      .button-link:hover {
        transform: translateY(-2px) rotate(-0.5deg);
        box-shadow: 0 14px 28px rgba(0, 0, 0, 0.3);
        background: linear-gradient(135deg, rgba(249, 38, 114, 0.24), rgba(102, 217, 239, 0.24));
      }

      .code-block {
        clear: both;
        margin: 1rem 0 0.5rem;
        border-radius: 22px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.08);
        background: var(--code-bg);
        box-shadow: 0 20px 34px rgba(0, 0, 0, 0.34);
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

      .tok-comment { color: #75715e; }
      .tok-string { color: #e6db74; }
      .tok-number { color: #ae81ff; }
      .tok-keyword { color: #f92672; font-weight: 700; }
      .tok-builtin { color: #66d9ef; }
      .tok-self { color: #fd971f; }
      .tok-class, .tok-function { color: #a6e22e; font-weight: 700; }
      .tok-name { color: #f8f8f2; }

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

        .margin-note {
          float: none;
          width: auto;
          margin: 0 0 0.8rem;
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
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(html_text, encoding="utf-8")
    print(f"Wrote {TARGET.name}")


if __name__ == "__main__":
    main()
