# namespaces

username = "Khushi-gunnu"

def func() :
    username = "Khushi"
    print(username)

print(username)

func()





# x = 99

# def func2(y) :
#     z = x + y
#     return z

# result = func2(1)
# print(result)







# x = 99

# def func3() :
#     # we should not overwrite global values like this
#     global x
#     x = 12

# func3()
# print(x)





# x = 99

# def f1() :
#     x = 88
#     def f2() :
#         print(x)
#     f2()
# f1()






# x = 99

# def f1() :
#     x = 88
#     def f2() :
#         print(x)
#     # In return, we are sending the whole definition of f2
#     return f2

# result = f1()
# result()        # lexical closure 

# A closure is a function bundled together with references to its surrounding state (the lexical environment) where it was defined. This means that a closure captures the variables in its enclosing scope (i.e., the scope where the function was defined), allowing the function to access those variables even if it is called outside of that scope.









# factory functions/ closure - mostly used in django
# def coder(num) :
#     def actual_func(x) :
#         return x ** num
#     return actual_func

# f = coder(2)
# g = coder(3)

# print(f(3))
# print(g(3))