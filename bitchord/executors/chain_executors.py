from typing import List
from ..core.context import Context
from ..core.nodes import Node

class ChainExecutor:
    """
    Executes nodes sequentially like a pipeline.
    """
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes

    async def run(self, context: Context, initial_input: str = ""):
        input_text = initial_input
        for node in self.nodes:
            input_text = await node.run(input_text, context)
        return context
