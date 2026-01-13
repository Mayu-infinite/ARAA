from core.agent import Agent
from llm.ollama import OllamaLLM
from tools import registry

class ExecutorAgent(Agent):
    def __init__(self):
        super().__init__("Executor")
        self.llm = OllamaLLM()

    def run(self, task: str, state):
        mode_key = f"mode::{task}"
        cached_mode = state.get_cached(mode_key)

        if cached_mode:
            mode = cached_mode
        else:
            mode = self._decide_mode(task)
            state.set_cache(mode_key, mode)

        if mode == "THINK":
            think_key = f"think::{task}"
            cached_think = state.get_cached(think_key)
            if cached_think:
                return cached_think

            think_tool = registry.get("think")
            if think_tool is None:
                return "Thinking tool is not available"
            result = think_tool.run(task)
            state.set_cache(think_key, result)
            return result

        search_key = f"search::{task}"
        cached_search = state.get_cached(search_key)
        if cached_search:
            return cached_search

        search_tool = registry.get("web_search")
        summarize_tool = registry.get("summarize")

        if search_tool is None or summarize_tool is None:
            return "Required tools are not available"

        raw_result = search_tool.run(task)
        summary = summarize_tool.run(raw_result)
        state.set_cache(search_key, summary)
        return summary
    
    def _decide_mode(self, task: str) -> str:
        prompt = (
            "Classify the following task.\n"
            "Answer with only one word: THINK or SEARCH.\n\n"
            f"TASK: {task}\n"
        )

        response = self.llm.generate(prompt).strip().upper()
        if response == "THINK":
            return "THINK"
        return "SEARCH"
