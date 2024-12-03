from turtle import Turtle

class Writer(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
    
    def write_state_name(self, state, x, y):
        self.goto(x, y)
        self.write(state, align="center")