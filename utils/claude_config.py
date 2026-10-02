import os
from pathlib import Path

from dotenv import load_dotenv


def find_project_root(start_path: str | None = None) -> Path:
    """Find the project root by walking upward until a .env file or repo root is reached."""
    current = Path(start_path or Path.cwd())
    candidates = [current, *current.parents]
    for path in candidates:
        if (path / ".env").exists():
            return path
        if (path / ".git").exists():
            return path
    return current


def load_env(start_path: str | None = None) -> Path:
    """Load the project .env file if present and return the project root."""
    root = find_project_root(start_path)
    env_file = root / ".env"
    if env_file.exists():
        load_dotenv(dotenv_path=env_file)
    else:
        load_dotenv()
    return root


def get_claude_settings() -> dict:
    """Return normalized Claude settings from environment variables."""
    load_env()
    settings = {
        "model": os.getenv("CLAUDE_MODEL_NAME", "claude-haiku-4-5"),
        "api_key": os.getenv("CLAUDE_API_KEY"),
        "api_url": os.getenv("CLAUDE_API_URL", "https://api.anthropic.com"),
    }
    return settings


def require_claude_settings() -> dict:
    """Validate the Claude settings and raise a clear error when the key is missing."""
    settings = get_claude_settings()
    if not settings["api_key"]:
        raise ValueError("CLAUDE_API_KEY is missing. Add your key to the project .env file.")
    return settings


def get_anthropic_client(api_key: str | None = None):
    """Create and return a configured Anthropic client."""
    from anthropic import Anthropic

    key = api_key or require_claude_settings()["api_key"]
    #return Anthropic(api_key=key)
    return Anthropic()
