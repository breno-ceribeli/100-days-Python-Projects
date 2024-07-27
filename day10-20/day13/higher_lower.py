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
    """Generates a new option preventing it from being the same as the last two and returns the option description and it's followers."""
    optionDescription = previous
    while optionDescription == previous or optionDescription == lastRound:
        option = choice(data)
        optionDescription = f"{prefix_B}{option['name']}, a {option['description']}, from {option['country']}."
    return (optionDescription, option['follower_count'])

def changePrefix(option):
    """Return the option changing the prefix B to prefix A."""
    prefixedOption = option[len(prefix_B):]
    prefixedOption = prefix_A + prefixedOption
    return prefixedOption

prefix_A = "Compare A: "
prefix_B = "Against B: "

def higherOrLower():
    score = 0
    scoreMessage = ""
    previousOption = ""
    lastRoundOption = ""
    FODescription, FOFollowers = newOption(previousOption, lastRoundOption)
    shouldContinue = True
    print(logo)
    while shouldContinue:
        if scoreMessage != "":
            print(scoreMessage)
        prefixedFO = changePrefix(FODescription)
        print(prefixedFO)
        lastRoundOption = previousOption
        previousOption = FODescription
        print(vs)
        SODescription, SOFollowers = newOption(previousOption, lastRoundOption)
        print(SODescription)
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
        FODescription = SODescription
        FOFollowers = SOFollowers
higherOrLower()

while input("Do you want to play again ? Type 'y': ").lower() == "y":
    clear_console()
    higherOrLower()

#Old game data