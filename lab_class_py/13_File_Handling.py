
# 1. Write a Program to count number of words in a file

f = open("text.txt", "rt")

text = f.read()

words = text.split()

print("Number of words in the file : ", len(words))



print()









# 2. Write a Program to find out longest word from a file

import re

f1 = open('text.txt', 'rt')

text = f1.read()

words = re.findall(r'\w+', text)

longest_word = max(words, key = len)

print(f"The longest word in the file is '{longest_word}' with length = {len(longest_word)}.")



print()










# 3. Write a Program to count total number of uppercase and lowercase characters in file

import re

f2 = open("text.txt", 'rt')

text = f2.read()

# upper_case_count = 0
# lower_case_count = 0

# for char in text :
#     if char.isupper() :
#         upper_case_count += 1
#     elif char.islower() :
#         lower_case_count += 1

upper_case_characters = re.findall("[A-Z]", text)
lower_case_characters = re.findall("[a-z]", text)

print("The upper case count is : ", len(upper_case_characters))
print("The lower case count is : ", len(lower_case_characters))

print()










# 4. Write a Program to read all the contents of CSV file and display only specific columns

import csv
with open('kh.csv', newline='') as csvfile:
  data = csv.DictReader(csvfile)
  print("ID Department Name")
  print("---------------------------------")
  for row in data:
    print(row['department_id'], row['department_name'])


print()











# 5. Write a Program to write python list to CSV file and display the contents

import csv
data = [[10,'a1', 1], [12,'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
with open("temp.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerows(data)
with open('temp.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ')
 for row in data:
   print(', '.join(row))
