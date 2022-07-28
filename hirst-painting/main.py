import random
import turtle
from turtle import  Turtle, Screen

import colorgram

# data = colorgram.extract("image.jpg", 70)
color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30), (16, 77, 106)]
turtle.colormode(255)
# for color in data:
#     color_list.append((color.rgb[0], color.rgb[1], color.rgb[2]))
#
#
# print(color_list)
my_turtle = Turtle()
my_sceen = Screen()

def draw_dotted_line():
    for _ in range(10):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.penup()
        my_turtle.fd(50)
        my_turtle.pendown()
        my_turtle.dot(20, random.choice(color_list))

def to_right():
    my_turtle.right(90)
    my_turtle.penup()
    my_turtle.fd(50)
    my_turtle.pendown()
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.right(90)
def to_left():
    my_turtle.left(90)
    my_turtle.penup()
    my_turtle.fd(50)
    my_turtle.pendown()
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.left(90)

for _ in range(5):
    draw_dotted_line()
    to_right()
    draw_dotted_line()
    to_left()
my_sceen.exitonclick()