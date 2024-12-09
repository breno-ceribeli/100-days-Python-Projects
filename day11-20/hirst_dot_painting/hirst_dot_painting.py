import turtle as t
import random
from color_extracting import colors

t.colormode(255)
painter = t.Turtle()
painter.speed(0)
painter.hideturtle()
painter.teleport(-200, -300)
num_lines = 10
num_columns = 10
for i in range(num_lines):
    painter.teleport(-200, painter.ycor() + 50)
    for j in range(num_columns):
        painter.dot(20, random.choice(colors))
        painter.teleport(painter.xcor() + 50, painter.ycor())



screen = t.Screen()
screen.exitonclick()