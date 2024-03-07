""" 
Exception - eventhough a statement is syntactically correct it might give error when executed 

"""

x = 5
if x < 0:
    raise Exception('x should be more than 0') # Exception: x should be more than 0

y = 5
assert (y >= 0), 'y in not greater than or equal to 0' # AssertionError

# a = 5/0 ZeroDivisionError: division by zero

# handling Error via try, except blocks so that program doesn't terminates
try:
    a = 5/1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('No exception')
finally:
    print('Runs always')

# define own excpetions from Exception class
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small',x)
    print(x)
    
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)