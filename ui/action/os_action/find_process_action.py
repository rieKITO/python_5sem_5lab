# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_with_max_range_input import natural_num_with_max_range_input

# ---------------- MODELS ---------------- #
from models.os import OS

# ---------------- UI ---------------- #
# ---------- MENU ---------- #
from ui.menu.additional_information_menu import additional_information_process_menu
# ---------- PRINT ---------- #
from ui.print.print_process_info import print_process_info


def find_process_action(os: OS):
    if os is None:
        raise ValueError
    if type(os) is not OS:
        raise TypeError

    process = None
    while process is None:
        print("\nEnter the process ID")
        process_id = natural_num_with_max_range_input(len(os.processes))
        process = os.search_process_from_id(process_id)
        if process is None:
            print("Process with this id does not exist!")
    print_process_info(process)

    additional_information_process_menu()
    additional_info_choice = str(input("-> "))
    if additional_info_choice == "Y" or additional_info_choice == "y":
        pass
