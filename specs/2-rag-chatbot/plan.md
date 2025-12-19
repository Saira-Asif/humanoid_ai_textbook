# Implementation Plan: 2-rag-chatbot

**Branch**: `feature/rag-chatbot` | **Date**: 2025-12-16 | **Spec**: specs/2-rag-chatbot/spec-1-embeddings.md
**Input**: Feature specification from `/specs/2-rag-chatbot/spec-1-embeddings.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the strategy for developing the RAG (Retrieval-Augmented Generation) chatbot embeddings pipeline. The implementation will extract content from the deployed textbook site (https://humanoid-ai-textbook.vercel.app/), generate semantic embeddings using Cohere, and store them in Qdrant vector database. The solution will be implemented as a single `main.py` file with specific functions as requested by the user.

## Technical Context

**Language/Version**: Python 3.10+
**Technology Stack/Dependencies Standards**:
- Package Manager: UV (as requested)
- Embedding Service: Cohere API
- Vector Database: Qdrant
- HTTP Client: requests for content extraction
- HTML Parsing: BeautifulSoup for content extraction
- Environment Management: .env for API keys
- Async Processing: asyncio for batch operations
- Progress Tracking: tqdm for progress indication
- Configuration: python-dotenv for environment management
**Storage**: Qdrant vector database cloud instance
**Testing**: Basic functionality tests, error handling validation
**Target Platform**: Python backend service
**Performance Goals**: Process pages efficiently, handle API rate limits gracefully
**Constraints**: Single file implementation in main.py, specific function signatures as requested
**Scale/Scope**:
- Process all pages from https://humanoid-ai-textbook.vercel.app/
- Create and populate Qdrant collection named "rag_emedding"
- Handle text extraction, chunking, embedding, and storage pipeline

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Security**: API keys stored securely in environment variables
- [x] **Error Handling**: Proper error handling for network requests and API calls
- [x] **Data Integrity**: Preserve content structure during extraction and processing
- [x] **Performance**: Efficient memory usage for large documents
- [x] **Reliability**: Retry logic for transient failures
- [x] **Maintainability**: Clean, well-documented code despite single-file constraint

## Project Structure

### Documentation (this feature)
```text
specs/2-rag-chatbot
├── checklists/          # Quality validation checklists
│   └── requirements.md
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (new backend directory)
```
backend/
├── pyproject.toml        # UV project configuration
├── main.py              # Main implementation file with all required functions
├── .env                 # Environment variables (not committed)
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

**Structure Decision:** Single-file implementation in main.py with all required functions as specified by user requirements.

## Implementation Phases

### Phase 1: Research & Requirements (Estimated: 2-4 hours)
**Objective:** Gather information about Cohere API, Qdrant client, and content extraction techniques.

### AI Tasks:
**Research Cohere embedding API best practices:**
- API rate limits and pricing
- Optimal chunk sizes for embeddings
- Error handling patterns
**Research Qdrant vector database:**
- Collection creation and management
- Vector storage and retrieval
- Metadata handling
**Research content extraction techniques:**
- URL discovery from deployed sites
- HTML parsing and text extraction
- Content cleaning strategies
**Identify optimal chunking strategies for academic content**
**Define error handling and retry mechanisms**

### Deliverables:
- **research.md** - Complete research findings with API details
- **chunking-strategy.md** - Optimal text chunking approach
- **error-handling.md** - Error handling and retry strategies

### Checkpoint:
Review API capabilities, verify technical feasibility, confirm chunking approach for academic content

### Phase 2: Foundation & Setup (Estimated: 1-2 hours)
**Objective**: Set up the project structure and install required dependencies.

### AI Tasks:
1. **Create backend directory structure**
2. **Initialize UV project with pyproject.toml:**
   - Add dependencies: cohere, qdrant-client, requests, beautifulsoup4, python-dotenv, tqdm
   - Configure project metadata
3. **Create .env file template with required API keys**
4. **Create basic main.py structure with function signatures**
5. **Set up .gitignore for sensitive files**
6. **Create README.md with project overview**

### Deliverables:
- Project structure with backend directory
- UV configuration in pyproject.toml
- Environment file template
- Basic main.py with function stubs
- Documentation in README.md

**Checkpoint:** Verify UV project initializes correctly, dependencies can be installed

### Phase 3: Core Implementation (Estimated: 4-6 hours)
**Objective:** Implement all required functions in main.py.

### AI Tasks:
1. **Implement get_all_urls function:**
   - Discover all pages from https://humanoid-ai-textbook.vercel.app/
   - Handle sitemap or crawl site structure
   - Return list of valid URLs

2. **Implement extract_text_from_url function:**
   - Fetch content from URL
   - Parse HTML and extract clean text
   - Preserve document structure and metadata
   - Handle different content types

3. **Implement chunk_text function:**
   - Split large documents into appropriate sizes
   - Maintain semantic coherence
   - Optimize for Cohere embedding limits
   - Preserve context boundaries

4. **Implement embed function:**
   - Interface with Cohere API
   - Handle API rate limits
   - Process text chunks into embeddings
   - Handle embedding errors gracefully

5. **Implement create_collection function:**
   - Connect to Qdrant instance
   - Create collection named "rag_emedding"
   - Configure vector dimensions for Cohere embeddings
   - Set up proper indexing

6. **Implement save_chunk_to_qdrant function:**
   - Store embeddings with metadata
   - Handle duplicate detection
   - Maintain document relationships
   - Implement error handling

7. **Implement main function:**
   - Orchestrate the complete pipeline
   - Handle command-line arguments
   - Provide progress feedback
   - Implement logging

### Deliverables:
- Complete main.py with all required functions
- Working pipeline from URL extraction to Qdrant storage
- Proper error handling throughout
- Command-line interface

**Checkpoint:** Verify each function works individually, test end-to-end pipeline

### Phase 4: Testing & Validation (Estimated: 2-3 hours)
**Objective:** Test the complete pipeline and validate results.

### AI Tasks:
1. **Unit Testing:**
   - Test each function individually
   - Validate error handling
   - Verify data transformations

2. **Integration Testing:**
   - Test complete pipeline
   - Validate Qdrant collection creation
   - Verify embedding storage and retrieval

3. **Performance Testing:**
   - Measure processing speed
   - Validate memory usage
   - Test with large documents

4. **Data Validation:**
   - Verify content integrity after extraction
   - Check embedding quality
   - Validate metadata preservation

### Deliverables:
- Test results and performance metrics
- Validated Qdrant collection with textbook content
- Performance benchmarks
- Quality validation report

**Checkpoint:** All functions pass tests, pipeline processes content correctly, Qdrant collection populated successfully

### Phase 5: Documentation & Deployment (Estimated: 1-2 hours)
**Objective:** Document the implementation and prepare for deployment.

### AI Tasks:
1. **Update README.md:**
   - Installation instructions
   - Usage examples
   - Configuration requirements
   - API key setup

2. **Create configuration guide:**
   - Environment variable setup
   - Qdrant connection configuration
   - Cohere API configuration

3. **Final validation:**
   - Verify complete functionality
   - Test with production-like data
   - Document any limitations

### Deliverables:
- Complete documentation
- Configuration guide
- Deployment instructions
- Final validation report

**Checkpoint:** Documentation complete, system ready for deployment, all functionality verified

## Dependencies and Sequencing
### Phase Dependencies:
- Phase 1 must complete before Phase 2 (need research before setup)
- Phase 2 must complete before Phase 3 (need foundation before implementation)
- Phase 3 must complete before Phase 4 (need implementation before testing)
- Phase 4 must complete before Phase 5 (need validation before documentation)

### Component Dependencies:
- URL extraction must work before text extraction
- Text extraction must work before chunking
- Chunking must work before embedding
- Embedding must work before Qdrant storage

### Parallel Opportunities:
- Research can happen in parallel for different components
- Documentation can be prepared alongside implementation

## Component Breakdown

-   **URL Discovery Component**: Function to discover all pages from the deployed textbook site `https://humanoid-ai-textbook.vercel.app/`. Will handle sitemap parsing or site crawling to identify all accessible content pages.

