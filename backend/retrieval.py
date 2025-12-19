"""
Textbook Retrieval Module

This module implements the retrieval pipeline for the textbook RAG chatbot.
It queries the Qdrant vector database to find relevant content chunks based on
semantic similarity to user queries, with support for filtering and context assembly.
"""
import os
import time
import logging
from typing import List, Dict, Optional, Any
from dataclasses import dataclass
import cohere
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue, Range, PointStruct, VectorParams, Distance
from qdrant_client.http import models
import dotenv


# Load environment variables
dotenv.load_dotenv()


@dataclass
class RetrievalResult:
    """Data class representing a single retrieval result."""
    content: str
    url: str
    title: str
    relevance_score: float
    chunk_index: int
    total_chunks: int
    metadata: Dict[str, Any]
    source_document_id: Optional[str] = None
    content_hash: Optional[str] = None


class TextbookRetriever:
    """Main retrieval class for the textbook RAG chatbot."""

    def __init__(self,
                 qdrant_url: Optional[str] = None,
                 qdrant_api_key: Optional[str] = None,
                 collection_name: Optional[str] = None,
                 cohere_api_key: Optional[str] = None):
        """
        Initialize the TextbookRetriever.

        Args:
            qdrant_url: Qdrant server URL (defaults to env var)
            qdrant_api_key: Qdrant API key (defaults to env var)
            collection_name: Qdrant collection name (defaults to 'rag_embedding')
            cohere_api_key: Cohere API key for query embedding (optional)
        """
        self.qdrant_url = qdrant_url or os.getenv('QDRANT_URL')
        self.qdrant_api_key = qdrant_api_key or os.getenv('QDRANT_API_KEY')
        self.collection_name = collection_name or os.getenv('QDRANT_COLLECTION_NAME', 'rag_embedding')
        self.cohere_api_key = cohere_api_key or os.getenv('COHERE_API_KEY')

        if not self.qdrant_url:
            raise ValueError("QDRANT_URL environment variable is required")

        # Initialize Qdrant client
        if self.qdrant_api_key:
            self.qdrant_client = QdrantClient(url=self.qdrant_url, api_key=self.qdrant_api_key, timeout=10)
        else:
            self.qdrant_client = QdrantClient(url=self.qdrant_url, timeout=10)

        # Initialize Cohere client if API key is provided
        self.cohere_client = None
        if self.cohere_api_key:
            self.cohere_client = cohere.Client(self.cohere_api_key)

        # Validate connection
        self.validate_connection()

        logging.info(f"TextbookRetriever initialized with collection: {self.collection_name}")

    def validate_connection(self) -> bool:
        """
        Validate connection to Qdrant and check if collection exists.

        Returns:
            True if connection and collection are valid, False otherwise
        """
        try:
            # Test connection by getting collections
            collections = self.qdrant_client.get_collections()
            collection_exists = any(col.name == self.collection_name for col in collections.collections)

            if not collection_exists:
                logging.error(f"Collection '{self.collection_name}' does not exist in Qdrant")
                return False

            logging.info(f"Connection to Qdrant validated successfully. Collection '{self.collection_name}' exists.")
            return True
        except Exception as e:
            logging.error(f"Failed to validate Qdrant connection: {str(e)}")
            return False

    def _embed_query(self, query: str) -> List[float]:
        """
        Embed a query string using Cohere.

        Args:
            query: Query text to embed

        Returns:
            Embedding vector as a list of floats
        """
        if not self.cohere_client:
            raise ValueError("Cohere client not initialized. Please provide COHERE_API_KEY.")

        try:
            # Use Cohere's embed function to create query embedding
            response = self.cohere_client.embed(
                texts=[query],
                model="embed-multilingual-v3.0",  # Same model used for document embeddings
                input_type="search_query"  # Specify this is a search query
            )
            return response.embeddings[0]  # Return the first (and only) embedding
        except Exception as e:
            logging.error(f"Error embedding query: {str(e)}")
            raise

    def search(self,
               query: str,
               top_k: int = 5,
               filters: Optional[Dict[str, Any]] = None,
               min_score: float = 0.0) -> List[RetrievalResult]:
        """
        Perform semantic search against the Qdrant collection.

        Args:
            query: Query text to search for
            top_k: Number of top results to return (3-10)
            filters: Optional dictionary of filters to apply
            min_score: Minimum relevance score threshold

        Returns:
            List of RetrievalResult objects sorted by relevance score
        """
        start_time = time.time()

        # Validate top_k parameter
        if not 3 <= top_k <= 10:
            logging.warning(f"top_k {top_k} is outside recommended range (3-10)")
            top_k = max(3, min(10, top_k))  # Clamp to 3-10 range

        # Embed the query
        query_vector = self._embed_query(query)

        # Build Qdrant filter if filters are provided
        qdrant_filter = None
        if filters:
            conditions = []

            # Handle module filters (e.g., "module-1-ros2")
            if 'modules' in filters and filters['modules']:
                if isinstance(filters['modules'], str):
                    filters['modules'] = [filters['modules']]

                # Create a filter for the module - assuming it's stored in metadata
                # This might need to be adjusted based on how modules are stored in the payload
                module_filter = FieldCondition(
                    key="metadata.module",  # Adjust key based on actual payload structure
                    match=models.MatchAny(any=filters['modules'])
                )
                conditions.append(module_filter)

            # Add other filters as needed
            for key, value in filters.items():
                if key == 'modules':  # Already handled above
                    continue

                if isinstance(value, list):
                    condition = FieldCondition(
                        key=key,
                        match=models.MatchAny(any=value)
                    )
                else:
                    condition = FieldCondition(
                        key=key,
                        match=models.MatchValue(value=value)
                    )
                conditions.append(condition)

            if conditions:
                qdrant_filter = Filter(must=conditions)

        try:
            # Perform search in Qdrant
            search_results = self.qdrant_client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                query_filter=qdrant_filter,
                limit=top_k,
                with_payload=True,
                with_vectors=False,
                score_threshold=min_score
            )

            # Convert results to RetrievalResult objects
            results = []
            for hit in search_results:
                payload = hit.payload

                result = RetrievalResult(
                    content=payload.get('content', ''),
                    url=payload.get('url', ''),
                    title=payload.get('title', ''),
                    relevance_score=hit.score,
                    chunk_index=payload.get('chunk_index', 0),
                    total_chunks=payload.get('total_chunks', 1),
                    metadata=payload.get('source_metadata', {}),
                    source_document_id=payload.get('chunk_id'),
                    content_hash=payload.get('content_hash')
                )
                results.append(result)

            end_time = time.time()
            query_time_ms = (end_time - start_time) * 1000
            logging.info(f"Search completed in {query_time_ms:.2f}ms, returned {len(results)} results")

            # Performance check
            if query_time_ms > 200:
                logging.warning(f"Query time {query_time_ms:.2f}ms exceeded 200ms threshold")

            return results

        except Exception as e:
            logging.error(f"Error performing search: {str(e)}")
            raise

    def search_by_module(self,
                         query: str,
                         module_ids: List[str],
                         top_k: int = 5) -> List[RetrievalResult]:
        """
        Search within specific textbook modules.

        Args:
            query: Query text to search for
            module_ids: List of module IDs to search within
            top_k: Number of top results to return

        Returns:
            List of RetrievalResult objects from specified modules
        """
        filters = {'modules': module_ids}
        return self.search(query, top_k, filters)

    def search_with_selection(self,
                              selected_text: str,
                              context_query: Optional[str] = None,
                              top_k: int = 5) -> List[RetrievalResult]:
        """
        Search using selected text as the basis for retrieval.

        Args:
            selected_text: Text that was selected by the user
            context_query: Optional additional query to provide context
            top_k: Number of top results to return

        Returns:
            List of RetrievalResult objects relevant to the selected text
        """
        # If context query is provided, combine it with selected text
        if context_query:
            query = f"{selected_text} {context_query}"
        else:
            query = selected_text

        # Perform search with the combined query
        return self.search(query, top_k)

    def get_available_modules(self) -> List[str]:
        """
        Get list of available modules in the collection.

        Returns:
            List of unique module IDs found in the collection
        """
        try:
            # Get all points to extract unique modules
            # This is a simplified approach - in practice, you might want to use Qdrant's
            # facet search capabilities if available
            all_points, _ = self.qdrant_client.scroll(
                collection_name=self.collection_name,
                limit=1000,  # Limit to avoid performance issues
                with_payload=True
            )

            modules = set()
            for point in all_points:
                payload = point.payload
                module = payload.get('metadata', {}).get('module')
                if module:
                    modules.add(module)

            return list(modules)

        except Exception as e:
            logging.error(f"Error retrieving available modules: {str(e)}")
            return []


