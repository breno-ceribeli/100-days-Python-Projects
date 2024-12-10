import pandas
from tkinter import *
import os
import random

BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, "data")
IMAGE_PATH = os.path.join(BASE_PATH, "images")

BACKGROUND_COLOR = "#B1DDC6"

try:
    # Try to load words that need to be learned
    data = pandas.read_csv(f"{DATA_PATH}/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    # If the file doesn't exist or is empty, load the default English words file
    data = pandas.read_csv(f"{DATA_PATH}/english_words.csv")

# Convert the data to a list of dictionaries
to_learn = data.to_dict(orient="records")
current_card = {}
button_enabled = True  # Variable to control button states

def next_card():
    """
    Display the next card by randomly selecting a word from the 'to_learn' list.
    If there are no words left, display a completion message and disable buttons.
    """
    global current_card, flip_timer, button_enabled
    window.after_cancel(flip_timer)  # Cancel the flip timer for the current card

    # Check if there are words left to learn
    if not to_learn:
        canvas.itemconfig(language_text, text="Parabéns!", fill="black")
        canvas.itemconfig(word_text, text="Você aprendeu todas as palavras!", fill="black", font=("Ariel", 35))
        canvas.itemconfig(card_image, image=card_front)
        check_button.config(state="disabled")
        cross_button.config(state="disabled")
        return

    # Select a random word from the list
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="Inglês", fill="black")
    canvas.itemconfig(word_text, text=current_card["English"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(5000, flip_card)  # Set a timer to flip the card
    button_enabled = False  # Disable the 'check' button temporarily

def is_known():
    """
    Remove the current card from the 'to_learn' list and save the updated list to a file.
    Then, display the next card.
    """
    global button_enabled
    if button_enabled:
        to_learn.remove(current_card)  # Remove the known card from the list
        data = pandas.DataFrame(to_learn)
        data.to_csv(f"{DATA_PATH}/words_to_learn.csv", index=False)  # Save the updated list
        next_card()

def flip_card():
    """
    Flip the current card to display the translation (in Portuguese).
    Reactivate the 'check' button after flipping the card.
    """
    global current_card, button_enabled
    canvas.itemconfig(language_text, text="Português", fill="white")
    canvas.itemconfig(word_text, text=current_card["Portuguese"], fill="white")
    canvas.itemconfig(card_image, image=card_back)
    button_enabled = True  # Enable the 'check' button after flipping

# Create the main application window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set a timer to flip the card
flip_timer = window.after(5000, flip_card)

# Create the canvas for displaying cards
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=f"{IMAGE_PATH}/card_front.png")
card_back = PhotoImage(file=f"{IMAGE_PATH}/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Create the 'cross' button for skipping the current card
cross_image = PhotoImage(file=f"{IMAGE_PATH}/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, cursor="hand2", command=next_card)
cross_button.grid(row=1, column=0)

# Create the 'check' button for marking the current card as known
check_image = PhotoImage(file=f"{IMAGE_PATH}/right.png")
check_button = Button(image=check_image, highlightthickness=0, cursor="hand2", command=is_known)
check_button.grid(row=1, column=1)

# Start the application by displaying the first card
next_card()

window.mainloop()
