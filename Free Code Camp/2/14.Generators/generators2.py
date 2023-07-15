import imp


import sys

def fibonacci(limit):

    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
# for i in fib:
#     print(i)

# generator expression
mygenerator = (i for i in range(100000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(100000) if i % 2 == 0]
print(sys.getsizeof(mylist))    