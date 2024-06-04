# Part - A  (Tuples)

# 01.) Write a program to demonstrate various tuple operations in python. 

fruits = ("apple", "mango", "banana", "lichi")
print("The Original tuple : ", fruits)

print("Length : ", len(fruits))

# tuple constructor
fruit_tuple = tuple(("watermelon", "cherry", "papaya"))
print(fruit_tuple)


# updating a tuple
x = list(fruits)
x.append("kiwi")
updated_tuple = tuple(x)
print("After updating the fruits tuple : ", updated_tuple)


# unpacking a tuple
green, red, yellow = fruit_tuple

print(green)
print(red)
print(yellow)

# joining tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# deleting a tuple
del fruits

print()





# 02.) Write a program to find the size of a tuple 

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Size of the tuple is : ", len(tup))

print()









# 03.) Write a program to find the maximum and minimum K elements in a tuple.

myTuple = (12, 34, 56, 23, 38, 65, 49, 20, 40)

print("The original tuple : ", myTuple)

k = int(input("Enter the value of k : "))

# first changing the tuple to list and then back, as tuple doesn't have a sort() method 
myList = list(myTuple)

myList.sort()

sorted_tuple = tuple(myList)

# Finding minimum k elements 
min_k = sorted_tuple[:k]

# Finding maximum k elements
max_k = sorted_tuple[-k:]

print("Minimum k elements of the tuple are : ", min_k)
print("Maximum k elements of the tuple are : ", max_k)

print()







# 04.) Write a program to create a list of tuples from given list having number and its cube in each tuple  

tup = (1, 2, 3, 4, 5)
# tup2 = (1, 8, 27, 64, 125)

tup_list = [(x, x**3) for x in tup]
print(tup_list)

# or
# tup_list = list(zip(tup, tup2))
# print(tup_list)

print()







# Part - B  (Dictionary)

# 01.) Write a program to demonstrate working with dictionaries in python 

myDict = {
    "apples" : 5, 
    "bananas" : 10,
    "oranges" : 7,
    "grapes" : 3
}

print("The original dictionary : ", myDict)

print("Length : ", len(myDict))

# accessing items
print("The number of apples are : ", myDict["apples"])

# adding in a dictionary
myDict["kiwi"] = 9
print("After addition : ", myDict)

# updating a dictionary
myDict["grapes"] = 8
print("After updation : ", myDict)

# removing an item
myDict.pop("apples")
print("After popping : ", myDict)

# looping in a dict 
for x, y in myDict.items():
    print(x, y)

# copying a dict
copied_dict = myDict.copy()
print("After copying : ", copied_dict)

print()
print()







# 02.) Write a Program to create a dictionary from a sequence.

sequence = [1, 2, 3, 4, 5]

dict = {item : item for item in sequence}

print('Dictionary from sequence : ', dict)

print()







# 03.) Write a Program to generate dictionary of numbers and their squares (i, i*i) from 1 to N 

N = int(input("Enter the number : "))

square_dict = {item : item**2 for item in range(N)}

print(square_dict)

print()







# 04.) Write a Program that determines and displays the number of unique characters in a string entered by the user. For example, “Hello, World!” has 10 unique characters while “zzz” has only one unique character. Use a dictionary to solve this problem. 

str = input("Enter the string : ")

count_dict = {item : str.count(item) for item in str}

print(count_dict)

print()







# 05.) Two words are anagrams if they contain all of the same letters, but in a different order. For example, “evil” and “live” are anagrams because each contains one ‘e’, one ‘I’, one ‘l’, and one ‘v’. Create a program that reads two strings from the user, determines whether or not they are anagrams, and reports the result.


str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

str1_dict = {item : str1.count(item) for item in str1}
str2_dict = {item : str2.count(item) for item in str2}

if str1_dict == str2_dict : 
    print("The two strings are anagrams.")
else :
    print("They are not anagrams.")