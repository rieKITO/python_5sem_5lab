class Object:
    def __init__(self, id: int, memory: int, name: str):
        self.id = id
        self.memory = memory
        self.name = name

    def delete(self):
        self.id = None
        self.memory = None
        self.name = None

    def calculate_memory(self):
        return self.memory
