import requests
from typing import List, Dict, Tuple

class Chat:
    def ask(self, query: str):
        pass

class GPT35TurboChat(Chat):
    def __init__(self, key: str):
        self._key = key
        self._context = []

    def _ask_with_context(self, context: List[Dict[str, str]]) -> str:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._key}",
        }

        payload = {
            "model": "gpt-3.5-turbo",
            "messages": context
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 300:
            raise RuntimeError(f"{response.status_code} {response.json()['error']['message']}")

        data = response.json()
        message = data["choices"][0]["message"]["content"]

        return message

    def ask(self, query: str) -> str:
        context = []
        for cquery, answear in self._context:
            context += [{ "role": "user", "content": cquery }, { "role": "assistant", "content": answear }]
        
        context.append({
            "role": "user",
            "content": query
        })

        response = self._ask_with_context(context)

        self._context.append((query, response))

        return response
    
    def regenerate(self, i: int):
        context = []
        for cquery, answear in self._context[:i]:
            context += [{ "role": "user", "content": cquery }, { "role": "assistant", "content": answear }]

        context.append({
            "role": "user",
            "content": self._context[i][0]
        })

        response = self._ask_with_context(context)
        context.append({
            "role": "assistant",
            "content": response
        })

        self._context = []

        j = 0
        while j < len(context):
            qr = ()
            for t in range(2):
                qr += (context[j+t]["content"],)
            
            self._context.append(qr)
            j += 2

        return response

    def get_context(self) -> Tuple[List[str], List[str]]:
        return ([query for query, _ in self._context], [response for _, response in self._context])

    def clear(self):
        self._context = []

class GPT35Turbo:
    def __init__(self, key: str):
        self._key = key
        self._history = []

    def ask(self, query: str) -> str:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._key}",
        }

        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 300:
            raise RuntimeError(f"{response.status_code} {response.json()['error']['message']}")

        data = response.json()
        return data["choices"][0]["message"]["content"]
    
    def new_chat(self) -> GPT35TurboChat:
        return GPT35TurboChat(self._key)
    
class Davinci3: # continues text, for example if you ask him "Hello, world" he will return "!" 
    def __init__(self, key: str):
        self.key = key

    def ask(self, query: str, temperature: float = 0.5) -> str:
        url = "https://api.openai.com/v1/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.key}",
        }

        payload = {
            "model": "text-davinci-003",
            "prompt": query,
            "temperature": temperature,
            "n": 1,
            "stop": "\n"
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 300:
            raise RuntimeError(f"{response.status_code} {response.json()['error']['message']}")

        data = response.json()
        return data["choices"][0]["text"]