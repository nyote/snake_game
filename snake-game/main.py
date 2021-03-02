import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
snake = Snake()
food = Food()
score = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:


    screen.update()
    time.sleep(0.1)

    snake.move_snake()
    #detect eating the food
    if snake.head.distance(food) < 15:
        food.new_food()
        score.add_score()
        snake.extend_snake()
    #detecting crushing into the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        with open("high_score.txt", mode="w") as file:
            file.write(str(score.high_score))
        # score.game_over()
        # game_is_on = False
    #detecting crushing into itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()
            with open("high_score.txt", mode="w") as file:
                file.write(str(score.high_score))
            # score.game_over()
            # game_is_on = False


screen.exitonclick()