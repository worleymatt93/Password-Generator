import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
amount_of_letters = int(input("How many letters would you like in your password?\n"))
amount_of_numbers = int(input(f"How many numbers would you like?\n"))
amount_of_symbols = int(input(f"How many symbols would you like?\n"))
password_length = amount_of_letters + amount_of_numbers + amount_of_symbols
password = []

for number in range(0, password_length):
    random_character = random.randint(0, 2)
    if random_character == 0:
        random_letter = random.randint(0, 51)
        letter = letters[random_letter]
        password.append(letter)
    elif random_character == 1:
        random_number = random.randint(0, 9)
        number = numbers[random_number]
        password.append(number)
    elif random_character == 2:
        random_symbol = random.randint(0, 8)
        symbol = symbols[random_symbol]
        password.append(symbol)
print(f"Your password is: {"".join(password)}")
