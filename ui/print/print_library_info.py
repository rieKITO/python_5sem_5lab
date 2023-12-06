# ---------------- MODELS ---------------- #
from models.dynamic_library import DynamicLibrary

# ---------------- CONFIG ---------------- #
from config import LOGGER


def print_library_info(library: DynamicLibrary):
    if library is None:
        LOGGER.error(ValueError)
        raise ValueError
    elif type(library) is not DynamicLibrary:
        LOGGER.error(TypeError)
        raise TypeError
    else:
        print(
            f"\nDynamic library id: {library.id}\n"
            f"Dynamic library name: {library.name}\n"
            f"Dynamic library memory: {library.memory}\n"
        )
