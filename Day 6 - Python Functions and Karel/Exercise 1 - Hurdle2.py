# Problem:
# Complete the below challange:

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Click on Reeborg's Keyboard to check existing functions

# Solution:
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
i = 6
while i > 0:
    step()
    i = i-1
'''
