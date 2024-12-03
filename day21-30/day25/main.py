import turtle
from writer import Writer
import pandas
import os

BASE_PATH = os.path.dirname(__file__)
IMAGE = os.path.join(BASE_PATH, "blank_states_img.gif")
DATA = os.path.join(BASE_PATH, "50_states.csv")

screen = turtle.Screen()
screen.title("Name the U.S. states")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

states_data = pandas.read_csv(DATA)

writer = Writer()

guessed_states = []

answer_state = ""
while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?")
        if answer_state != None:
            answer_state = answer_state.title()
            if answer_state == "Exit":
                missing_states = list(set(states_data.state.to_list()).difference(set(guessed_states)))
                missing_states.sort()
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv(f"{BASE_PATH}/states_to_learn.csv")
                break

            elif answer_state in states_data.state.to_list():
                guessed_states.append(answer_state)
                state = states_data[states_data.state == answer_state].squeeze()
                state_x = state.x
                state_y = state.y
                writer.write_state_name(answer_state, state_x, state_y)
                states_data = states_data[states_data.state != answer_state]

