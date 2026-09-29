from .base_agent import BaseAgent


class VerifierAgent(BaseAgent):
    def verify(self, answer):
        prompt = f"""
You are a verification agent.

Review the following answer for factual consistency,
clarity, and obvious errors.

Answer:
{answer}

Identify any problems you find and explain what should
be corrected. If the answer appears reasonable, say so.
"""

        return self.run(prompt)