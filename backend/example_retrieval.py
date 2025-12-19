"""
Example usage of the TextbookRetriever module.

This script demonstrates the main functionality of the retrieval pipeline.
"""
import os
from retrieval import TextbookRetriever, RetrievalResult


def example_usage():
    """Demonstrate the main functionality of TextbookRetriever."""
    print("Textbook RAG Retrieval Pipeline - Example Usage")
    print("=" * 50)

    # Note: This example shows the expected usage pattern
    # In practice, you would need valid Qdrant and Cohere credentials

    # Example 1: Basic semantic search
    print("\n1. Basic Semantic Search:")
    print("   Query: 'What is ROS2?'")
    print("   Expected: Retrieve top-k relevant chunks about ROS2")
    print("   (This requires a running Qdrant instance with embeddings)")

    # Example 2: Module-filtered search
    print("\n2. Module-Filtered Search:")
    print("   Query: 'DDS communication' in module 'module-1-ros2'")
    print("   Expected: Retrieve chunks only from the ROS2 module")

    # Example 3: Selected-text context search
    print("\n3. Selected-Text Context Search:")
    print("   Selected: 'rclpy is a Python library'")
    print("   Context: 'Tell me more about its features'")
    print("   Expected: Retrieve complementary information about rclpy")

    # Example 4: Performance characteristics
    print("\n4. Performance:")
    print("   Expected: <200ms response time for typical queries")
    print("   Relevance scores from Qdrant for each result")
    print("   Complete source metadata with each result")


def example_code_snippet():
    """Show how to use the TextbookRetriever in code."""
    print("\nCode Example:")
    print("""
# Initialize the retriever
retriever = TextbookRetriever(
    qdrant_url="your-qdrant-url",
    qdrant_api_key="your-api-key",
    collection_name="rag_embedding"
)

# Basic search
results = retriever.search("What is ROS2?", top_k=5)
for result in results:
    print(f"Score: {result.relevance_score}")
    print(f"Content: {result.content[:100]}...")

# Module-filtered search
results = retriever.search_by_module(
    query="DDS communication",
    module_ids=["module-1-ros2"],
    top_k=3
)

# Selected-text search
results = retriever.search_with_selection(
    selected_text="rclpy is a Python library",
    context_query="Tell me more about its features",
    top_k=4
)
    """)


if __name__ == "__main__":
    example_usage()
    example_code_snippet()