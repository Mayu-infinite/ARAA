from agents.executor import ExecutorAgent
from agents.reasoner import ReasonerAgent
from core.state import State
from agents.planner import PlannerAgent

class AgentLoop:
    def __init__(self) -> None:
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.reasoner = ReasonerAgent()
    
    def run(self, goal: str) -> State:
        state = State(goal)

        # ---- planning phase ----
        tasks = self.planner.run(state)
        for task in tasks:
            state.add_task(task)

        # ---- execution loop ----
        while not state.done:
            state.iteration += 1
            
            task = state.next_task()
            if task is None:
                break

            result = self.executor.run(task, state)
            state.add_result(task, result)

            decision = self.reasoner.run(state)
            if decision == "STOP":
                state.done = True

        return state
