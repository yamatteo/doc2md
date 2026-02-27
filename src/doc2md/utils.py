from __future__ import annotations

from pathlib import Path
from typing import Iterable


def ensure_directory(path: Path) -> None:
    """Create directory if it does not exist."""
    path.mkdir(parents=True, exist_ok=True)


def supported_extensions() -> Iterable[str]:
    return [".pdf", ".docx"]
