import asyncio
import importlib.resources
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM

class LocalLLM:
    """
    Minimal wrapper around a local quantized model using transformers.
    This is designed for a fully offline package.
    """

    def __init__(self, model_filename: str = "ggml-model-i2_s.gguf"):
        try:
            with importlib.resources.path("bitchord.llms", "models") as models_dir_context:
                models_path = Path(str(models_dir_context))
                
                tokenizer_path = models_path
                model_file_path = models_path / model_filename

                if not model_file_path.is_file():
                    raise FileNotFoundError(f"Model file not found: {model_file_path}")

                self.tokenizer = AutoTokenizer.from_pretrained(str(tokenizer_path))
                self.model = AutoModelForCausalLM.from_pretrained(str(model_file_path))

        except Exception as e:
            raise RuntimeError(
                f"Failed to load offline model/tokenizer. Ensure files are in 'bitchord/llms/models/'. Error: {e}"
            )

    async def generate(self, prompt: str, max_tokens: int = 256) -> str:
        """
        Run the local model asynchronously so it matches our LLM interface.
        """
        loop = asyncio.get_event_loop()

        def _blocking_generate():
            inputs = self.tokenizer(prompt, return_tensors="pt")
            outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
            text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            # The decoded text might include the prompt.
            if text.startswith(prompt):
                return text[len(prompt):].strip()
            return text.strip()

        result = await loop.run_in_executor(None, _blocking_generate)
        return result