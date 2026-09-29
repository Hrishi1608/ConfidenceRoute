from .base_agent import BaseAgent


class WriterAgent(BaseAgent):
    def write(self, research):
        prompt = f"""
You are a writing agent.

Your job is to transform the provided research into
a clear, well-structured answer.

Research:
{research}

Write a concise and useful final response based only
on the provided research.
"""

        return self.run(prompt)