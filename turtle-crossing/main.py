import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
game_is_on = True
screen.listen()
screen.onkey(player.move, 'Up')

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    for current_car in car.all_cars:
        if player.distance(current_car) < 20:
            game_is_on = False
            scoreboard.game_over()
        if player.distance(x=0, y=255) < 20:
            scoreboard.increase_score()
            car.increase_speed()
            player.goto(0, -280)



screen.exitonclick()
