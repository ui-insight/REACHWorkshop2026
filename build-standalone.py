#!/usr/bin/env python3
"""Build a self-contained HTML version of slides-ai-literacy.html.

All CSS, JS, and images are inlined so the file can be shared standalone.
Run from the repo root: python3 build-standalone.py
"""

import base64
import mimetypes
import os
import re
import urllib.request

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
SRC = os.path.join(DOCS, "slides-ai-literacy.html")
OUT = os.path.join(DOCS, "slides-ai-literacy-standalone.html")

# Image cache for external URLs
_url_cache: dict[str, str] = {}


def read_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def mime_for(path: str) -> str:
    mt, _ = mimetypes.guess_type(path)
    return mt or "application/octet-stream"


def to_data_uri(path: str) -> str:
    return f"data:{mime_for(path)};base64,{read_b64(path)}"


def fetch_b64(url: str) -> str:
    if url in _url_cache:
        return _url_cache[url]
    print(f"  Downloading {url} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = base64.b64encode(resp.read()).decode()
        ct = resp.headers.get("Content-Type", "image/jpeg").split(";")[0]
    uri = f"data:{ct};base64,{data}"
    _url_cache[url] = uri
    return uri


def inline_css(html: str) -> str:
    """Replace <link rel="stylesheet" href="..."> with inline <style>."""
    def replacer(m):
        href = m.group(1)
        path = os.path.join(DOCS, href)
        if not os.path.isfile(path):
            print(f"  WARNING: CSS not found: {path}")
            return m.group(0)
        print(f"  Inlining CSS: {href}")
        css = read_text(path)
        return f"<style>/* {href} */\n{css}\n</style>"

    return re.sub(
        r'<link\s+rel="stylesheet"\s+href="([^"]+)"\s*/?>',
        replacer,
        html,
    )


def inline_js(html: str) -> str:
    """Replace <script src="..."> with inline <script>."""
    def replacer(m):
        attrs = m.group(1)
        src_match = re.search(r'src="([^"]+)"', attrs)
        if not src_match:
            return m.group(0)
        src = src_match.group(1)
        path = os.path.join(DOCS, src)
        if not os.path.isfile(path):
            print(f"  WARNING: JS not found: {path}")
            return m.group(0)
        print(f"  Inlining JS: {src}")
        js = read_text(path)
        # Preserve type attribute but remove src
        tag_attrs = re.sub(r'\s*src="[^"]*"', "", attrs).strip()
        if tag_attrs:
            tag_attrs = " " + tag_attrs
        return f"<script{tag_attrs}>/* {src} */\n{js}\n</script>"

    return re.sub(r"<script\s+([^>]*src=\"[^\"]+\"[^>]*)>\s*</script>", replacer, html)


def inline_images(html: str) -> str:
    """Replace img src and CSS url() with data URIs."""
    def img_replacer(m):
        prefix = m.group(1)
        src = m.group(2)
        if src.startswith("data:"):
            return m.group(0)
        if src.startswith("http://") or src.startswith("https://"):
            try:
                uri = fetch_b64(src)
            except Exception as e:
                print(f"  WARNING: Could not fetch {src}: {e}")
                return m.group(0)
        else:
            path = os.path.join(DOCS, src)
            if not os.path.isfile(path):
                print(f"  WARNING: Image not found: {path}")
                return m.group(0)
            print(f"  Inlining image: {src}")
            uri = to_data_uri(path)
        return f'{prefix}"{uri}"'

    # Handle src="..." and href="..." for images
    html = re.sub(r'((?:src|poster)=)"([^"]+\.(?:png|jpg|jpeg|gif|svg|webp))"', img_replacer, html, flags=re.IGNORECASE)

    # Handle CSS url() in inline styles
    def css_url_replacer(m):
        src = m.group(1)
        if src.startswith("data:"):
            return m.group(0)
        path = os.path.join(DOCS, src)
        if not os.path.isfile(path):
            print(f"  WARNING: CSS url image not found: {path}")
            return m.group(0)
        print(f"  Inlining CSS url: {src}")
        return f"url({to_data_uri(path)})"

    html = re.sub(r'url\(([^)]+\.(?:png|jpg|jpeg|gif|svg|webp))\)', css_url_replacer, html, flags=re.IGNORECASE)

    return html


def inline_pdfs(html: str) -> str:
    """Replace PDF/XLSX download hrefs with data URIs so downloads work offline."""
    def replacer(m):
        prefix = m.group(1)
        href = m.group(2)
        suffix = m.group(3)
        path = os.path.join(DOCS, href)
        if not os.path.isfile(path):
            print(f"  WARNING: File not found: {path}")
            return m.group(0)
        print(f"  Inlining download: {href}")
        mime = mime_for(path)
        b64 = read_b64(path)
        return f'{prefix}"data:{mime};base64,{b64}"{suffix}'

    return re.sub(
        r'(href=)"(files/[^"]+\.(?:pdf|xlsx))"([^>]*download)',
        replacer,
        html,
        flags=re.IGNORECASE,
    )


def inline_modules(html: str) -> str:
    """Inline ES module imports so no external .js files are needed."""
    # Find inline <script type="module"> blocks that import from local files
    def replacer(m):
        body = m.group(1)
        # Collect all local imports
        imports = re.findall(r"import\s+\{([^}]+)\}\s+from\s+['\"]\.\/([^'\"]+)['\"];?", body)
        if not imports:
            return m.group(0)
        preamble = ""
        new_body = body
        for names, mod_path in imports:
            path = os.path.join(DOCS, mod_path)
            if not os.path.isfile(path):
                print(f"  WARNING: Module not found: {path}")
                continue
            print(f"  Inlining module: {mod_path}")
            mod_src = read_text(path)
            # Strip export keywords so functions are available in scope
            mod_src = re.sub(r"^export\s+", "", mod_src, flags=re.MULTILINE)
            preamble += f"/* {mod_path} */\n{mod_src}\n"
            # Remove the import line
            new_body = re.sub(
                r"import\s+\{[^}]*\}\s+from\s+['\"]\./" + re.escape(mod_path) + r"['\"];?\s*\n?",
                "",
                new_body,
            )
        # Change to regular script (no module) since we inlined everything
        return f"<script>\n{preamble}{new_body}</script>"

    return re.sub(
        r'<script\s+type="module">\s*(.*?)\s*</script>',
        replacer,
        html,
        flags=re.DOTALL,
    )


def strip_back_link(html: str) -> str:
    """Remove the 'Back to Sessions' link since this is standalone."""
    return re.sub(
        r'<div class="slides-home">.*?</div>',
        '<div class="slides-home"><span style="opacity:0.5;">AI4RA Workshop - Standalone</span></div>',
        html,
        flags=re.DOTALL,
    )


def main():
    print("Building standalone slide deck...")
    html = read_text(SRC)

    print("\n[1/6] Inlining CSS...")
    html = inline_css(html)

    print("\n[2/6] Inlining JS...")
    html = inline_js(html)

    print("\n[3/7] Inlining ES modules...")
    html = inline_modules(html)

    print("\n[4/7] Inlining images...")
    html = inline_images(html)

    print("\n[5/7] Inlining downloadable files...")
    html = inline_pdfs(html)

    print("\n[6/7] Adjusting standalone navigation...")
    html = strip_back_link(html)

    print(f"\n[7/7] Writing {OUT}...")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    size_mb = os.path.getsize(OUT) / (1024 * 1024)
    print(f"\nDone! {OUT}")
    print(f"File size: {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
