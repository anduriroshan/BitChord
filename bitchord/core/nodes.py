from abc import ABC, abstractmethod
from .context import Context
from .llm import LLM
from .tool import Tool


class Node(ABC):
    """
    Base class for all nodes in the orchestration graph/chain.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    async def run(self, input_text: str, context: Context) -> str:
        pass


class PromptNode(Node):
    """
    A node that uses an LLM to generate responses.
    """

    def __init__(self, name: str, llm: LLM):
        super().__init__(name)
        self.llm = llm

    async def run(self, input_text: str, context: Context) -> str:
        response = await self.llm.generate(input_text, context)
        context.add_to_history("assistant", response)
        return response


class ToolNode(Node):
    """
    A node that wraps a Tool.
    """

    def __init__(self, name: str, tool: Tool):
        super().__init__(name)
        self.tool = tool

    async def run(self, input_text: str, context: Context) -> str:
        result = await self.tool.run(input_text, context)
        context.add_to_history("tool", result)
        return result


class AnswerNode(Node):
    """
    A node that outputs the final response to the user.
    """

    def __init__(self, name: str):
        super().__init__(name)

    async def run(self, input_text: str, context: Context) -> str:
        context.add_to_history("final", input_text)
        return input_text
