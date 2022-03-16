#How to create
dict1 = {}
dict1 = { "key":"value",
          "key1":"value1",
          "key2":"value2"}
print(type(dict1))

# Create a dictionary with dict()
# You can create a dictionary with dict().
#
# Use keyword arguments
# It can be specified with the keyword argument key=value.

d = dict(k1=1, k2=2, k3=3)
print(d)
    # {'k1': 1, 'k2': 2, 'k3': 3}



# With a list of keys and a list of values
# Using zip(), you can create a dictionary from a list of keys and a list of values. Not only lists but also tuples can be used.

keys = ['k1', 'k2', 'k3']
values = [1, 2, 3]

d = dict(zip(keys, values))
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}


#Create a dictionary with dictionary comprehensions
####################################################
Name = ["Abhi", "bobby", "spandana"]
dName = {i :len(i) for i in Name}
print(dName)

keys = ['k1', 'k2', 'k3']
values = [1, 2, 3]

d = {k:v for k,v in zip(keys,values)}
print(d)






dict1 = { "key":"value",
          "key1":"value1",
          "key2":"value2"}
print(dict1)
print(dict1.values())
print(dict1.keys())
print(dict1.get("key"))
print(dict1.get("key1"))
print(dict1["key"])
print(dict1["key1"])

print(dict1.items())



#print(dict1.pop("key1"))
#print(dict1)
#print(dict1.popitem())
#print(dict1)

for i in dict1:
    print(i)

for i in dict1.values():
    print(i)

for i in dict1.items():
    print(i)
    print(type(i))

    # ('key', 'value')
    # ('key1', 'value1')
    # ('key2', 'value2')
# How to add
# How to access
# How to delete
