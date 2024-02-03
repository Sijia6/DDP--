class Staff:
    
    def __init__(self, given_name, family_name, initial_pay):
        self.first_name = given_name.capitalize()
        self.last_name = family_name.capitalize()
        self.pay = initial_pay
        
    def apply_raise(self, increment=5000):
        self.pay += increment

staff = Staff('john', 'doe', 50000)
print(f"Initial pay: {staff.pay}")

staff.apply_raise()
print(f"Pay after standard raise: {staff.pay}")

staff.apply_raise(10000)
print(f"Pay after custom raise: {staff.pay}")
