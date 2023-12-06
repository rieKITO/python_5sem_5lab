import logging
import sys


logging.basicConfig(level = logging.INFO, filename = 'logs\infos.log', filemode = 'w', format = "%(asctime)s %(levelname)s %(message)s")
consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))

LOGGER = logging.getLogger()
LOGGER.addHandler(consoleHandler)

ACTION_NUMBER_IN_OS_MENU = 4
ACTION_NUMBER_IN_PROCESS_MENU = 7
