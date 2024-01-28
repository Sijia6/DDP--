def is_leap_year(year):
    if(year%400==0) or (year%4==0 and year%100!=0):
        return True
    else:
        return False


# Test cases
print(is_leap_year(2020))  # Expected output: True
print(is_leap_year(1900))  # Expected output: False
print(is_leap_year(2000))  # Expected output: True
print(is_leap_year(2019))  # Expected output: False
