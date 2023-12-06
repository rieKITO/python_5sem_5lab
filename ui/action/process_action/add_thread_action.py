import random

# ---------------- MODELS ---------------- #
from models.process import Process


def add_thread(process: Process):
    if process is None:
        raise ValueError
    if type(process) is not Process:
        raise TypeError

    print("\nEnter the thread name:")
    thread_name = str(input("-> "))
    process.create_thread(
        len(process.threads) + 1,
        random.randint(1, 1024),
        thread_name,
    )
