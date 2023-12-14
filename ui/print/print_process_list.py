# ---------------- MODELS ---------------- #
from models.process import Process

# ---------------- CONFIG ---------------- #
from config import LOGGER


def print_process_list(processes: list[Process]) -> None:
    id_len = 0
    name_len = 0
    memory_len = 0
    for process in processes:
        if type(process) is not Process:
            LOGGER.error(TypeError)
            raise TypeError
        else:
            if len(str(process.id)) > id_len:
                id_len = len(str(process.id))
            if len(process.name) > name_len:
                name_len = len(process.name)
            if len(str(process.calculate_memory())) > memory_len:
                memory_len = len(str(process.calculate_memory()))

    before_name_spaces = ""
    before_memory_spaces = ""
    before_libraries_spaces = ""
    for i in range(id_len + 3):
        before_name_spaces += " "
    for i in range(name_len + 3):
        before_memory_spaces += " "
    for i in range(memory_len + 3):
        before_libraries_spaces += " "

    before_memory_spaces = before_memory_spaces[:-3]
    before_libraries_spaces = before_libraries_spaces[:-6]
    print(f"\nID{before_name_spaces} NAME {before_memory_spaces} MEMORY {before_libraries_spaces} LIBRARIES")
    before_memory_spaces += "   "
    before_libraries_spaces += "      "
    for process in processes:
        for i in range(len(str(process.id)) - 1):
            before_name_spaces = before_name_spaces[:-1]
        for i in range(len(process.name) - 1):
            before_memory_spaces = before_memory_spaces[:-1]
        for i in range(len(str(process.calculate_memory()))):
            before_libraries_spaces = before_libraries_spaces[:-1]
        process_libraries = ', '.join(str(el.id) for el in process.libraries)
        print(f"{process.id} {before_name_spaces} {process.name} {before_memory_spaces} {process.calculate_memory()} {before_libraries_spaces} {process_libraries}")
        for i in range(len(str(process.id)) - 1):
            before_name_spaces += " "
        for i in range(len(str(process.name)) - 1):
            before_memory_spaces += " "
        for i in range(len(str(process.calculate_memory()))):
            before_libraries_spaces += " "
    print('\n')
