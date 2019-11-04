import unittest

from Calculator import Calculator
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader('/src/Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(float(row['Value 1']), float(row['Value 2'])), result)
            self.assertEqual(self.calculator.result, result)

    def test_addition(self):
        test_data = CsvReader('/src/Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(float(row['Value 1']), float(row['Value 2'])), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader('/src/Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(float(row['Value 1']), float(row['Value 2'])), result)
            self.assertEqual(self.calculator.result, result)

    def test_division(self):
        test_data = CsvReader('/src/Division.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(float(row['Value 1']), float(row['Value 2'])), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        test_data = CsvReader('/src/Square.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqr(float(row['Value 1'])), result)
            self.assertEqual(self.calculator.result, result)

    def test_squareroot(self):
        test_data = CsvReader('/src/SquareRoot.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqrt(float(row['Value 1'])), result)
            self.assertEqual(self.calculator.result, result)

if __name__ == '__main__':
    unittest.main()
