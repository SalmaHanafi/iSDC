def isLeap(year):
        if year % 4 != 0: 
                return False
        if year % 100 != 0:
                return True
        if year % 400 != 0:
                return False
        return True
 
def nextDay(year, month, day):
    if isLeap(year):
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
    if day < months[month-1]:
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
    """
    Calculates the number of days between two dates.
    """
    
    assert date1BeforeDate2(year1, month1, day1, year2, month2, day2)
    date = year1, month1, day1
    condition = date1BeforeDate2(date[0], date[1], date[2], year2, month2, day2)
    days = 0
    
    while(condition):
        days = days + 1
        date = nextDay(date[0], date[1], date[2]) 
        condition = date1BeforeDate2(date[0], date[1], date[2], year2, month2, day2)
    return days
