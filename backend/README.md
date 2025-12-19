# Cohere-Qdrant RAG Backend

This backend service extracts content from the Humanoid AI Textbook site, generates embeddings using Cohere, and stores them in Qdrant vector database for RAG (Retrieval-Augmented Generation) functionality.

## Overview

The system processes textbook content from the deployed site, converts it to embeddings, and stores it in Qdrant for semantic search and retrieval. It implements the following pipeline:
1. Discover all URLs from the textbook site
2. Extract clean text content from each URL
3. Split documents into semantically coherent chunks
4. Generate vector embeddings using Cohere API
5. Store embeddings with metadata in Qdrant vector database

## Prerequisites

- Python 3.10+
- UV package manager
- Cohere API key
- Qdrant database instance (cloud or local)

## Installation

1. Install UV package manager:
```bash
pip install uv
```

2. Install project dependencies:
```bash
cd backend
uv sync  # This will install dependencies from pyproject.toml
```

## Configuration

Create a `.env` file in the project root with the following variables:

```env
COHERE_API_KEY=your_cohere_api_key_here
QDRANT_URL=your_qdrant_url_here
QDRANT_API_KEY=your_qdrant_api_key_here  # Required for cloud instances
SOURCE_URL=https://humanoid-ai-textbook.vercel.app/
COHERE_MODEL=embed-multilingual-v3.0  # Optional: defaults to embed-multilingual-v3.0
COHERE_INPUT_TYPE=search_document  # Optional: defaults to search_document
QDRANT_COLLECTION_NAME=rag_embedding  # Optional: defaults to rag_embedding
CHUNK_SIZE_TOKENS=250  # Optional: defaults to 250
CHUNK_OVERLAP_TOKENS=20  # Optional: defaults to 20
BATCH_SIZE=10  # Optional: defaults to 10
RATE_LIMIT_DELAY=0.1  # Optional: defaults to 0.1
```

## Usage

### Basic Usage
Run the main script to process the textbook content:

```bash
python main.py
```

### Command Line Options
The script supports various command-line options for customization:

```bash
python main.py --source-url https://example.com --collection-name my_collection --chunk-size 300 --limit-urls 5
```

Available options:
- `--source-url`: Source URL to process (default: from .env)
- `--collection-name`: Qdrant collection name (default: from .env)
- `--chunk-size`: Chunk size in tokens (default: from .env)
- `--limit-urls`: Limit number of URLs to process (for testing)

### Example Usage Scenarios

#### Process all content from the textbook site:
```bash
python main.py
```

#### Process only a limited number of URLs for testing:
```bash
python main.py --limit-urls 3
```

#### Process content with custom chunk size:
```bash
python main.py --chunk-size 350
```

#### Process different source URL:
```bash
python main.py --source-url https://my-site.com
```

## Architecture

The system is implemented in a single `main.py` file with the following functions:

### Core Functions
- `get_all_urls()`: Discover all pages from the textbook site (with sitemap support and crawling fallback)
- `extract_text_from_url()`: Extract clean text from a URL (with metadata extraction)
- `chunk_text()`: Split text into manageable chunks (with configurable size and overlap)
- `embed()`: Generate embeddings using Cohere (with batching and rate limiting)
- `create_collection()`: Create Qdrant collection named `rag_embedding`
- `save_chunk_to_qdrant()`: Store chunk with embedding in Qdrant (with retry logic)

### Supporting Functions
- `validate_environment()`: Validate required environment variables
- `initialize_cohere_client()`: Initialize Cohere client with validation
- `initialize_qdrant_client()`: Initialize Qdrant client with validation
- `add_cli_arguments()`: Parse command-line arguments
- `validate_config()`: Validate configuration values
- `configure_logging()`: Set up logging

## Features

### Error Handling
- Comprehensive error handling with logging
- Retry logic for API calls and storage operations
- Graceful degradation when individual URLs fail

### Performance Optimization
- Batch processing for embeddings (up to 96 items per request)
- Rate limiting to respect API quotas
- Progress tracking with tqdm
- Memory-efficient processing

### Data Integrity
- Complete metadata preservation
- Duplicate handling in Qdrant
- Validation of embedding dimensions (1024 for Cohere v3)
- Content filtering to remove navigation elements

### Configuration
- Environment variable-based configuration
- Command-line argument support
- Validation of configuration values
- Flexible parameter adjustment

## Output

The system generates:
- A Qdrant collection named `rag_embedding` with:
  - 1024-dimensional embedding vectors
  - Complete metadata including URL, title, content, chunk info
  - Proper indexing for fast search
- Detailed logs in `rag_backend.log`
- Progress tracking in console output
- Summary statistics at completion

## Testing

To test with a small subset of URLs:
```bash
python main.py --limit-urls 5
```

This allows for quick validation without processing the entire site.

## Performance Metrics

The system tracks and reports:
- Number of URLs processed
- Number of content chunks created
- Processing time
- Processing rate (chunks per minute)
- Any validation warnings or errors