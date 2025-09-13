import os
import aiohttp
from abc import ABC, abstractmethod
from bitchord.core.context import Context


class LLM(ABC):
    """
    Base class for all LLM wrappers.
    """

    def __init__(self, model: str):
        self.model = model

    @abstractmethod
    async def generate(self, prompt: str, context: Context) -> str:
        pass


class GroqLLM(LLM):
    """
    Groq API LLM wrapper.
    """

    def __init__(self, model: str = "meta-llama/llama-4-scout-17b-16e-instruct", api_key: str = None):
        super().__init__(model)
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("Groq API key not provided. Set GROQ_API_KEY env variable.")

    async def generate(self, prompt: str, context: Context) -> str:
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        messages = context.history + [{"role": "user", "content": prompt}]

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=payload) as resp:
                data = await resp.json()
                if "choices" in data and data["choices"]:
                    return data["choices"][0]["message"]["content"]
                else:
                    return f"[Groq API Error] {data}"
