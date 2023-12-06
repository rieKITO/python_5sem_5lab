import random

# ---------------- MODELS ---------------- #
from models.os import OS


def add_process(os: OS):
    if os is None:
        raise ValueError
    if type(os) is not OS:
        raise TypeError

    print("\nEnter the process name:")
    process_name = str(input("-> "))
    os.create_process(
        len(os.processes) + 1,
        random.randint(1, 1024),
        process_name,
    )
