import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
screen.listen()
screen.onkey(player.up, key="Up")
game_is_on = True
count = 0
car_managers = []
speed = 0.1

while game_is_on:

    time.sleep(speed)
    if count % 4 == 0:
        car_manager = CarManager()
        if len(car_managers) > 0:
            if abs(car_managers[-1].xcor()) - abs(car_manager.xcor()) > 10 or abs(car_managers[-1].ycor()) - abs(car_manager.ycor() > 10):
                car_managers.append(car_manager)
        if len(car_managers) == 0:
            car_managers.append(car_manager)
        for i in range(0, len(car_managers)):
            if car_managers[i].distance(player) < 30:
                game_is_on = False
                score.lose()
                time.sleep(1)
                break
            car_managers[i].move()
        if 300 - player.ycor() < 20:
            player.start()
            score.update_score()
            speed = speed * 0.8

    count = count + 1
    screen.update()
