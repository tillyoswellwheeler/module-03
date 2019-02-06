#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:16:05 2019

@author: matildaoswell-wheeler
"""

#----------------------------------------------------------
## MODULE 03 -- Chapter Five -- OOP PyUnit -- Function file
#----------------------------------------------------------

# Stage one and two:
#class Calculator(object):
#    def add(self, x, y):
##        Pass Intially we Passed so we could see that the import of the function was working
#        return x + y

## Stage three:
#class Calculator(object):
#    def add(self, x, y):
#        number_types = (int, float, complex)
#        if isinstance(x, number_types) and isinstance(y, number_types):
#            return x + y
#        else:
#            raise ValueError
            
# Stage four: Deliberate error
class Calculator(object):
    def add(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            import pdb; pdb.set_trace() # new debugging technique
            return x - y
            print('Result is: {}'.format(result))
        else:
            raise ValueError