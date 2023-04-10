## VoAI v0.0.3 - tool designed for working with ChatGPT API
## Change log
- Added `ask_with_context` method for `GPT35Turbo` that will do same as just `ask` method but will remember previous context
## Usage
```python
import voai

KEY = "your-api-key"

chat = voai.GPT35Turbo(KEY)
while True:
    query = input("> ")

    response = chat.ask(query)
    print(response)
```
## Using libraries
- <a href="https://pypi.org/project/requests/">requests</a>