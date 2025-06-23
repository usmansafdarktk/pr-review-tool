# GitHub PR Review Assistant

A toolkit to **extract, structure, and semantically search code review feedback** from any GitHub repository’s pull requests (PRs).  
Helps you learn from historical reviews, avoid repeating past mistakes, and automate best-practice checks on new code.

---

## Features

- **Fetches all PRs** (open/closed) from a GitHub repository.
- **Extracts all review summaries** (approve, request changes, comment) for each PR.
- **Retrieves all inline review comments** (attached to specific lines of code in PR diffs).
- **Extracts code context** (diff hunk, highlights the commented line) for each inline comment.
- **Outputs a clean, structured Markdown report**—easy to browse by PR, review, and code context.
- **Saves all data as structured JSONL** for further use.
- **Embeds all review comments & code snippets into a vector database** (ChromaDB) for semantic search and RAG use cases.
- **Lets you query for relevant past reviews** by searching with new code or natural language.
- **Includes an LLM-powered code reviewer**: submit new code, get automatic feedback based on similar past reviews (terminal output).

---

## Files & Scripts

| Script/File                    | Purpose                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------- |
| `github_pr_reviews_scraper.py` | Fetches all PRs & reviews, outputs structured Markdown and JSONL chunks.                |
| `index_reviews.py`             | Embeds JSONL reviews and indexes them in a local ChromaDB vector store.                 |
| `query_reviews.py`             | Query the ChromaDB with new code or text to find similar historical reviews/comments.   |
| `code_reviewer.py`             | Takes your new code, retrieves top similar reviews, and uses an LLM to give feedback.  |
| `requirements.txt`             | Lists all required Python packages.                                                     |

---

## Setup

1. **Clone this repo and navigate to the directory.**
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure your environment:**
   - Copy `.env.example` to `.env` and fill in your GitHub token and other settings.
   - Example:
     ```
     GITHUB_TOKEN=your_github_token
     OWNER=your_github_username_or_org
     REPO=your_repository_name
     OUTPUT_FILE=pr_review_comments.md
     ```

---

## Usage

### 1. **Fetch and Structure All PR Reviews**
```bash
python github_pr_reviews_scraper.py
```
Produces:
pr_review_comments.md (nicely structured Markdown report)
review_chunks.jsonl (structured review/comment data for embedding)

2. Index Reviews for Semantic Search
```bash
python index_reviews.py
```
Creates a local ChromaDB store with vector embeddings for all reviews/comments.

3. Query Reviews
```bash
python query_reviews.py
```
Search for relevant past reviews by providing new code or a natural language question.
Returns the top matching review comments from your repo’s history.

4. Run the Code Reviewer
```bash
python3 code_reviewer.py
```
Provide your new code file.

The script fetches similar past reviews and asks an LLM (via Hugging Face API) to check if you are repeating mistakes or missing best practices already discussed in PRs.

Output is shown in the terminal.

### Requirements
Python 3.8+
A GitHub personal access token (for API)
Free Hugging Face account + Inference API token (for LLM-powered review)
See requirements.txt for packages

###Feedback / Contributions
Pull requests and issues are welcome!
If you have ideas, find bugs, or want to add UI (Streamlit etc), open an issue or PR.
