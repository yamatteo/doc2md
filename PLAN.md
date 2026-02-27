# Implementation Plan for `doc2md` Package

This document describes a **detailed plan** to build a Python package that converts generic documents (DOCX, PDF, …) into a well‑structured Markdown file. The conversion library and CLI will be a thin wrapper around [docling](https://docling-project.github.io), which is already installed and provides most of the heavy lifting.

## 🎯 Goals

1.  Provide a **library API** usable from Python code for single files or batches.
2.  Expose a **command‑line tool** with options for single file, directory batch and recursive processing.
3.  Preserve document outline (chapters, sections, …), math formulas, and externalise images.
4.  Output Markdown that is clean, readable and easy to post‑process.
5.  Delegate parsing/conversion work to *docling*; avoid re‑implementing features it already offers.

> 🚩 The new package must *use* docling as its workhorse; we don’t plan to re‑invent its export logic.

---

## 📦 Project structure

```
doc2md/                # top‑level package
    __init__.py
    converter.py       # core functions/classes wrapping docling
    cli.py             # CLI implementation (click/argparse)
    utils.py           # helpers: path management, image extraction, logging
tests/                 # unit/functional tests
    data/              # example .pdf/.docx with headings, math, images
    test_converter.py  # library tests
    test_cli.py        # CLI tests
pyproject.toml         # poetry/uv project file
README.md              # usage examples
```

---

## 🧱 Core library design (`doc2md.converter`)

### 1. Converter class / functions

```python
from docling.document_converter import DocumentConverter

class Doc2Md:
    def __init__(self, **docling_options):
        self.converter = DocumentConverter(**docling_options)

    def convert_file(self, src: str, dst_dir: str) -> Path:
        """Convert a single file and return path to generated markdown."""
        doc = self.converter.convert(src).document
        image_dir = Path(dst_dir) / (Path(src).stem + "_files")
        md = doc.export_to_markdown(image_dir=str(image_dir))
        # write md to dst_dir / src.stem + ".md"
        # docling already embeds LaTeX for math; leave as is
        # images are written to <image_dir> and linked relatively
        return md_path

    def convert_directory(self, src_dir: str, dst_dir: str, recursive: bool = False):
        """Walk directory, call convert_file on each supported document."""
        # use os.walk if recursive, else iterate top level files
```

### 2. Image handling and links

- Use `export_to_markdown(image_dir=...)` option (docling supports this).
- Ensure the output `.md` uses relative paths to the image folder.
- If docling does not support `image_dir`, post‑process the `DoclingDocument` object: iterate `doc.elements` for `Image` nodes, export bytes, write files.

### 3. Math formula support

- Docling exports math using LaTeX delimiters (`$...$`/`$$...$$`).
- No additional work; maybe add optional postprocessor to convert to MathJax‑friendly form if needed.

### 4. Configuration options

- Allow passing `docling` pipeline options (OCR, layout model, etc.) from library/CLI.
- Provide default options tuned for high‑fidelity conversion.

---

## 🖥️ Command‑line Interface (`doc2md.cli`)

Design with `click` (or `argparse` if minimal).

### CLI signature

```
doc2md [-h] [-o OUTDIR] [-r] [-v] {file,directory} paths...
```

- `-o`, `--output` – base output directory (defaults to current working dir).
- `-r`, `--recursive` – when processing directories, recurse into subdirectories.
- `-v`, `--verbose` – enable logging / progress messages.
- `paths` – one or more input files or directories. If a directory is supplied, treat as batch input.

### Behaviour

1.  For each input path:
    - If file and supported extension, convert.
    - If directory, call `convert_directory`; respect `-r` flag.
2.  Replicate relative tree structure under output directory.
3.  Print a summary at the end: files processed, errors, output location.
4.  Exit code 0 on success, >0 if any conversion failed.

### Additional options (future/optional)

- `--extension` – restrict to certain file types (docx,pdf,…).
- `--keep-layout` – pass custom page‑layout hints to docling.
- `--suffix IMAGE_SUFFIX` – allow overriding image folder naming.

---

## ✅ Tests

1.  **Unit tests** for `Doc2Md` methods using small sample documents (see `tests/data`).
    - verify headings become `#`/`##`/…
    - formulas survive (string containment)
    - images are written, links are correct
    - recursive directory processing preserves structure

2.  **CLI tests** using `subprocess` or `click.testing.CliRunner`:
    - run `doc2md` on a single file
    - run on a directory with `-r` and without
    - supply output dir and verify tree

3.  **Edge cases**
    - unsupported formats are skipped with warning
    - file permissions errors handled gracefully

Tests should use pytest and create temporary directories via `tmp_path`.

---

## 🧩 Packaging & distribution

- Use `pyproject.toml` with `poetry` or `uv` for dependency management.
- Declare `docling` (>= current installed version) as a dependency.
- Add console script entry point:

```toml
[project.scripts]
doc2md = "doc2md.cli:main"
```

- Include tests in `tool.poetry.dev-dependencies` or equivalent.
- Add `README.md` with quick start, examples, and license.

---

## 🚧 Implementation roadmap (milestones)

1.  Scaffold package layout, add dependencies, initial `pyproject.toml`.
2.  Implement `Doc2Md` class and basic file‑conversion function (without CLI).
3.  Add directory/batch support and image output handling.
4.  Write unit tests, ensure they pass with existing docling installation.
5.  Implement CLI and integrate with library.
6.  Add tests for CLI.
7.  Write documentation in README and update `docling.md` references if necessary.
8.  Perform manual trials with real DOCX/PDF examples; tweak options.
9.  Tag version 0.1.0 and publish to PyPI (optional).

---

## 📝 Notes & caveats

- Docling already handles formula recognition and Markdown export; avoid duplicating logic.
- For very large batches, consider adding parallelization (future enhancement).
- If docling's Markdown output is insufficient in some cases, add optional post‑processors.

With the above plan, the `doc2md` package will satisfy all user requirements while leveraging existing docling functionality.