from engine import *
import sqlite3 
import json
import time

#-------------------------------------
## Phonebook project--Integration Test
#-------------------------------------

class TestEngine():
    def __init__(self):
        self.pb = Phonebook() # Here she is connecting the self test to the phonebook class via the .pb

    def test_check_db(self): # Running the check_db() with the Phonebook Class
        self.checked = self.pb.check_db() # repassing check_db through the new object: test_check_db.checked
        return self.checked

    def test_connectdb(self):
        self.test_check_db() # Calling the test_check_db() to use within the function and use self.check return value

        if self.checked:
            connected = self.pb.connect_db() # calling the function from engine.py and assigning the output of the validations to connected
            if connected: 
                self.connected = True # If the output of connect_db = TRUE return that via self.connected
                return self.connected
            else:
                self.connected = False # If the output of connect_db = FALSE return that via self.connected
                return self.connected
        else:
            print("Database Does not Exist: Connection Failed") 

    def test_query_db(self):
        query ="SELECT * FROM business;"
        results = self.pb.query_db(query) # the params=None in this functions arguements means you can call this function without calling params
        if results:
            self.queried = True # The successfully queried result
        else:
            self.query = False

    def run_tests(self): # This function runs all of the above functions.
        print(self.test_check_db())
        print(self.test_connectdb())
        print(self.test_query_db())


if __name__ == "__main__":
    newTest = TestEngine()
    newTest.run_tests()