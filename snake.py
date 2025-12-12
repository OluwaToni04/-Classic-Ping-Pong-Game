from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segement(position)

    def add_segement(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.segment.append(new_turtle)

    def extend(self):
        self.add_segement(self.segment[-1].position())


    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            nex_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(nex_x, new_y)
        self.head.forward(MOVE_DISTANCE )

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



