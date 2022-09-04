# Problem:

'''
You are going to write a program that will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names.
For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

When you run the code, just use a random number as the seed. e.g. 67346
It doesn't matter what you chose, it's only for our testing code to check your work.

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
'''

# Solution:

import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
index = random.randint(0, len(names)-1)

print(f"{names[index]} is going to buy the meal today!")