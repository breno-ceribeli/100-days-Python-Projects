from turtle import Turtle

# Constants for player positioning and movement
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """
    Represents the player's character in the Turtle Crossing game.
    The player is a turtle that moves vertically and aims to reach the finish line.
    """

    def __init__(self):
        """
        Initialize the player turtle with its starting position and orientation.
        """
        super().__init__(shape="turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        """
        Move the player upward by a fixed distance.
        """
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """
        Move the player downward by a fixed distance, ensuring it doesn't go below the starting line.
        """
        if self.ycor() > -280:
            self.setheading(270)
            self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """
        Reset the player's position to the starting point.
        """
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """
        Check if the player has reached the finish line.

        Returns:
            bool: True if the player is at or beyond the finish line, False otherwise.
        """
        return self.ycor() > FINISH_LINE_Y
