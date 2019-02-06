#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:16:25 2019

@author: matildaoswell-wheeler
"""

#-----------------------------------------
## MODULE 03 -- Phonebook -- PyUnit Test
#-----------------------------------------

#----- Import unittest first
import unittest 

#----- Import TestCase function to start a new test case
from unittest import TestCase
#----- Import function to test from function file
from phonebook_functionalities import *

class testString(unittest.TestCase):
    def test_string(self):
        self.assertsIsInstance(user_input_business(), str)

if __name__ == "__main__":
    unittest.main()
    
