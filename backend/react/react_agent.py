from backend.agents.base_agent import BaseAgent
from backend.tools.web_search import web_search


class ReActAgent(BaseAgent):
    def __init__(self, max_steps=5, model="llama3:8b"):
        super().__init__(model=model)
        self.max_steps = max_steps

    def run_task(self, task):
        history = []

        for step in range(self.max_steps):
            prompt = self._build_prompt(task, history)

            response = self.run(prompt)

            history.append({
                "step": step + 1,
                "response": response
            })

            if "Final Answer:" in response:
                final_answer = response.split(
                    "Final Answer:", 1
                )[1].strip()

                return {
                    "answer": final_answer,
                    "steps": history
                }

            action = self._extract_action(response)

            if action is None:
                history.append({
                    "step": step + 1,
                    "observation": response
                })

                continue

            if action.startswith("web_search:"):
                query = action.split(
                    "web_search:", 1
                )[1].strip()

                results = web_search(query)

                observation = self._format_results(results)

                history.append({
                    "step": step + 1,
                    "observation": observation
                })

        return {
            "answer": "Maximum reasoning steps reached.",
            "steps": history
        }

    def _build_prompt(self, task, history):
        prompt = f"""
You are a ReAct-style AI agent.

You must solve the following task:

Task:
{task}

You can use this action:

Action: web_search: <search query>

When you need external information, use the web_search action.

After receiving search results, continue reasoning.

When you are ready to answer, use:

Final Answer: <your answer>

Previous reasoning:
{history}

Respond with either:
Thought: <your reasoning>
Action: web_search: <query>

OR:

Thought: <your reasoning>
Final Answer: <answer>
"""

        return prompt

    def _extract_action(self, response):
        marker = "Action:"

        if marker not in response:
            return None

        action = response.split(
            marker, 1
        )[1].splitlines()[0].strip()

        return action

    def _format_results(self, results):
        formatted = []

        for result in results:
            formatted.append(
                f"Title: {result['title']}\n"
                f"URL: {result['url']}\n"
                f"Snippet: {result['snippet']}"
            )

        return "\n\n".join(formatted)