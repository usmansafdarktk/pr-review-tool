import os
import chromadb
from sentence_transformers import SentenceTransformer
import requests
from dotenv import load_dotenv
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

CODE_FILE = "/home/someone/Desktop/devops-internship-2025/submissions/muhammadUsmanSafder/examples/wordpress-deployment/main.tf"  # Change to your file

# Which model? (must support chat/completions)
HF_MODEL = "HuggingFaceH4/zephyr-7b-beta"

embedder = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("reviews")

# Read your code file
with open(CODE_FILE, "r", encoding="utf-8") as f:
    code = f.read()

# Retrieve similar reviews
code_emb = embedder.encode([code])
results = collection.query(
    query_embeddings=code_emb.tolist(),
    n_results=5
)
similar_reviews = []
for meta in results["metadatas"][0]:
    review = ""
    if meta.get("code"):
        review += f"Code:\n{meta['code']}\n"
    if meta.get("comment"):
        review += f"Review comment: {meta['comment']}\n"
    if meta.get("pr_url"):
        review += f"PR: {meta['pr_url']}\n"
    similar_reviews.append(review.strip())

if not similar_reviews:
    print("No similar past reviews found.")
    exit(0)

context = "\n\n".join(similar_reviews)
PROMPT = f"""
You are an expert reviewer for this code repository.

Here is new code submitted for review:

---CODE START---
{code}
---CODE END---

Here are similar past review comments and corrections from this repository:

---REVIEWS START---
{context}
---REVIEWS END---

Task:
Check if the new code is repeating any of the mistakes or discouraged practices from the past reviews above.
If yes, describe:
- What the issue is
- Why it matters
- The original review it relates to
- Suggest how to fix it

If there are no issues, say: "No repeated mistakes detected."
Your answer should be concise and actionable.
"""

# Call Hugging Face Inference API (free, but subject to limits)
API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

response = requests.post(API_URL, headers=headers, json={"inputs": PROMPT})
if response.status_code == 200:
    print("\n======= REVIEW FEEDBACK =======\n")
    print(response.json()[0]['generated_text'])
else:
    print("Hugging Face API error:", response.status_code, response.text)
