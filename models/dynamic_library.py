# ---------------- MODELS ---------------- #
from models.object import Object


class DynamicLibrary(Object):
    def __init__(self, id: int, memory: int, name: str, processes=None):
        from models.process import Process
        if id is None \
                or memory is None \
                or name is None:
            raise ValueError
        elif type(id) is not int \
                or type(memory) is not int \
                or type(name) is not str:
            raise TypeError
        super().__init__(id, memory, name)
        self.processes: list[Process] = []
        if processes:
            for processes in processes:
                if type(processes) is not Process:
                    raise TypeError
            self.processes = processes

    def add_process(self, process) -> None:
        from models.process import Process
        if process is None:
            raise ValueError
        elif type(process) is not Process:
            raise TypeError
        else:
            self.processes.append(process)

    def search_process_from_id(self, process_id):
        if process_id:
            if type(process_id) is not int:
                raise TypeError
            for process in self.processes:
                if process.id == process_id:
                    return process
        else:
            raise ValueError
        return None

    def remove_process_from_id(self, process_id: int):
        from models.process import Process
        if process_id is None:
            raise ValueError
        elif type(process_id) is not int:
            raise TypeError
        else:
            process: Process = self.search_process_from_id(process_id)
            self.processes.remove(process)

    def delete(self):
        super().delete()
        self.processes = None
