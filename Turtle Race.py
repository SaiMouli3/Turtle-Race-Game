import random
from turtle import Turtle,Screen

screen=Screen()
is_race_on=False
screen.setup(500,400)
x=screen.textinput(title="Make ur Bet",prompt="which turtle will Win")
print(x)
all_t=[]
col=["red","green","orange","black","blue","yellow","purple"]
y=[-70,-40,-10,20,50,80]
for t in range(0,6):
    tim = Turtle("turtle")
    tim.color(col[t])
    tim.penup()
    tim.goto(x=-230, y=y[t])
    all_t.append(tim)

if x:
    is_race_on=True
while is_race_on:
    for t  in all_t:
        if t.xcor()>230:
            is_race_on=False
            win_clr=t.pencolor()
            if (win_clr== x):
                print(f"Won!{win_clr}")
            else:
                print("you lost")



        ran=random.randint(0,12)
        t.forward(ran)




screen.exitonclick()
