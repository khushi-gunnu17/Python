# 1. Write a Program to illustrate handling of divide by zero exception

def divide_numbers(x, y) :
    try :
        result = x/y
        print(f"The result of {x}/{y} is : {result}")
    except ArithmeticError :
        print("Cannot divide by zero in this example !")


divide_numbers(20, 4)
divide_numbers(12, 0)


print()





# 2. Write a Program to illustrate handling of IndexError Exception

my_list = [1, 2, 3, 4, 5]
index = int(input("Enter the index : "))

try :
    value = my_list[index]
    print(f"Value at index {index} is : {value}")
except IndexError :
    print(f"Index {index} is out of the range for the list")


print()





# 3. Write a Program to illustrate handling of ValueError Exception

value = input("Enter any value : ")

try :
    num = int(value)
    print("the converted integer value is : ", num)
except ValueError :
    print(f"{value} is not a valid integer !")

print()





# 4. Write a Program to illustrate handling of Type exception

num_list = [10, 20, 30, 40, '50']

try :
    avg = sum(num_list) / len(num_list)
    print(avg)
except TypeError :
    print("Provide a list of numbers, Invalid data type !")