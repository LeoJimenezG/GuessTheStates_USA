import turtle
import pandas as pd

# Create the screen and the map
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
us_map = turtle.Turtle()
turtle.addshape(image)
us_map.shape(image)
# Create the turtle to write
state = turtle.Turtle()
state.penup()
state.hideturtle()

# Get the data
data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
x_cords = data["x"].to_list()
y_cords = data["y"].to_list()
# Variables to use
guessed_states = []

# Keep the game on
while len(guessed_states) < 50:
    # Ask the user for their answer
    answer = screen.textinput(title=f"Guess the state {len(guessed_states)}/50",
                              prompt="Write an state name").capitalize()
    # Check if the user wants to exit
    if answer == "Exit":
        break
    # Check if the answer is in the state list but not in the guessed ones list
    if answer in states and answer not in guessed_states:
        # Save the answer to avoid repetition and count points
        guessed_states.append(answer)
        # Get the coordinates using the index of the answer to look for in x and y lists
        cords = (x_cords[states.index(answer)], y_cords[states.index(answer)])
        # Write the answer on the right place
        state.goto(cords)
        state.write(arg=answer, align="center", font=("Arial", 10, "normal"))

# Create a list of not guessed states
missing_state = [state for state in states if state not in guessed_states]
# Convert list to dictionary for having a column header
states_to_learn = {"state": missing_state}
# Convert the dictionary into a dataframe
states_file = pd.DataFrame(states_to_learn)
# Create the csv file
states_file.to_csv("States_To_Learn.csv")
