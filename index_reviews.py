import json
import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

# Load the embedding model (MiniLM is fast and free!)
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Connect to ChromaDB (will store in ./chroma_db by default)
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="reviews")

def get_chunk_text(chunk):
    """Combine code and comment for embedding."""
    code = chunk.get("code") or ""
    comment = chunk.get("comment") or ""
    return f"{code}\n\n{comment}".strip()

def clean_metadata(md):
    """Replace all None values in metadata with empty string."""
    return {k: ("" if v is None else v) for k, v in md.items()}

# Read your jsonl file
with open('review_chunks.jsonl', 'r', encoding='utf-8') as jf:
    docs = [json.loads(line) for line in jf]

# Insert in batches for speed
batch_size = 32
for i in range(0, len(docs), batch_size):
    batch = docs[i:i+batch_size]
    texts = [get_chunk_text(c) for c in batch]
    embeddings = embedder.encode(texts, show_progress_bar=True)
    ids = [f"{c['type']}_{c['pr_number']}_{i+j}" for j, c in enumerate(batch)]
    # Clean each metadata dict in the batch before inserting
    metadatas = [clean_metadata(md) for md in batch]
    collection.add(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=texts,
        metadatas=metadatas
    )
print("All review chunks indexed in ChromaDB!")
