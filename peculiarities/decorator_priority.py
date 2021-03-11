# Using two decorators.

def my_decorator_1(f):
    print("Decorator 1.")
    return f

def my_decorator_2(f):
    print("Decorator 2.")
    return f

@my_decorator_1
@my_decorator_2
def my_function():
    print("My function!")

my_function()
