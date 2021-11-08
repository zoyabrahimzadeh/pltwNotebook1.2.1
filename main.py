# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random as rand
#-----game configuration----
turtle_color = 'lightgreen'
turtle_size = 1
turtle_shape = 'square'
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
colors = ['purple', 'blue', 'lightblue', 'yellow', 'white', 'yellow', 'green', 'pink']
sizes = [3, 2.5, 2, 1.5, 1.2, 1, 0.75, 0.5]
#-----initialize turtle-----
shortie = turtle.Turtle()
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(350,285)
shortie.shape(turtle_shape)
shortie.fillcolor(turtle_color)
shortie.shapesize(turtle_size)
counter =  turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-300, 285)
#-----game functions--------
def shortie_clicked(x, y):
  change_color()
  change_size()
  shortie.color('lightgreen')
  change_position()
  score_writer.clear()
  update_score()
  global timer_up
  if timer_up == False:
    change_position()
    score_writer.clear()
    update_score()
  else:
      shortie.hideturtle()
def change_position():
  new_xpos = rand.randint(-400,400)
  new_ypos = rand.randint(-300, 300)
  shortie.penup()
  shortie.hideturtle()
  shortie.goto(new_xpos, new_ypos)
  shortie.showturtle()
  shortie.pendown()
def update_score():
  global score
  score += 1
  score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def change_color():
  shortie.color(rand.choice(colors))
  shortie.stamp()
def change_size():
  shortie.turtlesize(rand.choice(sizes))
#-----events----------------
wn = turtle.Screen()
wn.bgcolor('red')
wn.ontimer(countdown, counter_interval) 
shortie.onclick(shortie_clicked)
wn.mainloop()