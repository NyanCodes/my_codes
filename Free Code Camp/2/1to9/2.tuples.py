# Tuple: ordered, immutable, allows duplicate element

import timeit

myTuple = ('Nyan', 18, 'San Francisco')
# print(myTuple)

item = myTuple[0]
# print(item)

a = (1, 2, 3, 4, 5)

b = a[::-1]
# print(b)

my_Tuple = (0, 1, 2, 3, 4, 5)

i1, *i2, i3 = my_Tuple

# print(i1)
# print(i2)
# print(i3)
# print(i4)

myTestList = [0, 1, 2, 'hello', True]
myTestTuple = (0, 1, 2, 'hello', True)

# print(sys.getsizeof(myTestList), 'bytes')   # 120
# print(sys.getsizeof(myTestTuple), 'bytes')  # 80

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) # 0.09s
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) # 0.01s





