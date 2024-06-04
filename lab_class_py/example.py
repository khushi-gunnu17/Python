str = input("Enter the string : ")


count_dict = {item : str.count(item) for item in str}

print(count_dict)

print()