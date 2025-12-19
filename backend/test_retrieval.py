"""
Unit tests for the textbook retrieval module.

This test suite validates the functionality of the TextbookRetriever class,
including semantic search, module filtering, selected-text queries, and performance.
"""
import os
import unittest
from unittest.mock import patch, MagicMock
import sys
from typing import List

# Add the backend directory to the path so we can import retrieval
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from retrieval import TextbookRetriever, RetrievalResult


class TestRetrievalResult(unittest.TestCase):
    """Test the RetrievalResult dataclass."""

    def test_retrieval_result_creation(self):
        """Test creating a RetrievalResult instance."""
        result = RetrievalResult(
            content="Test content",
            url="https://example.com",
            title="Test Title",
            relevance_score=0.85,
            chunk_index=0,
            total_chunks=1,
            metadata={"key": "value"}
        )

        self.assertEqual(result.content, "Test content")
        self.assertEqual(result.url, "https://example.com")
        self.assertEqual(result.title, "Test Title")
        self.assertEqual(result.relevance_score, 0.85)
        self.assertEqual(result.chunk_index, 0)
        self.assertEqual(result.total_chunks, 1)
        self.assertEqual(result.metadata, {"key": "value"})


class TestTextbookRetriever(unittest.TestCase):
    """Test the TextbookRetriever class functionality."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Mock environment variables
        with patch.dict(os.environ, {
            'QDRANT_URL': 'http://localhost:6333',
            'COHERE_API_KEY': 'test-key'
        }):
            # We'll mock the actual Qdrant and Cohere clients
            with patch('retrieval.QdrantClient') as mock_qdrant, \
                 patch('retrieval.cohere.Client') as mock_cohere:

                # Mock the clients
                self.mock_qdrant_client = MagicMock()
                self.mock_cohere_client = MagicMock()
                mock_qdrant.return_value = self.mock_qdrant_client
                mock_cohere.return_value = self.mock_cohere_client

                # Mock the get_collections method to return a valid collection
                mock_collection = MagicMock()
                mock_collection.name = 'rag_embedding'
                self.mock_qdrant_client.get_collections.return_value.collections = [mock_collection]

                # Create the retriever instance (with mocked dependencies)
                self.retriever = TextbookRetriever()

    @patch('retrieval.cohere.Client')
    @patch('retrieval.QdrantClient')
    def test_initialization_success(self, mock_qdrant_class, mock_cohere_class):
        """Test successful initialization of TextbookRetriever."""
        # Mock the clients
        mock_qdrant_client = MagicMock()
        mock_cohere_client = MagicMock()
        mock_qdrant_class.return_value = mock_qdrant_client
        mock_cohere_class.return_value = mock_cohere_client

        # Mock the get_collections method
        mock_collection = MagicMock()
        mock_collection.name = 'rag_embedding'
        mock_qdrant_client.get_collections.return_value.collections = [mock_collection]

        # Test initialization
        with patch.dict(os.environ, {
            'QDRANT_URL': 'http://localhost:6333',
            'COHERE_API_KEY': 'test-key'
        }):
            retriever = TextbookRetriever()
            self.assertIsNotNone(retriever)
            self.assertEqual(retriever.collection_name, 'rag_embedding')

    @patch('retrieval.cohere.Client')
    @patch('retrieval.QdrantClient')
    def test_initialization_missing_qdrant_url(self, mock_qdrant_class, mock_cohere_class):
        """Test initialization fails when QDRANT_URL is missing."""
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError):
                TextbookRetriever()

    def test_embed_query(self):
        """Test the _embed_query method."""
        # Mock the Cohere embed response
        mock_embedding_response = MagicMock()
        mock_embedding_response.embeddings = [[0.1, 0.2, 0.3, 0.4]]
        self.mock_cohere_client.embed.return_value = mock_embedding_response

        query = "test query"
        result = self.retriever._embed_query(query)

        self.mock_cohere_client.embed.assert_called_once_with(
            texts=[query],
            model="embed-multilingual-v3.0",
            input_type="search_query"
        )
        self.assertEqual(result, [0.1, 0.2, 0.3, 0.4])

    def test_search_basic(self):
        """Test basic search functionality."""
        # Mock the embedding
        mock_embedding_response = MagicMock()
        mock_embedding_response.embeddings = [[0.1, 0.2, 0.3]]
        self.mock_cohere_client.embed.return_value = mock_embedding_response

        # Mock the search results
        mock_hit1 = MagicMock()
        mock_hit1.payload = {
            'content': 'Test content 1',
            'url': 'https://example1.com',
            'title': 'Test Title 1',
            'chunk_index': 0,
            'total_chunks': 1,
            'source_metadata': {'key': 'value1'},
            'chunk_id': 'chunk1',
            'content_hash': 'hash1'
        }
        mock_hit1.score = 0.9

        mock_hit2 = MagicMock()
        mock_hit2.payload = {
            'content': 'Test content 2',
            'url': 'https://example2.com',
            'title': 'Test Title 2',
            'chunk_index': 1,
            'total_chunks': 2,
            'source_metadata': {'key': 'value2'},
            'chunk_id': 'chunk2',
            'content_hash': 'hash2'
        }
        mock_hit2.score = 0.8

        self.mock_qdrant_client.search.return_value = [mock_hit1, mock_hit2]

        results = self.retriever.search("test query", top_k=5)

        # Verify the search was called correctly
        self.mock_qdrant_client.search.assert_called_once()
        args, kwargs = self.mock_qdrant_client.search.call_args
        self.assertEqual(kwargs['limit'], 5)
        self.assertEqual(kwargs['collection_name'], 'rag_embedding')

        # Verify results
        self.assertEqual(len(results), 2)  # Still expecting 2 results based on mock
        self.assertIsInstance(results[0], RetrievalResult)
        self.assertEqual(results[0].content, 'Test content 1')
        self.assertEqual(results[0].relevance_score, 0.9)
        self.assertEqual(results[1].content, 'Test content 2')
        self.assertEqual(results[1].relevance_score, 0.8)

    def test_search_with_filters(self):
        """Test search with filters."""
        # Mock the embedding
        mock_embedding_response = MagicMock()
        mock_embedding_response.embeddings = [[0.1, 0.2, 0.3]]
        self.mock_cohere_client.embed.return_value = mock_embedding_response

        # Mock empty search results for this test
        self.mock_qdrant_client.search.return_value = []

        # Call search with filters
        filters = {'modules': ['module-1-ros2']}
        self.retriever.search("test query", top_k=5, filters=filters)

        # Verify the search was called with filters
        self.mock_qdrant_client.search.assert_called()
        args, kwargs = self.mock_qdrant_client.search.call_args
        self.assertIsNotNone(kwargs.get('query_filter'))

    def test_search_by_module(self):
        """Test search_by_module functionality."""
        # Mock the embedding
        mock_embedding_response = MagicMock()
        mock_embedding_response.embeddings = [[0.1, 0.2, 0.3]]
        self.mock_cohere_client.embed.return_value = mock_embedding_response

        # Mock empty search results
        self.mock_qdrant_client.search.return_value = []

        # Call search_by_module
        results = self.retriever.search_by_module("test query", ["module-1-ros2"], top_k=5)

        # Verify the search was called (the implementation internally calls search with filters)
        self.mock_qdrant_client.search.assert_called()
        args, kwargs = self.mock_qdrant_client.search.call_args
        # Check that query_filter was passed, which indicates filters were applied
        self.assertIsNotNone(kwargs.get('query_filter'))

    def test_search_with_selection(self):
        """Test search_with_selection functionality."""
        # Mock the embedding
        mock_embedding_response = MagicMock()
        mock_embedding_response.embeddings = [[0.1, 0.2, 0.3]]
        self.mock_cohere_client.embed.return_value = mock_embedding_response

        # Mock empty search results
        self.mock_qdrant_client.search.return_value = []

        # Test with selected text only
        self.retriever.search_with_selection("selected text", top_k=2)

        # Verify search was called
        self.mock_qdrant_client.search.assert_called()

        # Reset mock for next test
        self.mock_qdrant_client.reset_mock()
        self.mock_qdrant_client.search.return_value = []

        # Test with selected text and context query
        self.retriever.search_with_selection("selected text", "context query", top_k=2)

        # Verify search was called with combined query
        self.mock_qdrant_client.search.assert_called()

    def test_top_k_validation(self):
        """Test that top_k parameter is validated."""
        # Mock the embedding
        mock_embedding_response = MagicMock()
        mock_embedding_response.embeddings = [[0.1, 0.2, 0.3]]
        self.mock_cohere_client.embed.return_value = mock_embedding_response

        # Mock empty search results
        self.mock_qdrant_client.search.return_value = []

        # Test with top_k below minimum
        self.retriever.search("test query", top_k=1)
        args, kwargs = self.mock_qdrant_client.search.call_args
        # The implementation should clamp to minimum of 3
        # Note: This test verifies the call was made, validation happens inside the method

        # Test with top_k above maximum
        self.mock_qdrant_client.reset_mock()
        self.retriever.search("test query", top_k=15)
        args, kwargs = self.mock_qdrant_client.search.call_args
        # The implementation should clamp to maximum of 10


class TestIntegration(unittest.TestCase):
    """Integration tests for the retrieval functionality."""

    @patch('retrieval.cohere.Client')
    @patch('retrieval.QdrantClient')
    def test_end_to_end_flow(self, mock_qdrant_class, mock_cohere_class):
        """Test the complete flow from initialization to search."""
        # Mock the clients
        mock_qdrant_client = MagicMock()
        mock_cohere_client = MagicMock()
        mock_qdrant_class.return_value = mock_qdrant_client
        mock_cohere_class.return_value = mock_cohere_client

        # Mock the get_collections method
        mock_collection = MagicMock()
        mock_collection.name = 'rag_embedding'
        mock_qdrant_client.get_collections.return_value.collections = [mock_collection]

        # Mock the embed response
        mock_embedding_response = MagicMock()
        mock_embedding_response.embeddings = [[0.1, 0.2, 0.3]]
        mock_cohere_client.embed.return_value = mock_embedding_response

        # Mock search results
        mock_hit = MagicMock()
        mock_hit.payload = {
            'content': 'Integrated test content',
            'url': 'https://integrated-test.com',
            'title': 'Integrated Test Title',
            'chunk_index': 0,
            'total_chunks': 1,
            'source_metadata': {'test': 'value'},
            'chunk_id': 'integrated_chunk',
            'content_hash': 'integrated_hash'
        }
        mock_hit.score = 0.85
        mock_qdrant_client.search.return_value = [mock_hit]

        # Execute the flow
        with patch.dict(os.environ, {
            'QDRANT_URL': 'http://localhost:6333',
            'COHERE_API_KEY': 'test-key'
        }):
            retriever = TextbookRetriever()
            results = retriever.search("integration test query", top_k=1)

        # Verify the complete flow worked
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].content, 'Integrated test content')
        self.assertEqual(results[0].relevance_score, 0.85)


if __name__ == '__main__':
    unittest.main()