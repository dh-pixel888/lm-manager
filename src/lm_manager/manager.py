from typing import Any, Dict


class LMManager:
    """Simple manager for registering and calling LM providers."""

    def __init__(self) -> None:
        self._providers: Dict[str, Any] = {}

    def register(self, name: str, provider: Any) -> None:
        """Register a provider instance under `name`."""
        self._providers[name] = provider

    def providers(self):
        return list(self._providers.keys())

    def generate(self, provider_name: str, prompt: str, **kwargs) -> str:
        """Call the named provider's `generate` method."""
        if provider_name not in self._providers:
            raise KeyError(f"Provider '{provider_name}' not registered")
        provider = self._providers[provider_name]
        if not hasattr(provider, "generate"):
            raise TypeError("Provider must implement a `generate(prompt, **kwargs)` method")
        return provider.generate(prompt, **kwargs)
