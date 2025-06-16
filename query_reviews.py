import chromadb
from sentence_transformers import SentenceTransformer

query = """
what do reviewers say about security practises in terraform? any suggestions they give?
"""

embedder = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("reviews")

query_emb = embedder.encode([query])
results = collection.query(
    query_embeddings=query_emb.tolist(),
    n_results=5
)

for i, doc in enumerate(results['documents'][0]):
    print(f"\n--- Similar Review #{i+1} ---")
    print(doc)
    print("Metadata:", results['metadatas'][0][i])
