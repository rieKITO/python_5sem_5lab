# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_input import natural_num_input

# ---------------- MODELS ---------------- #
from models.process import Process

# ---------------- UI ---------------- #
# ---------- PRINT ---------- #
from ui.print.print_library_info import print_library_info


def find_library(process: Process):
    if process is None:
        raise ValueError
    if type(process) is not Process:
        raise TypeError

    library = None
    while library is None:
        print("\nEnter the thread ID")
        library_id = natural_num_input()
        library = process.search_library_from_id(library_id)
        if library is None:
            print("Library with this id does not exist!")
    print_library_info(library)
