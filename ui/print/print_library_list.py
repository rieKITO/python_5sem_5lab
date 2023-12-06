# ---------------- MODELS ---------------- #
from models.dynamic_library import DynamicLibrary

# ---------------- CONFIG ---------------- #
from config import LOGGER


def print_library_list(libraries: list[DynamicLibrary]) -> None:
    id_len = 0
    name_len = 0
    for library in libraries:
        if type(library) is not DynamicLibrary:
            LOGGER.error(TypeError)
            raise TypeError
        else:
            if len(str(library.id)) > id_len:
                id_len = len(str(library.id))
            if len(library.name) > name_len:
                name_len = len(library.name)

    before_name_spaces = ""
    before_memory_spaces = ""
    for i in range(id_len + 3):
        before_name_spaces += " "
    for i in range(name_len + 3):
        before_memory_spaces += " "

    before_memory_spaces = before_memory_spaces[:-3]
    print(f"\nID{before_name_spaces} NAME {before_memory_spaces} MEMORY")
    before_memory_spaces += "   "
    for library in libraries:
        for i in range(len(str(library.id)) - 1):
            before_name_spaces = before_name_spaces[:-1]
        for i in range(len(library.name) - 1):
            before_memory_spaces = before_memory_spaces[:-1]
        print(f"{library.id} {before_name_spaces} {library.name} {before_memory_spaces} {library.memory}")
        for i in range(len(str(library.id)) - 1):
            before_name_spaces += " "
        for i in range(len(str(library.name)) - 1):
            before_memory_spaces += " "
