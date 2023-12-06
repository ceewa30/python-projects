from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(cipher_direction, new_text, new_shift):
    cipher_text = ""

    if cipher_direction == 'decode':
        new_shift *= -1
    for letter in new_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + new_shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The {cipher_direction}ed text is {cipher_text}")


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(cipher_direction=direction, new_text=text, new_shift=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if restart == "no":
         should_end = True
         print("Goodbye")
