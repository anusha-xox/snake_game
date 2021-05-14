from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_segments = []
        self.no_of_segments = 3
        self.create_snake(self.no_of_segments)

    # makes new segments
    def create_snake(self, no_of_segments):
        for i in range(no_of_segments):
            new_segment = Turtle("square")
            new_segment.color("white")
            self.all_segments.append(new_segment)
            new_segment.penup()
            new_segment.goto((-20 * i), 0)
        self.all_segments[0].color("turquoise")

    # gives last segment position of the second last segment, done to make turning easier, 0th seg not iterated in loop
    def move(self):
        for i in range(len(self.all_segments) - 1):
            j = len(self.all_segments) - 1 - i
            self.all_segments[j].goto(self.all_segments[j - 1].position())
        self.all_segments[0].forward(MOVE_DISTANCE)

    # control the snake, NOT statements prevent the snake from going back on itself

    def up(self):
        if self.all_segments[0].heading() != DOWN:
            self.all_segments[0].setheading(90)

    def down(self):
        if self.all_segments[0].heading() != UP:
            self.all_segments[0].setheading(270)

    def left(self):
        if self.all_segments[0].heading() != RIGHT:
            self.all_segments[0].setheading(180)

    def right(self):
        if self.all_segments[0].heading() != LEFT:
            self.all_segments[0].setheading(0)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.all_segments.append(new_segment)
