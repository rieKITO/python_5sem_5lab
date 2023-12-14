# ---------------- MODELS ---------------- #
from models.thread import Thread

# ---------------- CONFIG ---------------- #
from config import LOGGER


def print_thread_info(thread: Thread):
    if thread is None:
        LOGGER.error(ValueError)
        raise ValueError
    elif type(thread) is not Thread:
        LOGGER.error(TypeError)
        raise TypeError
    else:
        print(
            f"\nThread id: {thread.id}\n"
            f"Thread name: {thread.name}\n"
            f"Thread memory: {thread.calculate_memory()}\n"
        )
