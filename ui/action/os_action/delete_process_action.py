# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_with_max_range_input import natural_num_with_max_range_input

# ---------------- MODELS ---------------- #
from models.os import OS


def delete_process_action(os: OS):
    if os is None:
        raise ValueError
    if type(os) is not OS:
        raise TypeError

    print("Enter the process ID:")
    process_id = natural_num_with_max_range_input(len(os.processes))
    try:
        os.delete_process_from_id(process_id)
    except ValueError:
        raise ValueError

