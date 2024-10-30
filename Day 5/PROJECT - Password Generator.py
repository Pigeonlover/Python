# RANDOM PASSWORD GENERATOR

import random

letters = int(input("Hello, how many letters would you like in your new password?\n"))

symbols = int(input("And how many symbols?\n"))

numbers = int(input("Finally, how many numbers?\n"))

lett = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symb = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


gen_password = ""

x = 0
while x < letters:
    gen_password += random.choice(lett)
    x += 1


y = 0
while y < symbols:
    gen_password += random.choice(symb)
    y += 1


z = 0
while z < numbers:
    gen_password += random.choice(numb)
    z += 1

    
final = list(gen_password)
random.shuffle(final)
password = ''.join(final)
print(password)
