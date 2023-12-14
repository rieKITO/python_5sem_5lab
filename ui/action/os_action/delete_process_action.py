# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_input import natural_num_input

# ---------------- MODELS ---------------- #
from models.os import OS
from models.process import Process


def delete_process(os: OS):
    if os is None:
        raise ValueError
    if type(os) is not OS:
        raise TypeError

    process = None
    process_id = None
    while process is None:
        print("\nEnter the dynamic library ID")
        process_id = natural_num_input()
        process: Process = os.search_process_from_id(process_id)
        if process is None:
            print("Library with this id does not exist!")
    try:
        os.delete_process_from_id(process_id)
    except ValueError:
        raise ValueError

