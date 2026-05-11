# import turtle
# from turtle import Turtle, Screen
# import random
#
# is_game_on = False
#
# screen = Screen()
# screen.setup(700, 500)
# user_bet = screen.textinput(title="Car Race", prompt="Which car will win? Enter a color (red, blue, green, orange, purple)")
# colors = ["red", "blue", "green", "orange", "purple"]
# y_positions = [-80, -40, 0, 40, 80]
# all_cars = []
#
# # Scoreboard turtle
# scoreboard = Turtle()
# scoreboard.hideturtle()
# scoreboard.penup()
# scoreboard.goto(0, 210)
# scoreboard.color("white")
#
# screen.bgcolor("black")
#
# for car_index in range(0, 5):
#     new_car = Turtle(shape="square")
#     new_car.color(colors[car_index])
#     new_car.penup()
#     new_car.goto(x=-320, y=y_positions[car_index])
#     all_cars.append(new_car)
#
# if user_bet:
#     is_game_on = True
#
# while is_game_on:
#     for car in all_cars:
#         if car.xcor() > 320:
#             is_game_on = False
#             winning_color = car.pencolor()
#             if winning_color == user_bet:
#                 scoreboard.write(f"You WON! {winning_color} car won!", align="center", font=("Arial", 16, "bold"))
#             else:
#                 scoreboard.write(f"You LOST! {winning_color} car won!", align="center", font=("Arial", 16, "bold"))
#
#         random_movement = random.randint(2, 12)
#         car.forward(random_movement)
#
# screen.exitonclick()


#----------day 19---------------------------
#-----------day 20-------------------------
#-----------day 21-------------------------
# from turtle import Turtle
# import random
#
#
# class Food(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
#         self.color("blue")
#         self.speed("fastest")
#         self.refresh()
#
#     def refresh(self):
#         random_x = random.randint(-280, 280)
#         random_y = random.randint(-280, 280)
#         self.goto(random_x, random_y)



#-----------day 21-------------------------
#-----------day 22-------------------------

# from turtle import Turtle
#
# class Scoreboard(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.l_score = 0
#         self.r_score = 0
#         self.update_scoreboard()
#
#     def update_scoreboard(self):
#         self.clear()
#         self.goto(-100, 200)
#         self.write(self.l_score, align = "center", font = ("courier", 80, "normal"))
#         self.goto(100, 200)
#         self.write(self.r_score, align="center", font=("courier", 80, "normal"))
#
#     def l_point(self):
#         self.l_score += 1
#         self.update_scoreboard()
#
#     def r_point(self):
#         self.r_score += 1
#         self.update_scoreboard()


#-----------day 22-------------------------------------
#-----------day 23-------turtle-crossing---------------

# from turtle import Turtle
#
# FONT = ("Courier", 24, "normal")
#
# class Scoreboard(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.level = 1
#         self.hideturtle()
#         self.penup()
#         self.goto(-280, 250)
#         self.update_scoreboard()
#
#
#     def update_scoreboard(self):
#         self.clear()
#         self.write(f"level: {self.level}", align="left", font=FONT)
#
#     def increase_level(self):
#         self.level += 1
#         self.update_scoreboard()
#
#     def game_over(self):
#         self.goto(0,0)
#         self.write(f"GAME OVER", align="center", font=FONT)


#-----------day 23----------------------------------------------------------
#-----------day 24-------file system + snake game highscore-----------------


"""below will be on a tab called board"""
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f" Score {self.score} High score {self.high_score}", align= ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
