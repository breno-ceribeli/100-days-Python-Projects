from art import logo, vs
from game_data import data
from random import choice
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def newOption(previous, lastRound):
    """Generates a new option preventing it from being the same as the last two and returns a list containing a option description and it's followers."""
    optionDescription = previous
    while optionDescription == previous or optionDescription == lastRound:
        option = choice(data)
        optionDescription = f"{prefix_B}{option['name']}, a {option['description']}, from {option['country']}."
    return [optionDescription, option['follower_count']]

def changePrefix(option):
    """Return the option with the right prefix."""
    if option.startswith(prefix_B):
        prefixedOption = option[len(prefix_B):]
        prefixedOption = prefix_A + prefixedOption
    else:
        prefixedOption = prefix_B + option
    return prefixedOption

prefix_A = "Compare A: "
prefix_B = "Against B: "

def higherOrLower():
    score = 0
    scoreMessage = ""
    previousOption = ""
    lastRoundOption = ""
    firstOption = newOption(previousOption, lastRoundOption)
    shouldContinue = True
    print(logo)
    while shouldContinue:
        if scoreMessage != "":
            print(scoreMessage)
        FODescription = firstOption[0]
        FOFollowers = firstOption[1]
        prefixedFO = changePrefix(FODescription)
        print(prefixedFO)
        lastRoundOption = previousOption
        previousOption = FODescription
        print(vs)
        secondOption = newOption(previousOption, lastRoundOption)
        SODescription = secondOption[0]
        SOFollowers = secondOption[1]
        print(SODescription)
        firstOption = secondOption
        userChoice = ""
        while userChoice not in ('A', 'B'):
            userChoice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if (userChoice == 'A' and FOFollowers > SOFollowers) or (userChoice == 'B' and SOFollowers > FOFollowers):
            score += 1
            clear_console()
            print(logo)
            print(f"You're right! Current score: {score}")
        else:
            shouldContinue = False
            clear_console()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
higherOrLower()

while input("Do you want to play again ? Type 'y': ").lower() == "y":
    clear_console()
    higherOrLower()

#Old game data