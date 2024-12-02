import os

# Get the main directory where the script is located
MAIN_PATH = os.path.dirname(__file__)

# Define the path for the directory where personalized letters will be saved
NAMED_LETTERS_PATH = f"{MAIN_PATH}/named_letters"

# Define the string to be replaced by the names
PLACEHOLDER = "[name]"

# Read the names from the 'names.txt' file and store them in the 'names' list
with open(f"{MAIN_PATH}/names.txt", mode="r") as names_file:
    names = names_file.readlines()

# Process the list of names to remove line breaks and extra spaces
name_count = 0
for name in names[:]: 
    correct_name = name.strip()
    if correct_name != "":
        names[name_count] = correct_name
        name_count += 1

# Read the content of the original letter from the 'original_letter.txt' file
with open(f"{MAIN_PATH}/original_letter.txt", mode="r") as original_letter:
    letter = original_letter.read()

# Ensure that the 'named_letters' directory exists
os.makedirs(f"{NAMED_LETTERS_PATH}", exist_ok=True)

# Replace the [name] placeholder with each person's name and save the personalized letters
for name in names:
    personalized_letter = letter.replace(PLACEHOLDER, f"{name}")
    with open(f"{NAMED_LETTERS_PATH}/{name}_letter.txt", mode="w") as new_letter:
        new_letter.write(personalized_letter)
