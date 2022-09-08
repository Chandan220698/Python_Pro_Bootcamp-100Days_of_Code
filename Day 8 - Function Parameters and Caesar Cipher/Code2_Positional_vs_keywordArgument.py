# @Author: Chandan Kumar: https://github.com/Chandan220698/

def greet_with(name, location):
    print("\nHello", name)
    print("What is it like in", location)

greet_with("Chandan", "New Delhi")  # Positional argument -> so name = Chandan, location = New Delhi

greet_with(location="New Delhi", name="CK") # Keyword argument