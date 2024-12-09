from turtle import Turtle

class Writer(Turtle):
    """
    A Writer class that extends the Turtle class to display state names on a map.
    This class handles writing text on specific coordinates on the screen.
    """
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
    
    def write_state_name(self, state, x, y):
        """
        Writes the name of a state at the specified (x, y) coordinates on the screen.
        
        Args:
            state (str): The name of the state to display.
            x (int): The x-coordinate on the screen where the name should be written.
            y (int): The y-coordinate on the screen where the name should be written.
        """
        self.goto(x, y)
        self.write(state, align="center")