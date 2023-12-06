import random

# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_with_max_range_input import natural_num_with_max_range_input

# ---------------- MODELS ---------------- #
from models.os import OS

# ---------------- UI ---------------- #
# ---------- ACTION ---------- #
# ---- OS ACTION ---- #
from ui.action.os_action.add_process_action import add_process_action
from ui.action.os_action.delete_process_action import delete_process_action
from ui.action.os_action.find_process_action import find_process_action
# ---------- MENU ---------- #
from ui.menu.os_menu import os_menu
# ---------- PRINT ---------- #
from ui.print.print_process_list import print_process_list

# ---------------- CONFIG ---------------- #
from config import ACTION_NUMBER_IN_OS_MENU


def main():
    os = OS()
    for i in range(10):
        os.create_process(i + 1, random.randint(10, 100), f"process {i+1}")
    for process in os.processes:
        for i in range(5):
            process.create_thread(i + 1, random.randint(10,1024), f"thread {i + 1}")
            process.create_library(i + 1, random.randint(10, 1024), f"library {i + 1}")
    is_exit = False
    while is_exit is False:
        print("\n----- Processes -----")
        print_process_list(os.processes)
        os_menu()
        os_action = natural_num_with_max_range_input(ACTION_NUMBER_IN_OS_MENU)
        match os_action:
            case 1:
                add_process_action(os)
            case 2:
                delete_process_action(os)
            case 3:
                find_process_action(os)
            case 4:
                is_exit = True


if __name__ == '__main__':
    main()
