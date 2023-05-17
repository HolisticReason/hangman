# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## New file: milestone_2.py.
Initial code to initialise variables and take input from user to begin game.
Uses a list of words from which to randomly select.
User input is then validated against a string of alphabetical letters

## New file: milestone_3.py
Development of file milestone_2.py, with two functions:

    ask_for_input() - iteratively requests user input of first guess.
                      validated for being a single letter and alphabetic.

    check_guess(str) - Called from above function.
                       Seeks presence of user input in random word.

## New file: milestone_4.py
Development of file milestone_3.py, with functions turned into methods in new class Hangman:

### Class variables:

    word_list       - list of available words given when constructing a Hangman object.
    num_lives       - Decrementing number of attempts. Default is 5.
    word            - a word randomly chosen from word_list.
    word_guessed    - list to hold each correctly guessed letter in position. Defulats to a line of
                      underscores, one for each letter position. 
    num_letters     - number of letters in randomly generated word.
    list_of_guesses - accumulating list of letters guessed so far.

### Methods:

    ask_for_input() - Iteratively request user to enter a letter for their guess.
                      Validated for being a single letter, alphabetic and not having already been entered.
                      If valid, below function check_guess is called, with the guessed letter argument.
                      On return, the guessed letter is appended to the list_of_guesses.

    check_guess(str) - Called from above function with guess value.
                       Enter a for loop to verify whether guessed letter is present in word.
                       If it is, leter is placed into the correct place in word_guessed.
                       If not, message is printed and num_lives is decremented by 1.
                       Return from function and get next user input
