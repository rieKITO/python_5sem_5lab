import random

# ---------------- MODELS ---------------- #
from models.process import Process
from models.thread import Thread
from models.dynamic_library import DynamicLibrary


def create_random_process_list_with_threads_and_libraries(
        process_number: int,
        threads_number: int,
        libraries_number: int
):
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
        libraries: list[DynamicLibrary] = []
        for library_i in range(libraries_number):
            library: DynamicLibrary = DynamicLibrary(
                library_i + 1,
                random.randint(10, 1024),
                f"library {library_i + 1}"
            )
            libraries.append(library)

        for process_i in range(process_number):
            library_number = 0
            used_libraries: list[bool] = []
            for i in range(0, len(libraries)):
                used_libraries.append(False)
            process: Process = Process(
                process_i + 1,
                random.randint(10, 1024),
                f"process {process_i + 1}"
            )
            for thread_i in range(threads_number):
                thread: Thread = Thread(
                    thread_i + 1,
                    random.randint(10, 1024),
                    f"thread {thread_i + 1}",
                    process
                )
                process.add_thread(thread)
            while library_number <= 2:
                random_library_id = random.choice(libraries).id
                if used_libraries[random_library_id - 1] is False:
                    used_libraries[random_library_id - 1] = True
                    library: DynamicLibrary = libraries[random_library_id - 1]
                    library.add_process(process)
                    process.add_library(library)
                    library_number += 1

            processes.append(process)

    return processes, libraries
