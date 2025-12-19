# Data Model: RAG Chatbot

**Feature**: 2-rag-chatbot
**Date**: 2025-12-16
**Status**: Complete
**Author**: Claude Code

## Overview

This document defines the data structures and models used in the RAG chatbot system. The system processes textbook content from the deployed site, converts it to embeddings, and stores it in Qdrant for retrieval.

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

### Collection: `rag_emedding`

**Configuration**:
- Vector size: 1024 (for Cohere embed-multilingual-v3.0)
- Distance: Cosine
- HNSW enabled for fast search

**Payload Structure**:
```json
{
  "document_id": "unique identifier for the source document",
  "chunk_id": "unique identifier for this specific chunk",
  "url": "source URL of the document",
  "title": "page/document title",
  "content": "the actual text content of the chunk",
  "chunk_index": "position of this chunk within the document",
  "total_chunks": "total number of chunks in the document",
  "word_count": "number of words in this chunk",
  "char_count": "number of characters in this chunk",
  "last_modified": "ISO 8601 timestamp of content modification",
  "created_at": "ISO 8601 timestamp of vector creation",
  "section_hierarchy": {
    "chapter": "Chapter title/ID",
    "section": "Section title/ID",
    "subsection": "Subsection title/ID",
    "level": "depth level in document hierarchy"
  },
  "breadcrumbs": ["Chapter 1", "Section 1.1", "Subsection 1.1.1"],
  "tags": ["relevant_tags", "extracted_from_content"],
  "entities": ["named_entities", "detected_in_chunk"],
  "categories": ["document_category", "domain_specific"],
  "difficulty_level": "beginner|intermediate|advanced",
  "technical_depth": "conceptual|practical|theoretical",
  "content_type": "text|code|equation|table|figure_caption",
  "language": "en|es|fr|etc.",
  "embedding_model": "cohere/embed-multilingual-v3.0",
  "embedding_version": "v1",
  "quality_score": "0.0-1.0 confidence score for content quality"
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
- Output: Vector points in `rag_emedding` collection

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
- Keyword index on `tags` field for categorical searches

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