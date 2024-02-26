# Tuples: ordered, immutable, allows duplicate elements
import sys
import timeit

mytuple = ("Max",21,"Boston")

mytuple1 = tuple(["Max",21, "Boston"])
print(mytuple, mytuple1)

item = mytuple[0]
print(item)

for i in mytuple:
    print(i)

if "Tim" in mytuple:
    print("yes")
else:
    print("No")

my_tuple = ('a','b','c','p','p')
print(len(my_tuple))

print(my_tuple.count('p'))
print(my_tuple.index('p'))
# print(my_tuple.index('o'))

mylist = list(my_tuple)
print(mylist)

tuples = tuple(mylist)
print(tuples)

# list size > tuple size
print(sys.getsizeof(mylist),"bytes")
print(sys.getsizeof(tuples), "bytes")

# creation = list time > tuple time
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))


a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5] # 2 - 4, excludes last index
c = a[:5]
ab = a[1::2]
print(b,c,ab)

# unpack
name, age, city = mytuple
print(name, age, city)

i1, *i2, i3 = a
print(i1)
print(i2)
print(i3)