import math

def is_leap(year): #creating a function 
    leap = False #this will return false if the year is not leap
    c = math.pow(10,5) #giving a condition, so that the year mentioned is not greater than equal to the 5h power of 10
    lp_year = year%4 #dividing the year by 4 to check if the non 100 year is a leap year or not
    lp_year1 = year%400 #division by 400 also, so that the 100 year can be verified if that is a leap or not 
    lp_year2 = year%100 #division by 100, so that if that is divisible by 100 then it will also be divisible by 400 also
    
    if lp_year == 0 and lp_year1 == 0:
        return True
    elif lp_year == 0:
        if lp_year2 == 0:
            return False
        else:
            return True
    elif lp_year != 0 and lp_year1 == 0:
        return True 
    else:
        return False

year = int(input()) #making user to input year
print(is_leap(year)) #calling out the function
