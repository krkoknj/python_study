import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for i in range(0, nr_letters - nr_symbols - nr_numbers):
    randint = random.randint(0, len(letters) - 1)
    password.append(letters[randint])

for i in range(0, nr_symbols):
    randint = random.randint(0, len(symbols) - 1)
    password.append(symbols[randint])

for i in range(0, nr_numbers):
    randint = random.randint(0, len(numbers) - 1)
    password.append(numbers[randint])

tmp = ''

for i in range(0, 10):
    randint = random.randint(0, len(numbers) - 1)
    tmp = password[i]
    password[i] = password[randint]
    password[randint] = tmp

a = ""
for pwd in password:
    a+=pwd
print(a)