# ARAA — Autonomous Research Assistant AI

ARAA is an **agentic AI project** designed to help automate research tasks. It can **plan goals**, **break them into subtasks**, and **search and summarize information** autonomously using the **LLaMA 3 model** via **Ollama** and **LangChain**.

---

## Features

* **Goal Planning:** Breaks research goals into clear, numbered subtasks.
* **Autonomous Search:** Uses DuckDuckGo search to find relevant information.
* **Summarization:** Summarizes search results into concise bullet points.
* **Agentic Workflow:** Mimics human-like decision making in completing research tasks.
* **Extensible:** Easily add new agents or tools.

---

## Folder Structure

```
ARAA/
├── venv/                     # Python virtual environment
├── agents/                   # Individual AI agents
│   ├── planner_agent.py      # Plans research goals
│   └── searcher_agent.py     # Searches and summarizes information
├── main.py                   # Main program to run ARAA
└── .gitignore
```

---

## Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Mayu-infinite/ARAA.git
cd ARAA
```

### 2️⃣ Create and activate Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install required packages

```bash
pip install --upgrade pip
pip install langchain langchain-ollama langchain-community duckduckgo-search openai pandas numpy
```

Optional for image processing:

```bash
pip install opencv-python pillow scikit-learn
```

### 4️⃣ Start Ollama server

In a new terminal:

```bash
ollama serve
```

Wait until you see:

```
Listening on 127.0.0.1:11434
```

### 5️⃣ Run ARAA

With venv active:

```bash
python main.py
```

---

## Usage

1. Enter your **research goal** when prompted.
2. ARAA will output a **numbered task plan**.
3. Choose a task number to execute → ARAA will **search and summarize** the task.
4. View the summarized output.

---

## GitHub Setup

* Your project is ready to push:

```bash
git add .
git commit -m "Initial commit: ARAA setup with planner & searcher agents"
git push -u origin main
```

---

## Future Work / Enhancements

* Add **more agent types** (e.g., data analysis, visualization)
* Add **React frontend** for a user-friendly interface
* Integrate **PDF or web scraping tools**
* Improve **task prioritization and chaining** in agentic workflow

---

## Author

**Mayu-infinite**
IIT Jodhpur, India

---

## License

This project is open-source under the **MIT License**.
