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
    src.write_bytes(b"%PDF-1.4\n")
    res = run_cli([str(src)], tmp_path)
    assert res.returncode == 0
    assert (tmp_path / "test.md").exists()


def test_cli_directory(tmp_path):
    d = tmp_path / "docs"
    d.mkdir()
    (d / "a.pdf").write_bytes(b"%PDF-1.4\n")
    res = run_cli([str(d), "-o", str(tmp_path / "out")], tmp_path)
    assert res.returncode == 0
    assert (tmp_path / "out" / "docs" / "a.md").exists()
