from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game v1")
screen.tracer(0)

snake = Snake()
food = Food()

# control the snake

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard = Scoreboard()

end_of_game = False
while not end_of_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.all_segments[0].distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update_display()

    x_cor = snake.all_segments[0].xcor()
    y_cor = snake.all_segments[0].ycor()

    if x_cor > 285 or x_cor < -285 or y_cor > 285 or y_cor < -285:
        end_of_game = True
        scoreboard.game_over()

    for body in snake.all_segments[1:]:
        if snake.all_segments[0].distance(body) < 10:
            end_of_game = True
            scoreboard.game_over()

screen.exitonclick()
