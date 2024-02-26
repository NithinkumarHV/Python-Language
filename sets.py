# Sets: unordered, mutable, no duplicates

mySet = {1,2,3,1}
print(mySet)

mySet1 = set([1,2,3])
print(mySet1)

mySet2 = set("Hello")
print(mySet2)

mySet3 = set()
print(mySet3)

mySet3.add(1)
mySet3.add(2)
mySet3.add(3)

mySet3.remove(3)
# mySet3.remove(10)  Error !

mySet3.discard(10)
print(mySet3.pop())

print(mySet3)

for i in mySet:
    print(i)

if i in mySet:
    print("Yes")

# union and intersection
    
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

union = odds.union(evens)
print(union)

intersection = odds.intersection(primes)
print(intersection)

# difference
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

# present in A but not in B
diff = setA.difference(setB)
print(diff)

# present in both A and B, but not intersection elements
diff1 = setA.symmetric_difference(setB)
print(diff1)

# updates setA
setA.update(setB)
print(setA)

# intersection update
setA.intersection_update(setB)
print(setA)

# difference update
setA.difference_update(setB)
print(setA)

set1 = {1,2,3,4,5,6}
set2 = {1,2,3,4,5}

print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))

# shallow copy - reference
set_cpy = set1
setCopy = set1.copy()
set_cpy.add(7)
print(set_cpy,set1)

print(setCopy)

const = frozenset([1,2,3,4,5,6])
print(const)