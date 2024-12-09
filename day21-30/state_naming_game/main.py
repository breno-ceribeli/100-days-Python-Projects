import turtle
from writer import Writer
import pandas
import os

BASE_PATH = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(BASE_PATH, "blank_states_img.gif")
DATA_PATH = os.path.join(BASE_PATH, "50_states.csv")

# Set up the turtle screen and load the US map image
screen = turtle.Screen()
screen.title("Name the U.S. States")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

# Load states data from CSV
states_data = pandas.read_csv(DATA_PATH)

# Initialize the Writer class for labeling states on the map
writer = Writer()

# List to store correctly guessed states
guessed_states = []

# Main game loop
answer_state = ""
while len(guessed_states) < 50:  # Run until all 50 states are guessed
    # Get user input for a state name
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state name?"
    )
    
    if answer_state is not None:  # Check if input is not empty
        answer_state = answer_state.title()  # Ensure the input has proper capitalization
        
        if answer_state == "Exit":
            # Create a list of missing states (not guessed)
            all_states = states_data.state.to_list()
            missing_states = [state for state in all_states if state not in guessed_states]
            
            # Save missing states to a CSV file
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv(f"{BASE_PATH}/states_to_learn.csv")
            break

        elif answer_state in states_data.state.to_list():  # Check if input is a valid state name
            guessed_states.append(answer_state)  # Add the guessed state to the list
            
            # Get the coordinates of the guessed state
            state = states_data[states_data.state == answer_state].squeeze()
            state_x = state.x
            state_y = state.y
            
            # Write the state's name on the map at the corresponding location
            writer.write_state_name(answer_state, state_x, state_y)
            
            # Remove the guessed state from the DataFrame
            states_data = states_data[states_data.state != answer_state]
