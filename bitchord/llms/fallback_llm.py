class FallbackLLM:
    """
    Try primary LLM first, fall back to secondary if any exception occurs.
    """
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary

    async def generate(self, prompt: str, **kwargs) -> str:
        try:
            return await self.primary.generate(prompt, **kwargs)
        except Exception as e:
            print(f"[FallbackLLM] Primary failed: {e}. Switching to local model.")
            return await self.secondary.generate(prompt, **kwargs)
