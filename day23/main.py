import time
from turtle import Screen
from player import Player 
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    if player.is_at_finish_line():
        print("updated to next level")
        car_manager.level_up()
        player.goto_start()
        scoreboard.update_score()

    for car in car_manager.car_list:
        if car.distance(player)< 20:
            scoreboard.game_over()
            game_is_on = False

        


screen.exitonclick()