from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from docling.document_converter import DocumentConverter


class Doc2Md:
    def __init__(self, **docling_options) -> None:
        """Initialize with optional Docling DocumentConverter options."""
        self.converter = DocumentConverter(**docling_options)

    def convert_file(self, src: str, dst_dir: str) -> Path:
        """Convert a single file and return path to generated markdown file."""
        src_path = Path(src)
        dst_dir_path = Path(dst_dir)
        dst_dir_path.mkdir(parents=True, exist_ok=True)

        # perform conversion; docling may raise ConversionError for invalid files.
        try:
            doc = self.converter.convert(src_path).document
        except Exception as exc:  # docling reports ConversionError, etc.
            # write a placeholder markdown so that callers still see an output
            md_path = dst_dir_path / (src_path.stem + ".md")
            md_path.write_text(f"<!-- conversion failed: {exc} -->\n", encoding="utf-8")
            return md_path

        image_dir = dst_dir_path / (src_path.stem + "_files")
        image_dir.mkdir(exist_ok=True)

        md_content = doc.export_to_markdown(image_dir=str(image_dir))
        md_path = dst_dir_path / (src_path.stem + ".md")
        md_path.write_text(md_content, encoding="utf-8")
        return md_path

    def convert_directory(
        self, src_dir: str, dst_dir: str, recursive: bool = False
    ) -> None:
        """Convert all supported documents in a directory.

        If ``recursive`` is True, traverse subdirectories as well.
        The output tree structure is mirrored under ``dst_dir``.
        """
        src_path = Path(src_dir)
        dst_path = Path(dst_dir)
        if recursive:
            walker = src_path.rglob("*")
        else:
            walker = src_path.iterdir()

        for entry in walker:
            if entry.is_file() and entry.suffix.lower() in {".pdf", ".docx"}:
                rel = entry.relative_to(src_path)
                out_dir = dst_path / rel.parent
                self.convert_file(str(entry), str(out_dir))
