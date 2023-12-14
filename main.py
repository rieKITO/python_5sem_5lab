# ---------------- MODELS ---------------- #
from models.os import OS

# ---------------- MODELS ---------------- #
# ---------- ACTION ---------- #
# ---- OS ACTION ---- #
from ui.action.os_action.os_action_choice import os_action_choice

# ---------------- UTILS ---------------- #
from utils.create_random_process_list_with_threads_and_libraries import (
    create_random_process_list_with_threads_and_libraries)


def main():
    processes, libraries = create_random_process_list_with_threads_and_libraries(10, 5, 15)
    os = OS(processes, libraries)
    os_action_choice(os)


if __name__ == '__main__':
    main()
