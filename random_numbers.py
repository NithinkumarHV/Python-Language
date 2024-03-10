import random # pseudo random numbers
import secrets # true random numbers
import numpy as np


array = np.random.rand(3,3)
print(array)

array_int = np.random.randint(0,10,(3,4)) # 3X4 matrix with 0 <= number < 10
print(array_int)

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))


a1 = secrets.randbelow(10)
print(a1)

a2 = secrets.randbits(4)
# max is 1111 => 0 - 15
print(a2)

myList = list("ABCDEF")

b1 = secrets.choice(myList)
print(b1)

a = random.random()
print(a)

b = random.uniform(1,10)
print(b)

c = random.randint(1,10)
print(c)

# normal variation
d = random.normalvariate(0,1)
print(d)

print(myList)

choice = random.choice(myList)
print(choice)

multichoice1 = random.sample(myList,3)
print(multichoice1)

# duplicate entry allowed
multichoice2 = random.choices(myList,k=3)
print(multichoice2)

random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1,10))