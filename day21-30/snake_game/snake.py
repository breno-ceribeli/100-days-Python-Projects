from turtle import Turtle

# Constants for snake's initial state and movement
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    A class representing the Snake in the Snake Game.
    Handles the creation, movement, and direction control of the snake.
    """

    def __init__(self):
        """Initializes the snake with its segments and head."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.can_change_direction = True  # Flag to prevent instant reverse direction changes

    def create_snake(self):
        """Creates the initial segments of the snake at predefined positions."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        """Adds a new segment to the snake at its tail."""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def move(self):
        """Moves the snake forward by shifting segments to the position of the one in front."""
        self.can_change_direction = True  # Allow direction change after movement
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turns the snake's direction upward if not currently moving down."""
        if self.can_change_direction and self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.can_change_direction = False

    def down(self):
        """Turns the snake's direction downward if not currently moving up."""
        if self.can_change_direction and self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.can_change_direction = False

    def left(self):
        """Turns the snake's direction leftward if not currently moving right."""
        if self.can_change_direction and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.can_change_direction = False

    def right(self):
        """Turns the snake's direction rightward if not currently moving left."""
        if self.can_change_direction and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.can_change_direction = False
