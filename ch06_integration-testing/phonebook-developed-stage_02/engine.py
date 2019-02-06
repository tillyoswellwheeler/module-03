# -*- coding: utf-8 -*-

#---------------------------------
## Phonebook project
#---------------------------------

import sqlite3
import json
import time

#-------------------------------------------------------
# Functionalities 
#-------------------------------------------------------

class Phonebook():
    def __init__(self):
        #initializes path to db
        self.db_path = sqlite3.connect("phonebook_project.db") #Connects to the database

    def check_db(self):
        #checks if database exist. if it does it creates a new Phonebook class attribute 'db_exist' which is set to True
        if exists(self.db_path):
            return True
        #and False if not
        else:
            return False
        
    def check_db_opens(self): # Check file opens
        try:
            f = open ("phonebook_project.db")
        except Exception as e:
            print(e)
            return False
        else:
            print("file found")
            return True

    def connectdb(self):
        try:
            if self.check_db():
                self.connection = connect(self.db_path)
                self.cursor = self.connection.cursor()
            else:
                print('Database Does Not Exist')
                return None
        except:
            print("Error")
            return False


    def query_db(self,query, params=None):  
        try:
            self.connect_db()
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.results = self.cursor.fetchall()
            self.connection.close()
        except Exception as e:
            print(e)
            
#---------------------------------
## Reusable Functions
#---------------------------------
            
    def searchby_city(self, table): # Trying to make a resuable search city function
        try:
            query = "SELECT address_line_2 FROM ?;", (table,)
            self.query_db(query)
            return self.results
        except Exception as e:
            print(e)

#---------------------------------
## Residential Search
#---------------------------------

    def ask_surname(self):
        db, conn = connectdb()
        surname = input("What's the surname of the person you are looking for?")
        db.execute('SELECT * FROM Residential WHERE surname = ?', (surname.title(),))
        surname_results = db.fetchall()
        if len(surname_results) <1:  #    if this is empty using length of list then you print error
            print("Sorry, name not in phonebook")
        else:
            print ("We found",len(surname_results),"results")
            time.sleep(2)
            print(surname_results)
            
    def residential_ask_location(self):
        db, conn = connectdb()
        town_city = input("What city or town do you want to search within?")
        db.execute('SELECT * FROM Residential WHERE town_city = ?', (town_city.title(),))
        location_results = db.fetchall()
        if len(location_results) <1:  #    if this is empty using length of list then you print error
            print("Sorry, there are no results for that location")
        else:
            print ("We found",len(location_results),"results")
            time.sleep(2)
            print(location_results)
            sorting_choice = input("Do you want to sort results by surname, alphabetically? y/n: ")
            if sorting_choice[0] == "y":
                return sort_surname(location_results)
            else:
                print(location_results)
    
    def sort_surname(self, location_results):
        sorted_by_surname = sorted(location_results, key=lambda tuple:tuple[1])
        print(sorted_by_surname)

#-------------------------------------------------------
# Residential subfunctions
#-------------------------------------------------------
        
    def sort_residential_location(self):
        db, conn = connectdb()
        loc_data = input("What city or town do you want to search within? ").title()
        db.execute('SELECT * FROM Residential WHERE town_city = ?', (loc_data,))
        for row in db.fetchall():
            print (row)


        
#---------------------------------
## Business Search
#---------------------------------


    def user_input_business():
        db, conn = connectdb()
        businesschoice = input("Would you like to search for business type or business name? ")
        if businesschoice == "type":
            print ("You chose business type")
    #        sort_business_type()
            # asks for user input
            user_input = input("What business type would you like to search for?")
            multi_user_input(user_input)
    #        selected_business_type()
    #        ask_business_location()
        elif businesschoice == "name":
            print ("You chose business name")
            time.sleep(1)
            sort_business_name()
            ask_business_location()
        else:
            print ("Error, please try again")
            return user_input_business()

#-------------------------------------------------------
# Business subfunctions
#-------------------------------------------------------
        
#--------# Sorting business data #----------
        
    # Trying to add user input
    def multi_user_input(user_input):
        validated_user_input = input("{}".format(user_input))
        return validated_user_input
            
    def selected_business_type(input):
        user_input = input
        db, conn = connectdb()
        db.execute('SELECT * FROM Business WHERE business_category IN ?',(user_input, ))
        for row in db.fetchall():
            print (row[7])
            
    def selected_business_name():
        db, conn = connectdb()
        db.execute('SELECT * FROM Business ORDER BY business_name')
        for row in db.fetchall():
            print (row[0])
            
    #def sort_business_type():
    #    db, conn = connectdb()
    #    db.execute('SELECT * FROM Business ORDER BY business_category')
    #    for row in db.fetchall():
    #        print (row[7])
    #        
    #def sort_business_name():
    #    db, conn = connectdb()
    #    db.execute('SELECT * FROM Business ORDER BY business_name')
    #    for row in db.fetchall():
    #        print (row[0])
    
    def ask_business_location():
        db, conn = connectdb()
        loc_data = input("please enter the town or city: ").title()
        time.sleep(1)
        db.execute('SELECT * FROM Business WHERE town_city = ?', (loc_data,))
        for row in db.fetchall():
            print (row)
        
     
