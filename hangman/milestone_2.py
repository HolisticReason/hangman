# Hangman project - milestone 2

import random

# string of valid letters
alpha_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# list of words
word_list = ["Apple", "Orange", "Mango", "Peach", "Plum"]
print(word_list)

# choose one at random
word = random.choice(word_list)
print(word)

# get user guess until valid
while True:
    guess = input("Please enter a single letter of the alphabet: ").upper()

    if len(guess) != 1 or guess not in alpha_string:
        print("Oops! That is not a valid input.")
    else:
        print(f"You entered the letter {guess}")
        break