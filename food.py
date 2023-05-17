# Renders itself as a small circle. When the snake touches it, food moves to new location. 

from turtle import Turtle
import random

class Food(Turtle):
    # We want the food class to inherit from turtle:
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        self.refresh()
        # ^ We can use these attributes bc we inherited from the super class

    # Create new random x and y and get the food to go to this location. 
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)