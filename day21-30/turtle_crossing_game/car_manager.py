from random import randint, choice
from turtle import Turtle

# Constants for car properties
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    """
    Manages the cars in the Turtle Crossing game. Handles car creation,
    movement, and speed adjustments as the game progresses.
    """

    def __init__(self):
        """
        Initialize the car manager with an empty list of cars and a starting speed.
        """
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        """
        Randomly generate a new car with a 1 in 6 chance. Ensures that cars 
        do not spawn too close to one another to avoid overlaps.
        """
        if randint(1, 6) == 1:
            new_x = 320
            new_y = randint(-240, 240)
            
            # Prevent cars from spawning too close to existing cars
            for car in self.cars:
                if abs(car.xcor() - new_x) < 40 and abs(car.ycor() - new_y) < 20:
                    return
            
            # Create a new car
            car = Turtle(shape="square")
            car.penup()
            car.color(choice(COLORS))
            car.setheading(180)
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(new_x, new_y)
            self.cars.append(car)

    def move_cars(self):
        """
        Move all cars across the screen based on the current speed. 
        Remove any car that moves off the left edge of the screen.
        """
        for car in self.cars[:]:  # Iterate through a copy of the list to avoid modification issues
            car.forward(self.car_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)

    def increase_car_speed(self):
        """
        Increase the speed of the cars to make the game more challenging.
        """
        self.car_speed += MOVE_INCREMENT 
