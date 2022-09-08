# Problem:

'''
Instructions
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.
'''

# Solution:

#Write your code below this line 👇

def prime_checker(number):
    isPrime = True
    for i in range(2, number):
        if number%i==0:
            isPrime = False
    
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# Alternate optimise solution
#Write your code below this line 👇

def prime_checker(number):
    isPrime = True
    i = 2
    while(i*i < number):
        i += 1
        if number%i == 0:
            isPrime = False
            break
    
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
