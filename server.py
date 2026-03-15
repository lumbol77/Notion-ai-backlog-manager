import os
import httpx
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Import AI logic
from app.ai_agent import generate_tasks_from_idea
from app.github_client import create_github_issue

# Load environment variables
load_dotenv()

# Initialize MCP Server
mcp = FastMCP("AI-Backlog-Manager")

# Load credentials
NOTION_TOKEN = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

# Validate environment variables
if not NOTION_TOKEN or not DATABASE_ID:
    raise ValueError("Missing NOTION_API_KEY or NOTION_DATABASE_ID in .env")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


@mcp.tool()
async def create_backlog_from_idea(idea: str):
    """
    Takes a project idea and automatically generates tasks,
    sends them to Notion, and creates GitHub issues.
    """

    # Generate tasks using AI
    tasks = generate_tasks_from_idea(idea)

    results = []

    async with httpx.AsyncClient() as client:

        for task in tasks:

            try:
                # Prepare Notion payload
                payload = {
                    "parent": {"database_id": DATABASE_ID},
                    "properties": {
                        "Name": {
                            "title": [
                                {
                                    "text": {
                                        "content": task["title"]
                                    }
                                }
                            ]
                        },
                        "Select": {
                            "select": {
                                "name": task["priority"]
                            }
                        },
                        "Status": {
                            "status": {
                                "name": "Not started"
                            }
                        }
                    }
                }

                # Send task to Notion
                notion_response = await client.post(
                    "https://api.notion.com/v1/pages",
                    headers=headers,
                    json=payload
                )

                notion_status = notion_response.status_code

                # Create GitHub Issue
                github_status = await create_github_issue(task["title"])

                results.append(
                    f"Created → {task['title']} | Notion:{notion_status} | GitHub:{github_status}"
                )

            except Exception as e:
                results.append(
                    f"Error creating task '{task['title']}': {str(e)}"
                )

    return "\n".join(results)


if __name__ == "__main__":
    mcp.run()