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