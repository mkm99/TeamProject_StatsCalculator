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


    '''
    This section is to make sure the calculator will no work if strings are being passed as arguments
    '''

    def test_add_str(self):
        self.assertEqual("Trying to use strings in calculator", addition("hi", " bye"))

    def test_minus_str(self):
        self.assertEqual("Trying to use strings in calculator", subtraction("no", " yes"))

    def test_division_str(self):
        self.assertEqual("Trying to use strings in calculator", division("dei", " boy"))

    def test_exponentiation_str(self):
        self.assertEqual("Trying to use strings in calculator", exponentiation("hi", " bye"))

    def test_log_str(self):
        self.assertEqual("Trying to use strings in calculator", logarithm("his", " brye"))

    def test_multiplication_str(self):
        self.assertEqual("Trying to use strings in calculator", multiply("hi", " bye"))

    def test_squareRoot_str(self):
        self.assertEqual("Trying to use strings in calculator", squareRoot("hi"))



if __name__ == '__main__':
    unittest.main()