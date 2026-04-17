
#----------day 19---------------------------
#-----------day 20-------------------------
#-----------day 21-------------------------
# from turtle import Turtle
# ALIGNMENT = "center"
# FONT = ("Courier", 24, "normal")
#
#
# class Scoreboard(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()
#         self.update_scoreboard()
#
#     def update_scoreboard(self):
#         self.write(f" Score {self.score}", align= ALIGNMENT, font = FONT)
#
#     def game_over(self):
#         self.goto(0, 0)
#         self.write("GAME OVER", align=ALIGNMENT, font=FONT)
#
#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.write(f" Score {self.score}", align= ALIGNMENT, font= FONT)


#-----------day 21-------------------------
#-----------day 22-------------------------

from  turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
