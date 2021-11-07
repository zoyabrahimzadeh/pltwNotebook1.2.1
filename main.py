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
#-----initialize turtle-----
shortie = turtle.Turtle()
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(350,250)
shortie.shape(turtle_shape)
shortie.fillcolor(turtle_color)
shortie.shapesize(turtle_size)
#-----game functions--------
def shortie_clicked(x, y):
  change_position()
  score_writer.clear()
  update_score()
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
#-----events----------------
shortie.onclick(shortie_clicked)
wn = turtle.Screen()
wn.mainloop()