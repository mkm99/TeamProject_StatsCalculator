import unittest

from Calculator.Calculator import Calculator
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiply
from Calculator.Division import division
from Calculator.Exponentiation import exponentiation
from Calculator.Logarithm import logarithm
from Calculator.SquareRoot import squareRoot
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        self.assertEqual(5, addition(2,3))

    def test_subtraction(self):
        self.assertEqual(10, subtraction(35,25))

    def test_multiplication(self):
        self.assertEqual(36, multiply(12,3))

    def test_division(self):
        self.assertEqual(4, division(16,4))

    def test_exponentiation(self):
        self.assertEqual(9, exponentiation(3,2))

    def test_logarithm(self):
        self.assertEqual(3, logarithm(729, 9))

    def test_squareRoot(self):
        self.assertEqual(5, squareRoot(25))

    def test_sqr2(self):
        self.assertEqual(4, squareRoot(16))

    def test_sqr3(self):
        self.assertEqual(9, squareRoot(81))

    def test_division_0(self):
        self.result = division(24, 0)
        self.assertEqual(self.result, 'Cannot divide by 0')

if __name__ == '__main__':
    unittest.main()