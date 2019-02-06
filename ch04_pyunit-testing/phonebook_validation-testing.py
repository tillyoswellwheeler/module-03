#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:20:44 2019

@author: matildaoswell-wheeler
"""
#--------------------------------------------
## MODULE 03 -- Phonebook -- Validation Tests
#--------------------------------------------

#----- Check for existence of database 

class testDBExists(unittest.TestCase):
    def test_dbexists(self):
        self.assertTrue(check_db_exists())
    
def check_db_exists():
    try:
        f = open ("phonebook_project.db")
    except Exception as e:
        print(e)
        return False
    else:
        print("file found")
        return True
        