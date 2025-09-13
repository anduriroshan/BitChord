from typing import Dict, Callable
from ..core import Context, Node

class GraphExecutor:
    """
    Each node key maps to (Node, next_selector)
    next_selector is a callable that gets Context and returns the next node key or None.
    """
    def __init__(self, graph: Dict[str, tuple[Node, Callable[[Context], str]]], start: str):
        self.graph = graph
        self.start = start

    async def run(self, context: Context):
        key = self.start
        while key:
            node, selector = self.graph[key]
            context = await node.run(context)
            key = selector(context)
        return context
