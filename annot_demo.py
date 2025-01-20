def decorator_tell_me(func):
    def wrapper(arg1, arg2):
        print("That's code before main function!")
        func(arg1, arg2)
        print("That's code after main function!")
    return wrapper



@decorator_tell_me
def print_sum(a, b):
    print(a + b)


print_sum(2, 3)


