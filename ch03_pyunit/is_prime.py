
#-----------------------------------------
## MODULE 03 -- Chapter Three -- PyUnit
#-----------------------------------------

#-----

#-----------------------------------------
# Function -- To be tested
#-----------------------------------------

def is_prime(number):
    for element in range(number):
        if number % element == 0:
            return False
    return True