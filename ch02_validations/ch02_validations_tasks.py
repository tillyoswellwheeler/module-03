#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:22:17 2019

@author: matildaoswell-wheeler
"""

#-----------------------------------------
## MODULE 03 -- Chapter Two -- Validations
#-----------------------------------------

#----- 

#-----------------------------------------
# TASK ONE -- Different input methods
#-----------------------------------------

#-----  With a new line
#print("What's your age?")
#age = input()

#----- With a space
#age = input("What's your age?")

#-----------------------------------------
# TASK TWO -- Casting values to ints
#-----------------------------------------

#----- The output will be a string, use int() to cast it to an int.
#age = input("What's your age? ")
#age_number = int(age) # This casts as an int
#print(age_number)
#print(type(age_number)) # This checks that the input is now an int

#----- You can do it like this too, which is better in terms of memory space:
#print("What's your age? ")
#age = int(input())
#print(type(age))

#-----------------------------------------
# TASK THREE -- Casting values to str types
#-----------------------------------------

#----- Casting to lowercase
#option = input("Please input yes or no ").lower()

#----- NOTE -- For OOP as all data types are objects then the casting them
#       works differently. You use .method  eg// 'ADsf'.low()

#----- Casting to uppercase
#option_up = input("Please input yes or no ").upper()

#-----------------------------------------
# TASK FOUR -- While True
#-----------------------------------------

#----- Using While True means that it loops until your if statement is True.
#def check_str_length():
#    print()
#
#    while True:
#        Name = input('Please enter your name: ')
#
#        if len(Name) > 1:
#            break
#        print("Your name is too short! ")
#
#    print()
#    return Name
#
#check_str_length()

#-----------------------------------------
# TASK FIVE -- Checking routines
#-----------------------------------------

#print('***choice****')
#print('1. Display my name')
#print('2. Display my age')
#print('3. Display my city')
#
#if choice == 1:
#    print('Ms Wu')
#elif choice == 2:
#    print('5 years old')
#elif choice == 3:
#    print('London')
#
#choice = input('What is your choice?')

#-----------------------------------------
# TASK SIX -- Handling error input
#-----------------------------------------

#----- Using a while True and try Exception for the above
#print('***choice****')
#print('1. Display my name')
#print('2. Display my age')
#print('3. Display my city')
#
#while True:
#    try:
#        while choice < 1 or choice > 3:
#            choice = int(input('What is your choice? '))
#        break
#    except ValueError:
#        print('Please only input a number')
#        choice = 0
#        
#if choice == 1:
#    print('Ms Wu')
#elif choice == 2:
#    print('5 years old')
#elif choice == 3:
#    print('London') 
    
#-----------------------------------------
# TASK SEVEN -- Classed based validation
#-----------------------------------------

class Spam(object):
    def __init__(self, description, value):
        if not description or value <=0:
            raise ValueError
        self.description = description
        self.value = value
        
s = Spam('s', 5)
s1 = Spam('', -1) # This raise the above Exception error
