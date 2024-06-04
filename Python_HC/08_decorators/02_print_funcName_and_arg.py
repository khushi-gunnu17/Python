
def debug(func) :
    def Wrapper(*args, **kwargs) :

        args_value = ', '.join(str(arg) for arg in args) or "Nothing"  # gives iterable list
        kwargs_value = ', '.join( f"{k} : {v}" for k, v in kwargs.items() ) or "Nothing"

        print(f"calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return Wrapper

@debug
def hello() :
    print("Hello")

hello()

@debug
def greet(name, greeting = "Hello") :
    print(f"{greeting}, {name}")

greet("khushi")

