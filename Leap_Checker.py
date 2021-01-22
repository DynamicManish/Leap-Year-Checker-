import math

def is_leap(year):
    leap = False
    c = math.pow(10,5)
    lp_year = year%4
    lp_year1 = year%400
    lp_year2 = year%100
    
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

year = int(input())
print(is_leap(year))
