# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_with_max_range_input import natural_num_with_max_range_input

# ---------------- MODELS ---------------- #
from models.process import Process


def delete_library(process: Process):
    if process is None:
        raise ValueError
    if type(process) is not Process:
        raise TypeError

    print("Enter the dynamic library ID:")
    library_id = natural_num_with_max_range_input(len(process.libraries))
    try:
        process.delete_library_from_id(library_id)
    except ValueError:
        raise ValueError

