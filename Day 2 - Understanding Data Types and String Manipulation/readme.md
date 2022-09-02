## Day 2: Beginner - Understanding Data Types and How to Manipulate Strings
Learnings: <b>Data Types & Converstions, Numbers, Operations, and f-strings<b>.<br>
project 2: Tip Calculator

### Code1: Python Primitive Data Types
These are the most primitive or the basic data structures. They are the building blocks for data manipulation and contain pure, simple values of a data. Python has four primitive variable types:
- Integers
- Float
- Strings
- Boolean


#### Some useful things:
` len(12345) # This will throw data type error `

` "2134"  # This is string not numbers `

` len("123+456")  # This will length of string i.e. 7 `

### Code2: Typer Error, Type Checking and Type Converstion
Type checking
` type(123)  # int type`

Type converstion:
` str(12345) # Now its str type`

` len(12345) # This will throw data type error `
> Note: Type converstion must be compatible int("string") -> Error: Not compatible converstion

### Code3: f-string: String formatting
```
val1 = 10
val2 = "Hello"

print(f"Integer value is {val1} and String value is {val2}")
```