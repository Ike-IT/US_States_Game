import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)  # Dis call promts d turtle 2 take d form of d image passed 2 it.

data = pandas.read_csv("50_states.csv")
# print(data)
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                    prompt="What's another state's name?").title()
    # print(answer_state)
    if answer_state == "Exit":
        missing_state = [states for states in all_states if states not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        # print(new_data)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:  # D (in) keyword works with if statement only wen d data has bin converted to a (list).
        guessed_states.append(answer_state)  # Dis code adds every correct answer to d empty list above.
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # Dis code returns all d information on d row of d mentioned state.
        print(state_data)
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)  # or dis t.write(state_data.state.item()) returns d same answer.

# States to learn csv


# """D method/function below returns the (x & y) coordinate of each state in U.S. on click."""


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()  # Dis works like exitonclick.
