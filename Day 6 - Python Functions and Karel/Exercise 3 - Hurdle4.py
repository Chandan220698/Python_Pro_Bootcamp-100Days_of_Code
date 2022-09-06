# Problem:
# Complete the below challange:

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# Click on WORLD INFO and Reeborg's Keyboard to check existing functions

# Solution:

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# front_is_clear() or wall_in_front(), at_goal(),
# and their negation.

while at_goal() != True:
    if front_is_clear() != True:
        step()
    else:
        move()
    
    
'''