# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_with_max_range_input import natural_num_with_max_range_input

# ---------------- MODELS ---------------- #
from models.process import Process


def delete_thread(process: Process):
    if process is None:
        raise ValueError
    if type(process) is not Process:
        raise TypeError

    print("Enter the thread ID:")
    thread_id = natural_num_with_max_range_input(len(process.threads))
    try:
        process.delete_thread_from_id(thread_id)
    except ValueError:
        raise ValueError

