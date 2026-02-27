from pathlib import Path

from doc2md.utils import extract_images_from_markdown


def test_extract_images_from_markdown(tmp_path):
    img_b64 = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAASsJTYQAAAAASUVORK5CYII="
    )
    md = f"Here is an image: ![one](data:image/png;base64,{img_b64})\n"
    image_dir = tmp_path / "test_files"
    new_md, written = extract_images_from_markdown(md, image_dir)
    assert len(written) == 1
    out_path = written[0]
    assert out_path.exists()
    assert out_path.suffix == ".png"
    # markdown should reference the image directory by name
    assert f"{image_dir.name}/{out_path.name}" in new_md
