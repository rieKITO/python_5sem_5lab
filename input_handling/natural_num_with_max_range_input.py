# ---------------- CONFIG ---------------- #
from config import LOGGER


def natural_num_with_max_range_input(count_of_actions: int):
    number = 0
    if type(count_of_actions) is not int:
        LOGGER.error(TypeError)
        raise TypeError
    is_correct = False
    while is_correct is False:
        try:
            number = int(input("-> "))
            if number < 1 or number > count_of_actions:
                LOGGER.warning("Inaccessible value entered!")
            else:
                is_correct = True
        except ValueError:
            LOGGER.error(ValueError)
            raise ValueError
    return number
