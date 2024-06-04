
# 01.) Write a python program to find factorial of a number 

num = int(input("Enter a Number to find out its factorial : "))
fact = 1

for i in range(1, num + 1) :
    fact *= i

print("The factorial of the number is : ", fact)

print()






# 02.) Write a python program that prints prime numbers less than 20. 

num = int(input("Enter the number upto which prime numbers has to be printed : "))

prime_num = []

for number in range (2, num + 1) :
    flag = False
    for j in range(2, number) :
        if (number % j) == 0 :
            flag = True
            break
    if flag == False :    
        prime_num.append(number)

print("Prime Numbers less than : ", num, ":", prime_num)

print()






# 03.) Write a Program to print multiplication table of any number 

n = int(input("Print the Table of : "))

for i in range(1, 11) :
    print(n ,"*", i, "=", n * i )

print()







# 04.) Write a Program to check whether a number is palindrome or not 

num = int(input("Enter a Number to check whether it is palindrome or not : "))
x = num

reverse = 0
while num != 0 :
    digit = num % 10
    reverse = (reverse * 10) + digit
    num = num // 10

print(reverse)

if reverse == x :
    print("The number is a palindrome.")
else :
    print("The number is not a palindrome.")

print()






# 05.) Write a Program to construct the following pattern using nested for loop: 
'''
    * 
    ** 
    *** 
    **** 
    ***** 
    ***** 
    **** 
    *** 
    ** 
    * 
'''

n = int(input("Enter the number : "))

for i in range(1, n+1) :
    for j in range(1, i + 1) :
        print("*", end = ' ')
    print()

for i in range(n+1, 1, -1) :
    for j in range(i, 1, -1) :
        print("*", end = ' ')
    print()

print()
    




# 06.) Write a Program to print Fibonacci series up to n terms using loop statement

n = int(input("Enter the number upto which fibonacci sequence has to be printed : "))

n1 = 0
n2 = 1

print(n1, n2, end = ' ')

for i in range(n - 2) : 
    n3 = n1 + n2 
    print(n3, end = ' ')
    n1 = n2 
    n2 = n3

print()






# 07.) Write a Program to check if the entered number is Armstrong or not

number = int(input("Enter the number : "))
check_num = number

cube_sum = 0

while number != 0 :
    digit = number % 10
    cube_sum = cube_sum + digit ** 3 
    number = number // 10

if check_num == cube_sum :
    print("It is an armstrong number.")
else :
    print("It is not an armstrong number.")