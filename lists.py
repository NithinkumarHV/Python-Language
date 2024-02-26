# Lists: ordered, mutable, allows duplicate elements
myList = ["banana","cherry", "apple"]
print(myList)

#duplicates / multiple datatypes
myList1 = [5, True, "apple", "apple"]
print(myList1)

item = myList[0]
print(item)

# last item = -1, last but second = -2
lastItem = myList[-1]
print(lastItem)

# looping
for i in myList:
    print(i)

# check if exists
if "lemon" in myList:
    print("yes")
else:
    print("No")

# append
myList.append("lemon")
print(myList)

# add at particular index
myList.insert(1,"berry")
print(myList)

# remove from last
print(myList.pop())
print(myList)

# remove a particular entry
myList.remove("cherry")
print(myList)

# sorted() - new list, reverse()
newList = sorted(myList)
print(newList, myList)

# sort same list
myList.sort()
print(myList)

# multiple same entries
newList1 = [0] * 5
print(newList1)

newList2 = [1,2,3]
concat = newList1 + newList2
print(concat)

print(len(myList))

slicing = [1,2,3,4,5,6,7,8,9,10]

a = slicing[1:5]
print(a) # exclude last index 1 to 4

b = slicing[:5] # 0 to 4
print(b)

c = slicing[::2] # step parameter
print(c)

lists = ["banana","cherry"]
lists_cpy = lists # shallow copy

lists_copy = lists.copy() # deep copy - independent
# lists[:] or list(lists)

lists_cpy.append("lemon") # modifies both posts and lists_cpy since it is shallow copy 

num = [1,2,3,4,5,6]
squares = [i*i for i in num]
print(squares)

print(lists_cpy, lists, lists_copy)

myList.clear()
print(myList)
