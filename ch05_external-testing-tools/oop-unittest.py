#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:02:26 2019

@author: matildaoswell-wheeler
"""

#-----------------------------------------
## MODULE 03 -- Chapter Five -- OOP PyUnit
#-----------------------------------------

import unittest
from calculator import Calculator


class TddInPythonExample(unittest.TestCase):
#    def test_calculator_add_method_returns_correct_result(self):
#        calc = Calculator()
#        result = calc.add(2,2)
#        self.assertEqual(4, result) This was the initial setup for the test file.
    def setUp(self): # Separating out the functions
        self.calc = Calculator ()
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2,2) # Representing the newly defined calc self from the above function
        self.assertEqual(4, result)
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
        
if __name__ == '__main__':
    unittest.main()