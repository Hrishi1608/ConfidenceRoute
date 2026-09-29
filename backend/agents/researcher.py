from .base_agent import BaseAgent


class ResearcherAgent(BaseAgent):
    def research(self, task):
        prompt = f"""
You are a research agent.

Your job is to analyze the user's task and provide
relevant, factual information that can help solve it.

Task:
{task}

Provide your research clearly and concisely.
"""

        return self.run(prompt)