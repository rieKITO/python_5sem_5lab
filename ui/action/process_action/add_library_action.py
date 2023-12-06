import random

# ---------------- MODELS ---------------- #
from models.process import Process


def add_library(process: Process):
    if process is None:
        raise ValueError
    if type(process) is not Process:
        raise TypeError

    print("\nEnter the dynamic library name:")
    library_name = str(input("-> "))
    process.create_library(
        len(process.libraries) + 1,
        random.randint(1, 1024),
        library_name,
    )
