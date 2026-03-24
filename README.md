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

> 🚩 The workhorse is `docling`; this project adds convenient I/O, postprocessing,
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

## Architecture & Design

### Project Structure

```
doc2md/                # top‑level package
    __init__.py
    converter.py       # core functions/classes wrapping docling
    cli.py             # CLI implementation (click)
    utils.py           # helpers: path management, image extraction, logging
tests/                 # unit/functional tests
    data/              # example .pdf/.docx with headings, math, images
    test_converter.py  # library tests
    test_cli.py        # CLI tests
pyproject.toml         # uv project file
README.md              # usage examples
```

### Core Library Design

The `Doc2Md` class in `doc2md.converter` provides the main functionality:

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

### Image Handling and Links

- Uses `export_to_markdown(image_dir=...)` option from docling
- Ensures the output `.md` uses relative paths to the image folder
- Images are written to `<filename>_files/` directories and linked relatively

### Math Formula Support

- Docling exports math using LaTeX delimiters (`$...$`/`$$...$$`)
- No additional work required; optional post-processing available for MathJax-friendly forms

### CLI Interface

The CLI is built with `click` and supports:

```
doc2md [-h] [-o OUTDIR] [-r] [-v] [-e EXTENSIONS] {file,directory} paths...
```

- `-o`, `--output` – base output directory (defaults to current working dir)
- `-r`, `--recursive` – when processing directories, recurse into subdirectories
- `-v`, `--verbose` – enable logging / progress messages
- `-e`, `--extensions` – restrict to certain file types (docx,pdf,…)

## Development

### Running Tests

Tests are located under `tests/`. You can generate sample documents using the
provided helper functions in tests (they require `python-docx`, `Pillow`, and
`reportlab`). Run them with:

```sh
uv run python -m pytest -q
```

### Test Coverage

1. **Unit tests** for `Doc2Md` methods using sample documents:
   - verify headings become `#`/`##`/…
   - formulas survive (string containment)
   - images are written, links are correct
   - recursive directory processing preserves structure

2. **CLI tests** using `subprocess` or `click.testing.CliRunner`:
   - run `doc2md` on a single file
   - run on a directory with `-r` and without
   - supply output dir and verify tree

3. **Edge cases**:
   - unsupported formats are skipped with warning
   - file permissions errors handled gracefully

## Implementation Roadmap

The project follows this implementation plan:

1. ✅ Scaffold package layout, add dependencies, initial `pyproject.toml`
2. ✅ Implement `Doc2Md` class and basic file‑conversion function
3. ✅ Add directory/batch support and image output handling
4. ✅ Write unit tests, ensure they pass with existing docling installation
5. ✅ Implement CLI and integrate with library
6. ✅ Add tests for CLI
7. ✅ Write documentation and examples
8. 🔄 Perform manual trials with real DOCX/PDF examples; tweak options
9. 📋 Tag version 0.1.0 and publish to PyPI

## Future Work

- Add support for additional formats via `docling` (e.g. PPTX, HTML)
- Improve math extraction, parallel batch processing, and progress reporting
- Publish to PyPI and add versioning
- Extend PDF text enhancement with more character encoding fixes
- Add configurable options for text processing intensity
- For very large batches, consider adding parallelization

## Notes & Caveats

- Docling already handles formula recognition and Markdown export; this project avoids duplicating logic
- If docling's Markdown output is insufficient in some cases, optional post‑processors can be added
- The package delegates parsing/conversion work to docling; we don't re‑implement features it already offers

## License

MIT
