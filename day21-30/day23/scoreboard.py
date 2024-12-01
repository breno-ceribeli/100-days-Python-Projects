from turtle import Turtle

# Constants for font styles used in the scoreboard
FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    """
    Represents the scoreboard for the Turtle Crossing game.
    Tracks and displays the player's level and shows a game over message.
    """

    def __init__(self):
        """
        Initialize the scoreboard with its starting position and initial level.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230, 265)
        self.level = 0
        self.level_update()

    def level_update(self):
        """
        Update the scoreboard to display the current level.
        Clears the previous display and increments the level by 1.
        """
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="center", font=FONT)

    def game_over(self):
        """
        Display the "Game Over" message at the center of the screen.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
