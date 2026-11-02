import json


class Memory:
    '''A class for agent memory'''

    def __init__(self):
        self.memory = []

    def add(self, role, content, **kwargs):
        self.memory.append({"role": role, "content": content, **kwargs})

    def get_memory(self):
        return self.memory
    
    def clear(self):
        self.memory.clear()

    def save(self, file_path):
        with open(file_path, "w") as f:
            json.dump(self.memory, f)

    def load(self, file_path):
        with open(file_path, "r") as f:
            self.memory = json.load(f)
