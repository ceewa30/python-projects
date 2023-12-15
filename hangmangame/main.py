#  https://en.wikipedia.org/wiki/Hangman_(game)
#  https://hangmanwordgame.com/?fca=1&success=0#/

import random

# TODO 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

# TODO 2 - Ask the user to guess a letter and assign their answer to a variable called guess.  Make guess lowercase.

guess = input("Guess a letter: ").lower()
   
# TODO 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for word in chosen_word:
    if word == guess:
        print("Right")
    else:
        print("Wrong")