# @Author: Chandan Kumar: https://github.com/Chandan220698/

## IF-ELSE

print("Welcome to the rollercoster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("Enjoy your ride")
else:
    print("Sorry! Cant ride")

## Nested IF-ELSE Statement

if height > 120:
    print("Enjoy your ride!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Need to pay $5.")
    elif age <= 18:
        print("Need to pay $7.")
    else:
        print("Need to pay $12.")
else:
    print("Sorry! Cant ride")