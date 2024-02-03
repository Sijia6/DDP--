favorite_numbers = {
    'mary': [42, 17],
    'mia': [42, 39, 56],
    'gas': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))