from turtle import Turtle

class Scoreboard(Turtle):
    """
    Represents the scoreboard in the Pong game. It keeps track of the scores
    for both players and displays them on the screen.

    Attributes:
        SCORE_FONT (tuple): Font style for displaying the scores.
        WINNING_FONT (tuple): Font style for displaying the winning message.
    """

    SCORE_FONT = ("Courier", 70, "bold")
    WINNING_FONT = ("Courier", 20, "bold")

    def __init__(self):
        """
        Initialize the scoreboard with initial scores set to 0
        and display the scoreboard on the screen.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clear the previous scores and display the updated scores on the screen.
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=self.SCORE_FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=self.SCORE_FONT)

    def r_point(self):
        """
        Increment the right player's score and update the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        """
        Increment the left player's score and update the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def winning_message(self):
        """
        Display the winning message on the screen based on the scores.
        """
        self.goto(0, 0)
        side = "Right" if self.r_score > self.l_score else "Left"
        self.write(f"The {side} sided player won.", align="center", font=self.WINNING_FONT)
