##### @Author: Chandan Kumar: https://github.com/Chandan220698/

### Day 12: Beginner - Scope and Number Guessing Game
Learnings: <b>Namespaces-Local vs Global<b>.<br>
project 12: Number Guessing Game

### Code1: Namespaces - Global vs Local Scope

eg:
```
enemies = 1                 # Global Scope

def increase_enemies():
    enemies = 2             # Local Scope
    print(f"enemies inside the function: {enemies}")

increase_enemies()
print(f"enemies outside the function: {enemies}")
```