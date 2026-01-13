import os
from google import genai
from dotenv import load_dotenv

from llm.base import LLM

load_dotenv()

class GeminiLLM(LLM):
    def __init__(self, model: str = "gemini-2.5-flash") -> None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY not set")

        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        text = response.text
        if text is None:
            return ""
        
        return text.strip()

