from turtle import Turtle
from random import choice
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
COLORS = ["violet", "red", "green", "cyan", "blue", "pink", "yellow", "orange"]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color(choice(COLORS))
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

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

    def is_game_over(self):
        """Checks if snake collides with walls or its body."""
        x = self.head.xcor()
        y = self.head.ycor()
        if x > 290 or x < -290 or y < -290 or y > 290:
            print("Game Over")
            return True
        for segment in self.segments[1:]:
            if segment.distance(self.head) < 10:
                return True
        return False