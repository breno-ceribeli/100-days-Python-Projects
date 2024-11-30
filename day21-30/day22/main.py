from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import pygame
import os

# Paths for audio files
base_dir = os.path.dirname(__file__)
music_path = os.path.join(base_dir, "audio", "pong_dreams.mp3")
bounce_path = os.path.join(base_dir, "audio", "bounce.mp3")

# Set up the game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Initialize music and sound effects using pygame
pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(0.35)
pygame.mixer.music.play(-1)
bounce_sound = pygame.mixer.Sound(bounce_path)
bounce_sound.set_volume(0.2)

# Configure keyboard controls
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the top and bottom walls
    if abs(ball.ycor()) > 280:
        ball.wall_bounce()
        bounce_sound.play()
    
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce('r')
        bounce_sound.play()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce('l')
        bounce_sound.play()
    
    # Detect if the ball goes out of bounds and update the score
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
    # Check if any player reaches the winning score
    if scoreboard.r_score == 10 or scoreboard.l_score == 10:
        game_is_on = False
        scoreboard.winning_message()

pygame.mixer.music.fadeout(4000)

screen.exitonclick()
