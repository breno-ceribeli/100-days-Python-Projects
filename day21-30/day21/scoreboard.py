from turtle import Turtle

# Constants for fonts
FONT = ("Courier", 24, "bold")
GAME_OVER_FONT = ("Courier", 35, "bold")


class Scoreboard(Turtle):
    """
    Handles the score display and game over message for the Snake Game.
    Inherits from the Turtle class to use its drawing functionalities.
    """

    def __init__(self):
        """Initializes the scoreboard with a starting score of 0."""
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 287)  # Position the scoreboard at the top-center of the screen
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the displayed score."""
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        """Increments the score by 1 and updates the scoreboard."""
        self.score += 1
        self.clear()  # Clear the previous score display
        self.update_scoreboard()

    def game_over(self):
        """
        Displays a blinking 'GAME OVER' message at the center of the screen.
        The message blinks 2 times before staying visible.
        """
        game_over_turtle = Turtle()  # Create a new Turtle instance for the message
        game_over_turtle.hideturtle()
        game_over_turtle.penup()
        game_over_turtle.color("red")
        game_over_turtle.goto(0, 0)

        def blink_message(counter=5):
            """
            Makes the 'GAME OVER' message blink a specified number of times.
            :param counter: Number of blinks remaining.
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
