def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
def date1BeforeDate2(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif year1 == year2 and month1 < month2:
        return True
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return True
    return False
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    date = year1, month1, day1
    condition = date1BeforeDate2(date[0], date[1], date[2], year2, month2, day2)
    s =0
    while(condition):
        s = s + 1
        date = nextDay(date[0], date[1], date[2]) 
        condition = date1BeforeDate2(date[0], date[1], date[2], year2, month2, day2)

    return s
