🎤 Kapil Sharma AI Chatbot – Built with Streamlit + OpenAI
Ever imagined if Kapil Sharma became your personal assistant?
This fun + functional chatbot answers anything — from coding help to relationship advice — in Kapil’s signature Hinglish style, with wit, sarcasm, and desi charm!

🚀 Project Overview
This is a small experimental project demonstrating persona-based (role) prompting using OpenAI GPT-4 and Streamlit.

The goal is to mix humor with utility and explore how celebrity-style AI personas can make user interactions more engaging and memorable.

🔧 Status:

Just the initial version — many updates and features will be added soon!

🛠️ Tech Stack
Frontend: Streamlit

LLM: OpenAI GPT-4, model:gpt-4.1-mini

Backend: Python

Persona: Kapil Sharma (comedian, actor, TV host)

✨ Features
Kapil Sharma–like tone using custom role prompting

Hinglish responses with light humor (not overacted)

Works for all kinds of queries: code, career, love-life, interviews, etc.

Modular structure: plug in other personas easily

Natural message flow with chat history


🧠 How It Works
The app uses a custom persona prompt that mimics Kapil Sharma’s tone and personality.

All user inputs and responses are stored in session-based chat history.

The system message (persona prompt) is sent once at the beginning of every conversation.

The OpenAI API handles generation; Streamlit handles display.

🧪 To Run Locally
bash
Copy
Edit
git clone https://github.com/yourusername/kapil-sharma-chatbot.git
cd kapil-sharma-chatbot

# Create virtual env and install deps
pip install -r requirements.txt

# Add your OpenAI key in .streamlit/secrets.toml
# Example:
# [openai]
# OPENAI_API_KEY = "sk-..."

streamlit run app.py
📚 Learnings / Concepts Used
Role-based (persona) prompting

OpenAI’s ChatCompletion API

Python session state handling in Streamlit

Natural language tone tuning with humor

Hinglish language modeling