def main():
    """Interactive CLI tester for manual validation."""
    import argparse

    parser = argparse.ArgumentParser(description='Textbook RAG Retrieval Tester')
    parser.add_argument('--query', type=str, help='Query to search for')
    parser.add_argument('--module', type=str, help='Module to filter by')
    parser.add_argument('--top-k', type=int, default=5, help='Number of results to return')
    parser.add_argument('--selected-text', type=str, help='Selected text for context search')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    parser.add_argument('--list-modules', action='store_true', help='List available modules')

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    try:
        # Initialize retriever
        retriever = TextbookRetriever()

        if args.list_modules:
            # List available modules
            modules = retriever.get_available_modules()
            print("Available modules:")
            for module in modules:
                print(f"  - {module}")
            return

        if args.interactive:
            # Interactive mode
            print("Textbook RAG Retrieval Interactive Tester")
            print("Commands:")
            print("  - search <query> - Basic semantic search")
            print("  - search-module <module> <query> - Search within specific module")
            print("  - search-selection <selected-text> [context-query] - Search with selected text")
            print("  - modules - List available modules")
            print("  - quit - Exit the tester")
            print()

            while True:
                try:
                    command = input("retriever> ").strip()
                    if not command:
                        continue

                    parts = command.split(' ', 2)  # Split into at most 3 parts
                    cmd = parts[0].lower()

                    if cmd == 'quit':
                        break
                    elif cmd == 'modules':
                        modules = retriever.get_available_modules()
                        print("Available modules:")
                        for module in modules:
                            print(f"  - {module}")
                    elif cmd == 'search' and len(parts) >= 2:
                        query = parts[1]
                        print(f"Searching for: '{query}'")
                        results = retriever.search(query, top_k=args.top_k)
                        display_results(results)
                    elif cmd == 'search-module' and len(parts) >= 3:
                        module = parts[1]
                        query = parts[2]
                        print(f"Searching for: '{query}' in module: '{module}'")
                        results = retriever.search_by_module(query, [module], top_k=args.top_k)
                        display_results(results)
                    elif cmd == 'search-selection' and len(parts) >= 2:
                        selected_text = parts[1]
                        context_query = parts[2] if len(parts) > 2 else None
                        print(f"Searching with selected text: '{selected_text[:50]}...'")
                        if context_query:
                            print(f"And context query: '{context_query}'")
                        results = retriever.search_with_selection(selected_text, context_query, top_k=args.top_k)
                        display_results(results)
                    else:
                        print(f"Unknown command: {command}")
                        print("Use 'help' for available commands (not implemented, see above)")

                except KeyboardInterrupt:
                    print("\nExiting...")
                    break
                except Exception as e:
                    print(f"Error: {str(e)}")
        else:
            # Command-line mode (original behavior)
            if args.selected_text:
                # Test selected-text search
                print(f"Searching with selected text: '{args.selected_text[:50]}...'")
                if args.query:
                    print(f"And context query: '{args.query}'")

                results = retriever.search_with_selection(
                    selected_text=args.selected_text,
                    context_query=args.query,
                    top_k=args.top_k
                )
            elif args.module:
                # Test module-filtered search
                print(f"Searching for: '{args.query}' in module: '{args.module}'")
                results = retriever.search_by_module(
                    query=args.query,
                    module_ids=[args.module],
                    top_k=args.top_k
                )
            elif args.query:
                # Test standard search
                print(f"Searching for: '{args.query}'")
                results = retriever.search(
                    query=args.query,
                    top_k=args.top_k
                )
            else:
                print("Please provide a query (--query) or use --interactive mode")
                return

            # Display results
            display_results(results)

    except Exception as e:
        print(f"Error: {str(e)}")
        logging.error(f"Error in CLI tester: {str(e)}")


def display_results(results: List[RetrievalResult]):
    """Helper function to display retrieval results in a formatted way."""
    print(f"\nFound {len(results)} results:")
    print("-" * 80)
    for i, result in enumerate(results, 1):
        print(f"{i}. Score: {result.relevance_score:.3f}")
        print(f"   URL: {result.url}")
        print(f"   Title: {result.title}")
        print(f"   Content (first 100 chars): {result.content[:100]}...")
        print(f"   Chunk: {result.chunk_index+1}/{result.total_chunks}")
        if result.metadata:
            print(f"   Metadata keys: {list(result.metadata.keys())}")
        print("-" * 80)


if __name__ == "__main__":
    main()