from models.process import Process


def processes_print(processes: list) -> None:
    for process in processes:
        if type(process) is not Process:
            raise TypeError
        else:
            print(
                f"\nid | name: {process.id} | {process.name}\n"
                f"memory: {process.memory}"
            )
