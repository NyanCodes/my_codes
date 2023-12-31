# Lambda arguments

from functools import reduce


add10 = lambda x : x + 10
print(add10(8))

mult = lambda x, y : x * y 
print(mult(9, 19))

points2D = [(1, 2), (15, 1), (5, -1), (10, 3)]
points2D_sorted = sorted(points2D, key = lambda x : x[1])

# print(points2D)
# print(points2D_sorted)

# map (Function, Sequence)
a = [1, 2, 3, 4, 5]
b = map(lambda x : x * 2, a)
# print(list(b))

c = [x * 2 for x in a]
# print(c)

d = filter(lambda x : x % 2 == 0, a)
# print(list(d)) 

product_a = reduce(lambda x, y : x * y, a)
print(product_a)
