from random import randrange
from math import ceil, log2

print("*** WELCOME TO THE NUMBER GUESSING GAME! ***")

lower_bound = int(input("enter the lower bound: "))
upper_bound = int(input("enter the upper bound: "))

number_to_be_guessed = randrange(lower_bound, upper_bound + 1)

chances = ceil(log2(upper_bound - lower_bound + 1))

print(f"You have {chances} chances to guess the number!")

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1

    user_guess = int(input(f"attempt n. {guess_counter}: try to guess the number: "))

    if user_guess == number_to_be_guessed:
        print("congratulations! you guessed the number! YOU WIN!!!")
        break
    elif guess_counter == chances and user_guess != number_to_be_guessed:
        print("sorry! YOU LOSE...")
    elif user_guess > number_to_be_guessed:
        print("sorry! you guessed too high...")
    elif user_guess < number_to_be_guessed:
        print("sorry! you guessed too small...")