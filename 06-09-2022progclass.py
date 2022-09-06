# def greeter(name):
#     print("Good Morning")
#     print("Hello " + str(name))

# print("Go")
# greeter("World") #Note how in the function caller you used a string, when working with strings, you can concantenate and wont invoke name error.

# Parameters are variable names used in function as a definition to refer to the arguments
# Arguments are the values we pass to the function in a particular function call

import math


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    return d

#If we put print inside the function, calling it will assign the d and print out directly when we call it
#If we didnt put print d and didnt return d, printing the function and its function call with give None
# this is why we need to use return d to make sure the result has a memory value stored 
print(distance(0, 0, 3, 4))
#So basically, if the function has no print(d), we don't need to put print(distance(...))
#If the function has return inside, you can put print(distance(x))