# ---------------- CONFIG ---------------- #
from config import LOGGER


def natural_num_input():
    number = 0
    is_correct = False
    while is_correct is False:
        try:
            number = int(input("-> "))
            if number < 1:
                LOGGER.warning("Inaccessible value entered!")
            else:
                is_correct = True
        except ValueError:
            LOGGER.error(ValueError)
    return number
