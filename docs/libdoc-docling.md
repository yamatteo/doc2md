---
title: "Docling Documentation"
package_name: "docling"
version: ">=2.75.0"
source: "https://docling-project.github.io/docling/"
last_updated: "2026-03-18 17:49:00"
description: "Docling is an open-source document parsing and conversion library for extracting structured data from PDFs and documents using advanced AI models."
---

# Docling

Docling is an open-source document parsing and conversion library for extracting structured data from PDFs and documents using advanced AI models. Developed by IBM Research, it provides powerful capabilities for document understanding and conversion.

## Version Information
- **Installed Version**: `>=2.75.0`
- **Documentation Source**: https://docling-project.github.io/docling/
- **Last Updated**: 2026-03-18 17:49:00

## Key Features
- 🗂️ Parsing of multiple document formats including PDF, DOCX, PPTX, XLSX, HTML, WAV, MP3, WebVTT, images, and LaTeX
- 📑 Advanced PDF understanding with page layout, reading order, table structure, code, formulas, and image classification
- 🧬 Unified DoclingDocument representation format
- ↪️ Various export formats including Markdown, HTML, WebVTT, DocTags, and JSON
- 📜 Support for application-specific XML schemas (USPTO patents, JATS articles, XBRL financial reports)
- 🔒 Local execution capabilities for sensitive data
- 🤖 Plug-and-play integrations with LangChain, LlamaIndex, Crew AI & Haystack
- 🔍 Extensive OCR support for scanned PDFs and images
- 👓 Support for Visual Language Models (GraniteDocling)
- 🎙️ Audio support with Automatic Speech Recognition (ASR) models
- 🔌 MCP server for agentic applications
- 💻 Simple and convenient CLI

## Installation
```bash
pip install docling>=2.75.0
```

## Basic Usage
```python
from docling.document_converter import DocumentConverter

# Initialize converter
converter = DocumentConverter()

# Convert document
result = converter.convert("document.pdf")
document = result.document

# Export to markdown
md_content = document.export_to_markdown()
```

## Advanced Configuration
```python
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.layout_model_specs import DOCLING_LAYOUT_V2
from docling.document_converter import PdfFormatOption

# Configure pipeline options
pipeline_options = PdfPipelineOptions()
pipeline_options.layout_options.model_spec = DOCLING_LAYOUT_V2
pipeline_options.do_formula_enrichment = True

# Create converter with custom options
format_options = {
    "pdf": PdfFormatOption(pipeline_options=pipeline_options)
}
converter = DocumentConverter(format_options=format_options)
```

## Additional Resources
- [Official Documentation](https://docling-project.github.io/docling/)
- [GitHub Repository](https://github.com/docling-project/docling)
- [PyPI Package](https://pypi.org/project/docling/)
- [Examples](https://docling-project.github.io/docling/examples/)
- [Integrations](https://docling-project.github.io/docling/integrations/)

---

*This documentation was automatically generated using Tavily Remote MCP and the dependency-documenter skill.*
