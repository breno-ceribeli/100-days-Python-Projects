from turtle import Turtle

class Ball(Turtle):
    """
    Represents the ball in the Pong game.
    """

    def __init__(self):
        """
        Initialize the ball with its starting properties.
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        Update the ball's position based on its current movement increments.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        """
        Reverse the ball's vertical direction when it collides with a wall.
        """
        self.y_move *= -1

    def paddle_bounce(self, paddle):
        """
        Reverse the ball's horizontal direction and increase speed after hitting a paddle.

        Args:
            paddle (str): Indicates which paddle ('r' for right, anything else for left) the ball collided with.
        """
        if paddle == 'r':
            self.x_move = -10
        else:
            self.x_move = 10
        self.move_speed *= 0.9  # Increase the ball's speed by reducing the move delay

    def reset_position(self):
        """
        Reset the ball's position to the center and reverse its horizontal direction.
        """
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1
