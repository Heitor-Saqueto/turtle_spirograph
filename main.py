import turtle
from turtle import Turtle, Screen
import random

teddy = Turtle()
teddy.shape("classic")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


teddy.speed(0)


def draw_spiograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        teddy.color(random_color())
        teddy.circle(100)
        teddy.setheading(teddy.heading() + size_of_gap)


draw_spiograph(10)

screen = Screen()
screen.exitonclick()
