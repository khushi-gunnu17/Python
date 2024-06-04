# 1. Write a Program to write user defined function to swap two numbers and display number before swapping and after swapping

def swap(a, b) :
    print("Numbers before being swapped , a :", a ,"and b :", b)
    a, b = b, a
    print("Numbers after being swapped , a :", a ,"and b :", b)

swap(4, 5)

print()







# 2. Write a Program to calculate arithmetic operation on two number using user defined function

def arithmetic_functions(a, b) :
    sum = a + b 
    print("Addition is : ", sum)

    sub = a - b   
    print("Subtraction is : ", sub)

    mul = a * b
    print("Multiplication is : ", mul)

    div = a//b
    print("Division is : ", div)

    rem = a % b
    print("Remainder is : ", rem)


x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
arithmetic_functions(x, y)

print()








# 3. Write a Program to Calculate diameter and area of circle using user defined function

def circle_parameters(r) :
    diameter = 2 * r
    print("Diameter of the circle is : ", diameter)

    area = 3.14 * r ** 2
    print("The area of the circle is : ", area)


radius = int(input("Enter the radius : "))
circle_parameters(radius)

print()








# 4. Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median.

def median(a, b, c) :
    values = [a, b, c]
    values.sort()
    return values[1]

def main() :
    val1 = int(input("Enter the first value : "))
    val2 = int(input("Enter the second value : "))
    val3 = int(input("Enter the third value : "))

    result = median(val1, val2, val3)

    print("The median value is : ", result)

if __name__ == '__main__' :
    main()

print()








# 5. Write a function that generates a random password. The password should have a random length of between 7 and 10 characters. Each character should be randomly selected from positions 33 to 126 in the ASCII table. Your function will not take any parameters. It will return the randomly generated password as its only result.

import random

def random_password_gen() :
    string = ''
    length = random.randint(7, 10)

    for i in range(length) :
        string += chr(random.randint(33, 126))
    
    return string


password = random_password_gen()
print("The randomly generated password is : ", password)

print()







# 6. Write a Program to filter even values from list using lambda function

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = lambda x : x % 2 == 0

filtered_list = [x for x in myList if even(x)]

print(filtered_list)

print()








# 7. Write a Program to find the sum of elements of a list using lambda function

num_list = [1, 2, 3, 4, 5, 6, 7, 8]

total_sum = lambda list_sum : sum(x for x in list_sum)

print("The sum is : ", total_sum(num_list))

print()








# 8. Write a Program to find small number between two numbers using Lambda function

small_num = lambda x, y : x if x < y else y

first_val = int(input("Enter the first number : "))
second_val = int(input("Enter the second number : "))

print("The smaller number is : ", small_num(first_val, second_val))