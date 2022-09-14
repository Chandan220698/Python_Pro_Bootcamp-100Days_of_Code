# @Author: Chandan Kumar: https://github.com/Chandan220698/

# Modifying Global Scope
enemies = 1                 # Global Scope

def increase_enemies():
    global enemies          # This will take the global enemies variable
    enemies += 1            # Local Scope
    print(f"enemies inside the function: {enemies}")

increase_enemies()
print(f"enemies outside the function: {enemies}")



