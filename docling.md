Docling simplifies document processing, parsing diverse formats — including advanced PDF understanding — and providing seamless integrations with the gen AI ecosystem.

## Getting started

🐣 Ready to kick off your Docling journey? Let's dive right into it!

## Features

-   🗂️ Parsing of [multiple document formats](https://docling-project.github.io/docling/usage/supported_formats/) incl. PDF, DOCX, PPTX, XLSX, HTML, WAV, MP3, WebVTT, images (PNG, TIFF, JPEG, ...), LaTeX, and more
-   📑 Advanced PDF understanding incl. page layout, reading order, table structure, code, formulas, image classification, and more
-   🧬 Unified, expressive [DoclingDocument](https://docling-project.github.io/docling/concepts/docling_document/) representation format
-   ↪️ Various [export formats](https://docling-project.github.io/docling/usage/supported_formats/) and options, including Markdown, HTML, [DocTags](https://arxiv.org/abs/2503.11576) and lossless JSON
-   🔒 Local execution capabilities for sensitive data and air-gapped environments
-   🤖 Plug-and-play [integrations](https://docling-project.github.io/docling/integrations/) incl. LangChain, LlamaIndex, Crew AI & Haystack for agentic AI
-   🔍 Extensive OCR support for scanned PDFs and images
-   👓 Support of several Visual Language Models ([GraniteDocling](https://huggingface.co/ibm-granite/granite-docling-258M))
-   🎙️ Support for Audio with Automatic Speech Recognition (ASR) models
-   🔌 Connect to any agent using the [Docling MCP](https://docling-project.github.io/docling/usage/mcp/) server
-   💻 Simple and convenient CLI

### What's new

-   📤 Structured \[information extraction\]\[extraction\] \[🧪 beta\]
-   📑 New layout model (**Heron**) by default, for faster PDF parsing
-   🔌 [MCP server](https://docling-project.github.io/docling/usage/mcp/) for agentic applications
-   💬 Parsing of Web Video Text Tracks (WebVTT) files
-   💬 Parsing of LaTeX files

### Coming soon

-   📝 Metadata extraction, including title, authors, references & language
-   📝 Chart understanding (Barchart, Piechart, LinePlot, etc)
-   📝 Complex chemistry understanding (Molecular structures)

## What's next

🚀 The journey has just begun! Join us and become a part of the growing Docling community.

-   [GitHub](https://github.com/docling-project/docling)
-   [Discord](https://docling.ai/discord)
-   [LinkedIn](https://linkedin.com/company/docling/)

## Live assistant

Do you want to leverage the power of AI and get live support on Docling? Try out the [Chat with Dosu](https://app.dosu.dev/097760a8-135e-4789-8234-90c8837d7f1c/ask?utm_source=github) functionalities provided by our friends at [Dosu](https://dosu.dev/).

[![Chat with Dosu](https://dosu.dev/dosu-chat-badge.svg)](https://app.dosu.dev/097760a8-135e-4789-8234-90c8837d7f1c/ask?utm_source=github)

## LF AI & Data

Docling is hosted as a project in the [LF AI & Data Foundation](https://lfaidata.foundation/projects/).

### IBM ❤️ Open Source AI

The project was started by the AI for knowledge team at IBM Research Zurich.

---

To use Docling, simply install `docling` from your Python package manager, e.g. pip:

```
pip install docling
```

Works on macOS, Linux, and Windows, with support for both x86\_64 and arm64 architectures.

Alternative PyTorch distributions

The Docling models depend on the [PyTorch](https://pytorch.org/) library. Depending on your architecture, you might want to use a different distribution of `torch`. For example, you might want support for different accelerator or for a cpu-only version. All the different ways for installing `torch` are listed on their website [https://pytorch.org/](https://pytorch.org/).

One common situation is the installation on Linux systems with cpu-only support. In this case, we suggest the installation of Docling with the following options

```
# Example for installing on the Linux cpu-only version
pip install docling --extra-index-url https://download.pytorch.org/whl/cpu

```
Installation on macOS Intel (x86\_64)

When installing Docling on macOS with Intel processors, you might encounter errors with PyTorch compatibility. This happens because newer PyTorch versions (2.6.0+) no longer provide wheels for Intel-based Macs.

If you're using an Intel Mac, install Docling with compatible PyTorch **Note:** PyTorch 2.2.2 requires Python 3.12 or lower. Make sure you're not using Python 3.13+.

```
# For uv users
uv add torch==2.2.2 torchvision==0.17.2 docling

# For pip users
pip install "docling[mac_intel]"

# For Poetry users
poetry add docling

```

The `docling` package is designed to offer a working solution for the Docling default options. Some Docling functionalities require additional third-party packages and are therefore installed only if selected as extras (or installed independently).

The following table summarizes the extras available in the `docling` package. They can be activated with: `pip install "docling[NAME1,NAME2]"`

### OCR engines

Docling supports multiple OCR engines for processing scanned documents. The current version provides the following engines.

The Docling `DocumentConverter` allows to choose the OCR engine with the `ocr_options` settings. For example

```
from docling.datamodel.base_models import ConversionStatus, PipelineOptions
from docling.datamodel.pipeline_options import PipelineOptions, EasyOcrOptions, TesseractOcrOptions
from docling.document_converter import DocumentConverter

pipeline_options = PipelineOptions()
pipeline_options.do_ocr = True
pipeline_options.ocr_options = TesseractOcrOptions()  # Use Tesseract

doc_converter = DocumentConverter(
    pipeline_options=pipeline_options,
)

```

Tesseract installation

[Tesseract](https://github.com/tesseract-ocr/tesseract) is a popular OCR engine which is available on most operating systems. For using this engine with Docling, Tesseract must be installed on your system, using the packaging tool of your choice. Below we provide example commands. After installing Tesseract you are expected to provide the path to its language files using the `TESSDATA_PREFIX` environment variable (note that it must terminate with a slash `/`).

```
brew install tesseract leptonica pkg-config
TESSDATA_PREFIX=/opt/homebrew/share/tessdata/
echo "Set TESSDATA_PREFIX=${TESSDATA_PREFIX}"

```

```
apt-get install tesseract-ocr tesseract-ocr-eng libtesseract-dev libleptonica-dev pkg-config
TESSDATA_PREFIX=$(dpkg -L tesseract-ocr-eng | grep tessdata$)
echo "Set TESSDATA_PREFIX=${TESSDATA_PREFIX}"

```

```
dnf install tesseract tesseract-devel tesseract-langpack-eng tesseract-osd leptonica-devel
TESSDATA_PREFIX=/usr/share/tesseract/tessdata/
echo "Set TESSDATA_PREFIX=${TESSDATA_PREFIX}"

```

#### Linking to Tesseract

The most efficient usage of the Tesseract library is via linking. Docling is using the [Tesserocr](https://github.com/sirfz/tesserocr) package for this.

If you get into installation issues of Tesserocr, we suggest using the following installation options:

```
pip uninstall tesserocr
pip install --no-binary :all: tesserocr

```

## Development setup

To develop Docling features, bugfixes etc., install as follows from your local clone's root dir:
```
uv sync --all-extras
```

---

## Basic usage

### Python

In Docling, working with documents is as simple as:

1.  converting your source file to a Docling document
2.  using that Docling document for your workflow

For example, the snippet below shows conversion with export to Markdown:

```
from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # file path or URL
converter = DocumentConverter()
doc = converter.convert(source).document

print(doc.export_to_markdown())  # output: "### Docling Technical Report[...]"

```

Docling supports a wide array of [file formats](https://docling-project.github.io/docling/usage/supported_formats/) and, as outlined in the [architecture](https://docling-project.github.io/docling/concepts/architecture/) guide, provides a versatile document model along with a full suite of supported operations.

### CLI

You can additionally use Docling directly from your terminal, for instance:

```
docling https://arxiv.org/pdf/2206.01062

```

The CLI provides various options, such as 🥚[GraniteDocling](https://huggingface.co/ibm-granite/granite-docling-258M) (incl. MLX acceleration) & other VLMs:

```
docling --pipeline vlm --vlm-model granite_docling https://arxiv.org/pdf/2206.01062

```

For all available options, run `docling --help` or check the [CLI reference](https://docling-project.github.io/docling/reference/cli/).

## What's next

Check out the Usage subpages (navigation menu on the left) as well as our [featured examples](https://docling-project.github.io/docling/examples/) for additional usage workflows, including conversion customization, RAG, framework integrations, chunking, serialization, enrichments, and much more!

---

# ⚡ RTX GPU Acceleration

![Docling on RTX](https://docling-project.github.io/docling/assets/nvidia_logo_green.svg)

Whether you're an AI enthusiast, researcher, or developer working with document processing, this guide will help you unlock the full potential of your NVIDIA RTX GPU with Docling.

By leveraging GPU acceleration, you can achieve up to **6x speedup** compared to CPU-only processing. This dramatic performance improvement makes GPU acceleration especially valuable for processing large batches of documents, handling high-throughput document conversion workflows, or experimenting with advanced document understanding models.

## Prerequisites

Before setting up GPU acceleration, ensure you have:

-   An NVIDIA RTX GPU (RTX 40/50 series)
-   Windows 10/11 or Linux operating system

## Installation Steps

### 1\. Install NVIDIA GPU Drivers

First, ensure you have the latest NVIDIA GPU drivers installed:

-   **Windows**: Download from [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx)
-   **Linux**: Use your distribution's package manager or download from NVIDIA

Verify the installation:

```
nvidia-smi

```

This command should display your GPU information and driver version.

### 2\. Install CUDA Toolkit

CUDA is NVIDIA's parallel computing platform required for GPU acceleration.

Follow the official installation guide for your operating system at [NVIDIA CUDA Downloads](https://developer.nvidia.com/cuda-downloads). The installer will guide you through the process and automatically set up the required environment variables.

### 3\. Install cuDNN

cuDNN provides optimized implementations for deep learning operations.

Follow the official installation guide at [NVIDIA cuDNN Downloads](https://developer.nvidia.com/cudnn). The guide provides detailed instructions for all supported platforms.

### 4\. Install PyTorch with CUDA Support

To use GPU acceleration with Docling, you need to install PyTorch with CUDA support using the special `extra-index-url`:

```
# For CUDA 12.8 (current default for PyTorch)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

# For CUDA 13.0
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130

```

Note

The `--index-url` parameter is crucial as it ensures you get the CUDA-enabled version of PyTorch instead of the CPU-only version.

For other CUDA versions and installation options, refer to the [PyTorch Installation Matrix](https://pytorch.org/get-started/locally/).

Verify PyTorch CUDA installation:

```
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
print(f"GPU device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")

```

### 5\. Install and Run Docling

Install Docling with all dependencies:

```
pip install docling

```

**That's it!** Docling will automatically detect and use your RTX GPU when available. No additional configuration is required for basic usage.

```
from docling.document_converter import DocumentConverter

# Docling automatically uses GPU when available
converter = DocumentConverter()
result = converter.convert("document.pdf")

```

**Advanced: Tuning GPU Performance** For optimal GPU performance with large document batches, you can adjust batch sizes and explicitly configure the accelerator:

```
from docling.document_converter import DocumentConverter
from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
from docling.datamodel.pipeline_options import ThreadedPdfPipelineOptions

# Explicitly configure GPU acceleration
accelerator_options = AcceleratorOptions(
    device=AcceleratorDevice.CUDA,  # Use CUDA for NVIDIA GPUs
)

# Configure pipeline for optimal GPU performance
pipeline_options = ThreadedPdfPipelineOptions(
    ocr_batch_size=64,      # Increase batch size for GPU
    layout_batch_size=64,   # Increase batch size for GPU
    table_batch_size=4,
)

# Create converter with custom settings
converter = DocumentConverter(
    accelerator_options=accelerator_options,
    pipeline_options=pipeline_options,
)

# Convert documents
result = converter.convert("document.pdf")

```

Adjust batch sizes based on your GPU memory (see Performance Optimization Tips below).

## GPU-Accelerated VLM Pipeline

For maximum performance with Vision Language Models (VLM), you can run a local inference server on your RTX GPU. This approach provides significantly better throughput than inline VLM processing.

### Linux: Using vLLM (Recommended)

vLLM provides the best performance for GPU-accelerated VLM inference. Start the vLLM server with optimized parameters:

```
vllm serve ibm-granite/granite-docling-258M \
  --host 127.0.0.1 --port 8000 \
  --max-num-seqs 512 \
  --max-num-batched-tokens 8192 \
  --enable-chunked-prefill \
  --gpu-memory-utilization 0.9

```

### Windows: Using llama-server

On Windows, you can use `llama-server` from llama.cpp for GPU-accelerated VLM inference:

#### Installation

1.  Download the latest llama.cpp release from the [GitHub releases page](https://github.com/ggml-org/llama.cpp/releases)
2.  Extract the archive and locate `llama-server.exe`

#### Launch Command

```
llama-server.exe `
  --hf-repo ibm-granite/granite-docling-258M-GGUF `
  -cb `
  -ngl -1 `
  --port 8000 `
  --context-shift `
  -np 16 -c 131072

```

Performance Comparison

vLLM delivers approximately **4x better performance** compared to llama-server. For Windows users seeking maximum performance, consider running vLLM via WSL2 (Windows Subsystem for Linux). See [vLLM on RTX 5090 via Docker](https://github.com/BoltzmannEntropy/vLLM-5090) for detailed WSL2 setup instructions.

### Configure Docling for VLM Server

Once your inference server is running, configure Docling to use it:

```
from docling.datamodel.pipeline_options import VlmPipelineOptions
from docling.datamodel.settings import settings

BATCH_SIZE = 64

# Configure VLM options
vlm_options = vlm_model_specs.GRANITEDOCLING_VLLM_API
vlm_options.concurrency = BATCH_SIZE

# when running with llama.cpp (llama-server), use the different model name.
# vlm_options.params["model"] = "ibm-granite_granite-docling-258M-GGUF_granite-docling-258M-BF16.gguf"

# Set page batch size to match or exceed concurrency
settings.perf.page_batch_size = BATCH_SIZE

# Create converter with VLM pipeline
converter = DocumentConverter(
    pipeline_options=vlm_options,
)

```

For more details on VLM pipeline configuration, see the [GPU Support Guide](https://docling-project.github.io/docling/usage/gpu/).

## Performance Optimization Tips

### Batch Size Tuning

Adjust batch sizes based on your GPU memory:

-   **RTX 5090 (32GB)**: Use batch sizes of 64-128
-   **RTX 4090 (24GB)**: Use batch sizes of 32-64
-   **RTX 5070 (12GB)**: Use batch sizes of 16-32

### Memory Management

Monitor GPU memory usage:

```
import torch

# Check GPU memory
if torch.cuda.is_available():
    print(f"GPU Memory allocated: {torch.cuda.memory_allocated(0) / 1024**3:.2f} GB")
    print(f"GPU Memory reserved: {torch.cuda.memory_reserved(0) / 1024**3:.2f} GB")

```

## Troubleshooting

### CUDA Out of Memory

If you encounter out-of-memory errors:

1.  Reduce batch sizes in `pipeline_options`
2.  Process fewer documents concurrently
3.  Clear GPU cache between batches:

```
import torch
torch.cuda.empty_cache()

```

### CUDA Not Available

If `torch.cuda.is_available()` returns `False`:

1.  Verify NVIDIA drivers are installed: `nvidia-smi`
2.  Check CUDA installation: `nvcc --version`
3.  Reinstall PyTorch with correct CUDA version
4.  Ensure your GPU is CUDA-compatible

### Performance Not Improving

If GPU acceleration doesn't improve performance:

1.  Increase batch sizes (if memory allows)
2.  Ensure you're processing enough documents to benefit from GPU parallelization
3.  Check GPU utilization: `nvidia-smi -l 1`
4.  Verify PyTorch is using GPU: `torch.cuda.is_available()`

## Additional Resources

-   [NVIDIA CUDA Documentation](https://docs.nvidia.com/cuda/)
-   [PyTorch CUDA Installation Guide](https://pytorch.org/get-started/locally/)
-   [Docling GPU Support Guide](https://docling-project.github.io/docling/usage/gpu/)
-   [GPU Performance Examples](https://docling-project.github.io/docling/examples/gpu_standard_pipeline/)

---

# Advanced options

## Model prefetching and offline usage

By default, models are downloaded automatically upon first usage. If you would prefer to explicitly prefetch them for offline use (e.g. in air-gapped environments) you can do that as follows:

**Step 1: Prefetch the models**

Use the `docling-tools models download` utility:

```
$ docling-tools models download
Downloading layout model...
Downloading tableformer model...
Downloading picture classifier model...
Downloading code formula model...
Downloading easyocr models...
Models downloaded into $HOME/.cache/docling/models.

```

Alternatively, models can be programmatically downloaded using `docling.utils.model_downloader.download_models()`.

Also, you can use `download-hf-repo` parameter to download arbitrary models from HuggingFace by specifying repo id:

```
$ docling-tools models download-hf-repo ds4sd/SmolDocling-256M-preview
Downloading ds4sd/SmolDocling-256M-preview model from HuggingFace...

```

**Step 2: Use the prefetched models**

```
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import EasyOcrOptions, PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

artifacts_path = "/local/path/to/models"

pipeline_options = PdfPipelineOptions(artifacts_path=artifacts_path)
doc_converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

```

Or using the CLI:

```
docling --artifacts-path="/local/path/to/models" FILE

```

Or using the `DOCLING_ARTIFACTS_PATH` environment variable:

```
export DOCLING_ARTIFACTS_PATH="/local/path/to/models"
python my_docling_script.py

```

## Using remote services

The main purpose of Docling is to run local models which are not sharing any user data with remote services. Anyhow, there are valid use cases for processing part of the pipeline using remote services, for example invoking OCR engines from cloud vendors or the usage of hosted LLMs.

In Docling we decided to allow such models, but we require the user to explicitly opt-in in communicating with external services.

```
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

pipeline_options = PdfPipelineOptions(enable_remote_services=True)
doc_converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

```

When the value `enable_remote_services=True` is not set, the system will raise an exception `OperationNotAllowed()`.

_Note: This option is only related to the system sending user data to remote services. Control of pulling data (e.g. model weights) follows the logic described in [Model prefetching and offline usage](https://docling-project.github.io/docling/usage/advanced_options/#model-prefetching-and-offline-usage)._

### List of remote model services

The options in this list require the explicit `enable_remote_services=True` when processing the documents.

-   `PictureDescriptionApiOptions`: Using vision models via API calls.

## Adjust pipeline features

The example file [custom\_convert.py](https://docling-project.github.io/docling/examples/custom_convert/) contains multiple ways one can adjust the conversion pipeline and features.

### Control PDF table extraction options

You can control if table structure recognition should map the recognized structure back to PDF cells (default) or use text cells from the structure prediction itself. This can improve output quality if you find that multiple columns in extracted tables are erroneously merged into one.

```
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions

pipeline_options = PdfPipelineOptions(do_table_structure=True)
pipeline_options.table_structure_options.do_cell_matching = False  # uses text cells predicted from table structure model

doc_converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

```

Since docling 1.16.0: You can control which TableFormer mode you want to use. Choose between `TableFormerMode.FAST` (faster but less accurate) and `TableFormerMode.ACCURATE` (default) to receive better quality with difficult table structures.

```
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode

pipeline_options = PdfPipelineOptions(do_table_structure=True)
pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE  # use more accurate TableFormer model

doc_converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

```

## Impose limits on the document size

You can limit the file size and number of pages which should be allowed to process per document:

```
from pathlib import Path
from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"
converter = DocumentConverter()
result = converter.convert(source, max_num_pages=100, max_file_size=20971520)

```

## Convert from binary PDF streams

You can convert PDFs from a binary stream instead of from the filesystem as follows:

```
from io import BytesIO
from docling.datamodel.base_models import DocumentStream
from docling.document_converter import DocumentConverter

buf = BytesIO(your_binary_stream)
source = DocumentStream(name="my_doc.pdf", stream=buf)
converter = DocumentConverter()
result = converter.convert(source)

```

## Limit resource usage

You can limit the CPU threads used by Docling by setting the environment variable `OMP_NUM_THREADS` accordingly. The default setting is using 4 CPU threads.

---

# Supported formats

Docling can parse various documents formats into a unified representation (Docling Document), which it can export to different formats too — check out [Architecture](https://docling-project.github.io/docling/concepts/architecture/) for more details.

Below you can find a listing of all supported input and output formats.

## Supported input formats

| Format | Description |
| --- | --- |
| PDF |  |
| DOCX, XLSX, PPTX | Default formats in MS Office 2007+, based on Office Open XML |
| Markdown |  |
| AsciiDoc | Human-readable, plain-text markup language for structured technical content |
| LaTeX | Scientific document preparation system |
| HTML, XHTML |  |
| CSV |  |
| PNG, JPEG, TIFF, BMP, WEBP | Image formats |
| WebVTT | Web Video Text Tracks format for displaying timed text |

Schema-specific support:

| Format | Description |
| --- | --- |
| USPTO XML | XML format followed by [USPTO](https://www.uspto.gov/patents) patents |
| JATS XML | XML format followed by [JATS](https://jats.nlm.nih.gov/) articles |
| XBRL XML | XML format for business and financial reporting following [XBRL](https://www.xbrl.org/) standard |
| Docling JSON | JSON-serialized [Docling Document](https://docling-project.github.io/docling/concepts/docling_document/) |

## Supported output formats

| Format | Description |
| --- | --- |
| HTML | Both image embedding and referencing are supported |
| Markdown |  |
| JSON | Lossless serialization of Docling Document |
| Text | Plain text, i.e. without Markdown markers |
| [Doctags](https://arxiv.org/pdf/2503.11576) | Markup format for efficiently representing the full content and layout characteristics of a document |

---

# Enrichment features

Docling allows to enrich the conversion pipeline with additional steps which process specific document components, e.g. code blocks, pictures, etc. The extra steps usually require extra models executions which may increase the processing time consistently. For this reason most enrichment models are disabled by default.

The following table provides an overview of the default enrichment models available in Docling.

| Feature | Parameter | Processed item | Description |
| --- | --- | --- | --- |
| Code understanding | `do_code_enrichment` | `CodeItem` | See [docs below](https://docling-project.github.io/docling/usage/enrichments/#code-understanding). |
| Formula understanding | `do_formula_enrichment` | `TextItem` with label `FORMULA` | See [docs below](https://docling-project.github.io/docling/usage/enrichments/#formula-understanding). |
| Picture classification | `do_picture_classification` | `PictureItem` | See [docs below](https://docling-project.github.io/docling/usage/enrichments/#picture-classification). |
| Picture description | `do_picture_description` | `PictureItem` | See [docs below](https://docling-project.github.io/docling/usage/enrichments/#picture-description). |

## Enrichments details

### Code understanding

The code understanding step allows to use advanced parsing for code blocks found in the document. This enrichment model also set the `code_language` property of the `CodeItem`.

Model specs: see the [`CodeFormula` model card](https://huggingface.co/ds4sd/CodeFormula).

Example command line:

```
docling --enrich-code FILE

```

Example code:

```
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat

pipeline_options = PdfPipelineOptions()
pipeline_options.do_code_enrichment = True

converter = DocumentConverter(format_options={
    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
})

result = converter.convert("https://arxiv.org/pdf/2501.17887")
doc = result.document

```

### Formula understanding

The formula understanding step will analyze the equation formulas in documents and extract their LaTeX representation. The HTML export functions in the DoclingDocument will leverage the formula and visualize the result using the mathml html syntax.

Model specs: see the [`CodeFormula` model card](https://huggingface.co/ds4sd/CodeFormula).

Example command line:

```
docling --enrich-formula FILE

```

Example code:

```
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat

pipeline_options = PdfPipelineOptions()
pipeline_options.do_formula_enrichment = True

converter = DocumentConverter(format_options={
    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
})

result = converter.convert("https://arxiv.org/pdf/2501.17887")
doc = result.document

```

### Picture classification

The picture classification step classifies the `PictureItem` elements in the document with the `DocumentFigureClassifier` model. This model is specialized to understand the classes of pictures found in documents, e.g. different chart types, flow diagrams, logos, signatures, etc.

Model specs: see the [`DocumentFigureClassifier` model card](https://huggingface.co/ds4sd/DocumentFigureClassifier).

Example command line:

```
docling --enrich-picture-classes FILE

```

Example code:

```
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat

pipeline_options = PdfPipelineOptions()
pipeline_options.generate_picture_images = True
pipeline_options.images_scale = 2
pipeline_options.do_picture_classification = True

converter = DocumentConverter(format_options={
    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
})

result = converter.convert("https://arxiv.org/pdf/2501.17887")
doc = result.document

```

### Picture description

The picture description step allows to annotate a picture with a vision model. This is also known as a "captioning" task. The Docling pipeline allows to load and run models completely locally as well as connecting to remote API which support the chat template. Below follow a few examples on how to use some common vision model and remote services.

```
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat

pipeline_options = PdfPipelineOptions()
pipeline_options.do_picture_description = True

converter = DocumentConverter(format_options={
    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
})

result = converter.convert("https://arxiv.org/pdf/2501.17887")
doc = result.document

```

#### Granite Vision model

Model specs: see the [`ibm-granite/granite-vision-3.1-2b-preview` model card](https://huggingface.co/ibm-granite/granite-vision-3.1-2b-preview).

Usage in Docling:

```
from docling.datamodel.pipeline_options import granite_picture_description

pipeline_options.picture_description_options = granite_picture_description

```

#### SmolVLM model

Model specs: see the [`HuggingFaceTB/SmolVLM-256M-Instruct` model card](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct).

Usage in Docling:

```
from docling.datamodel.pipeline_options import smolvlm_picture_description

pipeline_options.picture_description_options = smolvlm_picture_description

```

#### Other vision models

The option class `PictureDescriptionVlmOptions` allows to use any another model from the Hugging Face Hub.

```
from docling.datamodel.pipeline_options import PictureDescriptionVlmOptions

pipeline_options.picture_description_options = PictureDescriptionVlmOptions(
    repo_id="",  # <-- add here the Hugging Face repo_id of your favorite VLM
    prompt="Describe the image in three sentences. Be concise and accurate.",
)

```

#### Remote vision model

The option class `PictureDescriptionApiOptions` allows to use models hosted on remote platforms, e.g. on local endpoints served by [VLLM](https://docs.vllm.ai), [Ollama](https://ollama.com/) and others, or cloud providers like [IBM watsonx.ai](https://www.ibm.com/products/watsonx-ai), etc.

_Note: in most cases this option will send your data to the remote service provider._

Usage in Docling:

```
from docling.datamodel.pipeline_options import PictureDescriptionApiOptions

# Enable connections to remote services
pipeline_options.enable_remote_services=True  # <-- this is required!

# Example using a model running locally, e.g. via VLLM
# $ vllm serve MODEL_NAME
pipeline_options.picture_description_options = PictureDescriptionApiOptions(
    url="http://localhost:8000/v1/chat/completions",
    params=dict(
        model="MODEL NAME",
        seed=42,
        max_completion_tokens=200,
    ),
    prompt="Describe the image in three sentences. Be concise and accurate.",
    timeout=90,
)

```

End-to-end code snippets for cloud providers are available in the examples section:

-   [IBM watsonx.ai](https://docling-project.github.io/docling/examples/pictures_description_api/)

## Develop new enrichment models

Besides looking at the implementation of all the models listed above, the Docling documentation has a few examples dedicated to the implementation of enrichment models.

-   [Develop picture enrichment](https://docling-project.github.io/docling/examples/develop_picture_enrichment/)
-   [Develop formula enrichment](https://docling-project.github.io/docling/examples/develop_formula_understanding/)

---

# Vision Models

The `VlmPipeline` in Docling allows you to convert documents end-to-end using a vision-language model.

Docling supports vision-language models which output:

-   DocTags (e.g. [SmolDocling](https://huggingface.co/ds4sd/SmolDocling-256M-preview)), the preferred choice
-   Markdown
-   HTML

Complete Model Catalog

For a comprehensive overview of **all models and stages** in Docling (Layout, Table Structure, OCR, VLM, etc.), see the **[Model Catalog](https://docling-project.github.io/docling/usage/model_catalog/)**.

## Quick Start

For running Docling using local models with the `VlmPipeline`:

[CLI](https://docling-project.github.io/docling/usage/vision_models//#cli)[Python](https://docling-project.github.io/docling/usage/vision_models//#python)

```
docling --pipeline vlm FILE

```

See also the example [minimal\_vlm\_pipeline.py](https://docling-project.github.io/docling/examples/minimal_vlm_pipeline/).

```
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.pipeline.vlm_pipeline import VlmPipeline

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_cls=VlmPipeline,
        ),
    }
)

doc = converter.convert(source="FILE").document

```

## Available local models

By default, the vision-language models are running locally. Docling allows to choose between the Hugging Face [Transformers](https://github.com/huggingface/transformers) framework and the [MLX](https://github.com/Blaizzy/mlx-vlm) (for Apple devices with MPS acceleration) one.

The following table reports the models currently available out-of-the-box.

| Model instance | Model | Framework | Device | Num pages | Inference time (sec) |
| --- | --- | --- | --- | --- | --- |
| `vlm_model_specs.GRANITEDOCLING_TRANSFORMERS` | [ibm-granite/granite-docling-258M](https://huggingface.co/ibm-granite/granite-docling-258M) | `Transformers/AutoModelForVision2Seq` | MPS | 1 | \- |
| `vlm_model_specs.GRANITEDOCLING_MLX` | [ibm-granite/granite-docling-258M-mlx-bf16](https://huggingface.co/ibm-granite/granite-docling-258M-mlx-bf16) | `MLX` | MPS | 1 | \- |
| `vlm_model_specs.SMOLDOCLING_TRANSFORMERS` | [ds4sd/SmolDocling-256M-preview](https://huggingface.co/ds4sd/SmolDocling-256M-preview) | `Transformers/AutoModelForVision2Seq` | MPS | 1 | 102.212 |
| `vlm_model_specs.SMOLDOCLING_MLX` | [ds4sd/SmolDocling-256M-preview-mlx-bf16](https://huggingface.co/ds4sd/SmolDocling-256M-preview-mlx-bf16) | `MLX` | MPS | 1 | 6.15453 |
| `vlm_model_specs.QWEN25_VL_3B_MLX` | [mlx-community/Qwen2.5-VL-3B-Instruct-bf16](https://huggingface.co/mlx-community/Qwen2.5-VL-3B-Instruct-bf16) | `MLX` | MPS | 1 | 23.4951 |
| `vlm_model_specs.PIXTRAL_12B_MLX` | [mlx-community/pixtral-12b-bf16](https://huggingface.co/mlx-community/pixtral-12b-bf16) | `MLX` | MPS | 1 | 308.856 |
| `vlm_model_specs.GEMMA3_12B_MLX` | [mlx-community/gemma-3-12b-it-bf16](https://huggingface.co/mlx-community/gemma-3-12b-it-bf16) | `MLX` | MPS | 1 | 378.486 |
| `vlm_model_specs.GRANITE_VISION_TRANSFORMERS` | [ibm-granite/granite-vision-3.2-2b](https://huggingface.co/ibm-granite/granite-vision-3.2-2b) | `Transformers/AutoModelForVision2Seq` | MPS | 1 | 104.75 |
| `vlm_model_specs.PHI4_TRANSFORMERS` | [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) | `Transformers/AutoModelForCasualLM` | CPU | 1 | 1175.67 |
| `vlm_model_specs.PIXTRAL_12B_TRANSFORMERS` | [mistral-community/pixtral-12b](https://huggingface.co/mistral-community/pixtral-12b) | `Transformers/AutoModelForVision2Seq` | CPU | 1 | 1828.21 |

_Inference time is computed on a Macbook M3 Max using the example page `tests/data/pdf/2305.03393v1-pg9.pdf`. The comparison is done with the example [compare\_vlm\_models.py](https://docling-project.github.io/docling/examples/compare_vlm_models/)._

For choosing the model, the code snippet above can be extended as follow

```
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.pipeline.vlm_pipeline import VlmPipeline
from docling.datamodel.pipeline_options import (
    VlmPipelineOptions,
)
from docling.datamodel import vlm_model_specs

pipeline_options = VlmPipelineOptions(
    vlm_options=vlm_model_specs.SMOLDOCLING_MLX,  # <-- change the model here
)

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_cls=VlmPipeline,
            pipeline_options=pipeline_options,
        ),
    }
)

doc = converter.convert(source="FILE").document

```

### Other models

Other models can be configured by directly providing the Hugging Face `repo_id`, the prompt and a few more options.

For example:

```
from docling.datamodel.pipeline_options_vlm_model import InlineVlmOptions, InferenceFramework, TransformersModelType

pipeline_options = VlmPipelineOptions(
    vlm_options=InlineVlmOptions(
        repo_id="ibm-granite/granite-vision-3.2-2b",
        prompt="Convert this page to markdown. Do not miss any text and only output the bare markdown!",
        response_format=ResponseFormat.MARKDOWN,
        inference_framework=InferenceFramework.TRANSFORMERS,
        transformers_model_type=TransformersModelType.AUTOMODEL_VISION2SEQ,
        supported_devices=[
            AcceleratorDevice.CPU,
            AcceleratorDevice.CUDA,
            AcceleratorDevice.MPS,
            AcceleratorDevice.XPU,
        ],
        scale=2.0,
        temperature=0.0,
    )
)

```

## Remote models

Additionally to local models, the `VlmPipeline` allows to offload the inference to a remote service hosting the models. Many remote inference services are provided, the key requirement is to offer an OpenAI-compatible API. This includes vLLM, Ollama, etc.

More examples on how to connect with the remote inference services can be found in the following examples:

-   [vlm\_pipeline\_api\_model.py](https://docling-project.github.io/docling/examples/vlm_pipeline_api_model/)

---

# Model Catalog

This document provides a comprehensive overview of all models and inference engines available in Docling, organized by processing stage.

## Overview

Docling's document processing pipeline consists of multiple stages, each using specialized models and inference engines. This catalog helps you understand:

-   What stages are available for document processing
-   Which model families power each stage
-   What specific models you can use
-   Which inference engines support each model

## Stages and Models Overview

The following table shows all processing stages in Docling, their model families, and available models.

| Stage | Model Family | Models |
| --- | --- | --- |
| **Layout**  
_Document structure detection_ | Object Detection  
(RT-DETR based) | 
-   `docling-layout-heron` ⭐
-   `docling-layout-heron-101`
-   `docling-layout-egret-medium`
-   `docling-layout-egret-large`
-   `docling-layout-egret-xlarge`
-   `docling-layout-v2` (legacy)

 |
| **Inference Engine:** Transformers, ONNXRuntime (in progress) |
| **Purpose:** Detects document elements (paragraphs, tables, figures, headers, etc.) |
| **Output:** Bounding boxes with element labels (TEXT, TABLE, PICTURE, SECTION\_HEADER, etc.) |
| **OCR**  
_Text recognition_ | Multiple OCR Engines | 

-   **Auto** ⭐
-   **Tesseract** (CLI or Python bindings)
-   **EasyOCR**
-   **RapidOCR** (ONNX, OpenVINO, PaddlePaddle)
-   **macOS Vision** (native macOS)
-   **SuryaOCR**

 |
| **Inference Engines:** Engine-specific |
| **Purpose:** Extracts text from images and scanned documents |
| **Table Structure**  
_Table cell recognition_ | TableFormer | 

-   `TableFormer (accurate mode)` ⭐
-   `TableFormer (fast mode)`

 |
| **Inference Engine:** docling-ibm-models |
| **Purpose:** Recognizes table structure (rows, columns, cells) and relationships |
| **Table Structure**  
_Table cell recognition_ | Object Detection | 

-   _Work in progress_

 |
| **Inference Engine:** TBD |
| **Purpose:** Alternative approach for table structure recognition using object detection |
| **Picture Classifier**  
_Image type classification_ | Image Classifier  
(Vision Transformer) | 

-   `DocumentFigureClassifier-v2.0` ⭐

 |
| **Inference Engine:** Transformers |
| **Purpose:** Classifies pictures into categories (Chart, Diagram, Natural Image, etc.) |
| **VLM Convert**  
_Full page conversion_ | Vision-Language Models | 

-   **Granite-Docling-258M** ⭐ (DocTags)
-   **SmolDocling-256M** (DocTags)
-   **DeepSeek-OCR-3B** (Markdown, API-only)
-   **Granite-Vision-3.3-2B** (Markdown)
-   **Pixtral-12B** (Markdown)
-   **GOT-OCR-2.0** (Markdown)
-   **Phi-4-Multimodal** (Markdown)
-   **Qwen2.5-VL-3B** (Markdown)
-   **Gemma-3-12B/27B** (Markdown, MLX-only)
-   **Dolphin** (Markdown)

 |
| **Inference Engines:** Transformers, MLX, API (Ollama, LM Studio, OpenAI), vLLM, AUTO\_INLINE |
| **Purpose:** Converts entire document pages to structured formats (DocTags or Markdown) |
| **Output Formats:** DocTags (structured), Markdown (human-readable) |
| **Picture Description**  
_Image captioning_ | Vision-Language Models | 

-   **SmolVLM-256M** ⭐
-   **Granite-Vision-3.3-2B**
-   **Pixtral-12B**
-   **Qwen2.5-VL-3B**

 |
| **Inference Engines:** Transformers, MLX, API (Ollama, LM Studio), vLLM, AUTO\_INLINE |
| **Purpose:** Generates natural language descriptions of images and figures |
| **Code & Formula**  
_Code/math extraction_ | Vision-Language Models | 

-   **CodeFormulaV2** ⭐
-   **Granite-Docling-258M**

 |
| **Inference Engines:** Transformers, MLX, AUTO\_INLINE |
| **Purpose:** Extracts and recognizes code blocks and mathematical formulas |

## Inference Engines by Model Family

### Object Detection Models (Layout)

| Model | Inference Engine | Supported Devices |
| --- | --- | --- |
| All Layout models | docling-ibm-models | CPU, CUDA, MPS, XPU |

**Note:** Layout models use a specialized RT-DETR-based object detection framework from `docling-ibm-models`.

### TableFormer Models (Table Structure)

| Model | Inference Engine | Supported Devices |
| --- | --- | --- |
| TableFormer (fast) | docling-ibm-models | CPU, CUDA, XPU |
| TableFormer (accurate) | docling-ibm-models | CPU, CUDA, XPU |

**Note:** MPS is currently disabled for TableFormer due to performance issues.

### Image Classifier (Picture Classifier)

| Model | Inference Engine | Supported Devices |
| --- | --- | --- |
| DocumentFigureClassifier-v2.0 | Transformers (ViT) | CPU, CUDA, MPS, XPU |

### OCR Engines

| OCR Engine | Backend | Language Support | Notes |
| --- | --- | --- | --- |
| Tesseract | CLI or tesserocr | 100+ languages | Most widely used, good accuracy |
| EasyOCR | PyTorch | 80+ languages | GPU-accelerated, good for Asian languages |
| RapidOCR | ONNX/OpenVINO/Paddle | Multiple | Fast, multiple backend options |
| macOS Vision | Native macOS | 20+ languages | macOS only, excellent quality |
| SuryaOCR | PyTorch | 90+ languages | Modern, good for complex layouts |
| Auto | Automatic | Varies | Automatically selects best available engine |

### Vision-Language Models (VLM)

#### VLM Convert Stage

| Preset ID | Model | Parameters | Transformers | MLX | API (OpenAI-compatible) | vLLM | Output Format |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `granite_docling` | Granite-Docling-258M | 258M | ✅ | ✅ | Ollama | ❌ | DocTags |
| `smoldocling` | SmolDocling-256M | 256M | ✅ | ✅ | ❌ | ❌ | DocTags |
| `deepseek_ocr` | DeepSeek-OCR-3B | 3B | ❌ | ❌ | Ollama  
LM Studio | ❌ | Markdown |
| `granite_vision` | Granite-Vision-3.3-2B | 2B | ✅ | ❌ | Ollama  
LM Studio | ✅ | Markdown |
| `pixtral` | Pixtral-12B | 12B | ✅ | ✅ | ❌ | ❌ | Markdown |
| `got_ocr` | GOT-OCR-2.0 | \- | ✅ | ❌ | ❌ | ❌ | Markdown |
| `phi4` | Phi-4-Multimodal | \- | ✅ | ❌ | ❌ | ✅ | Markdown |
| `qwen` | Qwen2.5-VL-3B | 3B | ✅ | ✅ | ❌ | ❌ | Markdown |
| `gemma_12b` | Gemma-3-12B | 12B | ❌ | ✅ | ❌ | ❌ | Markdown |
| `gemma_27b` | Gemma-3-27B | 27B | ❌ | ✅ | ❌ | ❌ | Markdown |
| `dolphin` | Dolphin | \- | ✅ | ❌ | ❌ | ❌ | Markdown |

#### Picture Description Stage

| Preset ID | Model | Parameters | Transformers | MLX | API (OpenAI-compatible) | vLLM |
| --- | --- | --- | --- | --- | --- | --- |
| `smolvlm` | SmolVLM-256M | 256M | ✅ | ✅ | LM Studio | ❌ |
| `granite_vision` | Granite-Vision-3.3-2B | 2B | ✅ | ❌ | Ollama  
LM Studio | ✅ |
| `pixtral` | Pixtral-12B | 12B | ✅ | ✅ | ❌ | ❌ |
| `qwen` | Qwen2.5-VL-3B | 3B | ✅ | ✅ | ❌ | ❌ |

#### Code & Formula Stage

| Preset ID | Model | Parameters | Transformers | MLX |
| --- | --- | --- | --- | --- |
| `codeformulav2` | CodeFormulaV2 | \- | ✅ | ❌ |
| `granite_docling` | Granite-Docling-258M | 258M | ✅ | ✅ |

## Usage Examples

### Layout Detection

```
from docling.datamodel.pipeline_options import LayoutOptions
from docling.datamodel.layout_model_specs import DOCLING_LAYOUT_HERON

# Use Heron layout model (default)
layout_options = LayoutOptions(model_spec=DOCLING_LAYOUT_HERON)

```

### Table Structure Recognition

```
from docling.datamodel.pipeline_options import TableStructureOptions, TableFormerMode

# Use accurate mode for best quality
table_options = TableStructureOptions(
    mode=TableFormerMode.ACCURATE,
    do_cell_matching=True
)

```

### Picture Classification

```
from docling.models.stages.picture_classifier.document_picture_classifier import (
    DocumentPictureClassifierOptions
)

# Use default picture classifier
classifier_options = DocumentPictureClassifierOptions.from_preset("document_figure_classifier_v2")

```

### OCR

```
from docling.datamodel.pipeline_options import TesseractOcrOptions

# Use Tesseract with English and German
ocr_options = TesseractOcrOptions(lang=["eng", "deu"])

```

### VLM Convert (Full Page)

```
from docling.datamodel.pipeline_options import VlmConvertOptions

# Use SmolDocling with auto-selected engine
options = VlmConvertOptions.from_preset("smoldocling")

# Or force specific engine
from docling.datamodel.vlm_engine_options import MlxVlmEngineOptions
options = VlmConvertOptions.from_preset(
    "smoldocling",
    engine_options=MlxVlmEngineOptions()
)

```

### Picture Description

```
from docling.datamodel.pipeline_options import PictureDescriptionVlmOptions

# Use Granite Vision for detailed descriptions
options = PictureDescriptionVlmOptions.from_preset("granite_vision")

```

### Code & Formula Extraction

```
from docling.datamodel.pipeline_options import CodeFormulaVlmOptions

# Use specialized CodeFormulaV2 model
options = CodeFormulaVlmOptions.from_preset("codeformulav2")

```

## Additional Resources

-   [Vision Models Usage Guide](https://docling-project.github.io/docling/usage/vision_models/) - VLM-specific documentation
-   [Advanced Options](https://docling-project.github.io/docling/usage/advanced_options/) - Advanced configuration
-   [GPU Support](https://docling-project.github.io/docling/usage/gpu/) - GPU acceleration setup
-   [Supported Formats](https://docling-project.github.io/docling/usage/supported_formats/) - Input format support

## Notes

-   **DocTags Format:** Structured XML-like format optimized for document understanding
-   **Markdown Format:** Human-readable format for general-purpose conversion
-   **Model Updates:** New models are added regularly. Check the codebase for latest additions
-   **Engine Compatibility:** Not all engines work on all platforms. AUTO\_INLINE handles this automatically
-   **Performance:** Actual performance varies by hardware, document complexity, and model size

---

# GPU support

## Achieving Optimal GPU Performance with Docling

This guide describes how to maximize GPU performance for Docling pipelines. It covers device selection, pipeline differences, and provides example snippets for configuring batch size and concurrency in the VLM pipeline for both Linux and Windows.

Note

Improvements and optimizations strategies for maximizing the GPU performance is an active topic. Regularly check these guidelines for updates.

### Standard Pipeline

Enable GPU acceleration by configuring the accelerator device and concurrency options using Docling's API:

```
from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions

# Configure accelerator options for GPU
accelerator_options = AcceleratorOptions(
    device=AcceleratorDevice.CUDA,  # or AcceleratorDevice.AUTO
)

```

Batch size and concurrency for document processing are controlled for each stage of the pipeline as:

```
from docling.datamodel.pipeline_options import (
    ThreadedPdfPipelineOptions,
)

pipeline_options = ThreadedPdfPipelineOptions(
    ocr_batch_size=64,  # default 4
    layout_batch_size=64,  # default 4
    table_batch_size=4,  # currently not using GPU batching
)

```

Setting a higher `page_batch_size` will run the Docling models (in particular the layout detection stage) with a GPU batch inference mode.

#### Complete example

For a complete example see [gpu\_standard\_pipeline.py](https://docling-project.github.io/docling/examples/gpu_standard_pipeline/).

#### OCR engines

The current Docling OCR engines rely on third-party libraries, hence GPU support depends on the availability in the respective engines.

The only setup which is known to work at the moment is RapidOCR with the torch backend, which can be enabled via

```
pipeline_options = PdfPipelineOptions()
pipeline_options.ocr_options = RapidOcrOptions(
    backend="torch",
)

```

More details in the GitHub discussion [#2451](https://github.com/docling-project/docling/discussions/2451).

### VLM Pipeline

For best GPU utilization, use a local inference server. Docling supports inference servers which exposes the OpenAI-compatible chat completion endpoints. For example:

-   vllm: `http://localhost:8000/v1/chat/completions` (available only on Linux)
-   LM Studio: `http://localhost:1234/v1/chat/completions` (available both on Linux and Windows)
-   Ollama: `http://localhost:11434/v1/chat/completions` (available both on Linux and Windows)

#### Start the inference server

Here is an example on how to start the [vllm](https://docs.vllm.ai/) inference server with optimum parameters for Granite Docling.

```
vllm serve ibm-granite/granite-docling-258M \
  --host 127.0.0.1 --port 8000 \
  --max-num-seqs 512 \
  --max-num-batched-tokens 8192 \
  --enable-chunked-prefill \
  --gpu-memory-utilization 0.9

```

#### Configure Docling

Configure the VLM pipeline using Docling's VLM options:

```
from docling.datamodel.pipeline_options import VlmPipelineOptions

vlm_options = VlmPipelineOptions(
    enable_remote_services=True,
    vlm_options={
        "url": "http://localhost:8000/v1/chat/completions",  # or any other compatible endpoint
        "params": {
            "model": "ibm-granite/granite-docling-258M",
            "max_tokens": 4096,
        },
        "concurrency": 64,  # default is 1
        "prompt": "Convert this page to docling.",
        "timeout": 90,
    }
)

```

Additionally to the concurrency, we also have to set the `page_batch_size` Docling parameter. Make sure to set `settings.perf.page_batch_size >= vlm_options.concurrency`.

```
from docling.datamodel.settings import settings

settings.perf.page_batch_size = 64  # default is 4

```

#### Complete example

For a complete example see [gpu\_vlm\_pipeline.py](https://docling-project.github.io/docling/examples/gpu_vlm_pipeline/).

#### Available models

Both LM Studio and Ollama rely on llama.cpp as runtime engine. For using this engine, models have to be converted to the gguf format.

Here is a list of known models which are available in gguf format and how to use them.

TBA.

## Performance results

### Test data

|  | PDF doc | [ViDoRe V3 HR](https://huggingface.co/datasets/vidore/vidore_v3_hr) |
| --- | --- | --- |
| Num docs | 1 | 14 |
| Num pages | 192 | 1110 |
| Num tables | 95 | 258 |
| Format type | PDF | Parquet of images |

### Test infrastructure

|  | g6e.2xlarge | RTX 5090 | RTX 5070 |
| --- | --- | --- | --- |
| Description | AWS instance `g6e.2xlarge` | Linux bare metal machine | Windows 11 bare metal machine |
| CPU | 8 vCPUs, AMD EPYC 7R13 | 16 vCPU, AMD Ryzen 7 9800 | 16 vCPU, AMD Ryzen 7 9800 |
| RAM | 64GB | 128GB | 64GB |
| GPU | NVIDIA L40S 48GB | NVIDIA GeForce RTX 5090 | NVIDIA GeForce RTX 5070 |
| CUDA Version | 13.0, driver 580.95.05 | 13.0, driver 580.105.08 | 13.0, driver 581.57 |

### Results

| Pipeline | g6e.2xlarge | RTX 5090 | RTX 5070 |
| --- | --- | --- | --- |
| PDF doc | ViDoRe V3 HR | PDF doc | ViDoRe V3 HR | PDF doc | ViDoRe V3 HR |
| --- | --- | --- | --- | --- | --- |
| Standard - Inline (no OCR) | 3.1 pages/second | \- | 7.9 pages/second  
_\[cpu-only\]\* 1.5 pages/second_ | \- | 4.2 pages/second  
_\[cpu-only\]\* 1.2 pages/second_ | \- |
| Standard - Inline (with OCR) |  |  | tba | 1.6 pages/second | tba | 1.1 pages/second |
| VLM - Inference server (GraniteDocling) | 2.4 pages/second | \- | 3.8 pages/second | 3.6-4.5 pages/second | 2.0 pages/second | 2.8-3.2 pages/second |

_\* cpu-only timing computed with 16 pytorch threads._

---

# MCP server

New AI trends focus on Agentic AI, an artificial intelligence system that can accomplish a specific goal with limited supervision. Agents can act autonomously to understand, plan, and execute a specific task.

To address the integration problem, the [Model Context Protocol](https://modelcontextprotocol.io) (MCP) emerges as a popular standard for connecting AI applications to external tools.

## Docling MCP

Docling supports the development of AI agents by providing an MCP Server. It allows you to experiment with document processing in different MCP Clients. Adding [Docling MCP](https://github.com/docling-project/docling-mcp) in your favorite client is usually as simple as adding the following entry in the configuration file:

```
{
  "mcpServers": {
    "docling": {
      "command": "uvx",
      "args": [
        "--from=docling-mcp",
        "docling-mcp-server"
      ]
    }
  }
}

```

When using [Claude on your desktop](https://claude.ai/download), just edit the config file `claude_desktop_config.json` with the snippet above or the example provided [here](https://github.com/docling-project/docling-mcp/blob/main/docs/integrations/claude_desktop_config.json).

In **[LM Studio](https://lmstudio.ai/)**, edit the `mcp.json` file with the appropriate section or simply click on the button below for a direct install.

[![Add MCP Server docling to LM Studio](https://files.lmstudio.ai/deeplink/mcp-install-light.svg)](https://lmstudio.ai/install-mcp?name=docling&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyItLWZyb209ZG9jbGluZy1tY3AiLCJkb2NsaW5nLW1jcC1zZXJ2ZXIiXX0%3D)

Docling MCP also provides tools specific for some applications and frameworks. See the [Docling MCP](https://github.com/docling-project/docling-mcp) Server repository for more details. You will find examples of building agents powered by Docling capabilities and leveraging frameworks like [LlamaIndex](https://www.llamaindex.ai/), [Llama Stack](https://github.com/llamastack/llama-stack), [Pydantic AI](https://ai.pydantic.dev/), or [smolagents](https://github.com/huggingface/smolagents).

---

# Jobkit

Docling's document conversion can be executed as distributed jobs using [Docling Jobkit](https://github.com/docling-project/docling-jobkit).

This library provides:

-   Pipelines for running jobs with Kubeflow pipelines, Ray, or locally.
-   Connectors to import and export documents via HTTP endpoints, S3, or Google Drive.

## Usage

### CLI

You can run Jobkit locally via the CLI:

```
uv run docling-jobkit-local [configuration-file-path]

```

The configuration file defines:

-   Docling conversion options (e.g. OCR settings)
-   Source location of input documents
-   Target location for the converted outputs

Example configuration file:

```
options:               # Example Docling's conversion options
  do_ocr: false         
sources:               # Source location (here Google Drive)
  - kind: google_drive
    path_id: 1X6B3j7GWlHfIPSF9VUkasN-z49yo1sGFA9xv55L2hSE
    token_path: "./dev/google_drive/google_drive_token.json" 
    credentials_path: "./dev/google_drive/google_drive_credentials.json"  
target:                # Target location (here S3)
  kind: s3
  endpoint: localhost:9000
  verify_ssl: false
  bucket: docling-target
  access_key: minioadmin
  secret_key: minioadmin

```

## Connectors

Connectors are used to import documents for processing with Docling and to export results after conversion.

The currently supported connectors are:

-   HTTP endpoints
-   S3
-   Google Drive

### Google Drive

To use Google Drive as a source or target, you need to enable the API and set up credentials.

Step 1: Enable the [Google Drive API](https://console.cloud.google.com/apis/enableflow?apiid=drive.googleapis.com).

-   Go to the Google [Cloud Console](https://console.cloud.google.com/).
-   Search for “Google Drive API” and enable it.

Step 2: [Create OAuth credentials](https://developers.google.com/workspace/drive/api/quickstart/python#authorize_credentials_for_a_desktop_application).

-   Go to APIs & Services > Credentials.
-   Click “+ Create credentials” > OAuth client ID.
-   If prompted, configure the OAuth consent screen with "Audience: External".
-   Select application type: "Desktop app".
-   Create the application
-   Download the credentials JSON and rename it to `google_drive_credentials.json`.

Step 3: Add test users.

-   Go to OAuth consent screen > Test users.
-   Add your email address.

Step 4: Edit configuration file.

-   Edit `credentials_path` with your path to `google_drive_credentials.json`.
-   Edit `path_id` with your source or target location. It can be obtained from the URL as follows:
    -   Folder: `https://drive.google.com/drive/u/0/folders/1yucgL9WGgWZdM1TOuKkeghlPizuzMYb5` > folder id is `1yucgL9WGgWZdM1TOuKkeghlPizuzMYb5`.
    -   File: `https://docs.google.com/document/d/1bfaMQ18_i56204VaQDVeAFpqEijJTgvurupdEDiaUQw/edit` > document id is `1bfaMQ18_i56204VaQDVeAFpqEijJTgvurupdEDiaUQw`.

Step 5: Authenticate via CLI.

-   Run the CLI with your configuration file.
-   A browser window will open for authentication and gerate a token file that will be save on the configured `token_path` and reused for next runs.