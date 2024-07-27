from art import logo, vs
from game_data import data
from random import choice
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def new_option(previous, last_round):
    """Generates a new option preventing it from being the same as the last two and returns the option description and it's followers."""
    option_description = previous
    while option_description == previous or option_description == last_round:
        option = choice(data)
        option_description = f"{prefix_B}{option['name']}, a {option['description']}, from {option['country']}."
    return (option_description, option['follower_count'])

def change_prefix(option):
    """Return the option changing the prefix B to prefix A."""
    prefixed_option = option[len(prefix_B):]
    prefixed_option = prefix_A + prefixed_option
    return prefixed_option

prefix_A = "Compare A: "
prefix_B = "Against B: "

def higher_or_lower():
    score = 0
    score_message = ""
    previous_option = ""
    last_round_option = ""
    first_option_description, first_option_followers = new_option(previous_option, last_round_option)
    should_continue = True
    print(logo)
    while should_continue:
        if score_message != "":
            print(score_message)
        prefixed_first_option = change_prefix(first_option_description)
        print(prefixed_first_option)
        last_round_option = previous_option
        previous_option = first_option_description
        print(vs)
        second_option_description, second_option_followers = new_option(previous_option, last_round_option)
        print(second_option_description)
        user_guess = ""
        while user_guess not in ('A', 'B'):
            user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if (user_guess == 'A' and first_option_followers > second_option_followers) or (user_guess == 'B' and second_option_followers > first_option_followers):
            score += 1
            clear_console()
            print(logo)
            print(f"You're right! Current score: {score}")
        else:
            should_continue = False
            clear_console()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
        first_option_description = second_option_description
        first_option_followers = second_option_followers
higher_or_lower()

while input("Do you want to play again ? Type 'y': ").lower() == "y":
    clear_console()
    higher_or_lower()

#Old game data