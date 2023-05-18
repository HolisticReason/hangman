# Hangman project - milestone 5

import random

class Hangman:
    '''
    This class is used to represent a Hangman game.

    Attribues:

        word_list (list)      : List of available words given when constructing a Hangman object.
        num_lives (int)       : Decrementing number of attempts. Default is 5.
        word (str)            : A word randomly chosen from word_list.
        word_guessed (list)   : List to hold each correctly guessed letter in position. Defulats to a line of
                                underscores, one for each letter position. 
        num_letters (int)     : Number of letters in randomly generated word that are left to guess.
        list_of_guesses (list): Accumulating list of letters guessed so far.
    '''
    def __init__(self, word_list, num_lives=5) -> None:
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
    def ask_for_input(self) -> None:    
        '''
        This method enters a while loop and asks the user to enter a single letter choice.
        This is then validated for being a single letter and alphabetical, whilst also having not already been chosen.
        The function check_guess is then called to check whether the guessed letter is part of the word.
        The guessed letter is then appended to the reference list of guessed letters.
        '''
        while True:
            guess = input("Please enter a single letter of the alphabet: ")

            if len(guess) != 1 or not guess.isalpha():
                print("\nOops! That is not a valid input.")

            elif guess in self.list_of_guesses:
                print(f"\nYou already tried that letter!")  

            else:
                self.check_guess(guess.lower())
                self.list_of_guesses.append(guess)

                # show user progress
                print(self.word_guessed)

                # display the letters so far used
                used = ", ".join(self.list_of_guesses)
                print(f"Letters used so far: {used}") 
                break
   

    # Check whether the user's guess is in the word
    def check_guess(self, guess) -> None:
        '''
        This method checks that the given letter is present in the word.
        If it is, the relevant blank space in word_guessed is replaced with the guessed letter
        and num_letters is reduced by one.
        If not, num_lives is reduced by 1.

        Args:
            guess (str) - the guessed letter from the user
        '''
        if guess in self.word:
            print(f"\nGood guess, {guess} is in the word")

            # add guessed letter to relevant place in word
            for idx, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[idx] = guess # replace underscore with letter
                    self.num_letters -= 1 # one less letter left to guess

        else:  
            self.num_lives -= 1 
            print(f"\nSorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")


# List of available words from which to choose
word_list = ["apple", "orange", "mango", "peach", "plum"]

def play_game(word_list):
    '''
    This function instantiates the Hangman game class
    and loops until the game has been either won or lost.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print(f"\nYou lost. The word was {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("\nCongratulations! You won the game!")
            break

# Start everything off
play_game(word_list)