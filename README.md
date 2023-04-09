## VoAI v0.0.1 - tool designed for working with ChatGPT API
## Change log
- First release
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