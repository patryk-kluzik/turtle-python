"""
The Hirst Painting Project
"""
import turtle

import colorgram
from random import choice

colours_to_extract = 30
colours = colorgram.extract('image.jpg', colours_to_extract)
list_of_colour = []

for i in range(colours_to_extract):
    current_colour = colours[i]
    rgb = current_colour.rgb
    list_of_colour.append(tuple(rgb))

"""
10 by 10 dots , dot of size 20 , separated by empty by 50 units
"""
from turtle import Turtle, Screen

dot_size = 20
separation = 50
x_length = 460
y_length = 180
y_shift = y_length / 10

screen = Screen()
tom = Turtle()

turtle.colormode(255)

screen.setworldcoordinates(-5, -5, x_length, y_length)
tom.speed("fastest")
tom.hideturtle()
tom.penup()

for n in range(1,101):
    tom.dot(dot_size, choice(list_of_colour))
    tom.fd(separation)
    if n % 10 == 0:
        tom.goto(0, y_shift)
        y_shift += 20

screen.exitonclick()
