#!/usr/bin/env python3
"""Build lightweight four-up previews and per-skill full-resolution galleries."""

from __future__ import annotations

import html
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
PREVIEWS = ROOT / "assets" / "showcase-previews"
FIXTURES = ROOT / "fixtures"
README_ZH = ROOT / "README.md"
README_EN = ROOT / "README_EN.md"

SAMPLES = (
    ("01-architecture-cafe.png", "人造 / 建筑", "Built / Architecture"),
    ("02-mountain-lake.png", "自然 / 景观", "Nature / Landscape"),
    ("03-portrait-camera-duo.png", "人物 / 道具", "People / Props"),
    ("04-animal-cat-dog.png", "动物 / 互动", "Animals / Interaction"),
)

HEADING_RE = re.compile(r"^### \[([^]]+)]\(([^)]+)\)", re.MULTILINE)
TABLE_RE = re.compile(r"<table>\n.*?</table>", re.DOTALL)
SAMPLE_PATH_RE = re.compile(r"examples/([^/]+)/01-architecture-cafe\.png")
ENTRY_PATH_RE = re.compile(r"examples/([^/]+)/(?:01-architecture-cafe\.png|README\.md)")
PREVIEW_RE = re.compile(
    r'<a href="examples/([^/]+)/README\.md"><img '
    r'src="assets/showcase-previews/\1\.webp"'
)
FIXTURE_PATH_RE = re.compile(r"fixtures/01-architecture-cafe\.png")
FIXTURE_PREVIEW_RE = re.compile(
    r'<a href="fixtures/README\.md"><img '
    r'src="assets/showcase-previews/fixtures\.webp"'
)


def sample_directories() -> list[Path]:
    directories = []
    for directory in sorted(path for path in EXAMPLES.iterdir() if path.is_dir()):
        if all((directory / filename).is_file() for filename, _, _ in SAMPLES):
            directories.append(directory)
    return directories


def read_entry_metadata() -> dict[str, tuple[str, str]]:
    text = README_ZH.read_text(encoding="utf-8")
    headings = list(HEADING_RE.finditer(text))
    metadata: dict[str, tuple[str, str]] = {}

    for entry_path in ENTRY_PATH_RE.finditer(text):
        previous = [heading for heading in headings if heading.start() < entry_path.start()]
        if not previous:
            raise RuntimeError(f"No skill heading found before {entry_path.group(1)}")
        heading = previous[-1]
        metadata[entry_path.group(1)] = (heading.group(1), heading.group(2))

    return metadata


def build_four_up(directory: Path, output: Path) -> None:
    command = ["magick"]
    for filename, _, _ in SAMPLES:
        command.extend(
            [
                "(",
                str(directory / filename),
                "-auto-orient",
                "-thumbnail",
                "396x500>",
                "-background",
                "#f6f3ed",
                "-gravity",
                "center",
                "-extent",
                "396x500",
                "-bordercolor",
                "white",
                "-border",
                "2",
                ")",
            ]
        )
    command.extend(["+append", "-strip", "-quality", "80", str(output)])
    subprocess.run(command, check=True)


def build_preview(directory: Path) -> None:
    build_four_up(directory, PREVIEWS / f"{directory.name}.webp")


def build_detail_page(directory: Path, title: str, upstream: str) -> None:
    cells = []
    for filename, label_zh, label_en in SAMPLES:
        cells.append(
            "    <td width=\"25%\" align=\"center\">"
            f"<a href=\"{filename}\"><img src=\"{filename}\" "
            f"alt=\"{html.escape(title)} — {html.escape(label_en)}\" width=\"100%\"></a>"
            f"<br><code>{html.escape(label_zh)} · {html.escape(label_en)}</code></td>"
        )

    page = f"""<div align=\"center\">
  <h1>{html.escape(title)}</h1>
  <p><a href=\"../../README.md\">← 中文首页</a> · <a href=\"../../README_EN.md\">English home</a> · <a href=\"{html.escape(upstream)}\">Upstream Skill ↗</a></p>
  <p>四张统一输入的高清生成结果 · Full-resolution outputs from four standardized inputs</p>
</div>

<table>
  <tr>
{chr(10).join(cells)}
  </tr>
</table>
"""
    (directory / "README.md").write_text(page, encoding="utf-8")


