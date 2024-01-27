def speeding_ticket(speed, is_birthday):
    more=5
    if is_birthday:
        if speed <=(60+more):
           return "No Ticket"
        elif speed >=(61+more)and speed<=(80+more):
           return "Small Ticket"
        elif speed >=(81+more):
           return"Big Ticket"
       
    if not is_birthday:
        if speed <=60:
           return "No Ticket"
        elif speed >=61 and speed<=80:
           return "Small Ticket"
        elif speed >=81:
           return"Big Ticket"
        
       
print(speeding_ticket(60, False))  
print(speeding_ticket(75, False))  
print(speeding_ticket(85, False))
print(speeding_ticket(65, True))
print(speeding_ticket(85, True)) 
