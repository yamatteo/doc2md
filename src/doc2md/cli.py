from __future__ import annotations

import sys
from pathlib import Path
from typing import List

import click

from .converter import Doc2Md


SUPPORTED_EXTENSIONS = {".pdf", ".docx"}


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
@click.option("-v", "--verbose", is_flag=True, help="Verbose logging")
@click.argument("paths", nargs=-1, type=click.Path())
def main(
    output: str, recursive: bool, verbose: bool, paths: List[str]
) -> None:
    """Convert documents to markdown using docling.

    Provide one or more FILE or DIRECTORY paths.  Directories are
    processed as batches; use --recursive to traverse subfolders.
    """
    if not paths:
        click.echo("No input paths provided", err=True)
        sys.exit(1)

    converter = Doc2Md()
    base_out = Path(output)
    for p in paths:
        path = Path(p)
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            outdir = base_out
            converter.convert_file(str(path), str(outdir))
            if verbose:
                click.echo(f"Converted {path} -> {outdir}")
        elif path.is_dir():
            outdir = base_out / path.name
            converter.convert_directory(
                str(path), str(outdir), recursive=recursive
            )
            if verbose:
                click.echo(f"Processed directory {path} -> {outdir}")
        else:
            click.echo(f"Skipping unsupported path: {path}", err=True)


if __name__ == "__main__":
    main()  # type: ignore
