from turtle import Turtle
FIRST_COORDINATES = [(20,0), (0,0), (-20,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.snake_person()
        self.head = self.segments[0]


    def snake_person(self):
        for snake_pieces in FIRST_COORDINATES:
            self.grow_snake(snake_pieces)


    def grow_snake(self, snake_pieces):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(snake_pieces)
        self.segments.append(snake)

    def extend_snake(self):
        self.grow_snake(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)
    def down(self):
        self.segments[0].setheading(270)
    def left(self):
        self.segments[0].setheading(180)
    def right(self):
        self.segments[0].setheading(0)