#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:05:55 2019

@author: matildaoswell-wheeler
"""
#----------------------------------------
## MODULE 03 -- Chapter One -- Exceptions
#----------------------------------------

#----- Implicit exceptions are much better than catch-all solutions. 
#   you must be specific in your Exception tests.

#----------------------------------------
# TASK ONE
#----------------------------------------

# Intial test returns a specified error message.
#try:
#    f = open('testfile')
#except Exception:
#    print("Error!")
#    
# Second test returns a more specified error message for the user. 
#try:
#    f = open('testfile')
#except Exception:
#    print("""Sorry, this file does not exist,\
#or the file name is wrong. Please double check""")
    
# Without the error the message is nolonger printed
#try:
#    f = open('testfile.txt')
#except Exception:
#    print("""Sorry, this file does not exist,\
#or the file name is wrong. Please double check""")
    
#----------------------------------------
# TASK TWO -- Multiple errors
#----------------------------------------

#----- Same error message is passed even though the function is run. Why?
### Exception is used for general exceptions.

#try:
#    f = open('testfile.txt')
#    s1 = not_exsit
#except Exception:
#    print("""Sorry, this file does not exist,\
#or the file name is wrong. Please double check""")

#----- Changing the except Test run changes the outcome.
### FileNotFoundError is a specific built in except error.

#try:
#    f = open('testfile.txt')
#    s1 = not_exsit
#except FileNotFoundError:
#    print("""Sorry, this file does not exist,\
#or the file name is wrong. Please double check""")

#----------------------------------------
# Built-in Exceptions
#----------------------------------------
    
#----- Python has a list of built-in exceptions, you can find in the library, eg//:
#ValueError
#TypeError
#ZeroDivisionError
#SyntaxError 

#----- Always put specific exceptions before general, 
#      otherwise it only reads the general
#try:
#    f = open('testfile.txt')
#    s1 = not_exsit
#except FileNotFoundError:
#    print("""Sorry, this file does not exist,\
#or the file name is wrong. Please double check""")
#except Exception:
#    print("Sorry, something wrong after opening function")
    
#----------------------------------------
# TASK THREE -- Print exceptions as found
#----------------------------------------

#try: 
#    f = open('testfile.txt')
#    s1 = file_exsit
#except Exception as e: # The 'e' represents anything wrong, and the actual error is printed to the console.
#    print(e)

#----------------------------------------
# TASK FOUR -- Else block
#----------------------------------------

#----- It is used to confirm if your code is correct. It doesn't do anything.
#try:
#    f = open('testfile.txt')
#except Exception as e:
#    print(e)
#    
#else:              # This runs if your test returns nothing.
#    print(f.read())
#    f.close()

#----------------------------------------
# TASK FIVE -- Finally block
#----------------------------------------

#----- With error in Exception test section
#try:
#    f = open('testfile')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
#finally:
#    print("executing finally...")   

#----- Without error in Exception section
#try:
#    f = open('testfile.txt')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
#finally:
#    print("exceuting finally...")

#----- The finally block is always run no matter is there is an error or if
#    there is not an error. This is useful if you want to close a database for security reasons.

#----------------------------------------
# TASK SIX -- Manual Exceptions
#----------------------------------------

#----- Using booleans
try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
        raise Exception
except Exception as e:
    print("file name are the same")