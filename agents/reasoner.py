from core.agent import Agent

class ReasonerAgent(Agent):
    def __init__(self):
        super().__init__("Reasoner")

    def run(self, state):
        # stop when no pending tasks Remaining
        if not state.pending_tasks:
            return "STOP"
        
        return "CONTINUE"
