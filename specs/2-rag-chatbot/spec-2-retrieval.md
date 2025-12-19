# Specification: 2-rag-chatbot - Retrieval Pipeline

**Feature**: Textbook RAG Chatbot - Retrieval Pipeline
**Date**: 2025-12-17
**Status**: Draft
**Author**: Claude Code

## Overview

This specification defines the retrieval pipeline for the textbook RAG chatbot system. The retrieval module will query the Qdrant vector database to find relevant content chunks based on semantic similarity to user queries. The system will support various query types including standard semantic search, filtered search by module, and selected-text context queries.

## Requirements

### Functional Requirements

#### R1: Semantic Search
- The system SHALL perform semantic search against the Qdrant vector database
- The system SHALL return top-K most relevant content chunks (K configurable between 3-10)
- The system SHALL return relevance scores for each retrieved chunk
- The system SHALL include source metadata (URL, title, chunk index, etc.) with each result

#### R2: Module-Level Filtering
- The system SHALL support filtering search results by specific textbook modules (e.g., "module-1-ros2")
- The system SHALL allow users to specify one or more modules to search within
- The system SHALL exclude results from modules not specified in the filter

#### R3: Selected-Text Queries
- The system SHALL support queries that combine user-selected text with retrieved context
- The system SHALL be able to use selected text as the basis for semantic search
- The system SHALL return contextually relevant chunks that complement the selected text

#### R4: Performance Requirements
- The system SHALL achieve query response times under 200ms for typical searches
- The system SHALL handle concurrent queries efficiently
- The system SHALL maintain consistent performance across different query types

### Non-Functional Requirements

#### NFR1: Technology Stack
- Language: Python 3.10+
- Vector Database: Qdrant client
- Embedding Service: Cohere embeddings (compatible with embeddings from Spec 1)
- Testing: pytest framework

#### NFR2: Query Types Support
- Standard semantic search (user query → relevant chunks)
- Filtered search (user query + module filter → relevant chunks from specific modules)
- Selected-text context (selected text → relevant complementary chunks)

#### NFR3: Constraints
- No re-ranking models (use Qdrant scores directly)
- Must work with embeddings created by Spec 1 pipeline
- Command-line interactive tester for manual validation
- Direct Qdrant queries only (no caching layer)

## Architecture

### Components

#### TextbookRetriever Class
The main retrieval class that encapsulates all retrieval functionality:

**Methods:**
- `search(query: str, top_k: int = 5, filters: dict = None) -> List[RetrievalResult]`
- `search_by_module(query: str, module_ids: List[str], top_k: int = 5) -> List[RetrievalResult]`
- `search_with_selection(selected_text: str, context_query: str = None, top_k: int = 5) -> List[RetrievalResult]`
- `validate_connection() -> bool`

**Attributes:**
- `qdrant_client`: Qdrant client instance
- `collection_name`: Name of the Qdrant collection ("rag_embedding")
- `cohere_client`: Cohere client for query embedding (optional, if needed for advanced queries)

#### RetrievalResult Class
Data class representing a single retrieval result:

**Attributes:**
- `content`: The retrieved text content
- `url`: Source URL of the content
- `title`: Title of the source document
- `relevance_score`: Semantic similarity score (from Qdrant)
- `chunk_index`: Position of this chunk within the original document
- `total_chunks`: Total number of chunks in the original document
- `metadata`: Additional source metadata

### Data Flow

1. User provides query text
2. Query is embedded using Cohere (or existing embedding service)
3. Vector search is performed against Qdrant collection
4. Results are filtered (if module filters are specified)
5. Results are scored and ranked by Qdrant
6. Top-K results are returned with metadata

## Implementation Plan

### Phase 1: Core Retrieval Module
- Implement TextbookRetriever class with basic search functionality
- Connect to Qdrant collection and perform vector similarity search
- Return results with relevance scores and metadata

### Phase 2: Filtering Support
- Add module-level filtering capability
- Implement search_by_module method
- Support multiple module filters

### Phase 3: Selected-Text Queries
- Add search_with_selection method
- Handle selected text as query input
- Combine with optional context queries

### Phase 4: Performance and Testing
- Optimize for <200ms response time
- Add comprehensive test coverage
- Create interactive CLI tester

## Testing Strategy

### Test Cases

#### TC1: Basic Semantic Search
- Input: Simple query text
- Expected: Top-K relevant chunks with proper metadata
- Validation: Check content relevance, metadata completeness

#### TC2: Module Filtering
- Input: Query + specific module filter
- Expected: Results only from specified modules
- Validation: Verify module filtering works correctly

#### TC3: Performance Test
- Input: Multiple queries in sequence
- Expected: Response time <200ms
- Validation: Measure and verify performance requirements

#### TC4: Selected-Text Queries
- Input: Selected text for context
- Expected: Relevant complementary content
- Validation: Check contextual relevance

#### TC5: Error Handling
- Input: Invalid queries, connection failures
- Expected: Graceful error handling
- Validation: Proper exception handling and messages

## Dependencies

- Qdrant vector database (already populated by Spec 1 pipeline)
- Cohere API (for query embedding if needed)
- Python 3.10+ runtime environment
- Existing embedding collection in Qdrant ("rag_embedding")

## Success Criteria

- [ ] TextbookRetriever class successfully retrieves relevant content
- [ ] Top-K parameter works correctly (configurable 3-10 results)
- [ ] Module filtering restricts results to specified modules
- [ ] Selected-text queries return contextual results
- [ ] Query response time <200ms for typical searches
- [ ] All test cases pass (5+ pytest test cases)
- [ ] Interactive CLI tester validates functionality manually
- [ ] Results include proper relevance scores and metadata