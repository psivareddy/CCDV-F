import os
import sys
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


def setup_project_path(start_path: str | None = None) -> Path:
    """Find the project root and add it to sys.path for notebook imports."""
    root = find_project_root(start_path)
    root_text = str(root)
    if root_text not in sys.path:
        sys.path.insert(0, root_text)
    return root


def load_env(start_path: str | None = None) -> Path:
    """Load the project .env file if present and return the project root."""
    root = setup_project_path(start_path)
    env_file = root / ".env"
    if env_file.exists():
        load_dotenv(dotenv_path=env_file, override=True)
    else:
        load_dotenv(override=True)
    return root


def clean_env_value(value: str | None) -> str | None:
    """Normalize simple env values and remove accidental inline comments."""
    if value is None:
        return None
    return value.split(" #", 1)[0].strip()


def get_claude_settings() -> dict:
    """Return normalized Claude settings from environment variables."""
    load_env()
    model = os.getenv("CLAUDE_MODEL") or os.getenv("CLAUDE_MODEL_NAME") or "claude-haiku-4-5"
    settings = {
        "model": clean_env_value(model),
        "api_key": clean_env_value(os.getenv("CLAUDE_API_KEY")),
        "api_url": clean_env_value(os.getenv("CLAUDE_API_URL", "https://api.anthropic.com")),
    }
    return settings


def require_claude_settings() -> dict:
    """Validate the Claude settings and raise a clear error when the key is missing."""
    settings = get_claude_settings()
    if not settings["api_key"]:
        raise ValueError("CLAUDE_API_KEY is missing. Add your key to the project .env file.")
    return settings


def setup_notebook_claude(start_path: str | None = None) -> dict:
    """Prepare notebook imports/env and return validated Claude settings."""
    setup_project_path(start_path)
    return require_claude_settings()


def get_anthropic_client(api_key: str | None = None):
    """Create and return a configured Anthropic client."""
    from anthropic import Anthropic

    key = api_key or require_claude_settings()["api_key"]
    return Anthropic(api_key=key)
