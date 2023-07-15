# Errors and Exceptions


x = 5

# if x < 0:
#     raise Exception('x should be positive')

assert (x >=0 ), 'x is not positive'

try:
    a = 5 / 1
    b = a + 3
except Exception as error:
    print(error)
else: 
    print("Everything is fine")
finally:
    print("Cleaning Up") 

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)

# test_value(200)

try: 
    test_value(1)
except ValueTooHighError as error:
    print(error)
except ValueTooSmallError as error:
    print(error)