def rewrite_sample_tables(path: Path, language: str) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    replacements = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal replacements
        sample_path = SAMPLE_PATH_RE.search(match.group(0))
        if not sample_path:
            return match.group(0)
        slug = sample_path.group(1)
        replacements += 1
        alt = (
            f"{slug} 的四张统一输入生成预览"
            if language == "zh"
            else f"{slug} — four standardized generated samples"
        )
        return (
            "<p align=\"center\">\n"
            f"  <a href=\"examples/{slug}/README.md\"><img "
            f"src=\"assets/showcase-previews/{slug}.webp\" "
            f"alt=\"{html.escape(alt)}\" width=\"100%\" loading=\"lazy\"></a>\n"
            "</p>"
        )

    rewritten = TABLE_RE.sub(replace, text)
    path.write_text(rewritten, encoding="utf-8")
    preview_count = len(PREVIEW_RE.findall(rewritten))
    return replacements, preview_count


def rewrite_fixture_table(path: Path, language: str) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    replacements = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal replacements
        if not FIXTURE_PATH_RE.search(match.group(0)):
            return match.group(0)
        replacements += 1
        alt = "四张统一示例输入预览" if language == "zh" else "Four standardized input fixtures"
        return (
            "<p align=\"center\">\n"
            "  <a href=\"fixtures/README.md\"><img "
            "src=\"assets/showcase-previews/fixtures.webp\" "
            f"alt=\"{alt}\" width=\"100%\" loading=\"lazy\"></a>\n"
            "</p>"
        )

    rewritten = TABLE_RE.sub(replace, text)
    path.write_text(rewritten, encoding="utf-8")
    preview_count = len(FIXTURE_PREVIEW_RE.findall(rewritten))
    return replacements, preview_count


def main() -> None:
    if not shutil.which("magick"):
        raise SystemExit("ImageMagick's `magick` command is required.")

    directories = sample_directories()
    metadata = read_entry_metadata()
    missing = [directory.name for directory in directories if directory.name not in metadata]
    if missing:
        raise SystemExit(f"Missing README metadata for: {', '.join(missing)}")

    PREVIEWS.mkdir(parents=True, exist_ok=True)
    for directory in directories:
        title, upstream = metadata[directory.name]
        build_preview(directory)
        build_detail_page(directory, title, upstream)

    build_four_up(FIXTURES, PREVIEWS / "fixtures.webp")

    zh_replaced, zh_count = rewrite_sample_tables(README_ZH, "zh")
    en_replaced, en_count = rewrite_sample_tables(README_EN, "en")
    zh_fixture_replaced, zh_fixture_count = rewrite_fixture_table(README_ZH, "zh")
    en_fixture_replaced, en_fixture_count = rewrite_fixture_table(README_EN, "en")
    expected = len(directories)
    if zh_count != expected or en_count != expected:
        raise SystemExit(
            f"Expected {expected} sample tables per README; replaced zh={zh_count}, en={en_count}."
        )
    if zh_fixture_count != 1 or en_fixture_count != 1:
        raise SystemExit(
            "Expected one fixture preview per README; "
            f"found zh={zh_fixture_count}, en={en_fixture_count}."
        )

    print(
        f"Built {expected} previews and galleries; found {zh_count + en_count} "
        f"README previews ({zh_replaced + en_replaced} newly replaced), plus two fixture "
        f"previews ({zh_fixture_replaced + en_fixture_replaced} newly replaced)."
    )


if __name__ == "__main__":
    main()
