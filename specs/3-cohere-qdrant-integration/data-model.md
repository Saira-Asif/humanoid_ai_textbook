# Data Model: Cohere-Qdrant RAG Backend

**Feature**: 3-cohere-qdrant-integration
**Date**: 2025-12-16
**Status**: Complete
**Author**: Claude Code

## Overview

This document defines the data structures and models used in the Cohere-Qdrant RAG backend system. The system processes textbook content from the deployed site, converts it to embeddings, and stores it in Qdrant for retrieval.

## Entity Models

### 1. ContentChunk Entity

**Description**: Represents a chunk of text extracted from a URL, processed for embedding

**Fields**:
- `id` (string): Unique identifier for the chunk (UUID or content-based hash)
- `url` (string): Original source URL of the content
- `title` (string): Title/heading of the content section
- `content` (string): The actual text content of the chunk
- `chunk_index` (integer): Sequential index of this chunk within the original document
- `total_chunks` (integer): Total number of chunks from the original document
- `created_at` (datetime): Timestamp when the chunk was created
- `word_count` (integer): Number of words in the chunk
- `token_count` (integer): Number of tokens in the chunk (estimated)
- `metadata` (object): Additional metadata from the source page

**Relationships**:
- Belongs to one source URL
- Part of a sequence of chunks from the same document

### 2. Embedding Entity

**Description**: Represents the vector embedding of a content chunk

**Fields**:
- `chunk_id` (string): Reference to the ContentChunk this embedding represents
- `vector` (array[float]): The embedding vector (1024 dimensions for Cohere v3)
- `model` (string): The embedding model used (e.g., "embed-multilingual-v3.0")
- `created_at` (datetime): Timestamp when the embedding was generated

**Relationships**:
- Associated with one ContentChunk
- Stored in Qdrant collection

### 3. ProcessedURL Entity

**Description**: Represents a URL that has been processed and its content extracted

**Fields**:
- `url` (string): The URL that was processed
- `title` (string): Title of the page
- `status` (string): Processing status (e.g., "processed", "failed", "skipped")
- `chunk_count` (integer): Number of chunks created from this URL
- `processed_at` (datetime): Timestamp when processing was completed
- `error_message` (string, optional): Error message if processing failed
- `word_count` (integer): Total word count of the page content

**Relationships**:
- Contains multiple ContentChunk entities

## Qdrant Collection Schema

### Collection: `rag_embedding`

**Configuration**:
- Vector size: 1024 (for Cohere embed-multilingual-v3.0)
- Distance: Cosine
- HNSW enabled for fast search

**Payload Structure**:
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

**Points Structure**:
- ID: Unique identifier for the chunk
- Vector: 1024-dimensional embedding vector
- Payload: Metadata as defined above

## Data Flow

### 1. URL Discovery → ProcessedURL
- Input: Base URL (https://humanoid-ai-textbook.vercel.app/)
- Process: Crawl and discover all accessible URLs
- Output: List of ProcessedURL entities with status "pending"

### 2. Content Extraction → ContentChunk
- Input: ProcessedURL with status "pending"
- Process: Extract clean text, split into chunks
- Output: Multiple ContentChunk entities linked to the URL

### 3. Embedding Generation → Embedding
- Input: ContentChunk entities
- Process: Generate embeddings using Cohere API
- Output: Embedding entities with vector data

### 4. Storage → Qdrant Collection
- Input: ContentChunk + Embedding data
- Process: Store in Qdrant with metadata
- Output: Vector points in `rag_embedding` collection

## Validation Rules

### ContentChunk Validation
- `content` must be non-empty and less than 500 tokens
- `url` must be a valid URL format
- `chunk_index` must be >= 0 and < `total_chunks`
- `word_count` and `token_count` must be positive integers

### Embedding Validation
- `vector` must have exactly 1024 dimensions
- `model` must be a supported Cohere model
- `chunk_id` must reference an existing ContentChunk

### ProcessedURL Validation
- `url` must be a valid URL format
- `status` must be one of: "processed", "failed", "skipped", "pending"
- `chunk_count` must be >= 0

## State Transitions

### ProcessedURL States
```
pending → processing → processed
              ↓
            failed
```

### ContentChunk States
```
created → embedding → embedded
              ↓
            failed
```

## Indexing Strategy

### Qdrant Indexes
- Primary index on `url` field for document-based queries
- Secondary index on `title` field for title-based searches
- Payload index on `created_at` for time-based queries
- Keyword index on `source_metadata.tags` for categorical searches

### Search Optimization
- Use HNSW index for fast vector similarity search
- Implement payload filtering for metadata-based constraints
- Configure ef_search parameter (32-128) for performance vs accuracy trade-off

## Data Integrity

### Consistency Checks
- Each embedding must have a corresponding ContentChunk
- Chunk sequence must be complete for each URL (no missing indices)
- Vector dimensions must match expected size (1024)
- URLs in Qdrant must match original ProcessedURL entries

### Backup Strategy
- Qdrant collections can be backed up using Qdrant's snapshot functionality
- ProcessedURL and ContentChunk records can be exported as JSON for backup
- Embedding vectors are regenerated from source content if needed

## Performance Considerations

### Size Limits
- Individual content chunks should be < 500 tokens to fit Cohere limits
- Batch operations should limit to 96 items per Cohere request
- Qdrant payload should be < 1MB per point for optimal performance

### Memory Management
- Stream large documents to avoid memory overflow
- Process chunks in batches to manage memory usage
- Use generators where possible for large data sets