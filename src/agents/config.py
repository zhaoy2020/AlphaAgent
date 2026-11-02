import os 


class LLMConfig:
    '''A dataclass for LLM configuration'''

    def __init__(self, env: str = 'CAU_API_KEY'):
        url: str = 'https://openai.cau.edu.cn/v1'
        api_key: str = os.environ.get(env, '')
        model_name: str = 'qwen3.6'
        system_prompt: str = "You are a helpful assistant."