import sys
from pathlib import Path

import anthropic

if __package__ in (None, ""):
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from utils.claude_config import require_claude_settings, 

settings = require_claude_settings()

claude_api_key = settings["api_key"]
claude_api_url = settings["api_url"]
claude_model_name = settings["model"]

print(f"claude_model_name: {claude_model_name}")
print(f"claude_api_key set: {bool(claude_api_key)}")
# print(f"claude_api_key set: {claude_api_key}")
print(f"claude_api_url: {claude_api_url}")

client = anthropic.Client(api_key=claude_api_key)

message = client.messages.create(
    model=claude_model_name,
    system="You are Batman, the Dark Knight and Protector of Gotham City.",
    messages=[
        {
            "role":"user",
            "content":"How is Gotham City doing Today?",
        }
    ],
    max_tokens=100
)

for msg in message.content:
    if msg.type == "text":
        print(f"{msg.type} : {msg.text}")
