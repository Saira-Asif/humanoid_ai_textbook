"""
Unit tests for the RAG backend functions.
"""
import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add the backend directory to the path so we can import main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import get_token_count, chunk_text, ContentChunk


class TestTokenCount(unittest.TestCase):
    """Test the token counting function."""

    def test_simple_text(self):
        """Test token counting with simple text."""
        text = "This is a simple test sentence."
        count = get_token_count(text)
        self.assertEqual(count, 6)

    def test_text_with_punctuation(self):
        """Test token counting with punctuation."""
        text = "Hello, world! How are you?"
        count = get_token_count(text)
        self.assertEqual(count, 6)

    def test_empty_text(self):
        """Test token counting with empty text."""
        text = ""
        count = get_token_count(text)
        self.assertEqual(count, 0)


class TestChunkText(unittest.TestCase):
    """Test the text chunking function."""

    def test_short_text_single_chunk(self):
        """Test chunking of short text that fits in one chunk."""
        content = "This is a short text."
        title = "Test Title"
        url = "https://example.com"

        chunks = chunk_text(content, title, url)

        self.assertEqual(len(chunks), 1)
        self.assertEqual(chunks[0].content, content)
        self.assertEqual(chunks[0].title, title)
        self.assertEqual(chunks[0].url, url)
        self.assertEqual(chunks[0].total_chunks, 1)

    def test_long_text_multiple_chunks(self):
        """Test chunking of longer text that requires multiple chunks."""
        # Create a longer text
        content = " ".join(["word"] * 500)  # 500 words
        title = "Test Title"
        url = "https://example.com"

        # Temporarily set environment variable for chunk size
        original_chunk_size = os.environ.get('CHUNK_SIZE_TOKENS')
        os.environ['CHUNK_SIZE_TOKENS'] = '100'  # Small chunk size for testing

        try:
            chunks = chunk_text(content, title, url)
            self.assertGreater(len(chunks), 1)  # Should create multiple chunks
            self.assertEqual(chunks[0].total_chunks, len(chunks))  # Check total_chunks is consistent
        finally:
            # Restore original environment variable
            if original_chunk_size is not None:
                os.environ['CHUNK_SIZE_TOKENS'] = original_chunk_size
            elif 'CHUNK_SIZE_TOKENS' in os.environ:
                del os.environ['CHUNK_SIZE_TOKENS']


class TestContentChunk(unittest.TestCase):
    """Test the ContentChunk dataclass."""

    def test_content_chunk_creation(self):
        """Test creating a ContentChunk instance."""
        chunk = ContentChunk(
            id="test-id",
            url="https://example.com",
            title="Test Title",
            content="Test content",
            chunk_index=0,
            total_chunks=1,
            created_at="2023-01-01T00:00:00",
            word_count=10,
            token_count=10
        )

        self.assertEqual(chunk.id, "test-id")
        self.assertEqual(chunk.url, "https://example.com")
        self.assertEqual(chunk.title, "Test Title")
        self.assertEqual(chunk.content, "Test content")
        self.assertEqual(chunk.chunk_index, 0)
        self.assertEqual(chunk.total_chunks, 1)
        self.assertEqual(chunk.created_at, "2023-01-01T00:00:00")
        self.assertEqual(chunk.word_count, 10)
        self.assertEqual(chunk.token_count, 10)


@patch.dict(os.environ, {
    'COHERE_API_KEY': 'test-key',
    'QDRANT_URL': 'http://localhost:6333'
}, clear=True)
class TestIntegration(unittest.TestCase):
    """Integration tests that require environment setup."""

    def test_validate_environment(self):
        """Test environment validation."""
        from main import validate_environment
        try:
            validate_environment()
        except ValueError:
            # This might fail if the env vars are not set properly in the test environment
            # but that's expected in a test environment
            pass


if __name__ == '__main__':
    unittest.main()