import random
from hangman_words import word_list
from hangman_art import logo, stages
import os
#Module for clearing the console
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

end_of_game = False

#Chooses a random word out of the list.
chosen_word = random.choice(word_list)

#This variable will help the code to easier to read and simplify the loops
word_lenght = len(chosen_word)

#The quantity of times that the player can guess a wrong letter
lives = 6

#Creates a display that will contain all of the '_' that will be replaced by the right letters.
display = []

#for letter in chosen_word:
for _ in range(word_lenght):
    #display += "_"
    display.append("_")

print(logo + "\n")

guessed_letters = []

while not end_of_game:
    #Assign the letter guessed to a variable in lowercase.
    guess = input("Choose a letter: ").lower()

    clear_console()

    if guess in guessed_letters:
        print(f"You have already guessed {guess}. Try another one.")
    else:
        guessed_letters.append(guess)
        #Checks if the letter guessed is one of the letters of the chosen word and changes the display to show that letter at the right positions. If the letter isn't one of the letters, reduces the number of lives by 1
        if guess in chosen_word:
            for position in range(word_lenght):
                if guess == chosen_word[position]:
                    display[position] = guess
        else:
            lives -= 1
            print(f"The letter {guess} is not on this word.")
        
    print(stages[lives])
    print(f"{" ".join(display)}\n")

    if "_" not in display:
        end_of_game = True
        print("You won")
    elif lives == 0:
        end_of_game = True
        print("You lose")
        print(f"The word was: {chosen_word}")