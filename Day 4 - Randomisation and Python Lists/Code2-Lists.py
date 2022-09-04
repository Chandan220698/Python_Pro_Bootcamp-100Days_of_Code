# @Author: Chandan Kumar: https://github.com/Chandan220698/

# https://docs.python.org/3/tutorial/datastructures.html

fruits = ["Apple", "Orange", "Grapes"]
print(fruits)

# Fetch first fruit:
print(fruits[0])

# Fetch last fruit:
print(fruits[-1])

# Updating element at index 1:
fruits[1] = "Banana"

print("Updated List:", fruits)

# Insert new item at end of list:
fruits.append("Orange")
print("Updated List:", fruits)

# Adding multiple items to end of list:
fruits.extend(['Watermelon', 'Kiwi', 'Pineapple'])
print("Updated List:", fruits)

## Nested List:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])