## VoAI v0.0.4 - tool designed for working with ChatGPT API
## Change log
- Removed `ask_with_context` method from `GPT35Turbo`
- Added `new_chat` method for `GPT35Turbo` to create `GPT35TurboChat` instance, now to use `ask_with_context` you need to create it
- Added `ask` method for `GPT35TurboChat` is same as `ask_with_context` of `GPT35Turbo` in v0.0.3
- Added `clear` method for `GPT35TurboChat` which clears whole chat
- Added `regenerate` method for `GPT35TurboChat` which regenerates response using index of context array returned by `get_context` method of the same struct
## Usage
```python
# here is cli example of chat gpt api
import voai

KEY = "your-api-key"

gpt = voai.GPT35Turbo(KEY)
chat = gpt.new_chat()
while True:
    query = input("> ")

    response = chat.ask(query)
    print(response)
```
## Using libraries
- <a href="https://pypi.org/project/requests/">requests</a>