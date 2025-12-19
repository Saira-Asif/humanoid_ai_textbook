# Configuration Contract: Cohere-Qdrant RAG Backend

**Feature**: 3-cohere-qdrant-integration
**Date**: 2025-12-16
**Status**: Complete
**Author**: Claude Code

## Overview

This document specifies the configuration interface and external service contracts for the Cohere-Qdrant RAG backend. Since this is a command-line application rather than a web API, the "contracts" define the expected configuration parameters, external service interfaces, and data exchange formats.

## Environment Configuration Contract

### Required Environment Variables

#### Cohere API Configuration
```env
COHERE_API_KEY = "string"  # Required: Cohere API key for embedding generation
COHERE_MODEL = "string"    # Optional: Embedding model (default: "embed-multilingual-v3.0")
COHERE_INPUT_TYPE = "string"  # Optional: Input type (default: "search_document")
```

#### Qdrant Database Configuration
```env
QDRANT_URL = "string"      # Required: Qdrant instance URL (e.g., "https://your-cluster.qdrant.io:6333")
QDRANT_API_KEY = "string"  # Required for cloud instances: Qdrant API key
QDRANT_COLLECTION_NAME = "string"  # Optional: Collection name (default: "rag_embedding")
```

#### Source Configuration
```env
SOURCE_URL = "string"      # Required: Base URL to process (default: "https://humanoid-ai-textbook.vercel.app/")
```

#### Processing Configuration
```env
CHUNK_SIZE_TOKENS = "integer"     # Optional: Max tokens per chunk (default: 250)
CHUNK_OVERLAP_TOKENS = "integer"  # Optional: Token overlap between chunks (default: 20)
BATCH_SIZE = "integer"            # Optional: Batch size for API calls (default: 10)
RATE_LIMIT_DELAY = "float"        # Optional: Delay between API calls in seconds (default: 0.1)
```

### Default Values
- `COHERE_MODEL`: "embed-multilingual-v3.0"
- `COHERE_INPUT_TYPE`: "search_document"
- `QDRANT_COLLECTION_NAME`: "rag_embedding"
- `SOURCE_URL`: "https://humanoid-ai-textbook.vercel.app/"
- `CHUNK_SIZE_TOKENS`: 250
- `CHUNK_OVERLAP_TOKENS`: 20
- `BATCH_SIZE`: 10
- `RATE_LIMIT_DELAY`: 0.1

## External Service Interfaces

### Cohere API Interface Contract

#### Function: `cohere.embed()`
**Input**:
- `texts`: List[string] - List of text chunks to embed (max 96 items)
- `model`: string - Embedding model name
- `input_type`: string - Type of input ("search_document", "search_query")

**Output**:
- `embeddings`: List[List[float]] - List of embedding vectors (each 1024-dimensional)
- `meta`: object - API metadata including usage statistics

**Error Conditions**:
- `429`: Rate limit exceeded - implement exponential backoff
- `401`: Invalid API key - terminate with error message
- `400`: Bad request - invalid input - skip chunk and log error

#### Rate Limiting Contract
- Maximum 1000 requests per minute (varies by account)
- Implement exponential backoff starting at 1 second
- Retry up to 3 times before skipping content

### Qdrant API Interface Contract

#### Function: `qdrant.create_collection()`
**Input**:
- `collection_name`: string - Name of collection to create
- `vector_size`: integer - Size of vectors (1024 for Cohere v3)
- `distance`: string - Distance metric ("Cosine", "Euclid", etc.)

**Output**:
- Success: boolean indicating creation status
- Error: Exception with details

#### Function: `qdrant.upsert_points()`
**Input**:
- `collection_name`: string - Target collection
- `points`: List[PointStruct] - Points to upsert with vectors and payloads

**PointStruct**:
- `id`: string - Unique point identifier
- `vector`: List[float] - 1024-dimensional embedding vector
- `payload`: object - Metadata object with content details

**Output**:
- Success: boolean indicating upsert status
- Error: Exception with details

#### Expected Payload Structure
```json
{
  "chunk_id": "string",
  "url": "string",
  "title": "string",
  "content": "string",
  "chunk_index": "integer",
  "total_chunks": "integer",
  "word_count": "integer",
  "token_count": "integer",
  "created_at": "datetime_string",
  "source_metadata": {
    "og_title": "string",
    "og_description": "string",
    "h1": "string",
    "tags": ["string"]
  }
}
```

