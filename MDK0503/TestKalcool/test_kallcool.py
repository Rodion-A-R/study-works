import unittest
import math
from KallCool import (
    plus, minus, multiply, divide, power, sqrt, factorial,
    memory_save, memory_add, memory_read, memory_clear
)

class TestCalculatorOperations(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(plus(2, 3), 5)
        self.assertEqual(plus(-1, 1), 0)
        self.assertEqual(plus(0, 0), 0)
        self.assertAlmostEqual(plus(1.5, 2.5), 4.0)

    def test_minus(self):
        self.assertEqual(minus(5, 3), 2)
        self.assertEqual(minus(0, 5), -5)
        self.assertEqual(minus(-2, -3), 1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)
        self.assertAlmostEqual(multiply(1.5, 2), 3.0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertAlmostEqual(divide(1, 3), 1/3)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)
        self.assertAlmostEqual(power(9, 0.5), 3.0)

    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)
        self.assertAlmostEqual(sqrt(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(1.5)

class TestMemoryOperations(unittest.TestCase):
    def setUp(self):
        memory_clear()

    def test_memory_save_and_read(self):
        memory_save(42)
        self.assertEqual(memory_read(), 42.0)
        memory_save(3.14)
        self.assertAlmostEqual(memory_read(), 3.14)

    def test_memory_add(self):
        memory_save(10)
        memory_add(5)
        self.assertEqual(memory_read(), 15.0)
        memory_add(-3)
        self.assertEqual(memory_read(), 12.0)

    def test_memory_clear(self):
        memory_save(100)
        memory_clear()
        self.assertEqual(memory_read(), 0.0)

if __name__ == '__main__':
    unittest.main()