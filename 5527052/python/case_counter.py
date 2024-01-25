def case_counter(text):
    uppercase_count = sum(1 for char in text if char.isupper())
    lowercase_count = sum(1 for char in text if char.islower())
    return uppercase_count, lowercase_count
print(case_counter("PYTHON"))
print(case_counter("Hello,world"))
print(case_counter("Python"))
