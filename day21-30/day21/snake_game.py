from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import pygame
import os

# Paths for audio files
base_dir = os.path.dirname(__file__)
music_path = os.path.join(base_dir, "audio", "snake_chase.mp3")
food_path = os.path.join(base_dir, "audio", "food_collect.mp3")
game_over_path = os.path.join(base_dir, "audio", "game_over.mp3")

# Screen setup
screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Draw the game outline
outline = Turtle()
outline.hideturtle()
outline.color("white")
outline.penup()
outline.speed("fastest")
outline.goto(-290, 290)
outline.pendown()
outline.goto(290, 290)
outline.goto(290, -290)
outline.goto(-290, -290)
outline.goto(-290, 290)

# Initialize pygame mixer for background music and sound effects
pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(0.35)
food_collect_sound = pygame.mixer.Sound(food_path)
game_over_sound = pygame.mixer.Sound(game_over_path)
pygame.mixer.music.play(-1)

# Display start message
start_message = Turtle()
start_message.hideturtle()
start_message.penup()
start_message.color("white")
start_message.goto(0, 0)

# Variables for start message blinking and game start condition
show_message = True
start_game = False

# Start game function triggered by pressing space
def start():
    global start_game
    start_game = True

# Listen for the space key to start the game
screen.listen()
screen.onkey(start, "space")

# Blinking start message loop
while not start_game:
    if show_message:
        start_message.write("Press SPACE to start", align="center", font=("Courier", 20, "bold"))
        time.sleep(0.5)
    else:
        start_message.clear()
        time.sleep(1)
    show_message = not show_message
    screen.update()
start_message.clear()

# Initialize game components
snake = Snake()
food = Food()
food.refresh([segment.position() for segment in snake.segments])
scoreboard = Scoreboard()

# Configure controls for snake movement
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(scoreboard.game_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) <= 15:
        food.refresh([segment.position() for segment in snake.segments])
        snake.extend()
        scoreboard.increase_score()
        food_collect_sound.play()
    
    # Detect collision with walls
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Play game over sound and fade out background music
game_over_sound.play(loops=1)
pygame.mixer.music.fadeout(4000)

# Wait for user click to exit the game
screen.exitonclick()
