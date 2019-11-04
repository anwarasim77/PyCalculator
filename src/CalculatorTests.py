import unittest

from Calculator import Calculator
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader("Data Files/Unit Test Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(float(row['Value 1']), float(row['Value 2']), result))
            self.assertEqual(self.calculator.result, result)

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
