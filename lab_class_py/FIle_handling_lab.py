# f = open('text.txt', "w")

# text = '''
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# '''

# f.write(text)

# f = open('text.txt', "rt")

# print(f.read())

# f.close()











# f1 = open("tables.java", "w")

# n = int(input("Enter the number : "))

# for i in range(1, 11) :
#     result = str(n * i)
#     f1.write(result + "\n")
#     f1.write("\n")

# f1.close()













# f2 = open("all_tables.txt", "w")

# for i in range(1, 11) :
#     for j in range(1, 11) :
#         result = str(i*j)
#         f2.write(result + "\n")
#     f2.write("\n")    















# f3 = open("tables.txt", "a")

# for i in range(1, 11) :
#     for j in range(1, 11) :
#         result = str(i*j)
#         f3.write(result + "\n")
#     f3.write("\n")  















# f4 = open("all_tables.txt", "rt")

# print(f4.read())


# print("all_tables.txt")















# read count of words from a file


# f5 = open("text.txt", "rt")

# text = f5.read()

# words = text.split()

# print(len(words))













# read count of characters from a file

# f6 = open("text.txt", "rt")

# text = f6.read()

# l = list(text)

# print(len(l))














# count capital letters in a file 

import re 

f7 = open("text.txt", "rt")

text = f7.read()

count = 0

# for i in text :
#     if i >= 'A' and i <= 'Z' :
#         count += 1


# print(count)

x = re.findall("[A-Z]", text)

print(len(x))