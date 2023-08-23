from turtle import Turtle
from random import randint,choice
from snakes import COLORS

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        self.color(choice(COLORS))
        random_x = randint(-270,270)
        random_y = randint(-270, 270)
        self.goto(random_x, random_x)

