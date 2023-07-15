# Collections : Counter, namedtuple, OrderedDict, DefaultDict, deque

from ast import Or
from collections import Counter
import imp
from pprint import pprint

a = 'aaabbbbccccc'
myCounter = Counter(a)

print(list(myCounter.elements())) 
print(myCounter.keys())
print(myCounter.most_common(2)[0][0]) # Most common element...

from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt) 

from collections import OrderedDict

orderedDict = OrderedDict() 
orderedDict['a'] = 2
orderedDict['b'] = 3
orderedDict['c'] = 4

print(orderedDict)

from collections import defaultdict
d = defaultdict(float)
d['a'] = 1
d['b'] = 'hi'
print(d)

from collections import deque

deque = deque()

deque.append(1)
deque.append(2)
deque.appendleft(3)
print(deque)
deque.pop()
print(deque)

