# lambda arguments: expresion 
#   - creates a function with arguements evaluates expression and returns the result

from functools import reduce

add10 = lambda x: x+10
print(add10(5))

mult = lambda x,y: x*y
print(mult(2,3))

points2D = [(1,2),(15,1),(5,-1),(10,4)]
sortByX = sorted(points2D)
sortByY = sorted(points2D, key=lambda x:x[1])
sortBySum = sorted(points2D, key=lambda x:x[0] + x[1])

print(points2D)
print(sortByX)
print(sortByY)
print(sortBySum)

# map(func, seq)
a = [1,2,3,4,5,6,7]
b = map(lambda x:x*2, a)
print(list(b))

# filter
c = filter(lambda x: x%2 == 0, a)
print(list(c))

# reduce(func, seq, initialValue)
e = reduce(lambda x,y: x*y, a, 1)
print(e)