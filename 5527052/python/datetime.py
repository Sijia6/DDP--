from datetime import datetime

def day_of_year(year, month, day):

    given_date = datetime(year, month, day)
 
    day_of_year = (given_date - datetime(year, 1, 1)).days + 1
    return day_of_year

year = 2024  
month = 2  
day = 1  


print(f"{year}-{month}-{day} is the {day_of_year(year, month, day)}th day of the year {year}.")
