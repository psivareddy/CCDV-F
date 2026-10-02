# load env variables from .env file
import os

from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()

# Create an Anthropic client

#key = os.getenv("CLAUDE_API_KEY")
#client = Anthropic(api_key=key)
client = Anthropic()
def main():
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=100,        
        messages=[
            {
                "role": "user",
                "content": "Write a short poem about the beauty of nature."
            }
        ]
    )
    print(message.content)

if __name__ == "__main__":
    main()
