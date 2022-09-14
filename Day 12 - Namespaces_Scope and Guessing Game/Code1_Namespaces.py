# @Author: Chandan Kumar: https://github.com/Chandan220698/

enemies = 1                 # Global Scope

def increase_enemies():
    enemies = 2             # Local Scope
    print(f"enemies inside the function: {enemies}")

increase_enemies()
print(f"enemies outside the function: {enemies}")



