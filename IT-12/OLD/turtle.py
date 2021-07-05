#im done with life
#Author: jChisholm204
#Date: 2021-05-28

#import modules
import turtle
death = turtle.Turtle()
from tkinter import *
main = Tk()

#create movement class
class movement:
  def moveUp(event):
    death.forward(10)
  def moveDown(event):
    death.back(10)
  def moveRight(event):
    death.right(45)
  def moveLeft(event):
    death.left(45)
  def penUp(event):
    death.penup()
  def penDown(event):
    death.pendown()
  def circle(event):
    death.circle(15)

main.bind('<Left>', movement.moveLeft) 
main.bind('<Right>', movement.moveRight)
main.bind('<Up>', movement.moveUp) 
main.bind('<Down>', movement.moveDown)
main.bind('u', movement.penUp)
main.bind('d', movement.penDown)
main.bind('c', movement.circle)
main.mainloop()

########################################################

import turtle
colors = {"green":"#42692f", "brown":"#765c48"}
def draw_tree(level):
    if level == 0:
        turtle.color(colors["green"])
        turtle.stamp()
        turtle.color(colors["brown"])
    else:
        turtle.pensize(level)
        turtle.forward(30)
        turtle.left(20)
        draw_tree(level-1)
        turtle.right(40)
        draw_tree(level-1)
        turtle.left(20)
        turtle.back(30)
turtle.color(colors["brown"])
turtle.speed(0)
turtle.left(90)
scr = turtle.Screen()
draw_tree(5)
scr.exitonclick()