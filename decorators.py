# Function decorators and class decorators
import functools

print("FUNCTION DECORATORS:")
print("----DECORATORS WITHOUT ARGUMENTS----")
def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator # does the same thing as "printName = start_end_decorator(printName)"
def printName(x):
    print('Nithin')
    return x + 5

# printName = start_end_decorator(printName)

res = printName(10)
print(res)

# decorators with arguments
print("----DECORATORS WITH ARGUMENTS----")
def repeat(num_times):
    def decorator_repeat(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times = 3)
def greet(name):
    print(f"Hello {name}")

greet('Nithin')

print("CLASS DECORATORS:")
class CountCalls:

    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is run {self.num_calls} times')
        return self.func(*args, **kwargs)

    
@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()