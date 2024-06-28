from turtle import Screen, Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(xcor, ycor)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
