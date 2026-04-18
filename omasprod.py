# from nt import mkdir
# from operator import truediv
#
# from charset_normalizer.cd import alphabet_languages, mb_encoding_languages
# from Demos.EvtSubscribe_pull import query_text


############
#print("Welcome to the brand Name Generator.")
#city = input("Which city did you grow up in?\n")
#pet = input("What is the name of a pet?\n")
#print ("Your band name could be: "+city+" " + pet)

#print("hello"[2])
#print(type("abc"))
#print(type(123))
#print(type(1.3))
#print(type(true))

#name_of_the_user = input("enter your name? ")
#Length_of_name = len(name_of_the_user)

#print("Number of letters in your name: " + str(Length_of_name))

#print(type("Number of letters in your name: "))
#print(type(Length_of_name))

#print("hello")

# Bmi = 84 / 1.65 ** 2
#print(Bmi)
#print(round(Bmi, 2))

#print(round(5/3, 2))

#score = 5
#height = 1.8
#is_winning = True

#print (f"your score is {score}, your height is {height}, your winning is {is_winning}")
#print(6 + 4 / 2 - (1 * 2))

#a = int("5") / int(2.7)
#print (a)

#name = input("what is your name?")
#print(f"Hello, {name}")

#name = input("What is your name?")
#print("Hello, " + name)

#age = 12
#print(f"You are {age} years old")

# age = 12
# print("You are " + age + " years old")

# fruits = ["apple", "peach", "pear"]
# for k in fruits:
#     print (k)
#     print((k) + " for love")
# print(fruits)

# for numberr in range (1,21, 3 ):
#     print (numberr)

# total = 0
# for number in range (1, 101):
# #    total += number
# # print(total)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input ("type encode of decode \n")
# text = input("type the word \n")
# shift = int(input("type your shift number \n"))
#
# def ceaser (original_text, shifted_number, encode_or_decode):
#
#     output_text = ""
#     for letter in original_text:
#         if encode_or_decode == "decode":
#             shifted_number *= -1
#
#         shifted_position = alphabet.index(letter) + shifted_number
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print (f"here is your {encode_or_decode}d result {output_text}")
# ceaser (original_text = text, shifted_number = shift, encode_or_decode = direction)



# programming_dictionary = {
#     "bug": "an error in a program that prevents the program from running as expected",
#     "function": "a piece of code that you can easily call over and over again",
#
# }
#
# #print (programming_dictionary["bug"])
# programming_dictionary["loop"] = "the action of doing something over and over again"
# programming_dictionary["bug"] = "a moth in your computer"
# # programming_dictionary = {}
#
# for key in programming_dictionary:
#     print (key)
#     print(programming_dictionary[key])

# captital = {
#     "france": "paris",
#     "germany": "berlin",
# }
#
# travel_log = {
#     "france": ["paris", "lille", "dijon"],
#     "germany": ["stuttgart", "berlin"],
# }
# print(travel_log["france"][1])

# nested_list = ["a", "b", ["c", "d"]]
# print (nested_list[2][2])

# travel_log = {
#     "france": {
#         "cities_visited": ["paris", "lille", "dijon"],
#         "total_visits": 12,
#     },
#     "germany": {
#         "cities_visited": ["berlin", "hamburg", "stuttgart"],
#         "total_visits": 5,
#     },
# }
# print(travel_log["germany"]["cities_visited"][2])




# usage

# def find_highest_bidder(bidding_dictionary):
#     winner = ""
#     highest_bid = 0
#
#     max(bidding_dictionary)
#
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#
#     print(f"The winner is {winner} with a bid of ${highest_bid}.")
#
#
# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 20)


