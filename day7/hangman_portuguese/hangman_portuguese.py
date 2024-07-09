import random
from hangman_words import word_list
from hangman_art import logo, stages
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

end_of_game = False

chosen_word = random.choice(word_list)

word_lenght = len(chosen_word)

lives = 6

display = []

for _ in range(word_lenght):
    display.append("_")

print(logo + "\n")
print("*Não use qualquer tipo de acentuação.*\n")

guessed_letters = []

while not end_of_game:
    guess = input("Escolha uma letra: ").lower()
    clear_console()

    if guess in guessed_letters:
        print(f"Você já escolheu a letra {guess}. Tente outra.")
    else:
        guessed_letters.append(guess)
        if guess in chosen_word:
            for position in range(word_lenght):
                if guess == chosen_word[position]:
                    display[position] = guess
        else:
            lives -= 1
            print(f"A letra {guess} não está nesta palavra.")

    print(stages[lives])
    print(f"{' '.join(display)}\n")

    if "_" not in display:
        end_of_game = True
        print("Você venceu!")
    elif lives == 0:
        end_of_game = True
        print("Você perdeu.")
        print(f"A palavra era: {chosen_word}")