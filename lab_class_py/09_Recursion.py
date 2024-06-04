# 01.) Write a python program to find factorial of a number using Recursion.

def factorial(n) :
    if n == 1 :
        return 1
    
    fact = n * factorial(n - 1)
    return fact

n = int(input("Enter the number : "))
print("The factorial is :", factorial(n))

print()







# 02.) Write a Program to print Fibonacci series up to n terms using recursion

def fibonacci(n) :
    if n <= 1 :
        return n
    else :
        return (fibonacci(n - 1) + fibonacci(n - 2))
    
    
nTerms = int(input("Enter a positive integer : "))

if nTerms <= 0 : 
    print("Please enter a positive integer.")
else :
    print("Fibonacci Sequence.")
    for i in range(nTerms) :
        print(fibonacci(i))

print()








# 03.) Write a program that reads values from the user until a blank line is entered. Display the total of all of the values entered by the user (or 0.0 if the first value entered is a blank line). Complete this task using recursion. Your program may not use any loops

def values_sum() :
    value_str = input("Enter a value : ")

    if value_str == '' :
        return 0.0
    
    value = float(value_str)

    # recursive case
    return value + values_sum()


total_sum = values_sum()

print("Total sum of all the values entered : ", total_sum)