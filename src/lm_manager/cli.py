import typer
from lm_manager.manager import LMManager
from lm_manager.adapters.openai_adapter import OpenAIAdapter

app = typer.Typer()
manager = LMManager()


@app.command("register-openai")
def register_openai(name: str = "openai", api_key: str | None = None, model: str = "gpt-3.5-turbo"):
    """Register an OpenAI provider."""
    manager.register(name, OpenAIAdapter(api_key=api_key, model=model))
    typer.echo(f"Registered provider '{name}'")


@app.command()
def list_providers():
    """List registered providers."""
    for p in manager.providers():
        typer.echo(p)


@app.command()
def generate(provider: str, prompt: str):
    """Generate text from a registered provider."""
    out = manager.generate(provider, prompt)
    typer.echo(out)


if __name__ == "__main__":
    app()
