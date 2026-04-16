# data = [
#     {
#         'name': 'instagram',
#         'follower_count': 346,
#         'description': 'social media platform',
#         'country' : 'united states'
#     },
#     {
#         'name': 'christiano ronaldo',
#         'follower_count': 215,
#         'description': 'footballer',
#         'country' : 'portugal'
#     },
#     {
#         'name': 'ariana grande',
#         'follower_count': 185,
#         'description': 'musician and actress',
#         'country' : 'united states'
#     },
#     {
#         'name': 'dwayne johnson',
#         'follower_count': 181,
#         'description': 'actor and professional wrestler',
#         'country' : 'united states'
#     },
#     {
#         'name': 'selena gomez',
#         'follower_count': 174,
#         'description': 'musician actress',
#         'country' : 'united states'
#     },
#     {
#         'name': 'kylie jenner',
#         'follower_count': 172,
#         'description': 'reality tv personality and businesswoman and self-made bill',
#         'country' : 'united states'
#     },
#     {
#         'name': 'kim kardashian',
#         'follower_count': 167,
#         'description': 'reality tv personality and businesswoman',
#         'country' : 'united states'
#     }
#
# ]
#----------------------------

# while is_on:
#     choice = input ("state your preference mtn/glo/airtel: ")
#     if choice == "exit":
#         is_on = False
#     else:
#         network = networks[choice]
#         if is_system_sufficient(network["airtime"]):
#             payment = process_payment()
#             if transaction_is_sucessful(payment, network["cost"]):
#                 make_dispense(choice, network["airtime"])
#
#
# program_is_on = True
#
# while program_is_on:
#     choice = input ("select your course math/english/economics")
#     if choice == "shutdown":
#         program_is_on = False
#     else:
#         my_subject = list_of_courses[choice]
#         if seat_are_available(my_subject["core"]):
#             payment = process_payment()
#             if payment_is_succesful(payment, my_subject["cost"]):
#                 make_payment (choice, my_subject["core"])
#
#
# while cinema_is_open:
#     choice = input ("select movie to watch avatar/story/romance")
#     if choice == "close":
#         cinema_is_on = False
#     else:
#         to_watch = list_of_movie["choice"]
#         if seat_is_available(to_watch["movie"]):
#             payment = process_payment()
#             if payment_is_successful(payment, to_watch["cost"]):
#                 issue_ticket(choice, to_watch["movie"])
#
#
# warehouse_is_open = True
#
# while warehouse_is_open:
#     choice = input ("select the item you want shirt/short/cap")
#     if choice == "stop":
#         warehouse_is_open = False
#     else:
#         request = inventory["choice"]
#         if stock_level_is_ok(request["item"]):
#             payment = process_payment()
#             if billing_is_successful(payment, request["cost"]):
#                 proceed_to_dispatch(choice, request["item"])


#---------------------------
#another_variable = 12

# from turtle import Turtle, Screen
# my_screen = Screen()
#
# alex = Turtle()
# alex.shape("turtle")
# alex.color("green")
# alex.forward(150)
#
# print (my_screen.canvheight)
#my_screen.exitonclick()
#------------------------------------------
# from turtle import Turtle, Screen
# pen = Turtle()
# pen.shape("arrow")
# pen.color("red")
# pen.forward(100)
# pen.left(90)
# pen.forward(100)
#
# display = Screen()
#
# display.exitonclick()

#_________________________________________
# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         if self == user:
#             print ("you cannot follow yourself")
#         else:
#             user.followers += 1
#             self.following += 1
#
#     def unfollow(self, user):
#         user.followers -= 1
#         self.following -= 1
#
#     def display_profile(self):
#         print (f"username: {self.username}")
#         print (f"followers: {self.followers}")
#         print (f"following: {self.following}")
#
# user_1 = User("001", "angela")
# user_2 = User ("002", "jack")
# user_3 = User("003", "mike")

# user_2.follow(user_1)
# user_3.follow(user_1)

# user_1.follow(user_2)
# user_1.unfollow(user_2)

# user_1.display_profile()
# user_2.display_profile()
# user_3.display_profile()
# print (user_1.followers)
# print (user_1.following)
# print (user_2.followers)
# print (user_2.following)

# print (user_1.id, user_1.username, user_1.followers)
# print (user_2.id, user_2.username, user_2.followers)

#----------------------------------------------
# class BankAccount:
#
#     def __init__(self, account_number, account_name, pin):
#         self.account_number = account_number
#         self.account_name = account_name
#         self.account_balance = 0
#         self.pin = pin
#         self.transactions = []
#
#     def deposit_money(self, amount):
#         if amount > 0:
#             self.account_balance += amount
#             self.transactions.append(f"deposited {amount}")
#         else:
#             print ("invalid deposit amount")
#
#      def withdraw_money(self, amount, entered_pin):
#         if entered_pin != self.pin:
#             print ("incorrect pin")
#         elif amount > self.account_balance:
#             print ("insufficient balance")
#         else:
#             self.account_balance -= amount
#             self.transactions.append(f"withdraw {amount}")
#             print ("withdraw successful")
#
#     def transfer(self, other_account, amount):
#         if amount > self.account_balance:
#             print ("insufficient balance")
#         else:
#             self.account_balance -= amount
#             other_account.account_balance += amount
#
#     def show_transactions(self):
#         for transaction in self.transactions:
#             print (transaction)
#
#     def check_balance(self):
#         print (f"account number:, {self.account_number}")
#         print (f"account name:, {self.account_name}")
#         print(f"account balance:, {self.account_balance}")
#
# account_1 = BankAccount("M12345", "omasan", 8888)
# account_2 = BankAccount("M12346", "alero", 7777)

