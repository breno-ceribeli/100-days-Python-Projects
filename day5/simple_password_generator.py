import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nrLetters= int(input("How many letters would you like in your password?\n")) 
nrNumbers = int(input("How many numbers would you like?\n"))
nrSymbols = int(input("How many symbols would you like?\n"))

password = ""

# Loop runs 'nrLetters' times to add the desired number of letters
for char in range(nrLetters):
    # Select a random letter from the 'letters' list and add it to the password
    password += letters[random.randint(0, len(letters) - 1)]

for char in range(nrNumbers):
    password += numbers[random.randint(0, len(numbers) - 1)]

for char in range(nrSymbols):
    password += symbols[random.randint(0, len(symbols) - 1)]

print(f"Here is your password: {password}")