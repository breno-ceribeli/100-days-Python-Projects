import turtle as t
from random import randint

t.colormode(255)
pen = t.Turtle()

screen = t.Screen()


def move_forward():
    pen.forward(10)


def move_backward():
    pen.backward(10)


def rotate_clockwise():
    pen.right(10)


def rotate_anti_clockwise():
    pen.left(10)


def reset_sketch():
    pen.reset()


def change_color():
    pen.color(randint(0, 255), randint(0, 255), randint(0, 255))


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=rotate_clockwise, key="d")
screen.onkey(fun=rotate_anti_clockwise, key="a")
screen.onkey(fun=reset_sketch, key="c")
screen.onkey(fun=change_color, key="space")

screen.exitonclick()