import random

# ---------------- MODELS ---------------- #
from models.os import OS
from models.process import Process
from models.dynamic_library import DynamicLibrary


def create_and_add_library(os: OS, process: Process):
    if process is None:
        raise ValueError
    if type(process) is not Process:
        raise TypeError

    print("\nEnter the dynamic library name:")
    library_name = str(input("-> "))

    library: DynamicLibrary = DynamicLibrary(
        len(os.libraries) + 1,
        random.randint(1, 1024),
        library_name,
    )
    os.libraries.append(library)
    library.add_process(process)
    process.add_library(library)
