from typing import List, Dict, Any

class State:
    def __init__(self, goal: str):
        # User indent
        self.goal = goal

        #Task management
        self.pending_tasks: List[str] = []
        self.completed_tasks: List[str] = []

        # Memory
        self.memory : List[Dict[str, Any]] = []
        self.cache: Dict[str, str] = {}

        # Control
        self.done: bool = False
        self.iteration: int = 0

    # task - helpers
    def add_task(self, task: str):
        self.pending_tasks.append(task)

    def next_task(self)->str | None:
        if not self.pending_tasks:
            return None
        return self.pending_tasks.pop(0)

    # memory helpers
    def add_result(self, task: str, result: Any):
        self.completed_tasks.append(task)
        self.memory.append({
            "task": task,
            "result": result
        })

    def get_cached(self, key: str) -> str | None:
        return self.cache.get(key)

    def set_cache(self, key:str, value: str):
        self.cache[key] = value


