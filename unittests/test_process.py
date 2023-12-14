import unittest

# ---------------- MODELS ---------------- #
from models.process import Process
from models.dynamic_library import DynamicLibrary
from models.thread import Thread


class TestProcess(unittest.TestCase):
    def setUp(self):
        self.threads = []
        self.libraries = []
        self.process = Process(
            1,
            200,
            "process 1",
        )
        self.thread1 = Thread(1, 200, "thread 1", self.process)
        self.thread2 = Thread(2, 250, "thread 2", self.process)
        self.threads.append(self.thread1)
        self.threads.append(self.thread2)
        self.library1 = DynamicLibrary(1, 200, "library 1")
        self.library2 = DynamicLibrary(2, 300, "library 2")
        self.library1.add_process(self.process)
        self.library2.add_process(self.process)
        self.libraries.append(self.library1)
        self.libraries.append(self.library2)
        self.process.fill_thread_list(self.threads)
        self.process.fill_library_list(self.libraries)

    def test_init_with_valid_values(self):
        self.assertEqual(self.process.id, 1)
        self.assertEqual(self.process.memory, 200)
        self.assertEqual(self.process.name, "process 1")
        self.assertEqual(self.process.threads, self.threads)
        self.assertEqual(self.process.libraries, self.libraries)

    def test_init_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.__init__, None, None, None, None, None)
        self.assertRaises(ValueError, self.process.__init__, None, None, None)

        self.assertRaises(TypeError, self.process.__init__, "str", {2, 5}, 4.35, [4], None)
        self.assertRaises(TypeError, self.process.__init__, True, "str", [4], 2.35, {2})

    def test_fill_thread_list_with_valid_thread_list(self):
        self.process.fill_thread_list(self.threads)
        self.assertEqual(self.process.threads, self.threads)

    def test_fill_thread_list_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.fill_thread_list, None)

        self.assertRaises(TypeError, self.process.fill_thread_list, 2)
        self.assertRaises(TypeError, self.process.fill_thread_list, 2.35)
        self.assertRaises(TypeError, self.process.fill_thread_list, "str")
        self.assertRaises(TypeError, self.process.fill_thread_list, {2, 5})
        self.assertRaises(TypeError, self.process.fill_thread_list, [4])
        self.assertRaises(TypeError, self.process.fill_thread_list, True)

    def test_fill_library_list_with_valid_thread_list(self):
        self.process.fill_library_list(self.libraries)
        self.assertEqual(self.process.libraries, self.libraries)

    def test_fill_library_list_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.fill_library_list, None)

        self.assertRaises(TypeError, self.process.fill_library_list, 2)
        self.assertRaises(TypeError, self.process.fill_library_list, 2.35)
        self.assertRaises(TypeError, self.process.fill_library_list, "str")
        self.assertRaises(TypeError, self.process.fill_library_list, {2, 5})
        self.assertRaises(TypeError, self.process.fill_library_list, [4])
        self.assertRaises(TypeError, self.process.fill_library_list, True)

    def test_add_thread_with_valid_values(self):
        thread3 = Thread(3, 40, "thread 3", self.process)
        self.threads.append(thread3)
        self.process.add_thread(thread3)
        self.assertEqual(self.process.threads, self.threads)

    def test_add_thread_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.add_thread, None)

        self.assertRaises(TypeError, self.process.add_thread, 2)
        self.assertRaises(TypeError, self.process.add_thread, 2.35)
        self.assertRaises(TypeError, self.process.add_thread, "str")
        self.assertRaises(TypeError, self.process.add_thread, {2, 5})
        self.assertRaises(TypeError, self.process.add_thread, [4])
        self.assertRaises(TypeError, self.process.add_thread, True)

    def test_add_library_with_valid_values(self):
        library3 = DynamicLibrary(3, 40, "library 3")
        self.libraries.append(library3)
        self.process.add_library(library3)
        self.assertEqual(self.process.libraries, self.libraries)

    def test_add_library_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.add_library, None)

        self.assertRaises(TypeError, self.process.add_library, 2)
        self.assertRaises(TypeError, self.process.add_library, 2.35)
        self.assertRaises(TypeError, self.process.add_library, "str")
        self.assertRaises(TypeError, self.process.add_library, {2, 5})
        self.assertRaises(TypeError, self.process.add_library, [4])
        self.assertRaises(TypeError, self.process.add_library, True)

    def test_create_thread_with_valid_thread_values(self):
        self.process.create_thread(4, 250, "thread 4")
        self.assertEqual(self.process.threads[len(self.process.threads) - 1].id, 4)
        self.assertEqual(self.process.threads[len(self.process.threads) - 1].memory, 250)
        self.assertEqual(self.process.threads[len(self.process.threads) - 1].name, "thread 4")

    def test_create_thread_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.create_thread, None, None, None)

        self.assertRaises(TypeError, self.process.create_thread, "str", 2.34, True)
        self.assertRaises(TypeError, self.process.create_thread, 2.34, {2, 5}, [4])

    def test_create_library_with_valid_library_values(self):
        self.process.create_library(4, 250, "library 4")
        self.assertEqual(self.process.libraries[len(self.process.libraries) - 1].id, 4)
        self.assertEqual(self.process.libraries[len(self.process.libraries) - 1].memory, 250)
        self.assertEqual(self.process.libraries[len(self.process.libraries) - 1].name, "library 4")

    def test_create_library_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.create_library, None, None, None)

        self.assertRaises(TypeError, self.process.create_library, "str", 2.34, True)
        self.assertRaises(TypeError, self.process.create_library, 2.34, {2, 5}, [4])

    def test_delete_thread_from_id_with_valid_thread_id_value(self):
        self.process.delete_thread_from_id(2)
        self.assertEqual(len(self.process.threads), 1)

    def test_delete_thread_from_id_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.delete_thread_from_id, None)
        self.assertRaises(ValueError, self.process.delete_thread_from_id, 4)

        self.assertRaises(TypeError, self.process.delete_thread_from_id, 2.35)
        self.assertRaises(TypeError, self.process.delete_thread_from_id, True)
        self.assertRaises(TypeError, self.process.delete_thread_from_id, {2, 5})
        self.assertRaises(TypeError, self.process.delete_thread_from_id, [4])

    def test_delete_library_from_id_with_valid_library_id_value(self):
        self.process.delete_library_from_id(2)
        self.assertEqual(len(self.process.libraries), 1)

    def test_delete_library_from_id_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.delete_library_from_id, None)
        self.assertRaises(ValueError, self.process.delete_library_from_id, 4)

        self.assertRaises(TypeError, self.process.delete_library_from_id, 2.35)
        self.assertRaises(TypeError, self.process.delete_library_from_id, True)
        self.assertRaises(TypeError, self.process.delete_library_from_id, {2, 5})
        self.assertRaises(TypeError, self.process.delete_library_from_id, [4])

    def test_search_thread_from_id_with_valid_thread_id_value(self):
        thread: Thread = self.process.search_thread_from_id(1)
        self.assertEqual(thread.id, 1)
        thread: Thread = self.process.search_thread_from_id(4)
        self.assertEqual(thread, None)

    def test_search_thread_from_id_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.search_thread_from_id, None)

        self.assertRaises(TypeError, self.process.search_thread_from_id, 2.35)
        self.assertRaises(TypeError, self.process.search_thread_from_id, True)
        self.assertRaises(TypeError, self.process.search_thread_from_id, {2, 5})
        self.assertRaises(TypeError, self.process.search_thread_from_id, [4])

    def test_search_library_from_id_with_valid_library_id_value(self):
        library: DynamicLibrary = self.process.search_library_from_id(1)
        self.assertEqual(library.id, 1)
        library: DynamicLibrary = self.process.search_library_from_id(4)
        self.assertEqual(library, None)

    def test_search_library_from_id_with_invalid_values(self):
        self.assertRaises(ValueError, self.process.search_library_from_id, None)

        self.assertRaises(TypeError, self.process.search_library_from_id, 2.35)
        self.assertRaises(TypeError, self.process.search_library_from_id, True)
        self.assertRaises(TypeError, self.process.search_library_from_id, {2, 5})
        self.assertRaises(TypeError, self.process.search_library_from_id, [4])

    def test_calculate_memory(self):
        self.assertEqual(self.process.calculate_memory(), 1150)

    def test_delete(self):
        self.process.delete()
        self.assertEqual(self.process.id, None)
        self.assertEqual(self.process.memory, None)
        self.assertEqual(self.process.name, None)
        self.assertEqual(self.process.threads, [])
        self.assertEqual(self.process.libraries, [])
