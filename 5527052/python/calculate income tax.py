def calculate_income_tax(income):
    brackets = [
        (5000, 0.0),  
        (10000, 0.1),  
        (20000, 0.2),  
        (30000, 0.3),  
        (None, 0.4),   
    ]
    
    tax = 0.0
    remaining_income = income
    
    for i in range(len(brackets)):
        upper = brackets[i][0]
        rate = brackets[i][1]
        
        if upper is None:
            tax += remaining_income * rate
            break
        
        if income > upper:
            tax += (upper - (brackets[i-1][0] if i > 0 else 0)) * rate
            remaining_income -= upper
        else:
            tax += remaining_income * rate
            break
    
    return tax

income = 35000
tax = calculate_income_tax(income)
print(f"The tax for an income of {income} is {tax:.2f}")
