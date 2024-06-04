# Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args) :

    print(*args)
    print(args)

    # can do loops on args instead of pre - defined sum function
    # sum = 0
    # for i in args :
    #     sum += i
    # return sum
        
    return sum(args)

print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5))