import requests


class BaseAgent:
    def __init__(self, model="llama3:8b"):
        self.model = model
        self.ollama_url = "http://localhost:11434/api/generate"

    def run(self, prompt):
        response = requests.post(
            self.ollama_url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        data = response.json()
        return data["response"]


if __name__ == "__main__":
    agent = BaseAgent()

    answer = agent.run(
        "Explain what an AI agent is in one sentence."
    )

    print(answer)