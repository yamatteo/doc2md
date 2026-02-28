import shutil
from pathlib import Path

from tests.test_cli import run_cli


def count_paragraphs(md_text: str) -> int:
    # split on double newlines and count non-empty segments
    parts = [p for p in md_text.split("\n\n") if p.strip()]

    # filter out section headers
    parts = [p for p in parts if not p.strip().startswith("#")]

    # filter out image lines
    parts = [p for p in parts if not p.strip().startswith("<!--")]
    return len(parts)


def test_sample_pdf_conversion(tmp_path):
    # copy the provided sample PDF into tmpdir
    src_pdf = Path("assets/pdf/sample.0.pdf")
    assert src_pdf.exists(), "sample PDF not found in assets/pdf"
    dst_pdf = tmp_path / "sample.pdf"
    shutil.copy(src_pdf, dst_pdf)

    out_dir = tmp_path / "out"
    res = run_cli([str(dst_pdf), "-o", str(out_dir)], tmp_path)
    assert res.returncode == 0, f"CLI failed: {res.stderr}\n{res.stdout}"

    md_file = out_dir / "sample.md"
    assert md_file.exists(), "markdown output not created"
    text = md_file.read_text(encoding="utf-8")

    # checks from task description
    assert "Sample PDF" in text, "title missing"
    # subtitle may be prefixed with heading markup and OCR may inject 'is'
    assert "PDF file. Fun fun fun" in text, "subtitle missing"
    paras = count_paragraphs(text)
    assert paras == 4, (
        f"expected exactly 4 paragraphs (body only), got {paras}"
    )
