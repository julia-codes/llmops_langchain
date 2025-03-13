from pinecone import Pinecone, ServerlessSpec
import os

DIMENSIONS = 3

pc = Pinecone(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment="us-east-1-aws"
)

# Create an index
index_name = "llm-ops-index2"
if index_name not in pc.list_indexes().names():
    pc.create_index(index_name, dimension=DIMENSIONS, spec=ServerlessSpec( cloud='aws', region='us-east-1'))

# Connect to the index
index = pc.Index(index_name)

# Add vectors
vectors = [
    ("id1", [0.1, 0.2, 0.3]),
    ("id2", [0.4, 0.5, 0.6]),
]

index.upsert(vectors)

# Query the index
query_vector = [0.1, 0.2, 0.3]
results = index.query(vector=query_vector, top_k=10, include_metadata=True)
print("Query results:", results)
