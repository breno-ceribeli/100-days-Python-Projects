import pandas
import os
import unicodedata

BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, "nato_phonetic_alphabet.csv")

# Read the CSV file containing the NATO phonetic alphabet
data = pandas.read_csv(DATA_PATH)

# Create a dictionary from the CSV, mapping letters to their phonetic codes
data_dict = {row.letter: row.code for index, row in data.iterrows()}

# Inform the user about the "EXIT" keyword to end the program
print("Type \033[31mEXIT\033[0m to end the program.")  # Adds red-colored "EXIT" for emphasis

# Start an infinite loop to continually prompt the user for input
while True:
    # Normalize user input to remove accents and convert it to uppercase
    user_input = unicodedata.normalize("NFKD", input("Type your word: ")).encode('ASCII', 'ignore').decode('ASCII').upper()
    
    # Check if the user wants to exit the program
    if user_input == "EXIT":
        break
    
    # Check if the input contains only alphabetic characters
    elif not user_input.isalpha() and user_input != "":
        print("Type only letters.")
    
    else:
        # Create a list of phonetic code words for each letter in the input
        code_words = [data_dict[letter] for letter in user_input]
        
        # Print the code words in green text for better readability
        print(f"\033[32mCode Words:\033[0m {' '.join(code_words)}")
