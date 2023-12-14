# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_input import natural_num_input

# ---------------- MODELS ---------------- #
from models.os import OS
from models.process import Process
from models.dynamic_library import DynamicLibrary


def delete_library(os: OS, process: Process):
    if process is None:
        raise ValueError
    if type(process) is not Process:
        raise TypeError

    library = None
    library_id = None
    while library is None:
        print("\nEnter the dynamic library ID")
        library_id = natural_num_input()
        library: DynamicLibrary = process.search_library_from_id(library_id)
        if library is None:
            print("Library with this id does not exist!")

    try:
        library.remove_process_from_id(process.id)
        process.delete_library_from_id(library_id)
        if len(library.processes) == 0:
            os.libraries.remove(library)
            library.delete()
    except ValueError:
        raise ValueError

