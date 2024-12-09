import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Create game components
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Configure keyboard controls
screen.listen()  # Activate keyboard listening
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    # Check for collisions between the player and the cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            screen.update()
            scoreboard.game_over()

    # Check if the player has reached the finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_car_speed()
        scoreboard.level_update()

screen.exitonclick()
