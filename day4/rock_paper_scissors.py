import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [
    [rock, paper, scissors],
    ["rock", "paper", "scissors"]
]

choice = input("What do you choose: Rock, Paper or Scissors ?\n").lower()
if choice == "rock" or choice == "paper" or choice == "scissors":
#OR if choice in ("rock", "paper", "scissors"):
#This checks if choice is in the tuple
    choiceIndex = options[1].index(choice)
    print(options[0][choiceIndex])
#Through an array, I checked the position of the text, and since it is the same as the figure, I simply print the figure corresponding to that index.

    computerChoice = random.randint(0, 2)
    print("Computer chose:")
    print(options[0][computerChoice])

    if choiceIndex == computerChoice:
        print("It's a draw")
    elif choiceIndex == 0 and computerChoice == 2:
        print("You win!")
    elif choiceIndex == 2 and computerChoice == 0:
        print("You lose")
    elif choiceIndex > computerChoice:
        print("You win!")
    else:
        print("You lose")
else:
    print("You typed an invalid option. You lose") 