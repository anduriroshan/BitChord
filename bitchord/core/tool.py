from abc import ABC, abstractmethod
from .context import Context


class Tool(ABC):
    """
    Abstract base class for tools.
    """

    @abstractmethod
    async def run(self, query: str, context: Context) -> str:
        pass


class MathTool(Tool):
    """
    Simple math evaluator.
    """

    async def run(self, query: str, context: Context) -> str:
        try:
            return str(eval(query))
        except Exception as e:
            return f"Math error: {e}"
