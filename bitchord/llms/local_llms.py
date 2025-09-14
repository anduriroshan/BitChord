import asyncio
from pathlib import Path
from llama_cpp import Llama  # pip install llama-cpp-python

class LocalLLM:
    """
    Minimal wrapper around a local quantized model (e.g., BitNet 1.58-bit GGUF).
    Usage:
        llm = LocalLLM(model_path="models/bitnet-1.58b.gguf")
        text = await llm.generate("Hello world")
    """

    def __init__(self, model_path: str, n_ctx: int = 2048, n_threads: int = 4):
        model_file = Path(model_path)
        if not model_file.exists():
            raise FileNotFoundError(
                f"Model file not found at {model_path}. "
                "Download a GGUF quantized BitNet model first."
            )
        self.model = Llama(model_path=str(model_file), n_ctx=n_ctx, n_threads=n_threads)

    async def generate(self, prompt: str, max_tokens: int = 256) -> str:
        """
        Run the local model asynchronously so it matches our LLM interface.
        """
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None, lambda: self.model(prompt, max_tokens=max_tokens)
        )
        return result["choices"][0]["text"].strip()
