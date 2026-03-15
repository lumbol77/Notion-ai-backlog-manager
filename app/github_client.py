import os
import httpx

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

async def create_github_issue(title, body="AI generated task"):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"

    payload = {
        "title": title,
        "body": body
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)

    return response.status_code