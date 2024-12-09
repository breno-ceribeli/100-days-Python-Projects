import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nrLetters= int(input("How many letters would you like in your password?\n")) 
nrNumbers = int(input("How many numbers would you like?\n"))
nrSymbols = int(input("How many symbols would you like?\n"))

passwordList = []

# Loop runs 'nrLetters' times to add the desired number of letters
for char in range(nrLetters):
    # Select a random letter from the 'letters' list and add it to the Password List
    passwordList.append(random.choice(letters))

for char in range(nrNumbers):
    passwordList.append(random.choice(numbers))

for char in range(nrSymbols):
    passwordList.append(random.choice(symbols))

# Shuffle the list to mix the characters
random.shuffle(passwordList)

# Join the list into a single string to form the final password
password = ''.join(passwordList)
# Join Method: The string whose method is called is inserted in between each given string. The result is returned as a new string.

print(f"Here is your password: {password}")