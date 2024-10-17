# Passowrd Generator

import random
import string

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to the PyPassowrd Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many nymbers would you like?\n"))

pwd = ""
letter = random.choices(letters, k=nr_letters)
l = ''.join(letter)
pwd += l

num = random.choices(numbers, k=nr_numbers)
n = ''.join(num)
pwd += n

symbol = random.choices(symbols, k=nr_symbols)
sym = ''.join(symbol)
pwd += sym

print(pwd)
