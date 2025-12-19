# ADR-005: Cohere-Qdrant Vector Search Stack Selection

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Search Stack" not separate ADRs for embedding model, vector database).

- **Status:** Accepted
- **Date:** 2025-12-16
- **Feature:** 2-rag-chatbot
- **Context:** The Physical AI & Humanoid Robotics textbook requires a RAG (Retrieval-Augmented Generation) chatbot to provide semantic search capabilities over the textbook content. The decision affects how content is indexed, searched, and retrieved for student queries, with performance requirements of <200ms response time and academic-quality semantic understanding.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

We will implement a Cohere-Qdrant vector search stack featuring:

- **Embedding Model**: Cohere's embed-multilingual-v3.0 for semantic representation
- **Vector Database**: Qdrant Cloud for storage and similarity search
- **Search Strategy**: Semantic similarity search with HNSW indexing
- **Performance Target**: <200ms response time for real-time interactions
- **Content Processing**: Text extraction from Docusaurus URLs with metadata preservation
- **Chunking Strategy**: 150-300 token chunks optimized for Cohere embeddings

## Consequences

### Positive

- **High-Quality Embeddings**: Cohere provides state-of-the-art semantic understanding with multilingual support
- **Optimized Performance**: Qdrant's HNSW indexing delivers fast approximate nearest neighbor search
- **Scalable Architecture**: Cloud-based vector database handles growth in textbook content
- **Robust API**: Cohere's reliable embedding service with consistent quality
- **Advanced Features**: Qdrant supports filtering, payload storage, and hybrid search
- **Academic Suitability**: Cohere models excel at technical and academic content understanding

### Negative

- **External Dependencies**: Reliance on Cohere API and Qdrant Cloud introduces third-party risks
- **Cost Considerations**: Both services have usage-based pricing models
- **Vendor Lock-in**: Migration to alternative embedding/vector solutions would require significant work
- **API Rate Limits**: Cohere API may impose rate limits affecting search performance
- **Data Privacy**: Textbook content is sent to external services for embedding generation

## Alternatives Considered

**Alternative Stack A: OpenAI Embeddings + Pinecone**
- Embeddings: OpenAI text-embedding-ada-002
- Vector DB: Pinecone with optimized indexes
- Why rejected: Higher costs, English-only focus, less suitable for technical academic content

**Alternative Stack B: Sentence Transformers + FAISS**
- Embeddings: Hugging Face sentence-transformers (all-MiniLM-L6-v2)
- Vector DB: Facebook AI Similarity Search (FAISS)
- Why rejected: Self-hosting complexity, potentially lower quality embeddings for technical content

**Alternative Stack C: Jina AI Embeddings + Weaviate**
- Embeddings: Jina AI text-embedding-v2
- Vector DB: Weaviate cloud
- Why rejected: Less proven in academic/technical content scenarios, smaller ecosystem

## References

- Feature Spec: specs/2-rag-chatbot/spec-1-embeddings.md
- Implementation Plan: specs/2-rag-chatbot/plan.md
- Related ADRs: ADR-004 (metadata-search-glossary-information-architecture)
- Evaluator Evidence: history/prompts/2-rag-chatbot/1-embeddings-pipeline-specification.spec.prompt.md