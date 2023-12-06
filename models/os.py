# ---------------- MODELS ---------------- #
from models.process import Process
from models.thread import Thread
from models.dynamic_library import DynamicLibrary


class OS:
    def __init__(self, processes: list[Process] = None):
        self.processes = []
        if processes:
            self.fill_process_list(processes)

    def fill_process_list(self, processes: list):
        if processes:
            for process in processes:
                if type(process) is Process:
                    self.processes.append(process)
                else:
                    raise TypeError
        else:
            raise TypeError

    def search_process_from_id(self, process_id: id):
        if process_id:
            if type(process_id) is not int:
                raise TypeError
            for process in self.processes:
                if process.id == process_id:
                    return process
        else:
            raise TypeError
        return None

    def add_process(self, process: Process):
        if process:
            if type(process) is not Process:
                raise TypeError
            self.processes.append(process)
        else:
            raise TypeError

    def create_process(
            self, process_id: int,
            process_memory: int,
            process_name: str,
            threads: list[Thread] = None,
            libraries: list[DynamicLibrary] = None
    ) -> None:
        if process_id and process_memory and process_name:
            if type(process_id) is not int or type(process_memory) is not int or type(process_name) is not str:
                raise TypeError
            try:
                process = Process(process_id, process_memory, process_name)
                if threads:
                    process.fill_thread_list(threads)
                if libraries:
                    process.fill_library_list(libraries)
                self.add_process(process)
            except ValueError:
                raise ValueError
        else:
            raise TypeError

    def delete_process_from_id(self, process_id: int):
        if type(process_id) is not int:
            raise TypeError

        process: Process = self.search_process_from_id(process_id)
        try:
            self.processes.remove(process)
            process.delete()
        except ValueError:
            raise ValueError
