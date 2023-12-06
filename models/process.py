# ---------------- MODELS ---------------- #
from models.object import Object
from models.thread import Thread
from models.dynamic_library import DynamicLibrary


class Process(Object):
    def __init__(self, id: int, memory: int, name: str, threads: list[Thread] = None,
                 libraries: list[DynamicLibrary] = None):
        super().__init__(id, memory, name)
        self.threads = []
        self.libraries = []
        if threads:
            self.fill_thread_list(threads)
        if libraries:
            self.fill_library_list(libraries)

    def fill_thread_list(self, threads: []):
        if threads:
            for thread in threads:
                if type(thread) is Thread:
                    self.threads.append(thread)
                else:
                    raise TypeError
        else:
            raise TypeError

    def fill_library_list(self, libraries: list):
        if libraries:
            for library in libraries:
                if type(library) is DynamicLibrary:
                    self.libraries.append(library)
                else:
                    raise TypeError
        else:
            raise TypeError

    def add_thread(self, thread: Thread):
        if type(thread) is not Thread:
            raise TypeError
        self.threads.append(thread)

    def create_thread(self, thread_id: int, thread_memory: int, thread_name: str):
        if thread_id and thread_memory and thread_name:
            if (type(thread_id) is not int or type(thread_memory) is not int
                    or type(thread_name) is not str):
                raise TypeError
            try:
                thread = Thread(thread_id, thread_memory, thread_name)
                self.add_thread(thread)
            except ValueError:
                raise ValueError
        else:
            raise TypeError

    def delete_thread_from_id(self, thread_id: int):
        if type(thread_id) is not int:
            raise TypeError

        thread: Thread = self.search_thread_from_id(thread_id)
        try:
            self.threads.remove(thread)
            thread.delete()
        except ValueError:
            raise ValueError

    def add_library(self, library: DynamicLibrary):
        if type(library) is not DynamicLibrary:
            raise TypeError
        self.libraries.append(library)

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
            raise TypeError

    def delete_library_from_id(self, library_id: int):
        if type(library_id) is not int:
            raise TypeError

        library: DynamicLibrary = self.search_library_from_id(library_id)
        try:
            self.libraries.remove(library)
            library.delete()
        except ValueError:
            raise ValueError

    def search_library_from_id(self, library_id):
        if library_id:
            if type(library_id) is not int:
                raise TypeError
            for library in self.libraries:
                if library.id == library_id:
                    return library
        else:
            raise TypeError
        return None

    def search_thread_from_id(self, thread_id):
        if thread_id:
            if type(thread_id) is not int:
                raise TypeError
            for thread in self.threads:
                if thread.id == thread_id:
                    return thread
        else:
            raise TypeError
        return None

    def calculate_memory(self):
        memory = super().calculate_memory()
        for thread in self.threads:
            memory += thread.memory
        for library in self.libraries:
            memory += library.memory

    def delete(self):
        super().delete()
        for thread in self.threads:
            self.threads.remove(thread)
        for library in self.libraries:
            self.libraries.remove(library)
