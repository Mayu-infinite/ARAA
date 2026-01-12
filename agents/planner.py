from core.agent import Agent
from llm.ollama import OllamaLLM

class PlannerAgent(Agent):
    def __init__(self):
        super().__init__("Planner")
        self.llm = OllamaLLM()

    def run(self, state):
        prompt = self._build_prompt(state.goal)
        response = self.llm.generate(prompt)

        ## print the response

        tasks = self._parse_tasks(response)
        ## Print tasks

        if not tasks:
            return [
                f"Research background of {state.goal}",
                f"Identify key concepts related to {state.goal}",
                f"Summarize information about {state.goal}",
            ]
        return tasks

    def _build_prompt(self, goal: str):
        return (
            "You are a planning agent.\n"
            "Break the following goal into 3 to 5 clear, actionable research tasks.\n\n"
            f"GOAL: {goal}\n\n"
            "Rules:\n"
            "- Each task must be a single sentence\n"
            "- Do not number the tasks\n"
            "- Do not include explanations\n"
            "- Output one task per line\n"
        )

    def _parse_tasks(self, text: str) -> list[str]:
        lines = [line.strip() for line in text.splitlines()]
        return [line for line in lines if line]