-   **Content Extraction Component**: Function to extract clean text from URLs, using HTML parsing libraries to remove markup and preserve content structure. Will handle different content types and maintain document hierarchy.

-   **Text Processing Component**: Function to chunk text into appropriate sizes for Cohere embeddings, maintaining semantic coherence and optimizing for embedding quality. Will handle boundary detection and context preservation.

-   **Embedding Component**: Function to interface with Cohere API for vector generation, handling authentication, rate limits, and error conditions. Will process text chunks into high-quality embeddings.

-   **Storage Component**: Function to store embeddings in Qdrant vector database with metadata, handling collection creation, vector storage, and relationship maintenance.

-   **Orchestration Component**: Main function to coordinate the complete pipeline from URL discovery through Qdrant storage, providing progress feedback and error handling.

## Design Decisions for ADRs

The following architecturally significant decisions are highlighted for potential Architectural Decision Records (ADRs) due to their impact, alternatives, and influence on the system:

1.  **Cohere-Qdrant Vector Search Stack**:
    *   **Description**: Decision to use Cohere for embeddings and Qdrant for vector storage
    *   **Rationale for ADR**: This decision impacts performance, cost, vendor dependencies, and scalability. It involves tradeoffs between different embedding models and vector databases.
    *   **ADR Reference**: history/adr/005-cohere-qdrant-selection.md

2.  **Single-File Implementation Strategy**:
    *   **Description**: Decision to implement all functionality in a single main.py file
    *   **Rationale for ADR**: This impacts maintainability, testability, and extensibility. It trades off code organization for simplicity and ease of deployment.
    *   **Alternative**: Modular implementation with separate files per component

3.  **Content Extraction and Chunking Approach**:
    *   **Description**: Decision on how to extract and chunk academic content for optimal embedding quality
    *   **Rationale for ADR**: This affects retrieval quality, processing efficiency, and semantic coherence. Different approaches may work better for textbook content.