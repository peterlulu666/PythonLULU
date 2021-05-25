def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
print(is_leap(2000))




# Implement function leap() that takes one input argument – a year – and returns True if the year is a leap year and False otherwise. 
# A year is a leap year if it is divisible by 4 but not by 100, unless it is divisible by 400, in which case it is a leap year. 
# For example, 1700, 1800, and 1900 are not leap years but 1600 and 2000 are
def leap(year):     
    if year % 400 == 0:         
        return True     
    if year % 4 == 0 and not (year % 100 == 0):         
        return True     
    return False


