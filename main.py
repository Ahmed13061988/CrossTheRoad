import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player1.distance(car) < 30:
            game_is_on = False
            score.game_over()





screen.exitonclick()
