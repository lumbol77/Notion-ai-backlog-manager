AI-Backlog-Manager 
An Intelligent Project Scoping Agent built with MCP and Google Gemini 2.5

Overview
AI-Backlog-Manager is a specialized "Agentic Middleware" that automates the transition from project ideation to structured execution. By leveraging the Model Context Protocol (MCP), this tool bridges the gap between Large Language Models (LLMs) and productivity ecosystems like Notion and GitHub.

Tech Stack
Language: Python 3.14

Protocol: Model Context Protocol (MCP)

AI Engine: Google Gemini 2.5 Flash (via the modern google-genai SDK)

Integrations: Notion API (Backlog Management) & GitHub API (Issue Tracking)

Orchestration: FastMCP for standardized tool definition

Key Features
Dual-Platform Sync: Simultaneously generates a Notion Kanban board and initializes GitHub Issues for a seamless dev-start.

Intelligent Decomposition: Uses Gemini 2.5 Flash to break vague ideas into 4 actionable, prioritized development phases.

Rate-Limit Protection: Implemented asynchronous delays to handle Notion API throttling (429 errors) during bulk task creation.

Architectural Decisions
Modular Agent Logic: The AI processing is decoupled from the server protocol, ensuring high maintainability.

Strict Schema Mapping: A custom transformation layer converts unstructured AI JSON into the strictly typed Notion "Pages" schema.

Zero-Footprint Security: All credentials (Notion Secret, GitHub Token, Google API Key) are managed via .env variables, ensuring no sensitive data is committed to version control.

How It Works
The Request: User provides a project idea (e.g., "Build a solar monitoring app") via an MCP client.

The Intelligence: Gemini 2.5 Flash analyzes the prompt and returns a structured JSON roadmap.

The Bridge: The Python server validates the JSON and maps data to Notion and GitHub schemas.

The Persistence: Tasks are created in real-time with dynamic properties (Priority, Status, Labels).

 Installation
Clone the repository:

Bash
git clone https://github.com/lumbol77/AI-Backlog-Manager.git
cd AI-Backlog-Manager

Install dependencies:
Bash
pip install -r requirements.txt

Configure environment: Create a .env file:

Code snippet
GOOGLE_API_KEY=your_key_here
NOTION_API_KEY=your_key_here
NOTION_DATABASE_ID=your_id_here
GITHUB_TOKEN=your_token_here
Run the server:

Bash
mcp dev server.py
