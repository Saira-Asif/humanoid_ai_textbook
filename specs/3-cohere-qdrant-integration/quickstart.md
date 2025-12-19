# Quickstart Guide: Cohere-Qdrant RAG Backend

**Feature**: 3-cohere-qdrant-integration
**Date**: 2025-12-16
**Status**: Complete
**Author**: Claude Code

## Overview

This guide provides quick instructions to set up and run the Cohere-Qdrant RAG backend that extracts content from the textbook site, generates embeddings, and stores them in Qdrant.

## Prerequisites

- Python 3.10 or higher
- UV package manager
- Cohere API key
- Qdrant database instance (cloud or local)

## Setup Instructions

### 1. Clone or Create Project Directory
```bash
mkdir backend
cd backend
```

### 2. Initialize UV Project
```bash
uv init
```

### 3. Install Dependencies
```bash
uv add cohere qdrant-client requests beautifulsoup4 python-dotenv tqdm
```

### 4. Create Environment File
Create a `.env` file in the project root:
```env
COHERE_API_KEY=your_cohere_api_key_here
QDRANT_URL=your_qdrant_url_here
QDRANT_API_KEY=your_qdrant_api_key_here
SOURCE_URL=https://humanoid-ai-textbook.vercel.app/
```

## Quick Run

### 1. Create main.py
Create the main.py file with all required functions as specified in the implementation plan.

### 2. Run the Application
```bash
python main.py
```

## Configuration Options

### Environment Variables
- `COHERE_API_KEY`: Your Cohere API key
- `QDRANT_URL`: Qdrant instance URL (e.g., "https://your-cluster.qdrant.io:6333")
- `QDRANT_API_KEY`: Qdrant API key (for cloud instances)
- `SOURCE_URL`: Target website to process (default: "https://humanoid-ai-textbook.vercel.app/")
- `CHUNK_SIZE_TOKENS`: Max tokens per chunk (default: 250)
- `BATCH_SIZE`: Batch size for API calls (default: 10)
- `RATE_LIMIT_DELAY`: Delay between API calls in seconds (default: 0.1)

## Expected Output

When you run the application, you should see:
1. URL discovery progress
2. Content extraction status
3. Embedding generation progress
4. Vector storage progress
5. Final summary with statistics

## Troubleshooting

### Common Issues

**API Rate Limits**:
- Ensure RATE_LIMIT_DELAY is set appropriately
- Check your Cohere account limits

**Connection Issues**:
- Verify QDRANT_URL is correct
- Check QDRANT_API_KEY is valid

**No URLs Found**:
- Verify SOURCE_URL is accessible
- Check if the site has a robots.txt that blocks crawling

## Next Steps

1. Review the generated Qdrant collection for completeness
2. Test retrieval functionality with a sample RAG application
3. Monitor processing performance and adjust configuration as needed