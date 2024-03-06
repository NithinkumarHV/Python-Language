# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate
from itertools import groupby
import operator

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
b = [5]
prod = product(a,b)
print(list(prod)) # cartesian product

perm = permutations(a, 2)
print(list(perm))

comb = combinations(a,2)
print(list(comb))

acc = accumulate(a)
print(list(acc))

accmul = accumulate(a, func=operator.mul)
print(list(accmul))

group = groupby(a, key=smaller_than_3)
# group = groupby(a, key=lambda x:x<3)
for key, value in group:
    print(key, list(value))

obj = [{'name':"tom","age":1},{'name':"jerry","age":2},{'name':"t","age":4},{'name':"j","age":4}]
group_obj = groupby(obj, key=lambda x:x['age'])
for key, value in group_obj:
    print(key, list(value))