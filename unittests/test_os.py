import unittest

# ---------------- MODELS ---------------- #
from models.os import OS
from models.process import Process
from models.dynamic_library import DynamicLibrary
from models.thread import Thread


class TestOs(unittest.TestCase):
    def setUp(self):
        self.threads = []
        self.libraries = []
        self.processes = []
        self.process1 = Process(1, 200, "process 1")
        self.process2 = Process(2, 200, "process 2")
        self.processes.append(self.process1)
        self.processes.append(self.process2)
        self.thread1 = Thread(1, 200, "thread 1", self.process1)
        self.thread2 = Thread(2, 250, "thread 2", self.process2)
        self.threads.append(self.thread1)
        self.threads.append(self.thread2)
        self.library1 = DynamicLibrary(1, 200, "library 1", self.processes)
        self.library2 = DynamicLibrary(2, 300, "library 2", self.processes)
        self.libraries.append(self.library1)
        self.libraries.append(self.library2)

        self.os = OS(self.processes, self.libraries)

    def test_init_with_valid_processes_value(self):
        self.assertEqual(self.os.processes, self.processes)

    def test_init_with_invalid_values(self):
        self.assertRaises(TypeError, self.os.__init__, "str")
        self.assertRaises(TypeError, self.os.__init__, 2)
        self.assertRaises(TypeError, self.os.__init__, 1.35)
        self.assertRaises(TypeError, self.os.__init__, [4])
        self.assertRaises(TypeError, self.os.__init__, {2, 5})

    def test_fill_process_list_with_valid_process_list(self):
        self.os.fill_process_list(self.processes)
        self.assertEqual(self.os.processes, self.processes)

    def test_fill_process_list_with_invalid_values(self):
        self.assertRaises(ValueError, self.os.fill_process_list, None)

        self.assertRaises(TypeError, self.os.fill_process_list, 2)
        self.assertRaises(TypeError, self.os.fill_process_list, 2.35)
        self.assertRaises(TypeError, self.os.fill_process_list, "str")
        self.assertRaises(TypeError, self.os.fill_process_list, {2, 5})
        self.assertRaises(TypeError, self.os.fill_process_list, [4])
        self.assertRaises(TypeError, self.os.fill_process_list, True)

    def test_search_process_from_id_with_valid_process_id_value(self):
        process: Process = self.os.search_process_from_id(1)
        self.assertEqual(process.id, 1)
        process: Process = self.os.search_process_from_id(4)
        self.assertEqual(process, None)

    def test_search_process_from_id_with_invalid_values(self):
        self.assertRaises(ValueError, self.os.search_process_from_id, None)

        self.assertRaises(TypeError, self.os.search_process_from_id, 2.35)
        self.assertRaises(TypeError, self.os.search_process_from_id, True)
        self.assertRaises(TypeError, self.os.search_process_from_id, {2, 5})
        self.assertRaises(TypeError, self.os.search_process_from_id, [4])

    def test_add_process_with_valid_values(self):
        process3 = Process(3, 40, "process 3")
        self.processes.append(process3)
        self.os.add_process(process3)
        self.assertEqual(self.os.processes, self.processes)

    def test_add_process_with_invalid_values(self):
        self.assertRaises(ValueError, self.os.add_process, None)

        self.assertRaises(TypeError, self.os.add_process, 2)
        self.assertRaises(TypeError, self.os.add_process, 2.35)
        self.assertRaises(TypeError, self.os.add_process, "str")
        self.assertRaises(TypeError, self.os.add_process, {2, 5})
        self.assertRaises(TypeError, self.os.add_process, [4])
        self.assertRaises(TypeError, self.os.add_process, True)

    def test_create_process_with_valid_process_values(self):
        self.os.create_process(4, 250, "process 4")
        self.assertEqual(self.os.processes[len(self.os.processes) - 1].id, 4)
        self.assertEqual(self.os.processes[len(self.os.processes) - 1].memory, 250)
        self.assertEqual(self.os.processes[len(self.os.processes) - 1].name, "process 4")

    def test_create_library_with_invalid_values(self):
        self.assertRaises(ValueError, self.os.create_process, None, None, None)

        self.assertRaises(TypeError, self.os.create_process, "str", 2.34, True)
        self.assertRaises(TypeError, self.os.create_process, 2.34, {2, 5}, [4])

    def test_delete_process_from_id_with_valid_process_id_value(self):
        self.os.delete_process_from_id(2)
        self.assertEqual(len(self.os.processes), 1)

    def test_delete_thread_from_id_with_invalid_values(self):
        self.assertRaises(ValueError, self.os.delete_process_from_id, None)
        self.assertRaises(ValueError, self.os.delete_process_from_id, 4)

        self.assertRaises(TypeError, self.os.delete_process_from_id, 2.35)
        self.assertRaises(TypeError, self.os.delete_process_from_id, True)
        self.assertRaises(TypeError, self.os.delete_process_from_id, {2, 5})
        self.assertRaises(TypeError, self.os.delete_process_from_id, [4])

