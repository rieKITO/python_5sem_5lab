# ---------------- MODELS ---------------- #
from models.thread import Thread

# ---------------- CONFIG ---------------- #
from config import LOGGER


def print_thread_list(threads: list[Thread]) -> None:
    id_len = 0
    name_len = 0
    for thread in threads:
        if type(thread) is not Thread:
            LOGGER.error(TypeError)
            raise TypeError
        else:
            if len(str(thread.id)) > id_len:
                id_len = len(str(thread.id))
            if len(thread.name) > name_len:
                name_len = len(thread.name)

    before_name_spaces = ""
    before_memory_spaces = ""
    for i in range(id_len + 3):
        before_name_spaces += " "
    for i in range(name_len + 3):
        before_memory_spaces += " "

    before_memory_spaces = before_memory_spaces[:-3]
    print(f"\nID{before_name_spaces} NAME {before_memory_spaces} MEMORY")
    before_memory_spaces += "   "
    for thread in threads:
        for i in range(len(str(thread.id)) - 1):
            before_name_spaces = before_name_spaces[:-1]
        for i in range(len(thread.name) - 1):
            before_memory_spaces = before_memory_spaces[:-1]
        print(f"{thread.id} {before_name_spaces} {thread.name} {before_memory_spaces} {thread.memory}")
        for i in range(len(str(thread.id)) - 1):
            before_name_spaces += " "
        for i in range(len(str(thread.name)) - 1):
            before_memory_spaces += " "
