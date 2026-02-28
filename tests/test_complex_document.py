import pytest
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from doc2md.converter import Doc2Md

def markdown_to_pdf(md_text: str, output_path: Path):
    """A very simple markdown-to-pdf generator for testing purposes."""
    doc = SimpleDocTemplate(str(output_path), pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Add a custom style for math if needed, but for now we just use paragraphs
    math_style = ParagraphStyle('Math', parent=styles['Normal'], fontName='Helvetica', fontSize=10)
    
    story = []
    lines = md_text.split('\n')
    
    current_para = []
    
    def flush_para():
        if current_para:
            text = " ".join(current_para)
            story.append(Paragraph(text, styles['Normal']))
            story.append(Spacer(1, 12))
            current_para.clear()

    for line in lines:
        line = line.strip()
        if not line:
            flush_para()
            continue
        
        if line.startswith('# '):
            flush_para()
            story.append(Paragraph(line[2:], styles['Heading1']))
            story.append(Spacer(1, 12))
        elif line.startswith('## '):
            flush_para()
            story.append(Paragraph(line[3:], styles['Heading2']))
            story.append(Spacer(1, 12))
        elif line.startswith('### '):
            flush_para()
            story.append(Paragraph(line[4:], styles['Heading3']))
            story.append(Spacer(1, 12))
        elif line.startswith('$$'):
            flush_para()
            # Block math
            content = line.strip('$').strip()
            story.append(Paragraph(f"$${content}$$", styles['Normal']))
            story.append(Spacer(1, 12))
        else:
            current_para.append(line)
            
    flush_para()
    doc.build(story)

def test_complex_math_and_headings_roundtrip(tmp_path):
    md_input = """# Main Title

This is a paragraph with some lorem ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

## Section 1: Math

Here is some inline math $E = mc^2$ and more text.

$$
\\int_{0}^{1} x^2 dx = \\frac{1}{3}
$$

### Subsection 1.1

Another paragraph with more lorem ipsum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

# Second Main Title

Just to check multiple level 1 headings.
"""
    pdf_path = tmp_path / "sample.1.pdf"
    markdown_to_pdf(md_input, pdf_path)
    
    assert pdf_path.exists()
    
    out_dir = tmp_path / "out"
    converter = Doc2Md()
    md_output_path = converter.convert_file(str(pdf_path), str(out_dir))
    
    assert md_output_path.exists()
    md_output = md_output_path.read_text(encoding="utf-8")
    
    import sys
    print("\n--- EXTRACTED MARKDOWN STARTS ---", file=sys.stderr)
    print(md_output, file=sys.stderr)
    print("--- EXTRACTED MARKDOWN ENDS ---\n", file=sys.stderr)
    
    # Normalize output for easier testing: Docling often escapes characters in math
    normalized_md = md_output.replace("\\_", "_").replace("\\{", "{").replace("\\}", "}")
    
    # Verification
    # 1. Headings - check for text content of headings
    assert "Main Title" in md_output
    assert "Section 1: Math" in md_output
    assert "Subsection 1.1" in md_output
    assert "Second Main Title" in md_output
    
    # 2. Math
    # Note: docling might normalize delimiters or change spacing
    # We check for the content of the math in the normalized string
    assert "E = mc^2" in normalized_md.replace(" ", "") or "E=mc^2" in normalized_md.replace(" ", "")
    assert "int_{0}^{1}" in normalized_md.replace(" ", "")
    
    # 3. Content
    assert "lorem ipsum" in md_output.lower()
    
    # Check that h1 demotion logic worked (if multiple h1 were detected)
    # The converter script may demote headers; we check that we don't have too many # headers
    assert md_output.count("\n# ") <= 1
