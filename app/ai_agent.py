# ai_agent.py
import os
from dotenv import load_dotenv

load_dotenv()

def generate_tasks_from_idea(idea: str):
    """
    Mock AI Agent: Simulates an AI PM to save you money while testing.
    This bypasses the OpenAI 429 error entirely.
    """
    print(f"PM Agent: Processing idea -> {idea}")
    
    # This simulates what a Senior PM would return for any idea
    return [
        {"title": f"Database Schema Design for {idea}", "priority": "High"},
        {"title": f"API Endpoint Development: {idea}", "priority": "Medium"},
        {"title": f"Frontend UI/UX Implementation for {idea}", "priority": "Medium"},
        {"title": f"Security Audit & Deployment", "priority": "Low"}
    ]