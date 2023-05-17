# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

New file: milestone_2.py.
Initial code to initialise variables and take input from user to begin game.
Uses a list of words from which to randomly select.
User input is then validated against a string of alphabetical letters

New file: milestone_3.py
Development of file milestone_2.py, with two functions:
    ask_for_input() - iteratively requests user input of first guess.
                      validated for being a single letter and alphabetic.

    check_guess(str) - Called from above function.
                       Seeks presence of user input in random word.
