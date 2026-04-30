
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

# from  turtle import Turtle
#
# class Paddle(Turtle):
#
#     def __init__(self, position):
#         super().__init__()
#         self.shape("square")
#         self.color("white")
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.penup()
#         self.goto(position)
#
#     def go_up(self):
#         new_y = self.ycor() + 20
#         self.goto(self.xcor(), new_y)
#
#     def go_down(self):
#         new_y = self.ycor() - 20
#         self.goto(self.xcor(), new_y)
#

#-----------day 22----------------------------------------
#-----------day 23-------------turtle-crossing------------

# from turtle import Turtle
# import random
#
# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10
#
# class CarManager:
#
#     def __init__(self):
#         self.all_cars = []
#         self.car_speed = STARTING_MOVE_DISTANCE
#
#     def create_car(self):
#         random_chance = random.randint(1, 6)
#         if random_chance == 1:
#             new_car = Turtle("square")
#             new_car.shapesize(stretch_wid=1, stretch_len=2)
#             new_car.penup()
#             new_car.color(random.choice(COLORS))
#             random_y = random.randint(-250, 250)
#             new_car.goto(340, random_y)
#             self.all_cars.append(new_car)
#
#     def move_cars(self):
#         for car in self.all_cars:
#             car.backward(self.car_speed)
#
#     def level_up(self):
#         self.car_speed += MOVE_INCREMENT


#-----------day 23----------------------------------------------------------
#-----------day 24-------file system + snake game highscore-----------------


"""below will be on a tab called snake"""
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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


