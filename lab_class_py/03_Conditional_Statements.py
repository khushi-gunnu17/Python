# 01.) Write a program to check whether an entered year is leap or not. 

year = int(input("Enter the year : "))

if (year % 4 == 0  and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year.")
else :
    print("Not a leap year.")

print()






# 02.) Write a program to find largest among 3 numbers. 

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

if a > b and a > c :
    print(a, "is the largest number.")
elif b > c :
    print(b, "is the largest number.")
else :
    print(c, "is the largest number.")

print()






# 03.) Write a Program to check if the entered number is even or odd. 

number = int(input("Enter a number : "))

if number % 2 == 0 : 
    print("The number is even.")
else :
    print("The number is odd.")

print()






# 04.) Write a program to check if the number is prime or not ?

num = int(input("Enter the number : "))

flag = False 

if num == 1 :
    print(num, "is not a prime number.")
elif num > 1 :
    for i in range(2, num) :
        if (num % i) == 0 :
            flag = True
            break
        
if flag :
    print(num, "is not a prime number.")
else :
    print(num, "is a prime number")







# 05.) Let us say a teacher decided to give grades to her students as follows: 
# a) Mark greater than or equal to 80: Excellent 
# b) Mark greater than or equal to 65 but less than 80: Good 
# c) Mark greater than or equal to 50 but less than 65: Pass 
# d) Mark less than 50: Fail 
# Write a program in python to print a grade according to a student's mark with multiple if statements
    
marks = int(input("Enter the marks : "))

if marks >= 80 :
    print("Excellent")
elif marks >= 65 and marks < 80 :
    print("Good")
elif marks >= 50 and marks < 65 : 
    print("Pass")
else :
    print("Fail")