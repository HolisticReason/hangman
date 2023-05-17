# Hangman project - milestone 3

import random

# get user guess until valid
def ask_for_input():

    while True:
        guess = input("Please enter a single letter of the alphabet: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Oops! That is not a valid input.")
        else:
            break

    check_guess(guess.lower())


# Check whether the user's guess is in the word
def check_guess(guess):

    if guess in word:
        print(f"Good guess, {guess} is in the word")
    else:   
        print(f"Sorry, {guess} is not in the word. Try again.")


# list of words
word_list = ["apple", "orange", "mango", "peach", "plum"]
print(word_list)

# choose a word at random
word = random.choice(word_list)
print(word)

ask_for_input()
