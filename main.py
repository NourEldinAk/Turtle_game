from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time 

screen = Screen()
screen.setup(width=600 , height=600)
screen.tracer(0)


player = Player()
scoreboard = ScoreBoard()
speed = 0
screen.listen()
screen.onkey(key="w",fun=player.move)
game_on = True
counter = 0
step = 0.1
cars = []
while game_on:
    if counter%6 ==0:
        car_manager = CarManager(speed)
        cars.append(car_manager)
    time.sleep(step)
    screen.update()
    for car in cars:
        car.move()
        if player.distance(car)<27:
            player.clear()
            car.clear()
            scoreboard.gameover()
            game_on = False
    if player.reset():
        # speed+=10
        step*= 0.6
        scoreboard.level+=1
        scoreboard.draw_score()
    counter+=1

screen.exitonclick()