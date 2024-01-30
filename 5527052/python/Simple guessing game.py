import random

number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Make a guess (1-100): "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low, try again.")
    elif guess > number_to_guess:
        print("Too high, try again.")
    else:
        print(f"Congratulations, you guessed it! The number was {number_to_guess}, and it took you {attempts} attempts.")
        break
