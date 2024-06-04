# 01.) Write a program to demonstrate different number data types in Python. 

a = 5
b = 17.5
c = 10j + 5

print("a is the type of : ", type(a))
print("b is the type of : ", type(b))
print("c is the type of : ", type(c))

print()






# 02.) Write a program to perform different Arithmetic Operations on numbers in Python. 

x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))

print("Addition of x and y : ", x + y)
print("Subtraction of x and y : ", x - y)
print("Multiplication of x and y : ", x * y)
print("Division of x and y : ", x / y)
print("Remainder of x and y : ", x % y)
print("Exponent of x and y : ", x ** y)
print("Float Division of x and y : ", x // y)

print()







# 03.) Program to create random number generator which generate random number between 1 and 6 

import random
print("Random Number between 1 and 6 : ", random.randint(1, 6))

print()







# 04.) Program to swap two number and display number before swapping and after swapping 

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
print("Before swapping the two numbers : ", x, y)
x, y = y, x
print("After swapping the two numbers : ", x, y)

print()






# 05.) Write a program in python, that calculates the volume of a sphere with radius r entered by the user. (Assume π = 3.14)

r = int(input("Enter the radius of the sphere : "))
pi = 3.14
vol = (4 / 3) * pi * r ** 3
print("The volume of the sphere is : ", vol)