from turtle import Turtle

class Paddle(Turtle):
    """
    Represents a paddle in the Pong game.
    """

    def __init__(self, position):
        """
        Initialize the paddle object at the specified position.

        Args:
            position (tuple): The initial (x, y) position of the paddle.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        """
        Move the paddle upwards by 20 units.
        """
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        """
        Move the paddle downwards by 20 units.
        """
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
