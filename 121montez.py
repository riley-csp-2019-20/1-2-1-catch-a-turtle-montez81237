# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
#-----game configuration----
# make smaller
#got ten seconds
turtleshape = "circle"
turtlesize = .09
turtlecolor = "red"
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False

score = 0
#-----initialize turtle-----
m = trtl.Turtle(shape = turtleshape)
m.color(turtlecolor)
m.shapesize(turtlesize)
m.speed(0)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-370,270)
score_writer.ht()
score_writer.clear()
font_setup = ("Arial", 30, "bold")

score_writer.write(score, font=font_setup)

counter = trtl.Turtle()
counter.speed(0)
counter.ht()
counter.penup()
counter.goto(275,275)
#-----game functions--------
def turtle_click(x,y):
    print("m got clicked")
    change_position()
    update_score()


def change_position():
    m.penup()
    m.ht()
    if not timer_up:
        mx = random.randint(-412, 400)
        my = random.randint(-300, 300)
        m.goto(mx,my)
        m.st()

def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
    global timer , timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Game Over", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)
#-----events----------------#
m.onclick(turtle_click)


wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()