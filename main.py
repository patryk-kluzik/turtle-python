import random
import turtle
from turtle import Turtle, Screen
from random import choice

#
# import hirst
# from hirst import get_colours_formatted

tommy = Turtle()

tommy.shape("turtle")
colours = ["black", "green", "blue", "red", "brown", "yellow", "purple", "orange"]
direction = [0, 90, 180, 270]
turtle.colormode(255)


# get_colours_formatted()

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple


# def colours_from_image():
#     print(hirst.list_of_colour)
#     return choice(hirst.list_of_colour)


"""
challenge 1 : draw a square
"""
# for i in range(4):
#     tommy.forward(100)
#     tommy.rt(90)

"""
challenge 2 : draw a dashed line
"""
# for i in range(15):
#     tommy.forward(10)
#     tommy.pu()
#     tommy.forward(10)
#     tommy.pd()

"""
challenge 3 : draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
"""
# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         tommy.fd(100)
#         tommy.rt(angle)
#
#
# colours = ["black", "green", "blue", "red", "brown", "yellow", "purple", "orange"]
# for i in range(3, 11):
#     tommy.color(choice(colours))
#     draw_shape(i)
#
# screen = Screen()
# screen.exitonclick()


"""
challenge 4 : draw a random walk
"""
# tommy.width(15)
# tommy.speed(0)
# for i in range(200):
#     tommy.color(random_colour())
#     tommy.seth(choice(direction))
#     tommy.forward(40)

"""
challenge 5: draw a spirograph
"""
# tommy.speed(0)
# num_of_circles = int(input("How many circles do you want to make?: "))
# full_angle_of_rotation = 360
# angle_change = full_angle_of_rotation / num_of_circles
# for n in range(num_of_circles):
#     tommy.color(random_colour())
#     tommy.circle(100)
#     tommy.setheading(tommy.heading() + angle_change)

screen = Screen()
screen.exitonclick()
