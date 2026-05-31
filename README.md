# 🤖 Agentic AI Coding Assistant

An advanced multi-agent AI Coding Assistant built using LangGraph, LangChain, Streamlit, and Groq.

This project demonstrates how autonomous AI agents can collaborate to plan, research, generate code, review implementations, create tests, and generate documentation.

---

## 🚀 Features

### Multi-Agent Architecture

The system consists of specialized AI agents:

* Router Agent
* Chat Agent
* Web Search Agent
* GitHub Research Agent
* Planner Agent
* Researcher Agent
* Coder Agent
* Reviewer Agent
* Tester Agent
* Documenter Agent

Each agent is responsible for a specific task and communicates through a LangGraph workflow.

---

## 🧠 Agent Workflow

### General Query

User Query
→ Router Agent
→ Chat Agent
→ Response

### Web Search Query

User Query
→ Router Agent
→ Web Search Agent
→ Web Tool
→ Response

### GitHub Repository Search

User Query
→ Router Agent
→ GitHub Agent
→ GitHub Search Tool
→ Response

### Coding Request

User Query
→ Router Agent
→ Planner Agent
→ Researcher Agent
→ Coder Agent
→ Reviewer Agent
→ Tester Agent
→ Documenter Agent
→ Final Output

---

## 🛠️ Tech Stack

### AI Frameworks

* LangChain
* LangGraph

### LLM

* Groq LLM

### Frontend

* Streamlit

### Search Tools

* DuckDuckGo Search
* GitHub Search API

### Deployment

* Docker
* Docker Compose

---

## 📂 Project Structure

```text
AI-Coding-Assistant/

├── agents/
│   ├── router_agent.py
│   ├── chat_agent.py
│   ├── web_search_agent.py
│   ├── github_agent.py
│   ├── planner.py
│   ├── researcher.py
│   ├── coder.py
│   ├── reviewer.py
│   ├── tester.py
│   └── documenter.py
│
├── graph/
│   ├── workflow.py
│   └── state.py
│
├── tools/
│   ├── web_tool.py
│   ├── github_tool.py
│   ├── file_tool.py
│   ├── shell_tool.py
│   └── project_generator.py
│
├── prompts/
│
├── llm/
│
├── utils/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🔧 Installation

### Clone Repository

```bash
git clone <repository-url>

cd AI-Coding-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a .env file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🐳 Docker

Build image:

```bash
docker build -t ai-coding-assistant .
```

Run container:

```bash
docker run -p 8501:8501 ai-coding-assistant
```

---

## 📈 Future Improvements

* Persistent Vector Memory
* Long-Term User Memory
* Code Execution Sandbox
* Multi-LLM Support
* Autonomous Bug Fixing
* GitHub Pull Request Generation
* Deployment Agent
* CI/CD Integration

---

## 🎯 Resume Highlights

* Multi-Agent Architecture using LangGraph
* Agent Routing System
* Tool Calling Architecture
* GitHub Repository Research
* Web Search Integration
* Autonomous Code Generation
* Dockerized Deployment
* Memory Enabled Workflows

---

## 📜 License

MIT License
