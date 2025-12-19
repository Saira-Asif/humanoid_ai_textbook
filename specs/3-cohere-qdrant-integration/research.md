# Research Document: Cohere-Qdrant RAG Backend

**Feature**: 3-cohere-qdrant-integration
**Date**: 2025-12-16
**Status**: Complete
**Author**: Claude Code

## Executive Summary

This research document provides the technical foundation for implementing a backend service that extracts content from the deployed textbook site, generates embeddings using Cohere, and stores them in Qdrant vector database. The research covers API capabilities, optimal implementation strategies, and technical considerations for the RAG pipeline.

## Cohere API Research

### Embedding Models
- **Recommended Model**: `embed-multilingual-v3.0`
  - Vector dimensions: 1024
  - Supports 10+ languages
  - Optimized for retrieval tasks
  - Max input length: 512 tokens per request (for v3 models)

### API Rate Limits & Pricing
- **Rate Limits**: Varies by account type, typically 100-1000 RPM for free/pro accounts
- **Pricing**: $0.003 per 1,000 tokens (as of 2024)
- **Input Types**:
  - `search_document` for storage (recommended for textbook content)
  - `search_query` for retrieval

### Best Practices
- Batch requests when possible (up to 96 texts per request)
- Handle rate limits with exponential backoff
- Optimize chunk sizes to under 500 tokens for efficiency
- Use appropriate input_type for documents vs queries

### Error Handling
- Common errors: `TooManyRequestsError`, `AuthenticationError`, `BadRequestError`
- Implement retry logic with exponential backoff
- Log detailed error information for debugging

## Qdrant Vector Database Research

### Collection Configuration
- **Vector Dimensions**: 1024 (matches Cohere v3 embeddings)
- **Distance Function**: Cosine (default, suitable for embeddings)
- **HNSW Index**: Enabled by default for fast approximate search
- **Payload Storage**: Supports metadata storage with vectors

### Client Libraries
- **Python Client**: `qdrant-client` package
- **Connection Options**: Cloud instance, local instance, or cluster
- **Authentication**: API key for cloud instances

### Performance Considerations
- **ef_search**: 32-128 for query performance (higher = more accurate but slower)
- **Batch Operations**: Efficient bulk upsert operations
- **Point IDs**: Use meaningful IDs for document tracking

### Data Model
- **Vectors**: Embedding vectors (1024 dimensions for Cohere v3)
- **Payload**: Metadata including source URL, content chunk, document title, etc.
- **Collection**: Named `rag_embedding` as specified

## Content Extraction Research

### URL Discovery Methods
- **Sitemap**: Check for `sitemap.xml` or `sitemap_index.xml`
- **Crawling**: Use requests to get HTML and parse for links
- **API**: Check if site has a content API (less likely for static sites)

### Text Extraction Techniques
- **BeautifulSoup**: Most reliable for HTML parsing
- **Selector Strategy**: Target main content areas, exclude navigation and ads
- **Content Filtering**: Remove duplicate content, navigation elements, footers

### Text Cleaning
- Remove HTML tags while preserving content structure
- Handle special characters and encoding issues
- Preserve important formatting like headings and lists

## Text Chunking Strategies

### Optimal Chunk Sizes
- **Recommended Range**: 150-300 tokens per chunk
- **Maximum**: Under 500 tokens to stay within Cohere limits
- **Semantic Boundaries**: Break at paragraph or section boundaries
- **Overlap**: 20-50 token overlap to maintain context

### Chunking Approaches
1. **Fixed Token Count**: Simple but may break semantic context
2. **Semantic Boundaries**: Break at paragraph/section boundaries (preferred)
3. **Sliding Window**: Overlapping chunks for better context recovery

### Academic Content Considerations
- Maintain section headings with content
- Preserve code examples with surrounding context
- Keep related concepts together
- Handle mathematical formulas as single units

## Implementation Architecture

### Function Design
Based on research, the following functions will be implemented:

1. **get_all_urls()**: Use requests to crawl site or parse sitemap
2. **extract_text_from_url()**: BeautifulSoup for HTML parsing and text extraction
3. **chunk_text()**: Semantic boundary detection with configurable chunk size
4. **embed()**: Cohere API integration with rate limit handling
5. **create_collection()**: Qdrant collection setup with proper configuration
6. **save_chunk_to_qdrant()**: Vector storage with metadata

### Error Handling Strategy
- Network errors: Retry with exponential backoff
- API errors: Handle rate limits and authentication issues
- Content errors: Skip problematic pages, continue processing
- Database errors: Queue failed items for retry

### Performance Optimizations
- Batch embedding requests (up to 96 texts per request)
- Parallel URL processing (with rate limiting)
- Efficient memory management for large documents
- Connection pooling for HTTP requests

## Security Considerations

### API Key Management
- Store in environment variables (not in code)
- Use python-dotenv for configuration
- Never commit API keys to version control

### Data Privacy
- Text content sent to Cohere API for embedding
- Consider data residency requirements
- Review Cohere's data usage policies

## Dependencies & Setup

### Required Packages
- `cohere`: For embedding generation
- `qdrant-client`: For vector database operations
- `requests`: For HTTP operations
- `beautifulsoup4`: For HTML parsing
- `python-dotenv`: For environment management
- `tqdm`: For progress indication (optional but recommended)

### Environment Variables
- `COHERE_API_KEY`: Cohere API authentication
- `QDRANT_URL`: Qdrant instance URL
- `QDRANT_API_KEY`: Qdrant authentication (if cloud instance)
- `TARGET_URL`: Base URL to process (https://humanoid-ai-textbook.vercel.app/)

## Risk Assessment

### Technical Risks
- **API Rate Limits**: Implement proper rate limiting and retry logic
- **Large Documents**: Implement streaming/chunked processing to manage memory
- **Network Issues**: Implement robust retry mechanisms
- **Content Structure Changes**: Site layout changes may break extraction

### Mitigation Strategies
- Comprehensive error handling and logging
- Configurable parameters for different scenarios
- Graceful degradation when components fail
- Regular monitoring and validation

## References

- Cohere API Documentation: https://docs.cohere.com/
- Qdrant Documentation: https://qdrant.tech/documentation/
- BeautifulSoup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Python Requests Documentation: https://requests.readthedocs.io/