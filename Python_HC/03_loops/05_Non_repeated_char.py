# Find the first non-repeated char

str = input("Enter the string : ")

for char in str : 
    if str.count(char) == 1 :
        print("Char is : ", char)
        break