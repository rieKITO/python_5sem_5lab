# ---------------- INPUT HANDLING ---------------- #
from input_handling.natural_num_with_max_range_input import natural_num_with_max_range_input

# ---------------- MODELS ---------------- #
from models.process import Process

# ---------------- UI ---------------- #
# ---------- ACTION ---------- #
# ---- PROCESS ACTION ---- #
from ui.action.process_action.add_library_action import add_library
from ui.action.process_action.add_thread_action import add_thread
from ui.action.process_action.delete_library_action import delete_library
from ui.action.process_action.delete_thread_action import delete_thread
from ui.action.process_action.find_library_action import find_library
from ui.action.process_action.find_thread_action import find_thread
# ---------- MENU ---------- #
from ui.menu.process_menu import process_menu
# ---------- PRINT ---------- #
from ui.print.print_process_info import print_process_info

# ---------------- CONFIG ---------------- #
from config import ACTION_NUMBER_IN_PROCESS_MENU


def process_action_choice(process: Process):
    is_exit = False
    while is_exit is False:
        print_process_info(process)
        process_menu()
        process_action = natural_num_with_max_range_input(ACTION_NUMBER_IN_PROCESS_MENU)
        match process_action:
            case 1:
                add_thread(process)
            case 2:
                add_library(process)
            case 3:
                delete_thread(process)
            case 4:
                delete_library(process)
            case 5:
                find_thread(process)
            case 6:
                find_library(process)
            case 7:
                is_exit = True
