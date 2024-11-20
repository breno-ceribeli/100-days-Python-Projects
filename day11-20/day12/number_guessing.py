from random import randint
from art import logo
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def compareNumber(guess, number):
    """Compare the number guessed to the correct number and prints if the number is bigger, smaller or equals the correct number."""
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    else:
        print(f"You got it! The number is {number}.")

def numberGame():
    number = randint(1, 100)

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    dificulty = input("Choose a dificulty. Type 'infinite', 'easy' or 'hard': ").lower()
    while dificulty not in ('infinite', 'easy', 'hard'):
        dificulty = input("Type 'infinite', 'easy' or 'hard': ").lower()
    if dificulty == "infinite":
        attempts = "infinite"
    elif dificulty == "easy":
        attempts = 10
    else:
        attempts = 5
    userGuess = ""
    while userGuess != number and attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        userGuess = input("Make a guess: ")
        while not userGuess.isdigit():
            userGuess = input("The guess should contain only a number: ")
        userGuess = int(userGuess)
        compareNumber(userGuess, number)
        if attempts != "infinite":
            attempts -= 1
        if attempts != 0 and userGuess != number:
            print("Guess again.")
        elif attempts == 0:
            print(f"You've run out of guesses. The number was {number}.")
numberGame()
while input("Do you want to play again ? Type 'y': ").lower() == "y":
    clear_console()
    numberGame()