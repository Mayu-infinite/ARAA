from tools import think
from tools.registry import Tool, ToolRegistry
from tools.dummy import echo_tool
from tools.search import web_search
from tools.summarize import summarize_text
from tools.think import think

registry = ToolRegistry()

registry.register(
    Tool(
        name="echo",
        description="Echos the input Text",
        func= echo_tool
    )
)

registry.register(
    Tool(
        name="web_search",
        description="Searches the we using DuckDuckGo",
        func=web_search
    )
)

registry.register(
    Tool(
        name="summarize",
        description="Summarizes long text into a short form",
        func=summarize_text
    )
)

registry.register(
    Tool(
        name="think",
        description="Uses reasoning to directly answer a task",
        func=think
    )
)
