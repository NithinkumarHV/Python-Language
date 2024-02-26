# Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

print(mydict)

mydict2 = dict(name="Max",age=20,city="Boston")
print(mydict2)

value = mydict["name"]
print(value)

# mutable
mydict["email"] = "max@xyz.com"
print(mydict)

mydict["email"] = "coolmax@xyz.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

# removes last inserted element
mydict.popitem()
print(mydict)

if "name" in mydict2:
    print(mydict2["name"])
else:
    print("No")

try:
    print(mydict["name"])
except:
    print("Error")

for key,value in mydict2.items():
    print(key, value)

print(mydict2.keys())

# shallow copy
mydict2_cpy = mydict2
print(mydict2_cpy)

mydict2_cpy["email"] = "max@xyz.com"
print(mydict2_cpy, mydict2)

# deep copy - dict(mydict2)
mydict2Copy = mydict2.copy()
mydict2Copy.popitem()
print(mydict2Copy, mydict2)

dict1 = {"name":"Max", "age":20, "email":"max@xyz.com"}
dict2 = dict(name="Muller",age=10,city="Boston")

# override and merge
dict1.update(dict2)
print(dict1)

#any immutable types can be used as keys
dictionary = {3:9,6:36,9:81}
print(dictionary)

# value = dictionary[0] ERROR !

# dictionary[${key}]
value = dictionary[3]
print(value)

mytuple = (8,7)
d = {mytuple: 15}
print(d)
print(d[mytuple])