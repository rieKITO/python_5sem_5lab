# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_input import natural_num_input

# ---------------- MODELS ---------------- #
from models.os import OS

# ---------------- UI ---------------- #
# ---------- ACTION ---------- #
from ui.action.process_action.process_action_choice import process_action_choice
# ---------- MENU ---------- #
from ui.menu.additional_information_menu import additional_information_process_menu
# ---------- PRINT ---------- #
from ui.print.print_process_info import print_process_info


def find_process(os: OS):
    if os is None:
        raise ValueError
    if type(os) is not OS:
        raise TypeError

    process = None
    while process is None:
        print("\nEnter the process ID")
        process_id = natural_num_input()
        process = os.search_process_from_id(process_id)
        if process is None:
            print("Process with this ID does not exist!")
    print_process_info(process)

    additional_information_process_menu()
    additional_info_choice = str(input("-> "))
    if additional_info_choice == "Y" or additional_info_choice == "y":
        process_action_choice(process)
