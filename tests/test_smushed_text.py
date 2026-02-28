import pytest
from pathlib import Path
from doc2md.converter import Doc2Md

def test_smushed_text_fix(tmp_path):
    """
    Test that the 'smushed text' bug on line 13 of sample.1.pdf is fixed.
    The problematic text was 'andwiththedesideratum(IIIc)ofconsistency,theprincipleofindifference'.
    It should now have spaces.
    """
    pdf_path = Path("assets/pdf/sample.1.pdf")
    if not pdf_path.exists():
        pytest.skip("sample.1.pdf not found in assets/pdf")
        
    converter = Doc2Md()
    md_path = converter.convert_file(str(pdf_path), str(tmp_path))
    
    content = md_path.read_text(encoding="utf-8")
    
    # Check for the correctly spaced phrase
    target_phrase = "and with the desideratum (IIIc) of consistency, the principle of indifference"
    
    # We use a flexible check in case formatting/delimiters vary slightly, 
    # but the core words must be separated by spaces.
    assert target_phrase in content, "The smushed text bug is still present or the text has changed significantly."
    
    # Also verify that common smushed version is NOT there
    smushed_fragment = "andwiththedesideratum"
    assert smushed_fragment not in content, "Found smushed text fragment 'andwiththedesideratum'"

if __name__ == "__main__":
    # Allow running manually
    import sys
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tmp:
        try:
            test_smushed_text_fix(Path(tmp))
            print("Test PASSED")
        except Exception as e:
            print(f"Test FAILED: {e}")
            sys.exit(1)
