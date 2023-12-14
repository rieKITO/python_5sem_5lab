import random

# ---------------- MODELS ---------------- #
from models.process import Process
from models.thread import Thread


def add_thread(process: Process):
    if process is None:
        raise ValueError
    if type(process) is not Process:
        raise TypeError

    print("\nEnter the thread name:")
    thread_name = str(input("-> "))
    thread: Thread = Thread(
        len(process.threads) + 1,
        random.randint(1, 1024),
        thread_name,
        process
    )
    process.add_thread(thread)
