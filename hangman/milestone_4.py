# Hangman project - milestone 3

import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list # populate list of words to choose from
        self.num_lives = num_lives

        self.word = random.choice(word_list) # choose a word at random

        # initiliase with underscores
        self.word_guessed = [] 
        for count in range(len(self.word)):
            self.word_guessed.append("_")
            
        self.num_letters = len(self.word)
        self.list_of_guesses = []

        #print(self.word)
        print(self.word_guessed)

    # get user guess until valid
    def ask_for_input(self):    

        while True:
            guess = input("Please enter a single letter of the alphabet: ")

            if len(guess) != 1 or not guess.isalpha():
                print("Oops! That is not a valid input.")
            elif guess in self.list_of_guesses:
                print(f"You already tried that letter!")  
            else:
                self.check_guess(guess.lower())
                self.list_of_guesses.append(guess)

            if self.num_lives == 0:
                break

            print(self.list_of_guesses)
            print(self.word_guessed)

    # Check whether the user's guess is in the word
    def check_guess(self, guess):

        if guess in self.word:
            print(f"Good guess, {guess} is in the word")

            # add guessed letter to word
            for idx, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[idx] = guess

            self.num_letters -= 1
        else:  
            self.num_lives -= 1 
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")


game = Hangman(["apple", "orange", "mango", "peach", "plum"])
game.ask_for_input()