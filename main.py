from models.os import OS
from models.process import Process

def main():
    os = OS()

    process1 = Process(1, 1024, "process1")
    os.add_process(1, )

if __name__ == '__main__':
    main()
