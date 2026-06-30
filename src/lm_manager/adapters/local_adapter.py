class LocalAdapter:
    """Placeholder adapter for local LLMs (e.g., llama.cpp, local server).

    Implement `generate(prompt, **kwargs)` to integrate a local model.
    """

    def __init__(self, config: dict | None = None) -> None:
        self.config = config or {}

    def generate(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError("LocalAdapter.generate is a placeholder; implement your local LLM integration")
