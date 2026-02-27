import subprocess
from pathlib import Path

import pytest


def run_cli(args, tmp_path):
    result = subprocess.run(
        ["uv", "run", "python", "-m", "doc2md.cli"] + args,
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    return result


def test_cli_single_file(tmp_path):
    src = tmp_path / "test.pdf"
    # create a minimal valid PDF so docling can open it
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    c = canvas.Canvas(str(src), pagesize=letter)
    c.drawString(100, 750, "Hello CLI")
    c.showPage()
    c.save()
    res = run_cli([str(src)], tmp_path)
    # CLI returns 0 when conversion succeeded
    assert res.returncode == 0
    assert (tmp_path / "test.md").exists()


def test_cli_directory(tmp_path):
    d = tmp_path / "docs"
    d.mkdir()
    # write a small valid PDF inside the directory
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    p = d / "a.pdf"
    c = canvas.Canvas(str(p), pagesize=letter)
    c.drawString(100, 750, "Doc A")
    c.showPage()
    c.save()
    res = run_cli([str(d), "-o", str(tmp_path / "out")], tmp_path)
    assert res.returncode == 0
    assert (tmp_path / "out" / "docs" / "a.md").exists()
