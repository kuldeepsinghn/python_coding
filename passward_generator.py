import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
          'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
print("Welcome to the Python Passward Generator")
num_letters = int(input("How many letter would you like in your passward\n"))
num_number = int(input("How many number would you like in your passward\n"))
num_symbols = int(input("How many symbols would you like in your passward\n"))

passward = ""

for char in range(1, num_letters + 1):
    passward += random.choice(letter)

for char in range(1, num_number + 1):
    passward += random.choice(numbers)

for char in range(1, num_symbols + 1):
    passward += random.choice(symbols)

print(passward)
