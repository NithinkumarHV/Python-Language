# strings: ordered, immutable, text representation
my_string = """Hello
world"""

my_string1 = """Hello\
world"""


print(my_string)
print(my_string1)

char = my_string[0]

# my_string[0] = 'i' ERROR !!
print(char)

substring = my_string[1:5] # 1,2,3,4
substring1 = my_string[::2] # every second character
reverse = my_string[::-1]

print(substring, reverse)

variable = "Hello"
name = "tom"
sentence = variable + " " + name
print(sentence)

for i in variable:
    print(i)

if 'e' in name:
    print("yes")
else:
    print("No")

var1 = '    Some data   '
var1 = var1.strip()
print(var1, var1.upper(), var1.lower())
print(var1.startswith('Some'))
print(var1.find('o'))
print(var1.count('e'))
print(var1.replace('data','info'))

# convert to list
my_list = my_string.split() # ["Hello","world"], by default delimiter is space

# list to string
string = ':'.join(my_list)
print(my_list, string)

lists = ['a'] * 6
print(lists)
strings = ''.join(lists)
print(strings)

# %
var = 'Tom'
var1 = "jerry"
string_1 = "the variable is %s" % var

# .format()
string_2 = "the variable is {} and {}".format(var, var1)
print(string_1)
print(string_2)

# f-Strings
string_3 = f"the variable is {var}"
print(string_3)