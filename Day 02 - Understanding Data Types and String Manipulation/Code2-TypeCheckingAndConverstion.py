# @Author: Chandan Kumar

# len(1234)         -> Error
name = input("What is your name?")
#print("Length of your name is: " + len(name))   # Error can't concatenate str to int

# Type checking:
print(type(len(name)))

# Type converstion:
str(len(name))
print(type(str(len(name))))

print("Length of your name is: " + str(len(name))) 