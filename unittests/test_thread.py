import unittest

# ---------------- MODELS ---------------- #
from models.thread import Thread


class TestThread(unittest.TestCase):
    def setUp(self):
        self.thread = Thread(
            1,
            200,
            "thread 1"
        )

    def test_init_with_valid_values(self):
        self.assertEqual(self.thread.id, 1)
        self.assertEqual(self.thread.memory, 200)
        self.assertEqual(self.thread.name, "thread 1")

    def test_init_with_invalid_values(self):
        self.assertRaises(ValueError, self.thread.__init__, None, 4, None)
        self.assertRaises(ValueError, self.thread.__init__, 1, None, None)
        self.assertRaises(ValueError, self.thread.__init__, None, None, None)

        self.assertRaises(TypeError, self.thread.__init__, "str", [4], 2.35)
        self.assertRaises(TypeError, self.thread.__init__, {2, 5}, 3.44, [2])
        self.assertRaises(TypeError, self.thread.__init__, 3.44, "str", 1)

    def test_delete(self):
        self.thread.delete()
        self.assertEqual(self.thread.id, None)
        self.assertEqual(self.thread.memory, None)
        self.assertEqual(self.thread.name, None)