# import random
#
# def deal_card():
#     cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
#     card = random.choice(cards)
#     return card
#
# def calculate_score(cards):
#     if sum(cards) == 21 and len (cards) == 2:
#         return 0
#
#     if 11 in cards and sum(cards) > 21:
#         cards.remove (11)
#         cards.append(1)
#
#     return sum (cards)
#
# def compare (u_score, c_score):
#     if u_score == c_score:
#         return "draw"
#     elif c_score == 0:
#         return "lose, opponent has blackjack"
#     elif u_score == 0:
#         return "win with a blackjack"
#     elif u_score > 21:
#         return "you went over. you lose"
#     elif c_score > 21:
#         return "opponent went over. you win"
#     elif u_score > c_score:
#         return "you win"
#     else:
#         return "you lose"
#
# def play_game():
#
#     user_cards = []
#     computer_cards = []
#     computer_score = -1
#     is_game_over = False
#
#     for _ in range (2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#
#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print (f"your cards: {user_cards}, current score: {user_score}")
#         print (f"computer's first card: {computer_cards[0]}")
#
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input ("type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True
#
#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)
#
#     print (f"your final hand: {user_cards}, final score: {user_score}")
#     print (f"computer's final hand: {computer_cards}, final score: {computer_score}")
#     print (compare(user_score, computer_score))
#
# while input ("do you want to play a game of blackjack? type 'y' or 'n': ") == "y":
#     print ("\n" * 20)
#     play_game()

# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print (f"enemies inside function: {enemies}")
#
# increase_enemies()
# print (f"enemies outside function {enemies}")




# def drink_portion():
#     portion_strength = 2
#     print (portion_strength)
#
# drink_portion()
# print (portion_strength)
#
# player_health = 10
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print (player_health)
#         print (f"the potion strength {potion_strength}")
#
#     drink_potion()
#
# game()
#
#
# #print (player_health)
# #drink_portion()
#
# game()
#     drink_potion()

#print (potion_strength)


# game_level = 3
# enemies = ["skeleton", "zombie", "alien"]
#
# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print (new_enemy)
# create_enemy()




# enemies = 1
#
# def increase_enemies(enemy):
#     print (f"enemies inside function: {enemies}")
#     return enemy + 1
#
# enemies = increase_enemies(enemies)
# print (f"enemies outside function {enemies}")






# from random import randint
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
# def check_answer (user_guess, actual_answer, turns):
#     if user_guess > actual_answer:
#         print ("too high")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print ("too low")
#         return turns -1
#     else:
#         print (f"you got it! the answer was {actual_answer}")
#
#Testing
#
# def set_difficult():
#     level = input ("choose a difficulty. type easy or hard: ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
#
# def game():
#     print ("welcome to the number guessing game")
#     print ("i am thinking of a number between 1 and 100")
#     answer = randint (1,100)
# #    print (f"psst, the correct answer is {answer}")
#
#     turns = set_difficult()
#
#     guess = 0
#     while guess != answer:
#         print (f"you have {turns} attempts remaining to guess the number")
#         guess = int(input("make a guess: "))
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print ("you have run out guess, you lose")
#             return
#         elif guess != answer:
#             print ("guess again")

#game()


# def my_function ():
#     for i in range (1, 21):
#         if i == 20:
#             print ("you got it")
#
# my_function()

# from random import randint
# dice_images = ['1', '2', '3', '4', '5', '6']
# dice_num = randint (0, 5)
# print (dice_images[dice_num])

# year = int(input("what is your year of birth "))
#
# if year > 1980 and year < 1994:
#     print ("you are a millennial")
# elif year >= 1994:
#     print ("you are a gen Z")

# try:
#     age = int(input ("how old are you "))
# except ValueError:
#     print ("you have type in an invalid input please try again")
#     age = int(input("how old are you "))
#
#
# if age > 18:
#     print ("you can drive at age {age}")

# import random
# import maths
#
# def add (n1, n2):
#     return n1 + n2
#
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint (1, 3)
#         new_item = maths.add(new_item, item)
#     b_list.append(new_item)
#     print(b_list)
#
# mutate ([1,2,3,5,8,13])
#-----------------------------


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


# from nnnn import data
# import random
#
# def format_data(account):
#     """takes the account data and returns the printable format"""
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account ["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}"
#
#
# def check_answer(user_guess, a_followers, b_followers):
#     """take a user guess and the follower counts and return if they got it right"""
#     if a_followers > b_followers:
#         return user_guess == "a"
#     else:
#         return user_guess == "b"
#
# #print (logo)
# score = 0
# game_should_continue = True
# account_b = random.choice(data)
#
# # make the game repeatable
# while game_should_continue:
#     #generate a random account from the gama data
#
#     # making account at position B become the next account at position A
#     account_a = account_b
#     account_b = random.choice(data)
#
#     if account_a == account_b:
#         account_b = random.choice(data)
#
#     print (f"compare A: {format_data(account_a)}.")
#     print ("vs")
#     print (f"against B: {format_data(account_b)}.")
#
#
#     #ask user for a guess
#     guess = input ("who has more followers? type 'A' or 'B' : ").lower()
#
#     #clear the screen
#     print ("\n" * 20)
#     #print (logo)
#
#     #check if user is correct
#     #get follower count of each account
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#     # give user feedback on their guess
#     # score keeping
#
#     if is_correct:
#         score += 1
#         print (f"you are right current score {score}")
#     else:
#         print (f"sorry that wrong final score {score}.")
#         game_should_continue = False

#------------------------

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resource = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# def is_resource_sufficient(order_ingredients):
#     """return true when order can be made, false if ingredient are insufficient"""
#     for item in order_ingredients:
#         if order_ingredients[item] >= resource[item]:
#             print(f"sorry there is not enough {item}.")
#             return False
#     return True
#
# def process_coins():
#     """return the total calculated from coins inserted"""
#     print ("please insert coins.")
#     total = int (input ("how many quarters? ")) * 0.25
#     total += int(input("how many dimes? ")) * 0.1
#     total += int(input("how many nickles? ")) * 0.05
#     total += int(input("how many pennies? ")) * 0.01
#     return total
#
# def is_transaction_successful(money_received, drink_cost):
#     """return true when the payment is accepted, of false if money is insufficient"""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print (f"here is ${change} in change")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print ("sorry that's not enough money. money refunded ")
#         return False
#
# def make_coffee(drink_name, order_ingredients):
#     """deduct the required ingredient from the resources"""
#     for item in order_ingredients:
#         resource[item] -= order_ingredients[item]
#     print (f"here is your {drink_name} ")
#
# is_on = True
#
# while is_on:
#     choice = input ("what would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"water: {resource['water']}ml")
#         print(f"milk: {resource['milk']}ml")
#         print(f"coffee: {resource['coffee']}g")
#         print(f"money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
#


#------------------------------------------

#import nnnn
#print (nnnn.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print (timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(200)
#
# my_screen = Screen()
# print (my_screen.canvheight)
# my_screen.exitonclick()

#__________________________________________
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column ("pokemon Name", ["Pikachu","Squirtle","Charmander"])
# table.add_column("Type",["Electric","Water","Fire"])
# table.add_column("class",["math", "english", "science",])
#
# table.align = "l"
# print (table)

#-------------------------------------------------------
# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
# money_machine = MoneyMachine()
# money_machine.report()

#---------------------------------------------------------

# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "angela")
# user_2 = User("002", "jack")
#
# user_1.follow(user_2)
# print (user_1.followers)
# print (user_1.following)
# print (user_2.followers)
# print (user_2.following)

#--------------------------------------------------
# this and the next are the same

# - data module
# question_data = [
#     {"text": "yemi is boy", "answer": "True"},
#     {"text": "helen is boy", "answer": "False"},
#     {"text": "laptop use internet", "answer": "True"}
# ]
#
# # - question_model module
# class Question:
#     def __init__(self, q_text, q_answer):
#         self.text = q_text
#         self.answer = q_answer
#
# # - quizbrain module
# class QuizBrain:
#     def __init__(self, q_list):
#         self.question_number = 0
#         self.question_list = q_list
#         self.score = 0
#
#     def still_has_questions(self):
#         return self.question_number < len(self.question_list)
#
#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
#         self.check_answer(user_answer, current_question.answer)
#
#     def check_answer(self, user_answer, correct_answer):
#         if user_answer.lower() == correct_answer.lower():
#             self.score += 1
#             print("You got it right")
#         else:
#             print("That's wrong")
#         print(f"The correct answer was {correct_answer}")
#         print(f"Your current score is {self.score}/{self.question_number}\n")
#
#
# # - main module
# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
#
# while quiz.still_has_questions():
#     quiz.next_question()
#
# print("You have completed the Quiz")
# print(f"Your final score was {quiz.score}/{len(quiz.question_list)}")


#----------------------------------------------
# this and the one above are the same. this one is just broken down

# question_data = [{"text": "yemi is boy", "answer": "True"},
#                  {"text": "helen is boy", "answer": "False"},
#                  {"text": "laptop use internet", "answer": "True"}]
# #data tab
#
# #question_model tab
#
# class Question:
#
#     def __init__(self, q_text, q_answer):
#         self.text = q_text
#         self.answer = q_answer
# #question_model tab
#
# #main tab
#
# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
#
# while quiz.still_has_questions():
#     quiz.next_question()
#
# print ("you have completed the Quiz")
# print (f"your final score was {quiz.score}/{quiz.question_answer}")
#
# #main tab
#
#
#
# #quizbrain tab
#
# class QuizBrain:
#
#     def __init__(self, q_list):
#         self.question_number = 0
#         self.question_list = q_list
#         self.score = 0
#
#     def still_has_questions(self):
#         return self.question_number < len(self.question_list)
#
#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         user_answer = input (f"Q.{self.question_number}: {current_question.text} (True/False): ")
#         self.check_answer(user_answer, current_question.answer)
#
#     def check_answer(self, user_answer, correct_answer):
#         if user_answer.lower() == correct_answer.lower():
#             self.score += 1
#             print ("you got it right")
#         else:
#             print("that's wrong")
#         print(f"The correct answer was {correct_answer}")
#         print (f"your current score is {self.score}/{self.question_number}")
#         print ("\n")

#------------------------------------------------------------
# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
# tim = Turtle()

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range (4):
#     tim.forward(100)
#     tim.left(90)


# for _ in range (15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# screen = Screen()
# screen.exitonclick()

############################
# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
# tim = Turtle()

# colours = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white", "cyan", "magenta", "gold", "navy", "lime", "turquoise", "violet", "salmon", "coral", "teal"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward (100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# screen = Screen()
# screen.exitonclick()

############################

# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
# tim = Turtle()

# colours = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white", "cyan", "magenta", "gold", "navy", "lime", "turquoise", "violet", "salmon", "coral", "teal"]
# directions = [0, 90, 180, 270]
# tim.pensize (15)
# tim.speed("fastest")
#
# for _ in range (200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# screen = Screen()
# screen.exitonclick()

############################

# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
# tim = Turtle()
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# directions = [0, 90, 180, 270]
# tim.pensize (15)
# tim.speed("fastest")
#
# for _ in range (200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# screen = Screen()
# screen.exitonclick()

#-----------------------------------------------

# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
# tim = Turtle()
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# tim.speed("fastest")
#
# def draw_spirograph(size_of_gap):
#     for _ in range (int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle (100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)
#
# screen = Screen()
# screen.exitonclick()


#-------------------------------------------------

# import turtle
# from turtle import Turtle, Screen
# import random
#
# turtle.colormode(255)
# tim = Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
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
# number_of_dots = 90
#
# for dot_count in range (1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading (90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
# screen = Screen()
# screen.exitonclick()

#--------------------------------------------------
# import turtle
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# #clear()
#
# screen.exitonclick()


#--------------------------------------------

# import turtle
# from turtle import Turtle, Screen
# import random
# is_race_on = False
#
# screen = Screen()
# screen.setup(500,400)
# user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_position = [-70, -40, -10, 20, 50, 80]
# all_turtles = []
#
# for turtle_index in range (0, 6):
#     new_turtle = Turtle(shape ="turtle")
#     new_turtle.color(colors[turtle_index])
#     new_turtle.penup()
#     new_turtle.goto(x = -230, y = y_position[turtle_index])
#     all_turtles.append(new_turtle)
#
#
#
# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                   print (f"you have won! the {winning_color} turtle is the winner")
#             else:
#                 print(f"you have lost! the {winning_color} turtle is the winner")
#
#
#         rand_distance = random.randint(0, 10)
#         turtle.forward(rand_distance)
#
# screen.exitonclick()

#----------day 19---------------------------
#-----------day 20-------------------------
#-----------day 21-------------------------

# """below will be on a tab called food"""
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
#
#
#
# """below will be on a tab called snake"""
# from turtle import Turtle
#
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0
#
# class Snake:
#
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head = self.segments[0]
#
#     def create_snake(self):
#         for position in STARTING_POSITIONS:
#             self.add_segment(position)
#
#
#     def add_segment(self, position):
#         new_segment = Turtle("square")
#         new_segment.color("white")
#         new_segment.penup()
#         new_segment.goto(position)
#         self.segments.append(new_segment)
#
#     def extend(self):
#         self.add_segment(self.segments[-1].position())
#
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1):
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)
#
#     def up(self):
#         if self.head.heading() != DOWN:
#             self.head.setheading(UP)
#
#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)
#
#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.head.setheading(LEFT)
#
#     def right(self):
#         if self.head.heading() != LEFT:
#             self.head.setheading(RIGHT)
#
#
#
# """below will be on a tab called board"""
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
#
#
# """below stays at the main prod"""
# import turtle
# from turtle import Turtle, Screen
# from snake import Snake
# from food import Food
# from board import Scoreboard
#
# import time
#
#
# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer (0)
#
# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()
#
# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#
#     #detect collision with food
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()
#
#     #detect collision with wall
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         scoreboard.game_over()
#
#     #detect collision with body
#     for segment in snake.segments[1:]:
#        if snake.head.distance (segment) < 10:
#             game_is_on = False
#             scoreboard.game_over()
#
#
# screen.exitonclick()



#-----------day 21-------------------------
#-----------day 22-------------------------

from  turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey (r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey (l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
        ball.bounce_x()

    #detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

aaaaa



screen.exitonclick()
