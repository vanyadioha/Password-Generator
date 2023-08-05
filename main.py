# Python Password Generator
import random

letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
letter_list = letters.split()
numbers = "0 1 2 3 4 5 6 7 8 9"
number_list = numbers.split()
symbols = "! @ # $ % & * ( ) + ^"
symbol_list = symbols.split()

print("Welcome to the Password.py")
password_letters_upper = int(
    input("How many upper case letters would you like in your password?\n")
)
password_letters_lower = int(
    input("How many lower case letters would you like in your password?\n")
)
password_symbols = int(input("How many symbols would you like in your password?\n"))
password_numbers = int(input("How many numbers would you like in your password?\n"))

pword_upper = []
for upper in range(1, password_letters_upper + 1):
    random_letter = random.choice(letter_list)
    pword_upper.append(random_letter.upper())

pword_lower = []
for lower in range(1, password_letters_lower + 1):
    random_letter = random.choice(letter_list)
    pword_lower.append(random_letter)

pword_number = []
for number in range(1, password_numbers + 1):
    random_number = random.choice(number_list)
    pword_number.append(random_number)

pword_symbol = []
for symbol in range(1, password_symbols + 1):
    random_symbol = random.choice(symbol_list)
    pword_symbol.append(random_symbol)

# Password Creator
pword_chars = [
    *pword_upper,
    *pword_lower,
    *pword_number,
    *pword_symbol,
]
password = ""
for char in range(0, len(pword_chars)):
    choice = random.choice(pword_chars)
    password += choice
    pword_chars.remove(choice)
print(f" Your password is: {password}")
