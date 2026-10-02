# CCDV-F Claude SDK Labs

This project contains practice labs for the **Claude Certified Developer - Foundation** certification. The examples use the Claude SDK to explore core developer workflows such as message creation, model capabilities, tool use, web search, and retrieval-augmented generation.

## Project Structure

- `getting-started/` - Basic Claude Messages API examples.
- `Model-Capabilites/` - Model behavior and capability experiments.
- `Tool-Use/` - Claude tool-use labs, including web search.
- `RAG/` - Retrieval and vector-loading experiments.
- `utils/` - Shared configuration helpers.

## Setup

Install dependencies with `uv`:

```powershell
uv sync
```

Create a `.env` file from `.env.example` and add your Claude API key:

```powershell
copy .env.example .env
```

Then run scripts or notebooks using the project environment:

```powershell
uv run python main.py
```

## Notes

These labs are for hands-on certification practice and experimentation with the Claude SDK. Keep API keys and local environment files out of source control.
