# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random as rand
#-----game configuration----
turtle_color = 'lightgreen'
turtle_size = 3
turtle_shape = 'square'
#-----initialize turtle-----
shortie = turtle.Turtle()
shortie.shape(turtle_shape)
shortie.fillcolor(turtle_color)
shortie.shapesize(turtle_size)
#-----game functions--------
def shortie_clicked(x, y):
  print("shorties been clicked! got to move her!")

#-----events----------------
shortie.onclick(shortie_clicked)
wn = turtle.Screen()
wn.mainloop()