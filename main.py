from turtle import Turtle, Screen
import random
race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Select your turtle")
colors = ["red", "blue", "green", "orange", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
if user_bet:
    race_on = True

for index in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[index])
    t.goto(x=-230, y=y_positions[index])
    turtles.append(t)

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            if user_bet == turtle.pencolor():
                print("Congrats! You've won!")
            else:
                print(f"Sorry! You've lose. The {turtle.pencolor().upper()} turtle is the winner.")
        d = random.randint(0, 10)
        turtle.forward(d)


screen.exitonclick()


