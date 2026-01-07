<<<<<<< HEAD
# ARAA — Autonomous Research Assistant AI

ARAA (Autonomous Research Assistant AI) is an **advanced agentic AI project** designed to automate complex research workflows. It leverages **LLM-based agents** to plan research goals, break them into actionable subtasks, perform autonomous searches, and summarize information efficiently. It mimics human decision-making and self-directed behavior, enabling researchers to focus on strategic work.

ARAA is built using the **LLaMA 3 model** via **Ollama**, integrated with **LangChain** for agent orchestration and task execution.

---

## Features

| Feature                    | Description                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------- |
| Goal Planning              | Breaks high-level research goals into sequential, prioritized tasks using Planner Agent |
| Autonomous Search          | Searches the web autonomously using DuckDuckGo and keyword expansion via Searcher Agent |
| Summarization              | Summarizes results into concise bullet points, pros/cons, or key insights               |
| Agentic Workflow           | Simulates human decision-making to select and execute tasks effectively                 |
| Extensible                 | Modular design allows integration of new agents or tools                                |
| Frontend Integration Ready | Supports easy integration with a React-based frontend for interactive dashboards        |

---

## Folder Structure

```
ARAA/
├── venv/                     # Python virtual environment
├── agents/                   # AI agent modules
│   ├── planner_agent.py      # Plans research goals and creates task sequences
│   └── searcher_agent.py     # Performs automated searches and summarizes information
├── main.py                   # Main entry point for running ARAA
├── requirements.txt          # Python dependencies
└── .gitignore
```

---

## Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Mayu-infinite/ARAA.git
cd ARAA
```

### 2️⃣ Create and Activate Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Required Python Packages

```bash
pip install --upgrade pip
pip install langchain langchain-ollama langchain-community duckduckgo-search openai pandas numpy
```

Optional for image processing or advanced tasks:

```bash
pip install opencv-python pillow scikit-learn
```

### 4️⃣ Start Ollama Server

In a separate terminal:

```bash
ollama serve
```

Wait until you see:

```
Listening on 127.0.0.1:11434
```

### 5️⃣ Run ARAA

With the virtual environment active:

```bash
python main.py
```

### 6️⃣ Interacting with ARAA

1. Enter your **research goal** when prompted.
2. ARAA generates a **numbered task plan** with subtasks.
3. Select the task number to execute; ARAA performs **search, summarization, and outputs results**.
4. Repeat for subsequent tasks to progress toward the overall research goal.

---

## Example Usage

| Input                                                  | Description                         | Output                                              |
| ------------------------------------------------------ | ----------------------------------- | --------------------------------------------------- |
| "Build a research plan for AI-based autonomous drones" | User provides overall research goal | Numbered subtask plan                               |
| Select task 2                                          | Execute a subtask                   | Summarized search results with links and key points |

---

## GitHub Setup

To version control your project and push updates:

```bash
git add .
git commit -m "Initial commit: Complete ARAA setup with planner & searcher agents"
git push -u origin main
```

---

## Future Enhancements

| Enhancement                 | Description                                                             |
| --------------------------- | ----------------------------------------------------------------------- |
| Additional Agents           | Data analysis, visualization, scraping agents can be added              |
| Frontend Dashboard          | React frontend for interactive task visualization and summaries         |
| Web Scraping & PDF Analysis | Automate extraction from academic papers, reports, and online resources |
| Enhanced Agentic Reasoning  | Implement task prioritization and chaining for better decision-making   |
| Multi-User Support          | Collaborative research environment with multiple users and profiles     |

---

## System Requirements

* **OS:** Linux (Fedora recommended) or macOS/Windows
* **Python:** >=3.11
* **RAM:** At least 8GB
* **Ollama:** Installed and running
* **Internet:** Required for autonomous search and updates

---

## Author

**Mayuri and Prasangeet**
---

## License

This project is open-source under the **MIT License**.

---

## Contact & Support

* GitHub Issues: [https://github.com/Mayu-infinite/ARAA/issues](https://github.com/Mayu-infinite/ARAA/issues)
* Email for collaboration and questions: (your GitHub email)

---

This README provides a **professional, comprehensive overview** of ARAA, including **features, setup, usage, examples, future plans, and contact info** for a GitHub-ready project page.
=======
# ARAA - Autonoumous Reasearch and Action Agent

**ARAA** is an agentic AI system designed to think, plan, and act autonomously — similar in spirit to Gemini or GPT-based agent frameworks — but built entirely using free, open-source tools like LangChain, local LLMs (via Ollama/llama.cpp), and ChromaDB for vector memory.
>>>>>>> 2994e7a (updated project)
