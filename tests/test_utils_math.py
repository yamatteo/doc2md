from doc2md.utils import normalize_math_in_markdown


def test_normalize_math_inline_and_display():
    md = "This is inline math: \\(a+b\\) and display math: \\[x^2+y^2\\]."
    out = normalize_math_in_markdown(md)
    assert "$a+b$" in out
    assert "$$\n x^2+y^2\n$$" in out or "$$\nx^2+y^2\n$$" in out
