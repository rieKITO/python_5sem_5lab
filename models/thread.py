# ---------------- MODELS ---------------- #
from models.object import Object


class Thread(Object):
    def __init__(self, id: int, memory: int, name: str, process):
        from models.process import Process
        if id is None \
                or memory is None \
                or name is None \
                or process is None:
            raise ValueError
        elif type(id) is not int \
                or type(memory) is not int \
                or type(name) is not str \
                or type(process) is not Process:
            raise TypeError
        super().__init__(id, memory, name)
        self.process: Process = process

    def set_process(self, process):
        from models.process import Process
        if process is None:
            raise ValueError
        elif type(process) is not Process:
            raise TypeError
        else:
            self.process = process

    def delete(self):
        super().delete()
        self.process = None
