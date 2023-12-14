# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_input import natural_num_input

# ---------------- MODELS ---------------- #
from models.os import OS
from models.dynamic_library import DynamicLibrary

# ---------------- UI ---------------- #
# ---------- PRINT ---------- #
from ui.print.print_library_list import print_library_list


def delete_library(os: OS):
    if os is None:
        raise ValueError
    if type(os) is not OS:
        raise TypeError

    print_library_list(os.libraries)

    library = None
    library_id = None
    while library is None:
        print("\nEnter the dynamic library ID")
        library_id = natural_num_input()
        library: DynamicLibrary = os.search_library_from_id(library_id)
        if library is None:
            print("Library with this id does not exist!")

    try:
        os.delete_library_from_id(library_id)
    except ValueError:
        raise ValueError
