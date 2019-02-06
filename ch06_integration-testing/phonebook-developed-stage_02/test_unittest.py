# -*- coding: utf-8 -*-

#---------------------------------
## Phonebook project-- PyUnit
#---------------------------------
import unittest
from phonebook_testfunctions import *
    
#----- Check for existence of database 

class testDBExists(unittest.TestCase):
    def test_dbexists(self):
        self.assertTrue(check_db_exists())
    

class testfuncs(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, checksurnameinput, 4) #if type is int
        self.assertRaises(TypeError, checksurnameinput, True) #if boolean
        
    
if __name__ == "__main__":
    unittest.main()