# account_1.deposit_money(10000)
# account_1.transfer(account_2, 2400)
# account_1.deposit_money(-200)
# account_1.withdraw_money(2000, 8888)
# account_1.check_balance()

# print (account_1.account_name)
# print (account_1.account_balance)
# account_2.show_transactions()


#-----------------------------------------
# quiz_items = [
#     {"text": "Phishing emails create urgency.", "answer": "True"},
#     {"text": "It’s safe to share OTP with IT.", "answer": "False"},
#     {"text": "Two-factor authentication improves security.", "answer": "True"},
#     {"text": "Public Wi-Fi is always safe.", "answer": "False"}
# ]
#
# class QuizItem:
#     def __init__(self, prompt, solution):
#         self.prompt = prompt
#         self.solution = solution
#
# class QuizManager:
#     def __init__(self, questions):
#         self.current_index = 0
#         self.questions = questions
#         self.points = 0
#         self.incorrect_list = []
#
#     def has_next_question(self):
#         return self.current_index < len(self.questions)
#
#     def ask_next(self):
#         current_question = self.questions[self.current_index]
#         self.current_index += 1
#         user_input = input (f"Q.{self.current_index} : {current_question.prompt} (True/False): ")
#         self.validate_answer (user_input, current_question.solution)
#
#     def validate_answer(self, user_input, correct_solution):
#         if user_input.lower == correct_solution.lower:
#             self.points += 1
#             print ("you got the answer")
#         else:
#             print ("you failed the answer")
#             self.incorrect_list.append(correct_solution)
#         print (f"the correct answer is {correct_solution}")
#         print (f"your current score is {self.points}/{self.current_index}\n")
#
# question_slide = []
#
# for bullet_slide in quiz_items:
#     bullet_question = bullet_slide["text"]
#     bullet_answer = bullet_slide ["answer"]
#     new_bullet_question = QuizItem(bullet_question, bullet_answer)
#     question_slide.append(new_bullet_question)
#
# quiz = QuizManager(question_slide)
#
# while quiz.has_next_question():
#     quiz.ask_next()
#
# print ("you have completed the quiz")
# print (f"your final score is {quiz.points}/{len(quiz.questions)}")
#---------------------------------------------------------------------------

# space_records = [
#     {"prompt": "The Sun is a star.", "response": "True"},
#     {"prompt": "Mars is the closest planet to the Sun.", "response": "False"},
#     {"prompt": "Jupiter is the largest planet in our solar system.", "response": "True"},
#     {"prompt": "The Moon produces its own light.", "response": "False"}
# ]
#
# class SpaceQuestion:
#     def __init__(self, space_statement, space_expected_response):
#         self.statement = space_statement
#         self.expected_response = space_expected_response
#
# class QuizController:
#     def __init__(self, questions):
#         self.question_collection = questions
#         self.current_position = 0
#         self.correct_total = 0
#
#     def has_more_items(self):
#         return self.current_position < len(self.question_collection)
#
#     def present_item(self):
#         active_item = self.question_collection[self.current_position]
#         self.current_position += 1
#         user_input = input (f"Q.{self.current_position} : {active_item.statement} (True/False) ")
#         self.evaluate_response(user_input, active_item.expected_response)
#
#     def evaluate_response(self, user_input, correct_response):
#         if user_input.lower() == correct_response.lower():
#             self.correct_total += 1
#             print ("correct answer")
#         else:
#             print ("wrong answer")
#         print (f"the correct answer is {correct_response}")
#         print (f"your current score is {self.correct_total}/{self.current_position}\n")
#
# compiled_item = []
# for question_nudget in space_records:
#     nudget_test = question_nudget["prompt"]
#     nudget_answer = question_nudget["response"]
#     new_question = SpaceQuestion(nudget_test, nudget_answer)
#     compiled_item.append(new_question)
#
#
# quiz = QuizController(compiled_item)
#
# while quiz.has_more_items():
#     quiz.present_item()
#
# print ("thank you for completing the quiz")
# print (f"you final score is {self.correct_total}/{len(self.question_collection)}")


#---------------------------------------------------------------------------------

