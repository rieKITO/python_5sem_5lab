from models.object import Object
from models.dynamic_library import DynamicLibrary


class Thread(Object):
    def __init__(self, id: int, memory: int, name: str):
        super().__init__(id, memory, name)

    def delete(self):
        super().delete()
