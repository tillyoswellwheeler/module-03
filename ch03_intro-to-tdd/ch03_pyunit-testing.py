#-----------------------------------------
## MODULE 03 -- Chapter Three -- PyUnit
#-----------------------------------------

#----- Import unittest first
import unittest

#----- Import TestCase function to start a new test case
from unittest import TestCase

#----- Import function to test from function file
from is_prime import is_prime

#-----------------------------------------
# Creating a class -- Defining the tests
#-----------------------------------------

#----- The class means that we can define all the variants of a test in one class.

#----- unittest.TestCase is a method from unittest
class prime_test(unittest.TestCase):
    def test_prime(self):
        self.assertIsInstance(sys.argv[1], int)
        self.assertTrue(sys.argv[1])
        
#----- sys.argv[0] is used when you want an input from the sys terminal. 
#        eg// python.py[0] arg1[1] arg [2] etc
#        This would allow you to automate the testing.

#-----  This is the start button, it looks for a main function and then runs the below code.    
if__name__=="__main__": 
    unittest.main()
        
