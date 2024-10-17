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

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))


# random.shuffle(password_list)
# print(password_list)

# passd = ""
# for char in password_list:
#     passd += char

# print(f"Your password is: {passd}")


p = ""
for i in range(1, len(password_list) + 1):
    p += random.choice(password_list)

print(p)