# import turtle
# from turtle import Turtle, Screen
# import random
#
# tutle.colormode(255)
# tom = Turtle()
# tom.speed("fastest")
# tom.penup()
# tom.hideturtle()
#
# color_list = [
#     (245, 243, 109), (247, 101, 150), (230, 237, 245), (212, 154, 98), (199, 78, 55),
#     (237, 212, 88), (159, 104, 57), (124, 165, 194), (178, 160, 43), (39, 104, 157),
#     (64, 152, 138), (30, 55, 104), (208, 134, 156), (236, 163, 176), (17, 43, 63),
#     (142, 182, 161), (72, 35, 27), (208, 91, 71), (164, 207, 191), (67, 86, 22),
#     (231, 176, 165), (102, 123, 167), (147, 27, 40), (37, 66, 43), (180, 192, 213)]
#
#
# tom.setheading(255)
# tom.forward(300)
# tom.setheading(0)
# number_of_dot = 100
#
#
# for dot_count in range (1, number_of_dot +1):
#     tom.dot(20, random.choice(color_list))
#     tom.forward(50)
#
#     if dot_count % 10 == 0:
#         tom.setheading(90)
#         tom.forward(50)
#         tom.setheading(180)
#         tom.forward(500)
#         tom.setheading(0)
#
#
#
#
# screen = Screen()
# screen.exitonclick()

#----------------------------------------------

# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
#
# tim = Turtle()
# tim.speed("slowest")
# #tim.penup()
#
# rows = 4
# columns = 6
# dot_size = 20
# gap = 50
#
# colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0)]
#
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
#
# for row in range(rows):
#     for column in range(columns):
#         tim.dot(dot_size, random.choice(colors))
#         tim.forward(gap)
#
#     tim.backward(columns * gap)
#     tim.left(90)
#     tim.forward(gap)
#     tim.right(90)
#
# screen = Screen()
# screen.exitonclick()

#-----------------------------------------------------------------
# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
# tim = Turtle()
# tim.speed("slowest")
# rows = 4
# draw_dots = 6
# gap = 50
# dot_size = 20
#
# color_list = [
#     (245, 243, 109), (247, 101, 150), (230, 237, 245), (212, 154, 98), (199, 78, 55),
#     (237, 212, 88), (159, 104, 57), (124, 165, 194), (178, 160, 43), (39, 104, 157),
#     (64, 152, 138), (30, 55, 104), (208, 134, 156), (236, 163, 176), (17, 43, 63),
#     (142, 182, 161), (72, 35, 27), (208, 91, 71), (164, 207, 191), (67, 86, 22),
#     (231, 176, 165), (102, 123, 167), (147, 27, 40), (37, 66, 43), (180, 192, 213)]
#
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
#
# for row in range (rows):
#     for draw_dot in range (draw_dots):
#         tim.dot(dot_size, random.choice(color_list))
#         tim.forward(gap)
#
#     tim.backward(gap * draw_dots)
#     tim.setheading(90)
#     tim.forward(gap)
#     tim.setheading(0)
#
#
# screen = Screen()
# screen.exitonclick()

#---------------------------------------------------

# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
#
# tim = Turtle()
# tim.speed("slowest")
# #tim.penup()
# #tim.hideturtle()
#
# colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0)]
#
# rows = 10
# cols = 10
# gap = 50
#
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
#
# for row in range(rows):
#
#     for col in range(cols):
#         tim.dot(20, random.choice(colors))
#         tim.forward(gap)
#
#     tim.backward(cols * gap)
#     tim.left(90)
#     tim.forward(gap)
#     tim.right(90)
#
#     if row % 2 == 1:
#         tim.right(180)
#
# screen = Screen()
# screen.exitonclick()

#--------------------------------------------------------

# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
# tim = Turtle()
# tim.speed("fast")
#
# def draw_color():
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     color = (r, b, g)
#     return color
#
# def draw_spirograph(shifting_of_circle):
#     for _ in range (int(360 / shifting_of_circle)):
#         tim.color(draw_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + shifting_of_circle)
#
# draw_spirograph(5)
#
# tim = Screen()
# tim.exitonclick()

#--------------------------------------------
# import turtle
# from turtle import Turtle, Screen
# import random
# is_game_on = False
# #
# # screen = Screen()
# # screen.setup(900, 600)
# # screen.bgcolor("black")
#
#
#
# screen = Screen()
# screen.setup(500, 400)
# screen.bgcolor("grey")
# user_bet = screen.textinput(title = "make a bet", prompt = "which turtle color will win")
# colors = ["red", "green", "yellow", "blue", "brown", "pink"]
# y_position = [-70,-40, -10, 20, 50, 80]
# all_turtle = []
#
# for turtle_index in range (0, 6):
#     new_turtle = Turtle(shape = "triangle")
#     new_turtle.color(colors[turtle_index])
#     new_turtle.penup()
#     new_turtle.goto(x = -230, y = y_position[turtle_index])
#     all_turtle.append(new_turtle)
#
# if user_bet:
#     is_game_on = True
#
# while is_game_on:
#     for turtle in all_turtle:
#         if turtle.xcor() > 230:
#             is_game_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print (f"you won the {winning_color} is the winner")
#             else:
#                 print(f"you lost the {winning_color} is the winner")
#
#         random_movement = random.randint(1, 10)
#         turtle.forward(random_movement)
#
# screen.exitonclick()

#----------day 19---------------------------
#-----------day 20-------------------------
#-----------day 21-------------------------
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

