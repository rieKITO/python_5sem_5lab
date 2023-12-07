import unittest

# ---------------- MODELS ---------------- #
from models.dynamic_library import DynamicLibrary


class TestDynamicLibrary(unittest.TestCase):
    def setUp(self):
        self.library = DynamicLibrary(
            1,
            200,
            "library 1"
        )

    def test_init_with_valid_values(self):
        self.assertEqual(self.library.id, 1)
        self.assertEqual(self.library.memory, 200)
        self.assertEqual(self.library.name, "library 1")

    def test_init_with_invalid_values(self):
        self.assertRaises(ValueError, self.library.__init__, None, 4, None)
        self.assertRaises(ValueError, self.library.__init__, 1, None, None)
        self.assertRaises(ValueError, self.library.__init__, None, None, None)

        self.assertRaises(TypeError, self.library.__init__, "str", [4], 2.35)
        self.assertRaises(TypeError, self.library.__init__, {2, 5}, 3.44, [2])
        self.assertRaises(TypeError, self.library.__init__, 3.44, "str", 1)

    def test_delete(self):
        self.library.delete()
        self.assertEqual(self.library.id, None)
        self.assertEqual(self.library.memory, None)
        self.assertEqual(self.library.name, None)
