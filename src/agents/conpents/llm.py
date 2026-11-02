from openai import OpenAI


class LLM:
    def __init__(self, url: str, api_key: str, model_name: str):
        self.model_name = model_name
        self.client = OpenAI(base_url=url, api_key=api_key)

    def generate(self, prompt):
        """Generate text based on the prompt."""
        while True:
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                break
            except Exception as e:
                print(f"Error occurred while generating text: {e}")
                continue