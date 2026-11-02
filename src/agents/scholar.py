from .conpents.agent import Agent, AgentConfig
from .prompts import PLANER_SYSTME_PROMPT


class ScholarConfig(AgentConfig):
    '''A dataclass for scholar agent configuration'''

    def __init__(self):
        super().__init__()
        self.name: str = "Scholar"
        self.description: str = "A paper reading agent"
        self.system_prompt: str = PLANER_SYSTME_PROMPT


class Scholar:
    '''A pipeline for the paper reading agent'''

    def __init__(self):
        self.planer = Agent(ScholarConfig())

    def run(self, research_goal):
        '''Run the scholar agent with a given research goal'''
        prompt = f"Please create a detailed plan for the following research goal: {research_goal}"
        response = self.planer.run(prompt)
        return response


if __name__ == "__main__":
    scholar = Scholar()
    research_goal = "Develop a new algorithm for image classification using deep learning."
    plan = scholar.run(research_goal)
    print(plan)