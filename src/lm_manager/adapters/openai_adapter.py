try:
    import openai
except Exception:  # pragma: no cover - optional dependency
    openai = None


class OpenAIAdapter:
    """Adapter for OpenAI's Chat Completions API.

    Usage:
        OpenAIAdapter(api_key="...", model="gpt-3.5-turbo")
    """

    def __init__(self, api_key: str | None = None, model: str = "gpt-3.5-turbo") -> None:
        if api_key and openai is not None:
            openai.api_key = api_key
        self.model = model

    def generate(self, prompt: str, **kwargs) -> str:
        if openai is None:
            raise RuntimeError("openai package is not installed")
        if not getattr(openai, "api_key", None):
            raise RuntimeError("OpenAI API key not configured (set OpenAI api_key or env OPENAI_API_KEY)")
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs,
        )
        return resp.choices[0].message.content.strip()
