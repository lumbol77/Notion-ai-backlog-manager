import os
import httpx
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Import your new Mock AI logic
from app.ai_agent import generate_tasks_from_idea

load_dotenv()

# Initialize the MCP Server
mcp = FastMCP("AI-Backlog-Manager")

# Credentials from your .env
NOTION_TOKEN = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

@mcp.tool()
async def create_backlog_from_idea(idea: str):
    """
    Takes a project idea and automatically creates 4 development 
    tasks in the Notion Backlog database.
    """
    # 1. Get the list of tasks from your Mock AI (ai_agent.py)
    tasks = generate_tasks_from_idea(idea)
    
    results = []
    
    # 2. Loop through the tasks and send each one to Notion
    async with httpx.AsyncClient() as client:
        for task in tasks:
            # ALL lines below are now properly indented inside the loop
            
            # Updated payload with the new Status column
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
                    "Status": {  # This matches the new column you just added
                        "status": {
                            "name": "Not started"  # Or "Not started" depending on your Notion settings
                        }
                    }
                }
            }
            
            response = await client.post(
                "https://api.notion.com/v1/pages", 
                headers=headers, 
                json=payload
            )
            
            if response.status_code == 200:
                results.append(f"Created: {task['title']}")
            else:
                # This will help us see exactly why it failed (like a 400 error)
                results.append(f"Failed: {task['title']} ({response.status_code})")
            
    return "\n".join(results)

if __name__ == "__main__":
    mcp.run()