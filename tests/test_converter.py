import shutil
from pathlib import Path

import pytest

from doc2md.converter import Doc2Md


def test_convert_file(tmp_path):
    # prepare a simple document from tests/data if available
    # for now we create an empty file to ensure the method runs
    src = tmp_path / "dummy.pdf"
    src.write_bytes(b"%PDF-1.4\n")
    dst = tmp_path / "out"
    converter = Doc2Md()
    md_path = converter.convert_file(str(src), str(dst))
    assert md_path.exists()
    assert md_path.suffix == ".md"


def test_convert_directory(tmp_path):
    src_dir = tmp_path / "srcdir"
    src_dir.mkdir()
    f1 = src_dir / "a.pdf"
    f1.write_bytes(b"%PDF-1.4\n")
    dst_dir = tmp_path / "outdir"
    converter = Doc2Md()
    converter.convert_directory(str(src_dir), str(dst_dir), recursive=False)
    # expect converted file
    out_file = dst_dir / "a.md"
    assert out_file.exists()
