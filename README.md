# 🤖 Nexus AI

Nexus AI is a desktop AI assistant built with **Python** and **Google Gemini**. It is designed as a modular AI agent that can answer questions, maintain conversation context, and perform actions on your computer using custom tools.

This project is being developed from scratch to understand how modern AI agents work internally, without relying entirely on frameworks.

---

## Current Features

- AI chat powered by Google Gemini 2.5 Flash
- Native Gemini Function Calling
- Windows application launcher
- PostgreSQL-backed conversation history
- Long-term memory storage
- Modular AI agent architecture
- Environment variable configuration

---

## 📂 Project Structure

```
Nexus/
│
├── agents/
│   └── agent.py
│
├── config/
│   └── settings.py
│
├── llm/
│   └── gemini.py
│
├── memory/
│   └── conversation.py
│
├── prompts/
│   └── system_prompt.py
│
├── tools/
│   ├── app_finder.py
│   ├── registry.py
│   └── system_tools.py
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

* Python 3.12+
* Google Gemini API
* python-dotenv
* subprocess
* Windows API (`os.startfile`)
* Git & GitHub

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/TanishMehta23/NexusAI
```

Move into the project

```bash
cd NexusAI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Running the Project

```bash
python app.py
```

---

## 🧠 Current Architecture

```
                User
                  │
                  ▼
            Nexus AI Agent
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
   Tool Registry         Gemini LLM
        │
        ▼
  System Tools
        │
        ▼
 Windows Applications
```

---

## 💻 Example Commands

```
Open Chrome

Open Spotify

Open Notepad

Explain Binary Search

What is Java?

Who created you?
```

---

## 📌 Upcoming Features

* Native Gemini Function Calling
* PostgreSQL Integration
* Long-Term Memory
* RAG (Retrieval-Augmented Generation)
* PDF Chat
* Web Search
* Browser Automation
* File Management
* LangChain
* LangGraph
* PySide6 Desktop Interface
* Voice Assistant
* Windows Executable (.exe)

---

## 🎯 Learning Goals

This project focuses on understanding AI agent development from first principles, including:

* Large Language Models (LLMs)
* Prompt Engineering
* Tool Calling
* Conversation Memory
* Agent Architecture
* Desktop Automation
* Retrieval-Augmented Generation (RAG)
* Long-Term Memory
* Modern AI Frameworks

---

## 👨‍💻 Author

**Tanish Mehta**

Building Nexus AI to learn AI Engineering and modern AI Agent development from the ground up.