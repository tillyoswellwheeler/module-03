#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:22:17 2019

@author: matildaoswell-wheeler
"""
#-----------------------------------------
## MODULE 03 -- Chapter Two -- Validations
#-----------------------------------------

#-----------------------------------------
# FUNCTIONS -- Using ch08 DataBundle files
#-----------------------------------------

import re

#login - password check, 3 attempts allowed
def DataBundlePurchase(truePassword, balance):
    count=0
    while count < 3:
        password = input("What's your password?")
    
        if password == truePassword:
            print("Welcome!")
            check(balance)
            break
            
        else:
            print("Wrong password, try again!")
            count += 1

# option to either check balance or to buy data     
def check(balance):
    choice = 0
    while True:
        try:
            while choice < 1 or choice > 2:
                choice = int(input("If you would like to check your balance - type 1. If you\
                           would like to top up your data - type 2." ))
            break
        except ValueError:
            print('Please only input a number')
            choice = 0
choice = 0        
if choice == 1:
    print ("Your current balance is: £" + str(balance))
elif choice == 2:
    DataBundlePurchasePhone(balance)
            



#asks for a phne number
# calls phone number validation function for UK numbers
#number to be entered twice - check if matches 
#total of 3 chances to get the phone number right
#called if buing data was the choice in the def choice (balance)
def DataBundlePurchasePhone(balance):
    count=0
    while count < 3:
        phoneNumber = input("Need more data. Please type your phone number first: ")
        if (isValid(phoneNumber)):  
            print ("Valid Number")   
            repeatPhoneNumber = input("Thanks, please confirm your phone number: ")
            if phoneNumber ==  repeatPhoneNumber:
                print ("Thanks! We can get you that extra data now!")
                DataBundleChoice(balance)
                break
            elif phoneNumber !=  repeatPhoneNumber:
                    print ("Numbers do not match. Please try again")
                    count += 1
        else : 
            print ("Invalid Number")  
            count += 1

#phone number validation function for UK numbers
def isValid(phoneNumber): 
      
    # 1) Begins with 0
    # 2) Then contains 7
    # 3) Then contains 9 digits 
    Pattern = re.compile("(0)?[7][0-9]{9}") 
    return Pattern.match(phoneNumber)
    

#adding data
# offers 3 options
# check if balance exceeds teh price. if not enough funds, calls topUp function 
def DataBundleChoice(balance):
    
    dataBundle = 0
    while dataBundle <1 or dataBundle >3:

        try:
            dataBundle = int(input("How much data do you need: (1)I don't need any data (2) 2BG for 5gbp or (3)5GB for 8gbp?. Please type 1, 2, 3. "))
            print("Please type a number between 1 and 3")
            
        except ValueError:
            print('Please type a number!')
    
#    dataBundle = input("How much data do you need: (1)I don't need any data (2) 2BG for 5gbp or (3)5GB for 8gbp?. Please type 1, 2, 3. ")
            
    ValidateChoice(balance, choice, dataBundle)
    return (balance)
    
def ValidateChoice(balance, choice, dataBundle):
    if dataBundle == 1:
        balance = balance
        print("That's ok, see you soon!")
        print ("Your current balance is: £" + str(balance))

    elif dataBundle ==2 and balance < 5:
        print ("Looks like you do not have enough credit. Top up and try again")
        print("Your current balance is: £" + str(balance))
        top_up(balance)
    elif dataBundle ==3 and balance < 8:
        print ("Looks like you do not have enough credit. Top up and try again")
        print("Your current balance is: £" + str(balance))
        top_up(balance)
    elif dataBundle == 2 and balance >= 5:
        balance = balance = balance - 5
        print("Done! Your current balance is: £" + str(balance))
        return balance
    elif dataBundle == 3 and balance >= 8:
        balance = balance = balance - 8
        print("Done! Your current balance is: £" + str(balance))
        return balance
    else:
        print("Value given was incorrect")
        
        

def top_up(balance):
    count=0
    while count < 3:
     
        try: 
            topUpValue = int(input("How much (in GBPs) would you like to top up? Please give number only. Minimum top up is 5GBP. Multiplies of 5 only please - eg.: 5, 10, 15, 20. "))
            
            if topUpValue == 0:
                print("That's ok, see you soon!")
              
            elif topUpValue > 1000:
                print ("That's too much. Max top up is 1000 GBP" )
              
            elif topUpValue < 0:
                print ("Cannot top up negative GBPs. Please pick a number between 1 and 1000")
            
            elif topUpValue % 5 == 0:
                balance = balance + int(topUpValue)
                print("Your current balance is: £" + str(balance))
                choice(balance)
                print ('frh3uf1')
                return balance
           
            else:
                print("Incorrect value")
                count += 1
        except ValueError:
            print("That was not a valid number.  Try again...")
            count += 1
  


