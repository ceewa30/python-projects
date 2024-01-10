#  https://en.wikipedia.org/wiki/Hangman_(game)
#  https://hangmanwordgame.com/?fca=1&success=0#/

import random
from hangman_art import stages, logo
from hangman_words import word_list


chosen_word = random.choice(word_list)

# Testing code
# print(f"The solution is {chosen_word}.")
print(logo)

wordlen = len(chosen_word)

lives = 6

display = []
for _ in range(wordlen):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(wordlen):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"The puzzle word is : {chosen_word} You lose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])