from typing import Any, Dict, List


class Context:
    """
    Holds conversation state and history.
    """

    def __init__(self):
        self.state: Dict[str, Any] = {}
        self.history: List[Dict[str, Any]] = []

    def add_to_history(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def get_history(self) -> List[Dict[str, Any]]:
        return self.history

    def set(self, key: str, value: Any):
        self.state[key] = value

    def get(self, key: str, default=None):
        return self.state.get(key, default)
