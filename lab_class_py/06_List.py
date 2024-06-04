# 01.) Write a Program to demonstrate various list operations in python.
fruits = ['apple', 'banana', 'kiwi', 'watermelon', 'mango']

fruits.append('orange')

print("After appending : ", fruits)

copy_list = fruits.copy()

print("After copying : ", copy_list)

count_fruit = fruits.count("orange")

print("counting the number of oranges : ", count_fruit)

one_seed_fruits = ['lychees', 'plums', 'dates', 'cherries']
fruits.extend(one_seed_fruits)

print("After extending : ", fruits)

fruits.insert(1, 'jackfruit')

print("After inserting : ", fruits)

fruits.reverse()

print("After reversing : ", fruits)

fruits.clear()

print("After clearing the entire list : ", fruits)

print()






# 02.) Write a Program to find even numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_numbers = []

for i in numbers :
    if (i % 2) == 0 :
        even_numbers.append(i)

print("The even numbers are : ")
print(even_numbers)


print()





# 03.) Write a Program to interchange first and last elements of a list.

random_num = [12, 23, 43, 56, 47, 28]
n = len(random_num)

print("before interchanging : ", random_num)

first = random_num[0]
last = random_num[n - 1]

random_num[0] = last
random_num[n - 1] = first

print("After interchanging : ")
print(random_num)

print()





# 04.) Write a Program to turn every item of a list into its square.

nums = [1, 2, 3, 4, 5, 6]

square_list = [ x**2 for x in nums ]

print(square_list)

print()





# 05.) Write a Program to check all elements are unique or not in python.

fruit_list = ['apple', 'banana', 'kiwi', 'watermelon', 'mango']

flag = False
for i in fruit_list:
    if fruit_list.count(i) > 1 :
        flag = True
    
if flag == True :
    print("The list is not unique.")
else :
    print("The list is unique.")


print()





# 06.) Write a Program to replace list's item with new value if found.

og_list = [2, 3, 1, 4, 2, 5, 6, 4, 8, 6, 5, 9]
print("Original List : ", og_list)
old_value = int(input("Enter any old value from the given original list : "))
new_value = int(input("Enter the value which you want to replace old one with it. : "))

modified_list = [new_value if item == old_value else item for item in og_list]
print("Modified List : ", modified_list)

print()






# 07.) Write a Program to find the position of minimum and maximum elements of a list.

num_list = [56, 34, 90, 87, 12, 14, 45, 24, 98]

x = num_list.index(max(num_list))
print("The max number's index is : ", x)

y = num_list.index(min(num_list))
print("The min number's index is : ", y)

print()






# 08.) Write a Program to find the cumulative sum of elements of a list.

nums = [1, 2, 3, 4, 5, 6, 7]
sum = 0

for i in nums :
    sum += i

print("The cumulative sum of the number list is : ", sum)


print()





# 09.) Write a program that reads integers from the user and stores them in a list. Your program should continue reading values until the user enters 0. Then it should display all of the values entered by the user (except for the 0) in order from smallest to largest, with one value appearing on each line. 

list = []

while True :
    x = int(input("Enter the integer value : "))

    if x == 0 :
        break

    list.append(x) 

list.sort()

print("The values are : ")

for i in list :
    print(i)


print()





# 10.) Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read your program should display them (except for the 0) in reverse order
    

myList = []

while True :
    x = int(input("Enter the integer value : "))

    if x == 0 :
        break

    myList.append(x) 

print("The original input list : ", myList)
myList.reverse()

print("The values in the reverse order are : ")

for i in myList :
    print(i)