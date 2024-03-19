# Number Guessing Game !
import random
from logo import logo
print(logo)

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
# print(number)

def guess_number(attempt):
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("You guessed it right!")
            break
        elif guess < number:
            print("Too low!")
            attempt -= 1
        elif guess > number:
            print("Too high!")
            attempt -= 1
    if attempt == 0:
        print("You lost the game. Better luck next time!")


choice = input("Choose a difficulty. Type 'easy' or 'hard' :")

attempts = {'easy': 10, 'hard': 5}

guess_number(attempts.get(choice))
