import unittest

from Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
            self.assertEqual(self.calculator.subtract(1,2), 1)

    def test_addition(self):
            self.assertEqual(self.calculator.add(1,2), 3)

    def test_multiplication(self):
            self.assertEqual(self.calculator.multiply(1,2), 2)

    def test_division(self):
            self.assertEqual(self.calculator.divide(1,2), 2)

    def test_square(self):
            self.assertEqual(self.calculator.sqr(4), 16)

    def test_squareroot(self):
            self.assertEqual(self.calculator.sqrt(16), 4)

if __name__ == '__main__':
    unittest.main()
