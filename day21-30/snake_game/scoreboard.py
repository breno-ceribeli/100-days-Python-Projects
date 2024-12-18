from turtle import Turtle
import os

# Constants for fonts
FONT = ("Courier", 24, "bold")
GAME_OVER_FONT = ("Courier", 35, "bold")

DATA_PATH = os.path.join(os.path.dirname(__file__), "data.txt")


class Scoreboard(Turtle):
    """
    Handles the score display and game over message for the Snake Game.
    Inherits from the Turtle class to use its drawing functionalities.
    """

    def __init__(self):
        """
        Initializes the scoreboard with a starting score of 0 and loads the high score from a file.
        If the file is not found or contains invalid data, it initializes the high score to 0.
        """
        super().__init__()
        self.score = 0
        try:
            with open(DATA_PATH, mode='r') as data_file:
                self.high_score = int(data_file.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.game_speed = 0.1
        self.increase_speed_score = 10
        self.hideturtle()
        self.penup()
        self.goto(0, 287)  # Position the scoreboard at the top-center of the screen
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the displayed score and high score on the screen."""
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align="center", font=FONT)

    def increase_score(self):
        """Increments the score by 1, updates the scoreboard and increases the game speed."""
        self.score += 1
        self.clear()  # Clear the previous score display
        self.update_scoreboard()
        if self.score == self.increase_speed_score:
            self.game_speed *= 0.9

    def game_over(self):
        """
        Displays a blinking 'GAME OVER' message at the center of the screen.
        If the current score exceeds the high score, updates the high score in the file.
        """
        if self.score > self.high_score:
            with open(DATA_PATH, 'w') as data_file:
                data_file.write(f"{self.score}")
        game_over_turtle = Turtle()  # Create a new Turtle instance for the message
        game_over_turtle.hideturtle()
        game_over_turtle.penup()
        game_over_turtle.color("red")
        game_over_turtle.goto(0, 0)

        def blink_message(counter=5):
            """
            Makes the 'GAME OVER' message blink a specified number of times.
            Args:
                counter (int): Number of blinks remaining.
            """
            if counter > 0:
                if game_over_turtle.isvisible():
                    game_over_turtle.clear()
                    game_over_turtle.hideturtle()
                else:
                    game_over_turtle.write("GAME OVER", align="center", font=GAME_OVER_FONT)
                    game_over_turtle.showturtle()
                # Set a timer to call the blink_message function again after 500 ms
                self.getscreen().ontimer(lambda: blink_message(counter - 1), 500)
            else:
                # Ensure the message remains visible after blinking
                game_over_turtle.write("GAME OVER", align="center", font=GAME_OVER_FONT)

        blink_message()
    
    def reset_scoreboard(self):
        self.clear()
        self.score = 0
        self.update_scoreboard()
