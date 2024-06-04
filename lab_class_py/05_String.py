# Strings 

# 01.) Write a program to create, concatenate and print a string and accessing sub-string from a given string. 

x = "Hello"
y = "World"

str = x + " " + y
print("the concatenated string is : ", str)

sub_string = str[6:]
print("The substring is :", sub_string)

print()





# 02.) Write a program find length of a string. 

string = input("Enter a string : ")
print("The length of the string is :", len(string))

print()






# 03.) Write a Program to check whether a string is palindrome or not. 

myStr = input("Enter the string : ")
reverse_str = ''

for char in myStr :
    reverse_str = char + reverse_str
    
if myStr == reverse_str :
    print("It's a Palindrome")
else :
    print("It's not a Palindrome.")

print()
    





# 04.) Write a Program to count all letters, digits, and special symbols from a given string. 

line_of_string = input("Enter the string : ")

letters_count = 0
digits_count = 0
special_symb = 0

for i in line_of_string :
    if i.isalpha() :
        letters_count += 1
    elif i.isdigit() :
        digits_count += 1
    else :
        special_symb += 1

print("The count of :")
print("Letters : ", letters_count)
print("Digits : ", digits_count)
print("Special Symbols : ", special_symb)

print()





# 05.) Write a Program to calculate the sum and average of the digits present in your registration number.

reg_number = input("Enter your Registration Number : ")
count = 0
sum = 0

for i in reg_number :
    if i.isdigit() :
        count += 1
        sum += int(i)

avg = sum / count
print("The sum of the digits : ", sum)
print("The avg of the digits : ", avg)