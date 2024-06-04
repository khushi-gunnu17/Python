table_num = int(input("Enter the number : "))

for i in range(1, 11) :
    if i == 5 : continue
    print(table_num, "x", i, "=", table_num*i)
