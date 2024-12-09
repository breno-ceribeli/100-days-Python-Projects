from turtle import Turtle
import random


class Food(Turtle):
    """
    A class representing the food in the Snake Game.
    Handles the creation, positioning, and repositioning of the food item.
    """

    def __init__(self):
        """Initializes the food with its attributes."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")

    def generate_coordinates(self):
        """
        Generates random coordinates for the food within the game boundaries.
        Ensures the coordinates are multiples of 20 to align with the grid.
        Returns:
            tuple: Random x and y coordinates.
        """
        random_x = random.randint(-280, 280)
        random_x -= random_x % 20
        random_y = random.randint(-280, 280)
        random_y -= random_y % 20
        return random_x, random_y

    def refresh(self, snake_positions):
        """
        Repositions the food to a random location that does not overlap with the snake.
        Args:
            snake_positions (list): List of tuples representing the positions of snake segments.
        """
        random_x, random_y = self.generate_coordinates()
        while (random_x, random_y) in snake_positions:
            random_x, random_y = self.generate_coordinates()
        self.goto(random_x, random_y)
