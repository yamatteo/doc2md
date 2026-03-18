# doc2md

`doc2md` is a lightweight wrapper around [Docling](https://docling-project.github.io) that
converts generic documents (`.pdf`, `.docx`, and others) into well-structured
Markdown files with extracted images and preserved math formulas.

## Features

- **Library & CLI**: use from Python or as a command‑line tool
- **Outline preservation**: headings are translated to `#`/`##`/… levels
- **Math support**: LaTeX formulas are kept, with normalization of delimiters
- **Images**: embedded data‑URI graphics are written to separate files and linked
- **Batch & recursive processing**: convert single files or entire directories
- **Customizable extensions**: limit file types via CLI option
- **PDF text enhancement**: automatic fixing of common PDF extraction artifacts including:
  - Misplaced diaeresis and accent marks
  - Incorrect prime symbols and spacing
  - Smushed text (words without spaces)
  - Punctuation spacing issues
- **Simple dependencies**: relies on `docling` for heavy lifting

> The workhorse is `docling`; this project adds convenient I/O, postprocessing,
> and a user-friendly command line.

## Installation

```sh
# using uv (recommended for this repo)
cd /path/to/doc2md
uv sync --all-extras  # installs dependencies including dev extras

# or from PyPI once published
pip install doc2md
```

Dependencies (see `pyproject.toml`):

- `docling>=2.75.0`
- `click` for CLI
- `reportlab` (used in tests and by users for PDF creation)

## Quickstart

### As a library

```python
from doc2md.converter import Doc2Md

converter = Doc2Md()
out = converter.convert_file("/path/to/document.pdf", "/output/dir")
print("Generated markdown:", out)
```

Batch/recursive usage:

```python
converter.convert_directory("docs", "md-output", recursive=True)
```

### Command-line tool

```sh
# convert a single file
doc2md somefile.pdf

# specify output directory, process recursively
doc2md -o md-output -r folder_with_docs

# limit extensions (e.g. only .docx)
doc2md -e docx folder_with_mixed
```

The CLI prints progress messages and exits with status `0` on success, `2` if
any conversion failed.

## Development

Tests are located under `tests/`. You can generate sample documents using the
provided helper functions in tests (they require `python-docx`, `Pillow`, and
`reportlab`). Run them with:

```sh
uv run python -m pytest -q
```

## Future work

- Add support for additional formats via `docling` (e.g. PPTX, HTML)
- Improve math extraction, parallel batch processing, and progress reporting
- Publish to PyPI and add versioning
- Extend PDF text enhancement with more character encoding fixes
- Add configurable options for text processing intensity

## License

MIT
