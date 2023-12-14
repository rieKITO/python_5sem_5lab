# ---------------- MODELS ---------------- #
from models.process import Process
from models.thread import Thread
from models.dynamic_library import DynamicLibrary


class OS:
    def __init__(self, processes: list[Process] = None, libraries: list[DynamicLibrary] = None):
        self.processes = []
        self.libraries = []
        if processes:
            for process in processes:
                if type(process) is not Process:
                    raise TypeError
            self.fill_process_list(processes)
        if libraries:
            for library in libraries:
                if type(library) is not DynamicLibrary:
                    raise TypeError
            self.fill_library_list(libraries)

    def fill_process_list(self, processes: list):
        self.processes = []
        if processes:
            for process in processes:
                if type(process) is Process:
                    self.processes.append(process)
                else:
                    raise TypeError
        else:
            raise ValueError

    def fill_library_list(self, libraries: list):
        self.libraries = []
        if libraries:
            for library in libraries:
                if type(library) is DynamicLibrary:
                    self.libraries.append(library)
                else:
                    raise TypeError
        else:
            raise ValueError

    def search_process_from_id(self, process_id: id):
        if process_id:
            if type(process_id) is not int:
                raise TypeError
            for process in self.processes:
                if process.id == process_id:
                    return process
        else:
            raise ValueError
        return None

    def add_process(self, process: Process):
        if process:
            if type(process) is not Process:
                raise TypeError
            self.processes.append(process)
        else:
            raise ValueError

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
            raise ValueError

    def delete_process_from_id(self, process_id: int):
        if process_id is None:
            raise ValueError
        if type(process_id) is not int:
            raise TypeError

        process: Process = self.search_process_from_id(process_id)
        try:
            self.processes.remove(process)
            for library in process.libraries:
                library.remove_process(process)
            process.delete()
        except ValueError:
            raise ValueError

    def delete_library_from_id(self, library_id: int):
        if library_id is None:
            raise ValueError
        if type(library_id) is not int:
            raise TypeError

        library: DynamicLibrary = self.search_library_from_id(library_id)
        try:
            self.libraries.remove(library)
            for process in library.processes:
                process.delete_library_from_id(library_id)
            library.delete()
        except ValueError:
            raise ValueError

    def search_library_from_id(self, library_id: id):
        if library_id:
            if type(library_id) is not int:
                raise TypeError
            for library in self.libraries:
                if library.id == library_id:
                    return library
        else:
            raise ValueError
        return None
