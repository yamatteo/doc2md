from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from docling.document_converter import DocumentConverter
from .utils import ensure_directory, extract_images_from_markdown


class Doc2Md:
    def __init__(self, **docling_options) -> None:
        """Initialize with optional Docling DocumentConverter options."""
        from docling.datamodel.base_models import InputFormat
        from docling.document_converter import PdfFormatOption
        from docling.datamodel.pipeline_options import PdfPipelineOptions
        from docling.datamodel.layout_model_specs import DOCLING_LAYOUT_V2
        from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend

        pipeline_options = PdfPipelineOptions()
        pipeline_options.layout_options.model_spec = DOCLING_LAYOUT_V2
        pipeline_options.do_formula_enrichment = True

        # merge with provided options
        format_options = docling_options.pop("format_options", {})
        if InputFormat.PDF not in format_options:
            format_options[InputFormat.PDF] = PdfFormatOption(
                pipeline_options=pipeline_options,
                backend=PyPdfiumDocumentBackend
            )

        self.converter = DocumentConverter(
            format_options=format_options, **docling_options
        )

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
            md_path.write_text(
                f"<!-- conversion failed: {exc} -->\n", encoding="utf-8"
            )
            return md_path

        image_dir = dst_dir_path / (src_path.stem + "_files")
        image_dir.mkdir(exist_ok=True)

        # Some docling versions do not accept an `image_dir` argument.
        # Call export_to_markdown() without kwargs and post-process images.
        md_content = doc.export_to_markdown()

        # Post-process Markdown: extract any embedded data-URI images into image_dir
        try:
            md_content, _written = extract_images_from_markdown(
                md_content, image_dir
            )
        except Exception:
            # if extraction fails, continue with original md_content
            pass

        # Normalize math delimiters (\( \) -> $ $, \[ \] -> $$ $$)
        try:
            from .utils import normalize_math_in_markdown, fix_pdf_extraction_artifacts

            md_content = normalize_math_in_markdown(md_content)
            md_content = fix_pdf_extraction_artifacts(md_content)
        except Exception:
            pass

        # ensure title elements inside pictures are preserved by prepending
        try:
            extras: list[str] = []
            for item in getattr(doc, "texts", []):
                # look for section headers whose parent is a picture
                if item.__class__.__name__ == "SectionHeaderItem":
                    parent = getattr(item, "parent", None)
                    if parent and getattr(parent, "cref", "").startswith(
                        "#/pictures"
                    ):
                        extras.append(f"# {item.text}")
            if extras:
                md_content = "\n\n".join(extras) + "\n\n" + md_content
        except Exception:
            pass

        # Post-process headers: if multiple level-1 headers, demote all but the first.
        try:
            lines = md_content.splitlines()
            new_lines = []
            h1_found = False
            for line in lines:
                if line.startswith("# "):
                    if h1_found:
                        new_lines.append("## " + line[2:])
                    else:
                        new_lines.append(line)
                        h1_found = True
                else:
                    new_lines.append(line)
            md_content = "\n".join(new_lines)
        except Exception:
            pass

        # write result and return
        md_path = dst_dir_path / (src_path.stem + ".md")
        md_path.write_text(md_content, encoding="utf-8")
        return md_path

    def convert_directory(
        self, src_dir: str, dst_dir: str, recursive: bool = False
    ) -> None:
        """Convert all supported documents in a directory.

        If ``recursive`` is True, traverse subdirectories as well.
        The output tree structure is mirrored under ``dst_dir"""
        src_path = Path(src_dir)
        dst_path = Path(dst_dir)
        if recursive:
            walker = src_path.rglob("*")
        else:
            walker = src_path.iterdir()

        for entry in walker:
            if entry.is_file() and entry.suffix.lower() in {".pdf", ".docx"}:
                rel = entry.relative_to(src_path)
                # rel.parent is '.' for files at the root of src_path
                if rel.parent == Path("."):
                    out_dir = dst_path
                else:
                    out_dir = dst_path / rel.parent
                ensure_directory(out_dir)
                self.convert_file(str(entry), str(out_dir))
