from typing import Callable, Dict, Any

class Tool:
    def __init__(self, name: str, description: str, func: Callable[..., Any]):
        self.name = name
        self.description = description
        self.func = func

    def run(self, *args, **kwargs)-> Any:
        return self.func(*args, **kwargs)

class ToolRegistry:
    def __init__(self) -> None:
        self.tools: Dict[str, Tool] = {}

    def register(self, tool: Tool):
        self.tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:
        return self.tools.get(name)

    def list_tools(self):
        return list(self.tools.keys())
        
