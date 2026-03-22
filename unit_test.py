import unittest
from test_file import *

class TestMathUtilsUnittest(unittest.TestCase):

    def test_add_success(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(1.5, 2), 3.5)

    def test_subtract_success(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 7), -7)

    def test_multiply_success(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 0), 0)

    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    # Тесты на некорректные типы
    def test_type_errors(self):
        with self.assertRaises(TypeError):
            add("1", 2)

        with self.assertRaises(TypeError):
            subtract(None, 5)

        with self.assertRaises(TypeError):
            multiply([1], 2)

        with self.assertRaises(TypeError):
            divide(10, "0")

if __name__ == "__main__":
    unittest.main()
