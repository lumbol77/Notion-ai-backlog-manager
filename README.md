# AI-Backlog-Manager 
**An Intelligent Project Scoping Agent built with MCP and Google Gemini**

## Overview
AI-Backlog-Manager is a specialized "Agentic Middleware" that automates the transition from project ideation to structured execution. By leveraging the **Model Context Protocol (MCP)**, this tool bridges the gap between Large Language Models (LLMs) and productivity ecosystems like **Notion**.

## Tech Stack
* **Language:** Python 3.14
* **Protocol:** Model Context Protocol (MCP)
* **AI Engine:** Google Gemini 1.5 Flash (via Google Generative AI SDK)
* **Integrations:** Notion API (Internal Integration)
* **Async Networking:** `httpx` for non-blocking API orchestration

## Architectural Decisions
* **Modular Agent Logic:** The AI processing is decoupled from the server protocol, allowing for easy swapping of LLM providers.
* **Schema Mapping Layer:** Implemented a custom transformation layer to convert unstructured AI JSON into the strictly typed Notion "Pages" schema.
* **Security First:** Utilizes a Zero-Footprint approach by managing all sensitive credentials via environment variables (`.env`), ensuring no secrets are committed to version control.

## How It Works
1. **The Request:** The user provides a project idea through an MCP-compatible client.
2. **The Intelligence:** Gemini 1.5 Flash analyzes the prompt and generates a 4-phase development roadmap.
3. **The Bridge:** The Python server validates the JSON and maps the data to the target Notion Database ID.
4. **The Persistence:** Notion entries are created with dynamic properties (Task Name, Priority, and Status).

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Configure your `.env` with `GOOGLE_API_KEY`, `NOTION_API_KEY`, and `NOTION_DATABASE_ID`.
4. Run the server: `mcp dev server.py`.
