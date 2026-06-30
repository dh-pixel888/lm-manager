from lm_manager.manager import LMManager


class MockProvider:
    def generate(self, prompt: str, **kwargs) -> str:
        return f"echo:{prompt}"


def test_generate_with_mock_provider():
    m = LMManager()
    m.register("mock", MockProvider())
    assert m.generate("mock", "hello") == "echo:hello"
