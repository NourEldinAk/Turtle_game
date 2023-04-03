COLORS = ["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 30


from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self,level):
        super().__init__()
        self.cars = []
        self.level = level
        self.speed = 0
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.random_y = random.randint(-250,250)
        self.penup()
        self.goto(300, self.random_y)
        self.setheading(180)
        self.cars.append(self)
    
    def move(self):
        for car in self.cars:
            car.fd(STARTING_MOVE_DISTANCE + self.level)
            