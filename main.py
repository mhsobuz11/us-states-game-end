import turtle
import pandas as pd

screen=turtle.Screen()
screen.title("U.S. State Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()

guesses_state=[]

while len(guesses_state)<50:
    ans_state = screen.textinput(title=f"{len(guesses_state)}/50 Guess The State",
                                 prompt="What's the another state's name?").title()
    if ans_state=="Exit":
        missing_state=[]
        for state in all_states:
            if state not in guesses_state:
                missing_state.append(state)
        new_data=pd.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break

    if ans_state in all_states:
        guesses_state.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(ans_state)


screen.exitonclick()