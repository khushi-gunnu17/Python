number = int(input("Enter the number : "))

fact = 1

while number > 0 :
    fact *= number
    number -= 1

print("The factorial of the number is : ", fact) 