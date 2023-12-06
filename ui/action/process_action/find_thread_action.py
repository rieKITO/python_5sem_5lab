# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_input import natural_num_input

# ---------------- MODELS ---------------- #
from models.process import Process

# ---------------- UI ---------------- #
# ---------- PRINT ---------- #
from ui.print.print_thread_info import print_thread_info


def find_thread(process: Process):
    if process is None:
        raise ValueError
    if type(process) is not Process:
        raise TypeError

    thread = None
    while thread is None:
        print("\nEnter the thread ID")
        thread_id = natural_num_input()
        thread = process.search_thread_from_id(thread_id)
        if thread is None:
            print("Thread with this id does not exist!")
    print_thread_info(thread)
