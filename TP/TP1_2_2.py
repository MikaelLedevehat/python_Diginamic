import random
import math
from turtle import *


def draw_triangle(nb):
    random.seed(2)
    color('red', 'green')


    for e in range(0,nb):
        b = True if round(random.random()) == 0 else False

        left(120 * random.random())
        penup()
        setposition(random.random()*200,random.random()*200)
        pendown()
        if b:
            begin_fill()
        for i in range(0,3):
            forward(10)
            left(120)
        if b:
            end_fill()

def draw_square(nb):
    random.seed(2)
    color('red', 'blue')


    for e in range(0,nb):
        b = True if round(random.random()) == 0 else False

        left(90 * random.random())
        penup()
        setposition(random.random()*200,random.random()*200)
        pendown()
        if b:
            begin_fill()
        for i in range(0,4):
            forward(20)
            left(90)
        if b:
            end_fill()

draw_triangle(5)
draw_square(5)
done()
