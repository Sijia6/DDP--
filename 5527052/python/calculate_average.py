def calculate_average(numbers):
    if numbers:  
        return sum(numbers) / len(numbers)
    else:
        return 0  


numbers_list = [12, 34, 56, 70, 99]
average = calculate_average(numbers_list)
print(average)
