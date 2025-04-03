from random import randrange
from math import ceil, log2

print("*** WELCOME TO THE NUMBER GUESSING GAME! ***")

lower_bound = int(input("enter the lower bound: "))
upper_bound = int(input("enter the upper bound: "))

number_to_be_guessed = randrange(lower_bound, upper_bound)

chances = ceil(log2(upper_bound - lower_bound + 1))

print("You have", chances, "chances to guess the number!")