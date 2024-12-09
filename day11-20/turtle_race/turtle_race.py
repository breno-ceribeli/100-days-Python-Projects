from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
user_bet = ""
colors = ["red", "blue", "green", "purple", "orange", "yellow"]
y_positions = [100, 60, 20, -20, -60, -100]
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet!", prompt="Enter the color of the turtle you want to bet on.").lower()
turtles = []

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    turtles.append(new_turtle)

race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

        turtle.forward(randint(0, 10))


screen.exitonclick()