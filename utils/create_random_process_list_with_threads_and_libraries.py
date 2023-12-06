import random

# ---------------- MODELS ---------------- #
from models.process import Process
from models.thread import Thread
from models.dynamic_library import DynamicLibrary


def create_random_process_list_with_threads_and_libraries(
        process_number: int,
        threads_number: int,
        libraries_number: int
) -> list[Process]:
    if process_number is None \
            or threads_number is None \
            or libraries_number is None:
        raise ValueError
    elif type(process_number) is not int \
            or type(threads_number) is not int \
            or type(libraries_number) is not int:
        raise TypeError
    else:
        processes: list[Process] = []
        for process_i in range(process_number):
            process: Process = Process(
                process_i + 1,
                random.randint(10, 1024),
                f"process {process_i + 1}"
            )
            for thread_i in range(threads_number):
                thread: Thread = Thread(
                    thread_i + 1,
                    random.randint(10, 1024),
                    f"thread {thread_i + 1}"
                )
                process.add_thread(thread)
            for library_i in range(libraries_number):
                library: DynamicLibrary = DynamicLibrary(
                    library_i + 1,
                    random.randint(10, 1024),
                    f"library {library_i + 1}"
                )
                process.add_library(library)
            processes.append(process)

    return processes
