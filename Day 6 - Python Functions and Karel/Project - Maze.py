# Problem:
# Complete the below challange:

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Click on Reeborg's Keyboard to check existing functions

# Solution:
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear(): # To make sure robot touch/near to a wall
    move()

while at_goal() != True:    # Follow right side and move along right side till goal position
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''