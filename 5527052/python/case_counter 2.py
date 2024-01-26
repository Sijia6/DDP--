def case_counter(text):
    
    uppercase_count = sum(1 for char in text if char.isupper())
    lowercase_count = sum(1 for char in text if char.islower())
    
    print(f"Uppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}")

case_counter("Hello World!")  
case_counter("PYTHON")  
case_counter("python")  
case_counter("1234!@#$")  
