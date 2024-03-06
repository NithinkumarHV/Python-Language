# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a = "aaaabbbbccc"
my_counter = Counter(a)
print(my_counter) # Counter({'a': 4, 'b': 4, 'c': 3})
print(my_counter.most_common(1)) # [('a', 4)]
print(my_counter.most_common(1)[0]) # ('a', 4)
print(list(my_counter.elements()))

Point = namedtuple('Point','x,y')
p1 = Point(1,-4)
print(p1) # Point(x=1, y=-4)
print(p1.x, p1.y)

ordered_dict = OrderedDict()
ordered_dict['b'] = 1
ordered_dict['a'] = 2
print(ordered_dict)

default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict, default_dict['a'], default_dict['z'])

d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.extend([4,5,6])
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
d.clear()
print(d)
