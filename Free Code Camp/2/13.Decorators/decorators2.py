from unittest import result


def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('End')
    return wrapper

@start_end_decorator
def add_5(x):
    return x + 5

result = add_5(5)
print(result)