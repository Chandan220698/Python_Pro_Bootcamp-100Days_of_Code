# @Author: Chandan Kumar: https://github.com/Chandan220698/

############DEBUGGING#####################

# Code 1
# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# Solution 1: change range to range(1, 21)


# Code 2
# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Solution: List index out of range error occurs sometimes as randint giving 6 but list range is till 5.
# Change randint to randin(0,5)

# Code 3
# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# Solution: for 1994 code will not work. So change year > 1994 to year >= 1994


# Code 4
# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# Solution: 1. Indentation error. 2. Typecast the input to int()


# Code 5
# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# Solution: "word_per_page == int(input("Number of words per page: ")) there is a conditional check it should be assignment"


# Code 6
# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
# Solution: Indent b_list.append(new_item) inside for loop