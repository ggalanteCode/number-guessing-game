from random import randrange

print("*** WELCOME TO THE NUMBER GUESSING GAME! ***")

lower_bound = int(input("enter the lower bound: "))
upper_bound = int(input("enter the upper bound: "))

number_to_be_guessed = randrange(lower_bound, upper_bound)