## Internal Function Interface Contracts

### Function: `get_all_urls()`
**Input**: None (uses SOURCE_URL from config)
**Output**: List[string] - List of all discovered URLs from the site
**Contract**:
- Returns only valid HTTP/HTTPS URLs
- Filters out external links, images, CSS, JS files
- Handles both sitemap discovery and web crawling
- Returns URLs in discovery order

### Function: `extract_text_from_url(url: string)`
**Input**: `url` - Valid URL string to extract content from
**Output**:
- `title`: string - Page title
- `content`: string - Clean text content extracted from page
- `metadata`: object - Additional metadata from page (og tags, etc.)
**Contract**:
- Removes HTML tags while preserving content structure
- Extracts title from `<title>` or `<h1>` tags
- Handles common HTML structures for documentation sites
- Returns empty content for non-HTML resources

### Function: `chunk_text(content: string, title: string, url: string)`
**Input**:
- `content`: Text content to chunk
- `title`: Title of the source document
- `url`: Source URL for metadata
**Output**: List[ContentChunk] - List of content chunks
**Contract**:
- Each chunk is between 100-500 tokens (configurable)
- Preserves semantic boundaries (paragraphs, sections)
- Maintains reference to source URL and document structure
- Includes overlap between chunks if configured

### Function: `embed(texts: List[string])`
**Input**: `texts` - List of text chunks to embed (max batch size from config)
**Output**: List[List[float]] - List of embedding vectors
**Contract**:
- Respects Cohere API rate limits
- Handles API errors gracefully
- Returns embeddings in same order as input texts
- Implements retry logic for transient failures

### Function: `create_collection(collection_name: string)`
**Input**: `collection_name` - Name for the Qdrant collection
**Output**: boolean - Success status
**Contract**:
- Creates collection with 1024-dimensional vectors
- Uses Cosine distance metric
- Configures HNSW index for fast search
- Handles collection already existing

### Function: `save_chunk_to_qdrant(chunk: ContentChunk, embedding: List[float])`
**Input**:
- `chunk`: Content chunk with metadata
- `embedding`: 1024-dimensional embedding vector
**Output**: boolean - Success status
**Contract**:
- Stores vector with complete metadata payload
- Uses chunk ID as point ID in Qdrant
- Handles duplicate IDs appropriately
- Implements retry logic for transient failures

## Data Exchange Formats

### Input Data Format
- Source: HTML pages from documentation site
- Format: Standard HTML with common documentation structures
- Encoding: UTF-8

### Processing Data Format
- Text chunks: Plain text with preserved formatting
- Metadata: JSON-compatible object structure
- Embeddings: Array of 1024 float values

### Output Data Format
- Qdrant payload: JSON object with structured metadata
- Vector storage: 1024-dimensional float array
- Collection: Named vector collection in Qdrant

## Error Handling Contract

### Error Types and Responses
- **NetworkError**: Retry with exponential backoff (max 3 attempts)
- **APIError**: Log error, skip content, continue processing
- **ValidationError**: Log error, skip invalid content, continue
- **AuthenticationError**: Terminate with clear error message
- **RateLimitError**: Wait and retry, implement backoff strategy

### Logging Contract
- All errors logged with timestamp and context
- Progress updates logged at configurable intervals
- Summary statistics logged at completion
- Failed URLs tracked separately for review

## Performance Contract

### Expected Performance Metrics
- URL discovery: < 30 seconds for complete site
- Content extraction: < 5 seconds per page (average)
- Embedding generation: < 2 seconds per chunk (with rate limiting)
- Vector storage: < 1 second per chunk

### Resource Usage Limits
- Memory usage: < 500MB during processing (with streaming)
- Concurrent connections: Max 5 for web requests
- API requests: Within rate limits (configurable delay)

## Validation Contract

### Pre-execution Validation
- All required environment variables present
- API keys are valid format (basic validation)
- Source URL is accessible
- Qdrant connection is available

### Post-execution Validation
- All discovered URLs processed or logged as failed
- Qdrant collection contains expected number of vectors
- No duplicate vectors stored
- Metadata integrity maintained