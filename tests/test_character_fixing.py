import pytest
from doc2md.utils import fix_pdf_extraction_artifacts

def test_fix_diaeresis():
    assert fix_pdf_extraction_artifacts("G\u00a8odel") == "Gödel"
    assert fix_pdf_extraction_artifacts("G\u00a8 odel") == "Gödel"
    assert fix_pdf_extraction_artifacts("M\u00a8uller") == "Müller"
    assert fix_pdf_extraction_artifacts("Schr\u00a8odinger") == "Schrödinger"

def test_fix_primes():
    # \x04 should become '
    assert fix_pdf_extraction_artifacts("A\x04") == "A'"
    # Spaces between letter and prime should be removed if it's a math-like prime (not followed by word)
    assert fix_pdf_extraction_artifacts("A '") == "A'"
    assert fix_pdf_extraction_artifacts("A  ''") == "A''"
    assert fix_pdf_extraction_artifacts("A ' '") == "A''"
    # Opening quotes in text should keep their spaces
    assert fix_pdf_extraction_artifacts("take 'A implies B'") == "take 'A implies B'"

def test_fix_punctuation_spacing():
    assert fix_pdf_extraction_artifacts("Hello , world .") == "Hello, world."
    assert fix_pdf_extraction_artifacts("Is it true ? Yes !") == "Is it true? Yes!"
    assert fix_pdf_extraction_artifacts("Wait ; what : this .") == "Wait; what: this."

def test_fix_ellipses():
    assert fix_pdf_extraction_artifacts("A, B, . . .") == "A, B,..."
    assert fix_pdf_extraction_artifacts("more . . . points") == "more... points"

def test_sample_case_robust():
    sample = "(A , A  , A  , . . . )"
    # (A , -> (A,
    # A  , -> A',
    # A  , -> A'',
    # . . . -> ...
    # Result: (A, A', A'',... )
    # Note: my current regex for primes pulls them to previous letter if not followed by \w
    # "(A , A  , A  , . . . )" 
    # -> "(A, A  , A  , . . . )" (punctuation space)
    # -> "(A, A', A'', . . . )" (if \x04 was there, but sample.2.md had spaces then dots/newlines)
    
    # Let's test what actually happens with the \x04 input as seen in od output
    raw = "(A , A \x04 , A \x04 \x04 , . . . )"
    fixed = fix_pdf_extraction_artifacts(raw)
    assert "A'" in fixed
    assert "A''" in fixed
    assert "..." in fixed
    assert " ," not in fixed
