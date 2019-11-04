import unittest

from Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
            self.assertEqual(self.calculator.subtract(1,2), 0)

if __name__ == '__main__':
    unittest.main()
