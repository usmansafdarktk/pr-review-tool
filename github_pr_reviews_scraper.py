import requests
import re
import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

# USER CONFIGURATION
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
OWNER = os.getenv('OWNER')
REPO = os.getenv('REPO')
OUTPUT_FILE = os.getenv('OUTPUT_FILE', 'pr_review_comments.md')

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github+json'
}


def get_all_pull_requests():
    prs = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls?state=all&per_page=100&page={page}"
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            print(f"Failed to get PRs: {resp.status_code}")
            break
        data = resp.json()
        if not data:
            break
        prs.extend(data)
        page += 1
    return prs


def get_reviews_for_pr(pr_number):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pr_number}/reviews"
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return []
    return resp.json()


def get_review_comments_for_pr(pr_number):
    comments = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pr_number}/comments?per_page=100&page={page}"
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            break
        data = resp.json()
        if not data:
            break
        comments.extend(data)
        page += 1
    return comments


def extract_commented_lines(diff_hunk, line_number):
    """
    Extracts the line commented on from the diff hunk (if possible).
    Returns a string of code with the commented line highlighted.
    """
    if not diff_hunk or not line_number:
        return ''
    lines = diff_hunk.split('\n')
    code_lines = []
    line_re = re.compile(r'^@@.*\+(\d+),?(\d*) @@')
    start_line = None

    # Find the start line in the hunk header (e.g. @@ -4,7 +4,8 @@)
    for i, l in enumerate(lines):
        m = line_re.match(l)
        if m:
            start_line = int(m.group(1))
            code_lines = lines[i + 1:]
            break
    if start_line is None:
        return ''

    # Find which line was commented on
    commented_idx = line_number - start_line
    display = []
    for idx, cl in enumerate(code_lines):
        # Remove diff signs
        code_only = cl[1:] if cl.startswith(('+', '-', ' ')) else cl
        # Mark the actual commented line
        if idx == commented_idx:
            display.append(f">>> {code_only} <<<   # Line commented on")
        else:
            display.append(code_only)
    return '\n'.join(display)


def main():
    prs = get_all_pull_requests()
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# GitHub Pull Request Reviews and Comments\n\n")
        for pr in prs:
            pr_num = pr['number']
            pr_title = pr['title']
            pr_url = pr['html_url']
            f.write(f"\n---\n\n## PR #{pr_num}: [{pr_title}]({pr_url})\n\n")

            # PR metadata
            author = pr['user']['login']
            created_at = pr['created_at']
            state = pr['state']
            f.write(f"- **Author:** `{author}`\n- **Created at:** {created_at}\n- **State:** {state}\n\n")

            # Review summaries
            reviews = get_reviews_for_pr(pr_num)
            if reviews:
                f.write("### Review Summaries:\n\n")
                for review in reviews:
                    reviewer = review['user']['login']
                    state = review['state']
                    submitted = review.get('submitted_at', 'N/A')
                    body = review['body'] or ''
                    f.write(f"**Reviewer:** `{reviewer}`\n")
                    f.write(f"- **State:** `{state}`\n- **Submitted:** {submitted}\n")
                    if body.strip():
                        f.write(f"> {body.strip()}\n\n")
                    else:
                        f.write("> _No comment text_\n\n")
            else:
                f.write("_No review summaries._\n\n")

            # Inline comments (with code context)
            comments = get_review_comments_for_pr(pr_num)
            if comments:
                f.write("### Inline Comments with Code Context:\n\n")
                for comment in comments:
                    reviewer = comment['user']['login']
                    path = comment['path']
                    line = comment.get('line', comment.get('original_line'))
                    body = comment['body']
                    diff_hunk = comment.get('diff_hunk', '')
                    f.write(f"**Reviewer:** `{reviewer}`\n")
                    f.write(f"- **File:** `{path}`\n- **Line:** `{line}`\n")
                    if diff_hunk and line:
                        code_block = extract_commented_lines(diff_hunk, line)
                        f.write("```diff\n")
                        f.write(f"{code_block}\n")
                        f.write("```\n")
                    f.write(f"> {body.strip()}\n\n")
            else:
                f.write("_No inline comments._\n\n")
    print(f"Structured review report written to {OUTPUT_FILE}")

import json

def save_review_chunks_jsonl(prs, output_jsonl_file='review_chunks.jsonl'):
    with open(output_jsonl_file, 'w', encoding='utf-8') as jf:
        for pr in prs:
            pr_num = pr['number']
            pr_title = pr['title']
            pr_url = pr['html_url']

            # PR metadata
            author = pr['user']['login']
            created_at = pr['created_at']
            state = pr['state']

            # Review summaries
            reviews = get_reviews_for_pr(pr_num)
            for review in reviews:
                reviewer = review['user']['login']
                state = review['state']
                submitted = review.get('submitted_at', 'N/A')
                body = review['body'] or ''
                jf.write(json.dumps({
                    "type": "review_summary",
                    "pr_number": pr_num,
                    "pr_title": pr_title,
                    "pr_url": pr_url,
                    "author": author,
                    "reviewer": reviewer,
                    "created_at": created_at,
                    "review_state": state,
                    "review_submitted": submitted,
                    "comment": body.strip(),
                    "file": None,
                    "line": None,
                    "code": None
                }) + '\n')

            # Inline comments (with code context)
            comments = get_review_comments_for_pr(pr_num)
            for comment in comments:
                reviewer = comment['user']['login']
                path = comment['path']
                line = comment.get('line', comment.get('original_line'))
                body = comment['body']
                diff_hunk = comment.get('diff_hunk', '')
                code_block = extract_commented_lines(diff_hunk, line) if diff_hunk and line else None
                jf.write(json.dumps({
                    "type": "inline_comment",
                    "pr_number": pr_num,
                    "pr_title": pr_title,
                    "pr_url": pr_url,
                    "author": author,
                    "reviewer": reviewer,
                    "created_at": created_at,
                    "file": path,
                    "line": line,
                    "code": code_block,
                    "comment": body.strip()
                }) + '\n')
    print(f"Structured review chunks written to {output_jsonl_file}")

if __name__ == '__main__':
    prs = get_all_pull_requests()
    main()
    save_review_chunks_jsonl(prs, 'review_chunks.jsonl')
