# ---------------- MODELS ---------------- #
from models.object import Object
from models.thread import Thread
from models.dynamic_library import DynamicLibrary


class Process(Object):
    def __init__(
            self, id: int,
            memory: int,
            name: str,
            threads: list[Thread] = None,
            libraries: list[DynamicLibrary] = None
    ):
        if id is None \
                or memory is None \
                or name is None:
            raise ValueError
        elif type(id) is not int \
                or type(memory) is not int \
                or type(name) is not str:
            raise TypeError
        elif threads:
            for thread in threads:
                if type(thread) is not Thread:
                    raise TypeError
        elif libraries:
            for library in libraries:
                if type(library) is not DynamicLibrary:
                    raise TypeError

        super().__init__(id, memory, name)
        self.threads = []
        self.libraries = []
        if threads:
            self.fill_thread_list(threads)
        if libraries:
            self.fill_library_list(libraries)

    def fill_thread_list(self, threads: []):
        self.threads = []
        if threads:
            for thread in threads:
                if type(thread) is Thread:
                    self.threads.append(thread)
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

    def add_thread(self, thread: Thread):
        if thread:
            if type(thread) is not Thread:
                raise TypeError
            self.threads.append(thread)
        else:
            raise ValueError

    def create_thread(self, thread_id: int, thread_memory: int, thread_name: str):
        if thread_id and thread_memory and thread_name:
            if (type(thread_id) is not int or type(thread_memory) is not int
                    or type(thread_name) is not str):
                raise TypeError
            try:
                thread = Thread(thread_id, thread_memory, thread_name, self)
                self.add_thread(thread)
            except ValueError:
                raise ValueError
        else:
            raise ValueError

    def delete_thread_from_id(self, thread_id: int):
        if thread_id is None:
            raise ValueError
        if type(thread_id) is not int:
            raise TypeError

        thread: Thread = self.search_thread_from_id(thread_id)
        try:
            self.threads.remove(thread)
        except ValueError:
            raise ValueError

    def add_library(self, library: DynamicLibrary):
        if library:
            if type(library) is not DynamicLibrary:
                raise TypeError
            self.libraries.append(library)
        else:
            raise ValueError

    def create_library(self, library_id: int, library_memory: int, library_name: str):
        if library_id and library_memory and library_name:
            if (type(library_id) is not int or type(library_memory) is not int or
                    type(library_name) is not str):
                raise TypeError
            try:
                library = DynamicLibrary(library_id, library_memory, library_name)
                self.add_library(library)
            except ValueError:
                raise ValueError
        else:
            raise ValueError

    def delete_library_from_id(self, library_id: int):
        if library_id is None:
            raise ValueError
        if type(library_id) is not int:
            raise TypeError

        library: DynamicLibrary = self.search_library_from_id(library_id)
        try:
            self.libraries.remove(library)
        except ValueError:
            raise ValueError

    def search_library_from_id(self, library_id: int):
        if library_id:
            if type(library_id) is not int:
                raise TypeError
            for library in self.libraries:
                if library.id == library_id:
                    return library
        else:
            raise ValueError
        return None

    def search_thread_from_id(self, thread_id: int):
        if thread_id:
            if type(thread_id) is not int:
                raise TypeError
            for thread in self.threads:
                if thread.id == thread_id:
                    return thread
        else:
            raise ValueError
        return None

    def calculate_memory(self) -> int:
        memory = super().calculate_memory()
        for thread in self.threads:
            memory += thread.memory
        for library in self.libraries:
            memory += library.memory
        return memory

    def delete(self):
        super().delete()
        for thread in self.threads:
            self.threads.remove(thread)
        for library in self.libraries:
            self.libraries.remove(library)
        self.threads = []
        self.libraries = []
