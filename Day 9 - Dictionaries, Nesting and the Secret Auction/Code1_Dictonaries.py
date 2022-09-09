# @Author: Chandan Kumar: https://github.com/Chandan220698/

programming_dict = {
    "bug": "An error in some cases",
    "function": "A piece of code that can be reused",
    "loop": "Action of doing something over and over again"
}

print("\n", programming_dict)

# Dictionary is identified by keys
print(programming_dict["loop"])

# Adding new items to dictionary if key is not present else update the value to corresponding key
programming_dict["object"] = "An intance of the class"

print("\n", programming_dict, "\n")

# Loop throught dictionary
for thing in programming_dict:
    print(thing)                        # Just printing keys
    print(programming_dict[thing])      # Value corresponding to the key

for k,v in programming_dict.items():
    print(k, ":", v)                         # Print both key and value
