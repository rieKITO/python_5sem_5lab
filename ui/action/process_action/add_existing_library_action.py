import random

# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_input import natural_num_input

# ---------------- MODELS ---------------- #
from models.os import OS
from models.process import Process
from models.dynamic_library import DynamicLibrary

# ---------------- UI ---------------- #
# ---------- ACTION ---------- #
# ---------- PRINT ---------- #
from ui.print.print_library_list import print_library_list


def add_existing_library(os: OS, process: Process):
    if process is None:
        raise ValueError
    if type(process) is not Process:
        raise TypeError

    print_library_list(os.libraries)
    library = None
    library_id = None
    while library is None:
        print("\nEnter the dynamic library ID")
        library_id = natural_num_input()
        if process.search_library_from_id(library_id) is not None:
            print("This library is already linked to this process")
        else:
            library: DynamicLibrary = os.search_library_from_id(library_id)
            if library is None:
                print("Library with this id does not exist!")

    if library is not None:
        library.add_process(process)
        process.add_library(library)
    else:
        raise ValueError
