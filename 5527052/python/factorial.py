def calculate_factorial(number):
    if number < 0:
        return "Error message or specific value"
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    return factorial


print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(3))  # Expected output: 6
print(calculate_factorial(-1))  # Expected: Error message or specific value
