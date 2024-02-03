from datetime import datetime

def date_passed(todays_date, scheduled_date):
    date_format ="%dth %B"
    todays_datetime = datetime.strptime(todays_date, date_format)
    scheduled_datetime = datetime.strptime(scheduled_date, date_format)
 
    if todays_datetime > scheduled_datetime:
        print("Scheduled date has passed.") 
    elif todays_datetime == scheduled_datetime:
        print("Scheduled date is today.")
    else:
        print("Scheduled date is yet to pass.")   
    
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
