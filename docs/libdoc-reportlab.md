---
title: "ReportLab Documentation"
package_name: "reportlab"
version: ">=4.4.10"
source: "https://docs.reportlab.com/"
last_updated: "2026-03-18 17:49:00"
description: "ReportLab is an open-source Python library for generating PDF documents programmatically with high-quality graphics and text rendering."
---

# ReportLab

ReportLab is an open-source Python library that enables direct creation of PDF documents using Python programming language. It provides comprehensive tools for generating reports, charts, and data graphics in various formats, with PDF as its primary output format.

## Version Information
- **Installed Version**: `>=4.4.10`
- **Documentation Source**: https://docs.reportlab.com/
- **Last Updated**: 2026-03-18 17:49:00

## Key Features
- 📄 Direct PDF generation without intermediate steps
- 🎨 High-quality graphics and chart creation
- 📊 Comprehensive table and layout support
- 🔤 Advanced text formatting and typography
- 🖼️ Image embedding and manipulation
- 📐 Precise positioning and layout control
- 🚀 Fast performance for report generation
- 🔧 Extensible architecture for custom components
- 📱 Cross-platform compatibility
- 🌐 Unicode and international text support

## Installation
```bash
pip install reportlab>=4.4.10
```

## Basic Usage
```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create PDF canvas
c = canvas.Canvas("hello.pdf", pagesize=letter)

# Add text
c.drawString(100, 750, "Hello, World!")
c.drawString(100, 730, "This is a PDF generated with ReportLab")

# Save PDF
c.save()
```

## Working with Platypus (Document Templates)
```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

# Create document
doc = SimpleDocTemplate("example.pdf", pagesize=letter)
styles = getSampleStyleSheet()

# Build content
story = []
story.append(Paragraph("ReportLab Example", styles["Title"]))
story.append(Spacer(1, 12))
story.append(Paragraph("This is a paragraph using the Normal style.", styles["Normal"]))

# Generate PDF
doc.build(story)
```

## Creating Tables
```python
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

# Table data
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '25', 'New York'],
    ['Bob', '30', 'San Francisco'],
    ['Charlie', '35', 'Chicago']
]

# Create table
table = Table(data)

# Add styling
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
```

## Drawing Graphics
```python
from reportlab.graphics.shapes import Drawing, Circle, Rect
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.barcharts import VerticalBarChart

# Create drawing
d = Drawing(400, 200)

# Add shapes
d.add(Circle(100, 100, 50, fillColor=colors.red))
d.add(Rect(200, 50, 100, 100, fillColor=colors.blue))

# Add bar chart
bc = VerticalBarChart()
bc.x = 50
bc.y = 50
bc.height = 125
bc.width = 300
bc.data = [(1, 2, 3, 4), (5, 6, 7, 8)]
d.add(bc)
```

## Additional Resources
- [Official Documentation](https://docs.reportlab.com/)
- [PyPI Package](https://pypi.org/project/reportlab/)
- [User Guide](https://docs.reportlab.com/reportlab/userguide/)
- [GitHub Repository](https://github.com/reportlab/reportlab)
- [Community Support](http://two.pairlist.net/mailman/listinfo/reportlab-users)

---

*This documentation was automatically generated using Tavily Remote MCP and the dependency-documenter skill.*
