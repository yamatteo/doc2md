from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import List, Set

import click

from .converter import Doc2Md


def _parse_extensions(exts: str) -> Set[str]:
    return {('.' + e.strip().lstrip('.').lower()) for e in exts.split(',') if e.strip()}


@click.command()
@click.option(
    "-o",
    "--output",
    type=click.Path(file_okay=False),
    default=".",
    help="Base output directory",
)
@click.option(
    "-r", "--recursive", is_flag=True, help="Recursively process directories"
)
@click.option(
    "-e",
    "--extensions",
    default="pdf,docx",
    help="Comma-separated list of extensions to process (default: pdf,docx)",
)
@click.option("-v", "--verbose", is_flag=True, help="Verbose logging")
@click.argument("paths", nargs=-1, type=click.Path())
def main(
    output: str, recursive: bool, extensions: str, verbose: bool, paths: List[str]
) -> None:
    """Convert documents to markdown using docling.

    Provide one or more FILE or DIRECTORY paths. Directories are
    processed as batches; use --recursive to traverse subfolders.
    """
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="[%(levelname)s] %(message)s",
    )

    if not paths:
        logging.error("No input paths provided")
        sys.exit(1)

    exts: Set[str] = _parse_extensions(extensions)
    converter = Doc2Md()
    base_out = Path(output)

    failures = 0
    processed = 0

    for p in paths:
        path = Path(p)
        if path.is_file() and path.suffix.lower() in exts:
            outdir = base_out
            md = converter.convert_file(str(path), str(outdir))
            processed += 1
            # detect placeholder failure inserted by converter
            try:
                content = md.read_text(encoding='utf-8')
                if content.lstrip().startswith('<!-- conversion failed'):
                    logging.error("Conversion failed for %s", path)
                    failures += 1
                else:
                    logging.info("Converted %s -> %s", path, outdir)
            except Exception:
                logging.error("Unable to read output for %s", path)
                failures += 1

        elif path.is_dir():
            outdir = base_out / path.name
            converter.convert_directory(str(path), str(outdir), recursive=recursive)
            logging.info("Processed directory %s -> %s", path, outdir)

        else:
            logging.warning("Skipping unsupported path: %s", path)

    logging.info("Processed %d files; failures: %d", processed, failures)
    if failures:
        sys.exit(2)


if __name__ == "__main__":
    main()  # type: ignore
