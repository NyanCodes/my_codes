# Sets : Unordered, Mutable, No Duplicates

from re import S


SetA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
SetB = {10, 11, 12}

# SetA.symmetric_difference_update(SetB)

print(SetB.issuperset(SetA))
print(SetB.isdisjoint(SetA))
print(SetA)

a = frozenset([1, 2, 3, 4, 5]) # this is immutable

myList = ['apple', 'banana', 'cherry']
x = frozenset(myList)

