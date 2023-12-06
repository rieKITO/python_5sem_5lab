# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_with_max_range_input import natural_num_with_max_range_input

# ---------------- MODELS ---------------- #
from models.os import OS

# ---------------- UI ---------------- #
# ---------- ACTION ---------- #
# ---- OS ACTION ---- #
from ui.action.os_action.add_process_action import add_process
from ui.action.os_action.delete_process_action import delete_process
from ui.action.os_action.find_process_action import find_process
# ---------- MENU ---------- #
from ui.menu.os_menu import os_menu
# ---------- PRINT ---------- #
from ui.print.print_process_list import print_process_list

# ---------------- CONFIG ---------------- #
from config import ACTION_NUMBER_IN_OS_MENU


def os_action_choice(os: OS):
    is_exit = False
    while is_exit is False:
        print("\n----- Processes -----")
        print_process_list(os.processes)
        os_menu()
        os_action = natural_num_with_max_range_input(ACTION_NUMBER_IN_OS_MENU)
        match os_action:
            case 1:
                add_process(os)
            case 2:
                delete_process(os)
            case 3:
                find_process(os)
            case 4:
                is_exit = True
