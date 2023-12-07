class Object:
    def __init__(self, id: int, memory: int, name: str):
        if id is None \
                or memory is None \
                or name is None:
            raise ValueError
        elif type(id) is not int \
                or type(memory) is not int \
                or type(name) is not str:
            raise TypeError
        self.id = id
        self.memory = memory
        self.name = name

    def delete(self):
        self.id = None
        self.memory = None
        self.name = None

    def calculate_memory(self):
        return self.memory
