# Feature Specification: Cohere-Qdrant RAG Backend

**Feature**: 3-cohere-qdrant-integration
**Date**: 2025-12-16
**Status**: Draft
**Author**: Claude Code

## Overview

Create a backend service that extracts content from the deployed textbook site, generates embeddings using Cohere, and stores them in Qdrant vector database for RAG (Retrieval-Augmented Generation) functionality.

## Requirements

### Functional Requirements

1. **URL Content Extraction**: Extract all URLs from the deployed textbook site `https://humanoid-ai-textbook.vercel.app/`
2. **Text Processing**: Extract clean text content from each URL
3. **Content Chunking**: Split large documents into smaller, semantically coherent chunks
4. **Embedding Generation**: Generate vector embeddings using Cohere's embedding API
5. **Vector Storage**: Store embeddings in Qdrant vector database with metadata
6. **Collection Management**: Create and manage Qdrant collection named `rag_embedding`

### Technical Requirements

1. **Package Management**: Use UV package manager for Python dependencies
2. **Single File Implementation**: All functionality in a single `main.py` file
3. **System Design**: Implement functions as specified:
   - `get_all_urls` - Discover all URLs from the site
   - `extract_text_from_url` - Extract clean text from a URL
   - `chunk_text` - Split text into manageable chunks
   - `embed` - Generate embeddings using Cohere
   - `create_collection` - Create Qdrant collection named `rag_embedding`
   - `save_chunk_to_qdrant` - Store chunk with embedding in Qdrant
4. **Main Execution**: Execute all functions in the main function

### Performance Requirements

1. **Response Time**: Individual embedding generation should be under 2 seconds
2. **Throughput**: Process at least 10 pages per minute
3. **Memory Usage**: Efficient memory management for large documents

### Quality Requirements

1. **Error Handling**: Graceful handling of network errors, API failures, and malformed content
2. **Data Integrity**: Preserve content structure and metadata during processing
3. **Retry Logic**: Implement retry mechanisms for transient failures

## Architecture

### Components

1. **URL Discovery Module**: Discovers all pages from the textbook site
2. **Content Extraction Module**: Extracts clean text from HTML content
3. **Text Processing Module**: Chunks text appropriately for embedding
4. **Embedding Module**: Interfaces with Cohere API for vector generation
5. **Storage Module**: Interfaces with Qdrant for vector storage
6. **Main Orchestrator**: Coordinates the entire pipeline

### Technology Stack

- **Language**: Python 3.10+
- **Package Manager**: UV
- **Embedding Service**: Cohere API
- **Vector Database**: Qdrant
- **HTTP Client**: requests/httpx for content extraction
- **HTML Parser**: BeautifulSoup for content extraction

## Acceptance Criteria

- [ ] Successfully discovers all URLs from `https://humanoid-ai-textbook.vercel.app/`
- [ ] Extracts clean text content from each URL without HTML tags
- [ ] Chunks text into appropriate sizes for Cohere embeddings
- [ ] Generates embeddings using Cohere API successfully
- [ ] Creates Qdrant collection named `rag_embedding`
- [ ] Stores all chunks with embeddings and metadata in Qdrant
- [ ] Single `main.py` file contains all required functionality
- [ ] Main function orchestrates the complete pipeline
- [ ] Handles errors gracefully with appropriate logging