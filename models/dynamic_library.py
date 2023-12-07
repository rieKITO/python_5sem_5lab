# ---------------- MODELS ---------------- #
from models.object import Object


class DynamicLibrary(Object):
    def __init__(self, id: int, memory: int, name: str):
        if id is None \
                or memory is None \
                or name is None:
            raise ValueError
        elif type(id) is not int \
                or type(memory) is not int \
                or type(name) is not str:
            raise TypeError
        super().__init__(id, memory, name)

    def delete(self):
        super().delete()
