from random import randrange
from math import ceil, log2

print("*** WELCOME TO THE NUMBER GUESSING GAME! ***")

lower_bound = int(input("enter the lower bound: "))
upper_bound = int(input("enter the upper bound: "))

number_to_be_guessed = randrange(lower_bound, upper_bound)

chances = ceil(log2(upper_bound - lower_bound + 1))

print("You have", chances, "chances to guess the number!")

while chances > 0:

    user_guess = int(input("try to guess the number: "))

    if user_guess == number_to_be_guessed:
        print("congratulations! you guessed the number! YOU WIN!!!")
        break

    if user_guess > number_to_be_guessed:
        print("sorry! you guessed too high...")
    elif user_guess < number_to_be_guessed:
        print("sorry! you guessed too small...")

    chances -= 1

else:
    print("sorry! YOU LOSE...")