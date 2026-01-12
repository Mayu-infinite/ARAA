from core.agent import Agent
from llm.ollama import OllamaLLM

class ReasonerAgent(Agent):
    def __init__(self):
        super().__init__("Reasoner")
        self.llm = OllamaLLM()

    def run(self, state):
        prompt = self._build_prompt(state)
        response = self.llm.generate(prompt).strip().upper()

        if response == "DONE":
            return "STOP"
        if response == "REPLAN":
            return "REPLAN"
        return "CONTINUE"

    def _build_prompt(self, state) -> str:
        completed = "\n".join(
            f" - {item['task']}: {item['result']}"
                for item in state.memory
            )
        
        pending = "\n".join(state.pending_tasks)

        return (
            "You are a reasoning agent.\n"
            "Decide whether the goal has been achieved.\n\n"
            f"GOAL:\n{state.goal}\n\n"
            f"COMPLETED WORK:\n{completed}\n\n"
            f"PENDING TASKS:\n{pending}\n\n"
            "Rules:\n"
            "- If the goal is sufficiently satisfied, answer DONE\n"
            "- If more tasks are needed, answer REPLAN\n"
            "- Otherwise answer CONTINUE\n"
            "Answer with exactly one word.\n"
        )
        
        
