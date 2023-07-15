# itertools : product, permutations, combinations, accumulate
#             groupby and infinite iterators

from ast import operator
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
import operator

# product
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
# print(list(prod))

# permutations
c = [1, 2, 3]
permu = permutations(c, 2)
# print(list(permu))

# combinations
d = [1, 2, 3, 4]
comb = combinations(d, 2)
# print(list(comb))
comb_wr = combinations_with_replacement(d, 2)
# print(list(comb_wr))

# accumulate
acc2 = accumulate(d, func=operator.mul)
acc = accumulate(d, func=max)
# print(d)
# print(list(acc))
# print(list(acc2))

#groupby

group_obj = groupby(d, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

persons = [
    {'name' : 'Tim', 'age' : 25}, {'name' : 'Dan', 'age' : 25},  
    {'name' : 'Lisa', 'age' : 20}, {'name' : 'Clarie', 'age' : 28} 
]

group_obj2 = groupby(persons, key = lambda x : x['age'])
for key, value in group_obj2:
    print(key, list(value))

# There's also infinite iterators; count, cycle and repeat
# I'm so bored to code them