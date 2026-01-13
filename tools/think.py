from llm.gemini import GeminiLLM
from llm.ollama import OllamaLLM

_llm = OllamaLLM()

def think(task: str) -> str:
    prompt = (
        "You are an assistant executing a task.\n"
        "Answer the task clearly and concisely.\n\n"
        f"TASK: {task}\n"
    )

    return "THINK - " + _llm.generate(prompt=prompt)
