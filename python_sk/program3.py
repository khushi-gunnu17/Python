age = 1

if age >= 18:
    print("You are an adult")
    print("You can vote !")
elif age < 18 and age > 3 :
    print("You are in school")
else : 
    print("You are child")

print("thank you !")


first = input("Enter first number : ")
operator = input("Enter an operator : ")
second = input("Enter second number : ")

first = int(first)
second = int(second)

if operator == '+' :
    print(first + second)
elif operator == '-' :
    print(first - second)
elif operator == '/' :
    print(first / second)
elif operator == '*' :
    print(first * second)
elif operator == '%' :
    print(first % second)
else : 
    print("Invalid operator .")