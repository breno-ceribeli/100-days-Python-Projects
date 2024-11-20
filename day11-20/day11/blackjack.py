import random
from art import logo
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def dealCard(deck):
    """Appends a random card from the card list."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealtCard = random.choice(cards)
    deck.append(dealtCard)

def calculateScore(cards):
    """Takes a list of cards and returns the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return "Blackjack"
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare(userScore, computerScore):
    """Returns a message showing who's the winner."""
    if userScore == computerScore:
        return "Draw 😐"
    elif computerScore == "Blackjack":
        return "You lose, opponent has a Blackjack 😱"
    elif userScore == "Blackjack":
        return "Win with a Blackjack 🤩"
    elif userScore > 21:
        return "You went over. You lose 😭"
    elif computerScore > 21:
        return "Opponent went over. You win 😃"
    elif userScore > computerScore:
        return "You win 😎"
    else:
        return "You lose 😢"

def blackjack():
    userDeck = []
    computerDeck = []
    gameOver = False

    for n in range(2):
        dealCard(userDeck)
        dealCard(computerDeck)

    while not gameOver:
        userScore = calculateScore(userDeck)
        computerScore = calculateScore(computerDeck)
        print(f"    Your cards: {userDeck}, current score: {userScore}")
        print(f"    Dealer's first card: {computerDeck[0]}")

        if userScore == "Blackjack" or computerScore == "Blackjack" or userScore > 21:
            gameOver = True
        else:
            getAnotherCard = input("Type 'y' to get another card or type 'n' to pass: ").lower()
            if getAnotherCard == 'y':
                dealCard(userDeck)
            else:
                gameOver = True

    while computerScore != "Blackjack" and computerScore < 17:
        dealCard(computerDeck)
        computerScore = calculateScore(computerDeck)

    print("Final results:")
    print(f"    Your final hand: {userDeck}, final score: {userScore}")
    print(f"    Dealer's final hand: {computerDeck}, final score: {computerScore}")
    print(compare(userScore, computerScore))

while input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ").lower() == 'y':
    clear_console()
    print(logo)
    blackjack()
print("Goodbye ♥️ ♠️ ♦️ ♣️")