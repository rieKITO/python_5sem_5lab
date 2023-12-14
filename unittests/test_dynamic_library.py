import unittest

# ---------------- MODELS ---------------- #
from models.process import Process
from models.dynamic_library import DynamicLibrary


class TestDynamicLibrary(unittest.TestCase):
    def setUp(self):
        self.library = DynamicLibrary(
            1,
            200,
            "library 1"
        )
        library_list: list[DynamicLibrary] = []
        library_list.append(self.library)
        self.processes = [Process(1, 200, "process 1", None, library_list), Process(2, 200, "process 2"), None, library_list]
        self.library.processes = self.processes

    def test_init_with_valid_values(self):
        self.assertEqual(self.library.id, 1)
        self.assertEqual(self.library.memory, 200)
        self.assertEqual(self.library.name, "library 1")
        self.assertEqual(self.library.processes, self.processes)

    def test_init_with_invalid_values(self):
        self.assertRaises(ValueError, self.library.__init__, None, 4, None, {})
        self.assertRaises(ValueError, self.library.__init__, 1, None, None, "adad")
        self.assertRaises(ValueError, self.library.__init__, None, None, None, None)

        self.assertRaises(TypeError, self.library.__init__, "str", [4], 2.35)
        self.assertRaises(TypeError, self.library.__init__, {2, 5}, 3.44, [2])
        self.assertRaises(TypeError, self.library.__init__, 3.44, "str", 1)

    def test_add_process(self):
        process: Process = Process(3, 700, "process 3")
        process.add_library(self.library)
        self.processes.append(process)
        self.library.add_process(process)
        self.assertEqual(self.library.processes, self.processes)
        self.processes.remove(process)

    def test_search_process_from_id(self):
        process: Process = self.library.search_process_from_id(1)
        self.assertEqual(self.library.processes[0], process)

    def test_remove_process(self):
        self.library.remove_process_from_id(2)
        self.assertEqual(self.library.processes, self.processes)

    def test_delete(self):
        self.library.delete()
        self.assertEqual(self.library.id, None)
        self.assertEqual(self.library.memory, None)
        self.assertEqual(self.library.name, None)
