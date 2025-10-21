from qdrant_client import QdrantClient

# In-memory instance (data lost on restart)
client = QdrantClient(":memory:")

# Or persistent local storage (recommended)
client = QdrantClient(path="./qdrant_storage")

# Now you can use it normally
client.create_collection(
    collection_name="test_collection",
    vectors_config={"size": 4, "distance": "Dot"}
)