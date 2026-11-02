from dataclasses import dataclass 
import os 

from .config import LLMConfig
from .llm import LLM
from .tools import TOOLS, TOOL_FUNCTIONS 
from .memory import Memory


@dataclass
class AgentConfig:
    '''A dataclass for agent configuration'''
    name: str = "Agent"
    description: str = "A generic agent"

    # LLM configuration
    url: str = LLMConfig.url
    api_key: str = LLMConfig.api_key
    model_name: str = LLMConfig.model_name
    system_prompt: str = LLMConfig.system_prompt

    # Tool configuration
    # Memory configuration 
    save_memory_path: str = "memory.json"


class Agent:
    '''An agent class'''

    def __init__(self, config: AgentConfig):
        self.config = config
        self.name = config.name
        self.description = config.description
        self.llm = LLM(config)
        self.memory = Memory(config)
        self.tools = TOOLS
        self.tool_functions = TOOL_FUNCTIONS

    def run(self, prompt):
        '''Run the agent with a given prompt'''
        self.memory.add(role="user", content=prompt)
        response = self.llm.generate(prompt)
        self.memory.add(role="agent", content=response)
        return response