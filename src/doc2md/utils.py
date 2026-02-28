from __future__ import annotations

from pathlib import Path
from typing import Iterable
import re
import base64
from typing import Tuple, List


def ensure_directory(path: Path) -> None:
    """Create directory if it does not exist."""
    path.mkdir(parents=True, exist_ok=True)


def supported_extensions() -> Iterable[str]:
    return [".pdf", ".docx"]


def extract_images_from_markdown(md: str, image_dir: Path) -> Tuple[str, List[Path]]:
    """Extract data-URI images from Markdown and write them into image_dir.

    Returns (updated_markdown, [written_paths]).
    """
    ensure_directory(image_dir)
    pattern = re.compile(r'!\[([^\]]*)\]\((data:(image/[^;]+);base64,([^)]*?))\)', re.DOTALL)
    written: List[Path] = []
    idx = 1
    def _replace(m: re.Match) -> str:
        nonlocal idx
        alt = m.group(1)
        mime = m.group(3)  # e.g. image/png
        b64 = m.group(4)
        # sanitize and decode
        b64_clean = re.sub(r'\s+', '', b64)
        try:
            data = base64.b64decode(b64_clean)
        except Exception:
            return m.group(0)

        ext = mime.split('/', 1)[1]
        if ext == 'jpeg':
            ext = 'jpg'
        fname = f'image_{idx}.{ext}'
        out_path = image_dir / fname
        out_path.write_bytes(data)
        written.append(out_path)
        idx += 1
        # use relative path from markdown location: image_dir.name/fname
        rel = Path(image_dir.name) / fname
        return f'![{alt}]({rel.as_posix()})'

    new_md = pattern.sub(_replace, md)
    return new_md, written


def normalize_math_in_markdown(md: str) -> str:
    """Normalize common LaTeX math delimiters in Markdown.

    - Convert `\\(...\\)` -> `$...$`
    - Convert `\\[...\\]` -> `$$...$$`
    - Collapse multiple spaces inside delimiters
    """
    # inline: \( ... \) -> $...$
    md = re.sub(r"\\\((.+?)\\\)", lambda m: f"${m.group(1).strip()}$", md, flags=re.DOTALL)
    # display: \[ ... \] -> $$...$$
    md = re.sub(r"\\\[(.+?)\\\]", lambda m: f"$$\n{m.group(1).strip()}\n$$", md, flags=re.DOTALL)
    return md


def fix_pdf_extraction_artifacts(text: str) -> str:
    """Fix common PDF extraction artifacts using generalized patterns.

    - Misplaced diaeresis (e.g., G\u00a8odel -> Gödel)
    - Incorrect prime symbols (e.g., \x04 -> ')
    - Extra spaces around punctuation and symbols
    """
    import unicodedata

    # 1. Handle \x04 that should be primes
    text = text.replace("\x04", "'")

    # 2. Fix misplaced diaeresis (U+00A8)
    # They often appear as \u00a8 [space] vowel
    diaeresis_map = {
        'a': 'ä', 'e': 'ë', 'i': 'ï', 'o': 'ö', 'u': 'ü',
        'A': 'Ä', 'E': 'Ë', 'I': 'Ï', 'O': 'Ö', 'U': 'Ü'
    }

    def _fix_diaeresis(m: re.Match) -> str:
        vowel = m.group(1)
        if vowel:
            return diaeresis_map.get(vowel, str(m.group(0)))
        return str(m.group(0))

    text = re.sub(r"\u00a8\s*([aeiouAEIOU])", _fix_diaeresis, text)

    # 3. Generalized spacing fixes
    # Remove spaces before punctuation that shouldn't have them
    text = re.sub(r"\s+([,\.;:!\?])", r"\1", text)
    
    # Ensure a space after punctuation if missing (except at end of line/string)
    text = re.sub(r"([,\.;:!\?])(?=[a-zA-Z])", r"\1 ", text)

    # Fix primes spacing: "A '", "A  ' '", etc.
    # Letters followed by space and prime(s) (only if prime is NOT followed by another letter)
    text = re.sub(r"([a-zA-Z])\s+('+)(?!\w)", r"\1\2", text)
    # Multiple primes with spaces between them
    while True:
        new_text = re.sub(r"('\s+')|(' ')", "''", text)
        if new_text == text:
            break
        text = new_text

    # Fix ellipses (often extracted as . . .)
    text = re.sub(r"\.\s+\.\s+\.", "...", text)

    # 4. Final Unicode normalization
    text = unicodedata.normalize("NFC", text)

    return text
