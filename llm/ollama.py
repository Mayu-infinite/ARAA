import requests
from llm.base import LLM

class OllamaLLM(LLM):
    def __init__(
        self, 
        model: str = "llama3.1",
        host: str = "http://localhost:11434"
    ):
        self.model = model
        self.host = host

    def generate(self, prompt: str) -> str:
        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
