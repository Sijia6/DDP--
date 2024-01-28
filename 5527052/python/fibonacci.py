def fibonacci_sequence(max_value):
    if max_value < 0:
        return "Empty list or error message"
    sequence = [0]
    next_value = 1
    while next_value <= max_value:
        sequence.append(next_value)
        next_value = sequence[-1] + sequence[-2]
    return sequence

# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Empty list or error message
