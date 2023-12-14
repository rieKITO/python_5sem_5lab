# ---------------- MODELS ---------------- #
from models.process import Process

# ---------------- UI ---------------- #
# ---------- PRINT ---------- #
from ui.print.print_thread_list import print_thread_list
from ui.print.print_library_list import print_library_list

# ---------------- CONFIG ---------------- #
from config import LOGGER


def print_process_info(process: Process):
    if process is None:
        LOGGER.error(ValueError)
        raise ValueError
    elif type(process) is not Process:
        LOGGER.error(TypeError)
        raise TypeError
    else:
        print(
            f"\nProcess id: {process.id}\n"
            f"Process name: {process.name}\n"
            f"Process memory: {process.calculate_memory()}\n"
        )
        print("----- Thread list -----")
        print_thread_list(process.threads)
        print("\n----- Dynamic library list -----")
        print_library_list(process.libraries)
