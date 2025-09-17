import asyncio
import importlib.resources
from pathlib import Path
from llama_cpp import Llama

class LocalLLM:
    """
    Minimal wrapper around a local GGUF model using llama-cpp-python.
    This is designed for a fully offline package.
    """

    def __init__(self, model_filename: str = "ggml-model-i2_s.gguf"):
        try:
            with importlib.resources.path("bitchord.llms", "models") as models_dir_context:
                models_path = Path(str(models_dir_context))
                model_file_path = models_path / model_filename

                if not model_file_path.is_file():
                    raise FileNotFoundError(f"Model file not found: {model_file_path}")

                self.model = Llama(model_path=str(model_file_path), verbose=False)

        except Exception as e:
            raise RuntimeError(
                f"Failed to load offline model. Ensure GGUF file is in 'bitchord/llms/models/'. Error: {e}"
            )

    async def generate(self, prompt: str, max_tokens: int = 256) -> str:
        """
        Run the local model asynchronously so it matches our LLM interface.
        """
        loop = asyncio.get_event_loop()

        def _blocking_generate():
            # llama-cpp-python returns a dict, we are interested in the text of the first choice.
            output = self.model(prompt, max_tokens=max_tokens)
            return output["choices"][0]["text"].strip()

        result = await loop.run_in_executor(None, _blocking_generate)
        return result
